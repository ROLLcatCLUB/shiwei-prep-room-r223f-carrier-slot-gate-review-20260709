import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
checks = []


def check(name, cond, detail=""):
    checks.append({"name": name, "passed": bool(cond), "detail": detail})


def read_text(name):
    return (ROOT / name).read_text(encoding="utf-8")


model = json.loads(read_text("R223F_render_slot_state_model.json"))
texts = {
    "slot_mapping": read_text("R223F_carrier_slot_mapping.md"),
    "mode_switch": read_text("R223F_mode_switch_contract.md"),
    "collapse": read_text("R223F_collapse_expand_state_contract.md"),
    "binding": read_text("R223F_binding_preview_carrier_policy.md"),
    "bottom": read_text("R223F_bottom_input_local_note_policy.md"),
    "report": read_text("R223F_implementation_gate_report.md"),
    "readme": read_text("README_FOR_GPT_REVIEW.md"),
}

check("stage_id", model.get("stage_id") == "1013R_R223F_CARRIER_SLOT_MAPPING_AND_IMPLEMENTATION_GATE")
check("status_static_contract_only", model.get("status") == "static_carrier_slot_contract_only")

for key in [
    "formal_ui",
    "r97b_modified",
    "frontend_backend_modified",
    "runtime_enabled",
    "provider_model_prompt_db",
    "formal_apply",
    "real_component_interaction",
]:
    check(f"boundary false: {key}", model.get("boundary", {}).get(key) is False)

expected_slots = [
    "prep_workbench.mode_switch_slot",
    "prep_workbench.source_risk_slot",
    "prep_workbench.prep_canvas_slot",
    "prep_workbench.focused_section_slot",
    "prep_workbench.component_suggestion_slot",
    "prep_workbench.binding_preview_slot",
    "prep_workbench.quick_projection_slot",
    "prep_workbench.local_note_slot",
]
slot_ids = [slot.get("slot_id") for slot in model.get("slots", [])]
check("all expected slots present", all(slot in slot_ids for slot in expected_slots), str(slot_ids))
check("slot count exact", len(slot_ids) == len(expected_slots), str(len(slot_ids)))

slot_by_id = {slot.get("slot_id"): slot for slot in model.get("slots", [])}
component_slot = slot_by_id.get("prep_workbench.component_suggestion_slot", {})
check("daily component max 3", component_slot.get("density_limits", {}).get("daily_max") == 3)
check("quick component max 2", component_slot.get("density_limits", {}).get("quick_max") == 2)
check("component shelf blocked", "global_12_component_shelf" in component_slot.get("blocked_behaviors", []))
check("component marketplace blocked", "component_marketplace" in component_slot.get("blocked_behaviors", []))

binding_slot = slot_by_id.get("prep_workbench.binding_preview_slot", {})
check("binding selected only", binding_slot.get("open_policy") == "selected_component_only")
check("all component bindings blocked", "all_component_bindings_open" in binding_slot.get("blocked_behaviors", []))

bottom_slot = slot_by_id.get("prep_workbench.local_note_slot", {})
check("bottom local note scope", bottom_slot.get("input_scope") == "current_section_local_constraint_only")
check("bottom global chat blocked", "global_chat_composer" in bottom_slot.get("blocked_behaviors", []))
check("bottom whole rewrite blocked", "whole_lesson_regeneration" in bottom_slot.get("blocked_behaviors", []))
for phrase in ["问我任何问题", "继续聊天生成", "告诉小教你想怎么改整份教案"]:
    check(f"forbidden bottom phrase recorded: {phrase}", any(phrase in item for item in bottom_slot.get("forbidden_placeholders", [])))

source_slot = slot_by_id.get("prep_workbench.source_risk_slot", {})
check("source risk collapsed except high risk", source_slot.get("default_state") == "collapsed_except_high_risk")
check("high risk always visible", "high_risk_confirmation" in source_slot.get("always_visible", []))
check("ordinary gaps collapsed", "ordinary_material_gaps" in source_slot.get("collapsed_by_default", []))

canvas_slot = slot_by_id.get("prep_workbench.prep_canvas_slot", {})
check("prep canvas highest priority", canvas_slot.get("priority") == "highest")
check("focused section inside canvas", "focused_section_slot" in canvas_slot.get("contains", []))

transition_events = [item.get("event") for item in model.get("state_transitions", [])]
for event in ["mode_select_daily", "mode_select_quick", "component_focus", "teacher_resolves_high_risk"]:
    check(f"transition present: {event}", event in transition_events)

required_files = [
    "R223F_carrier_slot_mapping.md",
    "R223F_render_slot_state_model.json",
    "R223F_mode_switch_contract.md",
    "R223F_collapse_expand_state_contract.md",
    "R223F_binding_preview_carrier_policy.md",
    "R223F_bottom_input_local_note_policy.md",
    "R223F_implementation_gate_report.md",
    "README_FOR_GPT_REVIEW.md",
]
for name in required_files:
    check(f"file exists: {name}", (ROOT / name).exists())

combined = "\n".join(texts.values())
for required in [
    "R97B_modified=false",
    "formal_ui=false",
    "runtime_enabled=false",
    "provider_model_prompt_db=false",
    "formal_apply=false",
    "selected_component_only",
    "center canvas + collapsible side rails",
    "current section only",
    "no global component shelf",
    "no chat composer",
]:
    check(f"text includes: {required}", required in combined)

for forbidden in [
    "R223F authorizes formal UI",
    "provider call allowed",
    "model call allowed",
    "database persistence allowed",
    "formal apply allowed",
]:
    check(f"forbidden assertion absent: {forbidden}", forbidden not in combined)

ref_files = [
    "_REFERENCE_INPUTS/R223E/R223E_static_visual_mock_spec.md",
    "_REFERENCE_INPUTS/R223E/R223E_static_visual_mock_state.json",
    "_REFERENCE_INPUTS/R223E/R223E_screenshot_smoke_result.md",
    "_REFERENCE_INPUTS/R223D/R223D_default_collapse_expand_policy.json",
    "_REFERENCE_INPUTS/R223D/R223D_carrier_layout_options.md",
]
for rel in ref_files:
    check(f"reference exists: {rel}", (ROOT / rel).exists())

slot_mapping = texts["slot_mapping"]
table_slots = re.findall(r"`(prep_workbench\.[^`]+_slot)`", slot_mapping)
check("slot mapping names implementation slots", all(slot in table_slots for slot in expected_slots), str(table_slots))

result = {
    "passed": all(item["passed"] for item in checks),
    "check_count": len(checks),
    "failed": sum(1 for item in checks if not item["passed"]),
    "failed_checks": [item for item in checks if not item["passed"]],
}
(ROOT / "validate_1013R_R223F_carrier_slot_mapping_gate_result.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
print(json.dumps(result, ensure_ascii=False))
raise SystemExit(0 if result["passed"] else 1)

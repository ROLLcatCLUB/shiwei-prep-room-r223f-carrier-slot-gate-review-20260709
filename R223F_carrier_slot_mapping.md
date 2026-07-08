# R223F Carrier Slot Mapping

```text
stage_id=1013R_R223F_CARRIER_SLOT_MAPPING_AND_IMPLEMENTATION_GATE
status=static_carrier_slot_contract_only
formal_ui=false
R97B_modified=false
frontend_backend_modified=false
runtime_enabled=false
provider_model_prompt_db=false
formal_apply=false
```

## Purpose

R223F translates the approved R223E static visual mock into implementation-facing
carrier slot contracts. It does not create or modify UI. The goal is to make the
future minimum workbench explicit enough that a later canary cannot accidentally
become a chat surface, component shelf, or uncontrolled R97B rewrite.

## Slot Map

| Visual Region From R223E | Proposed Carrier Slot | Default State | Primary Responsibility | Implementation Gate |
| --- | --- | --- | --- | --- |
| 精备 / 日常 / 快速 mode rail | `prep_workbench.mode_switch_slot` | visible, compact | Select projection density without changing the underlying prep object | static canary allowed only with fixture modes |
| 左侧资料与风险 | `prep_workbench.source_risk_slot` | collapsed rail except high risk | Show high-risk confirmation, fold ordinary gaps and assumptions | no full evidence browser in canary |
| 中间备课主画布 | `prep_workbench.prep_canvas_slot` | open, widest | Keep lesson plan and focused teaching section as the main reading object | required for any future canary |
| 聚焦环节卡 | `prep_workbench.focused_section_slot` | open inside canvas | Show current teacher action, student action, material need, evidence bottom line | must remain embedded in prep canvas |
| 当前组件建议条 | `prep_workbench.component_suggestion_slot` | open below focused section | Recommend 1-3 components for current section only | no global component library shelf |
| 右侧绑定预览 | `prep_workbench.binding_preview_slot` | selected-component-only | Preview screen prompt, learning sheet, teacher language, evidence output | open only after component focus |
| 快速模式简链 | `prep_workbench.quick_projection_slot` | open only in quick mode | Preserve 3-minute readable minimum teaching chain | max 2 components |
| 底部局部补充输入 | `prep_workbench.local_note_slot` | compact, low weight | Add local material/class constraints for the current section | no chat composer wording or whole-lesson generation |

## Carrier Decision

R223F keeps the R223D/R223E direction:

```text
DEFAULT_CARRIER_PATTERN = center canvas + collapsible side rails
PRIMARY_READING_OBJECT = prep_workbench.prep_canvas_slot
COMPONENT_VISIBILITY = current_section_only
BINDING_VISIBILITY = selected_component_only
BOTTOM_INPUT_SCOPE = local_note_current_section_only
```

## R97B Position

R97B remains a future carrier reference. R223F may name required slots, but it
does not add routes, DOM nodes, CSS, JavaScript, backend endpoints, or runtime
state to R97B.

## Minimum Slot Extension Candidates

These are candidates for later gated canary work, not current implementation:

| Candidate | Why It May Be Needed | Current Status |
| --- | --- | --- |
| `prep_workbench.component_suggestion_slot` | R223E shows components must sit near the focused section, not in a global right rail | candidate_only |
| `prep_workbench.binding_preview_slot` | selected component needs downstream preview without exposing all bindings | candidate_only |
| `prep_workbench.local_note_slot` | teachers need local material/class constraints without chat takeover | candidate_only |
| `prep_workbench.source_risk_slot` | high-risk confirmations must stay visible while ordinary gaps fold | candidate_only |

No candidate slot is active in R223F.

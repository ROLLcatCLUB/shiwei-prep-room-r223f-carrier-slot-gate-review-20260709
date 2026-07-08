# R223F Collapse / Expand State Contract

## Default State

R223F preserves the R223D and R223E density decision:

```text
default_open =
  prep_canvas
  focused_section_card
  current_component_suggestion_strip

default_collapsed =
  ordinary_source_assumptions
  ordinary_material_gaps
  non_selected_component_bindings
  full_reasoning_chain

always_visible_until_resolved =
  high_risk_confirmation
  selected_mode
  focused_section_title
  evidence_bottom_line
```

## State Table

| Information Type | Default State | Opens When | Closes When | Guard |
| --- | --- | --- | --- | --- |
| High-risk confirmation | visible | default | teacher resolves or explicitly folds after acknowledgement | must not be hidden behind ordinary gaps |
| Ordinary source assumptions | folded | teacher opens source/gap rail | teacher returns to reading | must not dominate default view |
| Ordinary material gaps | folded | teacher opens source/gap rail | teacher returns to reading | distinguish from high-risk |
| Full reasoning chain | folded | future precision review action | teacher returns to daily/quick projection | no default reasoning dump |
| Focused section card | open | default | never hidden in daily/quick default | primary teaching unit |
| Current component strip | open | focused section has candidate components | component count is zero or teacher hides strip | current section only |
| Selected component binding | closed until focus | teacher focuses one component | teacher clears selection | selected component only |
| Non-selected component bindings | folded | never by default | always folded by default | no all-binding list |
| Bottom local note input | compact | default | never becomes primary composer | local section scope only |

## Implementation State Names

```json
{
  "source_risk_slot": "folded_except_high_risk",
  "prep_canvas_slot": "open_primary",
  "focused_section_slot": "open_embedded",
  "component_suggestion_slot": "open_current_section_only",
  "binding_preview_slot": "closed_until_component_focus",
  "local_note_slot": "compact_low_weight"
}
```

## Non-Negotiable Guards

1. Default view must not show full reasoning chain.
2. Default view must not show all component bindings.
3. Default view must not show ordinary gaps as equal weight to high-risk confirmation.
4. Component strip must not exceed 3 in daily or 2 in quick.
5. Bottom input must never use chat-style placeholder text.

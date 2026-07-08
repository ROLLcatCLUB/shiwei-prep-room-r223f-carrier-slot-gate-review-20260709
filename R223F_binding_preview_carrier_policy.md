# R223F Binding Preview Carrier Policy

## Role

The binding preview explains what a selected classroom component affects. It is
not a second lesson plan, a component editor, or a right-side tool marketplace.

## Carrier Policy

```text
slot_id = prep_workbench.binding_preview_slot
default_state = closed_until_component_focus
open_policy = selected_component_only
```

## Visible Binding Fields

| Field | Purpose | Default Visibility |
| --- | --- | --- |
| `screen_prompt` | short big-screen wording if the component needs display support | selected component only |
| `learning_sheet` | learning sheet row or evidence capture field | selected component only |
| `teacher_language` | classroom wording for using the component | selected component only |
| `assessment_evidence` | observable output or record created by the component | selected component only |
| `media_requirements` | image, video, student work, material, or object needed | selected component only |

## Allowed Future Canary

- Show one selected component binding preview from fixture data.
- Let a teacher choose focus among already visible component cards.
- Keep non-selected bindings folded.

## Blocked

- Showing all component bindings at once.
- Running a real classroom component.
- Writing to database or lesson body.
- Calling provider/model/runtime.
- Replacing R97B right rail without a later formal UI gate.

## Density Rule

If width is constrained, binding preview should degrade to:

```text
selected component inline summary
or
right drawer concept
```

It must not compress the prep canvas below readable width.

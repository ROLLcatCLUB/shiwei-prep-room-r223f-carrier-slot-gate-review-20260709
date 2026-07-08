# R223F Bottom Input Local Note Policy

## Role

The bottom input is a low-weight local note area. It exists so a teacher can add
constraints such as local materials, class conditions, or a D-option supplement
for the current section.

It is not a chat composer.

## Slot Contract

```text
slot_id = prep_workbench.local_note_slot
default_state = compact_low_weight
scope = current_section_only
visual_priority = lower_than_prep_canvas_and_component_strip
```

## Allowed Wording

```text
补充本环节材料限制...
添加本班情况说明...
给这个组件加一条本地要求...
```

## Forbidden Wording

```text
问我任何问题...
继续聊天生成...
告诉小教你想怎么改整份教案...
让 AI 重新生成完整教案...
```

## Allowed Future Canary

- Static fixture note input with no persistence.
- Local note shown as pending supplement to the focused section.
- D-option supplement captured as fixture-only state.

## Blocked

- Global chat entry.
- Whole-lesson rewrite instruction.
- Runtime prompt submission.
- Provider/model call.
- Database persistence.
- Formal apply into R97B or lesson body.

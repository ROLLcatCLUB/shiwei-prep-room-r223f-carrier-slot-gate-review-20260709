# R223D Visual Density Review

```text
stage_id=1013R_R223D_STATIC_VISUAL_DENSITY_AND_CARRIER_REVIEW
status=static_visual_density_review_only
ui_implementation=false
R97B_modified=false
formal_apply=false
```

## Review Question

Can the future minimum workbench remain readable inside an R97B-like carrier if it contains a mode rail, prep canvas, source/gap rail, component strip, binding preview, and bottom local note input?

## Density Decision

```text
R223D_DENSITY_DECISION = PASS_WITH_COLLAPSE_POLICY_REQUIRED
FORMAL_UI = STILL_BLOCKED
```

The structure is feasible only if the default view is restrained:

```text
open: prep canvas + focused section card + current component suggestion strip
folded: ordinary source assumptions + ordinary material gaps + non-selected component bindings + full reasoning chain
visible: selected mode + focused section title + evidence bottom line + high-risk confirmation
open on focus: selected component binding preview only
```

## Density Review By Region

| Region | Default State | Density Risk | R223D Decision |
| --- | --- | --- | --- |
| Mode rail | open, compact | low | keep visible; selected state clear but small |
| Source/gap rail | ordinary items folded | medium | only high-risk confirmation remains visible |
| Prep canvas | open and widest | medium | must remain dominant reading area |
| Component suggestion strip | open for focused section | medium | max 3 daily, max 2 quick; no global component shelf |
| Binding preview | closed until component focus | medium-high | selected component only; no all-component binding list |
| Bottom input | minimized local note | medium | visual weight lower than prep canvas; no chat prompt |

## Pass Conditions

1. Teacher can read the lesson plan without opening side panels.
2. Component suggestions do not cover or push away the focused section.
3. High-risk confirmation remains visible, but ordinary gaps do not dominate.
4. Binding preview is contextual and selected-component-only.
5. Quick mode remains readable within 3 minutes.

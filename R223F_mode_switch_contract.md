# R223F Mode Switch Contract

## Purpose

The mode switch maps one prep object into three teacher-facing projections. It
must not become three separate generation products or three unrelated routes.

```text
precision = full teacher-in-loop reasoning workbench
daily = tomorrow-ready classroom plan
quick = 3-minute readable minimum teaching chain
```

## Mode Responsibilities

| Mode | Primary Teacher Need | Default Visible Density | Component Limit | R223F Status |
| --- | --- | --- | --- | --- |
| 精备 `precision` | make key teaching decisions and inspect reasoning | decision cards and reasoning graph can be surfaced in later gated work | decided by future precision gate | contract_only |
| 日常 `daily` | organize tomorrow's classroom flow | prep canvas, focused section, current components, high-risk confirmation | max 3 per focused section | contract_only |
| 快速 `quick` | preserve minimum viable class in minutes | concise steps, evidence bottom line, essential components only | max 2 per focused section | contract_only |

## Switch Rules

1. The selected mode must be visible but compact.
2. Switching mode changes projection density, not the lesson identity.
3. Daily mode must preserve the R222C teacher-readable sample quality line.
4. Quick mode must remain 3-minute readable and cannot expand into daily detail by default.
5. Precision mode remains blocked for formal UI until a later gate reopens teacher decision interactions.
6. No mode switch may call provider/model/runtime in R223F or any static canary.

## Implementation Gate For Future Canary

Allowed later, only after this gate is accepted:

- fixture-driven static mode tabs;
- local in-memory switch between static daily and quick mock states;
- no data persistence;
- no model call;
- no R97B formal route binding.

Still blocked:

- formal R97B mode routing;
- runtime generation;
- prompt/provider/model calls;
- database-backed mode state;
- automatic rewrite of lesson body on switch.

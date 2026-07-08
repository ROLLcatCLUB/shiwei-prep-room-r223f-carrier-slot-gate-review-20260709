# R223D Carrier Layout Options

R223D compares static carrier options only. It does not choose or implement a real UI.

| Option | Structure | Strength | Risk | R223D Decision |
| --- | --- | --- | --- | --- |
| Option A. Three-column persistent layout | left source/gap rail + center prep canvas + right binding panel | clear separation of roles | may feel compressed in R97B carrier | not default; use only when width is enough |
| Option B. Center canvas + collapsible side rails | prep canvas dominant; source/gap and binding panels collapse | best balance of readability and power | needs clear collapsed affordances later | recommended static direction |
| Option C. Inline component expansion | component binding opens inside the section card | keeps eyes in teaching flow | section card may become too tall | useful for quick mode only |
| Option D. Right drawer on component focus | binding preview slides or opens from right conceptually | keeps default view light | drawer could cover right resources | candidate for future visual mock, not implementation |

## Recommendation

```text
DEFAULT_STATIC_DIRECTION = Option B
QUICK_MODE_VARIANT = Option C for one selected component
FUTURE_TEST = Option D as density-relief alternative
```

R97B remains a future carrier reference only. No file, route, component, CSS, or runtime changes are allowed in R223D.

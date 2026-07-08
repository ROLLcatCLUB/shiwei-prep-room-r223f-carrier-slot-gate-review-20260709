# R223E Screenshot Smoke Result

stage_id: `1013R_R223E_STATIC_VISUAL_MOCK_FIXTURE`

status: `PASS`

## Smoke Target

- URL: `http://127.0.0.1:8792/R223E_static_visual_mock_fixture.html`
- Screenshot: `R223E_static_visual_mock_screenshot.png`
- Result JSON: `R223E_screenshot_smoke_result.json`
- Viewport requested: `1440 x 1000`

## Verified Signals

| Check | Result |
| --- | --- |
| Static stage marker is `R223E` | PASS |
| Fixture is static mock only | PASS |
| R97B modified marker is false | PASS |
| Runtime marker is false | PASS |
| Default open includes prep canvas | PASS |
| Default open includes focused section card | PASS |
| Default open includes current component suggestion strip | PASS |
| Ordinary gaps and non-selected bindings are folded by default | PASS |
| High-risk confirmation remains visible | PASS |
| Daily mode component count is `3 / 3` | PASS |
| Quick mode component count is `2 / 2` | PASS |
| Binding preview is selected-component-only | PASS |
| Bottom input is local supplement, not chat | PASS |
| No global 12-component shelf marker | PASS |
| No chat placeholder marker | PASS |
| No forbidden chat prompt text found | PASS |
| No horizontal overflow in smoke viewport | PASS |

## Smoke Data

```json
{
  "passed": true,
  "dailyComponentCount": 3,
  "dailyMax": 3,
  "quickComponentCount": 2,
  "quickMax": 2,
  "highRiskVisible": true,
  "ordinaryGapsFolded": true,
  "selectedOnlyBinding": true,
  "bottomNonChat": true,
  "noGlobalComponentShelf": true,
  "noChatPlaceholder": true,
  "bodyScrollWidth": 1265,
  "bodyClientWidth": 1265,
  "screenshotBytes": 123456
}
```

## Boundary Note

This smoke check only validates the static visual mock fixture. It does not
modify R97B, frontend/backend code, provider/model/runtime, prompt, database, or
formal apply paths.

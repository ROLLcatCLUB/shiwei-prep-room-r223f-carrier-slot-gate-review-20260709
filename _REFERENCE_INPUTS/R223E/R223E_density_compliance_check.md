# R223E Density Compliance Check

| Requirement | Static Mock Evidence | Result |
| --- | --- | --- |
| 默认只打开备课主画布、聚焦环节卡、当前组件建议条 | `data-default-open` includes `prep_canvas focused_section_card current_component_suggestion_strip` | pass |
| 普通资料缺口折叠，高风险确认可见 | left rail marks ordinary gaps folded and high-risk card visible | pass |
| 右侧绑定预览只显示被选中组件 | binding panel has `data-open-policy=selected_component_only` and selected `material_mystery_box` | pass |
| 日常模式每环节最多 3 个组件 | component strip has 3 cards and `data-max-components-daily=3` | pass |
| 快速模式每环节最多 2 个组件 | quick block has 2 cards and `data-max-components-quick=2` | pass |
| 底部输入视觉权重低于备课主画布 | compact footer input; placeholder is local constraint only | pass |
| 快速模式保持 3 分钟可读 | quick panel shows 4 concise steps before details | pass |
| 组件建议不能遮挡主阅读 | strip sits below workbench region and does not overlay canvas | pass |
| 不出现 12 个组件按钮货架 | visible daily strip has 3 cards; quick strip has 2 cards | pass |
| 不出现聊天式输入主入口 | footer placeholder avoids chat wording | pass |

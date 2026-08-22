# kang-product-architect

[![status](https://img.shields.io/badge/status-public%20release-2ea44f)](https://github.com/KanG-ciyuan/kang-product-architect/releases)
[![version](https://img.shields.io/github/v/release/KanG-ciyuan/kang-product-architect?label=version)](https://github.com/KanG-ciyuan/kang-product-architect/releases)
[![tests](https://img.shields.io/badge/contract%20tests-3-2ea44f)](tests/)
[![license](https://img.shields.io/badge/license-MIT-6f42c1)](LICENSE)

Kang 的通用产品架构数字员工 Skill。适用于 SaaS、内部工具、工作流产品和数字服务，在开发前明确入口、角色、权限、模块、状态归属、交接和完成标准。

调用：`$kang-product-architect`

输入：产品目标、目标用户、核心任务、约束和现有证据。输出：带证据状态、判断理由、替代方案和验收标准的版本化产品契约。它不写代码，也不替产品负责人做最终取舍。

## 你可以直接这样说

“使用 `$kang-product-architect` 审查这个 CRM 的入口、角色权限、状态归属和模块边界，先只读并输出产品契约。”

## 安装与验证

```bash
npx skills add KanG-ciyuan/kang-product-architect
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/kang-product-architect
python3 ~/.codex/skills/kang-meta-skill/scripts/validate_skill.py ~/.codex/skills/kang-product-architect
```

## 前置条件

- [ ] 已准备产品目标、目标用户、核心任务和已知约束
- [ ] 已阅读只读权限边界
- [ ] 已确认实施前需要人工批准

## Troubleshooting

如果输入不足，它会输出有限审查并标记 `to_verify`，不会补造角色或战略。显式点名 `$kang-product-architect`，并指定输入、输出路径和本轮决策范围。

## License

MIT. See [LICENSE](LICENSE). This is a reusable product-development agent Skill, separate from any private enterprise product.

<!-- kang-author:start -->
## About Kang

Maintained by Kang. GitHub: https://github.com/KanG-ciyuan/

<!-- kang-author:end -->


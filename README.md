# kang-product-architect

[![status](https://img.shields.io/badge/status-public%20release-2ea44f)](https://github.com/KanG-ciyuan/kang-product-architect/releases)
[![version](https://img.shields.io/github/v/release/KanG-ciyuan/kang-product-architect?label=version)](https://github.com/KanG-ciyuan/kang-product-architect/releases)
[![tests](https://img.shields.io/badge/local%20tests-1%20passed-2ea44f)](tests/)
[![license](https://img.shields.io/badge/license-Kang%20terms-6f42c1)](LICENSE)

Kang 的企业 AI 流程诊断产品架构审查 Skill。用于在开发前明确官网、登录、角色权限、页面边界、主任务和完成标准。

调用：`$kang-product-architect`

输入：产品目标、角色模型、当前页面、领域模型和用户反馈。输出：带 `confirmed` / `inferred` / `to_verify` 标记的架构交接文档。它不写代码，也不替产品负责人做最终取舍。

## 你可以直接这样说

“使用 `$kang-product-architect` 审查这个 SaaS 的入口、角色权限和页面边界，先只读并输出交接文档。”

## 安装与验证

```bash
npx skills add KanG-ciyuan/kang-product-architect
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/kang-product-architect
python3 ~/.codex/skills/kang-meta-skill/scripts/validate_skill.py ~/.codex/skills/kang-product-architect
```

## 前置条件

- [ ] 已准备产品目标、角色模型和当前页面证据
- [ ] 已阅读只读权限边界
- [ ] 已确认实施前需要人工批准

## Troubleshooting

如果没有按岗位输出，显式点名 `$kang-product-architect`，并指定输入和输出路径。它不负责写代码或视觉实现。

## License

Copyright (c) Kang. See [LICENSE](LICENSE).

<!-- kang-author:start -->
## About Kang

Maintained by Kang. GitHub: https://github.com/KanG-ciyuan/

<!-- kang-author:end -->

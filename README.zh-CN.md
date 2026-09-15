# Kang Product Architect

[English](README.md) | 简体中文

[![Release](https://img.shields.io/github/v/release/KanG-ciyuan/kang-product-architect?display_name=tag&sort=semver&style=flat-square)](https://github.com/KanG-ciyuan/kang-product-architect/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/KanG-ciyuan/kang-product-architect?style=flat-square)](https://github.com/KanG-ciyuan/kang-product-architect/commits/main)

**在 AI 开始写代码之前，把模糊业务需求转化为可实施、可审查、可验收的产品契约。**

**定位：** 面向 AI 构建软件的产品契约架构角色（Product Contract Architect for AI-built Software） · **生态阶段：** DEFINE 定义

`kang-product-architect` 是给 AI agent 使用的只读产品架构决策角色。它把产品目标与已观察到的用户需求，收敛成一份最小且自洽的产品契约；当证据不足时，它拒绝补造角色、能力或战略。

整个包都是文字：`SKILL.md`（42 行）加 [`references/architecture-rubric.md`](references/architecture-rubric.md)（48 行）。没有可执行代码、没有脚本、没有模板、也没有运行时依赖——包自身声明 `"scripts": []`。适用领域是中性的：SaaS、内部工具、工作流产品和数字服务。

> **更快的实现速度不会自动解决需求模糊，反而可能更快地把错误理解变成完整产品。**

---

## 为什么要在 AI 动手写代码之前先做定义？

AI 不会在模糊的需求前面停下来。它会自己把模糊补掉——悄悄选定一个角色、一条权限规则、一个状态归属方，以及一套没人批准的“完成”定义。产物看起来是完整的，于是这些决定从来不会被当成决定来审查。

下游的一切都在继承这里定义过、或者在这里根本没被定义的结构。流程设计、体验审查、产品验收，都作用在一个已经默认了“某些角色存在、某些数据对他们可见、某些状态有人负责”的产品之上。

本项目要做的，就是在实现开始**之前**，把这些默认假设变成显式、可审查的书面契约，而不是聊天里的口头约定。

## 提示词驱动 vs 契约驱动

同一个需求，两种做法。

| | 提示词驱动 | 契约驱动 |
| --- | --- | --- |
| 需求存在哪里 | 聊天消息里 | 书面的契约产物 |
| 缺口谁来补 | 下一个写代码的人，隐式补掉 | 具名的人类负责人，显式决定；否则该项保持 `to_verify` |
| 证据 | 文字断言 | 每条 finding 都带 `evidence_status` 和 `source` |
| 替代方案 | 没有记录 | 至少比较一个更简单的方案及其取舍 |
| 模糊暴露的时机 | 代码写出来之后 | 实现之前，作为 `unresolved decisions` 暴露 |
| 完成 | “看起来做完了” | 每个 core job 对应一个可观察的完成信号 |
| 停止条件 | 没有 | 存在 `blocker`，或关键权限为 `to_verify`，即不满足可实施条件 |

这个 Skill 选的是右边一列。它输出一份带版本的契约，并在交接里写清楚：哪些已确认、哪些仍是提案、哪些尚未决定、哪些在阻塞。

**更快的实现速度不会自动解决需求模糊，反而可能更快地把错误理解变成完整产品。** 构建越快，错误理解被完整实现得越早，被写进代码的部分也越多。

## 它如何工作

`SKILL.md` 定义了一套 8 步方法。它没有执行器；是让模型按这段文字去做。

1. 冻结审查范围，把已批准的事实和提案分开。
2. 定义产品目的，并为每个 core job 定义**一个**可观察的完成信号。
3. 把角色映射到 core job、数据可见性、允许的操作、其拥有的状态和交接。
4. 只在产品确实需要时，才拆分公开、已认证、工作区和管理后台这几类 surface。
5. 把每条关键路径从入口追到完成，包括前置条件和受阻状态。
6. 至少与一个更简单的结构做比较。
7. 应用 [Architecture Rubric](references/architecture-rubric.md) 中的判断准则。
8. 返回一份带版本的架构契约和未决事项。**不要**推进到实施批准。

必需输入是：产品目标、目标用户或角色、他们的 core job、已知约束、以及现有的产品证据。界面、领域模型、用户反馈和现有流程属于可选的辅助输入。任何有限的建议给出之前，缺失或互相冲突的输入必须先被记录下来。

## Product Architect 定义什么

| 领域 | 这个 Skill 会定下什么 |
| --- | --- |
| 目的 | 用不含实现术语的方式说清产品目的 |
| Core job | 每个 core job 一个可观察的完成信号 |
| 角色 | 角色是谁——每个角色都必须来自证据，并且有独立的职责或权限 |
| 权限 | 每个敏感操作和数据视图是允许、拒绝，还是未决 |
| Surface | 公开、已认证、工作区、管理后台，且只在产品需要时才拆 |
| 关键路径 | 从入口到完成，包括前置条件和受阻状态 |
| 状态归属 | 每一次实质性状态流转，都由唯一的系统或角色负责 |
| 交接 | 接手方是否知道收到了什么、为什么、要做什么决定 |
| 结构决策 | 对现有结构做保留、合并、改名或删除 |
| 替代方案 | 至少一个更简单的结构，以及它的取舍 |
| Findings | 有证据支撑的问题项，每条带严重级别和具名负责人 |
| 未决事项 | 还有什么没定，以及由哪个人类负责 |

有两条边界是由 Skill 定义本身固定的，不靠配置：

- **只读。** 不修改代码，只输出被指派的那一份审查产物。
- **不补造。** 不用虚构的角色、能力或战略去填补缺失的证据，也绝不把推断当作已批准的需求。

## 产品契约

`SKILL.md` 点名了**十一个输出小节**。它们就是这份契约：

| # | 输出小节 |
| --- | --- |
| 1 | scope and evidence register |
| 2 | one-sentence purpose |
| 3 | actor/job/permission matrix |
| 4 | surface and navigation model |
| 5 | critical paths and state ownership |
| 6 | keep/merge/rename/remove decisions |
| 7 | simpler alternative and trade-offs |
| 8 | findings |
| 9 | unresolved decisions |
| 10 | observable acceptance criteria |
| 11 | downstream handoff |

每条 finding 必须带齐十个键：

```text
id  evidence_status  source  affected_actor  decision
reason  impact  alternative  verification  owner
```

下游交接必须带十一个字段：

```text
skill_name  skill_version  scope  input_paths  output_path
confirmed_decisions  proposals  open_decisions  blockers
evidence_status  next_role
```

<details>
<summary>判断准则中的词表（第 7 步引用）</summary>

**证据标签**——每条 finding 必须声明其中之一：

- `confirmed`：由已批准的需求、可观察的产品行为、权威领域来源，或具名的人类决定直接支撑。
- `inferred`：至少有一个来源支撑的当前最佳解释，但未被批准、也未被直接观察到。
- `to_verify`：关键信息缺失、自相矛盾、已过期，或来自不可信来源、演示来源。

**严重级别**——`blocker`、`high`、`medium`、`low`。

**判断优先级**，按顺序应用：

1. 用户任务与可观察结果；
2. 法律、数据、权限与组织边界；
3. 状态归属与跨角色交接的完整性；
4. 能支撑关键路径的最简信息架构；
5. 便利性、视觉偏好与实现复用。

没有明确的人类批准，低优先级的收益不能覆盖高优先级的约束。

**九项架构测试**——Purpose、Actor、Permission、Surface、State、Handoff、Completion、Recovery、Simplicity。

**质量门**——只有当所有关键角色、权限、状态归属方、入口、完成信号和未决的人类决定都已显式化时，架构才可交给下游做流程或体验审查；只要还存在任何 `blocker`，或有关键权限处于 `to_verify`，它就不满足可实施条件。

</details>

### 这份契约不覆盖什么

必须直说，因为“没有定义”和“定义了”同样重要：

| 不覆盖 | 仓库中的实际情况 |
| --- | --- |
| 模块或模块边界 | `module` 在 Skill 定义中**零命中**，不存在任何模块概念。 |
| 任务（Tasks）或 workflow 契约字段 | `task` 在 `SKILL.md` 中**零命中**；`workflow` 只作为产品类别和可选输入出现。仓库自己的用词是 **core job**。 |
| 异常（Exceptions） | `exception` 与 `异常` 在整个仓库**零命中**。最接近的已定义概念是 `blocked states` 和 **Recovery** 架构测试。 |
| 把入口作为独立输出小节 | 入口在触发描述和质量门中被点名，但它不是十一个输出小节之一——它隐含在 surface and navigation model 里。 |
| 契约自身的版本方案 | 第 8 步要求返回一份**带版本的**架构契约，但契约本身没有定义版本字段、格式或递增规则。仓库里唯一具体的版本号是包版本 `0.2.0`。 |
| 机器可读的 schema | 没有 JSON Schema、没有模板、没有 `templates/` 目录、也没有示例产物。 |

## 证据感知的架构

这个 Skill 不把“没有答案”当成待填空格，而是当成一种证据状态。

- 每条 finding 同时带 `evidence_status` **和** `source`。没有来源的 finding 不成立。
- 当来源冲突时，两者都保留，只用最权威、最新的来源给临时建议，并点名必须解决这个冲突的人类负责人。
- 如果产品目标、授权模型、数据边界或目标角色自相矛盾或缺失，Skill 会**带着有限的局部审查停下来**，而不是产出一份看起来很完整的契约。
- 没有引用批准来源时，不得暗示已获得人类批准。

这些都是文字，不是机制。仓库里没有任何东西强制执行它们：没有 linter、没有 schema 校验、也没有 CI 会在未来某次编辑删掉这些规则时失败。

## 人的决策边界

这个 Skill 是决策**角色**，不是决策**权力**。

| 它会做 | 它不会做 |
| --- | --- |
| 记录决定，连同判断理由和证据状态 | 批准战略 |
| 点名必须解决冲突的人类负责人 | 取代人类产品负责人 |
| 把不可逆的范围、权限、合规或战略选择升级给人类产品负责人 | 自己做出这些不可逆选择 |
| 输入缺失时返回有限的局部审查 | 编造需求来填坑 |
| 在实施批准之前停下 | 批准实施 |
| 把已批准的事实和提案分开 | 把推断变成已批准的需求 |

`manifest.json` 用机器可读的方式声明同一条边界：`"permissions": {"default": "read-only", "implementation": "requires human approval"}`。这些是声明，不是强制——仓库里没有任何产物会验证人类是否真的批准过。

## 什么时候该用

在产品结构还在被决定的阶段使用，适用于 SaaS、内部工具、工作流产品和数字服务：

- 要定义入口、角色、权限、core job 或信息架构；
- 要决定某个状态由哪个系统或角色负责；
- 要定义角色之间、系统之间的交接；
- 要决定某个 core job 的“可观察完成”是什么；
- 要在扩展之前先审查现有产品结构；
- 要把一个业务目标加上真实的用户证据，变成实现团队能直接开工的东西。

## 什么时候不该用

`SKILL.md` 明确排除了这几类：

- **视觉样式。** 它不是样式或设计品味工具。
- **实现。** 它不写代码，也不批准实施。
- **产品结构已经批准的、孤立的流程或体验缺陷。** 如果结构已经定了，问题只是某条流程断了或某个页面看不懂，那该找的不是这个角色。

以下同样不在范围内，依据是仓库里有什么，而不是某条显式排除：

- 产出机器可读的 schema、模板或生成式产物。
- 验证一个已经做出来的产品。这个角色负责定义契约；对已交付产品做独立判断，是同一生态里的另一个角色。
- 任何需要 output-eval 执行器、校验脚本或 CI 的事——本仓库一样都没有。

## 示例

一次调用，遵守“执行前先记录输入路径、输出路径、权限和决策范围”的显式调用规则：

```text
$kang-product-architect

Input:  docs/crm-brief.md, interviews/ops-notes.md
Output: reports/crm-product-contract.md
Mode:   read-only
Scope:  entry points, sales/manager/finance/admin actors, permissions,
        state ownership, handoffs, observable completion
```

返回的是那十一个小节组成的契约：先是 scope and evidence register，然后是目的、actor/job/permission matrix、surface and navigation model、带状态归属的关键路径、keep/merge/rename/remove 决策、含取舍的更简方案、每条都带 `evidence_status` 和 `source` 的 findings、带具名负责人的未决事项、可观察的验收标准，以及交接块。

如果需求文档只提到“销售”和“管理员”，但访谈记录里描述了同一个记录上的财务审批人，上面的规则只留下两种正当结果：把这个缺口记为一条带具名人类负责人的未决事项，或者在有证据支撑时才把它作为第四个角色接受。Skill 不允许做的，是悄悄把这个角色编出来。

本仓库自带的对应记录 fixture，是 [`evals/output_cases.json`](evals/output_cases.json) 里的那条 CRM 提示词。**仓库中没有存放任何示例输出产物**——上面描述的是 `SKILL.md` 要求的契约形状，不是一次真实运行的抓取结果。

## 状态与限制

**版本 `0.2.0`。** 字符串 `0.2.0` 在 `SKILL.md`、[`manifest.json`](manifest.json)、`reports/skill-ir.json`、[`tests/test_contract.py`](tests/test_contract.py)、git tag `v0.2.0` 和 GitHub release `v0.2.0` 中一致（发布于 2026-08-22，不是 prerelease，无 release 附件）。

**声明状态：`public-release-candidate`**（`manifest.json`）。本 README 采用该状态。这不是生产就绪声明，本文也不做任何生产就绪声明。

- `manifest.json` 同时写着 `"maturity_tier": "production"`。仓库中没有任何产物支撑这一档位——没有 CI、没有可复现的 eval 执行器、也没有任何使用记录——而且仓库自己的 [`reports/creation-handoff.md`](reports/creation-handoff.md) 明确写着发布与隔离安装证据“必须由发布流程生成”。请以 `public-release-candidate` 为准。
- **没有 CI。** 没有 `.github/` 目录、没有 workflow 文件、没有 lint 配置、没有打包配置。仓库里没有任何东西会自动校验一次改动。
- `manifest.json` 列了五个 release gate——`package validation`、`trigger evaluation`、`output contract evaluation`、`secret scan`、`isolated installation`。其中没有任何一个可以在仓库内部执行、复现或被 CI 强制。`output contract evaluation`、`secret scan` 和 `isolated installation` 连产物都不存在。
- 厂商适配描述文件 [`agents/interface.yaml`](agents/interface.yaml) 和 [`agents/openai.yaml`](agents/openai.yaml) 仍在宣传 `模块边界`。Skill 定义中并没有这个字段，`SKILL.md` 和判断准则都不支撑该说法。
- 评测 fixture 是手写的、合成的，没有记录任何来源信息——没有作者、没有日期、没有采集方法，也没有关联任何真实会话、工单或日志。它们不来自真实使用。
- [`reports/skill-ir.json`](reports/skill-ir.json) 基本是空的：`"inputs": []`、`"outputs": []`、`"router_rules": []`、`"output_contract": []`、`"gates": {}`、`"scripts": []`。尽管名字叫 IR，它并没有描述这个 Skill 的流程或门禁。

## 快速开始

**拿到文件。**

```bash
git clone https://github.com/KanG-ciyuan/kang-product-architect.git
cd kang-product-architect
```

**读 Skill。** `SKILL.md` 就是全部行为面——42 行，加一份 48 行的判断准则。使用前没有别的东西需要检查。

**调用它。** 在能加载 `SKILL.md` 这类 Skill 的 agent host 中，用 `$kang-product-architect` 调用，并说明输入路径、输出路径、权限和本轮决策范围。`manifest.json` 声明 `target_platforms: ["codex", "agent-skills-compatible"]`；`agents/interface.yaml` 声明 `adapter_targets: [openai, claude, generic, agent-skills-compatible]`。仓库没有记录最低 host 版本，也没有平台矩阵。

**运行包契约测试。** 不需要第三方包、不需要虚拟环境、也不需要 `pytest`：

```bash
python3 -m unittest discover -s tests -v
```

下面两种写法都在本检出上实际执行过并通过：

```bash
python3 -m unittest discover -s tests -v
PYTHONPATH=. python3 -m unittest discover -s tests -t tests -p 'test_*.py'
```

**安装方式尚未验证。** 本 README 的早期版本记录过 `npx skills add KanG-ciyuan/kang-product-architect`。核实时环境中没有 `skills` CLI，因此该命令从未被执行；它属于 `TO_VERIFY`，本文不把它当作可用安装方式。同一份旧 README 还记录过两个校验脚本，它们位于本仓库之外的私有本地 skills 目录中——其中一个还属于另一个项目。任何克隆本仓库的人都跑不了这两条命令，因此本文不再记录它们。本仓库自身不附带任何校验脚本。

## 证据 / 验证

下面说明跑了什么、结果如何、还有什么没被验证。

| 声明 | 类别 | 证据 |
| --- | --- | --- |
| 只读决策角色；不写代码；只输出被指派的产物 | `VERIFIED` | `SKILL.md:11`、`SKILL.md:42`；`manifest.json` `"permissions": {"default": "read-only"}` |
| 十一个具名输出小节 | `VERIFIED` | `SKILL.md:32` |
| 每条 finding 必须有十个键 | `VERIFIED` | `SKILL.md:34` |
| 十一个具名交接字段；3 个证据标签；5 级判断优先级；9 项架构测试；4 个严重级别；1 个质量门 | `VERIFIED` | `references/architecture-rubric.md:3-48` |
| 输入不足时带有限的局部审查停下；升级给人类产品负责人 | `VERIFIED` | `SKILL.md:36-38` |
| 版本 `0.2.0` 在包、测试、tag 和 release 之间一致 | `VERIFIED` | `SKILL.md:6`、`manifest.json`、`reports/skill-ir.json`、`tests/test_contract.py:13-14`、tag `v0.2.0`、GitHub release `v0.2.0` |
| MIT 许可，`Copyright (c) Kang` | `VERIFIED` | [`LICENSE`](LICENSE) |
| 3 个测试通过；记录了 11 条触发提示词（5 应触发 / 3 不应触发 / 3 近似相邻） | 计数为 `VERIFIED` | `tests/test_contract.py`（运行结果：3 tests, OK）；`evals/trigger_cases.json` |
| 触发评测 11/11 通过 | `SIMULATED` | `reports/trigger-eval.json` 记录 `"pass_rate": 1.0`，但该指标是 `匹配到的关键词组数 / 4`，阈值 `0.3`，外加负向模式否决。它是一个**子串关键词匹配器**：不调用模型、不加载 `SKILL.md`、也不测试这个 Skill。仓库中没有能生成它的执行器。三条近似相邻用例之所以得 `0.0`，纯粹是因为缺少关键词，因此**这套 fixture 无法把本 Skill 与同生态的兄弟审查类 Skill 区分开。** |
| 这些测试验证了产品契约 | `SIMULATED`——不成立 | 它们是结构性检查：身份与版本一致性、`SKILL.md` 中 4 个标题字符串存在、判断准则中 4 个标题字符串存在、以及 fixture 形状。把 `## Output contract` 小节的**整个正文**删掉，3 个测试仍然全部通过；而只改这一个标题名反而失败。它们断言的是字符串和文件存在——与契约行为无关。 |
| 英文描述是中性的，不绑定某个企业产品 | v0.2.0 为 `VERIFIED` | 当前 `SKILL.md` 领域中立；`tests/test_contract.py:28` 防止旧措辞回流。`HISTORICAL`：v0.1.0 的 `SKILL.md` 明确绑定在一个企业 AI 流程诊断产品上，那段文本仍留在公开的 git 历史中。 |
| 存在 output contract 评测 | `TO_VERIFY`——缺失 | `evals/output_cases.json` 只有**恰好一个**用例，`"input_files": []`，四条断言字符串在仓库里没有任何东西解析。仓库中不存在任何 output-eval 报告。 |
| 已做隔离安装验证 | `TO_VERIFY`——缺失 | 被列为 release gate；无产物。 |
| 已做密钥扫描 | `TO_VERIFY`——缺失 | 被列为 release gate；无报告、无脚本、无配置。 |
| `npx skills add ...` 可安装本 Skill | `TO_VERIFY` | 未执行；环境中没有安装 `skills` CLI。 |
| 跨领域或多用户验证 | `TO_VERIFY`——缺失 | `reports/skill-ir.json` 只列了一个目标用户；`reports/creation-handoff.md` 把跨领域一致性称为 `hypothesis`，并说明 provider-backed 与长期人工证据都缺失。 |

请把触发评测报告读作一份**记录下来的 fixture**，而不是评测证据。它在内部是可复现的——任何人都能根据 `evals/trigger_cases.json` 重算出来——而这恰恰意味着，按现在的写法它不可能失败。

## 生态

```text
发现 DISCOVER
企业 AI 诊断 Skills
        ↓
定义 DEFINE
Kang Product Architect
Kang Enterprise Process Reviewer
        ↓
构建与协同 BUILD & COORDINATE
Kang Agent Workforce
Kang Agent Collab
Kang Frontend Standard
        ↓
验证 VERIFY
Kang B2B UX Auditor
Kang Product Acceptance Auditor
        ↓
交付 DELIVER
Kang GitHub README
Kang PPT Skill
```

> 这是一张生态地图，不是严格的运行时流水线。各阶段描述的是项目所处的工作位置，
> 而不是强制的执行顺序。

本项目位于 **DEFINE 定义** 阶段。它产出的契约，交给 `kang-enterprise-process-reviewer` 审查可执行性，也是 VERIFY 阶段判断已交付产品时的依据。

维护者：Kang — [github.com/KanG-ciyuan](https://github.com/KanG-ciyuan/)。

---

## 属于 Kang 开源 AI 体系

本项目是「面向企业 AI 转型、Agent 协作与 AI 原生产品交付的证据驱动体系」的一部分。

| 阶段 | 项目 | 作用 |
| --- | --- | --- |
| DISCOVER 发现 | [enterprise-ai-diagnostic-skills](https://github.com/KanG-ciyuan/enterprise-ai-diagnostic-skills) | 在自动化之前，先弄清企业真实业务如何运行 |
| DEFINE 定义 | [kang-product-architect](https://github.com/KanG-ciyuan/kang-product-architect) | 把模糊需求转化为可实施、可审查的产品契约 |
| DEFINE 定义 | [kang-enterprise-process-reviewer](https://github.com/KanG-ciyuan/kang-enterprise-process-reviewer) | 审查流程是否可执行、可追责、可恢复 |
| BUILD & COORDINATE 构建与协同 | [kang-agent-workforce](https://github.com/KanG-ciyuan/kang-agent-workforce) | 角色化的 Agent 数字员工团队与显式交接 |
| BUILD & COORDINATE 构建与协同 | [kang-agent-collab](https://github.com/KanG-ciyuan/kang-agent-collab) | Agent 协作与交接协议 |
| BUILD & COORDINATE 构建与协同 | [kang-frontend-standard](https://github.com/KanG-ciyuan/kang-frontend-standard) | AI 构建界面的前端质量标准 |
| VERIFY 验证 | [kang-b2b-ux-auditor](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor) | 用户能否真正把工作做完 |
| VERIFY 验证 | [kang-product-acceptance-auditor](https://github.com/KanG-ciyuan/kang-product-acceptance-auditor) | AI 构建产品的独立验收 |
| DELIVER 交付 | [kang-github-readme](https://github.com/KanG-ciyuan/kang-github-readme) | 证据感知的 README 工程 |
| DELIVER 交付 | [kang-ppt-skill](https://github.com/KanG-ciyuan/kang-ppt-skill) | 证据感知的演示文稿设计 |

**横向基础设施：** [kang-meta-skill](https://github.com/KanG-ciyuan/kang-meta-skill) —
Skill 工程化、评估与发布治理。

**早期工作：** [ai-agent-rules](https://github.com/KanG-ciyuan/ai-agent-rules)、
[workflow-five-steps](https://github.com/KanG-ciyuan/workflow-five-steps)、
[renovation-agent](https://github.com/KanG-ciyuan/renovation-agent)。

## 开源许可证

本项目采用 [MIT License](LICENSE) 开源。

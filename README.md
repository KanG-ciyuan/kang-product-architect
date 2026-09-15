# Kang Product Architect

English | [简体中文](README.zh-CN.md)

[![Release](https://img.shields.io/github/v/release/KanG-ciyuan/kang-product-architect?display_name=tag&sort=semver&style=flat-square)](https://github.com/KanG-ciyuan/kang-product-architect/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/KanG-ciyuan/kang-product-architect?style=flat-square)](https://github.com/KanG-ciyuan/kang-product-architect/commits/main)

**Turn ambiguous business requirements into an implementation-ready product contract before AI starts building.**

**Positioning:** Product Contract Architect for AI-built Software · **Ecosystem stage:** DEFINE

`kang-product-architect` is a read-only product-architecture decision role for AI agents. It converts a product objective and observed user needs into the smallest coherent product contract, and it refuses to invent actors, capabilities, or strategy to fill missing evidence.

The entire package is prose: `SKILL.md` (42 lines) plus [`references/architecture-rubric.md`](references/architecture-rubric.md) (48 lines). There is no executable code, no script, no template and no runtime dependency — the package itself declares `"scripts": []`. Scope is domain-general: SaaS, internal tools, workflow products and digital services.

> **Implementation speed does not correct requirement ambiguity. It amplifies it.**

---

## Why Define Before AI Builds?

An AI builder does not stop at an ambiguous requirement. It resolves the ambiguity itself — silently picking an actor, a permission rule, a state owner and a definition of "done" that nobody approved. The result looks finished, so those decisions are never reviewed as decisions.

Everything downstream inherits the structure that was defined here, or left undefined here. Process design, UX review and acceptance testing all operate on a product that already assumes certain actors exist, that certain data is visible to them, and that certain states have an owner.

This project exists to make those assumptions explicit and reviewable **before** implementation, as a written contract rather than a conversational convention.

## Prompt-Driven vs Contract-Driven

Same requirement, two ways to build it.

| | Prompt-driven | Contract-driven |
| --- | --- | --- |
| Where the requirement lives | a chat message | a written contract artifact |
| Who fills the gaps | whoever builds next, implicitly | a named human owner, explicitly — or the item stays `to_verify` |
| Evidence | asserted in prose | `evidence_status` and `source` on every finding |
| Alternatives | none recorded | at least one simpler alternative compared, with trade-offs |
| When ambiguity surfaces | after the code exists | before implementation, as `unresolved decisions` |
| Completion | "it looks done" | one observable completion signal per core job |
| Stop condition | none | a `blocker`, or a critical permission at `to_verify`, blocks implementation readiness |

The skill takes the second column. Its output is a versioned contract, and its handoff tells the next role what was confirmed, what is still a proposal, what remains open, and what is blocking.

**Implementation speed does not correct requirement ambiguity. It amplifies it.** A faster build cycle produces a more complete version of the wrong understanding, sooner, with more code already committed to it.

## How It Works

`SKILL.md` defines an eight-step method. There is no runner; a model following this prose is asked to perform it.

1. Freeze the review scope and separate approved facts from proposals.
2. Define the product purpose and one observable completion signal per core job.
3. Map actors to jobs, data visibility, allowed actions, owned states, and handoffs.
4. Separate public, authenticated, workspace, and administrative surfaces only when the product needs them.
5. Trace each critical path from entry to completion, including prerequisites and blocked states.
6. Compare the proposed structure with at least one simpler alternative.
7. Apply the decision rules in the [Architecture Rubric](references/architecture-rubric.md).
8. Return a versioned architecture contract and unresolved decisions. Do not proceed to implementation approval.

Required inputs are the objective, the target users or actors, their core jobs, known constraints, and available product evidence. Screens, domain models, user feedback and current workflows are treated as optional supporting inputs. Missing or conflicting inputs must be recorded before any bounded recommendation is made.

## What Product Architect Defines

| Area | What the skill decides |
| --- | --- |
| Purpose | The product purpose, stated without implementation terms |
| Core jobs | One observable completion signal per core job |
| Actors | Who the actors are — each one must come from evidence and have a distinct job or authority |
| Permissions | Whether each sensitive action and data view is allowed, denied, or unresolved |
| Surfaces | Public, authenticated, workspace and administrative surfaces, only where the product needs them |
| Critical paths | Each path traced from entry to completion, including prerequisites and blocked states |
| State ownership | One system or role accountable for each material state transition |
| Handoffs | Whether the receiver knows what arrived, why, and what decision is expected |
| Structure decisions | Keep, merge, rename or remove, applied to the existing structure |
| Alternatives | At least one simpler structure, with its trade-offs |
| Findings | Evidence-backed findings, each with a severity and a named owner |
| Open decisions | What remains unresolved, and which human owns it |

Two boundaries are fixed by the skill definition, not by configuration:

- **Read-only.** It does not modify code, and it outputs only the assigned review artifact.
- **No invention.** It does not invent actors, capabilities, or strategy to fill missing evidence, and never turns an inference into an approved requirement.

## The Product Contract

`SKILL.md` names **eleven output sections**. These are the contract:

| # | Output section |
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

Every finding must carry all ten keys:

```text
id  evidence_status  source  affected_actor  decision
reason  impact  alternative  verification  owner
```

The downstream handoff must carry eleven fields:

```text
skill_name  skill_version  scope  input_paths  output_path
confirmed_decisions  proposals  open_decisions  blockers
evidence_status  next_role
```

<details>
<summary>Rubric vocabularies (referenced from step 7)</summary>

**Evidence labels** — every finding states one:

- `confirmed`: directly supported by an approved requirement, observable product behavior, authoritative domain source, or named human decision.
- `inferred`: the best current interpretation supported by at least one source, but not approved or directly observed.
- `to_verify`: material information is absent, contradictory, stale, or from an untrusted or demo source.

**Severity** — `blocker`, `high`, `medium`, `low`.

**Decision priority**, applied in order:

1. user job and observable outcome;
2. legal, data, permission, and organizational boundaries;
3. state ownership and cross-role handoff integrity;
4. simplest information architecture that supports the critical path;
5. convenience, visual preference, and implementation reuse.

A lower-priority benefit cannot override a higher-priority constraint without explicit human approval.

**Nine architecture tests** — Purpose, Actor, Permission, Surface, State, Handoff, Completion, Recovery, Simplicity.

**Quality gate** — an architecture is ready for downstream process or UX review only when all critical actors, permissions, state owners, entry points, completion signals, and unresolved human decisions are explicit. It is not implementation-ready while any `blocker` remains or a critical permission is `to_verify`.

</details>

### What the contract does not cover

Stated plainly, because the absence matters as much as the presence:

| Not covered | Reality in this repository |
| --- | --- |
| Modules or module boundaries | `module` has **zero hits** anywhere in the skill definition. No module concept exists. |
| Tasks, or a workflow contract field | `task` has **zero hits** in `SKILL.md`. `workflow` appears only as a product category and as an optional input. The repo's own term is **core job**. |
| Exceptions | `exception` and `异常` have **zero hits** repo-wide. The nearest defined concepts are `blocked states` and the **Recovery** architecture test. |
| Entry points as a named output section | Entry points are named in the trigger description and in the quality gate, but they are not one of the eleven output sections — they are implicit inside the surface and navigation model. |
| A versioning scheme for the contract itself | Step 8 says to return a *versioned* architecture contract, but no version field, format, or bump rule is defined for the contract. The only concrete version is the package version `0.2.0`. |
| A machine-readable schema | No JSON Schema, no template, no `templates/` directory and no example artifact. |

## Evidence-Aware Architecture

The skill does not treat a missing answer as a blank to be filled. It treats it as an evidence status.

- Every finding carries `evidence_status` **and** `source`. A finding without a source is not a finding.
- When sources conflict, both are preserved, the most authoritative and current one is used only for a provisional recommendation, and the human owner who must resolve it is named.
- If the product objective, authority model, data boundary or target actor is contradictory or absent, the skill **stops with a bounded partial review** instead of producing a complete-looking contract.
- Human approval may not be implied unless an approval source is cited.

This is prose, not machinery. Nothing in the repository enforces any of it: there is no linter, no schema validation and no CI that would fail if a future edit deleted these rules.

## Human Decision Boundary

The skill is a decision **role**, not a decision **authority**.

| It does | It does not |
| --- | --- |
| Records decisions with their reasoning and their evidence status | Approve strategy |
| Names the human owner who must resolve a conflict | Replace the human product owner |
| Escalates irreversible scope, permission, compliance or strategy choices to the human product owner | Make those irreversible choices itself |
| Returns a bounded partial review when inputs are missing | Invent requirements to close the gap |
| Stops before implementation approval | Approve implementation |
| Separates approved facts from proposals | Turn an inference into an approved requirement |

`manifest.json` states the same boundary machine-readably: `"permissions": {"default": "read-only", "implementation": "requires human approval"}`. These are declarations, not enforcement — no artifact in this repository verifies that a human actually approved anything.

## When to Use

Use it when the product structure is still being decided, for SaaS, internal tools, workflow products and digital services:

- defining entry points, actors, permissions, core jobs or information architecture;
- deciding which system or role owns a given state;
- defining handoffs between roles or systems;
- deciding what observable completion means for a core job;
- reviewing an existing product structure before it is extended;
- turning a business objective plus real user evidence into something an implementation team can work from.

## When NOT to Use

`SKILL.md` excludes these explicitly:

- **Visual styling.** Not a styling or design-taste tool.
- **Implementation.** It writes no code and does not approve implementation.
- **Isolated workflow or UX defects whose product structure is already approved.** If the structure is settled and the problem is one broken flow or one unclear screen, this is the wrong role.

Also out of scope, by what the repo contains rather than by an explicit exclusion:

- Producing a machine-readable schema, template or generated artifact.
- Verifying a built product. This role defines the contract; independent judgement of a delivered product is a different role in the same ecosystem.
- Anything that needs an output-eval runner, a validator script or CI — this repository ships none of those.

## Example

An invocation, following the explicit-invocation rule that input paths, output path, permissions and decision scope are recorded before execution:

```text
$kang-product-architect

Input:  docs/crm-brief.md, interviews/ops-notes.md
Output: reports/crm-product-contract.md
Mode:   read-only
Scope:  entry points, sales/manager/finance/admin actors, permissions,
        state ownership, handoffs, observable completion
```

What comes back is the eleven-section contract: a scope and evidence register first, then the purpose, the actor/job/permission matrix, the surface and navigation model, critical paths with state ownership, keep/merge/rename/remove decisions, a simpler alternative with trade-offs, findings each carrying `evidence_status` and `source`, the decisions left open with a named owner, observable acceptance criteria, and the handoff block.

If a brief names only "sales" and "admin" while the notes describe a finance approver acting on the same records, the rules above leave two legitimate outcomes: record the gap as an unresolved decision with a named human owner, or accept the fourth actor only if the evidence supports one. What the skill must not do is silently invent the role.

The repository's own recorded fixture for this scenario is the CRM prompt in [`evals/output_cases.json`](evals/output_cases.json). **No example output artifact is stored in this repository** — the shape above is the contract `SKILL.md` requires, not a captured run.

## Status and Limitations

**Version `0.2.0`.** The string `0.2.0` is consistent across `SKILL.md`, [`manifest.json`](manifest.json), `reports/skill-ir.json`, [`tests/test_contract.py`](tests/test_contract.py), git tag `v0.2.0`, and GitHub release `v0.2.0` (published 2026-08-22, not a prerelease, no release assets).

**Declared status: `public-release-candidate`** (`manifest.json`). This README uses that status. It is not a production claim, and none is made here.

- `manifest.json` also carries `"maturity_tier": "production"`. No artifact in this repository supports that tier — there is no CI, no reproducible eval runner and no usage record — and the repo's own [`reports/creation-handoff.md`](reports/creation-handoff.md) states that publication and isolated-install evidence "must be generated by the release flow". Treat `public-release-candidate` as authoritative.
- **No CI.** There is no `.github/` directory, no workflow file, no lint config and no packaging config. Nothing in this repository automatically validates a change.
- `manifest.json` lists five release gates — `package validation`, `trigger evaluation`, `output contract evaluation`, `secret scan`, `isolated installation`. None of them is executable, reproducible or CI-enforced from inside the repository. `output contract evaluation`, `secret scan` and `isolated installation` have no artifact at all.
- The vendor adapter descriptors [`agents/interface.yaml`](agents/interface.yaml) and [`agents/openai.yaml`](agents/openai.yaml) still advertise `模块边界` (module boundaries). The skill definition does not define that field, and the claim is not supported by `SKILL.md` or the rubric.
- The evaluation fixtures are hand-written and synthetic, with no recorded provenance — no author, no date, no collection method, no link to a real session, ticket or log. They did not come from real usage.
- [`reports/skill-ir.json`](reports/skill-ir.json) is largely empty: `"inputs": []`, `"outputs": []`, `"router_rules": []`, `"output_contract": []`, `"gates": {}`, `"scripts": []`. It does not describe this skill's workflow or gates, despite its name.

## Quick Start

**Get the files.**

```bash
git clone https://github.com/KanG-ciyuan/kang-product-architect.git
cd kang-product-architect
```

**Read the skill.** `SKILL.md` is the entire behavioural surface — 42 lines plus a 48-line rubric. There is nothing else to inspect before using it.

**Invoke it.** In an agent host that loads `SKILL.md`-style skills, invoke it as `$kang-product-architect` and state the input paths, output path, permissions and expected decision scope. `manifest.json` declares `target_platforms: ["codex", "agent-skills-compatible"]`; `agents/interface.yaml` declares `adapter_targets: [openai, claude, generic, agent-skills-compatible]`. No minimum host version and no platform matrix are documented.

**Run the package contract tests.** These need no third-party package, no virtualenv and no `pytest`:

```bash
python3 -m unittest discover -s tests -v
```

Both of these forms were executed against this checkout and pass:

```bash
python3 -m unittest discover -s tests -v
PYTHONPATH=. python3 -m unittest discover -s tests -t tests -p 'test_*.py'
```

**Installation is not verified.** An earlier version of this README documented `npx skills add KanG-ciyuan/kang-product-architect`. The `skills` CLI was not available when this was checked, so that command was never executed; it is `TO_VERIFY` and is not presented here as a working install. The same README documented two validator scripts that lived in a private local skills directory outside this repository — one of them belonging to a different project. Those commands cannot work for anyone who clones this repository, so they are not documented here. This repository ships no validator script of its own.

## Evidence / Validation

What was run, what it showed, and what remains unverified.

| Claim | Class | Evidence |
| --- | --- | --- |
| Read-only decision role; writes no code; outputs only the assigned artifact | `VERIFIED` | `SKILL.md:11`, `SKILL.md:42`; `manifest.json` `"permissions": {"default": "read-only"}` |
| Eleven named output sections | `VERIFIED` | `SKILL.md:32` |
| Ten required keys on every finding | `VERIFIED` | `SKILL.md:34` |
| Eleven named handoff fields; 3 evidence labels; 5-step decision priority; 9 architecture tests; 4 severity levels; 1 quality gate | `VERIFIED` | `references/architecture-rubric.md:3-48` |
| Stops with a bounded partial review; escalates to the human product owner | `VERIFIED` | `SKILL.md:36-38` |
| Version `0.2.0` consistent across package, tests, tag and release | `VERIFIED` | `SKILL.md:6`, `manifest.json`, `reports/skill-ir.json`, `tests/test_contract.py:13-14`, tag `v0.2.0`, GitHub release `v0.2.0` |
| MIT licensed, `Copyright (c) Kang` | `VERIFIED` | [`LICENSE`](LICENSE) |
| 3 tests pass; 11 trigger prompts recorded (5 should-trigger / 3 should-not-trigger / 3 near-neighbour) | `VERIFIED` as counts | `tests/test_contract.py` (run: 3 tests, OK); `evals/trigger_cases.json` |
| Trigger evaluation passed 11/11 | `SIMULATED` | `reports/trigger-eval.json` records `"pass_rate": 1.0`, but the metric is `matched_keyword_groups / 4` with a `0.3` threshold and a negative-pattern veto. It is a **substring keyword matcher**: it never invokes a model, never loads `SKILL.md`, and never tests the skill. No runner for it exists in the repository. The three near-neighbour cases score `0.0` purely for missing keywords, so **the fixture does not discriminate this skill from its sibling auditor skills.** |
| The tests validate the product contract | `SIMULATED` — not supported | They are structural checks: identity and version agreement, four heading strings present in `SKILL.md` and four in the rubric, and fixture shape. Deleting the **entire body** of the `## Output contract` section still passes all three tests; renaming only that heading fails. They assert that strings and files exist — nothing about contract behaviour. |
| English description is generic, not bound to one enterprise product | `VERIFIED` for v0.2.0 | Current `SKILL.md` is domain-neutral; `tests/test_contract.py:28` guards against the older phrasing. `HISTORICAL`: the v0.1.0 `SKILL.md` was explicitly bound to one enterprise AI process diagnosis product; that text remains in public git history. |
| Output-contract evaluation exists | `TO_VERIFY` — missing | `evals/output_cases.json` holds **exactly one** case with `"input_files": []` and four assertion strings that nothing in the repository parses. There is no output-eval report anywhere. |
| Isolated installation was validated | `TO_VERIFY` — missing | Listed as a release gate; no artifact. |
| A secret scan was performed | `TO_VERIFY` — missing | Listed as a release gate; no report, script or config. |
| `npx skills add ...` installs the skill | `TO_VERIFY` | Not executed; the `skills` CLI was not installed. |
| Cross-domain or multi-user validation | `TO_VERIFY` — missing | `reports/skill-ir.json` names a single target user; `reports/creation-handoff.md` calls cross-domain consistency a `hypothesis` and states that provider-backed and long-term human evidence are missing. |

Read the trigger report as a **recorded fixture**, not as evaluation evidence. It is internally reproducible — anyone can recompute it from `evals/trigger_cases.json` — and that is exactly why it cannot fail as written.

## Ecosystem

```text
DISCOVER
Enterprise AI Diagnostic Skills
        ↓
DEFINE
Kang Product Architect
Kang Enterprise Process Reviewer
        ↓
BUILD & COORDINATE
Kang Agent Workforce
Kang Agent Collab
Kang Frontend Standard
        ↓
VERIFY
Kang B2B UX Auditor
Kang Product Acceptance Auditor
        ↓
DELIVER
Kang GitHub README
Kang PPT Skill
```

> This is an ecosystem map, not a strict runtime pipeline. The stages describe where
> each project sits in the work, not a mandatory execution order.

This project sits at **DEFINE**. It produces the contract that `kang-enterprise-process-reviewer` reviews for executability, and that the VERIFY stage later judges the delivered product against.

Maintained by Kang — [github.com/KanG-ciyuan](https://github.com/KanG-ciyuan/).

---

## Part of the Kang Open-Source AI System

This project is one part of an evidence-driven system for enterprise AI transformation,
agent collaboration, and AI-native product delivery.

| Stage | Project | Role |
| --- | --- | --- |
| DISCOVER | [enterprise-ai-diagnostic-skills](https://github.com/KanG-ciyuan/enterprise-ai-diagnostic-skills) | Understand how the business actually works before automating it |
| DEFINE | [kang-product-architect](https://github.com/KanG-ciyuan/kang-product-architect) | Turn ambiguous requirements into an implementation-ready product contract |
| DEFINE | [kang-enterprise-process-reviewer](https://github.com/KanG-ciyuan/kang-enterprise-process-reviewer) | Review whether workflows are executable, accountable and recoverable |
| BUILD & COORDINATE | [kang-agent-workforce](https://github.com/KanG-ciyuan/kang-agent-workforce) | Role-based AI product workforce with explicit handoffs |
| BUILD & COORDINATE | [kang-agent-collab](https://github.com/KanG-ciyuan/kang-agent-collab) | Agent collaboration and handoff protocol |
| BUILD & COORDINATE | [kang-frontend-standard](https://github.com/KanG-ciyuan/kang-frontend-standard) | Frontend quality standard for AI-built interfaces |
| VERIFY | [kang-b2b-ux-auditor](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor) | Can users actually finish the work? |
| VERIFY | [kang-product-acceptance-auditor](https://github.com/KanG-ciyuan/kang-product-acceptance-auditor) | Independent acceptance of AI-built products |
| DELIVER | [kang-github-readme](https://github.com/KanG-ciyuan/kang-github-readme) | Evidence-aware README engineering |
| DELIVER | [kang-ppt-skill](https://github.com/KanG-ciyuan/kang-ppt-skill) | Evidence-aware presentation design |

**Cross-cutting infrastructure:** [kang-meta-skill](https://github.com/KanG-ciyuan/kang-meta-skill) —
Skill engineering, evaluation and release governance.

**Earlier work:** [ai-agent-rules](https://github.com/KanG-ciyuan/ai-agent-rules),
[workflow-five-steps](https://github.com/KanG-ciyuan/workflow-five-steps),
[renovation-agent](https://github.com/KanG-ciyuan/renovation-agent).

## License

Released under the [MIT License](LICENSE).

# Product Architecture Rubric

## Evidence labels

- `confirmed`: directly supported by an approved requirement, observable product behavior, authoritative domain source, or named human decision.
- `inferred`: the best current interpretation supported by at least one source, but not approved or directly observed.
- `to_verify`: material information is absent, contradictory, stale, or from an untrusted or demo source.

When sources conflict, preserve both, use the most authoritative and current source only for a provisional recommendation, and name the human owner who must resolve it.

## Decision priority

Apply in this order:

1. user job and observable outcome;
2. legal, data, permission, and organizational boundaries;
3. state ownership and cross-role handoff integrity;
4. simplest information architecture that supports the critical path;
5. convenience, visual preference, and implementation reuse.

A lower-priority benefit cannot override a higher-priority constraint without explicit human approval.

## Architecture tests

- **Purpose:** Can the product be described without implementation terms?
- **Actor:** Does every actor come from evidence, and do they have a distinct job or authority?
- **Permission:** Is each sensitive action and data view allowed, denied, or unresolved?
- **Surface:** Does each surface serve a job that cannot be simpler elsewhere?
- **State:** Is one system or role accountable for each material state transition?
- **Handoff:** Does the receiver know what arrived, why, and what decision is expected?
- **Completion:** Can an observer tell that the user's job is complete?
- **Recovery:** Can blocked, rejected, expired, or interrupted work resume safely?
- **Simplicity:** Would removing or merging a surface preserve the core outcome?

## Severity

- `blocker`: critical job, permission boundary, or state ownership cannot be defined safely.
- `high`: a core role cannot complete or hand off its main job reliably.
- `medium`: the path works but creates substantial ambiguity, duplication, or operational cost.
- `low`: local clarity or consistency issue with no material task failure.

## Quality gates

An architecture is ready for downstream process or UX review only when all critical actors, permissions, state owners, entry points, completion signals, and unresolved human decisions are explicit. It is not implementation-ready while any `blocker` remains or a critical permission is `to_verify`.

## Handoff fields

Include `skill_name`, `skill_version`, `scope`, `input_paths`, `output_path`, `confirmed_decisions`, `proposals`, `open_decisions`, `blockers`, `evidence_status`, and `next_role`. Do not imply human approval unless an approval source is cited.

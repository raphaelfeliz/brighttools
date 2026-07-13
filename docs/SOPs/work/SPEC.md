# SPEC: Work Management

## Contract
This spec is the canonical rule set for organizing and executing work.

## Roots
```text
system/  code and apps
docs/    documentation
work/    execution state
```

## Vocabulary
- `seed`: raw idea, not executable.
- `init`: root objective.
- `incr`: deliverable slice.
- `wp`: executable work package.
- `task`: checklist item inside `todo.md`.
- `evidence`: proof stored under local `evidence/`.
- `approval evidence`: human statement or artifact showing what was reviewed.
- `deviation`: documented exception.

## Required Work Layout
```text
work/
  README.md
  SPEC.md
  CHECKLIST.md
  seeds/
  templates/
  examples/
  archive/
  01-init-<slug>/
    meta.yaml
    SPEC.md
    CHECKLIST.md
    onboarding.md
    blueprint.md
    01-incr-<slug>/
      meta.yaml
      SPEC.md
      CHECKLIST.md
      onboarding.md
      blueprint.md
      handover.md
      01-wp-<slug>/
        meta.yaml
        todo.md
        handover.md
        evidence/
          logs/
            001.yaml
```

## Placement Algorithm
```text
IF input is raw -> create seed.
IF seed fits existing WP -> append task to WP todo.
ELSE IF seed fits existing incr -> create next WP.
ELSE IF seed fits existing init -> create next incr + first WP.
ELSE -> create next init + first incr + first WP.
```

## Numbering
- Use next two-digit sibling prefix.
- Never renumber existing siblings unless explicitly requested.
- `meta.id` MUST equal directory name.
- `meta.parent` MUST equal parent `meta.id`.
- Dependencies and blockers MUST reference existing ordered IDs.

## WP Start Gate
A WP MUST NOT start until:
- `todo.md` exists.
- `meta.yaml` exists.
- `evidence/logs/` directory is initialized.
- `evidence/` exists.
- `onboarding.md` and `blueprint.md` exist at the parent initiative/increment level.
- approval to start is recorded in `todo.md`.
- start approval includes approval evidence.

If a WP changes materially after approval, execution MUST stop until renewed approval evidence is recorded.

Material change means:
- scope changed
- risk changed
- rollback changed
- tasks added/removed
- dependencies changed
- approval or deployment boundary changed

## Human Approval Gate
Human approval MUST include:
- approval phrase, default `raphael approved`
- evidence text describing what the human reviewed or observed (verifying details in the WP's `handover.md`)
- date
- approver
- decision: approved, rejected, or blocked

Approval phrase alone is invalid.

Invalid:
```text
raphael approved
```

Valid:
```text
approver: Raphael
decision: approved
phrase: raphael approved
evidence: I checked the local CRM dropdown and saw all five statuses; card toggle updated correctly (matching the behavioral change in handover.md).
date: 2026-06-03
```

If evidence is missing, approval is blocked.

## Split Rules
Create separate WPs for:
- discovery/planning
- data/schema mutation
- local implementation
- local human approval
- live deployment
- live human approval
- rollback/cleanup

Each separate WP MUST maintain its own independent `handover.md` to cleanly isolate changed files and behavioral boundaries.

MAY combine only if all are true:
- local-only
- no human approval gate
- no shared data
- no deployment
- rollback is trivial

## Risk Rules
Rollback is REQUIRED before:
- production data mutation
- shared data mutation
- schema contract change
- infrastructure change
- secret change
- deployment

Verification MUST immediately follow mutation.
Human approval MUST follow verification when live or user-facing behavior changes.

## Edge Cases
MAY adapt only if:
- deviation is logged in `todo.md`
- rollback/evidence/approval boundaries remain explicit
- production, data, security, and live-user risk are not hidden

## Status
Allowed transitions:
```text
planned -> ready -> active -> review -> done
active -> blocked -> active
planned|ready|blocked -> abandoned
```

## Done Rule
A WP is not done until:
- all tasks are complete
- `evidence/logs/` contains the full set of sequential, append-only step files detailing execution steps and command outcomes
- `handover.md` is fully populated with files, commands, and behavioral change details
- evidence is referenced and linked in `handover.md`
- required approvals include evidence
- rollback is documented or explicitly not applicable
- handover state is current, and parent/increment `handover.md` files contain the conceptual summary of this completed WP.

## Abstract, Don't Duplicate (Redundancy Rule)
To optimize AI context window limits and maintain single sources of truth, adhere to strict scoping guidelines:
1. **Parents Abstract, Children Detail**: Parent files (`onboarding.md`, `blueprint.md`) should only connect high-level conceptual dots. Do not replicate fine-grained details or list of files changed in parent levels; instead, point to child locations (e.g. `handover.md`).
2. **Onboarding vs Blueprint**: `onboarding.md` is strictly about the "big picture" context (how the system behaves/architecture context). `blueprint.md` defines the final desired state ("what" we want in the end, such as schema models or API outputs), not "how" to implement it (which belongs in `todo.md`).
3. **No Boilerplate Propagation**: Children assume parent context has already been read. Do not duplicate background context, goals, or glossary lists in child `todo.md` files.

## Agent Orchestration & Dependency Annotations
To support orchestrators planning and spinning subagents dynamically:
1. **Syntactic Annotations**: All tasks inside `todo.md` must append assignment and dependency metadata:
   `- [ ] {id}. {task} [agent: {agent_name}] [blocks: {none|id|wp_id}] [blocked_by: {none|id|wp_id}]`
2. **Dependency Scoping Rules**:
   - **Internal Blocker**: Reference the specific 2-digit task ID within the same file (e.g., `blocked_by: 01`).
   - **Smallest Foreign Blocker**: Reference a parent work package ID (e.g., `blocked_by: 01-wp-prepare-migration`). Never reference internal task IDs of foreign work packages.

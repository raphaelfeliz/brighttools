# Approval Protocol

## Purpose
Prevent false approval states when AI asks the human to approve work.

## Rule
Approval requires phrase plus evidence.

The default phrase is:
```text
raphael approved
```

The phrase alone is invalid.

## Required Approval Record
Use this block in `todo.md` under `## Approvals`.

```yaml
- gate: start | local-human | pre-mutation | live-human | changed-wp
  approver: Raphael
  decision: approved | rejected | blocked
  phrase: "raphael approved"
  evidence: "<what the human saw, tested, reviewed, or rejected>"
  date: YYYY-MM-DD
```

## Start Approval
Before starting any WP, approval MUST be recorded.

Start approval evidence can be short:
```yaml
evidence: "Reviewed the WP scope, tasks, rollback, and blockers; OK to start."
```

## Changed WP Approval
If a WP changes materially after approval, execution MUST stop.

Required action:
1. Mark todo status as `blocked`.
2. Add blocker: `Needs renewed approval due to WP change`.
3. Record what changed.
4. Request approval with evidence.
5. Resume only after approval record is complete.

## Approval Step Evidence
For human verification tasks, evidence must describe observed behavior, verifying details documented in the package's `handover.md` (e.g., matching the listed behavioral changes).

Good:
```text
I opened the live app, changed a status to Agent Lead, refreshed, and saw the purple badge persist (matching the behavioral change in handover.md).
```

Bad:
```text
Looks good.
```

## Blocker Rule
Missing approval evidence is a blocker for both human and AI.

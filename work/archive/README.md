# Archived Work Compaction Guide

To minimize token cost and context bloat, completed or archived work items across all levels (Initiative, Increment, Work Package) must be compacted into high-density reference blocks.

## Retention Priorities
1. **Decisions**: Architectural, structural, and schema designs (from Blueprints).
2. **Contracts**: APIs, data models, interface changes.
3. **Net Changes**: Final files modified, verification commands, and system behavior.
4. *Discard*: Onboarding files, step-by-step logs, intermediate checklists, and boilerplate tasks.

## Compact Representation Structure

```yaml
# Archived Initiative/Increment/WP Summary (Token-Efficient Format)
id: [ID]
type: [init|incr|wp]
status: archived
scope: [1-sentence goal]
decisions:
  - [Decision detail & reason]
impact:
  files:
    - [path]
  behavior:
    - [Net behavioral change]
verify: [Key validation command/check]
```

## Compilation Rules
- **Consolidate**: Merge child Work Packages into their parent Increment summary upon completion.
- **Prune**: Delete the original work item directories once their summaries are compiled into this archive index.


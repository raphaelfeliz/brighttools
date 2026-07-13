# Work SOP Entry Point

## Purpose
This folder defines a project-agnostic execution-management system for humans and AI agents.

This folder is the portable scaffold export of the authored PM-2 work docs in `C:\code\PM-2\Docs\work\`. Keep only target-project rules, templates, and examples here.

## Canonical Read Order
1. `README.md`
2. `SPEC.md`
3. `CHECKLIST.md`
4. `APPROVALS.md`
5. relevant template under `templates/`

## Core Model
```text
work/
  seeds/
  templates/
  examples/
  archive/
  01-init-<slug>/
    onboarding.md
    blueprint.md
    01-incr-<slug>/
      onboarding.md
      blueprint.md
      handover.md
      01-wp-<slug>/
        todo.md
        handover.md
        evidence/
          logs/
            001.yaml
```

## Hard Rules
- `system/` contains actual code.
- `docs/` contains documentation.
- `work/` contains execution state.
- Raw ideas go to `work/seeds/`.
- Work item dirs use ordered IDs.
- A WP starts only after approval evidence exists, `evidence/logs/` is initialized, and parent onboarding/blueprint files are initialized.
- A WP completes only after `evidence/logs/` contains append-only step files, `handover.md` is populated (files changed, commands run, behavioral changes), and parent handovers are updated.
- A changed WP requires renewed approval evidence before continuing.
- Human approval must include evidence, not just the approval phrase, and verify the behavioral changes in `handover.md`.

## Approval Phrase
The default approval phrase is:
```text
raphael approved
```

The phrase alone is never sufficient for approval steps. Approval must include evidence.

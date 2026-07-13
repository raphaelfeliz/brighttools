# CHECKLIST: Work Compliance

## Root
- [ ] Code is under `system/`.
- [ ] Docs are under `docs/`.
- [ ] Work state is under `work/`.

## Structure
- [ ] Work item dirs use ordered IDs.
- [ ] Every work item has `meta.yaml`.
- [ ] Parent levels have initialized `onboarding.md` and `blueprint.md`.
- [ ] Every WP has `todo.md` and `handover.md`.
- [ ] Every WP has `evidence/logs/` directory initialized.
- [ ] Every WP has `evidence/`.
- [ ] No standalone task files exist.

## Metadata
- [ ] `meta.id` equals directory name.
- [ ] `meta.parent` equals parent ID.
- [ ] Dependencies and blockers reference existing IDs.

## Approval
- [ ] WP start approval exists.
- [ ] Approval phrase is present where required.
- [ ] Approval evidence is present.
- [ ] Changed WPs have renewed approval.
- [ ] Missing approval evidence is marked blocked.

## Risk
- [ ] Risky mutations have rollback.
- [ ] Verification follows mutation.
- [ ] Human approval follows verification when required.

## Done
- [ ] Tasks complete.
- [ ] `evidence/logs/` is populated with append-only step YAML files detailing execution history.
- [ ] `handover.md` is populated (files, commands, behavioral changes) and parent level handovers updated.
- [ ] Evidence referenced and linked in `handover.md`.
- [ ] Deviations documented.
- [ ] Handover current.
- [ ] "Abstract, don't duplicate" redundancy rule is followed.

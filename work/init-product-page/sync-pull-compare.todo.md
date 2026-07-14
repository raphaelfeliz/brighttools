# Todo: Sync with Live Theme and Compare against Previous Commit

## Status
owner: Antigravity
status: planned
updated: 2026-07-14

## Scope
Execute the sync-pull-compare protocol:
1. Pull live theme files into a temporary `worktrees/pull` directory.
2. Compare the pulled state in `worktrees/pull` against the previous git commit (`HEAD~1` or specific revision before the current pull) to identify remote changes.
3. Separate and present changes into:
   - Code files (liquid templates, css, js) with a detailed diff.
   - Editor changes (JSON templates configuration, styles, parameters, text content).
4. Await human approval before merging.
5. Once approved, merge into `worktrees/main`, update registries, commit changes, and push to GitHub.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User authorized starting the theme sync and comparison."
  date: 2026-07-14

## Tasks
- [x] 01. Create temporary directory `C:\code\BrightTools\worktrees\pull` if it does not exist. [agent: Antigravity] [blocks: 02] [blocked_by: none]
- [x] 02. Pull remote theme files from staging (#180366573842) into `worktrees/pull`. [agent: Antigravity] [blocks: 03] [blocked_by: 01]
- [x] 03. Compare `worktrees/pull` against the previous commit (`HEAD~1` or `1c25eb5` where our local changes are committed). [agent: Antigravity] [blocks: 04] [blocked_by: 02]
- [x] 04. Present a detailed code diff and a brief summary of editor configuration changes to the user for approval. [agent: Antigravity] [blocks: 05] [blocked_by: 03]
- [x] 05. Merge approved changes from `worktrees/pull` to `worktrees/main`. [agent: Antigravity] [blocks: 06] [blocked_by: 04]
- [x] 06. Run registry sync scripts to update local documentation/registries. [agent: Antigravity] [blocks: 07] [blocked_by: 05]
- [x] 07. Delete temporary `worktrees/pull` folder. [agent: Antigravity] [blocks: 08] [blocked_by: 06]
- [ ] 08. Commit merged changes and push to GitHub. [agent: Antigravity] [blocks: none] [blocked_by: 07]

## Rollback
- trigger: Merge conflict or layout breakage.
- steps: Revert modifications to `worktrees/main` using Git.
- verify: Ensure local repository status is clean.

## Blockers
- None

## Evidence
- None

## Handover
- [ ] Create/update handover.md
- next: Push merged codebase to GitHub repository.
- risks: None

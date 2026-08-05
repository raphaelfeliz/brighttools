# Todo: Sync Pull from Shopify

## Status
owner: Antigravity
status: completed
updated: 2026-07-13

## Scope
Execute the pull-compare-merge protocol to fetch remote changes from Shopify, identify all changes, present them to the user for design/code approval, merge approved changes into `worktrees/main`, update registries, and clean up temporary paths.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User authorized starting the pull-compare-merge protocol."
  date: 2026-07-13

## Tasks
- [x] 01. Create temporary directory `C:\code\BrightTools\worktrees\pull` if it does not exist. [agent: Antigravity] [blocks: 02] [blocked_by: none]
- [x] 02. Pull remote theme files from staging (#180366573842) into the `worktrees/pull` folder. [agent: Antigravity] [blocks: 03] [blocked_by: 01]
- [x] 03. Compare `worktrees/pull` with `worktrees/main` to identify diffs (new templates, JSON changes, and liquid/asset code changes). [agent: Antigravity] [blocks: 04] [blocked_by: 02]
- [x] 04. Present the analysis summary to the user for review and explicit approval of code/styling changes. [agent: Antigravity] [blocks: 05] [blocked_by: 03]
- [x] 05. Merge approved changes from `worktrees/pull` to `worktrees/main`. [agent: Antigravity] [blocks: 06] [blocked_by: 04]
- [x] 06. Run registry sync scripts to update local documentation/registries. [agent: Antigravity] [blocks: 07] [blocked_by: 05]
- [x] 07. Delete temporary `worktrees/pull` folder. [agent: Antigravity] [blocks: none] [blocked_by: 06]

## Rollback
- trigger: Layout or configuration corrupted during merge.
- steps: Revert modifications to `worktrees/main` from Git.
- verify: Ensure local working directory is clean and compile/runs correctly.

## Blockers
- None

## Evidence
- None

## Handover
- [x] Create/update handover.md
- next: Commit merged changes to Git.
- risks: None

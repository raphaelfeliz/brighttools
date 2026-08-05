# Todo: Sync Shopify Editor Changes

## Status
owner: Antigravity
status: completed
updated: 2026-07-13

## Scope
Pull the latest theme state from staging, compare against local `worktrees/main`, halt if there are any code/script/style changes, and auto-merge content-only changes (JSON config/templates) if no code changes exist.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User authorized syncing and comparing editor content changes."
  date: 2026-07-13

## Tasks
- [x] 01. Pre-create the temporary folder [worktrees/pull](file:///C:/code/BrightTools/worktrees/pull) (removing any existing folder first). [agent: Antigravity] [blocks: 02] [blocked_by: none]
- [x] 02. Pull the staging theme contents into the temporary pull folder using: `shopify theme pull --theme 180366573842 --path C:\code\BrightTools\worktrees\pull --store brighttools-au.myshopify.com`. [agent: Antigravity] [blocks: 03] [blocked_by: 01]
- [x] 03. Compare [worktrees/pull](file:///C:/code/BrightTools/worktrees/pull) against [worktrees/main](file:///C:/code/BrightTools/worktrees/main) to identify differences. Specifically distinguish between:
  - Code changes (assets, liquid files, scripts, stylesheets).
  - Content changes (JSON templates, config files). [agent: Antigravity] [blocks: 04] [blocked_by: 02]
- [x] 04. Check if there are any differences on code, scripts, or styles. If there are, HALT and report to user. Otherwise, proceed with merging the content-only changes (JSON files) into [worktrees/main](file:///C:/code/BrightTools/worktrees/main). [agent: Antigravity] [blocks: 05] [blocked_by: 03]
- [x] 05. Run the custom templates summary and sections registry sync scripts:
  - `python scripts/generate_custom_templates_summary.py` (if applicable)
  - `python scripts/generate_sections_registry.py` (if applicable) [agent: Antigravity] [blocks: 06] [blocked_by: 04]
- [x] 06. Clean up by deleting the temporary [worktrees/pull](file:///C:/code/BrightTools/worktrees/pull) directory. [agent: Antigravity] [blocks: 07] [blocked_by: 05]
- [x] 07. Verify git status and changes in main worktree. [agent: Antigravity] [blocks: 08] [blocked_by: 06]
- [x] 08. Approve the content sync (human gate approval). Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 07]

## Rollback
- trigger: Sync introduces invalid template structures or content errors.
- steps: Discard changes in [worktrees/main](file:///C:/code/BrightTools/worktrees/main) using git restore/checkout.
- verify: Ensure local repository returns to the previous clean git commit head state.

## Blockers
- None

## Evidence
- None

## Handover
- [x] Create/update handover.md
- next: Commit changes to Git now that content changes are synced.
- risks: None

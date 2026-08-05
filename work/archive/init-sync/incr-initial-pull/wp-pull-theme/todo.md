# Pull Theme from Shopify

## Status
owner: self
status: completed
updated: 2026-07-13

## Scope
Pull the active staging Shopify theme code into worktrees/main.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User authorized via asdf secret code."
  date: 2026-07-13

## Tasks
- [x] 01. Pull staging theme (ID 180366573842) from brighttools-au.myshopify.com to C:\code\BrightTools\worktrees\main. [agent: self] [blocks: none] [blocked_by: none]
- [x] 02. Verify result. [agent: self] [blocks: none] [blocked_by: 01]

## Rollback
- trigger: Pull command fails or results in corrupted folder structure.
- steps: Delete worktrees/main contents and retry.
- verify: Check that directory is empty or returns to initial state.

## Blockers
- None

## Evidence
- [001-pull.yaml](file:///c:/code/BrightTools/work/init-sync/incr-initial-pull/wp-pull-theme/evidence/logs/001-pull.yaml)

## Handover
- [x] Create/update handover.md
- next: Initialize git tracking for the local repository
- risks: None

## Deviations
- None

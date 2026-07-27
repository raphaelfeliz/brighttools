# TODO: Live Theme Sync & Diff Review (July 26)

## Status: Completed

- [x] **Step 1: Local Git Baseline**
  - [x] Inspect git status in `C:\code\BrightTools`.
  - [x] Commit any pending uncommitted changes to `main` branch to guarantee a clean baseline.

- [x] **Step 2: Pull Live Theme Content**
  - [x] Run PowerShell path configuration if needed.
  - [x] Execute `shopify theme pull --theme 180366573842 --path C:\code\BrightTools\worktrees\pull --store brighttools-au.myshopify.com`.

- [x] **Step 3: Analyze & Compare Differences**
  - [x] Diff contents of `worktrees/pull` against `worktrees/main`.
  - [x] Categorize diffs into:
    - Editor / JSON / Content changes (Recommend approval).
    - Code / Liquid / JS / CSS changes (Alert and flag for review).

- [x] **Step 4: Present Review & Update Handover Document**
  - [x] Present categorized summary on chat for user decisions.
  - [x] Document all observed changes and approved items into [july26-sync.handover.md](file:///C:/code/BrightTools/work/july26-sync/july26-sync.handover.md).

- [x] **Step 5: Apply Approved Merges & Clean Up**
  - [x] Merge approved files from `worktrees/pull` to `worktrees/main`.
  - [x] Retain `worktrees/pull` per user instruction.


# TODO: Live Theme Sync & Diff Review (July 26)

## Status: In Progress

- [ ] **Step 1: Local Git Baseline**
  - [ ] Inspect git status in `C:\code\BrightTools`.
  - [ ] Commit any pending uncommitted changes to `main` branch to guarantee a clean baseline.

- [ ] **Step 2: Pull Live Theme Content**
  - [ ] Run PowerShell path configuration if needed.
  - [ ] Execute `shopify theme pull --theme 180366573842 --path C:\code\BrightTools\worktrees\pull --store brighttools-au.myshopify.com`.

- [ ] **Step 3: Analyze & Compare Differences**
  - [ ] Diff contents of `worktrees/pull` against `worktrees/main`.
  - [ ] Categorize diffs into:
    - Editor / JSON / Content changes (Recommend approval).
    - Code / Liquid / JS / CSS changes (Alert and flag for review).

- [ ] **Step 4: Present Review & Update Handover Document**
  - [ ] Present categorized summary on chat for user decisions.
  - [ ] Document all observed changes and approved items into [july26-sync.handover.md](file:///C:/code/BrightTools/work/july26-sync/july26-sync.handover.md).

- [ ] **Step 5: Apply Approved Merges & Clean Up**
  - [ ] Merge approved files from `worktrees/pull` to `worktrees/main`.
  - [ ] Remove temporary directory `worktrees/pull`.

# TODO: Live Theme Sync & Diff Review (July 27)

## Status: Completed

- [x] **Step 1: Local Git Baseline Verification**
  - [x] Check `git status` in `C:\code\BrightTools` (ensure working tree is clean).
  - [x] Log baseline commit hash (`bbb47dc`).

- [x] **Step 2: Pull Live Theme Content**
  - [x] Ensure target workspace directory `C:\code\BrightTools\worktrees\pull` exists.
  - [x] Execute `shopify theme pull --theme 180366573842 --path C:\code\BrightTools\worktrees\pull --store brighttools-au.myshopify.com`.

- [x] **Step 3: Analyze & Categorize Differences**
  - [x] Compare `worktrees/pull` against `worktrees/main` using `git diff --no-index --name-status`.
  - [x] Categorize diffs into:
    - **Shopify Customizer / JSON Templates**: Recommend direct merge.
    - **Code Files (Liquid / JS / CSS)**: Alert and present code diffs for user review.

- [x] **Step 4: Present Review & Update Handover Document**
  - [x] Present categorized diff summary on chat for user approval.
  - [x] Create/update [july27-sync.handover.md](file:///C:/code/BrightTools/work/july27-sync/july27-sync.handover.md) with observed differences.

- [x] **Step 5: Apply Approved Merges & Log Execution**
  - [x] Apply approved changes into `worktrees/main`.
  - [x] Maintain `worktrees/pull` per workspace SOP.
  - [x] Log all actions and SOP observations into [july27-sync.log.md](file:///C:/code/BrightTools/work/july27-sync/july27-sync.log.md).


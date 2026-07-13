# Yellow Review Stars

## Status
owner: Antigravity
status: in_progress
updated: 2026-07-13

## Scope
Change the color of the product review stars (both Judge.me widgets and custom fallback/mock stars) from red to yellow using the native theme editor's color token (`--star-color`).

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User authorized yellow review stars implementation."
  date: 2026-07-13

## Tasks
- [x] 01. Update Judge.me rating stars override in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L853-L857) from `color: var(--mar26-clr-red) !important;` to `color: rgb(var(--star-color)) !important;`. [agent: Antigravity] [blocks: 04] [blocked_by: none]
- [x] 02. Update catalogv Judge.me rating stars override in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L1124-L1128) from `color: var(--mar26-clr-red) !important;` to `color: rgb(var(--star-color)) !important;`. [agent: Antigravity] [blocks: 04] [blocked_by: none]
- [x] 03. Update fallback mock stars color in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L1139-L1144) from `color: var(--mar26-clr-red);` to `color: rgb(var(--star-color));`. [agent: Antigravity] [blocks: 04] [blocked_by: none]
- [x] 04. Push modified stylesheet to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only assets/mar26-foundation.css.liquid --allow-live`. [agent: Antigravity] [blocks: 05] [blocked_by: 01, 02, 03]
- [ ] 05. Verify in browser/editor that the product reviews stars are yellow instead of red. [agent: Raphael] [blocks: 06] [blocked_by: 04]
- [ ] 06. Approve the color change in the browser (human gate approval). Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 05]

## Rollback
- trigger: Star styles broken or customer requests reverting to red stars.
- steps: Revert modifications in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid) and push the reverted file to staging.
- verify: Confirm stars display in red in the browser.

## Blockers
- None

## Evidence
- None

## Handover
- [ ] Create/update handover.md
- next: Commit changes to Git now that design approval has been received.
- risks: None

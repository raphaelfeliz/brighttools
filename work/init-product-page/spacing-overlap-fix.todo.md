# Spacing Overlap Fix: Main Product Section

## Status
owner: Antigravity
status: completed
updated: 2026-07-13

## Scope
Increase the bottom margin of the buy-buttons block inside the main product section to resolve the overlap of the absolute-positioned "More payment options" link onto the subsequent video section.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User authorized increasing spacing to prevent section overlap."
  date: 2026-07-13

## Tasks
- [x] 01. Update the style block in [mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid#L191-L195) to set `margin-bottom: 30px !important;` on the buy-buttons blocks, and bump the section version to 1.5.9. [agent: Antigravity] [blocks: 02] [blocked_by: none]
- [x] 02. Push modified file to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only sections/mar26-main-product.liquid --allow-live`. [agent: Antigravity] [blocks: 03] [blocked_by: 01]
- [x] 03. Verify in browser/editor that the "More payment options" link no longer overlaps the video section on both desktop and mobile layouts. [agent: Raphael] [blocks: 04] [blocked_by: 02]
- [x] 04. Approve the layout spacing change in the browser (human gate approval). Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 03]

## Rollback
- trigger: Layout spacing excessive or breaks design alignment.
- steps: Revert modifications in [mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid) and push the reverted file to staging.
- verify: Confirm the button margin returns to the previous state.

## Blockers
- None

## Evidence
- None

## Handover
- [x] Create/update handover.md
- next: Commit changes to Git now that spacing fix is verified.
- risks: None

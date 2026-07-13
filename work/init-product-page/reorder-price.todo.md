# Reorder Price on Product Page

## Status
owner: Antigravity
status: completed
updated: 2026-07-13

## Scope
Reorder the product price block so that it displays directly below the title and above the reviews badge on both desktop and mobile layouts for the brooms template.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User authorized price reordering implementation."
  date: 2026-07-13

## Tasks
- [x] 01. Modify the `block_order` array in [product.bt-brooms.json](file:///C:/code/BrightTools/worktrees/main/templates/product.bt-brooms.json) to place `price` below `mar26_title_and_tags_5z3hZR` and above `judge_me_reviews_preview_badge_kG7NLt`. [agent: Antigravity] [blocks: 03] [blocked_by: none]
- [x] 02. Swap the mobile CSS order values in [mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid) so that `price` gets `order: 2 !important` and `@app`/`rating` get `order: 3 !important`. [agent: Antigravity] [blocks: 03] [blocked_by: none]
- [x] 03. Push the modified files to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only templates/product.bt-brooms.json --only sections/mar26-main-product.liquid --allow-live`. [agent: Antigravity] [blocks: 04] [blocked_by: 01, 02]
- [x] 04. Verify in the browser/editor that the price renders below the title and above the review stars on both desktop and mobile views. [agent: Raphael] [blocks: 05] [blocked_by: 03]
- [x] 05. Approve the layout change in the browser (human gate approval). Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 04]

## Rollback
- trigger: Layout misalignment or user rejection of the new block order.
- steps: Revert modifications to the json template and liquid section, and push reverted files to staging.
- verify: Confirm the layout returns to the previous block order in the browser.

## Blockers
- Needs start approval with evidence.

## Evidence
- None

## Handover
- [x] Create/update handover.md
- next: Commit changes to Git now that design approval has been received.
- risks: None

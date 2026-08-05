# Todo: Desktop Title Typography Adjustments

## Status
owner: 2703a6a2-1341-44fd-a732-82cec0707bca
status: completed
updated: 2026-07-14

## Scope
Adjust the product title typography on desktop (min-width: 1000px) and mobile:
- Reduce the product title font-size to exactly 34px on desktop (10% reduction from 38px).
- Reduce the product title font-weight to 600 (semi-bold) on desktop.
- Reduce the product title font-size by 10% on mobile using a 0.9 multiplier.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User approved reducing product title font size by 10% on desktop and mobile."
  date: 2026-07-14

## Tasks
- [x] 01. Update `.product-info__title` style rules in `mar26-main-product.liquid` under desktop (min-width: 1000px) and mobile (max-width: 999px) queries. Bump section version to 1.7.3. [agent: 2703a6a2-1341-44fd-a732-82cec0707bca] [blocks: 02] [blocked_by: none]
- [x] 02. Push modified file to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only sections/mar26-main-product.liquid --allow-live`. [agent: 2703a6a2-1341-44fd-a732-82cec0707bca] [blocks: 03] [blocked_by: 01]
- [x] 03. Verify in desktop view that the product title font size is 34px and weight is 600, and that mobile font size is reduced by 10%. [agent: Raphael] [blocks: 04] [blocked_by: 02]
- [x] 04. Approve the title typography changes in the browser (human gate approval). Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 03]

## Rollback
- trigger: Title text is too small, hard to read, or alignment breaks.
- steps: Revert modifications in `mar26-main-product.liquid` and push the reverted file to staging.
- verify: Confirm the title returns to original sizing.

## Blockers
- None

## Evidence
- None

## Handover
- [x] Create `title-font-adjustments.handover.md` at the end.
- [x] Move `title-font-adjustments.todo.md` to `complete\` after git commit.
- next: Commit changes to Git now that desktop title typography is approved.
- risks: None

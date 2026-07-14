# Todo: Desktop Column Gap Adjustment

## Status
owner: 2703a6a2-1341-44fd-a732-82cec0707bca
status: completed
updated: 2026-07-14

## Scope
Increase the horizontal gap between the product gallery column and the product info column on desktop only:
- Set desktop `column-gap` to 60px on `.product` wrapper.
- Preserve mobile spacing and layout.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User approved increasing desktop column gap between gallery and info columns."
  date: 2026-07-14

## Tasks
- [x] 01. Update `.product` style rules in `mar26-main-product.liquid` under the desktop media query (`min-width: 1000px`) to set `column-gap: 60px !important;` and `row-gap: 0.875rem !important;` (instead of a single `gap: 0.875rem !important;`). Bump section version to 1.6.8. [agent: 2703a6a2-1341-44fd-a732-82cec0707bca] [blocks: 02] [blocked_by: none]
- [x] 02. Push modified file to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only sections/mar26-main-product.liquid --allow-live`. [agent: 2703a6a2-1341-44fd-a732-82cec0707bca] [blocks: 03] [blocked_by: 01]
- [x] 03. Verify in desktop view that the gap between the image gallery and the product details column is visually increased to 60px, and that mobile remains unaffected. [agent: Raphael] [blocks: 04] [blocked_by: 02]
- [x] 04. Approve the desktop column gap changes in the browser (human gate approval). Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 03]

## Rollback
- trigger: Column gap is too wide or breaks desktop side-by-side alignment.
- steps: Revert column-gap modifications in `mar26-main-product.liquid` and push to staging.
- verify: Confirm the gap returns to original styling.

## Blockers
- None

## Evidence
- None

## Handover
- [x] Create `column-gap-fix.handover.md` at the end.
- [x] Move `column-gap-fix.todo.md` to `complete\` after git commit.
- next: Commit changes to Git now that desktop column gap is approved.
- risks: None

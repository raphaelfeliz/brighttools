# Yellow Review Stars - Global Overrides

## Status
owner: Antigravity
status: completed
updated: 2026-07-13

## Scope
Apply global CSS overrides to ensure product review stars (both Judge.me widgets and custom fallback/mock stars) render in yellow using the native theme editor's color token (`--star-color`) across all pages, including the product detail page app block.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User authorized global yellow review stars implementation and version bumps."
  date: 2026-07-13

## Tasks
- [x] 01. Add global Judge.me star color overrides to [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L841-L846) targeting `.jdgm-star` and `--jdgm-star-color` with `rgb(var(--star-color))`. [agent: Antigravity] [blocks: 03] [blocked_by: none]
- [x] 02. Ensure fallback mock stars also use `rgb(var(--star-color))` in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L1139-L1144). [agent: Antigravity] [blocks: 03] [blocked_by: none]
- [x] 03. Push modified files to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only assets/mar26-foundation.css.liquid --only sections/mar26-main-product.liquid --allow-live`. [agent: Antigravity] [blocks: 04] [blocked_by: 01, 02]
- [x] 04. Verify in browser/editor that the reviews stars are yellow on both catalog grid pages and the product detail page. [agent: Raphael] [blocks: 05] [blocked_by: 03]
- [x] 05. Approve the color change in the browser (human gate approval). Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 04]

## Rollback
- trigger: Star styles broken or customer requests reverting to red stars.
- steps: Revert modifications in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid) and push the reverted file to staging.
- verify: Confirm stars display in red in the browser.

## Blockers
- Needs start approval with evidence (secret "asdf").

## Evidence
- None

## Handover
- [x] Create/update handover.md
- next: Commit changes to Git now that design approval has been received.
- risks: None

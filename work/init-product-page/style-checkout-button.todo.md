# Style Add to Cart Button like Accelerated Checkout

## Status
owner: Antigravity
status: completed
updated: 2026-07-13

## Scope
Apply custom scoped overrides in the foundation stylesheet to style the primary Add to Cart button exactly like the dynamic accelerated checkout button (height: 55px, border-radius: 3.75rem, font-size: 20px, font-weight: 500, Montserrat font-family, center alignment), keeping its existing colors.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User authorized styling the primary checkout button like accelerated checkout."
  date: 2026-07-13

## Tasks
- [x] 01. Add CSS overrides to [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L280-L283) and update the style block in [mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid#L170-L177) to use `border-radius: 3.75rem !important;` to match the accelerated checkout button, and bump the stylesheet version to 0.8.9 and section version to 1.5.7. [agent: Antigravity] [blocks: 02] [blocked_by: none]
- [x] 01.1. Add `border: none !important;` and `box-shadow: none !important;` to [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid) and [mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid) to eliminate the thin outline, and bump stylesheet to 0.8.10 and section to 1.5.8. [agent: Antigravity] [blocks: 02] [blocked_by: none]
- [x] 02. Push modified files to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only assets/mar26-foundation.css.liquid --only sections/mar26-main-product.liquid --allow-live`. [agent: Antigravity] [blocks: 03] [blocked_by: 01]
- [x] 03. Verify in browser/editor that the primary Add to Cart button is styled as a pill matching the Shop Pay button in height, border-radius, font-family, and alignment, without any thin outlines. [agent: Raphael] [blocks: 04] [blocked_by: 02]
- [x] 04. Approve the layout styling change in the browser (human gate approval). Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 03]

## Rollback
- trigger: Styles misaligned or user rejects the new button style.
- steps: Revert modifications in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid) and push the reverted file to staging.
- verify: Confirm the button styling returns to original theme settings values.

## Blockers
- None

## Evidence
- None

## Handover
- [x] Create/update handover.md
- next: Commit changes to Git now that design approval has been received.
- risks: None

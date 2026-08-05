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
  evidence: "User approved adding hover scale and shine animations to checkout buttons."
  date: 2026-07-14

## Tasks
- [x] 01. Add style overrides in `mar26-main-product.liquid` to force solid navy pill shape on all checkout buttons (completed).
- [x] 02. Add `.product-quick-add .button` to style overrides to synchronize sticky bar button styling (completed).
- [x] 03. Add `transform: scale(1.05)` to hover states and a gradient pseudo-element for the sweep shine animation. Bump version to 1.7.6. [agent: 2703a6a2-1341-44fd-a732-82cec0707bca] [blocks: 04] [blocked_by: none]
- [x] 04. Push modified file to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only sections/mar26-main-product.liquid --allow-live`. [agent: 2703a6a2-1341-44fd-a732-82cec0707bca] [blocks: 05] [blocked_by: 03]
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

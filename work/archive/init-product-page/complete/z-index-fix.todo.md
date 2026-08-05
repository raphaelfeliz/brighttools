# Todo: Fix Sticky Add-to-Cart and Section z-index Overlaps

## Status
owner: Antigravity
status: completed
updated: 2026-07-14

## Scope
Harden the z-index stacking levels by reducing top-level custom section containers to `z-index: 1` and elevating the floating quick-add bar to `z-index: 100 !important` inside foundations. Pushing changes to Shopify staging and verifying visual correctness on desktop/mobile scroll layouts.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User approved the z-index overlaps implementation plan."
  date: 2026-07-14

## Tasks
- [x] 01. Modify [mar26-testimonials.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-testimonials.liquid#L21) to set `.mar26-revolution-sec` to `z-index: 1;`. [agent: Antigravity] [blocks: 05] [blocked_by: none]
- [x] 02. Modify [mar26-bestsellerpage-included-grid.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-bestsellerpage-included-grid.liquid#L12) to set `.mar26-included-wrapper` to `z-index: 1;`. [agent: Antigravity] [blocks: 05] [blocked_by: none]
- [x] 03. Modify [mar26-panorama-slices.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-panorama-slices.liquid#L20) to set `.panorama-slices-wrapper` to `z-index: 1;`. [agent: Antigravity] [blocks: 05] [blocked_by: none]
- [x] 04. Modify [mar26-main-special-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-special-product.liquid#L51) to set `.mar26-hero-grid` to `z-index: 1;`. [agent: Antigravity] [blocks: 05] [blocked_by: none]
- [x] 05. Add z-index override rule `.product-quick-add { z-index: 100 !important; }` in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid). [agent: Antigravity] [blocks: 06] [blocked_by: 01, 02, 03, 04]
- [x] 06. Push modified files to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only sections/mar26-testimonials.liquid --only sections/mar26-bestsellerpage-included-grid.liquid --only sections/mar26-panorama-slices.liquid --only sections/mar26-main-special-product.liquid --only assets/mar26-foundation.css.liquid --allow-live`. [agent: Antigravity] [blocks: 07] [blocked_by: 05]
- [x] 07. Verify in the browser/editor that the floating quick add bar and sticky header overlay all page content sections and the footer correctly. [agent: Raphael] [blocks: 08] [blocked_by: 06]
- [x] 08. Approve the z-index changes in the browser (human gate approval). Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 07]

## Rollback
- trigger: Layout or layering broken on sections.
- steps: Revert modifications to sections and foundation files, and push reverted files to staging.
- verify: Confirm the layout returns to original styling.

## Blockers
- None

## Evidence
- None

## Handover
- [x] Create/update handover.md
- next: Commit changes to Git.
- risks: None

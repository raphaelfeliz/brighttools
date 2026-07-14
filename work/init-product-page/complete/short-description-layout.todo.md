# Todo: Short Description Layout Refinement

## Status
owner: 5abf69b2-6741-4d06-b8ec-709e8e4dee82
status: completed
updated: 2026-07-13

## Scope
Adjust short description card sizing:
- Desktop: Fit-content width (just wide enough to fit each item in 1 line).
- Mobile: Full width (no outer margin or block item padding), height shrink-wrapped to elements.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User authorized fit-content width on desktop and full-width/zero-outer-spacing on mobile for short description card."
  date: 2026-07-13

## Tasks
- [x] 01. Modify [mar26-short-description.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/mar26-short-description.liquid#L26-L35) to set `width: fit-content; max-width: 100%;` on `.mar26-short-description-card` for desktop layout. [agent: 5abf69b2-6741-4d06-b8ec-709e8e4dee82] [blocks: 03] [blocked_by: none]
- [x] 02. Update mobile styles in [mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid#L320-L360) to set the short description block item padding to `0 !important`, the card's `margin-left` and `margin-right` to `0 !important`, card `border-radius` to `0 !important`, and keep internal padding (e.g. `12px 16px`) so text doesn't bleed. Bump section version to 1.6.3 and snippet version to 0.0.13. [agent: 5abf69b2-6741-4d06-b8ec-709e8e4dee82] [blocks: 03] [blocked_by: none]
- [x] 03. Push modified files to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only snippets/mar26-short-description.liquid --only sections/mar26-main-product.liquid --allow-live`. [agent: 5abf69b2-6741-4d06-b8ec-709e8e4dee82] [blocks: 04] [blocked_by: 01, 02]
- [x] 04. Verify in browser/editor that the card is fit-content on desktop and edge-to-edge on mobile with proper internal padding. [agent: Raphael] [blocks: 05] [blocked_by: 03]
- [x] 05. Approve the layout refinement in the browser. Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 04]

## Rollback
- trigger: Layout sizing looks broken.
- steps: Revert modifications in snippets and sections and push reverted files to staging.
- verify: Confirm elements return to their previous styling.

## Blockers
- None

## Evidence
- None

## Handover
- [x] Create/update handover.md
- next: Commit changes to Git now that layout is approved.
- risks: None

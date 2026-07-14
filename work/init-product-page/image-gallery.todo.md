# Todo: Image Gallery Layout

## Status
owner: 2703a6a2-1341-44fd-a732-82cec0707bca
status: in_progress
updated: 2026-07-14

## Scope
Adjust image gallery layout:
- Make the main product images strictly square (1:1 aspect ratio) on desktop, sized around 500px (responsive, max 650px).
- Add a light grey outline to the main image container.
- Move thumbnails to the left side of the main image on desktop (if there is space, otherwise fallback to displaying them below).
- Fix page padding on desktop by centering and constraining the product container to match standard page padding.
- Ensure mobile layout remains unchanged from its current state.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User approved changing image gallery to square (500px-650px), lightgrey outline, left-aligned thumbnails, and fixing page padding."
  date: 2026-07-14

## Tasks
- [x] 01. Update gallery layout styling in `mar26-product-gallery.liquid` to constrain main image size (500px-650px) and add page padding/margins on desktop in `mar26-main-product.liquid`. Bump relevant versions. [agent: 2703a6a2-1341-44fd-a732-82cec0707bca] [blocks: 02] [blocked_by: none]
- [x] 02. Push modified files to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only snippets/mar26-product-gallery.liquid --only sections/mar26-main-product.liquid --only templates/product.bt-brooms.json --allow-live`. [agent: 2703a6a2-1341-44fd-a732-82cec0707bca] [blocks: 03] [blocked_by: 01]
- [ ] 03. Verify in desktop view that the main image is square with a grey outline, thumbnails are on the left, and mobile view remains unchanged. [agent: Raphael] [blocks: 04] [blocked_by: 02]
- [ ] 04. Approve the image gallery layout changes in the browser (human gate approval). Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 03]

## Rollback
- trigger: Gallery breaks on mobile or desktop layout overlaps awkwardly.
- steps: Revert modifications in snippets/sections/assets and push reverted files to staging.
- verify: Confirm gallery returns to original styling.

## Blockers
- None

## Evidence
- None

## Handover
- [ ] Create `image-gallery.handover.md` at the end.
- [ ] Move `image-gallery.todo.md` to `complete\` after git commit.
- next: Commit changes to Git now that gallery layout is approved.
- risks: None

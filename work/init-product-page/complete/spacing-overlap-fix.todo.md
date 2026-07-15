# Spacing Overlap Fix: Main Product Section

## Status
owner: 2703a6a2-1341-44fd-a732-82cec0707bca
status: completed
updated: 2026-07-14

## Scope
Adjust vertical spacing of the main product section:
- Increase bottom margin of buy buttons (completed).
- Set top and bottom margins/padding of the entire main product section to exactly 60px on desktop, while reducing mobile top padding to exactly 20px.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User approved reducing mobile top spacing between the product section and the header to 20px, keeping desktop margins at 60px."
  date: 2026-07-14

## Tasks
- [x] 01. Update style block in `mar26-main-product.liquid` to set bottom margin of buy buttons to 30px (completed).
- [x] 02. Push modified file to Shopify staging (completed).
- [x] 03. Verify in browser that buy buttons bottom margin resolves overlap (completed).
- [x] 04. Approve the buy button bottom margin spacing change (completed).
- [x] 05. Update style block in `mar26-main-product.liquid` to set `padding-top: 60px !important;` and `padding-bottom: 60px !important;` on `#shopify-section-{{ section.id }} .section` on desktop, and override mobile top padding to `20px !important`. Bump section version to 1.7.4. [agent: 2703a6a2-1341-44fd-a732-82cec0707bca] [blocks: 06] [blocked_by: none]
- [x] 06. Push modified file to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only sections/mar26-main-product.liquid --allow-live`. [agent: 2703a6a2-1341-44fd-a732-82cec0707bca] [blocks: 07] [blocked_by: 05]
- [x] 07. Verify in browser that the top and bottom margins of the main product section are exactly 60px. [agent: Raphael] [blocks: 08] [blocked_by: 06]
- [x] 08. Approve the 60px top/bottom margins in the browser (human gate approval). Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 07]

## Rollback
- trigger: Section spacing is visually incorrect or breaks layout.
- steps: Revert modifications in `mar26-main-product.liquid` and push the reverted file to staging.
- verify: Confirm the section spacing returns to the previous state.

## Blockers
- None

## Evidence
- None

## Handover
- [x] Create/update `spacing-overlap-fix.handover.md` at the end.
- [x] Move `spacing-overlap-fix.todo.md` to `complete\` after git commit.
- next: Commit changes to Git now that spacing fix is verified.
- risks: None

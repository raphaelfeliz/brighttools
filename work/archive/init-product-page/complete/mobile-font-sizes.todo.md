# Todo: Mobile Font Size Adjustments

## Status
owner: 5abf69b2-6741-4d06-b8ec-709e8e4dee82
status: in_progress
updated: 2026-07-13

## Scope
Adjust mobile (max-width: 999px) typography for standard and custom templates:
- Increase product title by 2px (to `calc(var(--text-h1) + 2px)`).
- Reduce short description title and bullet text by 2px (from 20px to 18px).
- Desktop font sizes remain unchanged.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User approved increasing mobile product title by 2px and reducing mobile short description by 2px."
  date: 2026-07-13

## Tasks
- [x] 01. Update mobile style overrides in [mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid#L320-L365) to set mobile `.product-info__title` font-size to `calc(var(--text-h1) + 2px) !important` and mobile `.mar26-short-description-text`, `.mar26-short-description-item` font-size to `18px !important`. Bump section version to 1.6.5. [agent: 5abf69b2-6741-4d06-b8ec-709e8e4dee82] [blocks: 02] [blocked_by: none]
- [x] 02. Push modified files to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only sections/mar26-main-product.liquid --allow-live`. [agent: 5abf69b2-6741-4d06-b8ec-709e8e4dee82] [blocks: 03] [blocked_by: 01]
- [ ] 03. Verify in mobile view/customizer that the title size is increased by 2px and short description card text size is reduced to 18px. [agent: Raphael] [blocks: 04] [blocked_by: 02]
- [ ] 04. Approve the mobile typography changes in the browser (human gate approval). Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 03]

## Rollback
- trigger: Mobile layout text is misaligned or too large/small.
- steps: Revert modifications in sections and push reverted file to staging.
- verify: Confirm mobile typography returns to original styling.

## Blockers
- None

## Evidence
- None

## Handover
- [ ] Create/update handover.md
- next: Commit changes to Git now that mobile font sizes are approved.
- risks: None

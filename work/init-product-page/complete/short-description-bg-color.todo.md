# Todo: Short Description Adjustable Background Color

## Status
owner: 5abf69b2-6741-4d06-b8ec-709e8e4dee82
status: completed
updated: 2026-07-13

## Scope
Add a schema color setting to the short description block allowing background color adjustment via the theme editor, defaulting to `#FFF2CC`.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User authorized adding adjustable background color to short description block (#FFF2CC default)."
  date: 2026-07-13

## Tasks
- [x] 01. Add a color setting `background_color` with default value `#FFF2CC` to the `mar26_short_description` block schema in [mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid#L743-L750). [agent: 5abf69b2-6741-4d06-b8ec-709e8e4dee82] [blocks: 03] [blocked_by: none]
- [x] 02. Modify [mar26-short-description.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/mar26-short-description.liquid#L26-L30) to read the custom background color setting dynamically, defaulting to `#FFF2CC`. [agent: 5abf69b2-6741-4d06-b8ec-709e8e4dee82] [blocks: 03] [blocked_by: none]
- [x] 03. Push modified files to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only snippets/mar26-short-description.liquid --only sections/mar26-main-product.liquid --allow-live`. [agent: 5abf69b2-6741-4d06-b8ec-709e8e4dee82] [blocks: 04] [blocked_by: 01, 02]
- [x] 04. Verify in the Shopify Customizer that the background color can be adjusted and defaults to `#FFF2CC`. [agent: Raphael] [blocks: 05] [blocked_by: 03]
- [x] 05. Approve the layout styling change in the browser (human gate approval). Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 04]

## Rollback
- trigger: Background color breaks layout aesthetics or fails editor parsing.
- steps: Revert modifications in snippets and sections and push reverted files to staging.
- verify: Confirm short description card background returns to original styling.

## Blockers
- None

## Evidence
- None

## Handover
- [x] Create/update handover.md
- next: Commit changes to Git now that background color adjustment is verified.
- risks: None

# Scale Short Description Component to 20px

## Status
owner: Antigravity
status: completed
updated: 2026-07-13

## Scope
Scale up the text font size, checkmark icon dimensions, margins, padding, border-radius, and gaps in the March 2026 short description component to be exactly 20px (1.667x scale) for increased legibility.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User authorized scaling short description component to 20px."
  date: 2026-07-13

## Tasks
- [x] 01. Modify style rules in [mar26-short-description.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/mar26-short-description.liquid) to scale fonts to 20px, icons to 27px/13px, padding/gaps to 13px, and bump version to 0.0.10. [agent: Antigravity] [blocks: 02] [blocked_by: none]
- [x] 02. Push modified snippet to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only snippets/mar26-short-description.liquid --allow-live`. [agent: Antigravity] [blocks: 03] [blocked_by: 01]
- [x] 03. Verify in browser/editor that the short description card renders at 20px scale and looks proportional. [agent: Raphael] [blocks: 04] [blocked_by: 02]
- [x] 04. Approve the layout scaling in the browser (human gate approval). Do not commit to git before this is approved. [agent: Raphael] [blocks: none] [blocked_by: 03]

## Rollback
- trigger: Layout too large or visual degradation.
- steps: Revert modifications in [mar26-short-description.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/mar26-short-description.liquid) and push the reverted file to staging.
- verify: Confirm components return to original scale (12px text).

## Blockers
- None

## Evidence
- None

## Handover
- [x] Create/update handover.md
- next: Commit changes to Git now that design approval has been received.
- risks: None

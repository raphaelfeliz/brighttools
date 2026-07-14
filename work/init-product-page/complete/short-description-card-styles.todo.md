# Todo: Short Description Card Styling and Width Synchronization

## Status
owner: 2703a6a2-1341-44fd-a732-82cec0707bca
status: completed
updated: 2026-07-14

## Scope
Adjust the styling and desktop layout of the short description card:
- Make the grey background slightly lighter (#F8FAFC) and add a 2px light grey outline.
- Darken the font and increase weight (color #0F172A, weights 500/600).
- Align desktop width of the card and buy buttons by setting max-width to 440px.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User approved styling adjustments to short description card and desktop width alignment."
  date: 2026-07-14

## Tasks
- [x] 01. Update card, border, text color, and font-weight styles in `mar26-short-description.liquid`. Bump version to 0.0.15. [agent: 2703a6a2-1341-44fd-a732-82cec0707bca] [blocks: 02] [blocked_by: none]
- [x] 02. Update desktop and mobile buy-buttons style rules in `mar26-main-product.liquid` to sync max-width to 440px on desktop and 100% on mobile. Bump version to 1.7.1. [agent: 2703a6a2-1341-44fd-a732-82cec0707bca] [blocks: 03] [blocked_by: 01]
- [x] 03. Push modified files to Shopify staging using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only snippets/mar26-short-description.liquid --only sections/mar26-main-product.liquid --allow-live`. [agent: 2703a6a2-1341-44fd-a732-82cec0707bca] [blocks: 04] [blocked_by: 02]
- [x] 04. Verify in desktop and mobile viewports that the card background, outline, text weight, and button alignments are correct. [agent: Raphael] [blocks: 05] [blocked_by: 03]
- [x] 05. Approve the short description card adjustments in the browser (human gate approval). [agent: Raphael] [blocks: none] [blocked_by: 04]

## Rollback
- trigger: Styling breaks typography structure or causes layout misalignments.
- steps: Revert modifications in snippets/sections and push to staging.
- verify: Confirm description card and buttons return to original styling.

## Blockers
- None

## Evidence
- None

## Handover
- [x] Create `short-description-card-styles.handover.md` at the end.
- [x] Move `short-description-card-styles.todo.md` to `complete\` after git commit.
- next: Commit changes to Git now that styling and width are approved.
- risks: None

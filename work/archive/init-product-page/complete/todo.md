# Init Product Page Typography

## Status
owner: Antigravity
status: completed
updated: 2026-07-13

## Scope
Harden product title font weight on mar26 product pages by defining a semantic title class in the global foundations stylesheet, applying it to the custom title snippet, pushing changes to Shopify staging, and verifying visual correctness.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User authorized implementation start."
  date: 2026-07-13

## Tasks
- [x] 01. Add `.mar26-product-title` style rule utilizing the Extra Bold weight token in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid). [agent: Antigravity] [blocks: 03] [blocked_by: none]
- [x] 02. Apply the `.mar26-product-title` class to the heading tag in [mar26-title-and-tags.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/mar26-title-and-tags.liquid). [agent: Antigravity] [blocks: 03] [blocked_by: none]
- [x] 03. Push the specific modified files to the Shopify staging theme (#180366573842) using: `shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only assets/mar26-foundation.css.liquid --only snippets/mar26-title-and-tags.liquid`. [agent: Antigravity] [blocks: 04] [blocked_by: 01, 02]
- [x] 04. Verify in the browser/editor that the "Japanese Broom" product title now renders with the Extra Bold (800) font weight. [agent: Raphael] [blocks: 05] [blocked_by: 03]
- [x] 05. Approve the design change in the browser (human gate approval). Do not commit changes to git before this is approved. [agent: Raphael] [blocks: 06] [blocked_by: 04]
- [x] 06. Update [bt-brooms.md](file:///C:/code/BrightTools/docs/documentation/product-pages/bt-brooms.md) design tokens section to document the unified product title styling class. [agent: Antigravity] [blocks: none] [blocked_by: 05]

## Rollback
- trigger: Layout breakage or user rejection of the Extra Bold product title.
- steps: Revert modifications to `mar26-foundation.css.liquid` and `mar26-title-and-tags.liquid`, and push the reverted files to staging.
- verify: Confirm the title returns to standard font weight in the browser.

## Blockers
- None

## Evidence
- [change-title.png](file:///C:/code/BrightTools/work/init-product-page/evidence/change-title.png)

## Handover
- [x] Create/update handover.md
- next: Commit changes to Git now that design approval has been received.
- risks: None

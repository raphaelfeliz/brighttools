# Todo: Recode MAR26 Quantity + Buy Block & Height Alignment

## Status
owner: Antigravity
status: in_progress
updated: 2026-07-26

## Scope
Recode the `mar26_quantity_price` block ("MAR26 Quantity + Buy") in [sections/mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid) and [snippets/mar26-quantity-buy.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/mar26-quantity-buy.liquid):
- Target `[data-block-type="mar26_quantity_price"]` with MAR26 pill CSS rules (`#0F172A`, `border-radius: 3.75rem`, hover scale `1.05`, light sweep `::after`).
- Synchronize height between the quantity selector (`<quantity-selector>`) pill and the buy buttons (`min-height` & padding matching).
- Add block settings schema (`show_payment_button`, `atc_button_background`, `atc_button_text_color`, `payment_button_background`, `payment_button_text_color`) to `mar26_quantity_price` block schema in [sections/mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid).
- Bump version to `1.7.9`.

**Constraint**: Modify ONLY `mar26` and `bt` files (`mar26-main-product.liquid`, `mar26-quantity-buy.liquid`, docs/work). DO NOT touch core theme files. DO NOT COMMIT to Git without explicit human approval.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User approved implementation approach plan and requested work tracking setup."
  date: 2026-07-26

## Tasks
- [x] 01. Research & Planning: Analyze `mar26_quantity_price` block markup in [snippets/mar26-quantity-buy.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/mar26-quantity-buy.liquid) and CSS in [sections/mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid). [agent: Antigravity] [blocks: 02] [blocked_by: none]
- [x] 02. Work Tracking Initialization: Initialize task tracking files (`.todo.md`, `.log.md`, `.handover.md`) in `work/init-updates-july26`. [agent: Antigravity] [blocks: 03] [blocked_by: 01]
- [ ] 03. Implementation: Update CSS rules in [sections/mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid) (v1.7.9), height alignment in [snippets/mar26-quantity-buy.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/mar26-quantity-buy.liquid), and block schema settings. [agent: Antigravity] [blocks: 04] [blocked_by: 02]
- [ ] 04. Documentation Update: Update section documentation [mar26-main-product.md](file:///C:/code/BrightTools/docs/documentation/sections/mar26-main-product.md) and [mar26-main-product.yaml](file:///C:/code/BrightTools/docs/documentation/sections/mar26-main-product.yaml). [agent: Antigravity] [blocks: 05] [blocked_by: 03]
- [ ] 05. Deploy: Push updated section (v1.7.9) and snippet to live theme #180366573842 (`shopify theme push --allow-live --only sections/mar26-main-product.liquid,snippets/mar26-quantity-buy.liquid`). [agent: Antigravity] [blocks: 06] [blocked_by: 04]
- [ ] 06. Human Gate Approval: User's visual approval (checking live product page on storefront and theme editor for v1.7.9 on desktop and mobile). [agent: Raphael] [blocks: 07] [blocked_by: 05]
- [ ] 07. Handover Update: Update execution log [recode-mar26-quantity-buy.log.md](file:///C:/code/BrightTools/work/init-updates-july26/recode-mar26-quantity-buy.log.md) and handover document [recode-mar26-quantity-buy.handover.md](file:///C:/code/BrightTools/work/init-updates-july26/recode-mar26-quantity-buy.handover.md) with final evidence and completion status. [agent: Antigravity] [blocks: none] [blocked_by: 06]

## Rollback
- trigger: Layout regression or height mismatch on MAR26 Quantity + Buy block.
- steps: Revert modifications in [sections/mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid) and [snippets/mar26-quantity-buy.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/mar26-quantity-buy.liquid) using Git restore (`git restore worktrees/main/sections/mar26-main-product.liquid worktrees/main/snippets/mar26-quantity-buy.liquid`) and push baseline to theme.
- verify: Ensure product page reverts to v1.7.8 state.

## Blockers
- None

## Evidence
- User requirement prompt and screenshot.

## Handover
- [x] Create [recode-mar26-quantity-buy.handover.md](file:///C:/code/BrightTools/work/init-updates-july26/recode-mar26-quantity-buy.handover.md)
- next: Await user authorization to execute Task 03 implementation.
- risks: None

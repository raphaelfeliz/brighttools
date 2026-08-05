# Todo: Testimonial Card Product Name & Clickable Link

## Status
owner: Antigravity
status: completed
updated: 2026-07-26

## Scope
Implement subtle dark grey product name text with compact spacing, in-editor instructions, hover hint badge/title, stationary navigation buttons, and clickable product links on testimonial cards in [mar26-testimonials.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-testimonials.liquid):
- Add `product` (product picker) and `product_name` (text input) block settings with inline `📌 INSTRUCTIONS:` header.
- Render product name in subtle dark grey font (`#475569`, bold uppercase Montserrat) between quotation icon and rating stars.
- Wrap card as an interactive link targeting the selected product URL with a subtle hover effect (card elevation, border glow, and `SEE PRODUCT →` hint badge).
- Move carousel navigation controls outside scrolling container so buttons remain completely stationary.
- Bump version to `1.9.5`.

**Constraint**: DO NOT COMMIT to Git without explicit human approval.

## Approvals
- gate: start
  approver: Raphael
  decision: approved
  phrase: "asdf"
  evidence: "User visually inspected and approved v1.9.5 on storefront and authorized Git commit."
  date: 2026-07-26

## Tasks
- [x] 01. Research & Planning: Analyze testimonial card structure and block schema in [mar26-testimonials.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-testimonials.liquid). [agent: Antigravity] [blocks: 02] [blocked_by: none]
- [x] 02. Work Tracking Initialization: Initialize task tracking files (`.todo.md`, `.log.md`, `.handover.md`) in `work/init-updates-july26`. [agent: Antigravity] [blocks: 03] [blocked_by: 01]
- [x] 03. Implementation: Moved nav controls outside scrolling container, updated card link with `title` attribute and `.mar26-card-hover-hint` badge, dark grey product title, and CSS hover styles in [mar26-testimonials.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-testimonials.liquid) (v1.9.5). [agent: Antigravity] [blocks: 04] [blocked_by: 02]
- [x] 04. Documentation Update: Updated section documentation [mar26-testimonials.md](file:///C:/code/BrightTools/docs/documentation/sections/mar26-testimonials.md). [agent: Antigravity] [blocks: 05] [blocked_by: 03]
- [x] 05. Deploy: Pushed updated section (v1.9.5) to live theme #180366573842 (`shopify theme push --allow-live --only sections/mar26-testimonials.liquid`). [agent: Antigravity] [blocks: 06] [blocked_by: 04]
- [x] 06. Human Gate Approval: User's visual approval (checking live site at https://brighttools-au.myshopify.com for v1.9.5 on desktop and mobile). [agent: Raphael] [blocks: 07] [blocked_by: 05]
- [x] 07. Handover Update: Update execution log [testimonial-card-product-links.log.md](file:///C:/code/BrightTools/work/init-updates-july26/testimonial-card-product-links.log.md) and handover document [testimonial-card-product-links.handover.md](file:///C:/code/BrightTools/work/init-updates-july26/testimonial-card-product-links.handover.md) with final evidence and completion status. [agent: Antigravity] [blocks: none] [blocked_by: 06]

## Rollback
- trigger: Layout regression or unexpected broken links on testimonial cards.
- steps: Revert modifications in [mar26-testimonials.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-testimonials.liquid) using Git restore (`git restore worktrees/main/sections/mar26-testimonials.liquid`) and push baseline to theme.
- verify: Ensure testimonial cards revert to non-linked v1.8.2 state.

## Blockers
- None

## Evidence
- Section v1.9.5 pushed to live theme `#180366573842` and visually approved by user.

## Handover
- [x] Create [testimonial-card-product-links.handover.md](file:///C:/code/BrightTools/work/init-updates-july26/testimonial-card-product-links.handover.md)
- next: Task complete and committed to Git.
- risks: None

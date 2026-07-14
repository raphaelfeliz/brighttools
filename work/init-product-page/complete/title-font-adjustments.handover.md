# Handover: Desktop Title Typography Adjustments

---
wp_id: init-product-page
parent_id: none
status: completed
timestamp: 2026-07-14T16:45:10-03:00

files_changed:
  - path: worktrees/main/sections/mar26-main-product.liquid
    type: modify

commands_run:
  - command: shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only sections/mar26-main-product.liquid --allow-live
    status: success
    output_ref: none

behavioral_change: |
  Adjusted the product title typography on desktop (min-width: 1000px) and mobile inside `mar26-main-product.liquid`:
  - Reduced the desktop font-size to exactly 34px (a 10% reduction from 38px) and set font-weight to 600 (semi-bold).
  - Reduced the mobile font-size by 10% using a multiplier formula: `calc((var(--text-h1) + 2px) * 0.9)`.
  - Pushed section version 1.7.3 to staging.

evidence_links:
  - path: none
    type: text
---

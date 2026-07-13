# Handover: Reordered product price block below title and above reviews

---
wp_id: init-product-page
parent_id: none
status: completed
timestamp: 2026-07-13T17:55:00-03:00

files_changed:
  - path: worktrees/main/templates/product.bt-brooms.json
    type: modify
  - path: worktrees/main/sections/mar26-main-product.liquid
    type: modify
  - path: docs/documentation/product-pages/bt-brooms.md
    type: modify

commands_run:
  - command: shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only templates/product.bt-brooms.json --only sections/mar26-main-product.liquid --allow-live
    status: success
    output_ref: none

behavioral_change: |
  Reordered the product price block to display directly below the title and above the reviews stars badge. This was completed by updating the template JSON block order for desktop and swapping Flexbox order priorities (Order 2 and 3) inside the custom product section styling for mobile.

evidence_links:
  - path: none
    type: text
---

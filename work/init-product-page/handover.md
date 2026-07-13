# Handover: Changed font weight on mar26 product page titles

---
wp_id: init-product-page
parent_id: none
status: completed
timestamp: 2026-07-13T17:44:00-03:00

files_changed:
  - path: worktrees/main/assets/mar26-foundation.css.liquid
    type: modify
  - path: worktrees/main/snippets/mar26-title-and-tags.liquid
    type: modify
  - path: docs/documentation/product-pages/bt-brooms.md
    type: modify

commands_run:
  - command: shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only assets/mar26-foundation.css.liquid --only snippets/mar26-title-and-tags.liquid --allow-live
    status: success
    output_ref: none

behavioral_change: |
  Defined a global .mar26-product-title class in the custom stylesheet and applied it to the unified title and tags snippet. This forces product page titles on custom mar26-main-product templates (like Japanese Broom using product.bt-brooms.json) to render with the brand's Extra Bold (800) font weight.

evidence_links:
  - path: work/init-product-page/evidence/change-title.png
    type: image
---


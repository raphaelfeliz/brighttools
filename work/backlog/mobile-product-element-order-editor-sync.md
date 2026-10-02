# Mobile Product Block Ordering via Shopify Editor

**Status:** Backlog item; identified technical debt in mobile product template layout.

## Problem Statement

Changing the block sequence in the Shopify Theme Editor sidebar for product templates using `mar26-main-product` does not alter the actual visual element order on mobile devices.

## Root Cause Analysis

1. **DOM vs CSS Flexbox `order`**:
   The Shopify Theme Editor reorders blocks by modifying the JSON template block arrays and resulting HTML DOM sequence.
2. **Hardcoded CSS Overrides in `sections/mar26-main-product.liquid`**:
   The section stylesheet enforces hardcoded Flexbox `order` numbers using `!important` under `@media screen and (max-width: 999px)`:
   - `order: 0` – Gallery (`.product-gallery-column`)
   - `order: 1` – Title & badges (`mar26_title_and_tags`, `title`, `mar26_tags`)
   - `order: 2` – Pricing & purchase selectors (`price`, `quantity_selector`, `buy_buttons`)
   - `order: 4` – Social proof / ratings (`@app`, `rating`)
   - `order: 5` – Descriptions (`mar26_short_description`, `description`)
   - `order: 6` – Separators
   - `order: 10` – All other blocks (`.product-info__block-item`)
3. In CSS Flexbox, explicit `order` properties take absolute precedence over the natural HTML document order, overriding whatever order is configured in the editor.

## Proposed Resolution

1. **Remove Hardcoded CSS `order` Declarations**:
   Remove the explicit `order: ... !important` rules from the mobile media query in `sections/mar26-main-product.liquid`.
2. **Normalize Column Structure**:
   Adjust container flattening (`display: contents !important`) so that product-info blocks naturally follow the DOM order produced by the template JSON, while ensuring the product image gallery reliably renders above or in the desired position relative to the details.
3. **Verification**:
   Verify on an unpublished test theme that rearranging blocks in the Shopify Theme Editor sidebar dynamically changes their mobile screen layout without breaking responsive spacing.

## Effort & Complexity

- **Difficulty**: Low (straightforward CSS cleanup and layout regression testing).

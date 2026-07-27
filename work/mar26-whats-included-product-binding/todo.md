# Work Package: Whats Included Product Binding (`todo.md`)

## Target File Versioning
- **Target File**: `sections/mar26-whats-included.liquid`
- **Old Version**: `1.2.0`
- **New Version**: `1.3.0` (Product Binding Enhancement)

---

## Action Checklist

- [x] **Task 1: Add Block Schema Setting**
  - Added `"type": "product"` setting (`id: "product"`) to `item` block schema in `sections/mar26-whats-included.liquid`.

- [x] **Task 2: Implement Product Data Resolution in Liquid**
  - Extracts product title (`product.title`).
  - Extracts main image (`product.featured_image`).
  - Extracts short description strictly from `product.metafields.custom.short_description.value` (NO fallback).
  - Extracts specs 1, 2, 3 from `product.metafields.custom.mar26_highlight_1`..`3`.

- [x] **Task 3: Implement `custom.included_products` Reference Support**
  - Renders product objects dynamically when populated on the product metafield `custom.included_products`.

- [x] **Task 4: Version Bump to v1.3.0**
  - Updated file header comment to `VERSION: 1.3.0`.

- [x] **Task 5: User Handover & Copy-Paste Instructions**
  - Modified code ready in `sections/mar26-whats-included.liquid` for copy-pasting to Shopify Theme Editor.

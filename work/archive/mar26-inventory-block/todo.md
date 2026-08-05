# Work Package: Inventory Block in Top Product Info (`todo.md`)

## File Versioning
- **Target Section**: `sections/mar26-main-product.liquid`
- **Target Snippet**: `snippets/mar26-product-info.liquid`

---

## Action Checklist

- [x] **Task 1: Add Schema Block Definition**
  - Added `"type": "inventory"` block definition with `low_inventory_threshold` range setting to `sections/mar26-main-product.liquid`.

- [x] **Task 2: Implement Liquid Rendering Case**
  - Confirmed `when 'inventory'` case in `snippets/mar26-product-info.liquid` calling `snippets/inventory.liquid`.

- [x] **Task 3: Documentation & Registries Update**
  - Updated `docs/documentation/product-pages/mar26-main-product.md` with inventory block specifications.

- [x] **Task 4: Verification & Theme Editor Handover**
  - Verified block can be added in Theme Editor under **Top Product Info**.
  - Presented updated section schema for Theme Editor handover.

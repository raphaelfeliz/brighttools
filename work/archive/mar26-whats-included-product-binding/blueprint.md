# What's Included Product Binding Blueprint (`blueprint.md`)

This blueprint outlines the architectural enhancement for `sections/mar26-whats-included.liquid` to enable direct product connections that automatically resolve product Title, Featured Image, Short Description (`custom.short_description`), and Highlight Metafields (`mar26 Highlight 1`, `2`, `3`).

---

## 1. Overview & Goal

Enhance `sections/mar26-whats-included.liquid` by adding a **Direct Product Picker (`"type": "product"`)** to section blocks and resolving product object references (`custom.included_products`).

### Data Extraction Rules:
1. **Title**: `product.title`
2. **Image**: `product.featured_image`
3. **Description**: `product.metafields.custom.short_description.value` *(Strictly `custom.short_description` only, NO fallback to `product.description`)*
4. **Spec 1**: `product.metafields.custom.mar26_highlight_1.value`
5. **Spec 2**: `product.metafields.custom.mar26_highlight_2.value`
6. **Spec 3**: `product.metafields.custom.mar26_highlight_3.value`

---

## 2. Liquid Data Resolution Hierarchy

For each item block or product reference in the grid:

* **Item Title**: `block.settings.title | default: linked_product.title`
* **Item Image**: `block.settings.image | default: linked_product.featured_image`
* **Item Description**: `block.settings.description | default: linked_product.metafields.custom.short_description.value`
* **Spec 1**: `block.settings.spec_1 | default: linked_product.metafields.custom.mar26_highlight_1.value`
* **Spec 2**: `block.settings.spec_2 | default: linked_product.metafields.custom.mar26_highlight_2.value`
* **Spec 3**: `block.settings.spec_3 | default: linked_product.metafields.custom.mar26_highlight_3.value`

---

## 3. Schema Specifications (`sections/mar26-whats-included.liquid`)

Add the `"product"` setting as the first setting inside the `item` block schema:

```json
{
  "type": "item",
  "name": "Included Item",
  "settings": [
    {
      "type": "product",
      "id": "product",
      "label": "Product (optional)",
      "info": "Connect a product to automatically pull title, main image, short description, and highlight specs."
    },
    {
      "type": "text",
      "id": "title",
      "label": "Title Override (optional)"
    },
    {
      "type": "image_picker",
      "id": "image",
      "label": "Image Override (optional)"
    },
    {
      "type": "richtext",
      "id": "description",
      "label": "Description Override (optional)"
    },
    {
      "type": "text",
      "id": "spec_1",
      "label": "Spec 1 Override (optional)"
    },
    {
      "type": "text",
      "id": "spec_2",
      "label": "Spec 2 Override (optional)"
    },
    {
      "type": "text",
      "id": "spec_3",
      "label": "Spec 3 Override (optional)"
    }
  ]
}
```

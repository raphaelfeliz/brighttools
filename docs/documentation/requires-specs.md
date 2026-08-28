# REQUIRES SPECS — Product Metafield Pattern

> [!WARNING]
> **MERGE DEBT** — `fix-add-wipes` branch contains the live implementation of this pattern in `snippets/mar26-product-card-catalogv.liquid` (v1.6.1). That branch has **not yet been merged into `main`**. Once the fix is verified on Shopify, merge `fix-add-wipes` → `main` and remove this notice.

## Purpose

`custom.requires_specs` is a boolean product metafield that signals to the Catalog Card component that a product **requires user selection before it can be added to the cart**.

When `true`, the catalog card CTA renders a **link to the product page (PDP)** instead of a direct Add to Cart form, preventing invalid cart submissions.

---

## Problem This Solves

The `mar26-product-card-catalogv.liquid` snippet renders an Add to Cart button overlay on every product card in the catalog engine.

For most products this works correctly. However, some products require a selection step (scent, size, type, bundle configuration) that is **managed outside Shopify variants** — typically via a third-party app such as Dealasy Bundle Builder. From Shopify Liquid''s perspective, these products may appear as single-variant, making `product.variants.size` an unreliable gate.

**Symptom**: The product is briefly added to the cart, then immediately removed, because no selection was made. This is caused by the cart form submitting `selected_or_first_available_variant.id` without the required app-managed selection data.

---

## Metafield Definition

| Property | Value |
|---|---|
| Namespace & key | `custom.requires_specs` |
| Type | Boolean (True or False) |
| Scope | Products |
| Set via | Shopify Admin → Products → [product] → Metafields |

---

## How It Works in Code

Introduced in `mar26-product-card-catalogv.liquid` **v1.6.1**:

```liquid
{%- assign requires_specs = product.metafields.custom.requires_specs.value -%}
{%- if requires_specs == true -%}
  {%- comment -%} Redirect to PDP for selection {%- endcomment -%}
  <a href="{{ product.url }}" class="mar26-card-catalogv-btn" aria-label="Choose options for {{ product.title | escape }}">
    ...
  </a>
{%- else -%}
  {%- comment -%} Direct Add to Cart {%- endcomment -%}
  {%- form 'product', product ... -%}
    ...
  {%- endform -%}
{%- endif -%}
```

---

## SOP: Flagging a Product

Any product that requires a selection step before adding to cart must have this metafield set.

1. Shopify Admin → **Products** → open the product
2. Scroll to the **Metafields** section at the bottom
3. Set **Requires Specs** → **True**
4. Save

### Current products flagged

| Product | Handle | Reason |
|---|---|---|
| Quick Mop Floor Wipes Bundle of 3 | `choose-your-bundle-of-3-packs-quick-mop-floor-wipes-1` | Dealasy scent picker |
| Quick Mop Floor Wipes Bundle of 5 | `choose-your-bundle-of-5-packs-quick-mop-floor-wipes-1` | Dealasy scent picker |

---

## When to Apply This

Apply `requires_specs = true` to any product where:

- Scent, flavour, or fragrance selection is required before purchase
- Size or type must be chosen and is handled by an app (not a Shopify variant)
- A bundle builder (e.g. Dealasy) manages the selection flow on the PDP
- Any cart validation rejects an add-to-cart that lacks a required selection

Do **not** apply it to products where Shopify variant selection is handled natively — those are already gated correctly by the theme''s standard product form.

---

## Version History

| Version | Date | Change |
|---|---|---|
| v1.6.1 | 2026-08-27 | Switched CTA gate from `variants.size` to `custom.requires_specs` metafield |
| v1.6.0 | 2026-08-27 | Initial fix attempt using `variants.size == 1` gate (insufficient for app-managed selections) |

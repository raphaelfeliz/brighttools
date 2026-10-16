# Client Feedback: Product Page Last Bits & Special Page Enhancements

**Date:** 2026-10-15  
**Source:** Client request (Nikki)  
**Status:** Backlog / Ready for implementation  

---

## 1. Product Page Last Bits

### 1.1 Slightly Reduce Size of Title
- **Requirement:** Reduce the product title font size slightly across responsive breakpoints.
- **Affected Files:**
  - `sections/mar26-main-product.liquid`
- **Current State:**
  - Hardcoded to `34px` desktop and `28px` mobile via `#shopify-section-{{ section.id }} .product-info__title`.
- **Target Implementation:**
  - Adjust desktop title to `~28px–30px`.
  - Adjust mobile title to `~22px–24px`.

### 1.2 Spacing Between Stars and '14 reviews'
- **Requirement:** Add visible horizontal separation between the Judge.me star rating icons and the review count text.
- **Affected Files:**
  - `sections/mar26-main-product.liquid`
- **Current State:**
  - `.jdgm-widget`, `.jdgm-preview-badge`, `.jdgm-prev-badge` rendered as flex containers with zero horizontal gap between `.jdgm-prev-badge__stars` and `.jdgm-prev-badge__text`.
- **Target Implementation:**
  - Apply `gap: 6px` or `margin-left: 6px` to `.jdgm-prev-badge__text`.

### 1.3 Add to Cart Button: Smaller Text & Reduced Width
- **Requirement:** Make button text slightly smaller and reduce button width slightly.
- **Affected Files:**
  - `snippets/mar26-product-info.liquid`
- **Current State:**
  - `.mar26-quantity-inline-row .mar26-inline-buy-buttons .button` renders at `16px` font size and stretches `100%` width within flex container.
- **Target Implementation:**
  - Adjust button typography to `14px` (or `0.875rem`).
  - Constrain button width / max-width / flex-basis cleanly without clipping or breaking adjacent quantity selector.

### 1.4 DealEasy - Example 'B' Scents Not Showing on Bundles
- **Requirement:** Resolve DealEasy bundle selection widget not rendering on:
  - `https://brighttools.com.au/products/choose-your-bundle-of-3-packs-quick-mop-floor-wipes-1`
  - `https://brighttools.com.au/products/choose-your-bundle-of-5-packs-quick-mop-floor-wipes-1`
- **Affected Files / Settings:**
  - `templates/product.bt-bundles.json` (or active bundle product template)
  - DealEasy Shopify App Admin Dashboard
- **Root Cause & Resolution:**
  - `templates/product.bt-bundles.json` currently lacks the `dealeasy_mm_bundle_builder` block (`shopify://apps/dealeasy/blocks/mm-bundle-builder/...`).
  - Confirm target template for bundle products and inject block into JSON template definition and `block_order`.
  - Verify offer eligibility rules inside DealEasy app for these two product handles.
  - Note: Third-party app widgets do not hydrate in the Shopify Theme Editor preview; verify exclusively on live/storefront URLs.

---

## 2. Special Page (Caravan Cleaning Bundle Page)

### 2.1 Permanent '2 Year Warranty' Hero Stamp
- **Requirement:** Place a small, permanent '2 year warranty' stamp/badge on the hero section so it remains constantly visible rather than being hidden inside an image slider.
- **Affected Files:**
  - `sections/mar26-main-special-product.liquid`
  - `templates/product.caravan-c-b-page.json`
- **Target Implementation:**
  - Introduce an overlay badge or badge block in `mar26-main-special-product` pinned over the hero media container or header text area.
  - Ensure responsive visibility across mobile and desktop viewports without covering key product visuals or CTA buttons.

### 2.2 Base Bundle Card Preceding 'Complete Your Set' (Locked Selection)
- **Requirement:** Add the 'Caravan Cleaning Bundle' product card (with product image, price, quantity selector) directly before or at the start of the 'Complete your set' flow. One bundle must be selected by default and cannot be removed (quantity $\ge 1$). Customers must not be able to purchase add-ons without the base bundle.
- **Affected Files:**
  - `sections/mar26-buy-flow.liquid`
  - `templates/product.caravan-c-b-page.json`
- **Target Implementation:**
  - Render the primary Caravan Cleaning Bundle card above add-on cards.
  - Initialize bundle quantity to `1` with minimum quantity locked to `1` (disable decrease button at 1).
  - Enforce purchase dependency in checkout handler: add-ons cannot be added to cart unless base bundle is in cart/selected.

---

## 3. Theme Update Strategy

- **Recommendation:** Defer theme update until after upcoming go-live.
- **Rationale:** The store relies heavily on custom `mar26-*` sections, overridden snippet styling, and custom JSON template block placements. Directly updating the base theme will overwrite customizations or cause severe regressions.
- **Protocol:**
  1. Complete go-live on stable current release.
  2. Perform theme update in a separate draft theme in Shopify Theme Library.
  3. Diff and migrate custom `mar26-*` sections, snippets, and template JSONs to the updated theme.
  4. Perform full visual and functional regression testing before publishing.

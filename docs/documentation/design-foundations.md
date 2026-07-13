# DESIGN FOUNDATIONS

This document establishes the foundations and design tokens for storefront customizations.

## 1. Review Rating Stars Color
* **Token**: `--star-color`
* **Theme Customizer Mapping**: Tied directly to the **Star rating** setting (`product_rating_color`) in Shopify Theme Settings, which defaults to amber/yellow (`#ffb74a`).
* **Implementation**: Resolved dynamically at the foundation layer via:
  ```css
  rgb(var(--star-color))
  ```
* **Overrides**: Implemented globally on `.jdgm-star` and `--jdgm-star-color` to synchronize all third-party widgets and fallback mock rating elements.
* **Component Details**: Refer to [judgeme.md](file:///C:/code/BrightTools/docs/documentation/plugins-addons/judgeme.md) for the complete integration overrides, elements, and styles.

## 2. Primary Checkout Button (Add to Cart)
* **Design Synchronization**: Styled to match the exact visual layout properties of accelerated checkouts (e.g., Shop Pay) on product page forms to establish geometric harmony.
* **Tokens**:
  - **Height**: Locked to `55px` to match dynamic wallet buttons.
  - **Border Radius**: Overridden to `3.75rem` (60px pill-shape) to match accelerated checkout button radius.
  - **Typography**: Uses Montserrat, `20px` font size, and `500` (Medium) weight.
  - **Borders & Shadows**: Disabled (`border: none`, `box-shadow: none`) on the host button element to prevent thin browser rendering outlines.
* **Component Details**: Refer to [checkout-button.md](file:///C:/code/BrightTools/docs/documentation/plugins-addons/checkout-button.md) and [accelerated-checkout-button.md](file:///C:/code/BrightTools/docs/documentation/plugins-addons/accelerated-checkout-button.md) for structural overrides.

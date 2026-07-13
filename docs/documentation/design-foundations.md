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

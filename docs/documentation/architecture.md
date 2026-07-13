# ARCHITECTURE

## Theme Core Structure
The storefront is modular, containing components isolated by custom namespaces.

### Naming Conventions
- **Prefixes**:
  - `mar26-`: Core Shopify liquid templates, snippets, and assets (e.g. `mar26-catalog-engine.liquid`, `mar26-product-card-catalogv.liquid`, `mar26-foundation.css.liquid`).
  - `bt-`: Custom collection configurations and JSON templates (e.g. `collection.windows-care-bt.json`, `collection.brooms-bt.json`).
- **Suffixes**:
  - `-catalogv`: Elements specifically scoped to the Catalog Version card layout.

## Catalog Engine Layout Architecture
- File: [mar26-catalog-engine.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-catalog-engine.liquid)
- Grid Class: `.mar26-products-grid.mar26-products-grid--catalogv`
- Layout configuration:
  - Mobile: 2-column grid
  - Tablet: 3-column grid
  - Desktop: 4-column grid

### Product Card Alignment Logic
- Snippet: [mar26-product-card-catalogv.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/mar26-product-card-catalogv.liquid)
- Text Block Container: `.mar26-card-catalogv-text-group` (height locked to `78px` with `overflow: hidden`).
- Dynamic Height Observer:
  - A `ResizeObserver` monitors elements with `[data-catalogv-title]`.
  - Calculates line counts using `lineHeight` and `scrollHeight`.
  - **1 Line**: Displays title, description, and tags.
  - **2 Lines**: Adds `.has-2-lines` class. Hides description row, allows title to take `48px`.
  - **3+ Lines**: Adds `.has-3-lines` class. Hides description and tags row, allows title to take `78px`.

### Card CTA Actions
- Buttons default to disabled state when `product.available` is false.
- Unconditional plus SVG icon rendered for both states.
- Disabled state styling applied via `.mar26-card-catalogv-btn[disabled]` in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid).
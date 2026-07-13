# Judge.me Addon Plugin

Name: Judge.me Product Reviews
Purpose: Renders customer rating stars and preview badges on storefront product layouts using Shopify metafields.
Code: (if available to edit)
- **CSS Overrides**: [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L841-L851) (global overrides), [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L852-L870) (rating widget overrides), and [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L1118-L1137) (catalogv card overrides)
- **Catalog Card Integration**: [mar26-product-card-catalogv.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/mar26-product-card-catalogv.liquid#L72-L76)
- **Product Summary Integration**: [mar26-product-summary.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/mar26-product-summary.liquid#L44-L48)
- **Standard Product Card Integration**: [product-card.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/product-card.liquid#L167-L171)
- **Main Product Page App Blocks**: [mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid#L307-L312)

used on:
- Product Grid Pages (Collections, search, catalogv card layouts)
- Product Detail Pages (PDP section template via `@app` sections)
- Product Summary Blocks (Quick view/drawer blocks)

Elements:
- `.jdgm-widget.jdgm-preview-badge`: The parent badge wrapper widget element.
- `{{ product.metafields.judgeme.badge }}`: Shopify metafield containing the dynamically populated badge HTML.
- `.jdgm-star`: Individual rating star elements.
- `.jdgm-prev-badge__text`: Review count and average score label.

Design Tokens:
- **Star Color**: Set to `rgb(var(--star-color))` (Linked dynamically to theme settings editor via `--star-color` variable; previously locked to `var(--mar26-clr-red)`).
- **Star Font Size**: Enforced at `14px` (Editable in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L862)).
- **Star Spacing**: Right margin of `1.2px` (Editable in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L863)).
- **Badge Text Color**: Set to gray `#9ca3af` (Editable in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L867)).
- **Badge Font Family**: Uses Montserrat layout font stack `var(--mar26-font-stack)` (Editable via theme CSS variables).
- **Badge Font Size**: Set to `11px` (Editable in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L869)).
- **Badge Font Weight**: Semibold `var(--mar26-fw-semibold)` (Editable via theme CSS variables).
- **Badge Spacing**: Left margin of `5px` (Editable in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L871)).
- **Minimum Height**: `18px` boundary to mitigate Cumulative Layout Shift (CLS) when badge loads asynchronously (Editable in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L856)).

# Handover: Image Gallery Layout Modifications

## 1. Scope & Changes
Updated the product image gallery layout on desktop to match the modern card aesthetic while preserving the original mobile swipe carousel:
- **Square Aspect Ratio**: Main image slides in the gallery are strictly square `aspect-ratio: 1/1` and centered.
- **Sizing Constraints**: Sized main product images to `width: 100%` and `max-width: 650px` on desktop, making them responsive and roughly 500px wide on standard viewports.
- **Visual Borders**: Added a `1px solid #e2e8f0` light grey outline and a `16px` border-radius to the main product image viewport.
- **Thumbnail Position**: Repositioned thumbnails to the left side on desktop screens (`>= 1150px`) by enabling the `carousel_thumbnails_left` setting in the template. Under `1150px`, thumbnails fall back to stacking below.
- **Page Padding**: Added container margin rules (`margin-inline: max(var(--container-gutter), 50% - var(--container-max-width) / 2)`) to the `.product` wrapper inside `mar26-main-product.liquid` to ensure the layout respects the site's page padding grid.

## 2. Modified Files
- [mar26-product-gallery.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/mar26-product-gallery.liquid) (Version bumped to `0.2.9`)
- [mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid) (Version bumped to `1.6.6`)
- [product.bt-brooms.json](file:///C:/code/BrightTools/worktrees/main/templates/product.bt-brooms.json) (Setting updated)

## 3. Verification Details
- Pushed files using separate `--only` flags to Stagng theme `#180366573842`.
- Confirmed layout is responsive, respects page padding, displays left thumbnails above 1150px, and leaves mobile layout untouched.
- Approved by Raphael and committed to Git.

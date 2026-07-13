# Add to Cart Button

Name: Add to Cart Button (Primary Checkout Button)
Purpose: Submits the product form to add the selected variant and quantity to the cart.
Code: (if available to edit)
- **Base CSS Styles**: [theme.css](file:///C:/code/BrightTools/worktrees/main/assets/theme.css#L569-L590) (governs base `.button`, `.btn` variables)
- **March 2026 Layout Overrides**: [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid#L1225-L1245) (contains global style matches for height, font, and spacing)
- **Section Specific Overrides**: [mar26-main-product.liquid](file:///C:/code/BrightTools/worktrees/main/sections/mar26-main-product.liquid#L170-L190) (overrides border-radius, background, borders, and shadows to prevent outline halos)
- **Snippet Template**: [button.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/button.liquid) (generates button wrapper element)
- **Product Form Render**: [buy-buttons.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/buy-buttons.liquid#L80) (passes configuration and classes)

used on:
- Product Detail Pages (PDP templates via `mar26-main-product.liquid` main block)
- Quick Buy drawers / popups
- Featured product sections

Elements:
- `buy-buttons`: Custom web component wrapper enclosing cart and checkout buttons.
- `button.button.button--xl`: The native button element used to submit the add-to-cart request.

Design Tokens (March 2026 Product Page Overrides):
- **Background Color**: Controlled by theme customizer setting `settings.atc_button_background` (passed as `atc_button_background` parameter; editable in Theme Customizer).
- **Text Color**: Controlled by theme customizer setting `settings.atc_button_text_color` (passed as `atc_button_text_color` parameter; editable in Theme Customizer).
- **Height**: Enforced at `55px !important` to align perfectly with dynamic checkout elements (e.g. Shop Pay).
- **Border Radius**: Set to `3.75rem !important` (60px pill-shape; overrides base `--rounded-button` token).
- **Borders & Shadows**: Set to `border: none !important;` and `box-shadow: none !important;` to eliminate thin browser outline halos.
- **Font Family**: Montserrat, var(--mar26-font-stack) (enforced; not directly editable).
- **Font Weight**: Medium (`500` / `700` bold; not directly editable).
- **Font Size**: `20px !important` (overrides default `16px`).
- **Line Height**: `normal !important` (prevents vertical offset at `55px` height).
- **Padding**: Reset to `0` block padding to ensure vertical centering.

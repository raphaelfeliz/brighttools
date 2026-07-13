# Accelerated Checkout Button

Name: Accelerated Checkout Button (Dynamic Checkout)
Purpose: Bypasses the shopping cart and checkout steps to complete transactions immediately using dynamic wallet providers (e.g. Shop Pay, Apple Pay, PayPal).
Code: (if available to edit)
- **Shopify Form Integration**: Generated dynamically by Shopify using the liquid tag `{{- form | payment_button -}}` in [buy-buttons.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/buy-buttons.liquid#L83).
- **Inline Custom Styling Overrides**: Styles mapped dynamically in [buy-buttons.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/buy-buttons.liquid#L85-L101) to inject specific theme configurations into the Shopify payment button wrapper container.

used on:
- Product Detail Pages (PDP templates via `mar26-main-product.liquid` main block)
- Quick Buy drawers / popups

Elements:
- `.shopify-payment-button`: Dynamic container wrapper generated and injected by Shopify.
- `.shopify-payment-button__button`: The unbranded button container element.
- `gravity-button.accelerated-checkout-button`: Injected checkout integration web component host element container.

Design Tokens:
- **Block Size (Height)**: Clamped between `25px` and `55px` via `clamp(25px, var(--shopify-accelerated-checkout-button-block-size, 44px), 55px)` (defaults to `55px` high; not directly editable in theme styles).
- **Border Radius**: Set to `3.75rem` (`60px`) via `--shopify-accelerated-checkout-button-border-radius` producing a pill shape (not directly editable in theme styles).
- **Background Color**: Host container background color is transparent (`rgba(0,0,0,0)`), with visual brand backgrounds (e.g., Shop Pay purple) rendered on inner content elements.
- **Text Color**: Black (`rgb(0, 0, 0)`) driven by `--text-color: 0 0 0` (not directly editable).
- **Font Family**: Montserrat, sans-serif (inherited; not directly editable).
- **Font Size**: `20px` (governed by dynamic checkout host).
- **Font Weight**: `400` (Normal; not directly editable).
- **Text Alignment**: Left-aligned (`text-align: left !important`; not directly editable).
- **Letter Spacing**: `0.0em` via `--text-letter-spacing` (not directly editable).
- **Margins & Padding**: Static margins (`0px`) and padding (`0px`) on host container (not directly editable).

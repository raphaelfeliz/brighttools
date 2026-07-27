# MAR26 Main Product Section (`mar26-main-product.liquid`)

The primary product page template section for the MAR26 Revolution theme. It orchestrates the responsive product media gallery, custom product information blocks, variant selection, price calculations, and conversion-optimized purchase flows.

## Active Version: `1.7.8`

## Key Features & Architecture

- **Responsive Media Gallery**:
  - **Desktop**: Configurable media grid layouts (`grid_one`, `grid_two`, `grid_highlight`, or `carousel`) with customizable ratio (`desktop_media_width`), image zoom (`enable_image_zoom`), and video controls (autoplay and looping).
  - **Mobile**: Supports expanded edge-to-edge viewports or gutter-bounded carousels with optional free-scrolling momentum or dot controls.
- **MAR26 Custom Block Architecture**:
  - `mar26_title_and_tags`: Combines product title and product tag chips in a single unified header block.
  - `mar26_gradient_title`: Renders eye-catching gradient typography using customizable color stops.
  - `mar26_quantity_price`: Integrated quantity selector and live dynamic price stack.
  - `mar26_short_description`: Rich text product highlights section with support for bulleted features.
- **Unified Pill Buy Buttons (`#0F172A`)**:
  - Enforces synchronized pill geometry (`border-radius: 3.75rem`), uppercase typography, hover scale animation (`transform: scale(1.05)`), and a subtle light sweep highlight (`::after`).
- **Sticky / Fixed Add-to-Cart Bar**:
  - Configurable `show_fixed_add_to_cart` setting renders a sticky bottom bar on scroll for instant mobile and desktop checkout.

---

## Block Types

The section supports the following modular blocks:

| Block Type ID | Name | Description |
| :--- | :--- | :--- |
| `mar26_title_and_tags` | Title and Tags (Unified) | Unified header block rendering title and product tags. |
| `title` | Title | Standard product title block. |
| `mar26_gradient_title` | MAR26 Gradient Title | Gradient styled title block. |
| `vendor` | Vendor | Product vendor label. |
| `sku` | SKU | Variant SKU identifier. |
| `badges` | Badges | Product badges (e.g. Sale, Sold Out). |
| `price` | Price | Standard price display with compare-at price. |
| `mar26_quantity_price` | MAR26 Quantity + Buy | Combined quantity picker and price display block. |
| `payment_terms` | Payment Installments | Installment payment terms (Shop Pay). |
| `rating` | Rating | Star rating badge and review count. |
| `separator` | Separator | Horizontal divider rule. |
| `description` | Description | Standard full product description tab. |
| `mar26_short_description` | MAR26 Short Description | Rich text product highlights and feature lists. |
| `variant_picker` | Variant Picker | Option dropdowns or pill swatches. |
| `quantity_selector` | Quantity Selector | Standalone quantity input. |
| `buy_buttons` | Buy Buttons | Primary Add to Cart and dynamic checkout buttons. |
| `share_buttons` | Share Buttons | Social media sharing links. |
| `@app` | App Block | Shopify App block placeholder. |

---

## Section Settings

| Setting ID | Type | Description |
| :--- | :--- | :--- |
| `full_width` | Checkbox | Expand section container to full window width. |
| `show_fixed_add_to_cart` | Checkbox | Enable sticky bottom Add-to-Cart bar on scroll. |
| `short_description_position` | Select | Position of short description (`above_buy_buttons` or `below_buy_buttons`). |
| `desktop_media_width` | Range | Desktop gallery column width percentage (`30%` to `70%`). |
| `desktop_media_layout` | Select | Desktop layout (`grid_one`, `grid_two`, `grid_highlight`, `carousel`). |
| `mobile_media_size` | Select | Mobile media size (`contained` or `expanded`). |
| `mobile_carousel_control` | Select | Mobile gallery control style (`dots`, `thumbnails`, `free_scroll`). |
| `enable_video_autoplay` | Checkbox | Autoplay embedded product videos. |
| `enable_video_looping` | Checkbox | Loop product video playback continuously. |
| `enable_image_zoom` | Checkbox | Enable click-to-zoom on main product images. |
| `max_image_zoom_level` | Range | Maximum zoom multiplier (e.g. `2x`, `3x`). |
| `show_nav_icons_desktop` | Checkbox | Show carousel navigation arrows on desktop. |
| `show_nav_icons_mobile` | Checkbox | Show carousel navigation arrows on mobile. |
| `background` | Color | Solid section background color. |
| `background_gradient` | Color Background | Optional section background gradient. |
| `text_color` | Color | Section text color token override. |

# MAR26 Main Product Section (`mar26-main-product.liquid`)

This section drives the product page layout, mobile orchestration sequencing, and product detail configuration. It is the default main product section applied across all products on the storefront.

---

## Block List

| Display Name | Block Type | Limit | Purpose |
| --- | --- | --- | --- |
| **App Integrations** | `@app` | None | Integrates third-party Shopify app block widgets. |
| **Title and Tags (Unified)** | `mar26_title_and_tags` | 1 | Combines product title with custom metadata tags. |
| **Vendor** | `vendor` | 1 | Displays the product manufacturer/vendor name. |
| **Title** | `title` | 1 | Standard product title display. |
| **MAR26 Gradient Title** | `mar26_gradient_title` | None | Renders a stylized solid and gradient-colored title. |
| **SKU** | `sku` | 1 | Displays stock keeping unit codes. |
| **Badges** | `badges` | 1 | Shows promotional or feature badges from metafields. |
| **Price** | `price` | 1 | Displays pricing tier and taxes notices. |
| **MAR26 Quantity + Buy** | `mar26_quantity_price` | 1 | Unified quantity picker and checkout buttons block. |
| **Payment installments** | `payment_terms` | 1 | Integrates Shop Pay/installment terms. |
| **Rating** | `rating` | 1 | Shows average customer review rating scores. |
| **Separator** | `separator` | None | Adds visual divider lines between block elements. |
| **Description** | `description` | 1 | Displays product description text (collapsible). |
| **Variant picker** | `variant_picker` | 1 | Renders swatches and dropdown selectors. |
| **Quantity selector** | `quantity_selector` | 1 | Standalone quantity picker widget. |
| **Buy buttons** | `buy_buttons` | 1 | Standard Add to Cart & dynamic checkout buttons. |
| **MAR26 Short Description** | `mar26_short_description` | 1 | Renders details alongside three custom bullet highlights. |
| **Share buttons** | `share_buttons` | None | Renders social media share buttons. |

---

## Block Specifications

* **App block (`@app`)**
  - Renders third-party Shopify apps.
  - No settings.

* **Unified Title & Tags (`mar26_title_and_tags`)**
  - Pulls tags from the `custom.color_tags` metaobject list.
  - Settings: `heading_tag` (Style: `h1` - `h6`, default `h2`).

* **Vendor (`vendor`)**
  - Displays product vendor name.
  - No settings.

* **Title (`title`)**
  - Standard title rendering.
  - Settings: `heading_tag` (Style: `h1` - `h6`, default `h2`).

* **MAR26 Gradient Title (`mar26_gradient_title`)**
  - Renders solid top text and background gradient bottom text.
  - Settings: `show_on_mobile` (bool), `show_on_desktop` (bool), `text_top` (text), `text` (gradient text), `color_1` (hex), `color_2` (hex), `font_size` (range), `font_size_mobile` (range), `font_weight` (select).

* **SKU (`sku`)**
  - Renders the variant SKU.
  - No settings.

* **Badges (`badges`)**
  - Displays promotional labels.
  - No settings.

* **Price (`price`)**
  - Renders price tags.
  - Settings: `show_taxes_notice` (bool).

* **MAR26 Quantity + Buy (`mar26_quantity_price`)**
  - Unified quantity and button row.
  - Settings: `show_payment_button` (bool), `atc_button_background` (color), `atc_button_text_color` (color), `payment_button_background` (color), `payment_button_text_color` (color).

* **Payment installments (`payment_terms`)**
  - Shopify installments details.
  - No settings.

* **Rating (`rating`)**
  - Shows review ratings.
  - No settings.

* **Separator (`separator`)**
  - Horizontal separator line.
  - No settings.

* **Description (`description`)**
  - Main description text.
  - Settings: `icon` (select), `custom_icon` (image), `icon_width` (range), `collapse_content` (bool).

* **Variant picker (`variant_picker`)**
  - Renders swatch buttons or option lists.
  - Settings: `hide_sold_out_variants` (bool), `stack_blocks` (bool), `selector_style` (select), `swatch_selector_style` (select).

* **Quantity selector (`quantity_selector`)**
  - Standard quantity picker.
  - No settings.

* **Buy buttons (`buy_buttons`)**
  - Add to Cart and checkout buttons.
  - Settings: `show_payment_button` (bool), `atc_button_background` (color), `atc_button_text_color` (color).

* **MAR26 Short Description (`mar26_short_description`)**
  - Displays rich text and up to three highlight bullet points.
  - Settings: `description` (richtext), `highlight_1` (text), `highlight_2` (text), `highlight_3` (text), `icon_color` (color).

* **Share buttons (`share_buttons`)**
  - Social sharing links.
  - Settings: `alignment` (select, default `start`).

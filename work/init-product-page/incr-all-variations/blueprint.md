# Product Page Variations Blueprint (`blueprint.md`)

This blueprint outlines the architectural mapping between **Mandatory & Optional Template-Level Sections** and **Product-Level Metafields & Native Fields**.

---

## 1. Mandatory Template-Level Sections (Required Across ALL Product Templates)

1. 🔴 **`Scroll to Top`** (`sections/custom-liquid.liquid`): Floating scroll-to-top button widget (Mandatory).
2. 🔴 **`Top Product Info`** (`sections/mar26-main-product.liquid`): Core product details, title, price, gallery, quantity stepper, buy buttons, and short description (Mandatory).
3. 🔴 **`Footer`** (`sections/mar26-footer.liquid`): Storefront footer (Mandatory).

---

## 2. Full Section Rendering Sequence (Based on Live `bt-brooms`)

| Order | Section Name | Loose Note Item | Theme Section File | Default Status | Description |
| --- | --- | --- | --- | --- | --- |
| 1 | `Scroll to Top` | *(Mandatory)* | `sections/custom-liquid.liquid` | 🔴 Active | Floating scroll-to-top button widget. |
| 2 | `Top Product Info` | *(Mandatory)* | `sections/mar26-main-product.liquid` | 🔴 Active | Main product info, gallery, pricing, buy buttons. |
| 3 | `Video` | **4 x Videos Section** (Single Video) | `sections/video.liquid` | 🔴 Active | Full-width product demonstration video. |
| 4 | `Better Cleaning` | **Better Cleaning** | `sections/media-with-text.liquid` | 🔴 Active | Dual-column features showcase video & text. |
| 5 | `Q&A` | **Q&A** | `sections/faq.liquid` | 🔴 Active | Accordion FAQ listing 5 product Q&As. |
| 6 | `Built-Different` | **Built-Different** | `sections/mar26-highlights.liquid` | 🔴 Active | Banners highlighting Heavy Duty, Zero Risk, and Warranty. |
| 7 | `What's Included` | **What's Included** | `sections/mar26-whats-included.liquid` | 🔴 Active | Grid showcasing items included in the product/bundle. |
| 8 | `Testimonials` | **Testimonials** | `sections/mar26-testimonials.liquid` | 🔴 Active | Customer reviews and quotes slider. |
| 9 | `Best-Sellers` | **Best-Sellers** | `sections/mar26-best-sellers.liquid` | 🔴 Active | Best-selling products slider shelf. |
| 10 | `4 x Videos Section` | **4 x Videos Section** | `sections/_blocks.liquid` | ⚪ Disabled | Multiple inline video grid section (`blocks_jiJwFP`). |
| 11 | `Footer` | *(Mandatory)* | `sections/mar26-footer.liquid` | 🔴 Active | Storefront footer group. |

---

## 3. Product-Level Fields Mapping Summary

### Native Shopify Fields (100% Confirmed & Available)
* **Title**: `product.title`
* **Description / Product Details**: `product.description` (Main product description editor in Shopify Admin)
* **Images**: `product.media` / `product.images`

### Confirmed Custom Metafields (Configured & Created)
* ✅ **Product Video (Desktop)**: `custom.product_video` (`file_reference` - Video) — [Admin Link](https://admin.shopify.com/store/brighttools-au/settings/custom_data/product/metafields/165283856658)
* ✅ **Mobile Product Video**: `custom.mobile_product_video` (`file_reference` - Video) — Created in Admin
* ✅ **What's Included**: `custom.mar26_included_items` (`list.metaobject_reference` -> `mar26_included_item`)
* ✅ **Short Description Highlights**: `custom.short_description` & block settings `highlight_1`, `highlight_2`, `highlight_3`

---

## 4. Final Mapping Matrix for Product Admin Fields

| Loose Note Item | Mapping Type | Shopify Field / Metafield Key | Shopify Data Type | Status | Usage |
| --- | --- | --- | --- | --- | --- |
| **Title** | Native Shopify | `product.title` | `single_line_text_field` | **Confirmed Native** | Standard product title. |
| **Description / Product Details** | Native Shopify | `product.description` | `richtext` | **Confirmed Native** | Main product description rich-text body. |
| **Images** | Native Shopify | `product.media` | `list.file_reference` (image) | **Confirmed Native** | Main product image & media gallery. |
| **Product Video (Desktop)** | Custom Metafield | `custom.product_video` | `file_reference` (video) | ✅ **Done / Created** | Desktop `.mp4` feature video asset. |
| **Mobile Product Video** | Custom Metafield | `custom.mobile_product_video` | `file_reference` (video) | ✅ **Done / Created** | Mobile `.mp4` feature video asset. |
| **What's Included** | Custom Metafield | `custom.mar26_included_items` | `list.metaobject_reference` (`mar26_included_item`) | ✅ **Done / Created** | List of included bundle/system items. |

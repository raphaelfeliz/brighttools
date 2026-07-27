# BrightTools Metafields Registry (`metafields.registry.md`)

This registry documents all custom and native Shopify metafield definitions configured across products and collections in the BrightTools storefront, detailing their namespace, key, type, assignment coverage, Admin URL, and Liquid section usage.

---

## 1. MAR26 Custom Product Metafields

| Metafield Definition Name | Namespace & Key | Type | Assigned Count | Admin Link | Used In Liquid Code / Purpose |
| --- | --- | --- | --- | --- | --- |
| **Short Description** | `custom.short_description` | `single_line_text_field` | 7 products | - | Renders bullet highlight point in `mar26-bundles.liquid` and `mar26-short-description.liquid`. |
| **Product Video (Desktop)** | `custom.product_video` | `file_reference` (Video) | 0 products | [Admin Link](https://admin.shopify.com/store/brighttools-au/settings/custom_data/product/metafields/165283856658) | Stores desktop `.mp4` feature video to override global video in `video.liquid` / `media-with-text.liquid`. |
| **Mobile Product Video** | `custom.mobile_product_video` | `file_reference` (Video) | 0 products | Admin Created | Stores mobile vertical `.mp4` feature video for responsive mobile player. |
| **Included Products** | `custom.included_products` | `list.product_reference` | 3 products | - | References bundle item products rendered in `mar26-bundles.liquid`. |
| **color tags** | `custom.color_tags` | `list.metaobject_reference` | 31 products | - | Metaobject list rendering color tags above product title in `mar26-title-and-tags.liquid`. |
| **mar26 Product Tags (above Title)** | `custom.mar26_product_tags` | `single_line_text_field` | 1 product | - | Custom tag badge string displayed above title. |
| **mar26 Solid Top Text** | `custom.mar_26_solid_top_text` | `single_line_text_field` | 1 product | - | Top solid text string for `mar26-gradient-title.liquid`. |
| **mar26 Solid Bottom Gradient Text** | `custom.mar_26_solid_bottom_gradient_text` | `single_line_text_field` | 2 products | - | Gradient-colored text string for `mar26-gradient-title.liquid`. |
| **mar26 Highlight 1** | `custom.mar26_highlight_1` | `single_line_text_field` | 3 products | - | First bullet point highlight in `mar26-short-description.liquid`. |
| **mar26 Highlight 2** | `custom.mar26_highlight_2` | `single_line_text_field` | 3 products | - | Second bullet point highlight in `mar26-short-description.liquid`. |
| **mar26 Highlight 3** | `custom.mar26_highlight_3` | `single_line_text_field` | 3 products | - | Third bullet point highlight in `mar26-short-description.liquid`. |
| **MAR26 Sub-Category** | `custom.mar26_sub_category` | `single_line_text_field` | 5 products | - | Sub-category filter label for MAR26 catalog pages. |

---

## 2. Media Showcase Metafields (`media-with-text`)

| Metafield Definition Name | Namespace & Key | Type | Assigned Count | Admin Link | Used In Liquid Code / Purpose |
| --- | --- | --- | --- | --- | --- |
| **Media Text Box 1 (Rich Text)** | `custom.media_text_box_1_rich_text` | `richtext` | 2 products | - | Primary text content for feature block 1 in `media-with-text.liquid`. |
| **Mar26 Media Text Box 1 (Image)** | `custom.mar26_media_text_box_1_image` | `file_reference` (Image) | 1 product | - | Image asset for feature block 1 in `media-with-text.liquid`. |
| **Mar26 Media Text Box 2 (Rich Text)** | `custom.mar26_media_text_box_2_rich_text` | `richtext` | 2 products | - | Secondary text content for feature block 2 in `media-with-text.liquid`. |
| **Mar26 Media Text Box 2 (Video)** | `custom.mar26_media_text_box_2_video` | `file_reference` (Video) | 2 products | - | Feature video asset (`.mp4`) for feature block 2 in `media-with-text.liquid`. |

---

## 3. Product Accordion Metafields

| Metafield Definition Name | Namespace & Key | Type | Assigned Count | Admin Link | Used In Liquid Code / Purpose |
| --- | --- | --- | --- | --- | --- |
| **Accordion Title 1** | `custom.accordion_title_1` | `single_line_text_field` | 32 products | - | Header title for product collapsible tab 1 in `description` block. |
| **Accordion Body 1** | `custom.accordion_body_1` | `multi_line_text_field` | 32 products | - | Content body for product collapsible tab 1. |
| **Accordion Title 2** | `custom.accordion_title_2` | `single_line_text_field` | 32 products | - | Header title for product collapsible tab 2. |
| **Accordion Body 2** | `custom.accordion_body_2` | `multi_line_text_field` | 32 products | - | Content body for product collapsible tab 2. |
| **Accordion Title 3** | `custom.accordion_title_3` | `single_line_text_field` | 32 products | - | Header title for product collapsible tab 3. |
| **Accordion Body 3** | `custom.accordion_body_3` | `multi_line_text_field` | 32 products | - | Content body for product collapsible tab 3. |
| **Accordion Title 4** | `custom.accordion_title_4` | `single_line_text_field` | 28 products | - | Header title for product collapsible tab 4. |
| **Accordion Body 4** | `custom.accordion_body_4` | `multi_line_text_field` | 28 products | - | Content body for product collapsible tab 4. |

---

## 4. Product Catalog Attributes & Highlights

| Metafield Definition Name | Namespace & Key | Type | Assigned Count | Admin Link | Used In Liquid Code / Purpose |
| --- | --- | --- | --- | --- | --- |
| **Selling Points** | `custom.selling_points` | `multi_line_text_field` | 88 products | - | Key product value propositions displayed on product cards & headers. |
| **Collection Filter** | `custom.collection_filter` | `single_line_text_field` | 16 products | - | Filter key string used in faceted collection filtering. |
| **EAN** | `custom.ean` | `single_line_text_field` | 63 products | - | EAN / International Article Barcode Number for products. |
| **Related products settings** | `custom.related_products_settings` | `single_line_text_field` | 2 products | - | Configuration settings string for related product recommendations. |

---

## 5. Shopify System & App Standard Metafields

| Metafield Definition Name | Namespace & Key | Type | Assigned Count | Admin Link | Used In Liquid Code / Purpose |
| --- | --- | --- | --- | --- | --- |
| **Product rating** | `reviews.rating` | `rating` | 83 products | - | Standard review app rating score (e.g. Judge.me / Shopify Reviews). |
| **Product rating count** | `reviews.rating_count` | `number_integer` | 83 products | - | Total review count integer. |
| **Complementary products** | `shopify.complementary_products` | `list.product_reference` | 2 products | - | Native Shopify Search & Discovery app complementary cross-sell products. |
| **Related products** | `shopify.related_products` | `list.product_reference` | 2 products | - | Native Shopify Search & Discovery app recommendations. |
| **Trending right now** | `custom.trending_right_now` | `product_reference` | 0 products | - | Unassigned product reference for trending shelf. |
| **Search product boosts** | `shopify.search_product_boosts` | `single_line_text_field` | 0 products | - | Search term boosting metadata. |
| **Google: Custom Product** | `mm-google-shopping.custom_product` | `boolean` | 0 products | - | Google Shopping Feed custom product indicator flag. |
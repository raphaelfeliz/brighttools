# Store Updates & Theme Editor User Guide

## System Updates Overview
All updates have been implemented directly across your theme sections, snippets, and product templates. Changes focus on editor organization, responsive layout adjustments, and automated product content population.

## Start Here:
a) Open the Theme Editor (**Online Store > Themes > Customize**).
b) Using the top navigation bar dropdown, go to **Products**, or click any direct link below to open and edit a specific template:

1. **`bt-brooms`**: [Open Template in Theme Editor](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-brooms)
2. **`bt-bundles`**: [Open Template in Theme Editor](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-bundles)
3. **`bt-cleaningproducts`**: [Open Template in Theme Editor](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-cleaningproducts)
4. **`bt-dustpans`**: [Open Template in Theme Editor](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-dustpans)
5. **`bt-floor-wipes`**: [Open Template in Theme Editor](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-floor-wipes)
6. **`bt-microfibre`**: [Open Template in Theme Editor](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-microfibre)
7. **`bt-mops`**: [Open Template in Theme Editor](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-mops)
8. **`bt-squeegees`**: [Open Template in Theme Editor](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-squeegees)
9. **`bt-toilet`**: [Open Template in Theme Editor](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-toilet)
10. **`bt-windows-care`**: [Open Template in Theme Editor](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-windows-care)

c) To connect a product to a template: Open **Shopify Admin > Products > [Select Product]**, set the right-side **Theme template** dropdown to your target template (e.g. `bt-brooms`), and click **Save**.

---

# SECTION: Top Product Info (aka 'Product Card', the top section of each product)

### Action Summary:
a) **Renamed Section**: Display name changed from "MAR26 Product page" to "Top Product Info" in the left sidebar menu for clearer navigation.
b) **Inline Quantity Selector**: Reintroduced the `- 1 +` quantity stepper on the exact same horizontal row as the Add to Cart button on desktop screens.
c) **Responsive Mobile Stacking**: On mobile screens (< 1000px), quantity stepper, Add to Cart, and express checkout buttons automatically stack vertically at 100% full width (1 per line).
d) **Solid Navy Buy Buttons**: Applied solid navy (`#0F172A`) pill styling with white text across standard product templates, replacing red outline buttons when dynamic checkout is active.
e) **Automated Bullet Highlights**: Updated short description card to automatically pull `mar26 Highlight 1`, `2`, and `3` metafields from the Shopify product admin page.
f) **Inventory Stock Indicator Block**: Added native `inventory` block support allowing stock status indicators (e.g. "In stock", "Low stock - X left") to be displayed inside Top Product Info.

### 👉 How to Use It / Test It:
1. **Assign Product to New Template**: Open **Shopify Admin > Products > [Select Product]**. In the right-hand panel under **Theme template**, change `Default product` to the target collection template (e.g. `bt-brooms`, `bt-bundles`).
2. **Populate Metafield Bullets**: Scroll down to **Metafields** on the product page and enter text into `mar26 Highlight 1`, `Highlight 2`, and `Highlight 3`.
3. **Add Inventory Block in Theme Editor**: Open Theme Editor, go to **Top Product Info**, click **Add block**, select **Inventory**, and set your low stock threshold.
4. **Save**: Click **Save** in Shopify Admin and Theme Editor.
5. **Test Link**: [Preview `bt-brooms` in Theme Editor](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-brooms)

---

# SECTION: Testimonials

### Action Summary:
a) **Centered Rating Badge**: Positioned a 5-star rating icon stack centered directly above the section title and subheading.
b) **Product Link Badges**: Added product picker binding to review card blocks, rendering a clickable product tag badge on each review card.
c) **Dynamic Product Titles**: Leaving the custom product name field blank automatically displays the real title of the connected Shopify product.

### 👉 How to Use It / Test It:
1. Open Theme Editor (**Online Store > Themes > Customize**).
2. Select **MAR26 Testimonials** in the left sidebar.
3. Click an individual **Testimonial Card** block.
4. Select a product in the **Product** picker field.
5. *(Optional)* Leave **Custom Product Name** empty to automatically display the product's actual title, or enter custom text to override it.

---

# SECTION: What's Included

### Action Summary:
a) **Direct Product Connection**: Added an optional **Product** picker setting to each item block in Theme Editor.
b) **Automated Content Resolution**: Connecting a product automatically pulls its main image, title, short description strictly from `custom.short_description`, and bullet highlights (`mar26 Highlight 1`, `2`, `3`).
c) **Product Reference List Support**: Added support for `custom.included_products` metafield to render bundle cards automatically without creating blocks manually.
d) **Manual Overrides**: Entering manual text or images in Theme Editor block settings overrides product defaults.

### 👉 How to Use It / Test It:
- **Option A (Theme Editor)**: Open **MAR26 What's Included**, click an **Included Item** block, and select a product in the **Product** picker.
- **Option B (Shopify Admin Metafields)**: Open **Shopify Admin > Products > [Bundle Product]**, scroll to **Metafields**, and select items inside **Included Products** (`custom.included_products`).

---

# SECTION: Product Page Variations & Templates

### Action Summary:
a) **Catalog-Aligned Templates**: Established active registry structure for 10 custom product templates matching the 10 `-bt` collection pages (`bt-brooms`, `bt-bundles`, `bt-mops`, `bt-dustpans`, etc.).
b) **Mandatory Anchors**: Enforced 3 mandatory anchor sections across all templates: `Scroll to Top` (`custom-liquid`), `Top Product Info` (`mar26-main-product`), and `Footer` (`mar26-footer`).
c) **Standardized Flow**: Synchronized rendering order across templates: `Scroll to Top` → `Top Product Info` → `Video` → `Better Cleaning` → `Q&A` → `Built-Different` → `What's Included` → `Testimonials` → `Best-Sellers` → `Footer`.

### 👉 How to Use & Connect Products:
1. **Connect Products in Batches or One-by-One**:
   - Go to **Shopify Admin > Products > [Select Product]**.
   - In the right sidebar under **Theme template**, select the corresponding collection template for that product (e.g. `bt-brooms`, `bt-bundles`, `bt-mops`, etc.).
   - Click **Save**.

2. **Direct Editor Access Links**:
   - `bt-brooms`: [Open Template](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-brooms)
   - `bt-bundles`: [Open Template](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-bundles)
   - `bt-cleaningproducts`: [Open Template](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-cleaningproducts)
   - `bt-dustpans`: [Open Template](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-dustpans)
   - `bt-floor-wipes`: [Open Template](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-floor-wipes)
   - `bt-microfibre`: [Open Template](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-microfibre)
   - `bt-mops`: [Open Template](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-mops)
   - `bt-squeegees`: [Open Template](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-squeegees)
   - `bt-toilet`: [Open Template](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-toilet)
   - `bt-windows-care`: [Open Template](https://admin.shopify.com/store/brighttools-au/themes/180366573842/editor?previewPath=%2Fproducts%2Ftest-product%3Fview%3Dbt-windows-care)

---

# SECTION: Metafields & Custom Data

### Action Summary:
a) **Feature Video Slots**: Registered `custom.product_video` (Desktop) and `custom.mobile_product_video` (Mobile) to stream hosted `.mp4` feature videos.
b) **Centralized Registry**: Organized all storefront product and collection metafields into 5 structured tables in `docs/documentation/metafields/metafields.registry.md`.

### 👉 How to Use It / Test It:
1. Open **Shopify Admin > Products > [Select Product]**.
2. Scroll down to **Metafields**.
3. Under **Product Video (Desktop)** and **Mobile Product Video**, upload or select your `.mp4` video files.
4. Ensure the product is connected to a `bt-*` template in the right sidebar (**Theme template**).
5. Save the product page. Videos will stream in your product showcase sections automatically.
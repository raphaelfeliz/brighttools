# Brooms Custom Product Page (`product.bt-brooms.json`)

This document describes the layout, sections rendering sequence, block composition, and design tokens of the brooms product page template.

---

## Page Sections Render Order

| Section Key | Section Type | Status | Purpose |
| --- | --- | --- | --- |
| `custom_liquid_bYgJK7` | `custom-liquid` | Active | Renders a custom floating Scroll-to-Top button. |
| `main` | `mar26-main-product` | Active | Primary product details and buying flow section. |
| `video_PBmR83` | `video` | Active | Displays a full-width product demo video. |
| `video_demo` | `media-with-text` | Active | Dual-column features showcase with auto-play video. |
| `faq` | `faq` | Active | Accordion FAQ listing 5 common product questions. |
| `mar26_highlights_djAVBa` | `mar26-highlights` | Active | Banners highlighting Heavy Duty, Zero Risk, and Warranty. |
| `rich_text_JhBcCr` | `rich-text` | Disabled | Standalone text section. |
| `blocks_jiJwFP` | `_blocks` | Disabled | Multiple inline video blocks section. |
| `mar26_testimonials` | `mar26-testimonials` | Active | Displays customer reviews and quotes. |
| `mar26_best_sellers` | `mar26-best-sellers` | Disabled | Best-selling products slider shelf. |

---

## Main Product Info Block Order (`mar26-main-product`)

* **Title and Tags (`mar26_title_and_tags_5z3hZR`)**: Displays the product title and dynamically pulls custom metadata tags.
* **Reviews Badge (`judge_me_reviews_preview_badge_kG7NLt`)**: Star rating preview from Judge.me reviews integration.
* **Short Description (`mar26_short_description_tARAbB`)**: Displays highlight points tailored for brooms:
  - *Pivot head design for tight spaces*
  - *Fine particle dust catcher system*
  - *Effortless hair, dust & dirt pick-up*
* **Gradient Title (`mar26_gradient_title_RMQCET`)**: Styled gradient title *(Disabled)*.
* **Price (`price`)**: Displays current pricing.
* **Quantity Selector (`quantity_selector_dgjkJg`)**: Quantity input field.
* **Bundle Builder (`dealeasy_mm_bundle_builder_dCNcYL`)**: App-integrated bundle block *(Disabled)*.
* **Description (`description`)**: Collapsible description row *(Disabled)*.
* **Variant Picker (`variant_picker`)**: Option swatches for sizing or colors.
* **Buy Buttons (`buy_buttons_KpKVCY`)**: Add to Cart and dynamic checkout button row.

---

## Design Tokens

- **Gutter & Spacings**: Mobile uses custom inner spacings of 6px (`--spacing-1-5`) and 12px (`--spacing-3`) vertical margins. Desktop layout utilizes default `--container-gutter`.
- **Primary Color Palette**: Uses default white background `#ffffff` and black text `#000000`.
- **Button Tokens**: Cart buttons override default styles to unified navy background `#0F172A` and border-radius `10px` for geometric integration.
- **Typography Tokens**: Product titles render with the global `.mar26-product-title` utility class, forcing `--mar26-font-weight-title` (Extra Bold / `800`) and the `"Montserrat", sans-serif` font family.

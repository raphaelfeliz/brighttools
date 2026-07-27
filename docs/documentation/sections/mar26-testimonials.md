# MAR26 Testimonials Section (`mar26-testimonials.liquid`)

A high-impact, premium testimonial spotlight section featuring an infinite-looping marquee carousel, 3-tier 5-star header stack, interactive clickable product cards with subtle dark grey product titles and hover elevation, stationary navigation controls, country-specific verified customer badges, and background grain texture overlay.

## Active Version: `1.9.5`

## Key Features & Behavior

- **3-Tier 5-Star Centered Stack**: Top row of 5 upright pink stars with subtle drop shadow filter (`drop-shadow(0 2px 4px rgba(0, 0, 0, 0.18))`), centered main headline `"WHAT THEY'RE SAYING"`, and centered subheading paragraph.
- **Product Name & Clickable Card Links**:
  - Displays product title in subtle dark grey font (`#475569`, bold uppercase Montserrat) between the quotation icon and rating stars with compact `0.25rem` gap to stars.
  - Selecting a product or custom link wraps the card in an interactive `<a>` element with hover elevation (`transform: translateY(-4px)`), soft shadow, border highlight, native `title` tooltip, and a `SEE PRODUCT →` badge (`.mar26-card-hover-hint`) that fades in on card hover.
- **Stationary Navigation Controls**: Nav arrow controls (`.mar26-testi-controls`) are anchored to `<mar26-testimonials class="mar26-testimonials-wrapper">` outside the `[data-carousel-container]` scrollport so they remain 100% stationary at the outer sides of the section (`left: -1.5rem; width: calc(100% + 3rem)`) without scrolling along with the marquee cards.
- **📌 In-Editor Instructions**: Displays inline setup instructions (`📌 INSTRUCTIONS:`) in the Shopify Theme Customizer block sidebar.
- **Infinite Marquee Engine**: Liquid duplicates block items 3x (`{% for i in (1..3) %}`) and the `mar26-testimonials` Custom Web Component continuously scrolls the container horizontally via `requestAnimationFrame`. When scrolling reaches boundary thresholds, JS teleports `scrollLeft` seamlessly.
- **Interactive Pause**: Pauses scrolling when hovered (`mouseenter`/`mouseleave`) or touched (`touchstart`/`mousedown` for 2.5s).
- **Responsive Navigation Controls**: Desktop renders previous/next arrow buttons (`data-prev`, `data-next`) that scroll by card width. On mobile viewports (<768px), control buttons are hidden and native touch momentum scrolling (`overflow-x: auto`) is enabled.
- **Country Badge Integration**: Supports country chip flags (Australia `country-flags--AU` and New Zealand `country-flags--NZ`) using `country-flags.css`.

---

## Block Types (`testimonial`)

Each testimonial item inside the section supports the following block settings:

| Setting ID | Type | Description |
| :--- | :--- | :--- |
| `product` | Product | Shopify Product picker for card link & default title. |
| `product_name` | Text | Custom Product Name override in subtle dark grey font (e.g. `"Japanese Rubber Broom"`). |
| `custom_link` | URL | Optional custom URL link override. |
| `author` | Text | Name of the reviewer (default: `"James Anderson"`). |
| `country` | Select | Reviewer country (`australia` or `new_zealand`). |
| `content` | Rich Text | Testimonial quote body text. |
| `show_rating` | Checkbox | Toggles display of the 5-star rating row (default: `true`). |
| `rating` | Range | Star rating count from `1` to `5` (default: `5`). |

---

## Section Settings

| Setting ID | Type | Description |
| :--- | :--- | :--- |
| `title` | Text | Section heading text (default: `"What they're saying"`). |
| `subheading` | Text | Section subheading description text. |

# MAR26 Testimonials Section (`mar26-testimonials.liquid`)

A high-impact, premium testimonial spotlight section featuring an infinite-looping marquee carousel, country-specific verified customer badges, star rating controls, and background grain texture overlay.

## Key Features & Behavior

- **Infinite Marquee Engine**: Liquid duplicates block items 3x (`{% for i in (1..3) %}`) and the `mar26-testimonials` Custom Web Component continuously scrolls the container horizontally via `requestAnimationFrame`. When scrolling reaches boundary thresholds, JS teleports `scrollLeft` seamlessly.
- **Interactive Pause**: Pauses scrolling when hovered (`mouseenter`/`mouseleave`) or touched (`touchstart`/`mousedown` for 2.5s).
- **Responsive Navigation Controls**: Desktop renders previous/next arrow buttons (`data-prev`, `data-next`) that scroll by card width. On mobile viewports (<768px), control buttons are hidden and native touch momentum scrolling (`overflow-x: auto`) is enabled.
- **Design Tokens**: Uses global theme design tokens defined in [mar26-foundation.css.liquid](file:///C:/code/BrightTools/worktrees/main/assets/mar26-foundation.css.liquid) for colors (`--mar26-clr-white`, `--mar26-clr-pink`, `--mar26-clr-black`) and typography (`--mar26-font-stack`, `--mar26-fw-extrabold`, `--mar26-fw-medium`).
- **Country Badge Integration**: Supports country chip flags (Australia `country-flags--AU` and New Zealand `country-flags--NZ`) using `country-flags.css`.

---

## Block Types (`testimonial`)

Each testimonial item inside the section supports the following block settings:

| Setting ID | Type | Description |
| :--- | :--- | :--- |
| `author` | Text | Name of the reviewer (default: `"James Anderson"`). |
| `country` | Select | Reviewer country (`australia` or `new_zealand`). |
| `content` | Rich Text | Testimonial quote body text. |
| `show_rating` | Checkbox | Toggles display of the 5-star rating row (default: `true`). |
| `rating` | Range | Star rating count from `1` to `5` (default: `5`). |

---

## Section Settings

| Setting ID | Type | Description |
| :--- | :--- | :--- |
| `title` | Text | Section heading text (default: `"What they're saying"`). Rendered alongside a pink star SVG. |
| `subheading` | Text | Section subheading description text. |

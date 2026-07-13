# Short Description & Highlights

Summarizes the architecture, features, and design tokens of the March 2026 custom short description storefront component.

## Summary
The short description component displays a compact, rich text overview of the product followed by a list of up to three bulleted key highlights (features/selling points). It is rendered via the snippet [mar26-short-description.liquid](file:///C:/code/BrightTools/worktrees/main/snippets/mar26-short-description.liquid) and is managed as a theme section block.

## Layout & Architecture
* **Metafields Integration**: Displays description content dynamically sourced from the product metafield `product.metafields.custom.mar_26_highlights_description.value`, falling back to `block.settings.description`.
* **Bullet Points**: Renders up to three bullet points defined via block settings `highlight_1`, `highlight_2`, and `highlight_3`. Each bullet is accompanied by a custom styled SVG checkmark icon.
* **Mobile Responsiveness**: Enforces centering on screens under `1000px` with a maximum width boundary of `32rem` (`512px`).

## Design Tokens (Scaled to 1.667x / 20px)

| Token Area | Property | Value | Editable |
| :--- | :--- | :--- | :--- |
| **Card Container** | Background Color | `#fff` | No (hardcoded) |
| **Card Container** | Border | `none` | No (hardcoded) |
| **Card Container** | Border Radius | `1rem` (16px) | No (hardcoded) |
| **Card Container** | Padding | `13px` | No (hardcoded) |
| **Card Container** | Margin Top | `23px` | No (hardcoded) |
| **Description Text** | Font Size | `20px` | No (hardcoded) |
| **Description Text** | Color | `#1e293b` (slate-800) | No (hardcoded) |
| **Description Text** | Line Height | `1.45` | No (hardcoded) |
| **Highlight Text** | Font Size | `20px` | No (hardcoded) |
| **Highlight Text** | Font Weight | `500` (Medium) | No (hardcoded) |
| **Highlight Text** | Color | `#334155` (slate-700) | No (hardcoded) |
| **Highlight Text** | Line Height | `1.35` | No (hardcoded) |
| **Highlight Text** | Gap | `13px` | No (hardcoded) |
| **Icon Wrapper** | Dimensions | `27px` x `27px` | No (hardcoded) |
| **Icon Wrapper** | Color | `block.settings.icon_color` (Default: `#e11d48`) | **Yes** (via Block Settings) |
| **Icon Wrapper** | Background Color | `icon_color` with 10% opacity | **Yes** (via Block Settings) |
| **Icon SVG Checkmark**| Dimensions | `13px` x `13px` | No (hardcoded) |
| **Icon SVG Checkmark**| Stroke Width | `3` | No (hardcoded) |

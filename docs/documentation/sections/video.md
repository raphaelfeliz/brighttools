# Video Section (`video.liquid`)

A high-performance media section designed to render native HTML5 video or embedded external players (YouTube/Vimeo) as a full-bleed block or rounded container.

## Key Features & Behavior

- **Autoplay vs. Controls**: When autoplay is enabled, videos are automatically muted to conform to modern browser security policies, and player controls are hidden. 
- **Mobile Video Source**: Supports a distinct mobile video file to optimize loading speed and aspect ratio on smaller viewports.
- **Overlay & Typography**: Renders overlay texts, subheadings, buttons, and review badges directly on top of the media.

> [!IMPORTANT]
> **Overlay "Video" Text**: By default, this section initializes with a nested **Heading** block containing the default text `"Video"`. This text is overlaid on the media. It can be cleared or deleted in the Shopify Customizer sidebar without any code changes.

---

## Block Types

The section supports the following nested blocks:

| Block Type | Settings Label | Purpose |
| :--- | :--- | :--- |
| `play` | Play Button | Shows a custom play button overlay (hidden if Autoplay is active). |
| `subheading` | Subheading | Renders a small, bold text block above the title. |
| `heading` | Heading | Renders the section header (e.g., `"Video"`) with selectable heading tag sizes (`h0` through `h6`). |
| `richtext` | Paragraph | Renders a paragraph block for descriptive content. |
| `button` | Button | Renders an interactive call-to-action button (supports Outline or Fill styles). |

---

## Section Settings

| Setting ID | Type | Description |
| :--- | :--- | :--- |
| `full_width` | Checkbox | Toggles full-width layout (removes side margins and corner rounding). |
| `allow_transparent_header` | Checkbox | Allows the header background to overlay the section if it is the first element on the page. |
| `autoplay` | Checkbox | Enables autoplay with browser-enforced muting. |
| `video_size` | Select | Sets height parameters (Original aspect ratio, Small, Medium, Large, Fill screen). |
| `video` | Video | Native Shopify video upload object (takes priority over external URLs). |
| `mobile_video` | Video | Native video upload optimized for mobile viewports. |
| `external_video_url` | Video URL | Fallback URL for hosted YouTube or Vimeo videos. |
| `poster` | Image Picker | Image preview/cover displayed before play (only if Autoplay is disabled). |
| `text_color` | Color | Configures typography overlay color. |
| `overlay_color` | Color | Configures color for the backing overlay. |
| `overlay_opacity` | Range | Sets transparency percentage (0-100%) for the backing overlay. |

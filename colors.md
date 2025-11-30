# Colors Used in `black_friday_test.html`

This document lists all colors used in the file, including their hex and RGB values, and where they are used.

---

## Main Palette

| Name      | Hex       | RGB                | Usage/Location                                  |
|-----------|-----------|--------------------|-------------------------------------------------|
| Purple    | #9a69a7   | rgb(154, 105, 167) | CSS variable `--bf-yellow-glow`, gradients, glow|
| Blue      | #4e859e   | rgb(78, 133, 158)  | CSS variable `--bf-green-glow`, gradients, glow |
| Yellow    | #f9e504   | rgb(249, 229, 4)   | CSS variable `--bf-red`, highlights, badges     |

---

## Other Colors

| Name      | Hex       | RGB                | Usage/Location                                  |
|-----------|-----------|--------------------|-------------------------------------------------|
| Black     | #000000   | rgb(0, 0, 0)       | Backgrounds, buttons, badges                    |
| White     | #ffffff   | rgb(255, 255, 255) | Text, backgrounds, shadows                      |
| Gray      | #111111   | rgb(17, 17, 17)    | Card backgrounds (`--bf-card`)                  |
| Light Gray| #f4f4f4   | rgb(244, 244, 244) | Body background                                 |
| Medium Gray| #555555  | rgb(85, 85, 85)    | Separator text                                  |
| Border Gray| #333333  | rgb(51, 51, 51)    | Card borders                                    |
| Badge Gray| #888888   | rgb(136, 136, 136) | Old price text                                  |
| Card White| #fff      | rgb(255, 255, 255) | Card image backgrounds                          |
| Card Border| #444444  | rgb(68, 68, 68)    | Card button border                              |

---

## CSS Variables

| Variable           | Hex       | RGB                | Purpose/Location         |
|--------------------|-----------|--------------------|--------------------------|
| --bf-red           | #f9e504   | rgb(249, 229, 4)   | Main accent (yellow)     |
| --bf-yellow-glow   | #9a69a7   | rgb(154, 105, 167) | Glow/badge (purple)      |
| --bf-green-glow    | #4e859e   | rgb(78, 133, 158)  | Glow/badge (blue)        |
| --bf-bg            | #050505   | rgb(5, 5, 5)       | Section background       |
| --bf-card          | #111111   | rgb(17, 17, 17)    | Card background          |

---

## Gradients & Shadows

- **Gradient Blue:** `rgba(78, 133, 158, 0.15)` / **Hex:** #4e859e (used in radial-gradient)
- **Gradient Purple:** `rgba(154, 105, 167, 0.15)` / **Hex:** #9a69a7 (used in radial-gradient)
- **Glow Blue:** `rgba(78, 133, 158, 0.4)` / **Hex:** #4e859e (used in box-shadow)
- **Glow Purple:** `rgba(154, 105, 167, 0.7)` / **Hex:** #9a69a7 (used in box-shadow)
- **Glow Yellow:** `rgba(249, 229, 4, 0.5)` / **Hex:** #f9e504 (used in text-shadow)

---

## JavaScript CONFIG

| Key           | Hex       | RGB                | Purpose/Location         |
|---------------|-----------|--------------------|--------------------------|
| CYBER_BLUE    | #4e859e   | rgb(78, 133, 158)  | JS color reference       |
| CYBER_PURPLE  | #9a69a7   | rgb(154, 105, 167) | JS color reference       |
| CYBER_GREEN   | #f9e504   | rgb(249, 229, 4)   | JS color reference       |

---

## Example Usage Snippets

```css
--bf-red: #f9e504; /* YELLOW */
--bf-yellow-glow: #9a69a7; /* PURPLE */
--bf-green-glow: #4e859e; /* BLUE */
background-image:
  ...
  radial-gradient(circle at 20% 30%, rgba(78, 133, 158, 0.15) ...), /* blue #4e859e */
  radial-gradient(circle at 80% 70%, rgba(154, 105, 167, 0.15) ...); /* purple #9a69a7 */
```

---

**All colors above are used in `black_friday_test.html` for backgrounds, gradients, glows, text, and UI elements.**

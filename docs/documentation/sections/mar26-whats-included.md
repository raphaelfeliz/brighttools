# MAR26 What's Included Section (`mar26-whats-included.liquid`)

## Overview
Grid-based section displaying included bundle products and item cards with high-density layout and automatic product data resolution.

---

## Card Architecture (Centered Image & Equalized Spacing Layout)
Each card renders:
1. **Product Image**: `600x600` featured image centered inside a square 1:1 container with equal `1rem` padding and `object-fit: contain`.
2. **Included Badge**: Crimson pill badge (`INCLUDED`) with `0.375rem` top margin *(6px gap above chip)* and `0.375rem` bottom margin *(6px gap below chip)*.
3. **Product Title**: Bold header (`1.25rem`, Montserrat) with `0.75rem` bottom margin.
4. **Feature Specs**: Up to 3 highlight specs with checkmark icons (`custom.mar26_highlight_1..3`) spaced at `0.375rem` (20% tighter).

*Note: Card description text, description schema setting, and specs top divider line were removed to optimize card height.*

---

## Technical Specifications
- **File**: `sections/mar26-whats-included.liquid`
- **Version**: `1.7.0 - Centered Image & Equal Padding`
- **Supported Binding**: `custom.included_products` product reference list or `item` block product picker.

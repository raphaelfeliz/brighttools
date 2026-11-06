# Impact 7.2.0 Upgrade Conflict & Focus Audit

## Overview

- **Total Theme Files Scanned**: 309
- **Identical Content**: 35
- **Line Endings Only (Ignorable)**: 70
- **Fork Collisions (CRITICAL - Your custom code was removed)**: 9
- **Template & Config Drift (`templates/`, `config/`)**: 30
- **Pure Vendor Upgrades (Accept cleanly from 7.2.0)**: 161
- **New in Upstream 7.2.0**: 3
- **Local Only in Main**: 1

## 1. Critical Fork Collisions (Where to Focus First)

These core vendor files contain BrightTools customizations on `main` that Shopify's 7.2.0 update stripped out:

### `assets/theme.css`
- **Custom Tokens Found**: `mar26`
- **Custom Code Stripped in 7.2.0 (Sample)**:
```liquid
.mar26-title-tags {
```

### `layout/theme.liquid`
- **Custom Tokens Found**: `bt-, jdgm, mar26`
- **Custom Code Stripped in 7.2.0 (Sample)**:
```liquid
{{- 'mar26-foundation.css' | asset_url | stylesheet_tag -}}
<style>
.product-card .jdgm-preview-badge .jdgm-star.jdgm-star {
.product-card .jdgm-widget.jdgm-preview-badge.jdgm--done-setup, .jdgm-stars-collections {
</style>
{%- sections 'bt-header-group' -%}
{%- sections 'mar26-footer-group' -%}
```

### `sections/footer.liquid`
- **Custom Tokens Found**: `mar26`
- **Custom Code Stripped in 7.2.0 (Sample)**:
```liquid
<style>
--footer-font-family: var(--mar26-font-stack);
--footer-fw-semibold: var(--mar26-fw-semibold);
--footer-fw-extrabold: var(--mar26-fw-extrabold);
.footer .mar26-newsletter-title {
/* MAR26 Newsletter Spotlight Styling */
.mar26-newsletter-title {
.mar26-newsletter-title span.accent {
```

### `sections/header.liquid`
- **Custom Tokens Found**: `mar26`
- **Custom Code Stripped in 7.2.0 (Sample)**:
```liquid
--header-font-family: var(--mar26-font-stack);
--header-font-weight: var(--mar26-fw-semibold);
font-weight: var(--mar26-fw-extrabold) !important;
font-weight: var(--mar26-fw-semibold) !important;
<span class="header__logo-text mar26-title">{{ shop.name }}</span>
```

### `snippets/inventory.liquid`
- **Related Git Commits**: 320ba2a feat(product): scale title typography, sync atc/shop pay buttons, integrate dealeasy and selleasy across 10 bt-* templates, and center dealeasy grid layout

### `snippets/option-value.liquid`
- **Custom Tokens Found**: `mar26`
- **Custom Code Stripped in 7.2.0 (Sample)**:
```liquid
<span class="mar26-savings-badge">SAVE {{ savings }}%</span>
<{{ option_value_tag }} class="color-swatch {% if settings.color_swatch_style == 'rectangle' %}color-swatch--rectangle{% endif %} {% if size == 'sm' %}color-swatch--sm{% endif %} {% if disabled %}is-disabled{% endif %} {% if selected and option_value_tag == 'a' %}is-selected{% endif %} {% if white_label_list contains downcase_label %}ring-inset{% endif %} {% if settings.color_swatch_style == 'round' %}rounded-full{% endif %}" {% if show_tooltip %}data-tooltip="{{ label | default: value | escape }}"{% endif %} style="{{ swatch_style }}" {{ attributes }}>
```

### `snippets/price-list.liquid`
- **Custom Tokens Found**: `mar26`
- **Custom Code Stripped in 7.2.0 (Sample)**:
```liquid
MAR26 FORKED PRODUCT PRICE
```

### `snippets/product-card.liquid`
- **Custom Tokens Found**: `jdgm, judgeme`
- **Custom Code Stripped in 7.2.0 (Sample)**:
```liquid
<div class='jdgm-widget jdgm-preview-badge' data-id='{{ product.id }}'>
{{ product.metafields.judgeme.badge }}
<fieldset class="product-card__swatch-list h-stack {% if settings.color_swatch_style == 'rectangle' %}gap-2.5{% else %}gap-0.5{% endif %}" data-option-position="{{ product_option.position }}">
<a href="{{ product.url }}" data-instant class="color-swatch__view-more {% if settings.color_swatch_style == 'round' %}rounded-full{% endif %} text-xxs text-subdued">+{{ product_option.values.size | minus: 4 }}</a>
```

### `snippets/product-info.liquid`
- **Custom Tokens Found**: `mar26`
- **Custom Code Stripped in 7.2.0 (Sample)**:
```liquid
{%- when 'mar26_gradient_title' -%}
<style>
</style>
<div class="product-info__gradient-title v-stack gap-0" style="font-weight: {{ block.settings.font_weight }}; letter-spacing: -0.04em;">
<span class="mar26-solid-title" style="color: rgb(var(--text-color));">{{ top_text }}</span>
<span class="mar26-gradient-title" style="--gradient-color-1: {{ block.settings.color_1 }}; --gradient-color-2: {{ block.settings.color_2 }}; font-size: inherit; font-weight: inherit; padding-bottom: 0.15em; margin-bottom: -0.15em;">
{%- case block.settings.selector_style -%}
```

## 2. New in Upstream 7.2.0

- `assets/mar26-foundation copy.css`
- `snippets/cart-disclosures.liquid`
- `snippets/product-disclosures.liquid`

## 3. Local Only in Main

- `assets/collections-top-banner.png`

## 4. Template & Config Drift

JSON templates and settings where custom section blocks or presets changed:

- `config/settings_schema.json`
- `templates/collection.brooms-bt.json`
- `templates/collection.bundles-bt.json`
- `templates/collection.cleaning-products.json`
- `templates/collection.cleaningproducts-bt.json`
- `templates/collection.dustpans-bt.json`
- `templates/collection.floor-wipes-bt.json`
- `templates/collection.floor-wipes.json`
- `templates/collection.mar26-catalog.json`
- `templates/collection.microfibre-bt.json`
- `templates/collection.mops-bt.json`
- `templates/collection.shop-all-bt.json`
- `templates/collection.squeegees-bt.json`
- `templates/collection.toilet-bt.json`
- `templates/collection.windows-care-bt.json`
- `templates/gift_card.liquid`
- `templates/product.bt-brooms.json`
- `templates/product.bt-bundles.json`
- `templates/product.bt-cleaningproducts.json`
- `templates/product.bt-dustpans.json`
- `templates/product.bt-floor-wipes.json`
- `templates/product.bt-microfibre.json`
- `templates/product.bt-mops.json`
- `templates/product.bt-squeegees.json`
- `templates/product.bt-toilet.json`
- `templates/product.bt-windows-care.json`
- `templates/product.caravan-c-b-page.json`
- `templates/product.mar26-caravan-bundle-page.json`
- `templates/product.mar26-with-bundle-builder.json`
- `templates/product.mar26.json`

## 5. Pure Vendor Upgrades (Safe to accept)

Total 161 standard Impact files (locales, blocks, untouched vendor sections/snippets).

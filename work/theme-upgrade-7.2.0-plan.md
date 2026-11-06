# Plan: Impact 6.12.0 -> 7.2.0 Upgrade & Fork Reconciliation (`#188300787986`)

## 1. Classification: Deterministic vs. Careful Manual Merge

### A. 100% Deterministic (Automated / Zero-Token File Operations)
These files do not require LLM line-by-line inspection or manual editing and can be handled in bulk via scripted copy/keep rules:
- **161 Pure Vendor Upgrades (`locales/`, `blocks/`, untouched `sections/` & `snippets/`, `assets/theme.js`, `assets/vendor.min.js`)**: Copy directly from `worktrees/pull/` (7.2.0) into `main`. None of these files were customized in `main`.
- **2 New Upstream Snippets (`snippets/cart-disclosures.liquid`, `snippets/product-disclosures.liquid`)**: Copy from `worktrees/pull/` into `main` (required by Impact 7.2.0 product/cart templates).
- **105 Identical / Line-Ending-Only Files (including all standalone `mar26-*` and `bt-*` custom sections/snippets/CSS)**: Keep `main` as-is.
- **1 Local-Only Asset (`assets/collections-top-banner.png`)**: Keep `main` as-is; delete orphan `assets/mar26-foundation copy.css` from the target theme if unneeded.
- **1 Config Schema (`config/settings_schema.json`)**: Accept 7.2.0 version from `worktrees/pull/` (bumps version string to `7.2.0` and adds 6 lines of standard vendor schema).
- **28 Custom JSON Templates (`templates/collection.*-bt.json`, `templates/product.bt-*.json`, `templates/product.mar26*.json`)**: Keep `main` versions deterministically.
  - *Why*: During the automated update, Shopify's updater reverted the `"main"` section type inside these templates from `"mar26-catalog-engine"` / `"mar26-main-product"` back to stock `"main-collection"` / `"main-product"`, wiping your custom block trees (`category_banner`, `mar26_title_and_tags`, Dealeasy/Selleasy app blocks). Keeping `main` preserves all custom page architectures intact. (Only `templates/product.caravan-c-b-page.json` and `templates/product.mar26-caravan-bundle-page.json` have extra lines in `pull` and will be diff-checked before overwriting).

### B. Careful Manual Edit & Merge (9 Fork Collision Files)
These 9 files have both upstream Impact 7.2.0 changes and custom BrightTools (`mar26` / `bt-` / `jdgm`) code. For each file, we take the 7.2.0 file from `worktrees/pull/` as the base and surgical-port the exact custom hunks from `main`:
1. [`layout/theme.liquid`](file:///c:/code/BrightTools/layout/theme.liquid) (+24 custom lines)
2. [`assets/theme.css`](file:///c:/code/BrightTools/assets/theme.css) (+56 custom lines)
3. [`sections/header.liquid`](file:///c:/code/BrightTools/sections/header.liquid) (+96 custom lines)
4. [`sections/footer.liquid`](file:///c:/code/BrightTools/sections/footer.liquid) (+205 custom lines)
5. [`snippets/product-card.liquid`](file:///c:/code/BrightTools/snippets/product-card.liquid) (+52 custom lines)
6. [`snippets/price-list.liquid`](file:///c:/code/BrightTools/snippets/price-list.liquid) (+64 custom lines)
7. [`snippets/option-value.liquid`](file:///c:/code/BrightTools/snippets/option-value.liquid) (+54 custom lines)
8. [`snippets/product-info.liquid`](file:///c:/code/BrightTools/snippets/product-info.liquid) (+93 custom lines)
9. [`snippets/inventory.liquid`](file:///c:/code/BrightTools/snippets/inventory.liquid) (+25 custom lines)

---

## 2. Incremental Execution Phases & Testing Gates

To guarantee zero regressions and keep context small, we execute and push to unpublished theme **`188300787986`** in 4 vertical increments:

### Increment 1: Global Shell, Foundation CSS & Hero Recovery
- **Files**:
  - [`layout/theme.liquid`](file:///c:/code/BrightTools/layout/theme.liquid): Port `mar26-foundation.css` stylesheet tag, `.jdgm-preview-badge` inline styles, `{%- sections 'bt-header-group' -%}`, and `{%- sections 'mar26-footer-group' -%}` into the 7.2.0 file.
  - [`assets/theme.css`](file:///c:/code/BrightTools/assets/theme.css): Port `.mar26-title-tags` rules into the end of 7.2.0 `theme.css`.
- **Deploy & Test Gate 1**:
  - Push `--only layout/theme.liquid --only assets/theme.css` to theme `188300787986` and run verification pull per SOP.
  - **Visual Check**: Load homepage preview (`?preview_theme_id=188300787986`). Confirm `mar26-hero` red background, typography, buttons, and `bt-header-group` single-line layout are restored.

### Increment 2: Header & Footer Sections
- **Files**:
  - [`sections/header.liquid`](file:///c:/code/BrightTools/sections/header.liquid): Port `--header-font-family: var(--mar26-font-stack)`, font-weight overrides, and `.mar26-title` logo class into 7.2.0 `header.liquid`.
  - [`sections/footer.liquid`](file:///c:/code/BrightTools/sections/footer.liquid): Port `--footer-font-family` variables and `.mar26-newsletter-title` spotlight styles into 7.2.0 `footer.liquid`.
- **Deploy & Test Gate 2**:
  - Push `--only sections/header.liquid --only sections/footer.liquid` to `188300787986` and verify byte-for-byte.
  - **Visual Check**: Inspect header navigation weight/spacing, country selector absence/placement, and footer newsletter spotlight on preview.

### Increment 3: Collection Cards & Pricing Snippets
- **Files**:
  - [`snippets/product-card.liquid`](file:///c:/code/BrightTools/snippets/product-card.liquid): Port Judge.me badge (`product.metafields.judgeme.badge`) and custom swatch overflow counter (`+X`).
  - [`snippets/price-list.liquid`](file:///c:/code/BrightTools/snippets/price-list.liquid): Port `MAR26 FORKED PRODUCT PRICE` markup and classes.
  - [`templates/collection.*.json`](file:///c:/code/BrightTools/templates/collection.brooms-bt.json): Push the `main` versions of the collection JSON templates that were reverted to `main-collection` on `188300787986`.
- **Deploy & Test Gate 3**:
  - Push modified snippets and collection templates via `--only` flags to `188300787986` and verify.
  - **Visual Check**: Check `/collections/brooms` and `/collections/floor-wipes` on preview. Verify `mar26-catalog-engine` category banners, Judge.me stars, and card prices.

### Increment 4: Product Page (PDP) Snippets & Templates
- **Files**:
  - [`snippets/product-info.liquid`](file:///c:/code/BrightTools/snippets/product-info.liquid): Port `when 'mar26_gradient_title'` block handler and selector style cases.
  - [`snippets/option-value.liquid`](file:///c:/code/BrightTools/snippets/option-value.liquid): Port `<span class="mar26-savings-badge">SAVE {{ savings }}%</span>` and custom swatch classes.
  - [`snippets/inventory.liquid`](file:///c:/code/BrightTools/snippets/inventory.liquid): Port commit `320ba2a` stock/ATC synchronization logic.
  - [`templates/product.bt-*.json`](file:///c:/code/BrightTools/templates/product.bt-brooms.json) & [`templates/product.mar26*.json`](file:///c:/code/BrightTools/templates/product.mar26.json): Reconcile the 2 caravan templates and push the `mar26-main-product` JSON templates to `188300787986`.
- **Deploy & Test Gate 4**:
  - Push PDP snippets and product templates via `--only` flags to `188300787986`, run `shopify theme check`, and verify pull.
  - **Visual Check**: Test a `bt-*` product page and bundle page on preview (variant switching, savings badge, Dealeasy/Selleasy widgets, ATC button).

---

## 3. Token-Efficiency & Guaranteed Implementation Guidelines

1. **Diff-Only Context Loading (Never Read Full Vendor Files)**:
   - Files like `assets/theme.css` (15,000+ lines) or `sections/header.liquid` (1,200+ lines) waste massive token context if read in full.
   - Guideline: Run `git diff --unified=3 worktrees/pull/<file> <file>` via a Python helper to extract only the exact line numbers and surrounding 3-line anchors of custom code before editing.
2. **Scripted Bulk Copy for the 164 Pure Vendor Files**:
   - Use a single Python script execution to copy the 161 `pure_vendor_upgrades` + 2 new snippets + `config/settings_schema.json` from `worktrees/pull/` to `main`. Zero LLM token generation spent on vendor code.
3. **Selective Push Only (Never Full Theme Push)**:
   - Target theme `188300787986` on Shopify *already has* the 161 updated 7.2.0 vendor files. We only need to `shopify theme push --only ...` the 9 reconciled Liquid/CSS files and the ~28 restored JSON templates to `188300787986`, cutting upload/verification time by 85%.
4. **Hardening for Future Theme Upgrades (Optional Post-Merge Step)**:
   - Where custom CSS was injected inline into `sections/header.liquid`, `sections/footer.liquid`, and `assets/theme.css`, we can optionally consolidate those rules into `assets/mar26-foundation.css` after parity is verified so future Impact updates have fewer file collisions.
5. **SOP Receipt & Git Hygiene**:
   - Record [`worktrees/receipts/2026-11-05T23-02-13Z.pull.md`](file:///c:/code/BrightTools/worktrees/receipts/) before modifying `main`, commit reconciled baseline on `main`, and record `.handover.md` and `.push.md` receipts at completion.

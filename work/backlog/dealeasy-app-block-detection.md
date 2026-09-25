# Investigate Dealasy App-Block Detection

**Status:** Suspected issue; not yet verified on the storefront.

## Agreed working strategy

1. Bring the reviewed Shopify pull into `main` as a clearly labeled **live baseline** commit. This records the current behavior; it does **not** mean the Dealasy suppression is correct or that this issue is closed.
2. Keep this backlog item open as known technical debt. Investigate and fix it in a later, separate change rather than delaying unrelated urgent work.
3. Make urgent changes on `main` in separate commits, not on `fix-add-wipes`. If urgent work touches a theme file that still differs from the pull, reconcile that file first so the new work starts from a known baseline.

## Observation

The current Shopify pull contains Liquid checks that try to identify Dealasy app blocks with `block.type contains 'dealeasy'` in:

- `sections/mar26-addons-buy.liquid`
- `snippets/mar26-product-info.liquid`
- `snippets/product-info.liquid`

The first check is inside the `when '@app'` case. Shopify's documented theme pattern identifies app blocks using the generic `@app` block type and renders them with `{% render block %}`. This raises a concern that these checks cannot distinguish Dealasy from other apps, or may never match Dealasy blocks at all.

## Impact to determine

The code comments say Dealasy rendering is suppressed, but that intent may not match the actual behavior. Confirm whether Dealasy blocks render on the affected product templates and whether suppressing them is still desired. Other app blocks may also be affected if the implementation is changed broadly.

## Recommended investigation

1. Inspect the exact app-block data exposed to Liquid for the affected templates; do not infer the app identity from `block.type` alone.
2. Reproduce on an unpublished theme with a Dealasy block and at least one non-Dealasy app block.
3. Confirm the desired behavior with the user before implementing a behavior change or pushing a fix to the live theme.
4. If a fix is needed, make the detection specific and verify both Dealasy and other app blocks in the theme editor and storefront.

No theme code or Shopify configuration was changed while recording this backlog item.

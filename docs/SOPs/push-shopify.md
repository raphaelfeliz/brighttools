# SOP: Shopify Theme Pull, Reconciliation, Testing, and Push

## Purpose and paths

- Store: `brighttools-au.myshopify.com`
- Source theme: repository root (`C:\\code\\BrightTools`), tracked by the `main` branch.
- Pull snapshot: `worktrees/pull/`, a linked Git worktree on the `shopify-pulls` branch. This branch contains only the downloaded theme files.
- Receipts: `worktrees/receipts/`, tracked on `main`.
- Default: use the specified unpublished theme for testing and deployment. Never rely on Shopify CLI's default or interactive theme selection.
- Keep Shopify pulls as commits on `shopify-pulls`. Do not merge that archival branch wholesale into `main`.

## Required theme preflight

Before every pull, push, or live test:

1. Run `shopify theme list --store brighttools-au.myshopify.com`.
2. Match the intended theme by both name and ID; verify whether Shopify marks it as live or unpublished. If either is unclear, stop and resolve the target before proceeding.
3. Pass the confirmed `--theme <THEME_ID>` explicitly in the command. Never omit the theme ID or substitute the live theme because it is Shopify's default.
4. For any operation on the live theme, obtain explicit user approval for that specific operation. The live-testing exception in this SOP applies only when the feature cannot be tested on an unpublished theme.

## Pull and reconcile before development

1. Verify that the repository root is checked out on `main` and has no uncommitted theme changes. Do not create or use a nested `worktrees/main/` checkout.
2. Verify that `worktrees/pull/` is a registered Git worktree on `shopify-pulls`. Pull the selected Shopify theme there using the explicit store and theme ID. Commit the complete snapshot with store, theme ID/name, and UTC pull time. If the files are unchanged, make an empty dated commit to record the successful pull. Each earlier commit remains available for rollback.
3. Save `worktrees/receipts/<timestamp>.pull.md` on `main`. Include the UTC timestamp, store, theme ID/name and live status, `Outcome-Status`, snapshot commit SHA, file count, and any error. Mark reconciliation pending until comparison is complete.
4. Compare the snapshot against the repository root by file set and content. Distinguish line-ending-only differences from content changes. Review and classify every content difference before copying approved files into the repository root.
5. Decide changes with the user in batches where practical, or individually when needed. Always give a recommendation and explain material live-only changes.
   - Theme editor data, including JSON templates and settings, generally follows Shopify's live state.
   - Liquid, JavaScript, and CSS generally follow the local source.
   - These are defaults, not automatic overwrite rules. Surface major live-only functionality for an explicit decision.
6. Apply only approved changes to the repository root. Once all differences are resolved, review and commit the reconciled baseline on `main` before feature work starts. Commit the pull snapshot on `shopify-pulls`, then merge that branch into `main` and commit the merge.
7. Add `worktrees/receipts/<timestamp>.handover.md` on `main`, recording each decision, the snapshot SHA, the reconciled `main` commit SHA, remaining exceptions, and the outcome. Commit the handover separately so its own SHA need not be embedded in the file. Keep the pull receipt and handover on `main`; do not merge the archival branch to transfer them.

## Develop, test, and approve

1. Make the requested changes on `main`; follow the project's version-bump rules for code files.
2. Test on an unpublished theme by default. Run `shopify theme check` when applicable and verify relevant storefront behavior.
3. Live-theme testing is an exception, allowed only when the feature cannot be tested on an unpublished theme. Before testing, document why live is required, the exact change and scope, expected impact, and rollback steps; obtain the user's approval. Keep the change minimal and restore temporary changes after the test.
4. Present results and obtain approval. Commit the approved changes on `main` before pushing.

## Push

Push only files changed and approved for this deployment to the confirmed theme. Specify every file with its own `--only` flag; never pass a comma-separated list. Shopify CLI can report a successful upload even when it uploaded zero files, so command success alone is not proof that the push worked.

```powershell
shopify theme push --theme <THEME_ID> --path C:\code\BrightTools --store brighttools-au.myshopify.com --only <FILE_1> --only <FILE_2>
```

For a live theme, use `--allow-live` only when the user explicitly authorized a live push. Check the CLI output and confirm that the expected files were uploaded.

## Verify after push

1. Immediately after the push command completes, pull the same changed files from the same theme ID into `worktrees/pull/` on `shopify-pulls`, using one `--only` flag per file. Do not proceed based on the push's success message alone.
2. Compare every pulled file byte-for-byte with its approved local counterpart in the repository root. Require exact matches for all files pushed. Require a full-theme match only when the full theme was deployed and no one changed it during verification.
3. Investigate and report every missing or different file. Do not overwrite it automatically. Record the comparison result and any exception in a timestamped push receipt on `main`, then commit the verification snapshot with its UTC time and theme ID.

Example verification pull:

```powershell
shopify theme pull --theme <THEME_ID> --path C:\code\BrightTools\worktrees\pull --store brighttools-au.myshopify.com --only <FILE_1> --only <FILE_2>
```

## Example: push selected files

```powershell
shopify theme push --theme 180366573842 --path C:\code\BrightTools --store brighttools-au.myshopify.com --only snippets/mar26-product-gallery.liquid --only templates/product.bt-brooms.json
```

Shopify CLI reference: [theme pull](https://shopify.dev/docs/api/shopify-cli/theme/theme-pull), [theme push](https://shopify.dev/docs/api/shopify-cli/theme/theme-push), and [Theme Check](https://shopify.dev/docs/storefronts/themes/tools/theme-check).

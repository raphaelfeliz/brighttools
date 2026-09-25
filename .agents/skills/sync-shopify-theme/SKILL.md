---
name: sync-shopify-theme
description: Pull, reconcile, selectively push (--only), and verify Shopify themes on brighttools-au.myshopify.com.
---

# Sync Shopify Theme

## Preconditions
- Store identifier: `brighttools-au.myshopify.com`.
- Source path: `worktrees/main/`.
- Snapshot worktree: `worktrees/pull/` on the orphan `shopify-pulls` branch.
- Receipt path: `worktrees/receipts/` on `main`.
- Follow `docs/SOPs/push-shopify.md` for decision and approval gates.

## Procedure
1. **Preflight**:
   - Run `shopify theme list --store brighttools-au.myshopify.com`.
   - Confirm target theme name and ID (default to unpublished theme).
   - If operating on a live theme, confirm explicit authorization for that operation. Pass `--allow-live` for a live push only; the installed CLI does not support it on pull.
2. **Pull & Reconcile (Before Development)**:
   - Verify a clean `main` checkout and a registered, clean `worktrees/pull/` worktree on `shopify-pulls`. Preserve unrelated dirty checkouts.
   - Pull theme into `worktrees/pull/`:
     `shopify theme pull --theme <THEME_ID> --path C:\code\BrightTools\worktrees\pull --store brighttools-au.myshopify.com`
   - Commit the snapshot on `shopify-pulls`; use a dated empty commit if the file content is unchanged.
   - Save `<timestamp>.pull.md` on `main` with UTC timestamp, theme ID/name/status, outcome, file count, and snapshot SHA.
   - Compare file sets and contents against `worktrees/main/`. Separate line-ending differences from substantive changes.
   - Present differences with recommendations in batches or individually. Apply only user-approved reconciliation changes and commit the baseline on `main`.
   - Save and commit `<timestamp>.handover.md` on `main` with decisions, snapshot and main commit SHAs, exceptions, and outcome. Never merge the archival branch wholesale.
3. **Selective Push (`--only`)**:
   - Execute push specifying each file with its own discrete `--only` flag:
     `shopify theme push --theme <THEME_ID> --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only <FILE_1> --only <FILE_2>`
4. **Post-Push Verification Pull**:
   - Immediately pull the exact changed files into `worktrees/pull/`:
     `shopify theme pull --theme <THEME_ID> --path C:\code\BrightTools\worktrees\pull --store brighttools-au.myshopify.com --only <FILE_1> --only <FILE_2>`
   - Perform byte-for-byte comparison against `worktrees/main/`. Require exact match.
5. **Receipt & Commit**:
   - Record post-push verification in `worktrees/receipts/<timestamp>.push.md` on `main`.
   - Commit the verification pull on `shopify-pulls` and receipt on `main`.

## Gotchas & Edge Cases
- Never pass comma-separated files to `--only`; Shopify CLI requires separate `--only <file>` flags.
- Shopify CLI can report success with 0 files uploaded; post-push pull verification is mandatory.
- Never rely on default or interactive theme selection; always pass `--theme <ID>`.

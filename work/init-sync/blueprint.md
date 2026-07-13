# Initiative Blueprint: Shopify Sync

## Target End-State ("What")
- Track all Shopify theme sync operations (pulls and pushes) as distinct increments and work packages.
- Keep the local directory tree structured with theme files isolated in a dedicated worktree (`worktrees/main`) and project documentation outside in `docs`.

## Technical Specifications
- Staging theme ID is `180366573842` on `brighttools-au.myshopify.com`.
- **Initial Pull**: The initial pull will go directly into the `worktrees/main` folder to establish the baseline.
- **Subsequent Pulls**:
  1. Pull remote theme changes to a temporary comparison folder (`worktrees/pull`).
  2. Compare `worktrees/pull` against `worktrees/main` to identify diffs.
  3. Reconcile/merge approved changes into `worktrees/main`.
  4. Delete the temporary `worktrees/pull` folder.
- **Push Operations**: Sync local code changes back to Shopify using specific theme push CLI commands.

## Non-Goals
- Maintaining full git history on the remote Shopify servers (theme push only syncs source assets, not git commits).

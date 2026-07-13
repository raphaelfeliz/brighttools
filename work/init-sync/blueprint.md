# Initiative Blueprint: Shopify Sync

## Target End-State ("What")
- Track all Shopify theme sync operations (pulls and pushes) as distinct increments and work packages.
- Keep the local directory tree structured with theme files isolated in a dedicated worktree (`worktrees/main`) and project documentation outside in `docs`.

## Technical Specifications
- Staging theme ID is `180366573842` on `brighttools-au.myshopify.com`.
- **Initial Pull**: The initial pull will go directly into the `worktrees/main` folder to establish the baseline.
- **Subsequent Pulls**:
  1. Pre-create the temporary folder (`worktrees/pull`) if it does not exist (Shopify CLI requires target path existence).
  2. Pull remote theme changes to the temporary comparison folder (`worktrees/pull`).
  3. Compare `worktrees/pull` against `worktrees/main` to identify diffs and format changes.
  4. Present a summary of changes to the user for explicit confirmation before merging:
     - Mention new files (e.g., `New Template: product.bt-brooms.json was added`).
     - Provide a concise summary of theme editor configuration changes (JSON templates).
     - Provide a detailed diff if any code files (non-JSON assets, liquid snippets/sections, etc.) are different.
  5. Reconcile/merge approved changes into `worktrees/main`.
  6. Automatically run registry sync scripts (`generate_custom_templates_summary.py` and `generate_sections_registry.py`) to update documentation.
  7. Delete the temporary `worktrees/pull` folder.
- **Push Operations**: Sync local code changes back to Shopify using specific theme push CLI commands.

## Non-Goals
- Maintaining full git history on the remote Shopify servers (theme push only syncs source assets, not git commits).

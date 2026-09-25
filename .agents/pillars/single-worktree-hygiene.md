# Pillar: Worktree & Git Hygiene

## Principle
`worktrees/main/` is the source theme tracked on `main`. `worktrees/pull/` is a linked Git worktree on the archival `shopify-pulls` branch. Changes to the source must be reviewed and committed on `main`.

## Non-Negotiable Directives
1. **Clean Baseline**: Use a clean `main` checkout for reconciliation and deployment. Preserve unrelated dirty checkouts without switching or resetting them.
2. **Snapshot Preservation**: Commit each remote pull in the registered `worktrees/pull/` worktree on `shopify-pulls`, including a dated empty commit when the remote files are unchanged.
3. **Atomic Commits**: Stage and commit approved changes on `main` before initiating remote pushes.

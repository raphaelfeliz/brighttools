# Worktrees

- The repository root is the source checkout on `main`.
- `worktrees/pull/` is the only auxiliary checkout, on `shopify-pulls`.
- Do not create `worktrees/main/`; it duplicates the source checkout and causes branch confusion.

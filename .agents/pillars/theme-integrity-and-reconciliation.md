# Pillar: Theme Integrity & Reconciliation

## Principle
Shopify remote state and local repository files must never diverge silently. Every deployment requires deterministic preflight validation, surgical upload, and post-push byte-for-byte verification.

## Non-Negotiable Directives
1. **No Blind Pushes**: Never rely on Shopify CLI's success output alone. Always perform an immediate verification pull into snapshots.
2. **Explicit Targeting**: Always specify store (`brighttools-au.myshopify.com`) and theme ID explicitly in CLI commands.
3. **Discrete File Flags**: When pushing selective changes, pass individual `--only <file>` parameters; never pass comma-separated strings.

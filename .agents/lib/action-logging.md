# Sub-Routine: Action Logging & Receipts

## Purpose
Standardizes writing verifiable execution and sync receipts for BrightTools theme operations.

## Procedure
1. Create or open the target receipt on `main` at `worktrees/receipts/<timestamp>.<action>.md`. Use the same UTC timestamp for the related pull receipt and handover.
2. Format receipt containing:
   - **Timestamp**: ISO-8601 UTC timestamp.
   - **Store, Theme ID, Name, Status**: Verified Shopify target.
   - **Action and Outcome-Status**: Pull, push, or check; success, failure, or pending reconciliation.
   - **Snapshot Commit SHA**: Commit on `shopify-pulls` for a pull or verification pull.
   - **File Count / Files Touched**: Count for a full pull; individual `--only` paths for a selective operation.
   - **Comparison / Verification**: Content differences, line-ending-only differences, or byte-for-byte push verification.
3. Save and commit the receipt on `main`. After approved reconciliation, add `<timestamp>.handover.md` with decisions, the reconciled `main` commit SHA, exceptions, and outcome; commit that separately.

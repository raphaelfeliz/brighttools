# Sub-Routine: Shopify Theme Preflight

## Purpose
Enforces deterministic validation of target theme ID and status before executing any Shopify CLI operations.

## Procedure
1. Run `shopify theme list --store brighttools-au.myshopify.com`.
2. Inspect output to match target theme name and numeric ID.
3. Check whether the target theme is marked `live` or `unpublished`.
4. If target is `live`, confirm explicit user approval for the specific operation. Use `--allow-live` for an authorized live **push**; the installed CLI does not accept it for a pull. For pulls, pass the approved numeric theme ID with `--theme`.
5. If target ID is ambiguous or not listed, halt immediately and request clarification.

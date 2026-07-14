# SOP: Pushing Files to Shopify Theme

## 1. Context
When pushing changes to a Shopify store theme via the Shopify CLI, specifying exact files is critical to prevent accidental overwrites of unrelated files.

## 2. CLI Flag Syntax Pitfall
- **Issue**: Standard CLI tool behavior often permits comma-separated lists for file filters (e.g. `--only file1.liquid,file2.json`). 
- **Shopify CLI Behavior**: Shopify CLI does **not** parse comma-separated lists. It interprets the comma-separated string as a single literal filepath. Because no single file matches this composite name, the CLI silently uploads `0` files (whilst still reporting success with `100% upload complete`).

## 3. Correct Push Command Format
To push multiple specific files, you must repeat the `--only` flag for **each individual file**:

```bash
shopify theme push --theme <THEME_ID> --path <PATH_TO_THEME> --store <STORE_NAME>.myshopify.com --only <FILE_1> --only <FILE_2> --allow-live
```

### Example:
```bash
shopify theme push --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com --only snippets/mar26-product-gallery.liquid --only templates/product.bt-brooms.json --allow-live
```

## 4. Verification Check
After running a push command that targets specific files:
1. Double-check the CLI output to ensure actual files were uploaded.
2. If in doubt, verify the push by pulling the target file back from the remote theme to a temporary/scratch directory and comparing it to your local workspace changes.

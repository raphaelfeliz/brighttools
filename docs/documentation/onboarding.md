# ONBOARDING

## Project Context & Overview
- **Project Name**: BrightTools Storefront Customizations
- **Purpose**: Developing and maintaining custom modular features (e.g., product card layouts, collection grid filtering, and catalog engine) on the Shopify storefront.
- **Namespaces**: Core custom components use prefix namespaces `mar26-` and `bt-` to isolate custom functionality from default theme code.
- **Repository Structure**:
  - `worktrees/main/`: Holds the active Shopify theme source codebase (layouts, snippets, sections, config, templates, etc.).
  - `docs/`: Stores project specifications, architecture guidelines, and SOPs.
  - `work/`: Tracks project tasks, increments, and sync metadata (initiatives).

## Prerequisites
- Node.js: `v24.13.0`
- Package Manager: `pnpm` (`C:\Users\rapha\AppData\Local\nvm\v24.13.0\pnpm.CMD`)
- CLI: `@shopify/cli`

## Environment Path Config
Run in PowerShell before invoking CLI tools:
```powershell
$env:Path = 'C:\Users\rapha\AppData\Local\nvm\v24.13.0;' + $env:Path
```

## Initial Setup
1. Local Root: `C:\code\BrightTools`
2. Sync Staging Theme:
   ```powershell
   shopify theme pull --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com
   ```

## Development Sync Workflow

### Pulling Changes (Subsequent)
To pull remote changes without overwriting local modifications:
1. Pull to temporary workspace:
   ```powershell
   shopify theme pull --theme 180366573842 --path C:\code\BrightTools\worktrees\pull --store brighttools-au.myshopify.com
   ```
2. Diff/compare `worktrees/pull` against `worktrees/main`.
3. Merge approved remote changes into `worktrees/main`.
4. Delete `worktrees/pull`.

### Pushing Changes
Always target non-live theme unless instructed.
Using sync configuration script:
```powershell
node scripts/push-shopify/index.js <path-to-sync-yaml>
```
Sync schema spec details in [infrastructure.md](file:///C:/code/BrightTools/docs/documentation/infrastructure.md).

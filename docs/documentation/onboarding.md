# ONBOARDING

## Project Context & Overview
- **Project Name**: BrightTools Storefront Customizations
- **Purpose**: Developing and maintaining custom modular features (e.g., product card layouts, collection grid filtering, and catalog engine) on the Shopify storefront.
- **Namespaces**: Core custom components use prefix namespaces `mar26-` and `bt-` to isolate custom functionality from default theme code.
- **Repository Structure**:
  - Repository root: Holds the active Shopify theme source codebase (layouts, snippets, sections, config, templates, etc.) on `main`.
  - `docs/`: Stores project specifications, architecture guidelines, and SOPs.
  - `work/`: Tracks project tasks, increments, and sync metadata (initiatives).

## GitHub Repository
- **Remote URL**: `git@github.com:raphaelfeliz/brighttools.git`
- **Primary Branch**: `main`

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
   shopify theme pull --theme 180366573842 --path C:\code\BrightTools --store brighttools-au.myshopify.com
   ```

## Development Sync Workflow

Follow the pull, reconciliation, testing, push, and verification procedure in [the Shopify theme SOP](../SOPs/push-shopify.md). Pull snapshots are committed on `shopify-pulls` and merged into `main`; the maintained theme and approved code changes live at the repository root.

### Pushing Changes
Push updated files via Shopify CLI or sync configuration script:
```powershell
node scripts/push-shopify/index.js <path-to-sync-yaml>
```
Sync schema spec details in [infrastructure.md](file:///C:/code/BrightTools/docs/documentation/infrastructure.md).

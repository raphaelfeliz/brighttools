# ONBOARDING

## Project Context & Overview
- **Project Name**: BrightTools Storefront Customizations
- **Purpose**: Developing and maintaining custom modular features (e.g., product card layouts, collection grid filtering, and catalog engine) on the Shopify storefront.
- **Namespaces**: Core custom components use prefix namespaces `mar26-` and `bt-` to isolate custom functionality from default theme code.
- **Repository Structure**:
  - `worktrees/main/`: Holds the active Shopify theme source codebase (layouts, snippets, sections, config, templates, etc.).
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
   shopify theme pull --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com
   ```

## Development Sync Workflow

### Pulling Changes (Subsequent)
To pull remote changes without overwriting local modifications:
1. **Commit Local Baseline**: Ensure all pending local modifications are committed to Git before pulling.
2. **Pre-create Target Workspace Directory**:
   ```powershell
   New-Item -ItemType Directory -Force -Path C:\code\BrightTools\worktrees\pull
   ```
3. **Pull Remote Theme**:
   ```powershell
   $env:Path = 'C:\Users\rapha\AppData\Local\nvm\v24.13.0;' + $env:Path
   shopify theme pull --theme 180366573842 --path C:\code\BrightTools\worktrees\pull --store brighttools-au.myshopify.com
   ```
4. **Diff & Categorize Changes**: Compare `worktrees/pull` against `worktrees/main` (`git diff --no-index --name-status worktrees/main worktrees/pull`).
5. **Merge Policy**:
   - **Shopify Customizer / JSON Templates**: Overwrite local files from `worktrees/pull` directly, as Shopify live customizer is the source of truth for section configs.
   - **Code Files (Liquid / JS / CSS)**: Perform line-by-line diff review and selectively merge approved changes.
6. **Workspace Cleanup / Retention**: Retain or clean up `worktrees/pull` based on active initiative preferences.



### Pushing Changes
1. **Pre-Push Baseline Commit & Rollback Strategy**: Before pushing any changes live or to staging, ensure local changes are committed to Git as a clean baseline checkpoint with a clear rollback strategy (`git restore` / `git revert`).
2. **Mandatory Version Bumping**: Always bump the component version number (in both the top header comment and internal `console.log` statement) whenever modifying code files. Explicitly inform the user of the new version number so they can verify they are inspecting the active code version in browser console/devtools.
3. **Targeting Themes**: Always target non-live theme unless explicitly instructed.
4. **Execution**: Push updated files via Shopify CLI or sync configuration script:
```powershell
node scripts/push-shopify/index.js <path-to-sync-yaml>
```
Sync schema spec details in [infrastructure.md](file:///C:/code/BrightTools/docs/documentation/infrastructure.md).



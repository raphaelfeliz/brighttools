# INFRASTRUCTURE

## Environment
- Host Platform: Shopify Storefront
- Target URL: `https://brighttools-au.myshopify.com`
- Shopify CLI Integration: Local integration via `@shopify/cli` node module.

## Workspace Directory Mapping
- Root: `C:\code\BrightTools`
- Production / Working Theme: `C:\code\BrightTools\worktrees\main`
- Shared/SOP Docs: `C:\code\BrightTools\docs`
- Task Management Tiers: `C:\code\BrightTools\work`
- Automation Scripts: `C:\code\BrightTools\scripts`

## Theme Sync Automation Schema
Automated pushes use YAML sync configuration files matching the schema below:
```yaml
event_type: "shopify sync"
description: "Sync changes description"
timestamp: "YYYY-MM-DDTHH:MM:SSZ"
theme:
  store: "brighttools-au.myshopify.com"
  id: 180366573842
  name: "[live] July 1 2026"
files:
  - path: "shopify/snippets/mar26-product-card-catalogv.liquid"
    version: "1.5.4"
    change: "Change summary details"
    status: "completed"
status: "completed"
```
*Note: Pushing script parses files status and automatically uploads matching paths using `--only` selectors.*

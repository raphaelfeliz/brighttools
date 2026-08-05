# Increment Blueprint: Initial Pull from Shopify

## Target End-State ("What")
- Reconstruct the local Shopify theme files inside the `worktrees/main` folder.
- The destination `C:\code\BrightTools\worktrees\main` should contain the assets, sections, snippets, templates, layout, config, and locales of the remote theme ID `180366573842`.

## Technical Specifications
- Execution of `shopify theme pull --theme 180366573842 --path C:\code\BrightTools\worktrees\main --store brighttools-au.myshopify.com`.

## Non-Goals
- Pulling files into the root folder directly. All theme files must be isolated to `worktrees/main`.

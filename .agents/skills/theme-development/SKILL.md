---
name: theme-development
description: Develop, customize, and validate Liquid sections, snippets, JSON templates, and CSS/JS assets in BrightTools.
---

# Theme Development

## Preconditions
- Local source code located in `worktrees/main/`.
- Shopify CLI installed for running Theme Check.

## Procedure
1. Execute authorization check: verify `asdf` token for mutations.
2. Implement requested Liquid section, snippet, or JSON template under `worktrees/main/`:
   - Follow semantic HTML and responsive CSS design patterns.
   - Maintain clean schema blocks in section files.
3. Validate syntax and linting:
   - Run `shopify theme check --path C:\code\BrightTools\worktrees\main`.
   - Resolve any warnings or errors.
4. Prepare modified files list for handoff to `sync-commit` specialist.

## Gotchas & Edge Cases
- Do not modify files outside `worktrees/main/` during feature development.
- Always verify schema JSON validity within Liquid sections before testing.

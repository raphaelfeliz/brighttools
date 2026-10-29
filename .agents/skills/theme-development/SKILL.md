---
name: theme-development
description: Develop, customize, and validate Liquid sections, snippets, JSON templates, and CSS/JS assets in BrightTools.
---

# Theme Development

## Preconditions
- Local source code is in the repository root, checked out on `main`.
- Shopify CLI installed for running Theme Check.

## Procedure
1. Execute authorization check: verify `asdf` token for mutations.
2. Implement requested Liquid section, snippet, or JSON template in the repository root:
   - Follow semantic HTML and responsive CSS design patterns.
   - Maintain clean schema blocks in section files.
3. Validate syntax and linting:
   - Run `shopify theme check --path C:\code\BrightTools`.
   - Resolve any warnings or errors.
4. Prepare modified files list for handoff to `sync-commit` specialist.

## Gotchas & Edge Cases
- Do not modify files in `worktrees/pull/` during feature development.
- Always verify schema JSON validity within Liquid sections before testing.

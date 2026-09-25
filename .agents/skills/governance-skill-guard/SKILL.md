---
name: governance-skill-guard
description: Validate and enforce architectural compliance of any modifications to skills, roles, or library files in BrightTools .agents/.
---

# Governance Skill Guard

## Preconditions
- Target modification affects files inside `C:\code\BrightTools\.agents/` or root `AGENTS.md`.

## Procedure
1. Verify role files in `.agents/roles/`:
   - Must not exceed 30 lines.
   - Must contain standard headings (`## Onboarding`, `## Responsibility`, `## Boundaries & Permissions`, `## Completion & Handoff`).
2. Verify skills in `.agents/skills/<skill-id>/SKILL.md`:
   - Single file per skill with valid YAML frontmatter (`name`, `description`).
   - No embedded scripts or binary files.
   - Shared subroutines externalized to `.agents/lib/`.
3. Record validation findings before applying changes.

## Gotchas & Edge Cases
- Do not add procedural execution steps to role files; procedures belong in skills.

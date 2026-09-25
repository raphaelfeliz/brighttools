# Sub-Routine: Agent Onboarding Ritual

## Purpose
Establishes the one-time initial onboarding procedure for any BrightTools agent upon startup. Agents execute this ritual once, then wait for user instructions.

## One-Time Onboarding Sequence
1. **Read Conversation & Workitem Rules** (once upon initial startup only; do not re-read per task):
   - [`E:\code\Nokk\projects\site-and-crm\.agents\conversation-rules\styling.md`](file:///E:/code/Nokk/projects/site-and-crm/.agents/conversation-rules/styling.md)
   - [`E:\code\Nokk\projects\site-and-crm\.agents\conversation-rules\workitems.md`](file:///E:/code/Nokk/projects/site-and-crm/.agents/conversation-rules/workitems.md)
2. **Role Verification**: Confirm full comprehension of assigned role boundaries and permissions.
3. **Ask Clarifications**: Raise any clarifying questions if role or task scope is ambiguous.
4. **Onboarding Output**: Conclude onboarding by outputting the confirmation block:

```markdown
#### Onboarding Complete
Please confirm:
Current Worktree = <git rev-parse --show-toplevel output>
Current Task = <task description or awaiting user input>
```

5. **Wait for User**: Stop and await explicit user command before executing work.

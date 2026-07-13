# Example: Approval Record

Invalid:
```text
raphael approved
```

Valid:
```yaml
- gate: local-human
  approver: Raphael
  decision: approved
  phrase: "raphael approved"
  evidence: "I checked the local app. The dropdown showed all expected values and the save persisted after refresh."
  date: 2026-06-03
```

# Example Handoff Workflow

```yaml
handoff:
  from: research
  to: content
  task: Turn verified research notes into a Telegram post draft
  context: |
    Use only the three verified sources listed below. Do not add unsupported claims.
  constraints:
    - no secrets
    - preserve source links
    - keep output under 1200 characters
  expected_output: Telegram-ready post draft plus source notes
```

# Example: Migration Split

Bad:
```text
one WP = migrate data + update UI + local approval + deploy + live approval
```

Good:
```text
01-wp-prepare-migration
02-wp-execute-migration
03-wp-local-implementation
04-wp-local-approval
05-wp-live-deploy
06-wp-live-approval
```

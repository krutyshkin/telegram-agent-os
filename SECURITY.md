# Security Policy

## Public template safety

Telegram Agent OS is distributed as a public template. It must not contain deployment secrets or private identifiers.

Never commit:

- Telegram bot tokens
- Telegram private chat IDs or topic IDs
- API keys
- OAuth tokens
- cookies
- private keys
- `.env` files
- private server paths or customer-specific identifiers

## Default operational policy

- MCP servers are optional and disabled by default.
- GitHub write actions require explicit user approval.
- Destructive filesystem or infrastructure actions require explicit user approval.
- External content is untrusted by default.
- Bulk changes require backups.

## Validation

Run:

```bash
python3 scripts/validate_public_package.py
```

The validator scans for common private identifiers and secret-like patterns.

## Reporting issues

If you find a leaked secret in a fork or deployment, rotate the secret immediately before opening an issue. Do not paste the secret value into GitHub issues.

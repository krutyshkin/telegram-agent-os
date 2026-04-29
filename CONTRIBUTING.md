# Contributing

Thanks for improving Telegram Agent OS.

## Rules

- Do not commit real Telegram bot tokens, chat IDs, topic IDs, API keys, cookies, private keys, or `.env` files.
- Keep public examples generic and placeholder-based.
- Keep MCP optional and disabled by default unless a specific example clearly explains the risk.
- GitHub write operations in agent prompts must require explicit user approval.
- Run the validator before opening a pull request:

```bash
python3 scripts/validate_public_package.py
```

## Recommended changes

Good contributions include:

- better role templates
- safer install docs
- examples for Telegram forum routing
- optional MCP packs with security notes
- improved validation rules
- translations

## Style

- English is the primary README language.
- Russian documentation lives in `README.ru.md`.
- Keep commands copy-pasteable.
- Prefer short sections, concrete examples, and verification steps.

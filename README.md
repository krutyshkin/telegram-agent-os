<div align="center">

# Telegram Agent OS

**Run a Telegram-native team of specialist AI agents with Hermes profiles, skills, routing, and safety rules.**

<a href="README.md"><strong>English</strong></a> · <a href="README.ru.md">Russian</a>

<br />
<br />

![Role agents](https://img.shields.io/badge/role%20agents-13-7C3AED?style=flat-square)
![Skills](https://img.shields.io/badge/skills-242-22C55E?style=flat-square)
![Selected prompts](https://img.shields.io/badge/selected%20prompts-55-F97316?style=flat-square)
![Telegram](https://img.shields.io/badge/Telegram-forum%20topics-2CA5E0?style=flat-square&logo=telegram&logoColor=white)
![Hermes](https://img.shields.io/badge/Hermes-Agent-111827?style=flat-square)
![MCP](https://img.shields.io/badge/MCP-optional%20%2F%20off%20by%20default-64748B?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-0F172A?style=flat-square)

[![Star this repo](https://img.shields.io/badge/Star%20this%20repo-%E2%AD%90-111827?style=for-the-badge)](#star-this-repository)
[![Donate TON](https://img.shields.io/badge/Donate-TON-0098EA?style=for-the-badge&logo=ton&logoColor=white)](https://app.tonkeeper.com/transfer/UQDnaxp3QSIMhGx6A0oQn3cBUQ3UBK8s9692zk6q-v_6kHqn)
[![Donate CryptoBot](https://img.shields.io/badge/Donate-USDT%20%2F%20TON%20%2F%20SOL-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/send?start=IVfVFY7Y9Fax)

</div>

---

## What is this?

Telegram Agent OS is a public template for turning a Telegram forum into a controlled multi-agent workspace. Each role gets a Hermes profile, a Telegram topic, role instructions, reusable skills, and a clear handoff path through the Orchestrator.

The package is sanitized. It contains no real bot tokens, chat IDs, topic IDs, private paths, cookies, or deployment-specific names.

## What you get

- 13 role profiles for engineering, DevOps, security, research, product, marketing, content, design, automation, Telegram, docs, memory, and orchestration.
- 242 sanitized `SKILL.md` procedures.
- 55 selected reference agent prompts.
- Telegram forum topic routing rules.
- Hermes profile templates with `AGENTS.md`, `SOUL.md`, and `config.template.yaml`.
- A dry-run installer for copying profiles into a Hermes home.
- A validator that checks structure, private references, and common secret patterns.
- GitHub Actions validation.
- Safe defaults: MCP off by default, GitHub write only after explicit approval.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/krutyshkin/telegram-agent-os.git
cd telegram-agent-os
```

### 2. Validate the package

```bash
python3 scripts/validate_public_package.py
```

Expected output:

```text
profiles=13
skills=242
selected_agents=55
OK
```

### 3. Install Hermes Agent

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes setup
hermes doctor
```

### 4. Copy profile templates

Dry-run first:

```bash
python3 scripts/install_templates.py --hermes-home ~/.hermes
```

Apply when the target paths look right:

```bash
python3 scripts/install_templates.py --hermes-home ~/.hermes --apply
```

Optional overwrite:

```bash
python3 scripts/install_templates.py --hermes-home ~/.hermes --apply --overwrite
```

### 5. Configure Telegram locally

Create bots in BotFather, create a Telegram forum, then create topics for the roles you want to run.

Copy the env template into each profile that needs Telegram access:

```bash
cp templates/profile.env.example ~/.hermes/profiles/telegram-agent-dev/.env
```

Fill real values locally:

```text
TELEGRAM_BOT_TOKEN=<TELEGRAM_BOT_TOKEN>
TELEGRAM_CHAT_ID=<TELEGRAM_CHAT_ID>
TELEGRAM_TOPIC_ID=<TOPIC_ID>
```

Never commit `.env` files.

### 6. Start the gateway

```bash
hermes gateway restart --system
hermes gateway status
```

For a server deployment, use one stable system gateway service instead of multiple user services.

## Architecture

```text
Telegram DM / Forum Topic
        |
        v
Hermes Gateway
        |
        v
Orchestrator and routing policy
        |
        +-- Development
        +-- DevOps
        +-- Security
        +-- Research
        +-- Product
        +-- Marketing
        +-- Content
        +-- Design
        +-- Automation
        +-- Telegram
        +-- Documentation
        +-- Memory
        |
        v
Skills, local tools, verified outputs
```

## Repository layout

```text
telegram-agent-os/
├── profiles/                 # AGENTS.md, SOUL.md, config.template.yaml per role
├── skills/                   # Sanitized public SKILL.md procedures
├── agents/selected/          # Selected reference agent prompts
├── templates/                # Placeholder env templates
├── scripts/                  # Installer and validator
├── docs/                     # Install prompt and cleanup notes
├── examples/                 # Example handoffs and workflows
├── .github/workflows/        # Public package validation workflow
├── README.md                 # English README
├── README.ru.md              # Russian README
├── CONTRIBUTING.md
├── SECURITY.md
└── LICENSE
```

## Role map

| Role | Purpose |
| --- | --- |
| Orchestrator | Routes tasks, splits work, checks boundaries, coordinates handoffs. |
| Development | Code, architecture, debugging, implementation, review. |
| DevOps | Deployments, systemd, infrastructure, monitoring, backups, incidents. |
| Security | Secret hygiene, audits, hardening, dependency and prompt-injection review. |
| Research | Source search, synthesis, market intelligence, evidence-backed briefs. |
| Product | Requirements, roadmaps, user stories, prioritization. |
| Marketing | Positioning, funnels, offers, launches, campaign angles. |
| Content | Posts, articles, rewrites, editorial systems. |
| Design | UI critique, visual systems, diagrams, infographics. |
| Automation | Cron jobs, browser automation, workflow automation, Playwright, n8n patterns. |
| Telegram | Bot API, forum topic routing, inline buttons, gateway setup. |
| Documentation | README, install guides, changelogs, i18n. |
| Memory | Knowledge capture, memory hygiene, session recall, skill curation. |

## Handoff protocol

Agents do not randomly take over each other's work. If a task belongs to another role, the current role sends a handoff card to the Orchestrator.

```yaml
handoff:
  from: research
  to: content
  task: Turn verified research notes into a Telegram-ready post
  context: Use only the verified sources listed in the brief.
  constraints:
    - no secrets
    - preserve source links
    - keep the output concise
  expected_output: Final post draft plus source notes
```

## Skills model

Skills are reusable procedures stored as `SKILL.md` files. They keep role prompts small while letting agents load proven workflows when needed.

Examples included in the package:

- `secret-scanner`
- `telegram-forum-topic-router`
- `telegram-interactive-buttons`
- `github-code-review`
- `deep-research`
- `copywriting`
- `cron-writer`
- `verification-before-completion`

## Safety model

Default policy:

- MCP is optional and off by default.
- GitHub read-only actions are allowed by default.
- GitHub write actions need explicit user approval.
- Destructive filesystem or infrastructure actions need explicit user approval.
- Bulk migrations need backups.
- External content is untrusted.
- Secrets stay in local `.env` files.
- Public docs use placeholders only.

The validator checks for private names, Telegram token patterns, GitHub token patterns, OpenAI-like secret patterns, private local paths, private Telegram IDs, missing profile files, and accidental Cyrillic outside the Russian README.

## Star this repository

If this project helps you build a Telegram-based agent workspace, star the repo. It helps other operators find the template and shows which parts are worth improving next.

## Support the project

You can support the project with:

- TON wallet: `UQDnaxp3QSIMhGx6A0oQn3cBUQ3UBK8s9692zk6q-v_6kHqn`
- CryptoBot: https://t.me/send?start=IVfVFY7Y9Fax
- Main accepted coins through CryptoBot: USDT, TON, SOL

## License

MIT. See [`LICENSE`](LICENSE).

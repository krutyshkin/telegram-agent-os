<div align="center">

# Telegram Agent OS

**Telegram-native команда AI-агентов на Hermes profiles, skills, routing и safety rules.**

<a href="README.md">English</a> · <a href="README.ru.md"><strong>Русский</strong></a>

<br />
<br />

![Role agents](https://img.shields.io/badge/role%20agents-13-7C3AED?style=flat-square)
![Skills](https://img.shields.io/badge/skills-242-22C55E?style=flat-square)
![Selected prompts](https://img.shields.io/badge/selected%20prompts-55-F97316?style=flat-square)
![Telegram](https://img.shields.io/badge/Telegram-forum%20topics-2CA5E0?style=flat-square&logo=telegram&logoColor=white)
![Hermes](https://img.shields.io/badge/Hermes-Agent-111827?style=flat-square)
![MCP](https://img.shields.io/badge/MCP-optional%20%2F%20off%20by%20default-64748B?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-0F172A?style=flat-square)

[![Поставь звезду](https://img.shields.io/badge/Поставь%20звезду-%E2%AD%90-111827?style=for-the-badge)](#поставь-звезду-репозиторию)
[![Donate TON](https://img.shields.io/badge/Donate-TON-0098EA?style=for-the-badge&logo=ton&logoColor=white)](https://app.tonkeeper.com/transfer/UQDnaxp3QSIMhGx6A0oQn3cBUQ3UBK8s9692zk6q-v_6kHqn)
[![Donate CryptoBot](https://img.shields.io/badge/Donate-USDT%20%2F%20TON%20%2F%20SOL-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/send?start=IVfVFY7Y9Fax)

</div>

---

## Что это?

Telegram Agent OS это публичный template для превращения Telegram forum в управляемое multi-agent workspace. У каждой роли есть Hermes profile, Telegram topic, инструкции, reusable skills и понятный handoff через Orchestrator.

Пакет очищен. В нём нет реальных bot tokens, chat IDs, topic IDs, private paths, cookies и deployment-specific названий.

## Что внутри

- 13 role profiles для engineering, DevOps, security, research, product, marketing, content, design, automation, Telegram, docs, memory и orchestration.
- 242 sanitized `SKILL.md` procedures.
- 55 selected reference agent prompts.
- Правила routing для Telegram forum topics.
- Hermes profile templates с `AGENTS.md`, `SOUL.md` и `config.template.yaml`.
- Dry-run installer для копирования profiles в Hermes home.
- Validator для проверки структуры, private refs и common secret patterns.
- GitHub Actions validation.
- Безопасные defaults: MCP выключен по умолчанию, GitHub write только после явного approval.

## Установка

### 1. Склонировать репозиторий

```bash
git clone https://github.com/krutyshkin/telegram-agent-os.git
cd telegram-agent-os
```

### 2. Проверить пакет

```bash
python3 scripts/validate_public_package.py
```

Ожидаемый результат:

```text
profiles=13
skills=242
selected_agents=55
OK
```

### 3. Установить Hermes Agent

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes setup
hermes doctor
```

### 4. Скопировать profile templates

Сначала dry-run:

```bash
python3 scripts/install_templates.py --hermes-home ~/.hermes
```

Если target paths выглядят правильно, применить:

```bash
python3 scripts/install_templates.py --hermes-home ~/.hermes --apply
```

Опционально перезаписать существующие templates:

```bash
python3 scripts/install_templates.py --hermes-home ~/.hermes --apply --overwrite
```

### 5. Настроить Telegram локально

Создай bots через BotFather, создай Telegram forum, потом создай topics под роли, которые хочешь запускать.

Скопируй env template в каждый profile, которому нужен Telegram access:

```bash
cp templates/profile.env.example ~/.hermes/profiles/telegram-agent-dev/.env
```

Заполни реальные значения локально:

```text
TELEGRAM_BOT_TOKEN=<TELEGRAM_BOT_TOKEN>
TELEGRAM_CHAT_ID=<TELEGRAM_CHAT_ID>
TELEGRAM_TOPIC_ID=<TOPIC_ID>
```

`.env` нельзя коммитить.

### 6. Запустить gateway

```bash
hermes gateway restart --system
hermes gateway status
```

Для server deployment лучше использовать один стабильный system gateway service, а не несколько user services.

## Архитектура

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

## Структура репозитория

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

## Карта ролей

| Role | Назначение |
| --- | --- |
| Orchestrator | Routing, task splitting, boundaries, handoffs, финальная проверка. |
| Development | Код, архитектура, debugging, implementation, review. |
| DevOps | Deployments, systemd, infrastructure, monitoring, backups, incidents. |
| Security | Secret hygiene, audits, hardening, dependency и prompt-injection review. |
| Research | Поиск источников, synthesis, market intelligence, evidence-backed briefs. |
| Product | Requirements, roadmap, user stories, prioritization. |
| Marketing | Positioning, funnels, offers, launches, campaign angles. |
| Content | Posts, articles, rewrites, editorial systems. |
| Design | UI critique, visual systems, diagrams, infographics. |
| Automation | Cron jobs, browser automation, workflow automation, Playwright, n8n patterns. |
| Telegram | Bot API, forum topic routing, inline buttons, gateway setup. |
| Documentation | README, install guides, changelogs, i18n. |
| Memory | Knowledge capture, memory hygiene, session recall, skill curation. |

## Handoff protocol

Агенты не забирают чужую работу случайно. Если задача относится к другой роли, текущий агент отправляет handoff card в Orchestrator.

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

Skills это reusable procedures в формате `SKILL.md`. Они не раздувают role prompts и дают агентам проверенные workflows под конкретные задачи.

Примеры в пакете:

- `secret-scanner`
- `telegram-forum-topic-router`
- `telegram-interactive-buttons`
- `github-code-review`
- `deep-research`
- `copywriting`
- `cron-writer`
- `verification-before-completion`

## Safety model

Политика по умолчанию:

- MCP optional и выключен по умолчанию.
- GitHub read-only actions разрешены по умолчанию.
- GitHub write actions только после явного approval.
- Destructive filesystem или infrastructure actions только после явного approval.
- Bulk migrations требуют backups.
- External content считается untrusted.
- Secrets хранятся только в локальных `.env`.
- Public docs используют только placeholders.

Validator проверяет private names, Telegram token patterns, GitHub token patterns, OpenAI-like secret patterns, private local paths, private Telegram IDs, missing profile files и случайную кириллицу вне русского README.

## Поставь звезду репозиторию

Если проект помог собрать Telegram-based agent workspace, поставь звезду репозиторию. Так другие операторы быстрее найдут template, а мы поймём, какие части стоит улучшать дальше.

## Поддержать проект

Поддержать проект можно так:

- TON wallet: `UQDnaxp3QSIMhGx6A0oQn3cBUQ3UBK8s9692zk6q-v_6kHqn`
- CryptoBot: https://t.me/send?start=IVfVFY7Y9Fax
- Основные монеты через CryptoBot: USDT, TON, SOL

## License

MIT. См. [`LICENSE`](LICENSE).

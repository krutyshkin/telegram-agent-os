#!/usr/bin/env python3
from pathlib import Path
import re, sys
root = Path(__file__).resolve().parents[1]
patterns = {
    'project_specific_name': re.compile(r'\bMiniAI\b|\bminiai\b|@miniai', re.I),
    'source_reference_name': re.compile(r'gensecai|wshobson|voltagent|msitarzewski|0xfurai|lst97|awesome-claude|claude-code-subagents|agency-agents|subagents-collection', re.I),
    'private_chat_id': re.compile(r'-100\d{6,}'),
    'telegram_bot_token': re.compile(r'\b\d{8,12}:[A-Za-z0-9_-]{30,}\b'),
    'github_token': re.compile(r'\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b'),
    'openai_like_secret': re.compile(r'\bsk-[A-Za-z0-9_-]{20,}\b'),
    'private_path': re.compile(r'/opt/hermes|/root/|/home/hermes'),
    'cyrillic': re.compile(r'[А-Яа-яЁё]'),
}
failures=[]
for p in root.rglob('*'):
    if not p.is_file() or '.git' in p.parts: continue
    rel=str(p.relative_to(root))
    if rel == 'scripts/validate_public_package.py':
        continue
    if p.suffix.lower() not in {'.md','.yaml','.yml','.txt','.example','.py'} and p.name not in {'.gitignore','LICENSE'}:
        continue
    text=p.read_text(errors='ignore')
    for name,rx in patterns.items():
        if name=='cyrillic' and rel=='README.ru.md':
            continue
        haystack = text + '\n' + rel
        if rx.search(haystack):
            failures.append((name, rel))
roles = [p for p in (root/'profiles').iterdir() if p.is_dir()]
for r in roles:
    for fn in ['AGENTS.md','SOUL.md','config.template.yaml']:
        if not (r/fn).exists(): failures.append(('missing_profile_file', str((r/fn).relative_to(root))))
print(f'profiles={len(roles)}')
print(f'skills={len(list((root/"skills").glob("**/SKILL.md")))}')
print(f'selected_agents={len(list((root/"agents"/"selected").glob("**/*.md")))}')
if failures:
    print('FAIL')
    for kind, rel in failures[:200]: print(kind, rel)
    sys.exit(1)
print('OK')

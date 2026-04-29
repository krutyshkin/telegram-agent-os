#!/usr/bin/env python3
"""Install Telegram Agent OS profile templates into a Hermes home.

Default mode is dry-run. Use --apply to copy files.
This script never writes secrets and never creates Telegram bots for you.
"""
from pathlib import Path
import argparse, shutil, sys

ROOT = Path(__file__).resolve().parents[1]
ROLES = [p for p in (ROOT / "profiles").iterdir() if p.is_dir()]

parser = argparse.ArgumentParser()
parser.add_argument("--hermes-home", default=str(Path.home() / ".hermes"), help="Target Hermes home")
parser.add_argument("--prefix", default="telegram-agent-", help="Profile directory prefix")
parser.add_argument("--apply", action="store_true", help="Actually copy templates")
parser.add_argument("--overwrite", action="store_true", help="Overwrite existing AGENTS.md/SOUL.md/config.template.yaml")
args = parser.parse_args()

target_home = Path(args.hermes_home).expanduser().resolve()
profiles_dir = target_home / "profiles"

print(f"source={ROOT}")
print(f"target_profiles={profiles_dir}")
print(f"mode={'apply' if args.apply else 'dry-run'}")

for role_dir in sorted(ROLES):
    role = role_dir.name
    target = profiles_dir / f"{args.prefix}{role}"
    print(f"\nrole={role}")
    print(f"  target={target}")
    for name in ["AGENTS.md", "SOUL.md", "config.template.yaml"]:
        src = role_dir / name
        dst = target / name
        exists = dst.exists()
        action = "skip-existing" if exists and not args.overwrite else "copy"
        print(f"  {action}: {name}")
        if args.apply and action == "copy":
            target.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

print("\nNext steps:")
print("1. Copy templates/profile.env.example into each profile as .env and fill local secrets.")
print("2. Replace <TELEGRAM_CHAT_ID>, <TOPIC_ID>, and bot usernames in config files.")
print("3. Keep MCP disabled unless explicitly needed.")
print("4. Restart Hermes gateway and verify Telegram routing.")

#!/usr/bin/env python3
"""Lint the plugin's skills and agents. Run from the repo root: python3 scripts/lint.py

Checks: frontmatter (name == folder, a "Use when" description under 1024 chars, no
unquoted ': '), every relative .md link resolves, no em or en dashes, no names from
real campaigns or published settings, SKILL.md under 130 lines.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent / "plugins" / "questmaster-vtt"
BANNED = re.compile(
    r"Embers of the Gilded Quarter|A King'?s Wrath|Lanternreach|Gilded Quarter|"
    r"Forgotten Realms|Waterdeep|Baldur|Ravenloft|Strahd|Barovia|Eberron|Greyhawk|"
    r"Faer[uû]n|Cthulhu|Warhammer|Witcher|Middle-earth|Mordor",
    re.I,
)
errors = []

def err(path, msg):
    errors.append(f"{path.relative_to(ROOT.parent.parent)}: {msg}")

def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        err(path, "no frontmatter")
        return {}, text
    fields = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([a-z_-]+):\s*(.*)$", line)
        if kv:
            v = kv.group(2)
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1]
            elif ": " in v:
                err(path, f"unquoted ': ' in {kv.group(1)} (YAML would break)")
            fields[kv.group(1)] = v
    return fields, text

for skill in sorted((ROOT / "skills").iterdir()):
    sk = skill / "SKILL.md"
    if not sk.exists():
        err(skill, "missing SKILL.md")
        continue
    f, text = frontmatter(sk)
    if f.get("name") != skill.name:
        err(sk, f"name {f.get('name')!r} != folder {skill.name!r}")
    d = f.get("description", "")
    if not d or len(d) > 1024 or "Use when" not in d and "use when" not in d.lower():
        err(sk, f"description missing, too long, or without 'Use when' ({len(d)} chars)")
    if text.count("\n") > 130:
        err(sk, f"{text.count(chr(10))} lines (keep SKILL.md short; move depth to references/)")
    for link in re.findall(r"\]\((references/[^)]+\.md)\)", text):
        if not (skill / link).exists():
            err(sk, f"broken link {link}")

for agent in sorted((ROOT / "agents").glob("*.md")):
    f, _ = frontmatter(agent)
    if f.get("name") != agent.stem or not f.get("description"):
        err(agent, "agent needs name == filename and a description")

for path in sorted(list((ROOT / "skills").rglob("*.md")) + list((ROOT / "agents").glob("*.md"))):
    text = path.read_text(encoding="utf-8")
    for i, line in enumerate(text.splitlines(), 1):
        if "—" in line or "–" in line:
            err(path, f"line {i}: em or en dash")
        b = BANNED.search(line)
        if b:
            err(path, f"line {i}: banned name {b.group(0)!r}")

if errors:
    print("\n".join(errors))
    print(f"\n{len(errors)} problem(s)")
    sys.exit(1)
n = len(list((ROOT / 'skills').iterdir()))
print(f"ok: {n} skills, {len(list((ROOT / 'agents').glob('*.md')))} agents")

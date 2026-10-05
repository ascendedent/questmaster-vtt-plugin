#!/usr/bin/env python3
"""Lint the plugin's skills and agents. Run from the repo root: python3 scripts/lint.py

Checks: frontmatter (name == folder, a "Use when" description under 1024 chars, no
unquoted ': '), every relative .md link resolves, no em or en dashes, no names from
real campaigns or published settings, SKILL.md under 130 lines; one version across the
Claude, ChatGPT and Grok manifests, and the ChatGPT listing within OpenAI's field and icon limits.
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

# Manifests: one version everywhere, and the ChatGPT listing inside OpenAI's limits
# (developers.openai.com/plugins/deploy/submission, read 2026-10-05).
import json, struct

REPO = ROOT.parent.parent

def load(rel):
    p = REPO / rel
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        errors.append(f"{rel}: {e}")
        return {}

claude = load("plugins/questmaster-vtt/.claude-plugin/plugin.json")
claude_market = load(".claude-plugin/marketplace.json")
codex = load("plugins/questmaster-vtt/.codex-plugin/plugin.json")
codex_market = load(".agents/plugins/marketplace.json")
grok = load("plugins/questmaster-vtt/.grok-plugin/plugin.json")
versions = {
    ".claude-plugin/plugin.json": claude.get("version"),
    ".claude-plugin/marketplace.json": next((p.get("version") for p in claude_market.get("plugins", []) if p.get("name") == "questmaster-vtt"), None),
    ".codex-plugin/plugin.json": codex.get("version"),
    ".grok-plugin/plugin.json": grok.get("version"),
}
if len(set(versions.values())) != 1:
    errors.append(f"versions differ: {versions}")
if not any(p.get("name") == "questmaster-vtt" and p.get("source", {}).get("path") == "./plugins/questmaster-vtt" for p in codex_market.get("plugins", [])):
    errors.append(".agents/plugins/marketplace.json: no questmaster-vtt entry pointing at ./plugins/questmaster-vtt")

CODEX = "plugins/questmaster-vtt/.codex-plugin/plugin.json"
ui = codex.get("interface", {})

def limit(label, value, n, required=True):
    if value in (None, ""):
        if required:
            errors.append(f"{CODEX}: {label} is required")
        return
    if not isinstance(value, str) or len(value) > n:
        errors.append(f"{CODEX}: {label} must be a string of at most {n} chars ({len(str(value))})")
    elif "—" in value or "–" in value:
        errors.append(f"{CODEX}: {label} has an em or en dash")

limit("name", codex.get("name"), 64)
if codex.get("name") != "questmaster-vtt":
    errors.append(f"{CODEX}: name must be questmaster-vtt")
limit("description", codex.get("description"), 4000)
limit("author.name", codex.get("author", {}).get("name"), 120)
limit("displayName", ui.get("displayName"), 30)
limit("shortDescription", ui.get("shortDescription"), 30)
limit("longDescription", ui.get("longDescription"), 4000)
limit("developerName", ui.get("developerName"), 80)
for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
    limit(key, ui.get(key), 1024)
    if not str(ui.get(key, "")).startswith("https://"):
        errors.append(f"{CODEX}: {key} must be an https URL")
caps = ui.get("capabilities", [])
if len(caps) > 20 or any(not isinstance(c, str) or len(c) > 120 for c in caps):
    errors.append(f"{CODEX}: capabilities: at most 20, each at most 120 chars")
prompts = ui.get("defaultPrompt", [])
if not 1 <= len(prompts) <= 3:
    errors.append(f"{CODEX}: defaultPrompt needs 1 to 3 prompts ({len(prompts)})")
for i, p in enumerate(prompts):
    limit(f"defaultPrompt[{i}]", p, 128)

def image_size(path):
    """(width, height) of a PNG or an SVG's viewBox, else None."""
    data = path.read_bytes()
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", data[16:24])
    if path.suffix == ".svg":
        m = re.search(r'viewBox="\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)[\s,]+([\d.]+)', data.decode("utf-8", "replace"))
        return (float(m.group(1)), float(m.group(2))) if m else None
    return None

PLUGIN = REPO / "plugins/questmaster-vtt"
for key in ("composerIcon", "logo", "logoDark"):
    rel = ui.get(key)
    if rel is None and key == "logoDark":
        continue
    if not rel or not rel.startswith("./assets/") or not (PLUGIN / rel).is_file():
        errors.append(f"{CODEX}: {key} must be a file under ./assets/ ({rel!r})")
        continue
    f = PLUGIN / rel
    size = image_size(f)
    if f.stat().st_size > 5 * 1024 * 1024:
        errors.append(f"{CODEX}: {key} is over 5 MiB")
    if not size:
        errors.append(f"{CODEX}: {key} must be a PNG or an SVG with a viewBox")
    elif size[0] != size[1] or size[0] < 48 or (f.suffix == ".png" and size[0] > 4096):
        errors.append(f"{CODEX}: {key} must be square, 48 to 4096 px ({size[0]}x{size[1]})")
for rel in ui.get("screenshots", []):
    f = PLUGIN / rel
    if not rel.startswith("./assets/") or not rel.endswith(".png") or not f.is_file():
        errors.append(f"{CODEX}: screenshot {rel!r} must be a PNG under ./assets/")
    elif f.stat().st_size > 5 * 1024 * 1024 or max(image_size(f) or (0, 0)) > 4096:
        errors.append(f"{CODEX}: screenshot {rel!r} is over 5 MiB or 4096 px")
if grok.get("name") != "questmaster-vtt" or not (REPO / "plugins/questmaster-vtt" / str(grok.get("logo", ""))).is_file():
    errors.append("plugins/questmaster-vtt/.grok-plugin/plugin.json: name must be questmaster-vtt and logo an existing file")
# MCPSURF1: Claude reads .mcp.json, the standard endpoint (its directory listing
# makes no images); ChatGPT/Codex and Grok name .mcp.full.json, the full one.
def mcp_url(rel):
    try:
        servers = json.loads((PLUGIN / rel).read_text(encoding="utf-8"))["mcpServers"]
        return [s.get("url") for s in servers.values()]
    except Exception as e:  # noqa: BLE001
        return [f"unreadable: {e}"]
if mcp_url(".mcp.json") != ["https://questmastervtt.com/api/mcp"]:
    errors.append(f".mcp.json must point only at https://questmastervtt.com/api/mcp (Claude): {mcp_url('.mcp.json')}")
for label, m in ((".codex-plugin", codex), (".grok-plugin", grok)):
    rel = str(m.get("mcpServers", "")).removeprefix("./")
    if mcp_url(rel) != ["https://questmastervtt.com/api/mcp/full"]:
        errors.append(f"{label}/plugin.json mcpServers must name a file pointing only at https://questmastervtt.com/api/mcp/full: {rel!r} {mcp_url(rel)}")
for key in ("skills", "mcpServers"):
    if not (PLUGIN / str(codex.get(key, ""))).exists():
        errors.append(f"{CODEX}: {key} path {codex.get(key)!r} does not exist")

if errors:
    print("\n".join(errors))
    print(f"\n{len(errors)} problem(s)")
    sys.exit(1)
n = len(list((ROOT / 'skills').iterdir()))
print(f"ok: {n} skills, {len(list((ROOT / 'agents').glob('*.md')))} agents")

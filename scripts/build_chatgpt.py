#!/usr/bin/env python3
"""Build the ChatGPT plugin ZIP. Run from the repo root: python3 scripts/build_chatgpt.py

Writes dist/questmaster-vtt-chatgpt-<version>.zip for the Plugins page of the OpenAI
Platform dashboard. The archive holds the plugin's contents at its root:
.codex-plugin/plugin.json, .mcp.json, skills/, the assets the manifest names, and
LICENSE.md. The Claude-only parts (.claude-plugin/, agents/, evals/) stay out. Same
skills as the Claude plugin, so one release feeds both. Lint runs first, and the
archive is reproducible (sorted entries, fixed timestamps).
"""
import hashlib, json, pathlib, subprocess, sys, zipfile

REPO = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = REPO / "plugins" / "questmaster-vtt"

if subprocess.run([sys.executable, str(REPO / "scripts" / "lint.py")]).returncode != 0:
    sys.exit("lint failed: nothing built")

manifest = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
ui = manifest["interface"]
assets = {ui[k] for k in ("composerIcon", "logo", "logoDark") if ui.get(k)} | set(ui.get("screenshots", []))

entries = {".codex-plugin/plugin.json": PLUGIN / ".codex-plugin" / "plugin.json", ".mcp.json": PLUGIN / ".mcp.json"}
for f in sorted((PLUGIN / "skills").rglob("*")):
    if f.is_file() and not f.name.startswith("."):
        entries[f.relative_to(PLUGIN).as_posix()] = f
for rel in sorted(assets):
    entries[rel.removeprefix("./")] = PLUGIN / rel
entries["LICENSE.md"] = REPO / "LICENSE.md"

out = REPO / "dist" / f"questmaster-vtt-chatgpt-{manifest['version']}.zip"
out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for name in sorted(entries):
        info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
        info.external_attr = 0o644 << 16
        info.compress_type = zipfile.ZIP_DEFLATED
        z.writestr(info, entries[name].read_bytes())

digest = hashlib.sha256(out.read_bytes()).hexdigest()
skills = len({n.split("/")[1] for n in entries if n.startswith("skills/")})
print(f"{out.relative_to(REPO)}: {len(entries)} files, {skills} skills, {out.stat().st_size // 1024} KB, sha256 {digest}")

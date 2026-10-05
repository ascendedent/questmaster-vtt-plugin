# QuestMaster VTT for Claude and ChatGPT

The official plugin that connects Claude or ChatGPT to your [QuestMaster VTT](https://questmastervtt.com)
campaigns. Your assistant reads your campaign and drafts prep for you to approve: NPCs,
factions, places, plot threads and beats, sessions, fights, items, homebrew, map
notes and table screens. Nothing changes in your campaign until you approve it, and
live play stays yours.

## What's inside

- **The QuestMaster connector** (`questmaster-vtt`), signed in with your QuestMaster
  account. You choose which campaigns it can see and whether it may draft changes.
- **Workflow skills**: campaign kickoff (session zero), session prep, world building,
  NPCs, plot, encounters, items, homebrew mechanics, lore, maps, session recaps,
  in-the-moment improv, and a read-only campaign audit.
- **12 genre packs**: gothic horror, cosmic horror, political intrigue, grimdark,
  swashbuckling, heist, mystery, wilderness hexcrawl, dungeon crawl, war campaign,
  fey fairytale, high fantasy epic. They combine.
- **6 writing styles**: read-aloud text, NPC voices, in-world documents, DM prep notes,
  recaps, handouts.
- **Agents** (Claude Code and Cowork): campaign architect, continuity checker,
  encounter designer.

The same skills ship to both: `.claude-plugin/` is the Claude manifest and
`.codex-plugin/` the ChatGPT and Codex one.

## Install

You need a QuestMaster VTT account with AI features on, and agent access switched on
for each campaign you want your assistant to see (Account, then Connections).

**Claude Code**

```
/plugin marketplace add ascendedent/questmaster-vtt-plugin
/plugin install questmaster-vtt@questmaster-vtt
```

Then run `/mcp`, pick `questmaster-vtt`, and sign in to QuestMaster.

**claude.ai (web, desktop, mobile)**

Customize, then Plugins, then Add marketplace, and paste
`https://github.com/ascendedent/questmaster-vtt-plugin`. Add **QuestMaster VTT**
from Discover, then connect it and sign in to QuestMaster when asked.

**ChatGPT**

The plugin is being prepared for ChatGPT's plugin directory. Until it is listed, connect
QuestMaster in ChatGPT's developer mode as a custom connector (the help page below has
the steps); ChatGPT reads the same guidance from the server.

**Codex**

```
codex plugin marketplace add ascendedent/questmaster-vtt-plugin
codex plugin add questmaster-vtt@questmaster-vtt
```

Then run `codex mcp login questmaster-vtt` and sign in to QuestMaster.

Full walkthroughs for every assistant are at https://questmastervtt.com/help/agents.

## What it will and won't do

- It **drafts**; you **approve**, in the chat where your client supports it or on the
  Agent changes page in QuestMaster. Anything approved can be undone there.
- It never starts fights, pushes secrets to players, fires table-screen cues, opens
  shops or marks sessions played. It tells you which button to press.
- It treats your campaign as canon and asks one focused question when something is
  missing.

## Privacy and terms

What your assistant reads from your campaign is sent to its maker (Anthropic for
Claude, OpenAI for ChatGPT and Codex) to answer you, under your account's terms there. QuestMaster's [privacy policy](https://questmastervtt.com/legal/privacy)
and [terms](https://questmastervtt.com/legal/terms) cover the QuestMaster side.

## Building the ChatGPT package

`python3 scripts/build_chatgpt.py` lints, then writes
`dist/questmaster-vtt-chatgpt-<version>.zip` (the manifest, `.mcp.json`, the skills, the
icon and the license; the Claude-only agents and evals stay out) for the Plugins page of
the OpenAI Platform dashboard.

## Evals

`plugins/questmaster-vtt/evals/` holds `claude plugin eval` cases. Every case runs
against the mocks in `evals/mocks/questmaster-vtt/` (a fictional campaign, "The Ashfall
Reach"), never a real QuestMaster account; a case overrides suite mocks with its own
`mocks/` folder. Run the eval command from the plugin folder with `--no-publish`
(add `--runs 1` for a quick pass; the default is 3 runs per arm with a no-plugin
baseline).

## License

The writing (skills and agents) is CC BY-NC 4.0; manifests, configuration and evals
are MIT. See [LICENSE.md](LICENSE.md).

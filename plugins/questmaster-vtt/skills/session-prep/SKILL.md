---
name: session-prep
description: A procedure for turning an unplayed QuestMaster session into a run sheet the DM can run from, with a strong start, scenes drafted as session beats, staged secrets and clues, rated encounters, NPC quick refs, and optional prepared table screens with a cue list. Use when a DM asks to prep, plan or get ready for the next session, wants a run sheet or session outline, or wants screens queued for the table TV.
---

# Session Prep

The DM gets a one-page run sheet for the next session, and QuestMaster gets the matching session beats, staged clues, planned fights and (if wanted) screens in a cue list, all as one draft to approve.

## Use this when

- "Prep next session", "what do I need for Thursday", "make me a run sheet".
- The next unplayed session has few or no beats, secrets or encounters in `get_session_prep`.
- The DM wants handouts, maps or portraits queued for the players' screen.

## Steps

1. **Read first.** `get_campaign_overview` (it names the next unplayed session), or `list_entities` kind `session` to pick one. Then:
   - `get_session_prep` for that session: planned threads, plot beats, staged secrets, encounters.
   - `get_entity` kind `session` for its beats, and for the last played session's recap (where play stopped).
   - `get_plot_graph`: the current beat, and the beats one line away from it.
   - `get_party`: levels, passive Perception, XP budgets. `get_table_safety`: limits to respect.
   - `get_entity` on each thread and NPC the session touches; `search_campaign` before naming anything new.
   - `get_screen_prep` only if screens or cues are wanted.
2. **Ask one question if essential**, usually "Where did last session end?" when there is no recap, or "How long is the session?" (default 3 to 4 hours). Never a list.
3. **Build the run sheet** with [references/run-sheet.md](references/run-sheet.md): strong start, 3 to 5 scenes as situations with more than one way out, 6 to 10 secrets and clues, NPC quick refs, encounters, a closing hook, and a fallback scene.
4. **Plan the fights.** For each combat: `propose_encounter` for a starting roster at the DM's difficulty, then `plan_encounter`, which returns the 2024 rating; `rate_encounter` to compare alternatives. Existing planned fights: `update_encounter_plan`. Social, puzzle and exploration encounters use `plan_encounter` without monsters. An NPC who may fight and has no stats: `set_npc_statblock`.
5. **Draft the rest** (mapping below). Screens are optional: offer them once, draft them only on a yes.
6. **Recap and approve.** `get_changeset`, list what changes by kind, flag anything players will see, ask, then `request_approval`. Never call it saved before `applied`.
7. **Hand over the table work.** The DM pushes secrets, starts fights, puts maps up, fires cues, opens shops and marks the session played, all in the app.

## What to produce

The run sheet, in chat, fits on two screens (60 to 90 lines): strong start; scenes, each with a hook in, what is at stake, the NPCs and at least two exits; secrets and clues, each with where it might surface; NPC quick refs (three lines each: look, voice, want); encounters with rating, map and stakes; closing options; one fallback scene for when the party goes elsewhere. Then a short list of what was drafted.

## Drafting it

- Scenes: `upsert_session_beat` {`sessionId`, `title`, `description` (the scene's situation, stakes and exits), `npcIds`, `locationId`, `factionId`, `threadId`, `occurredAtInSession` 10, 20, 30 for running order}. Existing beats: pass `id`.
- Session: `upsert_session` {`id`, `summary` (the strong start and the session's question), `npcIds` (everyone likely to appear)}. Leave `title` alone unless the DM asks; players see it.
- Threads due: `upsert_thread` {`id`, `plannedSessionId`}; plot beats meant for this session: `upsert_plot_node` {`id`, `sessionId`}.
- Clues: `stage_secret` {`title`, `body` (what the player learns, in-world), `sessionId`, `subjectKind` + `subjectId` (or `free` + `subjectLabel`), `audienceCharacterIds` for the PC most likely to find it, `narrativeNodeId` for the beat it supports}.
- Fights: `plan_encounter` {`name` (no spoilers), `encounterType`, `monsters`, `npcs`, `includeParty`, `usedInSessionId`, `mapId`, `locationId`, `narrativePurpose`, `readAloudText`, DM-only `dmContext`, `terrainNotes`, `successConsequences`, `partialConsequences`, `failureConsequences`, DM-only `rewards`}.
- Screens: `save_monitor_preset` {`name`, `screen`: {`arrangement`, `focus`, `elements`: map, scene, npcPortrait, monsterPortrait, shop, text, combat}, `folderId`, `moduleId`, `areaId`}. Elements take saved ids from `get_screen_prep`, `list_entities` or `get_entity`, not refs from this draft. Then `build_cue_list` {`add`: the preset refs in running order}; `organize_presets` to file them in a folder for the session.
- Leave a field out to keep it; `null` clears it; list fields replace the whole list.

## Don'ts

- Don't do XP math, to-hit or DCs by hand. `propose_encounter`, `plan_encounter` and `rate_encounter` rate fights; `set_npc_statblock` computes NPC numbers.
- Don't script what the players do. A scene is a situation with exits, not a plot the party must walk through; never require one specific clue.
- Don't put spoilers where players look: session `title`, encounter `name`, `readAloudText`, screen text. A clue's `body` gives the clue, not the conclusion.
- Don't touch played sessions or beats already shown to players; the tools refuse. Move unfinished material to the next session instead.
- Don't change the cue list while the DM is running it, or a screen the players are looking at; both are refused.
- Don't put anything on a hard limit into a scene, clue or screen; soft limits stay off-screen.

## Pairs well with

- The campaign's `genre-*` pack(s) for scene structure and encounter situations.
- `style-dm-prep-notes` for the run sheet, `style-read-aloud` for the strong start and `readAloudText`, `style-npc-voice` for quick refs, `style-handouts` for text screens and clue bodies.
- `design-encounter` for a fight that needs more than a roster, `generate-npc` for a new face, `recap-session` first if last session has no recap, `campaign-audit` when prep keeps hitting loose ends.

## References

- [references/run-sheet.md](references/run-sheet.md): read when building the run sheet; the template, rules for each section, and a worked example.

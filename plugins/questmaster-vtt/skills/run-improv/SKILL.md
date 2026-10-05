---
name: run-improv
description: Fast improv support for QuestMaster. When players go off-script, gives the DM a one-line stalling move and two or three grounded, consequence-driven options, each showing what the world does next, what it costs and the choice it leaves the players, so the DM can pick one and keep playing. Use when the DM says the players did something unexpected, a plan collapsed mid-scene, a session derailed, or they need an instant answer at the table.
---

# Run Improv

The DM gets, in under a minute of reading, a holding move for right now and two or three different ways the world can answer what the players just did. The DM picks; nothing about the game changes unless they ask.

## Use this when

- "They just killed the quest-giver", "they set the inn on fire", "they skipped the dungeon".
- "The bard convinced the guard to join them, now what?"
- "My whole plan for tonight is gone", "they went the other way".
- The DM needs an NPC's reaction or the world's response, now.
- Not this: reworking the arc after the session (`develop-plot`); a full fight build (`design-encounter`).

## Steps

1. **Read fast.** `get_campaign_overview` (tone, active threads) and `search_campaign` for the NPCs, places and factions the DM named. Skip everything else. If one NPC's motive decides the options, one `get_entity` on that NPC is the limit.
2. **One question, only if needed.** If you cannot tell what happened, ask: "What did the players just do, specifically?" Otherwise answer straight away; the table is waiting.
3. **Find the core tension:** the question the players' action forces the world to answer ("Who now collects the debt the dead quest-giver was owed?").
4. **Generate** the bridge and the options in the format below, in the campaign's tone. Three options by default, two when the moment is narrow.
5. **Stop.** This is a chat answer. Draft nothing unless the DM asks to keep something.
6. **If the DM wants to keep it** (an NPC invented on the spot, a new thread): `search_campaign` first, then draft with `upsert_npc` or `upsert_thread`, `get_changeset`, a one-line recap, and `request_approval` when the DM says so, which can wait until after the session. Nothing is saved until it returns status applied.
7. **Hand back.** The DM chooses, plays it, and decides what every NPC does. Offer to log the choice later through `recap-session`.

## What to produce

Keep it short enough to read at the table. Lead with the bridge.

```
RIGHT NOW: one sentence the DM can use this second to buy a minute
(an NPC interjects, the environment demands attention, a messenger arrives).

THE SITUATION: what happened, in one sentence.
CORE TENSION: the question the world must now answer.

A. Evocative name (tone: escalation / opportunity / twist / emotional / practical / lateral)
   What happens: 2 to 3 specific sentences, with names and something observable.
   New dynamic: what the DM now has to play.
   Players can: the meaningful choice still in front of them.
   Upside: what it opens for the story.  Cost: what it complicates.
B. ...  (a clearly different tone and approach)
C. ...  (often the lateral one nobody expected)

THREADS TOUCHED: thread name: accelerated, derailed, reframed or untouched.
NEW THREAD?: name it, if the moment created one.
```

Read [references/options.md](references/options.md) the first time this skill runs in a session, or when the options feel samey: it holds the consequence engines, a bank of bridges, and a worked example.

## Drafting it

Only when the DM asks to keep something. Leaving a field out keeps it, null clears it, lists replace the whole list.

- **An NPC improvised at the table:** `upsert_npc` with `name`, `role`, `appearance`, `personality` (demeanor, coreTrait, flaw, speechPattern), `motivation` (immediate, longTerm, fear), `locationId`, `factionId`, and what happened in `notes`. Anything hidden goes in `secret`.
- **A new thread:** `upsert_thread` with `title`, `description`, `urgency` (low, medium, high, critical) and connected NPCs, factions and places. An existing thread that just got hotter: its `id` and a higher `urgency`.
- Everything else (what happened, which option was used) waits for `recap-session`.

## Don'ts

- Don't reset the world or quietly undo what the players did. The quest-giver stays dead, the inn stays burned; options build on that.
- Don't punish creativity. Consequences follow from the fiction; penalties invented to herd players back are railroading.
- Don't give three versions of the same idea, or an option whose only purpose is to return to the planned scene.
- Don't decide for the players or lock in an NPC's choice. These are options; the DM picks and plays them.
- Don't contradict canon. If you are unsure of a fact, frame the option around it ("if Ottile knows about the ledger, ...").
- Don't do long reads or write long answers mid-game, and don't draft anything unasked.

## Pairs well with

- `genre-*` packs for consequences that fit the genre; `style-npc-voice` when the DM needs the NPC's next line.
- `recap-session` to log what happened and the option chosen; `develop-plot` to rework the arc afterward; `generate-npc` to flesh out an NPC who stuck.

## References

- [references/options.md](references/options.md): read when you need consequence engines, a stalling move, or a model of good options.

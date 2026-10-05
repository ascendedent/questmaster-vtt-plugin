---
name: recap-session
description: Session recaps for QuestMaster. Turns a DM's raw notes, in any format, into a structured DM-only recap drafted onto the session, plus follow-through drafts the DM approves, such as thread updates, NPCs the party met, faction standing shifts and suggestions for next session. Use when the DM pastes notes, a transcript or a summary of a session that was just played, or asks to write up, log or recap a session.
---

# Recap Session

The DM gets their messy notes turned into a structured, searchable recap on the session, and a short list of follow-through changes so the campaign's state catches up with what happened at the table.

## Use this when

- The DM pastes session notes, bullet points, a timestamped log or a transcript.
- "Write up last session", "recap session 6", "log what happened tonight".
- "Update the threads after last night", "what do I need to follow up on?"
- Not this: planning the next session (`develop-plot`, which this hands off to); a live off-script moment (`run-improv`).

## Steps

1. **Read first.** `get_campaign_overview` (active threads, next unplayed session). Work out which session the notes cover: the notes may say; otherwise the session just played often still shows as the next unplayed one, because only the DM marks sessions played. Confirm with `list_entities` kind session if unsure. Then `get_session_prep` on that session (what was planned, staged secrets, planned encounters) to compare plan and play, `get_entity` on it to see whether a recap already exists, `get_plot_graph` for the beats in play, and `get_party` for character names. `search_campaign` every name in the notes to match existing NPCs, factions and places, spelling variants included.
2. **Don't interrogate.** Extract everything you can and mark anything ambiguous as [unclear]. Ask one question only when you cannot tell which session the notes are for, or when the session already has a recap: "Session 6 already has a recap. Replace it, or merge these notes into it?"
3. **Generate** the recap from [references/recap.md](references/recap.md), in the campaign's tone. For the prose voice of the story-so-far paragraph and the beats, follow `style-recap`.
4. **Build the follow-through list:** threads opened, advanced, closed or overdue; NPCs met for the first time; changes to known NPCs; faction standing shifts; staged secrets the players actually learned; loot; next-session focus. Mark judgment calls (closing a thread, an NPC's death, a standing change) so the DM checks them.
5. **Draft** the recap with `save_session_recap` and each follow-through change with the tools below, reusing existing ids and the refs creates return (`npc:2`).
6. **Recap and ask.** `get_changeset`, then show the DM the recap's headline and the follow-through list grouped by kind. Drop anything they reject with `discard_changes` and its `changeSeqs`, then `request_approval`. Nothing is saved until it returns status applied.
7. **Hand back.** Remind the DM what stays theirs in the app: marking the session played, setting the current plot beat and marking beats visited or shown, pushing the secrets players learned, handing items and gold to characters. Offer to start the next session's outline.

## What to produce

The recap, as Markdown: header, a one-paragraph "story so far", story beats (what happened, the player decision, the consequence, the thread impact), a player decisions log, NPC interactions, faction activity, threads (opened, advanced, closed, needing payoff), loot, DM follow-through, and a recommended focus for next session. Full template, parsing rules and an example: [references/recap.md](references/recap.md).

Specific beats generic: "Brannoc paid the toll-keeper's fine with the courier's ring, so the guild now thinks he has the ledger" is a decision the DM must honor; "the party dealt with the toll-keeper" is not.

## Drafting it

Leaving a field out keeps it, null clears it, and lists and long text fields replace the whole value, so read the record and resend what should stay.

- **The recap:** `save_session_recap` with `sessionId` and `recap` (the Markdown). It replaces the session's current recap when approved, and it is DM-only.
- **Session details:** `upsert_session` with the session's `id` for `playDate` (YYYY-MM-DD), `inWorldDate`, and `npcIds` of the NPCs who appeared. Leave the title alone unless it has none; players see it. The session is never marked played from here.
- **Threads:** `upsert_thread` with the thread's `id` to set `status` (active, resolved, abandoned), raise or lower `urgency`, or rewrite the `description` to include what moved. New threads: `title`, `description`, `urgency`, connected NPCs, factions and places. An overdue thread can be scheduled with `plannedSessionId` on the next session.
- **NPCs met:** `upsert_npc` for each new one (`name`, `role`, `appearance`, `relationshipToParty`, `locationId`, `factionId`, and what happened in `notes`). For known NPCs: `status` (alive, dead, unknown, missing), `relationshipToParty`, and `notes` with the new line appended to the existing text.
- **Factions:** `upsert_faction` with `partyStanding` (hostile, unfriendly, neutral, friendly, allied) when the session changed it.
- **What players learned:** match it against the session's staged secrets and list the ones the DM should now push. If players learned something that was never staged, offer `stage_secret` so the DM can push it as a record. Never push anything.
- **Unplanned developments:** if the party opened a new direction, offer a plot beat (`upsert_plot_node`) in the current arc; don't mark any beat current or visited.

## Don'ts

- Don't invent. No events, dialogue, rolls or outcomes that are not in the notes; gaps stay [unclear].
- Don't overwrite an existing recap, NPC notes or a thread description without reading it first and asking or merging.
- Don't push secrets, mark the session played, set plot beats current, or hand out items, gold or XP. Those are the DM's, in the app.
- Don't speak for player characters: record what players did, not what their characters secretly felt, and never rewrite a backstory as canon.
- Don't say the recap is saved before `request_approval` returns applied.

## Pairs well with

- `style-recap` for the voice of the story-so-far paragraph and the beats; `style-dm-prep-notes` for the follow-through list.
- `develop-plot` to turn the recommended focus into the next session's outline.
- `generate-npc` to flesh out an NPC the party met in passing; `genre-*` packs for tone.

## References

- [references/recap.md](references/recap.md): read before writing any recap; it holds the template, how to read messy notes, and a worked example.

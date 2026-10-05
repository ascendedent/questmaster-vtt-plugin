---
name: style-recap
description: Style rules for session recaps, a Previously on paragraph the DM can read aloud to open the next session plus a decisions table recording what the party chose and what it set in motion, written in the campaign's own tone. Keeps player-safe prose apart from DM-only notes and never invents what happened. Use when a DM shares session notes, a transcript or a summary after a session, or wants a recap to open the next one.
---

# Session recap

A recap does two jobs: it pulls the players back into the story in the campaign's own voice, and it records the choices the DM now has to honor.

## Use this when

- The DM pastes notes, a transcript, bullets or a voice-memo summary after a session.
- The DM wants an opening recap to read at the start of the next session.
- The DM asks what the party decided, promised or left unfinished.

## The rules

1. **Only what happened.** Work from the notes, not from the plan. Compare against `get_session_prep` to spot skipped beats, but never recap a planned scene the notes do not mention.
2. **Previously on: 4 to 8 sentences of prose.** Past tense, third person, in the campaign's register. Follow the session's shape: where they began, the turn, where they stopped. Close on the open question or cliffhanger the next session starts from. It must read aloud in under a minute.
3. **Credit choices to characters, specifically.** "Brannoc paid the toll in forged scrip" beats "the party crossed the river". Spell names as `get_party` does. A recap that could describe any party has failed.
4. **Never invent.** No added dialogue, motives, feelings or outcomes. Description of the world may carry the register; new actions may not. If a note is ambiguous, mark it [unclear: what] in the DM section and leave it out of the prose. If one gap changes the story (did the captain survive?), ask that one question, not a list.
5. **Player-safe prose, DM-only notes.** The prose holds only what the party saw or learned. An NPC's real motive, what happened off-screen and why the trap was there go in a separate section headed Behind the screen.
6. **The decisions table is a record, not a story.** One row per meaningful choice, including choices made by refusing or ignoring something; 4 to 10 rows. The last column is what the world may do about it, phrased as a possibility: "the ferry guild may refuse them passage", never "next session the guild attacks".
7. **Tone follows the campaign.** A grim campaign's recap does not crack jokes; a light one can keep a table joke if it is in the notes. Hold the register from `get_campaign_overview` (see the references).
8. **Flag, do not decide.** Close the DM section with up to three follow-through flags: threads that moved, threads gone quiet, promises made to NPCs. They are suggestions; the DM picks.

Hand it over in this shape:

```
## Previously on [campaign or arc]
[4 to 8 sentences of player-safe prose, ending on the open question]

## Decisions
| Who | What they chose | What happened | What it may set in motion |
|---|---|---|---|

## Behind the screen (DM only)
- [unclear: ...]
- Threads: opened ..., advanced ..., closed ...
- Follow-through: up to three flags
```

## Checklist before you hand it over

- [ ] Every event in the prose appears in the notes.
- [ ] Planned but unplayed beats are absent.
- [ ] The prose is 4 to 8 sentences, past tense, and ends on the open question.
- [ ] Choices are credited to named characters, spelled as in `get_party`.
- [ ] No secret, off-screen event or true motive in the prose.
- [ ] Ambiguities are marked [unclear], not guessed.
- [ ] The table includes refusals and inaction; its last column is phrased as possibility.
- [ ] The tone matches the campaign.
- [ ] NPC, place and faction names match `search_campaign`.

## Where it goes in QuestMaster

- Read `get_campaign_overview` (tone), `get_party` (names), `get_session_prep` (what was planned) and `search_campaign` for every NPC, place and faction in the notes.
- Draft the recap with `save_session_recap`. It drafts the session's recap; like every other draft, it waits for the DM's approval.
- Offer, do not assume: a new thread from the table goes in via `upsert_thread`, an NPC whose status or attitude changed via `upsert_npc`. Ask the DM before adding either.
- The prose can open the next session: offer it as the first beat of the next unplayed session via `upsert_session_beat`.
- Then `get_changeset` and `request_approval`.

## References

- Read [references/registers.md](references/registers.md) when matching the recap to the campaign's tone, or when the DM wants the opening recap to sound different.
- Read [references/examples.md](references/examples.md) before the first recap for a campaign, and whenever a draft feels generic, invents details or leaks a secret.

---
name: style-read-aloud
description: Style rules for boxed read-aloud text, the short passages a DM reads word for word when the party enters a place or a scene turns. Gives the assistant a 2 to 4 sentence form that leads with the senses, ends on something the players can act on, and never tells players what their characters feel or do. Use when drafting read-aloud for an encounter, a location or a session beat, or when tightening boxed text the DM already wrote.
---

# Read-aloud text

Boxed text is the DM's opening move in a scene: short enough to hold a table, concrete enough to picture, and finished with something the players can grab.

## Use this when

- Drafting the read-aloud for an encounter, a location, or a planned session beat.
- The party arrives somewhere new, a scene turns (the floor gives way, the bell stops), or an NPC makes an entrance.
- The DM asks to trim, tighten or rework boxed text they already wrote.
- Not for NPC dialogue (use `style-npc-voice`) or for text the players read themselves (use `style-in-world-documents` or `style-handouts`).

## The rules

1. **Two to four sentences, under about 70 words.** A table stops listening after roughly thirty seconds. Anything that does not fit goes into the DM notes as detail to give when a player asks or looks closer.
2. **Senses before facts.** Open on what reaches the characters first: a sound, a smell, heat or cold, movement. Layout and objects come after. Use at least two senses, and at least one of them is not sight.
3. **One exact detail beats three mood words.** Cut "eerie", "ominous", "mysterious" and "a sense of dread". Write the thing that causes the mood: a child's boot, still laced, set on the altar.
4. **Never assume what the characters feel, think or do.** No "you shiver", "you feel uneasy", "you step inside", "you draw your blade", "you realize". Describe the world; the players supply the reactions. "You see" and "you hear" are fine, because everyone perceives the obvious.
5. **End on something actionable.** The last sentence is the handoff: a door, a voice, an object that invites a hand, a sound coming closer, a figure who has just noticed them. Never end on a summary of mood.
6. **Show what anyone would notice, not what a check should earn.** Hidden doors, traps, true identities and monster names stay in the DM notes. Describe an unfamiliar creature by how it looks and what it is doing, not by its stat block name.
7. **Write for the mouth.** Present tense, short sentences, no parentheses, no numbers except a distance the party needs. If a sentence makes you stumble when you say it, rewrite it.
8. **Match the campaign and respect the table.** Hold the campaign's register (see the references). If `get_table_safety` lists a veil, describe the aftermath and the closed door, not the act; never put a line on screen.

## Checklist before you hand it over

- [ ] 2 to 4 sentences, readable aloud in under thirty seconds.
- [ ] The first sentence is a sense, not a measurement.
- [ ] At least two senses; at least one is not sight.
- [ ] No feelings, thoughts, decisions or movements given to the characters.
- [ ] No secret that a check, a question or a spell should earn.
- [ ] The last sentence gives the players something to act on.
- [ ] No mood adjective doing the job a detail should do.
- [ ] Names, colors and layout match what `search_campaign` returns.
- [ ] Nothing crosses the table's lines; veiled content stays off-screen.
- [ ] Overflow details are kept as DM notes, not thrown away.

## Where it goes in QuestMaster

- Read `get_campaign_overview` first for tone, and `search_campaign` for the place or NPC so details match what is already established (a door the campaign calls green stays green).
- **Encounter:** the box goes into the encounter's read-aloud text via `plan_encounter`. Tactics, hidden features and the "if they look closer" details go in the encounter's DM notes, never in the box.
- **Session beat:** a planned scene in an unplayed session gets its box via `upsert_session_beat`, followed by one DM-only line on what is hidden there.
- **Location overflow:** details that did not fit the box (what a closer look finds) can sit in the location's DM notes via `upsert_location`, ready whichever session the party walks in.
- When the tone is uncertain, offer two versions (say, a quiet one and a tense one) and let the DM choose. Then `get_changeset` and `request_approval`.

## References

- Read [references/registers.md](references/registers.md) when matching a campaign's tone, or when the DM asks for a different feel (grittier, lighter, punchier).
- Read [references/examples.md](references/examples.md) before the first box you write for a campaign, and whenever a draft feels long, flat or presumptuous.

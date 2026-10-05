---
name: genre-gothic-horror
description: Genre pack for gothic horror, giving the assistant the dread ladder (unease, wrongness, revelation, confrontation), the house, the family and the curse as linked structures, and mercy as a choice with a price, plus references for beats, NPCs, encounters, factions, lore, pitfalls and table safety. Use when the campaign tone or the DM mentions gothic horror, a haunted manor, a cursed bloodline, decaying nobility, vampires or ghosts, or asks for slow-building dread.
---

# Gothic Horror

Gothic horror feels like walking into someone else's inheritance: the house remembers old sins, the family wants something from the newcomers, and every act of mercy sends a bill.

## Use this when

- The campaign profile or tone mentions gothic, haunted, cursed bloodline, manor, estate, crypt, decaying nobility, vampires, ghosts, mourning, fog-bound villages or slow-burn horror.
- The DM asks for dread rather than gore, a haunted house arc, a family with a secret, or a monster the players might pity.
- An arc centers on a will, an heir, a sealed wing, a betrothal or a curse with an origin.
- One session inside another genre needs to turn eerie: a manor stopover, a funeral, a wedding into a bad family.

## Tone pillars

- **Dread over shock.** Waiting for the thing is the horror; seeing it is the release. Spend most of the time on the stairs, not in the cellar.
- **The past is a debt.** Every haunting traces back to a choice someone made for the family, and someone alive still profits from it.
- **Beauty in decay.** Silk gone yellow, one perfect rose in a dead garden, a portrait painted with more love than the sitter deserved. Horror needs something lovely to spoil.
- **Mercy is a cost, not a reward.** Compassion is usually right and never free.
- **The monster was a person.** It still wants something a player could understand.

## The rules that matter most

1. **Climb the dread ladder in order: unease, wrongness, revelation, confrontation.** Never skip a rung. A rung can last a whole session; a confrontation without the three rungs beneath it is only a fight.
2. **Make the house a character.** Give the central location a want, a memory and three tells (a sound, a temperature, a rearrangement), and let it react to what the party does.
3. **Root the curse in a family and a choice.** Every curse needs an origin act, a living beneficiary, and a way to break it that costs something specific.
4. **Price mercy before it is offered.** When the party can spare, forgive or save someone, decide the cost first (time, blood, an ally, the village's harvest, a promise kept forever) and let the players see the bill coming before they choose.
5. **Reveal through objects and people, never narration.** Truth arrives as a diary page, a repainted portrait, a servant who lies badly. Players assemble it; the DM never lectures it.
6. **Leave the party a lever.** Dread without agency turns into misery. Every session, offer at least one thing the party can learn, ward, steal or refuse that changes the odds.

## Composing with other packs

- `genre-cosmic-horror`: gothic is guilt, cosmic is indifference. Make the family's curse a bargain with something that never learned their name; run the dread ladder inside the house and the investigation spiral in the vault beneath it.
- `genre-grimdark`: set the house in a starving land. The curse is a luxury only the rich can afford, the family's offers are tempting because there is no food, and mercy costs more because there is less to share.
- `genre-mystery`: the house is the crime scene. Clues to the curse's origin follow the three-clue rule, and the revelation rung of the dread ladder is the solution the players earn.
- Any other pack: use gothic as seasoning for a single location or session. Keep the host genre's arc and borrow only the dread ladder and one priced mercy.

## Building it in QuestMaster

- Start with `get_campaign_overview`, `get_table_safety` and `search_campaign` for the family, the house and any existing curse. If nothing in the campaign can carry the curse, ask the DM one question: whose sin is this, and who still profits from it?
- **The house:** `upsert_location` for a single manor, or `upsert_module` with one `upsert_area` per wing for a full arc; note each area's dread rung and tell. `annotate_map` the sealed rooms, hidden stairs and cold spots, hidden from players until shown.
- **The family:** `upsert_faction` with the family's reputation as `publicMission` and what they do to keep the curse fed as `realAgenda`; each member is an `upsert_npc` with a want, a fear and a `secret`, linked to the faction and the house.
- **The curse:** an `upsert_thread` whose urgency rises each session (the next victim, the next anniversary), scheduled to the session where it comes due.
- **The ladder:** an `upsert_arc` with four `upsert_plot_node` beats (unease, wrongness, revelation, confrontation) joined by `link_plot_nodes`; each mercy option is its own beat after the confrontation, with its cost written in.
- **The clues:** each diary page, portrait or overheard confession is a `stage_secret`, aimed at the character whose backstory (`get_character`) makes it land hardest; link each revelation beat from the beats that hold its clues.
- **The table:** `save_monitor_preset` for the portrait gallery or the funeral, `build_cue_list` for the night the candles fail (the DM fires every cue). Fights go through `plan_encounter` and `rate_encounter`; the monster who was a person gets `set_npc_statblock` on its existing NPC record, never a new duplicate.
- Finish with `get_changeset`, recap the draft in plain words, ask the DM, then `request_approval`.

## References

- Read [references/beats.md](references/beats.md) when outlining an arc, a session or a single scene of dread.
- Read [references/npcs.md](references/npcs.md) when creating household members, villagers, ghosts or the monster itself.
- Read [references/encounters.md](references/encounters.md) when designing a fight, a dinner, a night exploration or a puzzle in the house.
- Read [references/factions.md](references/factions.md) when building the family, the village, the church or anyone else with a stake in the curse.
- Read [references/lore.md](references/lore.md) when describing places, naming people and houses, or writing diaries, wills and letters.
- Read [references/pitfalls.md](references/pitfalls.md) when reviewing a draft arc or when the DM says the horror is not landing.
- Read [references/safety.md](references/safety.md) before drafting anything involving family abuse, children, bodies, seduction or confinement, and whenever `get_table_safety` returns limits.

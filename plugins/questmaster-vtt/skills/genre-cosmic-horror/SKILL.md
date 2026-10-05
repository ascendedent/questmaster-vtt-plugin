---
name: genre-cosmic-horror
description: Genre pack for cosmic horror, giving the assistant the investigation spiral, rules for making knowledge cost the investigators something lasting, and small achievable wins against a threat that cannot be beaten whole, plus references for beats, NPCs, encounters, factions, lore, pitfalls and table safety. Use when the campaign tone or the DM mentions cosmic or eldritch horror, forbidden knowledge, cults, an unknowable entity, an investigation that keeps getting bigger, or horror the party cannot simply defeat.
---

# Cosmic Horror

Cosmic horror feels like pulling a thread that never ends: every answer makes the world larger and the investigators smaller, and the wins that matter are the ones that let ordinary people sleep tonight.

## Use this when

- The campaign profile or tone mentions cosmic, eldritch, unknowable, forbidden knowledge, cults, the deep, the stars, impossible geometry, strange signals or slow transformation.
- The DM wants an investigation campaign, a mystery that keeps widening, or a threat the party cannot simply kill.
- An arc involves a book, a site or a ritual that changes whoever studies it.
- The DM asks for horror that is vast and impersonal rather than personal and haunted.

## Tone pillars

- **Scale.** The threat is vast and indifferent. It does not hate anyone; it barely notices them, and that is worse.
- **Knowledge is damage.** Learning the truth costs the learner something that does not heal on a long rest.
- **The investigation is the adventure.** Legwork, interviews, archives and field visits are the main play, not the filler between fights.
- **Small wins are real.** Close this door, save this town, burn this copy. The whole remains, but the people saved are saved.
- **Human faces.** The entity stays off-screen; the cultist's children, the drowned surveyor's widow and the changed fisherman are on-screen.

## The rules that matter most

1. **Run the investigation spiral.** Each loop goes hook, legwork, brush with the edge, revelation, cost, wider frame. Every answer opens a larger question one ring further out (a house, a town, a region, a history, the sky).
2. **Make knowledge cost, and pay for it.** Each major revelation gives the investigator something useful (a ward, a weakness, a way in) and a lasting mark (a compulsion, a changed sense, a flaw, a debt). Offer the player the choice of mark from two or three.
3. **Never show the whole.** Describe edges, effects and human reactions. Never write a stat block for the entity itself; stat its servants, its cultists and the things it leaves behind.
4. **Define the small win before play.** Every session and every arc has a concrete, achievable victory written down in advance, so the party can succeed even though the whole cannot be beaten.
5. **Never let the spiral stall on one roll.** Every conclusion the party needs has at least three clues in different places, found by different methods.
6. **Offer an exit at every loop.** The party can stop digging at any revelation. State honestly what stopping costs (the town is not saved, the mark still spreads) and let them choose.

## Composing with other packs

- `genre-gothic-horror`: personal guilt over cosmic indifference. A family made a bargain with something that never learned their name: run the dread ladder in the house and the investigation spiral beneath it.
- `genre-grimdark`: the war is the small thing; the big thing is waking. Factions fight over forbidden knowledge as a weapon, nobody can be trusted with the cure, and scarcity makes the cult's free bread tempting.
- `genre-mystery`: an investigation where solving it costs. Keep three routes to every truth, as the mystery pack says, even though each route wounds the one who walks it.
- Any other pack: use cosmic horror as one discovered layer under another genre's arc. Keep the host genre's structure; borrow one spiral loop and one knowledge cost.

## Building it in QuestMaster

- Start with `get_campaign_overview`, `get_table_safety` and `search_campaign` for existing cults, sites and strange threads. If the campaign has no anchor for the threat, ask the DM one question: what ordinary thing in this world is already wrong, and has been for a long time?
- **The spiral:** an `upsert_arc` with one `upsert_plot_node` per revelation, linked outward with `link_plot_nodes` (each loop links to the next, wider one; no loops back). Mark which node holds each loop's small win.
- **The clues:** each clue is a `stage_secret` aimed at the character most likely to find it (the scholar gets the marginalia, the ranger gets the tracks); every revelation node is linked from at least three clue sources.
- **The costs:** each knowledge mark is an `upsert_homebrew` effect, shaped with `structure_homebrew` and checked with `validate_effects`, so the engine handles the numbers.
- **The threat:** the cult is an `upsert_faction` with a harmless `publicMission` and the real ritual in `realAgenda`; the waking is an `upsert_thread` with urgency, scheduled to the session it arrives.
- **The sites:** `upsert_location` or `upsert_area` for each site, and `annotate_map` for the wrong places (paths that loop, a valley only there at night), hidden until shown.
- **The fights:** `search_monster_sources` for servants and cultists, `upsert_bestiary_monster` to reskin them, then `plan_encounter` with `rate_encounter`. The entity itself is a thread and a set of effects, never a monster entry.
- **The table:** `save_monitor_preset` for a handout reveal (the corrected map, the surveyor's last sketch), `build_cue_list` for the signal sequence; the DM fires every cue. Finish with `get_changeset`, recap, ask, then `request_approval`.

## References

- Read [references/beats.md](references/beats.md) when outlining an investigation arc, a session or a single scene.
- Read [references/npcs.md](references/npcs.md) when creating scholars, witnesses, cultists, the changed or a patron.
- Read [references/encounters.md](references/encounters.md) when designing a brush with the edge, a cult fight, an interrogation, a strange site or the final closing of a door.
- Read [references/factions.md](references/factions.md) when building cults, institutions, suppressors or the town that made a bargain.
- Read [references/lore.md](references/lore.md) when describing the wrong, naming entities and places, or writing field notes and handouts.
- Read [references/pitfalls.md](references/pitfalls.md) when reviewing a draft or when the investigation stalls or the horror stops landing.
- Read [references/safety.md](references/safety.md) before drafting knowledge costs, transformation, madness, drowning or despair, and whenever `get_table_safety` returns limits.

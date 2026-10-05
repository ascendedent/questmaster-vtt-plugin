---
name: genre-swashbuckling
description: Genre pack for swashbuckling campaigns, giving the assistant set-piece escalation as the signature structure, rivals with honor codes, and design that rewards daring over caution, plus references for beats, NPCs, encounters, factions, lore, pitfalls and table safety. Use when the campaign tone or the DM mentions duels, pirates, privateers, masked heroes, port cities, court fencing or cinematic derring-do, or asks for play where bold moves pay off.
---

# Swashbuckling

Swashbuckling feels like a blade fight on a moving deck: quick wit, bold leaps, rivals who bow before they lunge, and a world that pays out for style.

## Use this when

- The campaign profile or tone mentions duels, rapiers, pirates, privateers, smugglers, masked vigilantes, regattas, masquerades, port cities, galleons or rooftop chases.
- The DM says "cinematic", "pulpy", "swashbuckler", "derring-do", "I want them swinging from the rigging", or complains that the party plans for an hour and then hesitates.
- A recurring rival, a duel, a chase or a heist with swords is the center of the next session.
- Another genre is running and the DM wants a lighter, faster register for one arc or one set piece.

## Tone pillars

- **Daring is the currency.** The bold move is the fast move, and the world rewards it with position, reputation and applause.
- **Rivals, not monsters.** The best enemies have names, codes, tailors and grudges with respect in them.
- **The floor never stays still.** Big scenes escalate in stages; every stage is higher, hotter or more crowded than the last.
- **Wit is an action.** Taunts, toasts, wagers and promises change a scene as much as a thrust.
- **Losing is a scene change, not an ending.** Capture, humiliation, debt and a lost ship are the usual price of failure.

## The rules that matter most

1. **Build every big scene as a set piece in 3 to 4 escalating stages.** Each stage adds a new prop, a new problem and a raised stake (the rope snaps, the fire reaches the sails, the hostage moves to the yardarm). Write each stage change as a trigger ("when the first barrel bursts"), not a schedule.
2. **Put the fastest path behind a risk.** Every set piece offers a safe route that costs time the villain uses, and a daring route (swing, leap, bluff, cut the line) that saves it. A failed stunt costs position, gear, dignity or freedom, almost never a life.
3. **Give every rival a written honor code.** Three clauses the rival keeps even when it hurts, plus one clause they will break under a named pressure. The code makes them predictable enough to exploit and devastating when broken. A rivalry climbs one rung per meeting: slight, draw, defeat, respect, resolution.
4. **Always write the outs.** Every fight lists how it ends without a death: yield, first blood, quarter, parley, a dive into the harbor. Defeat flows into the next scene (the brig, the stocks, the gala where the captor shows off the prize).
5. **Arm the room for both sides.** List 5 or more props per set piece, each with what it does when used (chandelier, rigging, powder kegs, a cart of oranges, a bell rope). Enemies use props first, so players learn the room is fair game.
6. **There is always an audience.** A crowd, a court, a crew or a broadsheet sees what happens. Track the party's reputation as a thread; let it open doors, close others and summon new challengers.

If the main rival or how lethal the DM wants duels to be is missing, ask the DM that one question before drafting.

## Composing with other packs

- `genre-heist`: the job is the set piece. Legwork sets up the stages, the execution escalates through them, and the rival crew robbing the same vault tonight has an honor code the party can exploit.
- `genre-political-intrigue`: court fencing. Duels settle votes, every challenge is a political move, and the masquerade is the stage where a mask slips at the worst moment.
- `genre-war-campaign`: privateers or commandos inside a war. Each set piece is a lever against a front's clock, enemy officers become rivals with codes, and capture feeds prisoner exchanges.
- `genre-gothic-horror`: a cursed ship or a plague port. Alternate bravado with dread, and let a rival's code be the one thing the horror cannot corrupt.

## Building it in QuestMaster

- Start with `get_campaign_overview`, `get_table_safety` and `get_party`; note what each character is good at so every stage of a set piece has a spotlight for someone. `search_campaign` for existing rivals, ships and ports before creating any.
- **Rivals:** `upsert_npc` with the honor code in the profile and the breakable clause in the DM-only `secret`. A rival who fights gets `set_npc_statblock` on that same record; QuestMaster computes the numbers.
- **Rivalries and reputation:** each is an `upsert_thread` with urgency that rises as the rematch nears, scheduled to the session where it lands.
- **Set pieces:** a chain of `upsert_plot_node` beats, one per stage, joined with `link_plot_nodes`. Inside a planned session, each stage is an `upsert_session_beat` with its trigger, its props and its outs written in.
- **Fights:** `plan_encounter`, then `rate_encounter` or `propose_encounter` for difficulty. Put props and hazards on the battle map with `annotate_map` (chandelier, powder, loose rigging), hidden until the DM shows them.
- **Places and gear:** ships, ports and rooftops are `upsert_location` or `upsert_area`; a fence or black market is an `upsert_shop`; a named blade is an `upsert_magic_item`.
- **Handouts and screens:** challenges, wanted posters and coded love letters are `stage_secret`, aimed at the character the rival has chosen. A ship's silhouette on the horizon is a `save_monitor_preset` or a `build_cue_list` the DM fires.
- Finish with `get_changeset`, recap the draft in plain words, ask the DM, then `request_approval`.

## References

- Read [references/beats.md](references/beats.md) when outlining an arc, a session or a single set piece.
- Read [references/npcs.md](references/npcs.md) when creating a rival, a captain, a patron or any recurring character.
- Read [references/encounters.md](references/encounters.md) when designing a duel, chase, boarding action, masquerade or any encounter.
- Read [references/factions.md](references/factions.md) when building navies, pirate compacts, trading companies, fencing schools or exiled courts.
- Read [references/lore.md](references/lore.md) when describing a port or ship, naming people and vessels, or writing challenges, articles and broadsheets.
- Read [references/pitfalls.md](references/pitfalls.md) when reviewing a draft or when the DM says the game feels static, silly or consequence-free.
- Read [references/safety.md](references/safety.md) before drafting captivity, cruelty at sea, romance or anything near slavery, and whenever `get_table_safety` returns limits.

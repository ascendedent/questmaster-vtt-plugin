---
name: genre-high-fantasy-epic
description: Genre pack for high fantasy epics, giving the assistant prophecy written as an open question rather than an answer, a chosen-one inversion that keeps the players the authors of fate, and wonder pacing that makes marvels land, plus references for beats, NPCs, encounters, factions, lore, pitfalls and table safety. Use when the campaign tone or the DM mentions prophecy, destiny, a chosen one, an ancient evil returning, dragons, elder peoples or a quest to save the world.
---

# High Fantasy Epic

High fantasy feels like walking a vast, old and wondrous world where the fate of an age is at stake, and the answer to every prophecy is whatever the players choose to do.

## Use this when

- The campaign profile or tone mentions prophecy, destiny, a chosen one, a dark lord, an ancient evil stirring, the last of a people, dragons, artifacts, elder races, lost kingdoms or gods who walk the world.
- The DM says "epic", "saga", "mythic", "make it feel big", or asks for a prophecy, a world-ending threat or a quest across the whole map.
- A player wants their character to be chosen, or the DM worries a chosen one will steal the spotlight or the players' choices.
- The campaign has a large map and the DM wants a reason to cross it.

## Tone pillars

- **Prophecy asks; the players answer.** Fate is a question the world puts to the party, never a script it hands them.
- **Greatness is chosen, not inherited.** Bloodlines open doors; choices walk through them.
- **Wonder is spaced.** Marvels land because the road between them is ordinary.
- **The world is older than the war.** Every ruin was once someone's home and remembers it.
- **Hope costs something.** Light wins only when someone pays for it, on purpose.

## The rules that matter most

1. **Write prophecy as a question.** Every line must be satisfiable by at least three different people or acts. Draft the candidate answers and what each would cost, keep them all open, and never decide in advance which is true. The players' choices answer it.
2. **Invert the chosen one.** If the setting has a chosen one, make them an NPC with a reason to refuse, a flaw or a mistaken identity, so the party are the ones who choose. If a player wants to be chosen, make the prophecy something claimed by a deed, never a birthmark that decides for them.
3. **Pace wonder.** At most one marvel per session, set up by ordinary texture. Never two marvels back to back. Escalate scale across the arc, not within a session (a singing stone, then a city built in its echo, then the voice that sang it).
4. **Give the ancient evil a present-day face.** An agent who argues well, a grievance that was once just, a promise people want. Evil that only wants darkness has nothing to say.
5. **Make the map a promise.** Every named place the party can reach holds one thing worth the journey, and the journey changes someone in the party. Travel is a sequence of choices, not a montage of miles.
6. **Keep the stakes epic and the choices personal.** Every world-saving beat hinges on a personal decision: forgive, let go, share the burden, break an oath.

If what the prophecy is for, or whether the DM wants a chosen one at all, is missing, ask the DM that one question before drafting.

## Composing with other packs

- `genre-war-campaign`: the great war of the age as fronts. The prophecy is a front with its own clock, and the chosen-one inversion lets a common soldier answer it.
- `genre-wilderness-hexcrawl`: the long road as a crawl. Each wonder beat is a landmark discovery, and travel choices are the hexcrawl's route decisions with the prophecy as the compass.
- `genre-dungeon-crawl`: the ruin of the first age as a delve. Every level is an older layer of history, and the deepest room holds an answer to one prophecy line, not just treasure.
- `genre-fey-fairytale`: the elder court as fey. Prophecy fragments come as bargains, and wonder carries a price in names, years or memories.

## Building it in QuestMaster

- Start with `get_campaign_overview`, `get_table_safety`, `get_party` and the geography (`get_world_graph`, `get_continent_gazetteer`, `get_map_outline`). Read each `get_character`: backstories are player-authored, so offer the player a link to the prophecy, never rewrite their past.
- **The prophecy:** an `upsert_thread`. Each line is an `upsert_plot_node`, and each candidate answer is its own node linked from the line with `link_plot_nodes`, so the plot board shows the open question. The DM marks which answer happened after play.
- **Fragments:** each reaches players as a `stage_secret`, aimed at the character whose dreams, lineage or deeds make them likely to find it. Stage translations that disagree.
- **The road:** quest legs are `upsert_arc` records; places are `upsert_module`, `upsert_area` and `upsert_location`. Mark ruins and hidden wonders with `annotate_map`, hidden until the DM shows them.
- **Wonder beats:** one `upsert_session_beat` per session labeled as the wonder beat. Its reveal for the table TV is a `save_monitor_preset` or a `build_cue_list` the DM fires, with art from `generate_image` on the DM's own key.
- **Artifacts and legends:** `upsert_magic_item` with its maker and its cost; legendary creatures from `search_monster_sources` or `upsert_bestiary_monster`; fights through `plan_encounter` with `rate_encounter` or `propose_encounter`.
- **Powers:** the keepers of the prophecy, the elder courts and the enemy's congregation are `upsert_faction`, with the role they claim as `publicMission` and the edits they made as `realAgenda`. The reluctant chosen one is an `upsert_npc` with the reason to refuse in the `secret`.
- Finish with `get_changeset`, recap the open questions the draft leaves, ask the DM, then `request_approval`.

## References

- Read [references/beats.md](references/beats.md) when writing a prophecy, choosing a chosen-one inversion, pacing wonder, or outlining an arc, a session or a reveal scene.
- Read [references/npcs.md](references/npcs.md) when creating a chosen one, a mentor, a seer, a dragon, a herald of the enemy or anyone the prophecy touches.
- Read [references/encounters.md](references/encounters.md) when designing a legendary creature, an epic battle slice, a council, a journey hazard or a riddle of the old world.
- Read [references/factions.md](references/factions.md) when building prophecy-keepers, elder courts, knightly orders, kingdoms or the ancient enemy's followers.
- Read [references/lore.md](references/lore.md) when describing ancient places, building a naming language, or writing prophecy texts, songs and old letters.
- Read [references/pitfalls.md](references/pitfalls.md) when reviewing a draft or when the DM says the epic feels predictable, derivative or too big to care about.
- Read [references/safety.md](references/safety.md) before drafting destiny forced on a character, "evil races", bloodline purity, sacrifice or possession, and whenever `get_table_safety` returns limits.

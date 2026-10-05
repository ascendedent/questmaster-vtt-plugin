---
name: genre-wilderness-hexcrawl
description: Genre pack for wilderness exploration where travel is the play, giving the assistant route choices with real costs, weather and supply as visible clocks, landmark-driven discovery, and random tables that stay short, local and honest, plus references for beats, NPCs, encounters, factions, lore, pitfalls and table safety. Use when the campaign tone or the DM mentions a frontier, wilds, an expedition, a survey, survival or uncharted country, or asks for overland travel that matters, a hex map, regional tables or a sandbox to explore.
---

# Wilderness Hexcrawl

Play feels like standing on a ridge with two days of food left, three things on the horizon, and an argument about which one is worth it.

## Use this when

- The campaign profile or tone mentions a frontier, borderland, expedition, survey, colony, uncharted country, wild lands, survival, or a map the party is meant to fill in.
- The DM asks for travel that counts, a sandbox, a region to explore, encounter tables, weather, or "what is out there".
- Sessions keep skipping the road with "three days later you arrive", and the DM wants the road to matter.
- The party's goal sits far away and there is more than one way to reach it.

## Tone pillars

- **Distance is a cost.** Every day spends food, light, daylight and the patience of whoever waits at the far end.
- **The land was here first.** Boundary stones, game trails, a chimney with no house: the wild is full of other people's stories, half erased.
- **Seen before reached.** Landmarks show on the horizon long before the party can touch them. Curiosity is the engine.
- **Small comforts are treasure.** A dry cave, a clean spring, a trapper who shares his fire.
- **Honest dice.** Tables and weather produce surprises nobody scripted, and the DM lets them stand.

## The rules that matter most

1. **Every journey offers at least two routes with different costs.** The ford is fast and watched; the ridge is slow and dry; the river barge is safe and talks to everyone. Never one road.
2. **Make supply visible and finite.** Count rations, water and one scarce item (torches, fodder, arrows) in days, not pounds. A number the players can read turns travel into decisions.
3. **Put a landmark in every sightline.** Each region gets 1 to 3 things visible from far off (a smoking peak, a lone white tree, a tower with one wall). Players steer by them and discoveries hang from them.
4. **Weather changes plans, not hit points.** Set the day's weather before the party picks a route. It should alter speed, visibility, navigation or rest; damage is the rare exception.
5. **Keep tables short, local and spent.** 6 to 8 entries per region, each a situation in motion, not a monster count. Strike or change an entry once it has happened. A table serves the DM's prep; it never overrules canon or the table's safety limits.
6. **Bring news home.** Every expedition returns to a base where the discoveries change something: a map is sold, a rival hears, a patron pays or panics, a road opens.

If the campaign has no base, goal or region yet, ask the DM one question before drafting: where does the party sleep safely, and what makes them leave it?

## Composing with other packs

- `genre-dungeon-crawl`: dungeons are the sites the hexes point at. One supply clock runs through both, so the trail decides how strong the party is at the dungeon door.
- `genre-fey-fairytale`: the wild is where borders thin. Make one region a fey crossing whose weather is time (a night that lasts three days) and whose fords ask for a price.
- `genre-gothic-horror`: shrink the map to one cursed valley of 10 to 20 hexes and let dread replace distance as the cost.
- `genre-grimdark`: supply becomes politics. Every forage roll takes food from someone, and the frontier was somebody's home.

## Building it in QuestMaster

- **Read the land first:** `get_campaign_overview`, then `get_continent_gazetteer` for named places and their bearings, and `get_world_graph` for the modules, areas and maps that already exist. The gazetteer carries no coastline or water data, so ask before treating a place as coastal. `search_campaign` before creating any place, NPC or faction.
- **Regions:** one `upsert_module` per expedition or frontier, and one `upsert_area` per region (areaType wilderness, with climate, terrain and dangerLevel). Write the region's weather table and encounter table into the area description.
- **Landmarks and sites:** each is an `upsert_location` in its region. The description is what the party sees from afar (player-visible); dmNotes holds what is really there. Use exits (N, NE, up, down and so on) to chain sites into a point crawl where each link is a day's travel.
- **Maps:** read an existing map with `get_map_outline`, then `annotate_map` its rivers (water), scree (climb), bog (difficult) and rockfall zones (hazard). Annotations start hidden and reveal as the party sees them.
- **Rumors:** each is a `stage_secret` aimed at the character most likely to hear it (the ranger from the trapper, the scholar from the archive). True or false, the DM's note on the source says which.
- **The goal and its deadline:** an `upsert_thread` with urgency that rises as supply falls, scheduled with plannedSessionId to the session when the pass closes or the patron's patience ends.
- **Set pieces:** `plan_encounter` for the ambush at the ford or the lair at the find, with a theme from `propose_encounter` for regional creatures and `rate_encounter` for difficulty; `upsert_session_beat` for each planned travel day worth playing.
- Finish with `get_changeset`, recap in plain words, ask the DM, then `request_approval`.

## References

- Read [references/beats.md](references/beats.md) when outlining an expedition arc, a travel session or a single travel watch.
- Read [references/npcs.md](references/npcs.md) when drafting guides, rivals, locals or anyone met on the road.
- Read [references/encounters.md](references/encounters.md) when writing a regional table, a crossing, a storm, an ambush or a meeting at another campfire.
- Read [references/factions.md](references/factions.md) when deciding who claims, taxes, guards or races for the wild country.
- Read [references/lore.md](references/lore.md) when describing terrain and weather, naming places, or writing field books, maps and handbills.
- Read [references/pitfalls.md](references/pitfalls.md) when travel feels like a slog, a treadmill of fights or a spreadsheet.
- Read [references/safety.md](references/safety.md) before drafting starvation, exposure, animal harm, isolation or displaced peoples, and whenever `get_table_safety` returns limits.

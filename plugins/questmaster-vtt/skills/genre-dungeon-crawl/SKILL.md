---
name: genre-dungeon-crawl
description: Genre pack for dungeon crawls, giving the assistant jaquaysed layouts with loops, multiple paths and verticality, factions living inside the dungeon, and resource clocks that make every torch and every hour count, plus references for beats, NPCs, encounters, factions, lore, pitfalls and table safety. Use when the campaign tone or the DM mentions a dungeon, delve, tomb, ruin, vault, catacomb, megadungeon or underground complex, or asks for a keyed map, a lair, a multi-level site or a dungeon that changes between visits.
---

# Dungeon Crawl

Play feels like a whispered argument at a junction: left toward the drumbeat, right toward the draft of cold air, or back up the shaft while the torches last.

## Use this when

- The campaign profile or tone mentions a dungeon, delve, ruin, tomb, vault, mine, catacomb, sunken temple, megadungeon or underworld.
- The DM asks for a keyed map, a lair, a multi-level complex, room descriptions, traps, or a dungeon the party will return to.
- The party's next goal is inside a single place with walls, and getting out matters as much as getting in.
- Another genre needs a set-piece site: the hexcrawl's find, the gothic house's cellars, the fey hill's hollow halls.

## Tone pillars

- **A place, not a corridor.** Someone built it for a reason, someone lives in it now, and those are different people.
- **Information is treasure.** A map, a password, the patrol's timing or which faction hates which is worth more than coin.
- **Time is the monster.** Torches burn, spells run out, wanderers arrive, and the dungeon notices.
- **Choices of route are the game.** Every junction is a decision with a cost the players can partly read.
- **Fair danger.** Every lethal thing is telegraphed. Players die from choices, not from surprises.

## The rules that matter most

1. **Jaquays the layout.** Each level gets at least two loops, two ways in, and one vertical link (shaft, chute, collapsed floor, spiral stair) to another level. No level is a single chain of rooms, and no critical path hides behind one secret door.
2. **Key every room in three lines.** What it was built for, what uses it now, and what changed. Add one thing to interact with. If a room has none of these, merge it into a corridor.
3. **Seed two or three factions inside, with a grievance between them.** The party is a lever: they can ally, trade, betray or play one off another. Every faction has a reason not to fight to the death.
4. **Run visible resource clocks.** Count light in turns, check for wanderers on a fixed rhythm, and keep an alarm clock for the dungeon's response. Tell the players what is ticking.
5. **Telegraph every lethal thing.** Scorch marks before the fire trap, bones before the lair, a dead delver's chalk warning before the pit. A save without a warning is a gotcha.
6. **The dungeon remembers.** Between visits, restock with consequences: barricades where the party broke in, a faction that moved into the room they cleared, the dead stripped of gear.

If the dungeon's builder and current occupants are not established, ask the DM one question first: who made this place, and who lives in it now?

## Composing with other packs

- `genre-wilderness-hexcrawl`: dungeons are the sites the map points at. One supply clock runs through both, and the trail decides what the party has left at the door.
- `genre-gothic-horror`: the dungeon is the family vault under the house. Run the dread ladder down the levels and make the deepest room the origin of the curse.
- `genre-fey-fairytale`: a hollow hill whose halls obey etiquette instead of traps. Rooms bind by rules (who speaks first serves) and the faction war is a court feud.
- `genre-political-intrigue`: the dungeon's factions are a miniature court. Treaties, hostages and betrayals among the depths, with the party as the outside power everyone courts.

## Building it in QuestMaster

- **Read first:** `get_campaign_overview`, `search_campaign` for any existing site, faction or NPC, and `get_world_graph` to see which modules, areas and maps exist. For an existing map, `get_map_outline` shows its grid, its travel exits and where they lead, its pins to interiors and floors, and its annotations; `view_map` shows the map itself with its grid numbered, so you can key rooms and place terrain by what is actually drawn.
- **Structure:** one `upsert_module` for the dungeon, one `upsert_area` per level (areaType dungeon, with dangerLevel), and one `upsert_location` per keyed room, with locationIdCode (A1, A2, B7), a player-visible description and dmNotes for the truth.
- **Loops and verticality:** draft doors as location exits (N, NE, E and so on, plus up and down). Exits are reciprocal by default, so set reciprocalExits false for one-way routes (a chute, a portcullis that only lifts from inside). Check each level has at least two loops before drafting.
- **Level maps:** when each level has its own battle map, connect them with `arrange_maps` (up and down between levels, two-way by default) and file each map under its level's area with `update_map`.
- **Map annotations:** `annotate_map` the terrain (difficult rubble, water, climb, tight crawlways, half and three-quarter cover), hazards (gas, collapse, the scything blade), zones for faction territory, and labels for secret doors. All start hidden and reveal as the party sees them.
- **Planned encounters:** `plan_encounter` for each lair and set piece with its mapId and locationId, encounterType (combat, social, puzzle, exploration, hybrid), success, partial and failure consequences, and faction politics in dmContext. QuestMaster rates them: use `propose_encounter` with a theme for a starting group and `rate_encounter` to check a mix. Never write the numbers yourself.
- **Inside factions:** `upsert_faction` per faction (publicMission is what they tell delvers, realAgenda is the truth), leaders as `upsert_npc` linked to their faction and lair room; monsters through `search_monster_sources` and `upsert_bestiary_monster`.
- **Clocks and finds:** the alarm clock is an `upsert_thread` whose urgency rises with each noisy foray; maps, passwords and rumors found inside are `stage_secret` entries aimed at the character who would read them.
- Finish with `get_changeset`, recap in plain words, ask the DM, then `request_approval`.

## References

- Read [references/beats.md](references/beats.md) when outlining a delve arc, an expedition session or a single room scene, or when laying out loops.
- Read [references/npcs.md](references/npcs.md) when drafting hirelings, faction envoys, prisoners, rivals or the boss.
- Read [references/encounters.md](references/encounters.md) when keying rooms, traps, puzzles, parleys, lairs or wandering tables.
- Read [references/factions.md](references/factions.md) when populating the dungeon with groups who want different things.
- Read [references/lore.md](references/lore.md) when describing rooms, naming the site and its levels, or writing graffiti, ledgers and chalk maps.
- Read [references/pitfalls.md](references/pitfalls.md) when a dungeon feels linear, grindy or unfair.
- Read [references/safety.md](references/safety.md) before drafting confinement, drowning, burial, crawling things, captives or desecrated remains, and whenever `get_table_safety` returns limits.

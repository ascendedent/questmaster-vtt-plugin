# Dungeon Crawl: factions

A dungeon with factions is a small country: borders, trade, grudges, a power vacuum. The party walks in as a new power, and every group inside starts calculating what it can get from them.

## How to use these

- Put 2 or 3 factions inside, plus one outside interest. More than four and players lose track.
- Each faction holds territory you can draw: mark it as a zone with `annotate_map` (hidden until seen) and note its border in the dmNotes of the rooms on the line.
- Draft each with `upsert_faction` (publicMission is what they tell delvers; realAgenda is the truth) and its leader with `upsert_npc` linked to the lair room.
- Give every pair of factions one specific grievance with a date or an object attached: the stolen furnace, the drowned chief, the bridge that was cut.

## Archetypes

### The squatters
- **Public face:** "We live here. Pass through quietly and nobody gets hurt."
- **Real agenda:** they hold the entrance as a toll business, and they quietly sell delvers' gear to the deeper factions.
- **Method:** tolls, guides for hire, and doors they can bar from their side.
- **Collides with:** anyone who finds a second entrance, because it ends their monopoly.

### The keepers
- **Public face:** the last servants of the builders, keeping the place as it was meant to be.
- **Real agenda:** they rewrote the builders' orders long ago to keep their own authority, and they fear anyone who can read the originals.
- **Method:** rules, keys, ceremony, and selective hospitality.
- **Collides with:** the cult (who want the place changed) and any party carrying the builders' records.

### The pack
- **Public face:** none. They are hungry and territorial.
- **Real agenda:** survive the season. They hunt the weak and avoid the strong.
- **Method:** ambush at chokepoints, retreat to a lair with one narrow entrance.
- **Collides with:** everyone. Other factions pay the party, or each other, to deal with the pack, or herd it at rivals.

### The cult below
- **Public face:** pilgrims who came to pray at a holy site.
- **Real agenda:** wake, free or feed whatever sleeps at the bottom.
- **Method:** buying sacrifices from the squatters, sabotaging the keepers' seals, recruiting the desperate.
- **Collides with:** the keepers directly; with the squatters, the alliance is profitable until someone learns what the sacrifices are for.

### The rival company
- **Public face:** a licensed delving crew with a fortified camp at the door, friendly to fellow adventurers.
- **Real agenda:** under contract from an outside patron to strip one specific item and then collapse the entrance with everyone else inside.
- **Method:** sharing maps generously, hiring away hirelings, and planting charges on the last day.
- **Collides with:** the party, once the party learns about the charges.

### The market
- **Public face:** neutral traders, scavengers and fences who sell to anyone.
- **Real agenda:** neutrality is profitable only while nobody wins. They prop up whoever is losing.
- **Method:** credit, information, and a hall where violence is forbidden by all sides' agreement.
- **Collides with:** whichever faction gets strong enough to stop needing them.

### The thing in the deep
- **Public face:** a legend in town; a voice in dreams; a cold draft from the lowest stair.
- **Real agenda:** out, or fed, or left asleep, depending on what it is. Decide which before play.
- **Method:** servants who do not know they serve; whispers to the desperate.
- **Collides with:** every faction above, who would unite against it if they knew. Usually they do not.

### The outside patron
- **Public face:** a temple, guild, crown or scholar who funds expeditions.
- **Real agenda:** one specific thing inside, and a reason to want everything else left alone.
- **Method:** charters, bounties, and expeditions sent to fail on purpose.
- **Collides with:** the builder's heirs, the rival company, and the party, the moment their interests split.

## Collision patterns

- **The power vacuum:** the party kills a faction leader, and the next session starts with the survivors fighting over who rules, and both sides asking the party to back them.
- **The alliance of convenience:** two hostile factions unite against the party after the alarm clock hits the top. Undo it by giving one of them a better offer.
- **The proxy war:** a faction hires the party to hit a rival, and the rival offers to pay double for the employer's head.
- **The secret treaty:** two factions that seem to be at war are trading in private (the squatters sell captives to the cult). Discovering it changes everyone's standing.

## Moving factions between visits

- Each faction takes one step on its real agenda and one reaction to the party.
- Write each move as an `upsert_plot_node` on the dungeon's arc, linked from the party action that caused it with `link_plot_nodes`.
- Update the zones on the map and the affected rooms' dmNotes, so the next visit shows the new borders.
- Adjust partyStanding on each faction as the party helps or harms it.

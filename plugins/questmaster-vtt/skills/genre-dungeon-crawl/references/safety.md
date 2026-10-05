# Dungeon Crawl: safety

Dungeons concentrate confinement, darkness, drowning, crawling things, captives and the dead. Most of it can be played as pressure and texture without lingering. Decide what stays on-screen before keying the rooms, because a keyed room is easy to forget is there.

## Always first

- Call `get_table_safety` before keying rooms, writing traps or filling a wandering table. If the owner has not shared limits, ask the DM once whether any topics should stay off the table.
- **Hard limits (lines) are absolute.** Remove them from the dungeon entirely: no rooms, no traps, no documents, no implied history.
- **Soft limits (veils) stay off-screen.** The fact can exist; the description stops at the door, and the party learns the outcome, not the detail.
- Write each safety change into the room's dmNotes ("veiled: captives' condition reported, never described") so a co-DM or a later session keeps it.

## Themes that commonly need a line or veil

### Confinement and claustrophobia
- **Risk:** crawlways, sealed rooms, cave-ins and being trapped can trigger real panic.
- **On-screen:** the tension of a tight squeeze with a visible exit, the relief of open space.
- **Off-screen or cut:** extended scenes of being stuck with no agency. Every sealed-room hazard needs a visible way out within the scene. If it is a line, remove tight terrain from the map annotations and replace crawlways with stairs.

### Being buried alive
- **Risk:** a common and severe fear; collapses and living tombs are dungeon staples.
- **Fix:** treat it as a default veil. A collapse cuts off a route; it does not bury a character. Report rescues in summary.

### Drowning
- **Risk:** flooding rooms and underwater passages are classic hazards and a common phobia.
- **On-screen:** rising water as a clock with clear outs.
- **Off-screen:** a character's experience of drowning from inside. If it is a line, swap water hazards for collapsing floors or gas.

### Darkness
- **Risk:** total-dark scenes can be distressing for some players, and frustrating for anyone without darkvision.
- **Fix:** keep total darkness short and give it a clear end (the torch relit, the shutter opened).

### Spiders, insects, worms and swarms
- **Risk:** among the most common table phobias, and dungeons are full of them.
- **Fix:** if any are lines, remove them from every room, table and bestiary pick now. Replace them with something equally dangerous: rats, oozes, constructs, animated rubble. Check `propose_encounter` themes before accepting a suggestion.

### Body horror
- **Risk:** parasites, oozes digesting the living, fused bodies, experiments.
- **On-screen:** the threat and its signs (a half-dissolved shield, a stitched seam).
- **Off-screen:** the process. Describe the result from a distance.

### Torture chambers and cruelty
- **Risk:** dungeons are often written with torture rooms as atmosphere.
- **Fix:** default to veil. A room can have been a cell; it does not need instruments described. Never put the party in a scene of being tortured unless the table has explicitly opted in.

### Captives and slavery
- **Risk:** factions holding prisoners, selling captives, using forced labor.
- **On-screen:** captives as people with names and choices, freeing them as a meaningful option, a faction's guilt as leverage.
- **Off-screen:** abuse of captives. Never describe it. If slavery is a line, make the prisoners hostages for ransom or debtors working off a contract they chose.

### Desecrated remains
- **Risk:** looting tombs, animated corpses, disturbed graves can clash with players' beliefs or recent grief.
- **On-screen:** respect or disrespect as a choice with consequences.
- **Off-screen:** decay in detail.

### Children
- **Risk:** child prisoners, child sacrifices, monster young.
- **Fix:** treat harm to children as a default line. Young monsters can be present and protected; their fate is a choice that never needs graphic description.

### Lethality and character death
- **Risk:** dungeon crawls are often more lethal than a table expects, and losing a character a player loves can sour a campaign.
- **Fix:** ask the DM how lethal the table wants this to be before drafting traps and set pieces. Telegraph every lethal danger, and offer costly retreats.

## Wandering tables and restocks

- Filter every table against `get_table_safety` when drafting and again when limits change.
- When restocking between visits, recheck: a faction's revenge on the party can easily drift into torture or captivity scenes the table veiled.

## Player characters

- Backstories from `get_character` are player-written. If a character has history with confinement, imprisonment or a lost companion in the depths, ask the DM before using it as a hook.

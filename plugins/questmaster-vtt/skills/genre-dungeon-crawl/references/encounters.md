# Dungeon Crawl: encounters

A dungeon encounter is a room with a problem in it and more than one way to solve it. Design the situation, the terrain and the outs; let QuestMaster rate the fight (`propose_encounter`, `rate_encounter`) and compute the numbers.

## Design principles

- **Something is already happening.** The goblins are arguing over a pot, the ooze is digesting a shield, the priest is mid-prayer. Activity gives the party a moment to choose.
- **Every fight has terrain.** A balcony, a pit, a narrow bridge, a rack of spears, a brazier to kick over. Mark it with `annotate_map` (cover, difficult, climb, water, tight, hazard).
- **Every inhabitant has a reason not to die.** Most will flee, surrender, bargain or call for help long before the last hit point.
- **Name the outs.** For each set piece, write at least two non-combat resolutions in the encounter's success and partial consequences.
- **Noise travels.** Every fight advances the alarm clock and draws attention from adjoining rooms.

## Combat situations

### The lair on two levels
- **Situation:** the faction's war band holds a hall with a gallery above it; archers on the gallery, the chief below.
- **Stakes:** the only stair down to the next level.
- **Complications:** the gallery is reachable from a side passage the party may already know; the chief's rival is on the gallery and would happily see him fall.
- **Outs:** take the gallery first; parley with the rival; go around by the vertical link and skip the hall.

### The barricade
- **Situation:** the party is holding a room while something tries to get in (a patrol, a swarm, the alarm response).
- **Stakes:** time to finish whatever they are doing (looting, ritual, healing).
- **Complications:** a second door nobody noticed; the barricade burns.
- **Outs:** abandon the room; collapse the corridor; open a different door and let the attackers meet a third party.

### The fighting retreat
- **Situation:** the party has what it came for and the dungeon is waking up.
- **Stakes:** the treasure, and whoever is slowest.
- **Complications:** the way they came in is now held. The loop is the escape.
- **Outs:** drop part of the loot as a distraction; take the one-way chute; bargain with a faction for passage.

## Social situations

### The parley at the border
- **Situation:** two factions' territories meet at a doorway marked with skulls on one side and paint on the other.
- **Stakes:** safe passage, an alliance, or a war the party starts by accident.
- **Complications:** each side wants the party to carry a message the other will not like.
- **Outs:** carry it honestly; edit it; refuse and pay the toll.
- Plan it with `plan_encounter`, encounterType social, and write what each side offers in dmContext.

### The prisoner exchange
- **Situation:** a faction holds someone the party wants, and wants something in return (a stolen idol, a captured chief, a key).
- **Stakes:** the prisoner's life and the faction's trust.
- **Complications:** the prisoner may not want to leave; the item the faction wants belongs to someone else.
- **Outs:** trade; steal back; offer a different service.

## Hazards and exploration

### The filling room
- **Telegraph:** waterlines on the walls at chest height; a drain grate packed with silt.
- **Effect:** a door seals and water rises over several rounds.
- **Outs:** clear the drain, open the ceiling hatch, break the sluice wheel, swim for the underwater exit marked by a draft of air bubbles.

### The bad air
- **Telegraph:** dead rats, torches burning blue and low, a sweet smell.
- **Effect:** flame ignites the pocket; breathing it slows everyone.
- **Outs:** go dark and feel along the rope line; vent it through the shaft above; burn it off deliberately from a safe distance.

### The loose floor
- **Telegraph:** cracked flagstones, a chair fallen through into darkness, wind coming up from below.
- **Effect:** the floor gives way to the level below.
- **Outs:** cross along the walls; use it as a deliberate shortcut down. A collapse is also a vertical link: draft it as an exit to the room beneath.

## Traps: the five parts

For every trap, write: **trigger** (what sets it off), **telegraph** (what warns), **effect** (what it does), **interaction** (how it can be disarmed, avoided, jammed or used), **reset** (whether it happens again). A trap with no telegraph is a gotcha; a trap with no interaction is a dice roll.

- **The counting stair:** every ninth step is a pressure plate that drops a portcullis behind the party. Telegraph: scratches on the wall every nine steps, left by the builders' workers. Use: lure pursuers onto it.
- **The honest scale:** a vault door opens only when its scale balances. Put too much on and the floor tilts; too little and nothing happens. Telegraph: a worn inscription of weights. Use: any object of the right heft works, including a party member.

## Puzzles with more than one answer

- **The sealed archive:** a door with three locks, keys held by three factions. Solutions: collect the keys (diplomacy or theft), break the hinges (loud: two steps on the alarm clock), or find the archivist's ventilation duct (tight, small creatures only).
- **The flooded chapel:** an altar underwater holds the item. Solutions: drain it by the sluice on another level, swim with a light source and a rope, bargain with whatever lives in the water.

## Wandering encounters, by activity

Roll or pick both a who and a what-they-are-doing. Six entries is enough per level.

1. A patrol on its rounds, bored, arguing about pay.
2. Scavengers stripping a body the party left behind.
3. A faction runner carrying a message the party could intercept.
4. Something wounded and fleeing deeper, leaving a trail.
5. A rival delver crew, as surprised as the party is.
6. A sign only: fresh droppings, a dropped torch still warm, a scream far off.

## Escalation: the alarm clock

1. **Quiet.** Normal routines. Wanderers on schedule.
2. **Uneasy.** Doubled patrols; doors that were open are shut.
3. **Alert.** Factions send scouts toward the noise; prisoners are moved.
4. **Mustered.** Barricades at chokepoints, ambushes on the obvious routes.
5. **Response.** The dungeon acts as a whole: the factions unite, the boss comes up, or the exits are sealed. The party should see this coming at step 4.

Track the alarm as an `upsert_thread` whose urgency climbs with the steps (low at quiet, critical at mustered), and tell the DM to announce each new step as it arrives.

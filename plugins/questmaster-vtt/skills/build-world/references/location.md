# Location template

Write this in chat first, then draft it. "Goes to" says where each part lands. Anything a
player could see goes in a `description`; everything else goes in `dmNotes`.

## Header

| Field | Value | Goes to |
|---|---|---|
| Type | town, dungeon, wilderness, structure, planar | area `areaType` (city covers village to metropolis) |
| Region | where it sits, or the nearest established place | area `description`, or the module it joins |
| Scale | village, town, city, site, region | how many locations you draft |
| Tone | dangerous, welcoming, ancient, corrupt | area `description` (as felt), module `tone` |
| Connected factions | who has presence or interest here | faction `primaryBaseLocationId`, threads |

## First impression (area `description`; repeat on the arrival location)

2 to 3 sensory sentences: what a traveler notices approaching or entering. This is what the
DM reads when the party arrives (`style-read-aloud` sharpens it).
- Generic: "A bustling market town with a dark secret."
- Specific: "You smell Coldharrow Ford before you see it: woodsmoke and fish oil. The toll
  bridge is lined with iron hooks, and every hook holds a cage no bigger than a birdcage, empty."

## History (DM-only: the main location's `dmNotes`)

- Founded: when, by whom, and why, even if approximate.
- Key event: the one moment that still shapes how people here live and think.
- Current state: who is in charge and what the dominant tension is.

## Districts or rooms (one `upsert_location` each)

For each meaningful part:
- **Character** (`description`): who lives or works here, what it looks, sounds and smells like.
- **Notable site** (the location's `name`): one building or feature worth naming.
- **Tension** (`dmNotes`): the local problem simmering here, and who is on each side.

## Power structure (`dmNotes`; rulers as NPCs)

- Who rules: name and title. Search for an existing NPC first; otherwise draft one with
  `upsert_npc` and this `locationId`.
- How they rule: force, tradition, coin, divine mandate, popular support.
- Who challenges them, legitimately or not.
- What the law looks like: enforced by whom, and the punishment a party is likely to meet.

## Economy (`dmNotes`; a shop with `upsert_shop` if the DM wants one)

- Primary industry: what it produces, trades or exploits.
- What's scarce, and why.
- Black market: what moves under the table and who profits.

## Culture and daily life

- Dominant attitude to outsiders, authority and magic (area `description`, as felt).
- Local custom: one tradition, superstition or social rule a traveler would notice
  (`description` for the visible part, `dmNotes` for what it hides).
- Common knowledge: what everyone here knows that outsiders don't. Each useful piece is a
  `stage_secret` with `subjectKind: "location"`, ready for the DM to push when the party asks.

## Internal tensions (threads)

Two tensions that interact, so pulling one moves the other. Each becomes an
`upsert_thread` with `connectedLocationIds` and the factions and NPCs on each side.
- Tension 1: "The bridge toll doubled after the flood; the farmers upriver are organizing."
- Tension 2: "The toll-keeper's son runs with the farmers." (Now tension 1 has a hostage.)

## Story hooks (threads)

1. Immediate: happening now, pulls the party in this session (`urgency` high).
2. Slow burn: takes sessions to uncover (`urgency` low or medium).
3. Personal: tied to a type of character (a former soldier, a cleric, a noble). If it ties to
   a specific character's backstory, offer it to the DM as an option in `dmNotes`; never
   write it as fact about that character.

## Dungeons and keyed sites

- One area (`areaType: "dungeon"` or `"structure"`), one location per keyed room.
- Room `description`: what they see on entering, in 2 sentences, naming the visible exits.
- Room `dmNotes`: what's hidden, who is here and what they want, what happens if the party
  lingers, and how the room changes if they come back.
- `exits` use N, NE, E, SE, S, SW, W, NW, up and down. Draft rooms in walking order and give
  each new room its exit back toward the entrance; the return door is added for you.
- Shape: loops instead of a single corridor, at least two ways to the deepest room, one
  room that changes on a second visit, one place to rest that isn't quite safe.
- Fights belong to `design-encounter`; mention the planned encounter in the room's `dmNotes`.

## Wilderness and planes

- Wilderness: the area carries `climate`, `terrain` and `dangerLevel`. Locations are the
  sites worth stopping at (the ford, the hermit's tree, the burned waystation), each with a
  sign the party sees from a distance in its `description`.
- Planes: give the place one rule that is different here ("sound arrives a heartbeat late"),
  shown in `description`, with its mechanics left to the DM or `homebrew-mechanics`.

## Worked example (compressed)

Area: **Coldharrow Ford** (`areaType` city, `dangerLevel` medium) in the current module.
- `description`: the smell, the bridge, the empty cages.

Locations, in walking order:
1. **The Toll Bridge**. `description`: cages on hooks, a clerk's booth, a bell. `dmNotes`:
   the cages held river-thieves until the flood; the new toll-keeper wants them full again.
2. **Pell's Smokehouse**, `exits {E: "location:1"}`. `dmNotes`: the black market for
   untaxed eel and stolen toll tokens.
3. **The Flood Shrine**, `exits {N: "location:2"}`. `dmNotes`: the priest knows the flood
   was let loose upstream on purpose.

Threads: "The farmers' toll revolt" (high), "Who opened the sluice?" (low).
Staged secret, `subjectKind` location: "Locals never ring the bridge bell after dark."

# Map recipes: gazetteer, hierarchy, exits, annotations

## Reading the gazetteer

`get_continent_gazetteer` returns, per place: `name`, `type` (region, settlement, mountain, river and so on), `fromNearestRegion` {`region`, `compass`, `bearingDeg`}, `position` {`x`, `y`} from 0 to 1 across and down the map, and any linked `module` and `map`. It also returns `attribution`.

- Position: `x` below 0.33 is the west, above 0.66 the east; `y` below 0.33 is the north (y grows downward). Say "far east", "south-west quarter", never a distance in miles unless the DM gave a scale.
- Bearing: "Holloway lies north-east of the Greyfen" comes straight from `fromNearestRegion`.
- What you cannot know: whether a place touches water, sits on a river or road, or is cut off by mountains. Region shapes, land and water are not in the gazetteer. Ask the DM, or keep the wording neutral.
- A place already showing a `module` or `map` is linked. Change it only if the DM asks.
- Quote `attribution` verbatim under any list of places you show or hand back.

## Grouping places into modules

- **Region module**: one region label and the settlements nearest it. Good for a sandbox arc.
- **Journey module**: a start, one or two waypoints and a destination along a bearing. Good for a travel arc.
- **City module**: one settlement linked to a module, its districts as areas, its buildings as maps.
- Linking a settlement to a module (`link_continent_location` with `moduleId`) gives it its own area in that module when approved. Don't also draft an area of the same name with `upsert_area`.
- One module per arc-sized chunk of play. If a module would hold more than six or seven places, split it.

## The hierarchy

```
continent place --link--> module --> area --> map(s)
                  \--link--> map (the map its pin opens)
```

- `update_map` with `moduleId`: the map gets its own area in that module (one map, one area).
- `update_map` with `areaId`: the map joins an existing area. Use this when a town area holds the town map plus its battle maps.
- Interiors and floors pinned inside a map appear in `get_world_graph` (`contains`). They are placed by the DM in the app; the assistant reads them and leaves them alone.
- `feetPerSquare`: 5 for battle maps; a larger value for town or regional maps, whatever scale the DM uses. `environment`: `exterior`, `interior` or `underground`.

## Exit patterns (`arrange_maps`)

- **Road chain**: Fen Road `E` to Holloway Town; Holloway Town `E` to Tallow Pass. Each exit comes back automatically (`W`).
- **Hub and spokes**: a market square map with exits to three district maps.
- **Vertical**: tower floors joined with `up` and `down`; a cellar is `down` from the ground floor.
- **Match the continent**: when both maps belong to places on the continent, the exit direction follows the bearing between them.
- **Check first**: `get_map_outline` lists each map's exits. If the other map already uses the opposite direction, no return exit is made: pick another direction or tell the DM.
- **Remove**: `{mapId, direction, to: null}`.

## Annotation recipes (`annotate_map`)

Grid squares count from the top-left (0, 0). `w` and `h` are in squares. Keep every rectangle inside the map's size from `get_map_outline`. Everything starts hidden; the app reveals it by what the party can see.

| Feature | Annotation |
|---|---|
| Rubble field | `terrain`, `terrainType` `difficult`, `moveCostMultiplier` 2 |
| Low wall, cart | `terrain`, `cover_half` |
| Arrow slit, thick hedge | `terrain`, `cover_three_quarters` |
| Pillar, standing stone | `terrain`, `cover_full`, `occludes` true |
| Mill pond, flooded crypt | `terrain`, `water` |
| Cliff face, ship's rigging | `terrain`, `climb` |
| Crawlspace, collapsed tunnel | `terrain`, `tight` |
| Forge, brazier field, acid pool | `terrain`, `hazard`, with a `hazard` block |
| Named place | `label` with `text` (players read it) |
| Building footprint | `building` with `text`; `occludes` true if its walls block sight |
| Region of interest | `zone` with `text` and a `color` |

Irregular shapes: send `geometry` as a list of rectangles. A river bend three squares wide:

```json
{ "kind": "terrain", "terrainType": "water", "color": "#3b6ea5",
  "geometry": [ { "gx": 0, "gy": 10, "w": 12, "h": 3 }, { "gx": 12, "gy": 8, "w": 3, "h": 8 } ] }
```

A forge hazard (dice and DC proposed, flagged for the DM):

```json
{ "kind": "terrain", "terrainType": "hazard", "text": "Forge",
  "geometry": { "gx": 14, "gy": 4, "w": 2, "h": 2 },
  "hazard": { "damageDice": "2d6", "damageType": "fire", "trigger": "enter",
    "save": { "ability": "dex", "dc": 13, "effect": "half" } } }
```

Annotation text is player-facing once revealed: "Forge", "Old Mill", "Collapsed Bridge". Never "Secret Door to the Cult Vault"; that belongs in the location's `dmNotes` or the encounter's `dmContext`.

## Worked example

The DM: "Link Holloway on my continent to the Greyfen module, and wire up its maps."

1. Read: the gazetteer shows Holloway (settlement) north-east of the Greyfen at position 0.62, 0.31, no module yet; `get_world_graph` shows module "The Greyfen Marches" and three unfiled maps: Fen Road, Holloway Town, Holloway Mill. None is on the players' screens.
2. Weave table shown to the DM:

| Place | Module | Area | Maps | Exits |
|---|---|---|---|---|
| Holloway (NE of the Greyfen) | The Greyfen Marches | Holloway (from the link) | Holloway Town, Holloway Mill | Fen Road `E` to Holloway Town |

3. Drafts:
   - `link_continent_location` {locationId: Holloway, moduleId: Greyfen Marches, mapId: Holloway Town}.
   - `update_map` {mapId: Fen Road, moduleId: Greyfen Marches}.
   - Holloway's area is created when the link is approved, so it has no ref in this draft. File the two Holloway maps in a second, small draft after approval: `get_world_graph` for the new area's id, then `update_map` {mapId: Holloway Town, areaId: it} and the same for Holloway Mill. Don't give them `moduleId` now: each would get an area of its own beside the settlement's.
   - `arrange_maps` {exits: [{mapId: Fen Road, direction: E, to: Holloway Town}]}.
   - `annotate_map` on Holloway Mill: the millrace as `water`, the grain loft edge as `climb`, sacks as `cover_half`, the wheel housing as `cover_full` with `occludes`.
4. `get_changeset`, the table again with the attribution under it, ask, `request_approval`.

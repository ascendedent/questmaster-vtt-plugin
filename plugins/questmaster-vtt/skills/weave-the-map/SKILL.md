---
name: weave-the-map
description: A procedure for weaving a QuestMaster campaign's geography together, from a continent map's places down to modules, areas and battle maps, with two-way travel exits and hidden map annotations, without ever touching the continent's land, water or regions. Use when a DM wants continent places linked to modules or maps, maps filed under modules and areas, maps connected by exits, or a map labelled and annotated with terrain and hazards.
---

# Weave the Map

The DM gets a campaign whose places connect: continent places linked to modules and maps, every map filed under the right module and area, exits that lead somewhere and back, and annotations waiting hidden until the party sees them.

## Use this when

- "Link my continent to my adventures", "this town on the map is where module two happens".
- `get_world_graph` shows maps with no module or area, or maps with no exits between them.
- "Label this map", "mark the difficult terrain and the cover", "add a fire hazard to the forge".
- A planned fight needs a map (put the map in place here; `update_encounter_plan` with `mapId` sets the fight on it).

## Steps

1. **Read first.** `get_campaign_overview`; `list_entities` kind `continent` and kind `map` (it shows `onPlayerScreen`); `get_world_graph` (modules, areas, maps, exits, interiors and floors); `get_continent_gazetteer` for the continent; `get_map_outline` for every map you will touch (grid size, exits, existing annotations, whether it is on the players' screens). `search_campaign` before naming a new module, area or location.
2. **Ask one question if essential**, for example "Which module do the settlements east of the Greyfen belong to?" Never a list.
3. **Plan the weave** and show it as a table before drafting: continent place, module and area, map(s), exits. Recipes: [references/map-recipes.md](references/map-recipes.md).
4. **Draft.**
   - Missing structure: `upsert_module`, `upsert_area` (refs work in the calls below).
   - Continent links: `link_continent_location` {`locationId` from the gazetteer, `moduleId`, `mapId`}. A settlement linked to a module also gets its area there, created on approval, so file maps into that area in a follow-up draft. `null` clears a link.
   - Filing maps: `update_map` {`mapId`, `moduleId` (the map gets its own area in that module; `null` unlinks) OR `areaId` (attach to an existing area; `null` sends it back to its own), `name`, `environment`, `feetPerSquare`, `diagonalRule`}.
   - Exits: `arrange_maps` {`exits`: [{`mapId`, `direction`, `to`}]}. Two-way by default: the other map gets the opposite exit unless it already has one there. `to: null` removes an exit.
   - Annotations: `annotate_map` {`mapId`, `add`, `update`, `remove`}. First `view_map` the map (zoom with `region` for precision) and read the coordinates off its numbered grid: columns along the top and rows down the left are the same `gx` and `gy` the geometry takes. Never guess where a feature is; if the picture doesn't settle it, ask the DM. Geometry stays inside the grid size.
5. **Recap and approve.** `get_changeset`, show the weave table and each map's annotations, flag any annotation `text` players will read once revealed, ask, then `request_approval`. Never call it saved before `applied`.
6. **Hand over.** Putting a map on the players' screens, revealing, moving tokens, and anything about the continent itself (generating it, its regions, its look) are the DM's, in the app.

## What to produce

- A weave table: place (with its gazetteer bearing) | module | area | map | exits.
- Per map: its annotations as a short list (kind, where, what it does, what players will read).
- When quoting the gazetteer: the `attribution` it returns, verbatim, under any list of its places.

## Drafting it

- `annotate_map` `add` entries: `kind` (`label`, `terrain`, `zone`, `building`); `geometry` {`gx`, `gy`, `w`, `h`} in grid squares, or a list of them for an irregular shape; `text`; `terrainType` (`difficult`, `cover_half`, `cover_three_quarters`, `cover_full`, `hazard`, `water`, `climb`, `tight`); `color` (#rrggbb); `occludes` (blocks sight); `moveCostMultiplier` (2 for difficult); `hazard` {`damageDice`, `damageType`, `trigger` (`enter`, `start`, `both`), `save` {`ability`, `dc`, `effect` (`half`, `negate`)} or null}.
- `arrange_maps` `direction`: N, NE, E, SE, S, SW, W, NW, up, down.
- `update_map` `environment`: exterior, interior, underground.
- Rooms inside an area that has no map: `upsert_location` {`areaId`, `name`, `description`, DM-only `dmNotes`, `exits`}.
- Leave a field out to keep it; `null` clears it; list fields replace the whole list.

## Don'ts

- Never edit, propose to edit, or work around the continent's land, water, coastlines or regions, and never generate a continent. The assistant only links places. If the DM asks for that, say it is outside what the assistant does and offer what is possible: linking, filing, exits, annotations.
- Never assume a place is coastal, riverside, in mountains or on a road. The gazetteer has names, types, bearings and rough positions, not land or water. Say "north-east of the Greyfen", not "on the Greyfen coast", unless a label says so.
- Never drop the map engine's attribution when quoting or listing gazetteer places.
- Don't touch a map that is on the players' screens; every map tool refuses it. Tell the DM it can be woven after it comes down.
- Don't put secrets in annotation `text` or map names; players read them once revealed. DM-only detail goes in a location's `dmNotes` or an encounter's `dmContext`.
- Hazard dice and save DCs are design numbers: propose them from the comparable rules hazard or ask, and flag them in the recap for the DM to confirm.

## Pairs well with

- `build-world` for what a linked place is like, `design-encounter` for the fight on a map, `session-prep` to put maps on prepared screens, `campaign-kickoff` for a new campaign's first module.
- `genre-wilderness-hexcrawl` and `genre-dungeon-crawl` for travel and layout patterns; `style-dm-prep-notes` for the weave table.

## References

- [references/map-recipes.md](references/map-recipes.md): read when planning the weave or annotating; reading the gazetteer, module and map hierarchies, exit patterns, and annotation recipes with geometry.

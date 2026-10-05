---
name: build-world
description: "A workflow for building places and powers in a QuestMaster campaign. Settlements, dungeons, wilderness sites and planes become areas and connected locations with DM-only notes; factions, faiths and political webs get a public mission, a hidden agenda, a leader, members and a base. Use when the DM asks for a location, a town or district, a dungeon layout, a faction, a religion, a cultural detail or the balance of power in a region."
---

# Build World

The DM gets a place or a power that existed before the party arrived and will go on after
they leave: named, causally grounded, full of tension and hooks, and drafted into
QuestMaster where NPCs, threads and fights can link to it.

## Use this when

- Location: "flesh out the river town", "a three-level crypt under the chapel", "what's in the salt marsh?"
- Faction: "a thieves' guild that isn't really about theft", "who actually runs the port?"
- A religion, a cultural detail, or the political landscape of a region or people.

## Steps

1. **Read.** `get_campaign_overview` (tone, setting, current module). `get_world_graph` for
   modules, areas and maps, so a new place lands in the right module. `search_campaign` for
   the name and for anything already filling the role; `list_entities` with kind `faction`
   to see every existing power. With a continent map, `get_continent_gazetteer` places
   things by name and bearing; it can't tell land from water, so never call a place coastal
   unless canon already does.
2. **Name the element**: location, faction, religion, cultural detail or political
   landscape. Pick the closest match and proceed. Ask one focused question only if something
   critical is missing ("Which module is this in: the current one, or a new one?").
3. **Write it** from [references/location.md](references/location.md) or
   [references/faction.md](references/faction.md) and show it in chat. Where taste decides
   (who really rules, how dark the agenda is), offer two options with their consequences.
4. **Draft it** as below, linking new records with the refs each create returns.
5. **Recap and ask.** `get_changeset`, a plain summary that separates what players can see
   from what is DM-only, then ask, then `request_approval`. Nothing is saved until it
   returns `applied`.
6. **Hand back.** Maps are drawn and linked in the app (`weave-the-map` can label and connect
   them once they exist). Opening a shop, pushing a secret and revealing a map annotation
   stay the DM's buttons.

## What to produce

- **Location**: first impression (2 to 3 sensory sentences for arrival), history (founding,
  key event, current state), districts or rooms each with a notable site and a tension,
  power structure, economy (industry, scarcity, black market), culture (attitude, custom,
  common knowledge), two tensions that interact, three hooks (immediate, slow burn, personal).
- **Faction**: type and scope, public mission vs real agenda, founding moment and turning
  point, leadership and hierarchy, recruitment and loyalty, what it controls, needs and is
  owed, relations with existing factions, an internal split, first contact with the party,
  three hooks (asset, obstacle, surprise).
- **Religion, culture, politics**: see the variants at the end of each reference.

## Drafting it

QuestMaster nests places: module (an adventure or region of play), then area (a town,
dungeon, wilderness, structure or plane), then location (a room or site in that area).
NPCs and faction bases point at locations.

- `upsert_module` only when the DM wants a new one: `name`, `description`, `tone`,
  `levelRangeMin`, `levelRangeMax`. Otherwise use the current module from the overview.
- `upsert_area`: `moduleId`, `name`, `areaType` (city, wilderness, dungeon, structure,
  planar), `description` (the first impression; keep secrets out), `climate`, `terrain`,
  `dangerLevel` (low, medium, high, extreme). A town is one area; a big city whose districts
  each need many sites gets one area per district.
- `upsert_location`: `areaId`, `name`, `description` (player-visible: what they see),
  `dmNotes` (DM-only: history, who rules, tensions, the black market, hooks), and `exits`
  like `{S: "location:2"}`. Exits only join locations in the same area, and the other
  location gets the return door by default. Draft rooms in walking order, giving each new
  one its exit back to a room already drafted.
- `upsert_faction`: `name`, `factionType`, `scope`, `description` and `publicMission`
  (player-visible: what the world believes), `realAgenda` (DM-only: the true aim, the
  internal split, the loyalty levers, who owes them), `partyStanding` (hostile, unfriendly,
  neutral, friendly, allied), `primaryBaseLocationId`, `leaderNpcId`.
- Leader and members: `upsert_npc` with `factionId: "faction:1"` and a `locationId`, then
  patch the faction with `leaderNpcId: "npc:2"`. Full profiles come from `generate-npc`.
- Relations between factions have no field of their own: write each side's view in its
  `realAgenda`, and make every live rivalry an `upsert_thread` naming both in
  `connectedFactionIds`.
- Hooks: one `upsert_thread` each (`title`, `description`, `urgency`, and the connected NPC,
  faction and location ids). The immediate hook usually has high urgency.
- Common knowledge and rumors players can pick up: `stage_secret` with `subjectKind`
  location or faction and the ref as `subjectId`.
- Patching existing records: `dmNotes`, `realAgenda` and `description` are replaced whole,
  so read them with `get_entity` and send the full new text.

## Don'ts

- Don't put a real agenda, a hidden ruler or a trap in `name`, `description` or
  `publicMission`. Those reach players.
- Don't contradict existing geography or history. If the request conflicts with canon, say
  so and offer a version that fits.
- Don't join locations in different areas with exits. Travel between maps is set in the app
  or with `weave-the-map`.
- Don't build a place nobody runs or a faction with no friction inside it: name who rules
  and who challenges them, and give every faction one internal split.
- Don't draft a whole region at once. A few locations and one faction per draft keeps the
  DM's approval readable.
- Don't say anything is saved before `request_approval` returns `applied`.

## Pairs well with

- The campaign's `genre-*` pack for faction archetypes and the sensory palette of its lore.
- `style-read-aloud` for first impressions, `style-dm-prep-notes` for `dmNotes` and `realAgenda`.
- `generate-npc` for rulers and members, `generate-lore` for histories and myths,
  `design-encounter` for what happens here, `develop-plot` for the threads, `weave-the-map`
  to attach the place to a map.

## References

- Read [references/location.md](references/location.md) when building a settlement,
  dungeon, wilderness site or plane, or a cultural detail of a place.
- Read [references/faction.md](references/faction.md) when building a faction, a religion
  or the political landscape of a region.

# Which tool for which job

Tools come in toolsets the DM chose when connecting: `core` (always), `rules`,
`encounters`, `content`, `maps`. If a tool you need isn't there, tell the DM which
toolset to turn on (Account, then Connections, in QuestMaster) rather than working
around it. `whoami` lists what this connection has.

## Finding your way

| Need | Tool |
|---|---|
| What can this connection do, which campaigns | `whoami`, `list_campaigns` |
| The campaign at a glance (always first) | `get_campaign_overview` |
| Find something by name before creating it | `search_campaign` |
| Browse one kind of record | `list_entities` (kinds: npc, faction, thread, session, arc, module, area, location, encounter, item, homebrew, monster, shop, map, continent, secret, draft) |
| Read one record in full, with its links | `get_entity` |
| Story structure | `get_plot_graph` |
| One session's prep | `get_session_prep` |
| The player characters | `get_party`, `get_character` |
| Table content limits | `get_table_safety` |
| How to work here (for clients without this plugin) | `get_assistant_guide` |

## Story and world (core)

| Make or change | Tool | Notes |
|---|---|---|
| An NPC | `upsert_npc` | `personality` {demeanor, coreTrait, flaw, speechPattern}, `motivation` {immediate, longTerm, fear}; `secret`, `notes` are DM-only |
| A faction | `upsert_faction` | `publicMission` (what the world believes) vs `realAgenda` (DM-only) |
| A plot thread | `upsert_thread` | urgency; `plannedSessionId` schedules it; connected ids replace the whole list |
| A story arc | `upsert_arc` | numbered when approved |
| A beat on the plot board | `upsert_plot_node` | needs `arcId`; a beat shown to players can't change |
| A line between beats | `link_plot_nodes` | no duplicates, no loops |
| A session | `upsert_session` | the title is player-visible; never marked played from here |
| A planned beat in a session | `upsert_session_beat` | unplayed sessions only |
| The session's DM recap | `save_session_recap` | replaces the current recap |
| Information for players | `stage_secret` | always staged; aim at characters with `audienceCharacterIds` |
| Module, area, room | `upsert_module`, `upsert_area`, `upsert_location` | room `exits` are two-way by default |
| Campaign name, setting, tone | `update_campaign_profile` | players see the name |
| A new campaign | `create_campaign` | approved by the DM; you can only keep building in it if they tick that box |
| Remove something | `delete_entity` | run with `dryRun: true` first to see what else it touches |

## Fights and monsters (encounters)

| Job | Tool |
|---|---|
| Find monsters (bestiary first, then homebrew and books) | `search_monster_sources` |
| A starting point at a difficulty | `propose_encounter` (drafts nothing) |
| Rate a mix or a planned fight (2024 budgets) | `rate_encounter` |
| Plan a fight with its roster | `plan_encounter` (read-aloud, `dmContext`, monsters, NPCs, `includeParty`) |
| Change a fight that hasn't started | `update_encounter_plan` (also puts it on a map with `mapId`) |
| Import or make bestiary monsters | `add_monsters_to_bestiary`, `upsert_bestiary_monster` |
| Give an NPC combat stats | `set_npc_statblock` (QuestMaster computes to-hit, DCs, damage) |

## Rules and content (rules, content)

| Job | Tool |
|---|---|
| Look up rules, spells, monsters, items | `search_rules`, `get_rules_entry` |
| Check structured effects before drafting | `validate_effects` |
| Homebrew class, subclass, species, spell, feat, monster, language, tool | `upsert_homebrew`; `structure_homebrew` turns prose into effects |
| Homebrew weapon or armor | `upsert_homebrew_gear` |
| A magic item or named heirloom | `upsert_magic_item` (`description`/`lore` player-visible, `secret` DM-only) |
| A rules item as the campaign's copy | `import_catalog_item` |
| An equipment pack | `define_equipment_pack` |
| A shop and its shelf | `upsert_shop` (never while open at the table) |
| A portrait for an NPC or monster | `generate_image` (the owner's own image key; write the appearance first) |

## Maps and the table screen (maps)

| Job | Tool |
|---|---|
| Read a map as text | `get_map_outline` |
| How modules, areas and maps connect | `get_world_graph` |
| A continent's places | `get_continent_gazetteer` (keep its attribution; land and water aren't known) |
| Rename or file a map | `update_map` |
| Travel between maps | `arrange_maps` (two-way by default) |
| Terrain, hazards, labels on a map | `annotate_map` (hidden until shown) |
| Link a continent place to a module or map | `link_continent_location` |
| Prepared screens and the running order | `get_screen_prep`, `save_monitor_preset`, `organize_presets`, `build_cue_list` |

Anything on the players' screens right now is refused. That is by design.

## Approval (core)

`get_changeset` (recap), `request_approval` (ask the owner), `discard_changes` (drop
some or all of the draft), `undo_changeset` (ask the owner to roll back an applied
change), `list_agent_history` (what happened before).

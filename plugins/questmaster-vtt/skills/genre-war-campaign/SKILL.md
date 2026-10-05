---
name: genre-war-campaign
description: Genre pack for war campaigns, giving the assistant fronts with clocks as the signature structure, missions where the party is the lever that moves a war, and consequences tracked at the scale of regions but shown at the size of one person, plus references for beats, NPCs, encounters, factions, lore, pitfalls and table safety. Use when the campaign tone or the DM mentions war, invasion, siege, occupation, armies, mercenary companies or resistance, or asks for choices that ripple across a whole region.
---

# War Campaign

A war campaign feels like standing in a storm of armies holding a crowbar: the war is far too big for the party to fight, and exactly the right size for them to move.

## Use this when

- The campaign profile or tone mentions war, invasion, siege, front lines, occupation, conscription, a mercenary company, resistance, rebellion, a border falling or refugees on the roads.
- The DM says "I want their choices to matter at scale", "mass battle", "the war should feel like it is moving", "they enlisted", or asks how to run a war without the party becoming the army.
- A battle, a siege or a mission behind enemy lines is the center of the next session.
- Several factions are already at odds and the DM wants a clock on all of it.

## Tone pillars

- **The war moves without permission.** Fronts advance between sessions whether the party acts or not.
- **The party is a lever, not an army.** They do the one thing a regiment cannot: the bridge, the courier, the ledger, the duke's captive son.
- **Every number has a face.** A lost village is a named miller; a won battle is a named recruit who lived.
- **Nothing is free.** Every mission spends time, and time ticks another front.
- **The other side is people.** Even a just war has soldiers across the line with reasons and letters home.

## The rules that matter most

1. **Run the war as 2 to 4 fronts, each with a clock.** A front has an objective, a clock of 4 to 8 segments where each segment is a visible change in the world, tick triggers, and a consequence when it fills. Tick clocks between sessions and whenever the party is elsewhere.
2. **Write every mission as a lever.** State it as "if the party does X, front Y moves by Z": a clock rolls back, freezes or jumps. If a mission moves no clock, no faction and no person the players care about, cut it.
3. **Make choices triage.** Offer 2 or 3 urgent missions at once that cannot all be done. Show what each one saves and what each one leaves exposed before they choose; let the untaken ones tick.
4. **Deliver scale at human size.** When a front moves, show it through one named person, one place and one object (the miller's daughter on the road carrying the millstone's iron pin, because the mill is gone).
5. **Give the enemy reasons.** A commander with a grievance, a soldier the party meets before they fight, one front where the enemy is in the right. Even a horde gets a logic: hunger, fear, an oath.
6. **Victory changes the problem.** Winning a front opens a new one: occupation, peace terms, an ally turned rival, soldiers coming home to nothing. Plan the morning after before the battle.

If who is fighting whom, and why, or whether the party serves an army or acts alone is missing, ask the DM that one question before drafting.

## Composing with other packs

- `genre-political-intrigue`: the war council and the peace table. One front is political (an ally wavering, a succession), and the court's schemes decide which fronts get reserves.
- `genre-grimdark`: a war without clean sides. Turn up the cost of every lever and keep the human-sized consequences, but give the party at least one thing per arc they can save outright, or misery stops being drama.
- `genre-swashbuckling`: privateers, commandos or a dashing officer corps. Lever missions become set pieces, enemy officers become rivals with honor codes, capture feeds prisoner exchanges.
- `genre-high-fantasy-epic`: the great war of the age. The prophecy is a front with its own clock, and the chosen-one inversion lets a quartermaster or a deserter answer it.

## Building it in QuestMaster

- Start with `get_campaign_overview`, `get_table_safety`, `get_party`, and the geography (`get_map_outline`, `get_world_graph`, `get_continent_gazetteer`) before placing fronts. `search_campaign` for existing armies, commanders and places.
- **Fronts:** each is an `upsert_arc`. Each clock segment is an `upsert_plot_node`, linked in order with `link_plot_nodes`. Lever outcomes branch forward from a segment and never loop back; to show a rollback, link to a new node that names the restored state.
- **Clock pressure:** each front also gets an `upsert_thread` whose urgency rises as the clock fills, scheduled to the session where it would fill.
- **Sides:** armies, crowns, mercenaries and partisans are `upsert_faction` records, with the war aims they announce as `publicMission` and what they want from the peace as `realAgenda`.
- **People:** commanders, soldiers and refugees are `upsert_npc`, each tied to a front; anyone who will fight gets `set_npc_statblock`. A mission is an `upsert_session` with `upsert_session_beat` entries for briefing, approach, lever, intrusion, exfil and ripple.
- **Battles:** `plan_encounter`, then `rate_encounter` or `propose_encounter`, for the party's slice of the fighting only. The wider battle is beats and map marks: front lines, fords, supply roads and hazards with `annotate_map`, hidden until the DM shows them.
- **Intelligence and screens:** dispatches, captured orders and letters home are `stage_secret`, aimed at the scout, the officer or the character with family in the war's path. The war map is a `save_monitor_preset`; a war council briefing is a `build_cue_list` the DM fires.
- Finish with `get_changeset`, recap which fronts and clocks the draft touches, ask the DM, then `request_approval`.

## References

- Read [references/beats.md](references/beats.md) when setting up fronts and clocks, running the between-session war turn, or outlining an arc, a mission or a scene.
- Read [references/npcs.md](references/npcs.md) when creating commanders, soldiers, enemies, profiteers or civilians caught in the war.
- Read [references/encounters.md](references/encounters.md) when designing a battle slice, a war council, a parley, a supply run or a codebreaking puzzle.
- Read [references/factions.md](references/factions.md) when building high commands, invaders, mercenaries, partisans or the powers that profit from the war.
- Read [references/lore.md](references/lore.md) when describing camps, sieges and occupied towns, naming units and battles, or writing dispatches and casualty lists.
- Read [references/pitfalls.md](references/pitfalls.md) when reviewing a draft or when the DM says the war feels static, pointless or relentlessly grim.
- Read [references/safety.md](references/safety.md) before drafting atrocity, interrogation, executions, children in danger or real-world parallels, and whenever `get_table_safety` returns limits.

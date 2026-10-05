# Campaign skeleton: outline, draft order, worked example

## The outline you show the DM (before drafting)

```
ASSUMPTIONS (overrule any): ...
PROFILE   name | setting | tone (+ packs) | pitch
FACTIONS  name: public face / real agenda (DM) / method / standing / leader
MODULE    name, levels X to Y; areas: name (type, danger)
THREADS   title (urgency) -> who it touches; [S1] if planned for session 1
ARC       title, theme; beats: opening -> middle options -> turn -> climax
SESSION 1 title; strong start; scenes; the choice; closing hook; clues
```

Keep it under 30 lines. Mark DM-only items with (DM). The DM should be able to say "swap faction two for something religious" and get a new outline, not a new interview.

## Draft order (each step uses refs returned by the steps before)

Refs below are illustrative. Always use the exact ref a call returns.

1. **Profile**: `update_campaign_profile` {name, setting, tone, description}. For a new campaign, `create_campaign` first and continue only if it was approved with build access (`list_campaigns` to find its id).
2. **Factions**: `upsert_faction` x2 or x3 -> `faction:1`, `faction:2`, `faction:3`.
3. **Leaders**: `upsert_npc` {name, role, factionId: `faction:1`, appearance, personality, motivation, secret} -> `npc:4` (one per faction).
4. **Leader links**: `upsert_faction` {id: `faction:1`, leaderNpcId: `npc:4`} for each.
5. **Module and areas**: `upsert_module` -> `module:7`; `upsert_area` {moduleId: `module:7`} -> `area:8` (and `area:9`).
6. **Optional rooms**: `upsert_location` {areaId: `area:8`, name, description, dmNotes}.
7. **Arc**: `upsert_arc` {title, description, theme, objectives} -> `arc:10`.
8. **Session 1**: `upsert_session` {title, summary, arcId: `arc:10`, npcIds} -> `session:11`.
9. **Threads**: `upsert_thread` {title, description, urgency, connectedNpcIds, connectedFactionIds, plannedSessionId: `session:11` for the session 1 ones} -> `thread:12`...
10. **Plot beats**: `upsert_plot_node` {arcId: `arc:10`, title, description, isRoot: true on the opening beat, threadIds, npcIds, sessionId: `session:11` on beats meant for session 1, moduleId: `module:7`} -> `node:16`...
11. **Lines**: `link_plot_nodes` {fromNodeId, toNodeId, label}. Middle beats fan out from the opening and converge on the turn. Loops are refused.
12. **Session beats**: `upsert_session_beat` {sessionId: `session:11`, title, description, npcIds, locationId, factionId, threadId, occurredAtInSession: 10, 20, 30...}.
13. **Clues**: `stage_secret` {title, body, sessionId: `session:11`, subjectKind, subjectId, narrativeNodeId}.
14. `get_changeset`, recap, ask, `request_approval`.

If a call is refused, fix that one call and continue; the rest of the draft stands. If the DM wants one part dropped, `discard_changes` with its `changeSeqs`.

## Field discipline

- Players see: campaign `name`, session `title`, NPC `name` and `appearance`, faction `name`, `description` and `publicMission`, location `name` and `description`, a staged secret's `title` and `body` once pushed.
- DM-only: faction `realAgenda`, NPC `secret` and `notes`, location `dmNotes`.
- A session title is a promise, not a spoiler: "Smoke over the Commons", never "The Wardens Betray You".

## Worked example: Ashfall Commons

Pitch (from Q1): a market town in the shadow of a dormant volcano, where the vents that keep it quiet are failing and three groups each think they know why. Packs: `genre-political-intrigue` primary, `genre-wilderness-hexcrawl` flavor. Tone: tense and grounded. Party: level 3, hired by the town council.

**Profile.** Name "Ashfall Commons". Setting "A terraced market town on the flank of the dormant mountain Old Kettle, rich from sulfur and ash-glass." Tone "Tense, grounded, political; small people under a large mountain."

**Factions.**
- The Kiln Wardens. Public: keep the vent caps sealed and the mountain asleep. Real (DM): they have been selling cap sulfur to an outside alchemist; the caps are thin and they are covering it up. Leader: Warden-Captain Oda Fenwright, precise, ashamed, will sacrifice a subordinate before admitting it.
- The Cinder Market. Public: free traders keeping prices fair. Real (DM): buying hillside deeds cheaply because their surveyor predicted an eruption. Leader: Hollis Varne, a jovial broker who never writes anything down.
- The Smokeless Chapel. Public: prayers keep the mountain calm. Real (DM): its founder had a vision that fire will cleanse the town and is quietly loosening a cap. Leader: Mother Sarai Quell, gentle, certain, generous to the poor.

Collisions: the Market needs the Wardens' secret kept until the deeds are bought; the Chapel needs the caps to fail; the Wardens need everyone looking at the Chapel.

**Module.** "The Terraces", levels 3 to 5. Areas: Lower Commons (city, medium danger), the Vent Fields (wilderness, high danger).

**Threads.**
- The Caps Are Cracking (high, S1): Wardens, Chapel.
- A Surveyor in the Ash (medium, S1): Market; the body holds a marked map.
- Deeds Changing Hands (medium): Market, the council.
- Hook slot for a PC backstory (low): to be filled once the DM picks one.

**Arc 1: The Mountain Remembers.** Theme: who pays when the people in charge lie. Objectives: learn why the caps fail; decide who the town hears it from; survive the first tremor.
- Opening (root, S1): ash storm on market day.
- Middle options: follow the surveyor's map; audit the Wardens' ledger; attend the Chapel's night vigil.
- Turn: the party learns two factions are lying for different reasons.
- Climax: a cap blows during the harvest fair; who the town blames is the party's call.

**Session 1: Smoke over the Commons.**
- 10 Strong start: an ash squall hits the market; the crowd stampedes toward the Chapel; a Warden is trampled clutching a cap-seal tally.
- 20 The council's job offer, made in a room with Varne already present.
- 30 The surveyor's body in the Vent Fields, map missing a corner.
- 40 Choice: report the tally to the Wardens, sell it to the Market, or show it to Mother Quell.
- 50 Closing hook: the mountain coughs once; every bell in town rings.

Clues staged for session 1: the cap-seal tally lists twice the sulfur the caps hold (subject: the Kiln Wardens); the surveyor's map is in Market handwriting (subject: the Cinder Market).

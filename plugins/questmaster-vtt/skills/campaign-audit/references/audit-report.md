# Audit checks and report template

Every check below names the data that proves it. If the data is missing (no recap, no sessions played yet), skip the check and say so in one line. Flags carry a weight: **high** (will bite at the next session), **medium** (will bite this arc), **low** (tidiness).

## Checks

### Threads (`list_entities` thread, `get_entity` thread)
- **Overdue payoff** (medium; high if urgency is high or critical): `status` active, `sessionsOpen` 3 or more, no `plannedSessionId`, and no unvisited plot beat lists it in `threadIds`.
- **Urgent but unplanned** (high): urgency high or critical, not planned for the next unplayed session, and no beat of that session has it as `threadId`.
- **Ready for resolution** (opportunity): every plot beat that lists it has been visited and its staged secrets are pushed. Suggest a payoff scene.
- **Orphaned** (medium): no connected NPC, faction or location, and no plot beat links it.
- **Dead end** (medium): every connected NPC is dead or missing and no faction is connected.
- **Zombie** (high): resolved or abandoned, but still planned for an unplayed session or listed on an unvisited beat.

### NPCs (`list_entities` npc, `get_entity` npc)
- **Orphan** (low): no `factionId`, no `locationId`, and in no thread, plot beat, session `npcIds` or encounter roster. A lone wanderer may be intended; ask, don't assume.
- **Overdue to reappear** (medium): connected to an active thread, but `lastSeenSessionId` is two or more played sessions back.
- **Secret never staged** (medium): the NPC has a `secret`, no staged secret has `subjectKind` npc with this NPC's id, and no plot beat lists them.
- **Dead but busy** (high): `status` dead, yet leading a faction, in an unplayed session's `npcIds` or beats, on a planned encounter roster, or the only contact of an active thread. A ghost may be intended; ask.

### Factions (`list_entities` faction, `get_entity` faction)
- **Orphan** (low): no members, no `leaderNpcId`, in no thread's `connectedFactionIds`.
- **Leaderless** (low): members but no leader.
- **Leader elsewhere** (medium): the leader NPC's `factionId` is a different faction.
- **Standing drift** (medium): the last recaps describe the party helping or hurting the faction, but `partyStanding` has not moved.
- **Unused collision** (opportunity): two `realAgenda`s that clash, with neither faction in an active thread.

### Secrets (`list_entities` secret)
- **Never assigned** (medium): `staged` true, no `sessionId`, and no `narrativeNodeId`.
- **Missed reveal** (high): `staged` true, and its `sessionId` is a played session. Move it forward or drop it.
- **Stale subject** (medium): about an NPC now dead or a thread now resolved.
- **Thin chain** (medium): the beat one line after the current beat is a revelation, but fewer than three secrets point at it.

### Sessions and prep (`list_entities` session, `get_entity` session, `get_session_prep`)
- **Unplayed without beats** (high for the next session, medium after): an unplayed session whose `beats` is empty.
- **Thin next session** (high): the next unplayed session has no beats, planned threads, encounters or secrets.
- **Out of order** (low): an unplayed session numbered below a played one. Skipped, or forgotten? Ask.
- **No recap** (medium): a played session with an empty `recap`. Point to `recap-session`.

### Encounters and maps (`list_entities` encounter, map, module)
- **No map** (low; medium if the DM runs fights on maps): a planned combat with no `mapId`.
- **Unscheduled** (low): a planned encounter with no `sessionId`.
- **Left behind** (medium): still planned, tied to a played session.
- **Out of level** (medium): its `partyLevel` is below the party's current level. `rate_encounter` with its `encounterId` and report the new rating.
- **Unfiled map** (low): a map with no `moduleId` and no `areaId`. Point to `weave-the-map`.
- **Empty module** (low): a module with no areas and no maps.

### Plot board (`get_plot_graph`)
- **Empty arc** (low): an arc with no beats.
- **Done but open** (medium): an arc marked complete with unvisited beats.
- **Island** (low): in an arc of three or more beats, a beat with no line in or out.
- **Dead end** (high): the current beat has no line out.
- **Skipped** (low): a beat tied to a played session but not visited.

### Contradictions with canon (recaps against records)
- **Recap vs record** (high): a played session's recap says an NPC died, left, moved or changed sides, but `status`, `locationId` or `factionId` says otherwise.
- **Duplicates** (medium): two NPCs or factions with the same or nearly the same name (`search_campaign`).
- **Timeline** (medium): a session's `inWorldDate` earlier than the session before it; a thread planned for a session before the one it opened in.
- **Level band** (low): the current module's level range does not contain the party's level.

### Agent history (`list_agent_history`)
- **Waiting** (medium): changesets frozen and waiting for approval. The DM may want to approve or discard them before more drafting.
- **Undone** (note): changesets the DM undid. Do not re-propose the same content without asking.
- **Recent additions** (note): what agents added since the last played session, for the DM to skim.

## Report template

```
# Campaign Audit: <campaign name>
Scope: <whole campaign | arc N> | Sessions played: N | Party level: X
Current arc: <title> | Current module: <name> | Next session: N <title>
Not covered: <anything skipped and why>

## Thread Health
| Thread | Status | Urgency | Sessions open | Planned for | Flag |
Overdue payoffs: ...
Ready for resolution: ...
Orphaned or dead-end threads: ...

## NPC Roster
| NPC | Role | Status | Last seen | Flag |
Overdue to reappear: ...
Secrets never staged: ...

## Faction Standings
| Faction | Standing | Leader | Members | Active threads | Flag |
Collisions in play / unused: ...
Standing shifts to consider: ...

## Secrets and Clues
## Prep Gaps (sessions, encounters, maps)
## Plot Board

## Consistency Issues
| Issue | Record A (where) | Record B (where) | Decision needed |

## Pending Agent Drafts

## Recommended DM Actions
1. **<action>** (<weight>): <why, in one line>. Skill: <workflow skill>.
2. ...
```

Mark DM-only content with (DM) when you must mention it. Use names, not ids, in the prose; ids only if the DM asks.

## Prioritizing the actions

1. Contradictions and zombies that will surface at the next session.
2. Gaps in the next session's prep (no beats, a missed reveal, an urgent unplanned thread).
3. Overdue high-urgency threads and NPCs overdue to reappear.
4. Anything blocking the current beat (dead end, thin clue chain).
5. Tidiness: orphans, unfiled maps, empty arcs.

Keep it to 3 to 7 actions. Each one names a single concrete step ("Plan The Caps Are Cracking for session 6 and give it a beat"), not a theme ("work on threads").

## Example findings

| Flag | Evidence | Action |
|---|---|---|
| Missed reveal (high) | Secret "Ledger in Market hand" staged, session 4 played | Move it to session 5 or drop it; `session-prep` |
| Dead but busy (high) | Oda Fenwright has status dead but is still leader of the Kiln Wardens | Pick a new leader or mark the faction headless; `build-world` |
| Overdue payoff (medium) | "Deeds Changing Hands", open 4 sessions, urgency medium, no beat | Give it a beat in arc 1 or downgrade it; `develop-plot` |

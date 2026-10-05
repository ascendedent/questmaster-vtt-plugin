---
name: campaign-audit
description: A read-only continuity and thread-health check for a QuestMaster campaign that reports threads overdue for payoff, orphan NPCs and factions, contradictions with canon, secrets never assigned to a session, unplayed sessions without beats, encounters without a map and stale drafts, each with a recommended DM action. Use when a DM asks what needs attention, what is overdue, whether anything contradicts, or wants a campaign health check or state summary.
---

# Campaign Audit

The DM gets one prioritized report on the campaign's loose ends and contradictions, with the evidence for each and what to do about it. Nothing in the campaign changes.

## Use this when

- "What needs attention?", "what's overdue?", "did I contradict myself?", "give me a state summary".
- Before a new arc, after a long break, or when session prep keeps tripping over loose ends.
- After a batch of approved drafts, to check they still fit together.

## Steps

1. **Read, and only read.** `get_campaign_overview` (session count, current arc and module, next unplayed session). Then, paging with `nextCursor` until done:
   - `list_entities` for `thread`, `npc`, `faction`, `session`, `encounter`, `secret`, `arc`, `map`, `module`.
   - `get_entity` where the short fields are not enough: threads (`sessionsOpen`, `plannedSessionId`, connected NPCs, factions, locations), NPCs (`status`, `secret`, `lastSeenSessionId`), factions (`leaderNpcId`, `members`), sessions (beats, `played`, the recap of the last two played sessions).
   - `get_plot_graph` (current beat, visited and shown beats, lines); `get_session_prep` for the next one or two unplayed sessions.
   - `list_agent_history` (drafts waiting for approval, recent applied and undone changesets); `get_party` (levels, for stale fights). `rate_encounter` on an old planned fight if the party has levelled since; it only reads.
   - In a large campaign, audit the current arc and everything it touches first, and say what was not covered.
2. **Ask one question only if the scope is unclear**, for example "Whole campaign, or just the current arc?" Default: whole campaign, current arc first.
3. **Run the checks** in [references/audit-report.md](references/audit-report.md): thread health, NPC and faction health, secrets, sessions and prep, encounters and maps, the plot board, contradictions with canon, agent history.
4. **Write the report** in the template from the same file. Every finding names the records (kind and name), the evidence, why it matters at the table, and one recommended action with the skill that can draft it.
5. **Draft nothing.** End by offering: "Want me to draft fixes for any of these?" A yes starts a new task with the matching workflow skill, its own draft, `get_changeset`, the DM's go-ahead and `request_approval`.
6. **Contradictions are the DM's call.** Present both versions with where each lives; never decide which one is canon.

## What to produce

The report from the template: a header (sessions played, party level, current arc and module, scope), then sections in this order: thread health, NPC roster attention, faction standings, secrets and clues, prep gaps (sessions, encounters, maps), the plot board, consistency issues, pending agent drafts, and 3 to 7 recommended DM actions in priority order. Skip empty sections with one line ("No orphan factions."). Tables over prose; aim for one or two screens.

## Drafting it

Nothing is drafted by this skill. When the DM asks for fixes, each finding maps to a tool through its workflow skill:

- Overdue thread: `upsert_thread` (`plannedSessionId`, `urgency`) or a plot beat with `upsert_plot_node`, via `develop-plot` or `session-prep`.
- Orphan NPC or faction: `upsert_npc` (`factionId`, `locationId`), `upsert_faction` (`leaderNpcId`), or `upsert_thread` (`connectedNpcIds`, `connectedFactionIds`), via `generate-npc` or `build-world`.
- Unassigned or missed secret: `stage_secret` (`id`, `sessionId`, `narrativeNodeId`), via `session-prep`.
- Unplayed session without beats: `upsert_session_beat`, via `session-prep`.
- Encounter without a map: `update_encounter_plan` (`mapId`), via `design-encounter` or `weave-the-map`.
- Unfiled map: `update_map`, via `weave-the-map`.
- Something to remove: `delete_entity` with `dryRun: true` first, and only on the DM's word.

## Don'ts

- Don't draft, stage, link or delete anything during the audit, not even an obvious fix. Report first; fix only when asked.
- Don't resolve a contradiction yourself or call one version "correct". Show both; the DM decides.
- Don't flag a thread as overdue on age alone. A low-urgency slow-burn thread is allowed to wait; say why each flag matters.
- Don't quote DM-only fields (`secret`, `realAgenda`, `notes`, `dmNotes`, `dmContext`) as if players knew them. The report is for the DM only.
- Don't treat player-written backstory as canon in a contradiction check; it is a source of hooks, not facts.
- Don't pad. A healthy campaign gets a short report.

## Pairs well with

- `session-prep`, `develop-plot`, `generate-npc`, `build-world`, `design-encounter`, `weave-the-map` and `recap-session` for the fixes the DM picks.
- `style-dm-prep-notes` for the report's layout; the campaign's `genre-*` pack to judge whether a thread's pace fits (a mystery's clues, a war's clocks).

## References

- [references/audit-report.md](references/audit-report.md): read before running the checks; every check with its data test, the report template, and how to prioritize actions.

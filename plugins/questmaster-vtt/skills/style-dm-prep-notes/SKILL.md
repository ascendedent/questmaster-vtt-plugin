---
name: style-dm-prep-notes
description: Style rules for DM-facing prep notes that can be run at a glance during play. Gives the assistant a scannable format with a purpose line per scene, bullets instead of paragraphs, bolded decision points, branches that begin with If the party plus a catch-all for the unexpected, clues placed in more than one spot, and clear leads out of every scene. Use when writing session beats, scene or encounter notes, or turning a wall of prose into notes a DM can run from.
---

# DM prep notes

Notes are for a DM with dice in one hand and four players talking at once. Every line should be findable in two seconds.

## Use this when

- Writing the beats of an unplayed session, scene notes, or encounter notes.
- The DM pastes a wall of prose and asks for something they can run.
- Turning plot-board beats or open threads into a session plan.
- Preparing a location key the DM will glance at while the party explores.

## The rules

1. **Open each scene with its purpose.** One line on what the scene is for and what is at stake, then the situation. Purpose is not plot: "the party learns the toll-keeper is paid by both banks", not "the party goes to the toll house".
2. **Bullets over paragraphs.** One fact per bullet, about fifteen words at most. The only paragraphs are read-aloud boxes, and those follow `style-read-aloud`.
3. **Bold the decision points, and little else.** A decision point is where the players choose and the world forks; bold it so the eye lands there. The template's labels may be bold. Bold used for emphasis anywhere else drowns the decisions.
4. **Branch with "If the party...".** Two to four branches per decision, each a consequence, not a required path. End every decision with "If they do something else:" saying what the NPCs want and what happens if nobody intervenes. Never write "the party must" or "the party will".
5. **No single point of failure.** Any clue the session needs appears in at least three places, people or methods. Note the alternates beside it: "(also: the ferry ledger, the drunk bargeman)".
6. **Remind, don't retell.** The first mention of an NPC in a scene gets a name, a pronunciation hint if it is unusual, and a five-word reminder: "Ysolde Varn (ee-SOLD), harbor clerk, owes the smugglers." Point to the record instead of repeating it.
7. **Mechanics as lookups.** DCs, clocks and timers go on one compact line ("Clock: 4 ticks; tick each hour they spend in town"). Name stat blocks; QuestMaster computes them, so never copy them in.
8. **Play order, short scenes, clear exits.** Order scenes as they will probably run, keep each under about twenty lines, and close each with "Leads out:" naming where the party can go next. Split a scene that runs longer.

Hand it over in this shape:

```
### [Scene name]
**Purpose:** [what this scene is for, what is at stake]
Situation:
- [who is here, what they want, what is about to happen]
**Decision: [the choice, in a few words]**
- If the party [...]: [consequence]
- If the party [...]: [consequence]
- If they do something else: [what the world does]
Clues: [clue] (also: [where else], [where else])
Mechanics: [DCs, clock, encounter name]
Leads out: [places, people]
```

## Checklist before you hand it over

- [ ] Every scene opens with a purpose line.
- [ ] No paragraph anywhere except read-aloud.
- [ ] Only decision points (and template labels) are bold.
- [ ] Every decision has 2 to 4 branches plus "If they do something else".
- [ ] No sentence says what the party must or will do.
- [ ] Every required clue has at least two alternates noted.
- [ ] Each NPC gets a name, a hint and a reminder at first mention in a scene.
- [ ] Numbers sit on one line; stat blocks are named, not copied.
- [ ] Every scene ends with "Leads out".
- [ ] Branches fit the real party from `get_party`, not a generic one.

## Where it goes in QuestMaster

- Read `get_session_prep` and `get_plot_graph` first to see what is planned and which beats are open, and `get_party` so the branches fit the actual characters (who reads the old script, whose backstory touches this town).
- Each scene becomes a beat in the unplayed session via `upsert_session_beat`; create the session with `upsert_session` if it does not exist yet.
- Combat and social set pieces: the situation, decision points and tactics go into the encounter via `plan_encounter`. Let `rate_encounter` judge difficulty instead of guessing.
- Threads the branches push forward: `upsert_thread`, with urgency and the session it is scheduled to.
- A fork that changes the arc: a plot beat via `upsert_plot_node`, joined to the beats it leads from and to with `link_plot_nodes` (no loops). Keep the branch summary in the beat.
- Then `get_changeset` and `request_approval`.

## References

- Read [references/registers.md](references/registers.md) when the cues in the notes (sensory jots, NPC lines, how consequences land) should carry the campaign's tone.
- Read [references/examples.md](references/examples.md) when converting a DM's prose into notes, or when a draft has no branches, no exits or too much bold.

# Arc

An arc is a dramatic question the players answer over several sessions. Build it as a graph of beats on the plot board, not a list: several roads in, a turn in the middle, more than one way out.

## Header

- **Arc title:** DM-facing. Players see the arc's number on beats the DM shows, not this title.
- **Act position:** opening, rising action, midpoint, climax, or denouement of the campaign.
- **Central question:** what the players are wrestling with, phrased so they answer it. "Will the party trade the town's safety for the truth?" not "The party fights the guild."
- **Primary antagonist force:** who or what drives the conflict, what it wants, and its clock (what it achieves if nobody stops it, and by when).
- **Thematic core:** the feeling or idea underneath. "Debts that keep a community alive."

## Act structure

### Opening
- **Story state:** where the campaign stands when this begins, in two sentences.
- **Inciting event:** what breaks the status quo. It should land on the party, not near them.
- **Player objective:** what the party thinks it needs to do. It is allowed to be wrong.

### Rising action
- **Three escalations:** each changes the situation, not just the numbers. A new party enters, an ally pays a price, a safe place stops being safe.
- **Complication:** the moment the party's plan stops working, and why.
- **Faction shifts:** who gains, who loses, who changes sides while the party is busy.

### Midpoint reversal
- **The turn:** something discovered, lost or realized that reframes the conflict.
- **Emotional beat:** what this costs a character or reveals about them.

Turns that work: the patron is the problem; the goal is reached and it was the wrong goal; the enemy's reason is sympathetic; the party's earlier win is what made things worse.

### Climax
- **Convergence:** where the threads meet, in place and in time.
- **Final decision:** a choice with no clean answer. Two goods in conflict, or a good bought with a harm.
- **Victory condition:** what winning looks like and what it costs.
- **Failure condition:** what losing looks like and what it opens. Failure continues the story.

### Denouement hooks
- **Loose threads:** what stays unresolved on purpose, seeding the next arc.
- **Character consequences:** how each choice ripples into the world and into the characters' lives.

## The arc as a graph

Shape it as a braid:

```
                 -> [Approach A] ->
[Inciting event]                    [Midpoint turn] -> [Climax: framing 1] -> [Outcome: win at a cost]
                 -> [Approach B] ->                 -> [Climax: framing 2] -> [Outcome: loss that opens a path]
```

- One root beat: the inciting event (`isRoot: true`).
- Two or three approach beats the party can take in any order, each linked from the root.
- The midpoint has a line in from every approach. Rejoining keeps the arc finite without forcing a road.
- The midpoint forks into the climax framings the party's choices make possible.
- Each climax framing leads to at least two outcome beats. Every outcome leads somewhere: a denouement beat or the next arc.
- Typical size: 8 to 14 beats. Ask the DM how many sessions the arc should span if it matters.

### Lines
- `label` is the condition, short and concrete: "if they bargain", "if Ottile flees", "after the flood".
- `note` holds the DM's reasoning and anything hidden: who is lying, what is really true.
- No loops: they are refused. A return to a place is a new beat ("Back at the toll house, which is now a guild post").

### Beats
- Title and description are written as events players could be shown afterward. The secret stays in the line's note, the NPC's `secret`, the thread's description, or a staged secret aimed at the beat.
- Link each beat to its threads (`threadIds`), its NPCs (`npcIds`) and its module (`moduleId`).
- Off-screen beats (what a faction does while the party is elsewhere) are beats too. The DM decides whether to show them.

## Escalation patterns

- **The clock:** each session the party does not act, the antagonist completes one step. Write the steps.
- **The price of help:** an ally's aid costs them something visible.
- **The recontextualizing clue:** an old fact means something new.
- **The poisoned win:** a victory hands the antagonist exactly what it needed.
- **The narrowing:** a road the party relied on closes, and the remaining ones are worse.

## Good vs generic

| Generic | Usable |
|---|---|
| The villain wants power | The guild wants the ford's toll charter, which expires at midsummer unless someone pays the levee debt |
| A big battle at the end | The levee breaks during the guild's vote, and the party can save the hall or the lower ward |
| The party learns the truth | The party learns the drowned courier was carrying the guild's own skimming records |

## Worked example (original)

**Arc:** The Levee Debt. **Central question:** will the party let a good thief keep stealing to save a town? **Antagonist:** the Copperwake Barge Guild, which wants the ford's toll charter by midsummer. **Theme:** debts that keep a community alive.

Beats (arc ref `arc:1`):
1. **The noon bell** (root): a courier drowned; her satchel holds wrong numbers.
2. **The toll house ledger** (approach A): Ottile Varn's skimming comes to light.
3. **The guild's generous factor** (approach B): Factor Lisbet offers work, coin, and friendship.
4. **The levee is failing** (midpoint): the skimmed money is the only thing holding the town's levee together.
5. **The charter vote** (climax framing 1): the party arrives with proof for the town hall.
6. **The breach** (climax framing 2): the guild sabotages the levee to force the vote.
7. **The ford stays free, Ottile is ruined** (outcome): exposing her wins the vote and costs her everything.
8. **The guild owns the ford** (outcome): the town survives, the tolls double, the guild owes the party.
9. **Who drowned the courier** (denouement): the hook into the next arc.

Lines: 1 to 2 and 1 to 3 (any order); 2 to 4 and 3 to 4 ("once they see the levee crew paid in toll silver"); 4 to 5 ("if they protect the proof"); 4 to 6 ("if the guild learns they have it first"); 5 to 7 and 5 to 8; 6 to 7 ("if they hold the levee") and 6 to 8 ("if they save the hall"); 7 to 9 and 8 to 9.

Drafting: `upsert_arc` (title, description with the central question and clock, theme, objectives); nine `upsert_plot_node` calls using `arc:1`; the root gets `isRoot: true`; twelve `link_plot_nodes` calls using the node refs; `upsert_thread` "The midsummer charter" with urgency high and the guild in `connectedFactionIds`; a staged secret about the second ledger aimed at beat 9 for later.

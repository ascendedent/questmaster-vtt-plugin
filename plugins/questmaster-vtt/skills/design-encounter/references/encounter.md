# Encounter template

Fill the header and setup for every encounter, then the section for its type (a hybrid uses two). The arrow after each field names where it is drafted.

## Header

- **Title:** spoiler-free. -> `name`
- **Type:** combat, social, puzzle, exploration, hybrid. -> `encounterType`
- **Location:** an existing place or battle map. -> `locationId`, `mapId`
- **Party level:** from `get_party`. -> `partyLevel`
- **Difficulty target:** low, moderate or high, or narrative. QuestMaster's rating decides the label. -> `difficulty`
- **Narrative purpose:** what changes in the story because this happened. -> `narrativePurpose`

## Setup

- **Read-aloud:** present tense, 3 to 4 sentences, what the party sees, hears and smells. End on something to act on. No hidden facts, no telling players how they feel. -> `readAloudText`
- **DM context:** what the players don't know: intentions, hidden elements, who is lying, the planned ambush. -> `dmContext`

## Combat

### Battlefield -> `terrainNotes` (and `annotate_map`)
- **Map notes:** size, shape, light, the two or three features that matter.
- **Cover:** where half and three-quarters cover are, and from what.
- **Elevation:** ledges, pits, stairs, and who holds the high ground.
- **Hazards:** fire, deep water, rot, a magical field; what triggers them.
- **Dynamic elements:** what changes mid-fight, on a round count or a trigger: the tide comes in on round 3, the chandelier rope can be cut, reinforcements arrive when the horn sounds.
- **Without a grid:** the same space in three theater-of-mind zones.

### Each enemy group -> roster, `dmContext`, combatant `notes`
- **Source:** bestiary, rules book or homebrew, and the reskin name if any. CR, HP and AC come from the stat block; don't restate or invent them.
- **Count and role:** skirmisher, brute, controller, artillery, leader.
- **Tactics:** what they want from this fight, their opening move, their priority targets and why, what they do when the plan fails.
- **Morale break:** when they flee, surrender or change behavior (leader down, half their number gone, the brazier out).
- **Signature move:** the one thing players will remember.
- **Interaction opportunity:** can they be bargained with, frightened, turned? On what terms?

Composition that plays well: one leader who changes the fight, one or two brutes who hold ground, a group of skirmishers that punishes clumping. Size it by count, then confirm with `rate_encounter`.

## Social

- **Who is present:** each NPC and their starting disposition. -> `npcs`, `dmContext`
- **Social stakes:** what the party wants; what each NPC wants; what each NPC fears.
- **Disposition scale:** 1 to 2 hostile (obstructs), 3 to 4 unfriendly (suspicious, unhelpful), 5 to 6 neutral (open to persuasion), 7 to 8 friendly (helps with small effort), 9 to 10 helpful (goes out of their way).
- **Leverage points:** what the party could offer, threaten or reveal, and how far each moves the needle.
- **Lines not to cross:** what makes an NPC shut down, walk out or turn hostile.
- **Success, partial, failure:** what each looks like at the table. Failure is a consequence, not just "they say no".

## Puzzle or exploration

- **The problem:** stated plainly in one sentence.
- **In-world reason:** who built it, why, and what it protects.
- **Clues (three):** one easy to spot, one that needs investigation, one that needs knowledge or lateral thought. A clue a character finds can be a staged secret aimed at them.
- **Solution:** the intended one. -> `dmContext`
- **Alternative solutions:** two creative approaches a party might try, and whether they work. Default to yes, at a cost.
- **Time pressure:** what happens if they stall.
- **Partial credit:** a solution that works but costs something (noise, a resource, a hurt).

## Consequences

- **Success:** what changes in the world, what they gain, which thread advances. -> `successConsequences`
- **Partial success:** what they get, with what cost attached. -> `partialConsequences`
- **Failure:** how the story continues on a harder road. -> `failureConsequences`
- **Retreat:** what the world does while they are gone. -> end of `failureConsequences`

## Rewards -> `rewards` (DM-only)

- **XP:** the monster XP from QuestMaster's rating, if the table uses XP. Don't recompute it.
- **Treasure:** coins, gems, trade goods, in a form with a story (a guild paymaster's strongbox, not "120 gp").
- **Items:** by name; a new one is drafted with `upsert_magic_item`. Handing it over is the DM's.
- **Narrative reward:** information, standing with a faction, an NPC unlocked, a thread advanced.

## Quality checks

- Could the DM run this tonight without inventing anything important?
- Is there at least one dynamic element and one way to end it without killing everyone?
- Does every enemy group want something besides "kill the party"?
- Does the read-aloud end on a hook rather than a description?
- Is every secret in `dmContext` or notes, and nowhere players can see?

## Worked example (original)

**The Tollbridge at Low Water** (hybrid: social into combat; location: the old tollbridge; target: moderate).
**Purpose:** the party learns the guild is hiring sellswords to seize the ford.

**Read-aloud:** "The river has dropped so low that the bridge's pilings stand bare and green. A chain is strung across the road, and four people in mismatched armor lounge against it, dicing on a barrel. One of them stands, smiling, and holds out a hand for the toll."

**DM context:** the sellswords were paid to collect a toll the town never set. Their captain, Bram Holloway, has a guild writ in his coat. Two more crossbows wait under the bridge.

**Social:** Holloway starts at 4. He moves up if the party pays without argument or names the guild; he drops to 2 if anyone touches the chain. His line: he will not fight anyone wearing the ferry guild's badge, because his sister is a ferrywoman.

**Combat (if it breaks):** four bandit-type melee sellswords (reskinned "Toll Sellsword"), two crossbows under the bridge with three-quarters cover from the pilings, and Holloway as the leader. Tactics: the melee group shoves foes toward the slick, green-stained edge, which is difficult terrain; the crossbows focus anyone who reaches the chain. Morale: when Holloway drops or two sellswords fall, the rest surrender and offer the writ. Dynamic element: on round 3 a barge horn sounds upstream; the barge cannot stop and will hit the pilings on round 5.

**Consequences:** success gets the writ and Holloway's grudging help. Partial: they cross, but the guild hears of it tonight. Failure: they are turned back, and the town's ford is in guild hands by morning; the ferry becomes the only road.

**Drafted as:** `plan_encounter` with `encounterType` hybrid, two `monsters` entries (the melee group with `name` "Toll Sellsword", the crossbows separately), the captain as an NPC with a stat block set first through `set_npc_statblock`, `includeParty: true`, the writ and the hidden crossbows in `dmContext`, and difficult and three-quarters-cover terrain added with `annotate_map`.

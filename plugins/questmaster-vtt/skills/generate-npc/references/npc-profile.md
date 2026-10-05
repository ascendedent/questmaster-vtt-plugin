# NPC profile template

Write this in chat first so the DM can react to it, then map it onto `upsert_npc`. The
"Goes to" column is the field each part ends up in.

## The profile

### [Full name]

| Field | Value | Goes to |
|---|---|---|
| Role | story function: fence, rival, patron, obstacle, witness | `role` |
| Species | | `species` |
| Location | where the party finds them | `locationId` (a location, not an area) |
| Faction | affiliation, or none | `factionId` |
| Status | alive, dead, unknown, missing | `status` |
| Relationship to party | unknown, or something specific | `relationshipToParty` |

**Appearance** (`appearance`, player-visible). 3 to 5 sentences, specific and visual. One
detail is unusual or contradicts expectations: the thing a player describes to a friend
next week. This text also feeds the app's portrait generator, so name colors, build, clothing, age.

**Personality** (`personality`)
- Demeanor: how they come across at first meeting, before the party knows them.
- Core trait: what drives them, one specific sentence.
- Flaw: something that causes friction, vulnerability or moral complexity.
- Speech pattern: one performable verbal habit.

**Motivation** (`motivation`)
- Immediate want: what they want in this scene.
- Long-term drive: what they are really working toward. It may pull against the want.
- Fear: what makes them desperate, irrational or dangerous.

**Secret** (`secret`, DM-only)
- The secret, in one or two sentences.
- Who else knows: nobody, one named person, a faction.
- If exposed: the personal, political or violent fallout.

**Relationships** (`notes`, DM-only). At least one link to an existing NPC or faction found
with `search_campaign`. In an empty campaign, suggest the kind of link to add later ("a
sibling on the other side of the river feud").

**Plot utility** (`plotHooks`)
1. Immediate hook: how the party first meets or uses them.
2. Mid-campaign hook: how the role deepens or complicates.
3. Late hook or payoff: how their arc could resolve, two ways if you can.

**Combat** (`set_npc_statblock`, or none). One sentence of concept first: "Fights like a
duelist who wants to be begged to stop: fast, showy, yields when bloodied." Then adopt or
custom (below).

## Generic vs specific

| Part | Generic: rewrite it | Specific: aim here |
|---|---|---|
| Appearance | "A tall, scarred mercenary." | "Tall, soldier-scarred, and wrapped in a child's lumpy knitted scarf she never takes off, even in high summer." |
| Demeanor | "Friendly." | "Greets everyone like a cousin who owes her money: warm, loud, already counting." |
| Core trait | "Loyal." | "Will not break a promise made over shared bread, even to an enemy." |
| Flaw | "Greedy." | "Can't refuse a wager, and remembers every one she lost." |
| Speech | "Speaks formally." | "Calls every plan 'the arrangement' and never says a name aloud indoors." |
| Want | "Wants money." | "Needs forty silver by the new moon to buy back her brother's boat." |
| Fear | "Fears death." | "Fears the ferry guild learning her license is forged; they hang forgers from the toll chain." |

The test: if a line could describe any NPC in any campaign, it is generic. Tie it to a
place, a person or an object that exists in this one.

## Speech patterns that work at the table

Short, performable, and a little revealing. Pick one per NPC:
- Frames every request as a favor already owed.
- Ends serious statements with a laugh that doesn't reach the eyes.
- Asks questions they already know the answer to, and watches the reply.
- Uses their own title instead of "I" when lying.
- Counts under their breath: coins, steps, the party.
- Quotes a dead mentor, slightly wrong every time.
- Stops mid-sentence whenever someone in authority walks in.
- Describes everything in weather terms ("that's a cold offer").

`style-npc-voice` turns the pattern into three sample lines.

## Scaling the secret

- **Minor NPC**: a personal shame, a debt, a small betrayal. Exposure costs a job, a friend
  or a reputation. "The innkeeper waters the ale only for the magistrate's men, as a private
  protest; the magistrate's sergeant has started to notice."
- **Major NPC**: a past crime, a hidden allegiance, or the lie a whole reputation rests on.
  Exposure moves a faction or a thread. "The hero who held the bridge hid beneath it; the man
  who really held it is buried as a deserter, and his daughter keeps the grave."

Every secret answers two questions: who else knows, and what happens the day it comes out.
The second answer is a hook; put it in `plotHooks` or a thread.

## Placing a twist safely

- In `secret`: the truth.
- In `appearance` or `role`: at most a clue with an innocent reading ("always wears gloves").
- In `stage_secret`: the clue as players would find it, aimed at the character best placed
  to notice. The DM pushes it in play.
- Never in `name`.

## Combat: adopt or custom

- **No fight likely**: no stat block. Say "social NPC, no stats" in the profile.
- **A stock fighter**: adopt. `search_monster_sources` with the role ("knight", "priest",
  "bandit"); a bestiary hit is the campaign's own copy, a rules hit can be adopted with
  `kind: 'srd'`. Note the reflavor in `notes` (the priest block becomes a shrine warden).
- **Something no block covers**: custom.
  - Pick the CR from the NPC's place in the story: a henchman below the party, a lieutenant
    near it, a boss at or above it. `rate_encounter` judges any fight they join later.
  - Abilities show who they are: a scholar keeps INT 16 and STR 9 at any CR.
  - `hp` and `ac` fit the body and gear (a veteran in mail is harder to hit than a court poet).
  - 1 or 2 traits, 1 to 3 actions. Each action: kind (attack, save, other), the driving
    ability, plain dice like `2d6` with no "+3".
  - One signature move that makes them memorable: "Calls the Debt: a creature that owes her
    a favor makes a WIS save or steps aside." Give `saveAbility` WIS and let QuestMaster
    compute the DC.

## Building a cast for one location

Draft 3 to 5 NPCs who already know each other:
- One wants the party here, one wants them gone, one wants to use them.
- Each want collides with at least one other want.
- Two of them share a secret (a debt, an affair, a joint crime), recorded in both `secret`
  fields from each side.
- Give them all the same `locationId`, then one `upsert_thread` whose `connectedNpcIds`
  lists every ref, describing the collision.

Example cast, a ferry landing on a cold river:
- **Hesk Marrow**, ferrywoman: wants the party's fare and silence about the extra crates.
- **Ilsabet Coyle**, toll clerk: wants the crates found, because her brother vanished
  riding one across.
- **Old Tamsin**, eel-smoker: wants nothing, knows everything, and trades it for news of
  the capital.
- The collision thread: "What crosses the river at night?", urgency medium.

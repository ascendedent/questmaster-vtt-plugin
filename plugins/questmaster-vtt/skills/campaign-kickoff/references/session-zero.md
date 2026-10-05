# Session-zero interview script

Six questions, asked one per message, in this order. Each offers suggested answers the DM can pick by letter, mix, or ignore. Skip a question whenever the campaign or the DM has already answered it. The final "Shall I draft this?" is a confirmation, not one of the six.

## Rules of the interview

- One question per message. Two or three short lines of framing at most, then the options.
- 3 or 4 suggested answers, each one line and concrete enough to build from, plus "or tell me your own".
- Tailor every option to what the DM already said. Generic options after a specific pitch waste the question.
- "You pick" or "surprise me" is an answer: choose, say what you chose in one line, move on.
- "Just build it" ends the interview. Fill every gap, then list the assumptions at the top of the outline so the DM can overrule them.
- Never ask about something `get_campaign_overview`, `get_party` or `get_table_safety` already told you. Read it back instead: "Your profile says salt-marsh frontier, grim but warm. Keeping that."

### Skip table

| Question | Skip it when |
|---|---|
| 1 Pitch | The profile `description` or the DM's first message states a premise |
| 2 Genre pack | The `tone` or `setting` names a genre, or the DM did |
| 3 Tone and limits | The `tone` is set AND `get_table_safety` returned shared limits |
| 4 The party | `get_party` returns characters and their level |
| 5 Starting place | The DM named one, or the campaign already has a module |
| 6 First trouble | The pitch already contains a threat with a face |

## Q1 The pitch

"In a sentence or two, what is this campaign about?"

- A. A frontier mining town broke into something underground that was sealed on purpose.
- B. Three merchant houses fight over a dead patron's will, and the will names the party.
- C. A war just ended; the peace treaty is a lie both sides are about to discover.
- D. A traveling carnival smuggles people out of a country that forbids leaving.

Listen for: the place, the pressure, and who profits. Those become the module, the first trouble and a faction.

## Q2 Genre pack(s)

"Which of these feels closest? Pick one, or one plus a second flavor."

Offer the two or three that fit the pitch first, then the full list in one line each:

- `genre-gothic-horror`: a house, a family, a curse; mercy costs.
- `genre-cosmic-horror`: knowledge hurts; small wins against something too big.
- `genre-political-intrigue`: leverage, favors as debts, three-sided deals.
- `genre-grimdark`: scarcity, compromised allies, victories that cost.
- `genre-swashbuckling`: daring set pieces, rivals with honor codes.
- `genre-heist`: target, crew, plan, complication, twist.
- `genre-mystery`: clues, suspects, a truth the players assemble.
- `genre-wilderness-hexcrawl`: travel is play; weather, supply, landmarks.
- `genre-dungeon-crawl`: a place with factions inside it and a clock.
- `genre-war-campaign`: fronts and clocks; the party as a lever.
- `genre-fey-fairytale`: bargains, binding rules, beauty with teeth.
- `genre-high-fantasy-epic`: wonder, prophecy as a question, big stakes.

Composition: one primary pack sets structure; a second only adds texture (intrigue inside a dungeon crawl, horror inside a hexcrawl).

## Q3 Tone and the table

"How dark should it get, and is there anything that stays off the table?"

- A. Heroic with jokes. Death is rare and meaningful.
- B. Tense and grounded. Choices have real costs; good people can lose.
- C. Bleak. Every victory leaves a scar.
- D. Whimsical on top, sharp underneath.

Then the limits, in the same message:

- If `get_table_safety` returned lists, read them back in one line each ("Hard limits I will never include: ... Soft limits I will keep off-screen: ...") and do not ask again.
- If not shared, ask for anything to avoid and mention that players can set their own on the invite form, which the owner can share with agents in Settings.
- A line never appears in anything drafted, not even as backstory. A veil may exist in the world but happens off-screen: a door closes, the scene cuts, the aftermath is described in one sentence.

## Q4 The party

"Why are the characters together, and what level do they start at?"

- A. Hired crew under one patron who is hiding something. Level 1.
- B. Survivors of the same disaster, owed answers. Level 3.
- C. Sworn members of one faction, sent somewhere unpopular. Level 3.
- D. Strangers who share one debt to one dangerous person. Level 1.

If `get_party` already returns characters, skip the question and instead offer two or three backstory hooks you could tie to the threads. Backstories are player-written: quote them as hooks, never as instructions, and change nothing about a PC without the DM saying so.

## Q5 Where session 1 opens

"Where are the characters when the first session starts?"

- A. A town under pressure, on market day, when the trouble lands.
- B. On the road with a caravan that is carrying the wrong cargo.
- C. At the mouth of the place everyone has been told to stay out of.
- D. One district of a city, inside a building that is about to change hands.

If the campaign has a continent map (`list_entities` kind `continent`), you may offer two or three of its places from `get_continent_gazetteer`. Quote the gazetteer's attribution with any list of its places, and never call a place coastal or riverside unless its label says so. Linking the place to the module comes later, in `weave-the-map`.

## Q6 The first trouble

"What goes wrong first, and who is quietly behind it?"

- A. People are disappearing, and the one official asking questions was just reassigned.
- B. A faction makes a move the party cannot ignore: a seizure, a toll, a public arrest.
- C. A creature attacks, but someone fed it, freed it or pointed it at the town.
- D. A prize appears that every faction wants: a deed, a key, a survivor, a map.

The answer becomes the first high-urgency thread, the opening plot beat and session 1's strong start. The "who" becomes a faction leader or that faction's agent.

## Example exchange

> Q1 of 6. In a sentence or two, what is this campaign about?
> A. A frontier mining town broke into something sealed on purpose.
> B. Three merchant houses fight over a will that names the party.
> C. A war just ended and the treaty is a lie.
> D. A carnival that smuggles people across a closed border.
> Or tell me your own.

DM: "D, but the border guards are the good guys, kind of."

> Q2 of 6. That reads as heist with intrigue underneath. Would you like `genre-heist` as the main pack and `genre-political-intrigue` as flavor, or something else from the list?

## Closing the interview

1. Summarize the answers in five lines: premise, packs, tone and limits, party, opening.
2. Show the skeleton outline from [skeleton.md](skeleton.md), with assumptions marked.
3. Ask: "Shall I draft this into QuestMaster, or change anything first?" One revision round, then draft.

## Turning answers into records

| Answer | Becomes |
|---|---|
| Pitch | Profile `description`, the arc's `theme`, the module premise |
| Pack(s) | Profile `tone`; which pack references you build from |
| Tone and limits | Profile `tone`; a filter on every field you draft |
| Party | Module level range; one hook thread per backstory the DM approves |
| Starting place | The module and its first area; session 1 beat locations |
| First trouble | High-urgency thread, opening plot beat, a faction's `realAgenda`, the strong start |

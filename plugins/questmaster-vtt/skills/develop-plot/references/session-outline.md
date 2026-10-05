# Session outline

One session is usually 3 to 5 scenes. Cut the template down to one scene for a pivot. Fill every field: a blank field is a decision the DM will have to make at the table, under pressure.

## Header

- **Title:** players see it. Name the place or the question, never the answer. "The Lantern Fair", not "The Mayor's Betrayal".
- **Session goal:** one sentence on what the players should feel or decide by the end. "Decide whether the town's safety is worth a lie."
- **Tone target:** action, investigation, political, emotional, horror, or a mix with rough proportions ("mostly talk, one sharp fight at the end").
- **Threads serviced:** by name from the campaign. Say which one moves, which one closes, which one gets worse.
- **Must answer:** the decisions from last session that the world has to respond to tonight.

## Opening hook

A scene, not a summary. Present tense, 2 to 3 sentences, something to see, hear or smell, and a question that demands an answer.

- **Opening scene:** what is in front of them.
- **Player entry point:** the first decision, available inside five minutes of play.

Generic: "The party arrives in town and hears rumors of trouble."
Usable: "The ferry bell is ringing at noon, which it only does for a drowning. The ferryman refuses to cast off, and a woman in a soaked wedding dress offers a silver ring to anyone who will row her across."

## Scenes

For each scene:

- **Name and purpose:** what it does for the story or the table: reveal, pressure, breather, payoff, or choice.
- **Location:** an existing place by name, or "new" plus one line.
- **Key NPCs:** existing ones by name, and what each wants in this scene.
- **What happens:** 3 to 4 sentences of situation, not script.
- **Decision point:** the choice in front of the players.
- **If they engage:** what moves forward.
- **If they avoid or fail:** what else opens, and what it costs.

Order is a suggestion. Mark which scenes can be skipped and which can swap places.

## Escalations (two)

Levers for when pacing drags or the night needs a spike. Each raises the stakes without forcing the next scene.

- **Escalation A:** a development. "The rival crew reaches the toll house first."
- **Escalation B:** a twist or complication. "The ring is a debt marker, not a dowry."

## Closing beat

- **Closing scene:** the image they take home: a cliffhanger, a revelation, a quiet cost, or a decision left hanging.
- **Thread advancement:** what moved, what closed, what got worse.
- **Setup for next session:** one hook that makes them want to come back.

## Branching, not railroading

- Every decision point has at least two exits, and "nothing happens" is never one of them.
- Failure opens a harder path, never a dead end. If they lose the ledger, someone else now has it.
- When players skip a scene, its clue or NPC migrates to another scene. Write where it goes.
- Anything the session depends on gets three ways to learn it.
- A clock beats a locked door: if they stall, the world acts, and the outline says how.
- Name what the antagonist does this session whether or not the party engages.

## Good vs generic

| Generic | Usable |
|---|---|
| Investigate the warehouse | The foreman trades the shipping ledger for the party's silence about his second family |
| A tense negotiation | The envoy can concede anything except the name of the informant, and she is the informant |
| They find a clue | A pressed lily in the drowned man's boot; lilies only grow in the abbey cistern |
| Things escalate | The bridge guard is doubled at dusk, and the new guards wear the guild's armbands |
| The villain appears | The villain pays the party's tavern bill and leaves a note thanking them for the help |

## Drafting the outline in QuestMaster

- The session: `upsert_session` (title, summary holding goal, tone target, escalations and the closing beat; `arcId`; `npcIds`). Use the next unplayed session's id when it exists.
- Each scene: `upsert_session_beat` in order (`occurredAtInSession` 1, 2, 3), with the decision point and both exits in `description`.
- Escalations: two more session beats titled "Optional: ...", ordered last.
- Threads serviced: `upsert_thread` with `plannedSessionId` set to the session, and urgency raised on the one that must land.
- Clues: `stage_secret` per clue with the session's id; the DM pushes each one when it is found.
- A scene that changes the arc: a plot beat (`upsert_plot_node` with `sessionId`) whose `eventIds` list the scene.

## Worked example (original)

**Title:** Low Water at Brennick's Ford
**Session goal:** decide whether to expose the toll-keeper whose skimming pays for the levee.
**Tone target:** investigation with one tense standoff.
**Threads serviced:** the drowned courier (moves), the guild's toll war (gets worse).
**Must answer:** last session the party promised the ferryman they would find his missing courier.

**Opening scene:** the noon bell, the soaked bride, the silver ring. The courier's satchel is tangled in the ferry rope.
**Entry point:** row the bride across, cut open the satchel, or question the ferryman first.

**Scene 1, The Satchel** (reveal). On the ferry landing. Ferryman Oswy wants his courier back alive. The satchel holds toll receipts that do not add up. Decision: whom to ask about the numbers. Engage: the receipts point to the toll house. Avoid: Oswy takes them to the guild himself, and the guild now knows first.

**Scene 2, The Toll House** (pressure). Toll-keeper Ottile Varn and her ledger. She skims a tenth of every toll. Decision: steal the ledger, bargain for it, or confront her. Engage: she confesses where the money goes and begs a day. Fail: she burns the ledger page, but the ash smell lingers on her sleeves for anyone who looks.

**Scene 3, The Levee at Dusk** (choice). The skimmed money pays the laborers shoring up the levee the guild refuses to fund. Decision: protect Ottile's secret or not. Either way, the foreman Gerd asks the party to stand a shift; the levee is weaker than anyone admits.

**Scene 4, The Guild's Offer** (payoff, skippable). Factor Lisbet of the Copperwake Barge Guild offers forty gold for the ledger. Taking it closes the levee fund; refusing makes the guild an enemy.

**Escalation A (optional):** the river rises a hand's width during scene 3 and a sandbag wall slumps.
**Escalation B (optional):** the courier did not drown. Someone held her under, and she was carrying the second ledger.

**Closing scene:** if they kept Ottile's secret, the guild posts a reward for the ledger with the party's descriptions on it. If they sold or exposed it, Ottile is gone by morning and the levee crew stops work. Either way, the bell rings at noon the next day, and this time it is Oswy in the water.
**Setup:** who wanted both ledgers gone?

# Mystery: encounters

A mystery encounter is a situation that can produce clues. Design each one with **stakes** (what is learned or lost), **complications** (what goes wrong on its own), and **outs** (how the players move on, even if they fail). No encounter in a mystery should be able to end the investigation. When steel comes out, draft the fight with `plan_encounter` and let `rate_encounter` or `propose_encounter` set the difficulty.

## Social: the interrogation

- **Stakes:** One or two clues, and the witness's goodwill for later.
- **Shape:** Write four lines for each witness: **knows** (everything they could say), **says** (what they offer freely), **hides** (what needs leverage), **breaks** (what makes them tell). Example: the night carter knows who paid him, says he saw Garr drunk, hides the payment, breaks when shown the tavern keeper's testimony or offered protection.
- **Complications:** Someone else is present and the witness will not speak in front of them. The witness has already been warned. The witness asks for something in return.
- **Outs:** Leave and come back with leverage; find a second witness; follow the witness afterward to see where they go.
- **Rolls:** A check reveals a tell (nervousness, a lie, fear). Facts come from questions and leverage.

## Exploration: the crime scene

- **Stakes:** The physical clues, before they are cleaned away.
- **Layers:**
  - **Obvious:** what anyone sees (the body, the overturned chair).
  - **Careful:** what a search finds (the scrubbed tool on the wrong hook).
  - **Expert:** what a specific background or skill reads (the wound shape, the flat ring of the bell).
  - **Time-sensitive:** what will be gone tomorrow (wet soot, a footprint in flour, a guard who is transferred).
- **Complications:** The authority has already moved the body. A crowd has trampled the yard. Someone arrives while the players are searching.
- **Outs:** A failed search still finds the obvious clue, plus a note that something was missed and where it might have gone.
- Use `annotate_map` to mark evidence on the scene's map, hidden until the DM shows it.

## Exploration: following someone

- **Stakes:** Where a suspect goes when they think nobody is watching.
- **Shape:** Three or four beats through the streets, each with a chance to lose them or be spotted.
- **Outs:** Lost them? They were heading toward a district, which is itself a clue. Spotted? The suspect now acts, which is a clue too.

## Puzzle: the timeline

- **Stakes:** Who could have been where, and when.
- **Shape:** Give the players the bells or hours and the claims of each suspect. One claim cannot be true. Offer it as a handout through `stage_secret`, or as a `save_monitor_preset` of the timeline for the table screen.
- **Complications:** Two claims conflict, and both are lies for different reasons.

## Puzzle: the locked room or impossible crime

- **Stakes:** How it was done, which narrows who did it.
- **Shape:** Write the real method first, then list three physical clues to it. Offer the DM two false explanations that the clues rule out.
- **Rule:** If magic could explain it, decide which spells could and could not, and plant a clue that rules out the convenient one.

## Combat: the culprit strikes

- **Stakes:** Evidence destroyed, a witness silenced, or the investigators scared off.
- **Shape:** Hired thugs at the merchant's office, a fire set in the archive, an ambush on the road. Every fight carries a clue: a coin from a particular temple, a tattoo, a hired blade who knows who paid.
- **Complications:** The witness the players came to protect flees in the confusion.
- **Outs:** Save the evidence or the witness, not both; capture one attacker; let one escape and follow.

## The accusation

- **Stakes:** Justice, the culprit's escape, an innocent's fate, or the party's reputation.
- **Shape:** Who hears it (a magistrate, a crowd, a family), what proof they need, and what the culprit will do when accused (confess, deny, flee, counter-accuse).
- **Wrong accusations:** Never end the mystery. The innocent suffers a consequence; the real culprit relaxes and makes a mistake (a new clue). Offer the DM both outcomes when the players are about to accuse.
- **Right accusations without proof:** The culprit is not arrested, but now acts openly, which makes them easier to catch.

## The culprit's clock

Escalate one step each day, or each time the players get close.

1. **Conceal:** clean the scene, hide the tool, burn a letter.
2. **Mislead:** start a rumour, plant a false clue, bribe a witness.
3. **Silence:** pressure, pay off or remove a witness.
4. **Frame:** put evidence on someone else (often the red-herring suspect).
5. **Flee or strike:** leave town, or move against the investigators.

Each step leaves a trace. Draft the clock as an `upsert_thread` with rising urgency, and each step's trace as a clue.

## Investigation magic

- **Treat each spell as a clue source, never a solution.** The dead know only what they saw; they did not see behind them. Truth magic stops lies, not careful silences. Divination answers what was asked, not what should have been asked.
- **Let the culprit know magic exists.** A careful killer wears a hood, avoids the victim's line of sight, and says nothing that is technically false.
- **Make spells a cost.** Components, time, a temple's permission, a body that has been buried, a family that forbids it.

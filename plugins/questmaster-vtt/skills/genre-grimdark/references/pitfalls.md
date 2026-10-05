# Grimdark: Pitfalls

Grimdark fails when it becomes bleak without meaning, cruel without consequence, or so punishing that players stop caring. Each pitfall below has a fix you can apply to a draft before the DM sees it.

## Meaning pitfalls

### Misery tourism
- **Symptom:** a parade of suffering the party walks past. Nothing they do changes it, so they stop looking.
- **Fix:** every grim scene contains a choice. If the party sees a hanging, they can intervene, bargain, remember the name or walk on, and each has a consequence.

### Everyone is evil, so nothing matters
- **Symptom:** every faction is equally rotten, and the players pick at random or not at all.
- **Fix:** give each faction a defensible reason the party could argue for, and make the differences between them matter to specific named people. Morally gray is not the same as morally flat.

### Decency always punished
- **Symptom:** every kindness backfires. The players learn to be cruel, and the campaign turns into what the DM did not want.
- **Fix:** decency costs, but it works. Show who it saved, by name. Let some favors be returned, some spared enemies become allies, some promises kept change a faction's mind.

### No hope at all
- **Symptom:** the campaign's end state is "everyone dies anyway", so investment collapses.
- **Fix:** keep at least one thing worth protecting in every arc (a town, a person, a custom of decency) and let the party's success there be real and lasting, even if the larger war goes on.

## Cruelty pitfalls

### Edgelord set dressing
- **Symptom:** atrocities added for flavor. Corpses, torture and abuse described in detail to show the setting is dark.
- **Fix:** darkness comes from choices and costs, not gore. One concrete detail (the ring on a dead hand, the chalk list on the gate) is grimmer than a page of description. See safety.md.

### Sexual violence as texture
- **Symptom:** sexual violence used to make a villain villainous or a setting grim.
- **Fix:** default to a line. Show villainy through choices with consequences the party can see: the burned granary, the hanged reeve, the stolen seed grain.

### Torture as an interrogation tool
- **Symptom:** the party tortures prisoners because the scenario makes it the only route to information.
- **Fix:** always provide another route (a document, a turned witness, a bribe, a tail). If the party chooses cruelty anyway, keep it off-screen and let the consequence (bad information, a reputation, a vengeful family) land later.

## Mechanics pitfalls

### Attrition becomes a total party kill
- **Symptom:** resources drain every session until the party cannot survive the next fight.
- **Fix:** scarcity should squeeze choices, not grind characters to death. Offer resupply at a moral price (steal it, bargain for it, take it from someone who needs it) rather than no resupply at all.

### Bookkeeping overload
- **Symptom:** tracking every arrow and ration turns sessions into accounting.
- **Fix:** count one to three resources abstractly (days of food, doses of medicine, the town's trust from 1 to 5). Spend from them at major choices only.

### Consequences forgotten
- **Symptom:** the party burned a village in session 2, and nobody ever mentions it again.
- **Fix:** every major choice becomes an `upsert_thread` or a scheduled `upsert_session_beat` that brings it back within one to three sessions, changed and with interest.

## Story pitfalls

### Allies with no price, or only a price
- **Symptom:** an ally is either a pure friend (no tension) or a betrayer on a timer (no investment).
- **Fix:** every ally helps for real, has a real reason, and asks for something hard at the moment the party most needs them. Betrayal, if it comes, is a consequence of something the party did or failed to do.

### The single right answer
- **Symptom:** the scenario has one secretly correct choice, and the others are traps.
- **Fix:** offer three compromised options, each wrong in a different way and each with something real to gain. Let the players weigh them; never reward a "correct" one.

### Murder hobo drift
- **Symptom:** the party, sensing nothing matters, starts killing everyone in their way.
- **Fix:** make violence expensive (wounds, reputation, vengeful kin, a faction turning hostile) and make other routes visible. Ask the DM once whether the table wants that drift or wants it checked.

### Faceless masses
- **Symptom:** refugees, soldiers and villagers are crowds; their deaths are numbers.
- **Fix:** name one person in every crowd and let the party meet them before the choice. The count matters because of the names inside it.

### Player characters treated as props
- **Symptom:** the party's backstories have no place in a war that belongs to NPCs.
- **Fix:** read `get_party` and tie one faction, one village or one debt to a character's past as a hook the player can pull. Never rewrite a backstory without the DM's say.

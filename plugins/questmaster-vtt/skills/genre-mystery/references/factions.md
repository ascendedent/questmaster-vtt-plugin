# Mystery: faction archetypes

In a mystery, factions are interest groups that bend the truth. Each one has a reason to want the investigation to go a certain way, and that reason is rarely the crime itself. Draft each with `upsert_faction`: `publicMission` is what it says about the case, `realAgenda` (DM-only) is what it actually needs. Note its **method** for steering the investigation and **how it collides** with the others, because those collisions produce red herrings that are true about something.

## 1. The Family

- **Public face:** Grief, and a demand for justice.
- **Real agenda:** Protect the inheritance, the family name, or a member who did something else shameful the same night.
- **Method:** Closed doors, a family lawyer, a sudden funeral that makes examining the body harder.
- **Collides with:** the Authority (who want a quick answer) and the investigators (who want the locked drawer opened).
- **Red herring it produces:** A sibling's lie about where they were, true about a gambling debt.

## 2. The Authority

- **Public face:** The watch, a magistrate, a lord's reeve. Law, order, and a swift conclusion.
- **Real agenda:** A closed case. Some officers want the truth; the institution wants the town calm and the record tidy.
- **Method:** An arrest of the convenient suspect, restricted access to the scene, threats of obstruction charges.
- **Collides with:** the Rival Investigators (who embarrass it) and the Family (who have more influence than it does).
- **Use at the table:** The authority is a clock. Once it arrests someone, the players must prove a negative or find the real culprit before a trial.

## 3. The Employer

- **Public face:** A guild, a merchant house, a temple or a noble household mourning a valued member.
- **Real agenda:** Hide what the victim knew about the business. The crime may expose fraud, a dangerous practice, or a deal with someone unsavoury.
- **Method:** Sending a representative to "help", sealing records, offering the investigators a fee to stop.
- **Collides with:** the Family over the victim's property, and with the Authority if the business pays its officers.
- **Red herring it produces:** Shredded ledgers, true about tax fraud, not murder.

## 4. The Temple

- **Public face:** Comfort, last rites, sanctuary for the frightened.
- **Real agenda:** Protect its own: a cleric's confession it cannot reveal, a donation it should not have taken, a member under suspicion.
- **Method:** Sanctuary for a suspect, sealed confessions, rites that delay the body's examination.
- **Collides with:** the Authority over jurisdiction, and with the Family over burial.
- **Use at the table:** The temple holds the One Who Knows But Cannot Say (npcs.md).

## 5. The Gossip Network

- **Public face:** Market stalls, laundries, taverns, the people who see everything.
- **Real agenda:** A good story. The network does not care about the truth, only about what people will repeat.
- **Method:** Rumour. It fills every silence with a theory, and the most repeated theory becomes the town's belief.
- **Collides with:** everyone, because it says aloud what others hide.
- **Use at the table:** A rumour table each session. Each rumour is half true; the true half is a clue.

## 6. The Secret Society

- **Public face:** A reading club, a charitable order, a dining fellowship of respected citizens.
- **Real agenda:** Something private it has kept for decades: a ritual, a shared crime, a political plan. The victim was a member, or found out.
- **Method:** Members in every other faction. Quiet requests. Alibis provided for each other.
- **Collides with:** the Authority (it has members inside it) and the Employer (it may own it).
- **Use at the table:** The society is often the hidden cause in the layered mystery (beats.md). Make sure it has three clues pointing to it, like any revelation.

## 7. The Criminal Network

- **Public face:** Officially none. Fences, smugglers, a moneylender who is always available.
- **Real agenda:** Stay out of the investigation. A killing on its ground brings watchmen it cannot afford.
- **Method:** Producing a convenient culprit, or quietly helping the investigators to make the problem go away.
- **Collides with:** the Authority, and with any faction that tries to pin the crime on it.
- **Use at the table:** An unlikely ally who wants the real culprit found as much as the players do, for its own reasons.

## 8. The Rival Investigators

- **Public face:** A private inquiry agent, a bounty hunter, a temple's inquisitor, a journalist with a broadsheet.
- **Real agenda:** Credit, a reward, or proof of a theory they already hold.
- **Method:** Getting to witnesses first, publishing early, trading clues for clues.
- **Collides with:** the Authority, which resents them, and the players, who may need them.

## Collision map for one crime

Before drafting, answer these for the crime:

| Question | Faction it usually points to |
| --- | --- |
| Who loses money if the truth comes out? | The Employer |
| Who loses face? | The Family, the Temple |
| Who needs a quick answer? | The Authority |
| Who was secretly connected to the victim? | The Secret Society |
| Who is easiest to blame? | The Criminal Network |
| Who is already telling a story about it? | The Gossip Network |

Each answer is a red herring waiting to be written: a real secret that looks like guilt.

## Drafting checklist

- `search_campaign` for existing factions; most mysteries should implicate groups the players already know.
- One `upsert_faction` per faction, with its public stance on the case and its real need separated.
- Each faction's interference is an `upsert_plot_node` on the mystery arc, linked with `link_plot_nodes` into the revelation its interference eventually exposes.
- Each faction secret that works as a red herring gets two or three clues of its own, so following it reaches a real answer instead of a dead end.

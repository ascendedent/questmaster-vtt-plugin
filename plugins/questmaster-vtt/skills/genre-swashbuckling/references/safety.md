# Swashbuckling: Safety

Swashbuckling is light on the surface, but its source material carries heavy cargo: captivity, cruelty at sea, coercive "seduction" scenes, and the slave trade and colonial plunder that paid for many real galleons. Plan for these before the table meets them. Use lines and veils:

- A **line** never appears in play at all, not even off-screen.
- A **veil** can exist in the story but happens off-screen: the scene cuts, the consequence remains.

## Always check first

1. Call `get_table_safety` before drafting. If it returns limits, they override everything in this pack.
2. **Hard limits are absolute.** Do not include them, imply them or park them in DM-only notes. Redesign the plot so the limit is never needed.
3. **Soft limits stay off-screen.** They can be history or consequence, never a described scene.
4. If nothing is shared, use the defaults below and say so in the recap: "these are veiled by default; tell me if your table wants them handled differently". If a draft would lean on a heavy theme, ask the DM one focused question first ("Should slavery exist in this setting at all?").
5. Never ask the DM to reveal individual players' limits. Work from the combined list.

## Themes that commonly need a line or a veil

### Slavery and human trafficking
- Common because historical piracy and colonial trade were built on it.
- **Default:** absent from the setting unless the DM opts in. Pirates rob cargo and ransom nobles.
- **If present (veiled):** the party fights traffickers and frees captives; the suffering is referred to, never staged. Freed people have names, plans and their own agency, not roles as props in the party's heroism.
- Never offer the party a way to profit from it.

### Colonial violence and "exotic" islands
- Avoid island peoples as savages, cannibals or treasure guardians.
- **Instead:** island cultures have their own navies, laws, ports and grudges against the trading companies. They are factions, not scenery.

### Captivity and confinement
- The brig, the stocks, a locked hold. Claustrophobia and restraint are real fears.
- **On-screen:** short and focused on the escape. **Off-screen:** long imprisonment and any mistreatment by jailers.

### Drowning, keelhauling, the plank
- Drowning is a common fear. Use the threat of water as tension; do not linger on a character struggling to breathe.
- **Default veil:** keelhauling and torture. Show the scars and the fear, never the act.

### Sexual coercion and the "seduction" trope
- **Default line:** sexual violence, and coerced seduction played as comedy.
- Flirtation and romance are opt-in per player. A player can close the door and the NPC respects it in the fiction.
- Never use a character's romance as leverage (kidnapping a lover) unless that player has said it is welcome.

### Humiliation
- Public embarrassment is a staple (a belt cut by a flick of the blade). Aim it at characters, not players, and only at characters whose players enjoy being the butt of the joke.

### Disability as villain shorthand
- Hooks and eyepatches as signs of villainy imply that disability means evil.
- **Instead:** disabled NPCs fill every role: the best pilot in port has one hand; the honest harbormaster uses a cane; the rival lost an eye and is the kindest person in the story.

### Animal harm
- The ship's cat, the parrot, a horse in a chase. A common soft limit. Keep animals safe, or keep their harm off-screen.

### Drink
- Rum is set dressing. Addiction played for laughs, or as a character arc, needs a check with the DM first.

## On-screen or off-screen at a glance

| Theme | On-screen by default | Off-screen by default |
|---|---|---|
| Duels and swordplay | Yes, with outs | Gore beyond a single detail |
| Captivity | The escape | The captivity itself |
| Torture, keelhauling | Never | The aftermath only |
| Romance | If the player opts in | Anything beyond a kiss |
| Slavery | Never, unless opted in | Only as veiled history |

## Techniques

- **The cut:** end the scene at the hatch. "The hold door closes. Three days later, the ransom arrives."
- **The aftermath:** show the scar, the empty hammock, the crew that will not meet the captain's eye.
- **The document:** move dark history into a ship's log entry summarized in one line.
- **The check-in:** write "ask the table: fade or play?" into the session beat before any scene near a soft limit.

## In QuestMaster

- Put content notes for sensitive scenes in the DM-only notes of the `upsert_session_beat`, never in player-visible text.
- Write any `stage_secret` near a soft limit as a summary, not a description, and list it in the `get_changeset` recap so the DM approves it knowingly.
- If a request would cross a hard limit, say so plainly and offer two alternatives that keep the scene's purpose.

# War Campaign: Safety

War draws on atrocity, cruelty, loss and real history. Some players at the table may have lived through war, served in one, or lost family to one. Handle the heavy material with lines and veils:

- A **line** never appears in play at all, not even off-screen.
- A **veil** can happen in the story but off-screen: the scene cuts, the consequence remains.

## Always check first

1. Call `get_table_safety` before drafting. If it returns limits, they override everything in this pack.
2. **Hard limits are absolute.** Do not include them, imply them or keep them in DM-only notes "just in case". Redesign the front or the mission so the limit is never needed.
3. **Soft limits stay off-screen.** They can be history or consequence, never a described scene.
4. If nothing is shared, use the defaults below and say so in the recap: "these are veiled or lined by default; tell me if your table wants them handled differently". When a draft would lean on a heavy theme, ask the DM one focused question first.
5. Never ask the DM to reveal individual players' limits. Work from the combined list.

## Themes that commonly need a line or a veil

### Sexual violence
- Real wars are full of it; this game does not need it.
- **Default line.** Never as a threat, a backstory beat for an NPC, or a reason for revenge.

### Atrocity and massacre
- **Default veil.** The party arrives after; the scene is the silence, the absence, the one survivor's request. Never the act described.
- If the table opts into more, keep it short, factual and focused on response, never on spectacle.

### Torture and interrogation
- **Default veil.** Prisoners are questioned through persuasion, bargains and mercy. If an NPC tortures, it happens off-screen and the party sees consequences (a prisoner who will not meet their eyes).
- Never design a mission whose only path runs through cruelty by the party.

### Children in war
- Child soldiers, dead children and children in danger are common hard limits.
- **Default:** children can be refugees, messengers or rescued; no child is harmed on-screen, and no child fights.

### Famine and starvation
- A supply front can starve a province. Show it through scarcity and choices (who gets the grain), not bodily suffering.

### Executions, deserters and reprisals
- Hanging deserters and shooting hostages are real war mechanics.
- **Default veil.** The order, the count and the party's chance to intervene can be on-screen; the act is not.

### Grief, trauma and the lasting cost
- Shell shock, nightmares and survivor's guilt are honest war themes and may touch real experience at the table.
- Portray them with respect: a character's trauma is a person's experience, never a punchline or a sudden "madness" mechanic. Let players choose how much their own characters carry.

### Real-world parallels
- Genocide, ethnic cleansing, specific real wars, real flags and symbols, and real peoples cast as an enemy.
- **Default line** on depicting real events or real peoples. Build fictional causes; never echo real slurs, symbols or propaganda.

### Dehumanizing the enemy
- "They are all evil" makes atrocity easy to justify at the table. Keep the enemy human, or if inhuman, give them a logic rather than a racial essence.

### War crimes by the characters
- The party may be offered a cruel shortcut (poison the well, burn the granary with people inside). Present it as a choice with visible human cost, and never make it the only or best option. Some tables want that moral weight; check before drafting it.

### Animals
- Warhorses and camp dogs die in war. A common soft limit. Keep animal death off-screen.

### Suicide
- **Default line** on depicting it, including "noble" last stands framed as self-destruction. A heroic sacrifice is a choice to save others, written as such.

## On-screen or off-screen at a glance

| Theme | On-screen by default | Off-screen by default |
|---|---|---|
| Combat | Yes, briefly | Gore beyond one detail |
| Atrocity | Never | The aftermath only |
| Interrogation | Talk, bargains, mercy | Any cruelty |
| Executions | The order and the chance to stop it | The act |
| Children | As refugees or messengers | Any harm |
| Sexual violence | Never | Never |

## Techniques

- **The ripple, softened:** a front's movement shown through an empty house, not a body.
- **The cut:** "The colonel gives the order. You hear it from the next valley. By noon, it is done."
- **The check-in:** write "ask the table: fade or play?" into any session beat that sits near a soft limit.
- **The out:** every grim mission has a path that does not require the party to be cruel.

## In QuestMaster

- Put content notes for sensitive scenes in the DM-only notes of each `upsert_session_beat`, never in player-visible text.
- Write any `stage_secret` near a soft limit as a summary, not a description (a casualty list, not a scene), and flag it in the `get_changeset` recap.
- If a request would cross a hard limit, say so plainly and offer two alternatives that keep the mission's purpose.

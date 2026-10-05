# Grimdark: Safety

Grimdark leans on war, atrocity, cruelty and despair. Those are exactly the themes most likely to cross a real person's limits, and the genre's sources often treat them carelessly. A good grimdark game is dark because of its choices and costs, not because of its graphic content. Use lines and veils.

- A **line** is something that never appears in play, not even off-screen.
- A **veil** is something that can happen in the story but off-screen: the scene fades, the consequence remains.

## Always check first

1. Call `get_table_safety` before drafting. If it returns limits, they override everything in this pack.
2. **Hard limits are absolute.** Do not include them, imply them, or keep them in DM-only notes as an option. Redesign the faction, the villain or the event so the limit is never needed.
3. **Soft limits stay off-screen.** They can exist in history or consequence, never in a described scene.
4. If `get_table_safety` returns nothing, apply the defaults below and tell the DM in the recap which defaults you used.
5. Never ask the DM to reveal individual players' limits; work from the combined list.

## Themes that commonly need a line or a veil

### Sexual violence
- Default: a **line**. Do not use it as a villain's motive, a backstory beat, a threat, or setting texture.
- Show villainy through other choices: theft of seed grain, a hanging, a broken truce, a burned granary.

### Torture
- Default: a veil. It can exist in a faction's methods or a character's past; it is never described in a scene.
- Never make torture the only path to information (see pitfalls.md). If the party chooses it, cut the scene and deliver the consequence.

### Massacre and atrocity
- Burned villages and war crimes are part of the genre. Default: the aftermath on-screen (the empty houses, the chalked names), the act itself off-screen.
- Avoid echoing specific real-world genocides or atrocities, especially with real ethnic, religious or national markers. Keep invented conflicts invented.

### Harm to children
- Default: children can be endangered, orphaned, hungry and saved. They are not hurt or killed on-screen. Child soldiers default to a **line**.

### Slavery and forced labor
- Default: a veil. It can be a faction's crime and a thing the party opposes; it is not a scene played for drama.
- Never present slavery as a neutral economic option for the party.

### Starvation and disease
- The core of the scarcity engine. Usually acceptable as pressure, but some players have real experience of hunger or illness.
- Default: count it, do not describe it in detail. Name the sick and the hungry; do not narrate their suffering.

### Animal cruelty
- Horses killed in battle, dogs hanged by an army. Default to a veil: the consequence is known, not shown.

### Suicide and self-harm
- Despair is a theme of the genre. Default to a **line** on depicting it.

### Despair at the table
- Grimdark can leave real people feeling hopeless. The rule "never make decency pointless" in SKILL.md is also a safety tool: every session should show the party saving someone real.
- If the DM mentions the table is having a hard time, offer lighter arcs within the setting: a truce, a festival, a rescue that works.

## On-screen and off-screen techniques

- **The cut:** end the scene before the act. "The captain gives the order. The next morning, the village is quiet."
- **The count:** move the worst of it into numbers and names on a list, not a scene.
- **The document:** a letter or report describes what happened in one or two calm lines.
- **The player's choice:** when a player character commits a dark act, let the player decide how much is described, and default to less.
- **The check-in prompt:** for any scene that leans on a soft limit, write "Before this scene, ask the table: fade or play?" into the session beat's DM notes.

## In QuestMaster

- Content notes go in DM-only fields (session beat DM notes, the NPC `secret`, a faction's `realAgenda`), never in player-visible text.
- Staged secrets that touch soft limits should summarize, not describe. List them in the recap so the DM can check in before pushing.
- Faction `realAgenda` text can name an indefensible act plainly for the DM; it should never describe it graphically.
- On a `build_cue_list` for a battle or an execution, begin with a quiet cue so the DM can pause or skip before anything graphic reaches the table screen.

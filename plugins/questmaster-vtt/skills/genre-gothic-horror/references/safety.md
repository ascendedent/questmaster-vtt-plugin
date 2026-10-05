# Gothic Horror: Safety

Gothic horror draws on family abuse, confinement, sickness, death and predatory seduction. These are the genre's materials, and they are also the themes most likely to hurt a real person at the table. Handle them with lines and veils.

- A **line** is something that never appears in play at all, not even off-screen.
- A **veil** is something that can happen in the story but off-screen: the scene fades, the consequence remains.

## Always check first

1. Call `get_table_safety` before drafting. If it returns limits, they override everything in this pack.
2. **Hard limits are absolute.** Do not include them, imply them, or put them in DM-only notes "just in case". Redesign the curse or the NPC so the limit is never needed.
3. **Soft limits stay off-screen.** They can be part of the history or a consequence, never described in a scene.
4. If `get_table_safety` returns nothing (not shared, or no limits set), use the defaults below as veils and flag them to the DM in the recap: "these are veiled by default; tell me if your table wants them handled differently".
5. Never ask the DM to reveal individual players' limits. Work from the combined list.

## Themes that commonly need a line or a veil

### Incest and bloodline obsession
- Common in the genre's sources. Default to a **line** unless the table says otherwise.
- Replacement: make the family's obsession about the name, the land or the bargain, not about who marries whom within the family. "Keeping the blood pure" becomes "keeping the debt in the family".

### Abuse of children
- Children in danger are a gothic staple; harm to children on-screen is a common hard limit.
- Default: children can be threatened by the curse, but no child is hurt on-screen, and no child's suffering is described. A rescued child is a valid win; a dead child, if the table allows it at all, is history, not a scene.

### Domestic abuse and coercive control
- The family as a cage is central to gothic. Keep the control structural (inheritance, money, the will, isolation) rather than physical violence described at the table.
- Veil any beating, imprisonment or starvation; show its aftermath through what the victim avoids and fears.

### Predatory seduction and supernatural charm
- The seductive monster is a cliché that easily crosses into non-consent.
- Default: no sexual content involving charm, domination or any supernatural compulsion. A monster's influence is framed as temptation the player chooses how to answer, or as compulsion toward non-sexual acts (open the window, hand over the key).
- Romance with NPCs, if the table wants it, stays between consenting adults and fades to black.

### Body horror and decay
- Rot, transformation, corpses, being eaten. Some tables love the detail; some do not.
- Default: describe one sharp detail and stop (the ring still on the finger), never a lingering inventory.

### Burial alive and confinement
- Sealed rooms, coffins, walled-up victims. Claustrophobia is a real fear for many players.
- Default: imply the confinement (scratches inside a coffin lid); never narrate a player character's experience of being buried alive without a check-in.

### Madness and institutions
- Avoid using real mental illness as a horror reveal ("she was mad all along") or the asylum as a house of monsters.
- Instead: supernatural influence is external and specific (the house is putting dreams in her head), and the people locked away are victims of the family, not of their own minds.

### Suicide and self-harm
- Ghosts and despairing heirs invite it. Default to a **line** on depicting it; at most a death in the family's past, referred to briefly and without method.

### Animals
- Hounds hanged, pets taken, horses killed in a crash. Default to a veil: the animal is missing, or the consequence is heard about, never seen.

## On-screen and off-screen techniques

- **The cut:** end the scene at the door. "The housekeeper closes the nursery door behind her. Morning."
- **The aftermath:** show the consequence, not the act. A sheet over a shape, a room scrubbed too clean.
- **The document:** move the worst of the history into a document summarized in one line, not read aloud in full.
- **The question:** before a scene that leans on a soft limit, the DM can ask "this next part involves X; fade or play?" Write that prompt into the session beat so the DM remembers to ask.

## In QuestMaster

- Put content notes for any sensitive scene in the session beat's DM notes, never in player-visible text.
- When staging a secret that touches a soft limit, write it to summarize, not describe, and tell the DM in the recap which secrets need a check-in before pushing.
- On a `build_cue_list` for a horror scene, add a quiet first cue (lights dimmed, nothing on screen) so the DM can pause or skip before anything graphic appears.

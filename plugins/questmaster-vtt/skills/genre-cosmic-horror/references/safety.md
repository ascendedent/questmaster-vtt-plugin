# Cosmic Horror: Safety

Cosmic horror deals in loss of self, transformation, existential despair and the fear that nothing matters. Those themes can reach real people at the table more directly than a monster can. Use lines and veils.

- A **line** is something that never appears in play, not even off-screen.
- A **veil** is something that can happen in the story but off-screen: the scene fades, the consequence remains.

## Always check first

1. Call `get_table_safety` before drafting. If it returns limits, they override everything in this pack.
2. **Hard limits are absolute.** Do not include them, imply them, or keep them in DM-only notes as an option. Redesign the mark, the site or the cult so the limit is never needed.
3. **Soft limits stay off-screen.** They can exist in history or consequence, never in a described scene.
4. If `get_table_safety` returns nothing, apply the defaults below as veils and tell the DM in the recap which ones you applied.
5. Never ask the DM to reveal individual players' limits; work from the combined list.

## Themes that commonly need a line or a veil

### Mental illness and "madness"
- The genre's sources often treat real mental illness as horror. Do not.
- Marks are specific, supernatural and external: the listening, the arithmetic, a changed hand. Never use labels for real conditions, and never make "the asylum" a house of monsters.
- If a character breaks under strain, describe it as a fantastic effect with a clear source, and let the player narrate their character's reaction.

### Loss of self and identity
- Memory loss, being replaced, becoming someone else. Powerful and distressing.
- Default: a mark can take a memory only if the player chooses it from the offered options. Never overwrite a player character's personality without the player's consent.

### Transformation and body horror
- Slow change into something else is central to the genre.
- Default: one precise detail per description (gills behind the ears, a hand with one joint too many), never a lingering inventory. Player character transformation is opt-in, offered as a mark.

### Drowning, suffocation and being buried
- The deep and the underground are genre staples, and common phobias.
- Default: imply rather than narrate a player character's experience of drowning or entombment. Check in before a scene that leans on it.

### Parasites, insects and infestation
- Common soft limit. Default to a veil: describe the aftermath (the empty husk, the hollowed timber), not the swarm on skin.

### Self-harm and suicide
- Compulsions and despairing NPCs invite it. Default to a **line** on depicting it.
- A mark's compulsion must never be self-harm. Use compulsions like counting, listening, drawing a shape or walking toward water at night, which the player can resist with a cost.

### Children and the changed
- The prodigy, the cultist's daughter, the drawing. Children in danger are effective; harm to children on-screen is a common hard limit.
- Default: children can be threatened, can be strange, can be saved. They are not hurt on-screen.

### Religious trauma
- Cults use kindness and community to recruit. That can echo real experiences of high-control groups.
- Default: keep the cult's recruitment in summary and its members humane; avoid scenes of coercion against a player character.

### Existential despair
- "Nothing matters" is a theme of the genre and a real feeling some players struggle with.
- The small win is also a safety tool: every session should show that the party's choices saved someone real. If the DM's table is having a hard time, lean on the small faith, the survivor and the saved.

## On-screen and off-screen techniques

- **Cut at the threshold:** end the scene as the door opens. Resume with what came out, or did not.
- **The report:** move the worst event into a calm document summarized in a sentence, not read in full.
- **Player narration:** for marks and transformation, ask the player how their character shows it. They control the intensity.
- **The check-in prompt:** write "Before this scene, ask the table: fade or play?" into the session beat's DM notes for any scene that leans on a soft limit.

## In QuestMaster

- Content notes go in DM-only fields (session beat DM notes, the NPC `secret`), never in player-visible text.
- Staged secrets that touch soft limits should summarize rather than describe; list them in the recap so the DM can check in before pushing.
- Knowledge marks built with `upsert_homebrew` should name the effect plainly in the DM layer so the DM can preview exactly what a player will be offered.
- On a `build_cue_list` for a manifestation, start with a quiet cue so the DM can pause or skip before anything graphic appears.

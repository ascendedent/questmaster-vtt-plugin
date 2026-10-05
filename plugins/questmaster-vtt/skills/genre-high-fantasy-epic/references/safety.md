# High Fantasy Epic: Safety

Epic fantasy looks gentle beside horror, but its traditions carry real hazards: destiny that overrides a player's choices, whole peoples painted as evil by birth, bloodline purity, noble sacrifice that slides toward self-destruction, and possession that strips a character of control. Handle them with lines and veils:

- A **line** never appears in play at all, not even off-screen.
- A **veil** can happen in the story but off-screen: the scene cuts, the consequence remains.

## Always check first

1. Call `get_table_safety` before drafting. If it returns limits, they override everything in this pack.
2. **Hard limits are absolute.** Do not include them, imply them or keep them in DM-only notes. Redesign the prophecy or the villain so the limit is never needed.
3. **Soft limits stay off-screen.** They can be history or consequence, never a described scene.
4. If nothing is shared, use the defaults below and say so in the recap: "these are veiled by default; tell me if your table wants them handled differently". When a draft would lean on a heavy theme, ask the DM one focused question first.
5. Never ask the DM to reveal individual players' limits. Work from the combined list.

## Themes that commonly need a line or a veil

### Destiny over agency
- Being declared chosen, doomed or fated can feel like losing control of one's own character.
- **Default:** no destiny is attached to a player character without that player's agreement. Offer it to the DM as a question for the player; never write it into a character's record.
- A prophecy can point at a character's situation; only the player decides what their character does with it.

### Evil races and essentialism
- A people evil by birth is the genre's oldest flaw, and it echoes real-world racism.
- **Default:** no people is evil by nature. The enemy is a cause, an oath or a congregation, recruited from many peoples. Monsters with no culture (an undead host, a made thing) are fine; a culture of people is never a monster.

### Bloodline purity
- "True blood", "pure lineage" and "tainted" heirs can echo eugenic ideas.
- **Default:** bloodlines open doors in the world (a seal recognizes an heir) but never confer worth. If a faction believes in purity, the story treats that belief as the wrong answer.

### Genocide and the destruction of peoples
- "Wipe them out" endings and burned elder cities.
- **Default veil** on the act; **default line** on the party committing it. The enemy can be defeated, broken, scattered or redeemed, never exterminated as a victory.

### Children and chosen ones
- Child chosen ones put children in mortal danger.
- **Default:** a child can be a candidate, a witness or someone to protect; no child is hurt on-screen. If the prophecy points at a child, the party can choose to carry the burden instead.

### Sacrifice and self-destruction
- Heroic sacrifice is a staple; framed carelessly, it slides into suicide.
- **Default line** on suicide and self-harm. A sacrifice is a choice to save others, made with clear eyes, never despair; the player chooses it, the DM never imposes it.

### Possession, mind control and corruption
- The dark artifact that whispers, the hero turned by the enemy.
- **Default:** never take control of a player character's actions without the player's agreement. Corruption is offered as temptation the player can answer, with visible costs, and an honest way back.

### Real faith
- Gods, temples and holy wars can echo real religions.
- **Default:** invent faiths; never borrow real scripture, real figures or real sacred symbols, and never make a real religion's analog the enemy.

### Grief and loss
- Mentors, homes and companions lost on the road. Some players are grieving in real life.
- Losses happen with weight and warning, never as a surprise to punish attachment.

### Phobias
- Giant spiders, swarms, deep water, heights, darkness underground. Check before building a set piece around one.

## On-screen or off-screen at a glance

| Theme | On-screen by default | Off-screen by default |
|---|---|---|
| Epic battle | Yes, the party's slice | Mass slaughter |
| Corruption | As temptation and cost | Body horror detail |
| Sacrifice | As a player's chosen act | Suicide, never |
| Possession | With player agreement | Any action taken against a player's will |
| A people's destruction | Never | History, briefly, if at all |

## Techniques

- **Ask before fating:** "Would the player like the prophecy to point at their character, or near them?" goes to the DM as a question, never as a draft.
- **The cut:** "The citadel falls before you reach it. What is left is the survivors on the road."
- **The way back:** every corruption path has a written route home, even if it costs something.
- **The check-in:** write "ask the table: fade or play?" into session beats near a soft limit.

## In QuestMaster

- Never write destiny, corruption or possession into a player character's record. Stage it as a `stage_secret` the DM decides whether to push, and only after the player agrees.
- Put content notes in the DM-only notes of each `upsert_session_beat`, and flag any sensitive item in the `get_changeset` recap.
- If a request would cross a hard limit, say so plainly and offer two alternatives that keep the scene's purpose.

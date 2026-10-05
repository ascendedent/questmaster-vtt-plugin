# Mystery: table safety

Mysteries usually start with a crime, often a death, and look at it closely. That makes the genre prone to detail the table did not ask for. Decide with the DM how much is shown, and build clues that work at that level.

## Always check first

- Call `get_table_safety` before drafting the crime, the victim or the motive. If the owner shares limits, they bind every draft, including DM-only notes.
- **Lines** are absolute: the theme does not appear on-screen, off-screen, as a motive, as a backstory detail, in a rumour or in a staged secret.
- **Veils** happen off-screen: the players learn that it happened and what it means, never the detail of the act.
- **Soft limits** stay off-screen even when not marked as veils.
- If no limits are shared and the crime involves one of the themes below, ask the DM one question ("Should X be on-screen, off-screen, or left out?") and follow the answer.

## Clues work at any level of detail

A clue needs one specific fact, not graphic description. "The wound is square; the edge of the pit is rounded brick" is a complete clue. Write every physical clue so the DM can read it aloud at a table that has veiled gore.

## Themes that commonly need a line or veil

### Gore and the body
- **Why it comes up:** Examining the body is a classic scene.
- **Off-screen handling:** An undertaker or healer gives findings in plain, clinical language. The players read the report, not the corpse.
- **On-screen with care:** Describe one detail that matters, then move on.

### Violence against children
- **Default:** A line at most tables. Do not use a child as a victim, a culprit or a motive unless the DM explicitly confirms the table wants it.
- **Replacement:** A missing apprentice can be an adult. A family's grief works without a child's death.

### Sexual violence as a motive
- **Default:** Leave it out. It is one of the most common lines, and mysteries reach for it as a cheap motive.
- **Replacement:** Money, inheritance, fear of exposure, revenge for a ruined business, a stolen invention, a political secret. These carry the same weight without the harm.

### Suicide
- **Why it comes up:** "It was not murder after all" and "made to look like suicide" are common twists.
- **Handling:** Treat as a veil by default. If it is part of the truth, handle it with compassion, no method detail, and focus on the people left behind. Avoid using it as a surprise reveal unless the DM confirms the table is comfortable.

### Domestic abuse
- **Handling:** Off-screen. If it is part of a motive, the players learn of it through testimony and its consequences. Never describe it in a scene. Treat survivors with dignity, not as suspects by default.

### Poisoning and illness
- **Handling:** Fine for most tables when described by effect and evidence rather than suffering. A cup, a smell, a register entry, a pale face.

### Drowning, burial and confinement
- **Handling:** Some players are distressed by suffocation imagery. Keep it brief and factual; offer the DM a different method if the table is sensitive.

### Interrogation and coercion
- **Handling:** Player characters questioning suspects is the heart of the genre. Keep it to pressure, leverage and deals. If the players or an NPC move toward torture, cut to the result and its cost (the genre-political-intrigue pack's safety reference covers this in more depth).

### Mental illness as motive
- **Pitfall:** "The madman did it" is a stigmatising cliché and a poor mystery.
- **Handling:** Give the culprit a comprehensible motive. Conditions are not motives.

### Real-world crimes
- **Handling:** Do not base a mystery on a real crime, a real victim, or a real ongoing case.

## Secrets aimed at characters

- `stage_secret` can aim a clue at one character. That is how clues reach the right player, and it can also set players against each other.
- Before staging a clue that implicates a player character, or that one player could hide from the others, ask the DM whether the table enjoys secrets between players.
- Never stage a clue that reveals a player's own backstory secret to the others without the DM confirming the player agreed.

## On-screen versus off-screen, quickly

| Theme | Usually fine on-screen | Usually off-screen | Check first |
| --- | --- | --- | --- |
| Discovering a body | Yes, briefly | Gore detail | Gore |
| Autopsy findings | As a report | The procedure | |
| Poison | Evidence and effects | Suffering | |
| Child victims | | | Always, often a line |
| Sexual violence | | | Always, usually a line |
| Suicide | | Yes | Always |
| Abuse as motive | | Yes | Always |

## When the assistant drafts

- Never include a lined theme anywhere, including the truth paragraph and DM-only notes.
- Write veiled material as decisions and consequences the DM can read aloud.
- Flag anything sensitive in the recap from `get_changeset` before `request_approval`.
- If the DM shares new limits later, offer to rewrite the truth paragraph and its clues to fit.

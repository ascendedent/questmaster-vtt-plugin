# Political intrigue: table safety

Intrigue games often reach for the harshest tools of power: torture, coercion, executions, forced marriages, children used as pawns. They can be handled with weight, or kept off-screen, or left out entirely. The table decides, and the assistant follows.

## Always check first

- Call `get_table_safety` before drafting anything that touches the themes below. If the owner shares limits, they bind every draft.
- **Lines** are absolute. A line means the theme does not appear at all: not on-screen, not off-screen, not implied, not as a motive, not in a staged secret or a rumour.
- **Veils** mean the event can happen in the story but off-screen. Show the decision and the consequence, never the act.
- **Soft limits** stay off-screen. Treat them as veils even if the DM did not mark them as such.
- If no limits are shared and the draft would include a theme from the list below, ask the DM one question: "This involves X; should it be on-screen, off-screen, or left out?" Then follow the answer.

## Themes that commonly need a line or veil

### Torture and interrogation
- **Off-screen handling:** The party hears that a prisoner was "questioned at length". They see the result: a signed confession in a shaky hand, a bandaged wrist, a witness who will no longer meet their eyes.
- **Never:** Ask the players to describe or perform torture. If a player character wants information from a prisoner, offer leverage-based options (a bargain, a threat to reputation, an offer of protection).

### Executions and purges
- **Off-screen handling:** The bell tolls, the gallows are empty by noon, a name is removed from the council roll. Focus on who benefits and who is afraid now.
- **On-screen with care:** A public execution as a political spectacle can be powerful. Describe the crowd, the ruler's face, the silence; not the death.

### Sexual coercion and blackmail
- **Default:** Leave sexual violence out of intrigue entirely unless the DM explicitly says the table wants it addressed. It is a common line.
- **Replacement:** Blackmail can use debts, forged documents, hidden heirs, religious heresy, a past crime. None of these need sexual content to bite.
- **Affairs:** A secret romance as leverage is usually fine; keep it at the level of letters and secret meetings.

### Forced and arranged marriage
- **Off-screen handling:** The contract is signed; the bride or groom is a character with opinions and a plan, not a prop.
- **Agency:** If a player character is being married off, ask the DM whether the player has agreed to that story. Never draft it as a surprise.

### Children as pawns
- **Off-screen handling:** Wards and child hostages can exist as political facts. Keep them safe on-screen. Threats against children should be rare, distant and handled by the plot, not described.
- **Line in many tables:** Harm to children. Check before using it even as a rumour.

### Betrayal of the party by trusted NPCs
- **Why it matters:** Players invest in allies. A betrayal can feel like the DM punishing them.
- **Handling:** Make betrayals conditional and foreshadowed (see pitfalls.md). Give the betrayer a reason the players can understand afterward. Offer the DM a version where the ally confesses before acting.

### Player-versus-player secrets
- **Risk:** Staged secrets aimed at one character can set players against each other.
- **Handling:** Before drafting a `stage_secret` that gives one player a reason to betray another, ask the DM whether the table enjoys inter-party scheming. If not, aim secrets at shared goals instead.

### Slavery, indenture and genocide
- **Default:** Treat these as lines unless the DM asks for them. If the setting includes them, keep them as historical or distant facts that factions argue about, never as on-screen spectacle.

### Real-world political parallels
- **Risk:** Factions that mirror real parties, religions or ethnic groups.
- **Handling:** Build factions from interests, not identities. Never give a faction a real-world religion's or ethnicity's markers.

## On-screen versus off-screen, quickly

| Theme | Usually fine on-screen | Usually off-screen | Check first |
| --- | --- | --- | --- |
| Assassination attempt | Yes, as a fight | The killing of a non-combatant | Poison details |
| Imprisonment | Yes | Conditions of a dungeon | Long confinement of a PC |
| Exile and disgrace | Yes | | |
| Torture | | Yes | Always |
| Executions | The aftermath | The act | Public spectacle |
| Arranged marriage | The contract and politics | Wedding night | A PC's own marriage |
| Children in danger | | Yes | Always |

## When the assistant drafts

- Never include a lined theme in any field, including DM-only notes, faction agendas or NPC secrets.
- For veiled themes, write the record so the DM can read it aloud safely: decision and consequence, no description of the act.
- Mark sensitive drafts in the recap from `get_changeset`, so the DM sees them before `request_approval`.
- If the DM later shares new limits, offer to revise existing drafts that cross them.

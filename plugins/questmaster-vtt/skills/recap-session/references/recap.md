# Recap template

The recap is DM-only Markdown drafted with `save_session_recap`. Write it in this order. Drop a section only when nothing happened in it. Keep the story-so-far paragraph safe to read aloud, because DMs often open the next session with it; hidden truths go in the later sections.

```
# Session N: Title drawn from what happened

**Date played:** from the notes, or blank
**In-world date:** if tracked, or "not tracked"
**Duration:** if noted
**Players present:** if noted

## The story so far
One tight paragraph, past tense, told like a story: where they started,
what they did, where they ended. Player-safe.

## Story beats
**Beat title**
- What happened: 2 to 4 sentences.
- Player decision: what they chose, specifically.
- Consequence: what resulted.
- Thread impact: the thread it opened, advanced or closed, or "new thread".
(Usually 4 to 8 beats, in order.)

## Player decisions
| Decision | Outcome | What it means going forward |
|---|---|---|

## NPC interactions
### NPC name (existing or new)
- Interaction: what passed between them and the party.
- Relationship shift: better, worse, or changed in kind, and why.
- After the session: where they are, what they want now, what they know.
- Flag: anything the DM must follow up.

## Faction activity
### Faction name
- How they appeared: in person, mentioned, or acting off-screen.
- Party standing: improved, worsened or unchanged, and why.
- What they did: their agenda this session, not just what the party saw.

## Threads
- New: name, one sentence, who is involved, what is at stake.
- Advanced: how it moved.
- Closed: how it resolved.
- Needs payoff soon: open for several sessions without movement.

## Loot and acquisitions
| Item | Source | Who has it | Notes (identified? cursed? significant?) |
|---|---|---|---|
Gold gained, spent, net, as the notes give them.

## DM follow-through
1. Action required: what to prep, decide or track before next session.

## Recommended focus for next session
- Primary hook: the thread that most needs to land next.
- Secondary hook: a subplot to weave in.
- NPC to bring back: whose return would feel earned now.
- Tone calibration: what the table needs after this session's energy.
```

## Reading messy notes

- **Fragments and shorthand:** expand them only as far as the notes support. "B > toll guy, ring" becomes "Brannoc gave the toll-keeper a ring" only if the notes elsewhere say who B is and which ring.
- **Timestamps:** use them for order; drop them from the prose.
- **In-character lines:** keep memorable ones verbatim, in quotes, attributed. Never invent dialogue.
- **Out-of-character table talk:** drop it, unless it records a ruling, a promise the DM made, or a player's stated plan for next time. Those go in DM follow-through.
- **Dice:** keep only rolls that decided something ("the natural 1 on the bridge cost them the satchel").
- **Unknown names:** `search_campaign` first; spelling in notes drifts. No match means a new NPC or place, marked (new). Still unsure: [unclear].
- **Contradictions inside the notes:** record both versions and flag them; the DM decides.
- **Plan vs play:** compare with `get_session_prep`. Planned scenes that never happened are not failures; list them in follow-through as still available.

## Judgment calls to flag, not settle

- Closing a thread the notes only imply is finished.
- An NPC's death or disappearance when the notes are ambiguous ("left him on the bridge").
- A faction standing change the party may not know about yet.
- Whether a staged secret was actually revealed, or only hinted at.
- Loot whose owner is unclear.

## Spotting threads that need payoff

- Open three or more sessions with no movement.
- A promise an NPC made to the party, or the party made to an NPC.
- An object the party picked up, asked about, and never used.
- A question a player asked out loud that nobody answered.
- A villain who has not acted on-screen since the thread opened.

## Next-session focus that helps

- Name one primary hook, not five. The DM can only open one session at a time.
- Bring back an NPC with a reason tied to this session's events.
- Read the energy: two combat-heavy sessions in a row call for a social or exploration night, and the reverse.

## Worked example (original)

Raw notes:

```
s7. ferry -> toll house. Ottile caught w/ ledger, B paid fine w/ courier ring (!!)
Lisbet showed up?? offered 40g for ledger, party said no. Mara rude to her
levee - helped crew, Wrenna learned money is skimmed (staged secret 2?)
fight on bridge w/ sellswords, captain surrendered, writ = guild seal
end: Oswy missing. bell at noon
```

Excerpt of the recap:

> **The story so far.** The party followed the courier's satchel to the toll house, where Brannoc paid Ottile Varn's fine with the drowned courier's ring. They turned down the guild's offer for her ledger, worked a shift on the failing levee, and broke a guild-paid blockade on the old bridge. At noon the next day, the ferry bell rang again, and Oswy was gone.

> **Player decisions**
> | Decision | Outcome | What it means going forward |
> |---|---|---|
> | Brannoc paid the fine with the courier's ring | Ottile is in the party's debt | The guild may now believe Brannoc has the ledger |
> | Refused Factor Lisbet's 40 gp | Lisbet left cold; Mara insulted her | Guild standing likely worse [judgment call] |

Follow-through drafted: thread "The drowned courier" advanced with urgency raised to high; new thread "Oswy is missing" with urgency critical and `plannedSessionId` on session 8; the Copperwake guild's `partyStanding` from neutral to unfriendly (flagged); Holloway the sellsword captain as a new NPC with `relationshipToParty` "surrendered, wary"; staged secret 2 listed for the DM to push to Wrenna's player.

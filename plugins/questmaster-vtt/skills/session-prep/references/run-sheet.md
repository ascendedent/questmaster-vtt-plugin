# Run sheet template

One page the DM can glance at mid-scene. Bullets, bold decision points, no paragraphs longer than three lines. Everything here is DM-facing unless marked (players see).

```
SESSION N: <title> (players see)          <length>, party level X
LAST TIME: two lines from the last recap: where they stand, what they want.
THE QUESTION: the one thing this session could answer.

STRONG START
  <30 seconds of read-aloud or a situation already in motion>
  Ask the table: <a question to a specific player>

SCENES (any order; drop any)
  1. <name> @ <location>
     In: <how the party gets here>   Stakes: <what changes if they win / lose / skip>
     Who: <NPCs>   Exits: <at least two places this can lead>
  2. ...

SECRETS AND CLUES (staged; push when earned)
  - <clue> | could surface: <scene, NPC, object> | for: <PC or party>

NPC QUICK REFS
  <Name>: looks <one detail> | sounds <one habit> | wants <now> | won't <line>

ENCOUNTERS
  <Name> (<type>, <rating>) map: <map or none> | stakes | how it ends without a kill

CLOSING OPTIONS
  - If they <did X>: <hook>
  - If they <did Y>: <hook>

FALLBACK
  <one ready scene for when the party goes somewhere unplanned>
```

## Section rules

### Last time and the question
- Pull from the last played session's recap (`get_entity` kind `session`). If none exists, ask the DM once, or run `recap-session` first.
- The question is open: "Will the ferrymen side with the toll-wardens?" not "The party discovers the betrayal".

### Strong start
- Start in motion: a fight already underway, a demand already made, a body already found. No tavern meet-and-greet unless the tavern is on fire.
- End on a choice or a question to one named player.
- Draft it as the first session beat (`occurredAtInSession` 10) and put its one-line version in the session `summary`.

### Scenes
- 3 to 5 per 3 to 4 hour session. One should be social, one should hold a decision that costs something.
- A scene is a situation: a place, people with wants, and a clock. Never "the party goes to X and learns Y".
- At least two exits per scene, and at least one exit that leads to a different scene than the obvious next one.
- Each scene is a session beat. Its `description` holds In / Stakes / Who / Exits in four short lines; link `npcIds`, `locationId`, `threadId`.
- Tie plot beats meant for this session with `upsert_plot_node` `sessionId`, so `get_session_prep` shows them.

### Secrets and clues
- 6 to 10 short, true facts. Not attached to scenes in advance: list two or three places each could surface, and deliver it wherever the party actually goes.
- Anything the party MUST learn has at least three clues, in three different places.
- Each is a `stage_secret` with `sessionId`. Aim it with `audienceCharacterIds` at the PC whose skills or backstory fit; leave it empty for the whole party.
- Write the `body` in-world (a ledger line, a whispered name, a smell on the coat), and set `subjectKind`/`subjectId` so the DM can find it from the NPC or faction.
- Unused clues roll forward: next prep, move them with `stage_secret` {`id`, `sessionId`: next session}.

### NPC quick refs
- Only the NPCs likely to speak this session. Read their `personality` and `motivation` with `get_entity`; don't contradict them.
- Three lines: a look, a voice habit the DM can perform, a want for tonight. Add what they will not do.
- New NPCs go through `generate-npc` and appear in the draft before they appear in the sheet.

### Encounters
- Combat: `propose_encounter` for a starting roster, then `plan_encounter` with `usedInSessionId` and `mapId`. Report the rating QuestMaster returns, never your own math.
- Every fight states why it happens, what the enemies want besides killing, and how it ends early (surrender, flight, a bargain, a collapsing floor).
- Social, puzzle and exploration encounters: `plan_encounter` with `encounterType` and the three consequence fields, no monsters.
- A fight without a map is fine for theater of the mind; say so on the sheet. A fight that wants a battle map is a `weave-the-map` job if the map exists but is unlinked.

### Screens and cues (optional)
- Offer once: "Want me to queue screens for the table TV?" Draft only on a yes.
- One preset per beat that deserves a screen: the opening scene image, a map, a portrait when a key NPC enters, a short text card (a letter, a sign). Text cards are player-visible.
- Use saved ids only (from `get_screen_prep` scene library, `list_entities` maps, `get_entity` NPCs). An NPC drafted tonight gets a portrait screen next time, after approval.
- `build_cue_list` `add` in running order; `clear: true` first only if the DM wants the old list gone.

### Closing and fallback
- Two or three closing hooks keyed to plausible party choices, each pointing at a thread.
- One fallback scene that fits anywhere: a messenger, a rival crew, weather. It uses an existing NPC or faction.

## Worked example

```
SESSION 4: The Bell-Founder's Debt      3.5 h, party level 4
LAST TIME: The party recovered the stolen bell clapper but owe the
  ferrymen a favor. Wexley Ford's toll-wardens want the clapper back.
THE QUESTION: Who does the party hand the clapper to?

STRONG START
  The ferry is halfway across when the rope goes slack: someone cut it
  upstream. Ask Brannoc's player: what do you grab first?

SCENES
  1. Adrift @ the river       In: strong start   Stakes: clapper lost or kept
     Who: ferryman Ilse Marrow  Exits: wardens' pier, the reed-cutters' camp
  2. The Foundry Ledger @ bell-foundry  In: Ilse's tip, or curiosity
     Stakes: proof the wardens melted church bells  Who: old founder Dace
     Exits: wardens' hall, the abbey
  3. Toll Hearing @ wardens' hall   In: summons, or arrest
     Stakes: party's standing with the wardens  Who: Warden Pell
     Exits: a deal, a fight, a public accusation
  4. Reed-Cutters @ camp       In: scene 1 drift   Stakes: an ally or an enemy
     Who: the cutters' elder    Exits: a hidden channel to the abbey

SECRETS AND CLUES
  - The rope was cut by a warden's knife | rope end, Ilse, cutters | party
  - Dace was paid in abbey silver | ledger, Dace's purse | Corwen (Investigation)
  - Pell owes the ferrymen money | hearing, Ilse, ledger | party
  - The abbey wants the clapper to ring a bell nobody should hear | cutters, abbey | Brannoc

ENCOUNTERS
  Cut Loose (combat, rated moderate) map: Ford Crossing | grab the clapper
    ends early if the thieves get the clapper or lose two of four
  Toll Hearing (social) no map | three outcomes drafted in consequences

CLOSING OPTIONS
  - Clapper to the wardens: the abbey sends a polite, terrifying letter.
  - Clapper to the abbey: the first bell rings at midnight.
FALLBACK
  A rival salvage crew is dredging for the same clapper. Ilse knows them.
```

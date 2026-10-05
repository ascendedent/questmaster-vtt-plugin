# Placing lore in QuestMaster

Lore is not a record type. It is spread across the records it is about, split by who may
see it. Decide the placement before drafting, and tell the DM where each piece will live.

## Decision rules

1. **Will players read, hear or find this text?** It is a `stage_secret`. Its `body` is the
   in-world text exactly as they would meet it. Give it a `title` the DM will recognize in
   the app ("Chapel founding stone"), a subject (`subjectKind` and `subjectId`, or `free`
   with `subjectLabel`), and an audience.
2. **Is it attached to an object the party could carry?** The player-facing story is the
   item's `lore`; the truth is its `secret`. (Item lore reaches players only when the DM
   pushes it.)
3. **Is it the truth about a place?** The location's `dmNotes`.
4. **Is it the truth about a power, a faith or a people?** The faction's `realAgenda`.
5. **Does one person know it, hide it, or carry a third version?** That NPC's `secret`
   (what they hide) or `notes` (what they know and how they'd tell it).
6. **Is there a moment when the party finally understands it?** A plot beat
   (`upsert_plot_node` with `arcId` and `title`) whose `description` says what they learn.
   Clue beats lead to it with `link_plot_nodes`.
7. **Will it take several sessions to unravel?** An `upsert_thread` connecting the NPCs,
   factions and locations involved.

One piece of lore usually lands in three or four of these places.

## Aiming staged secrets

- `audienceCharacterIds` is the character most likely to find it: the one who reads the
  script, worships at the shrine, grew up in the valley. Empty means the whole party.
- Spread clues across characters so each player holds part of the picture.
- When a session is planned for it, set the secret's `sessionId` so it shows up in
  `get_session_prep`. When it serves a beat, set `narrativeNodeId` to that beat.
- Never put the truth layer in a staged secret unless the DM wants players to learn it.

## Clue chains for a reveal

For each revelation, plan at least three clues, because the party will miss some:
1. Draft the revelation beat first: `upsert_plot_node {arcId, title: "The flood was
   opened"}` and keep its ref.
2. For each clue, a staged secret aimed at a different character, plus a clue beat
   (`upsert_plot_node`) joined to the revelation with
   `link_plot_nodes {fromNodeId: clue, toNodeId: revelation}`.
3. Put the clue's ref on the secret with `narrativeNodeId`.
4. Lines that would loop the plot are refused; clues point forward into the reveal.

## Worked example: the flood at Coldharrow Ford

Lore asked for: "Why did the river flood eleven years ago?"

**In-world pieces** (staged secrets):
- *Chapel chronicle* (`subjectKind: "location"`, the chapel's id, aimed at the cleric):
  "...the faithful were spared, the flood parting at our threshold."
- *Rumor A* (`subjectKind: "free"`, `subjectLabel: "the flood"`, aimed at the rogue): "Wasn't
  rain. My uncle heard the sluice chains running that night."
- *Rumor B* (aimed at the ranger): "The eel-smoker got rich the year after the flood. Ask
  where her new boats came from."
- *Ledger page* (`subjectKind: "faction"`, the millers' guild, aimed at the wizard): a
  column of payments to "C." ending the month of the flood.

**DM-only truth**:
- Location `dmNotes` (the upstream sluice): "Opened on purpose by the millers' guild to
  ruin the farmers downstream and buy their land cheap. The chapel was spared because it
  sits on the only high ground."
- Faction `realAgenda` (the millers' guild, read first and appended): the land purchases,
  and that their current master paid the sluice-keeper.
- NPC `secret` (the sluice-keeper, now the toll clerk): "He opened it. He was paid in
  forgiven debts and a job. He has kept the receipts."

**Structure**:
- Thread: "Who opened the sluice?", urgency low, connected to the guild, the clerk and the
  sluice location.
- Revelation beat: "The flood was opened". Its `description` says what the party learns
  (the guild paid for it), not the clerk's guilt, which stays a further discovery.
- Clue beats for the chronicle, the two rumors and the ledger, each linked into the
  revelation.

## Revising lore that already exists

- Read the record with `get_entity` first; `dmNotes`, `realAgenda`, `secret` and `notes` are
  replaced whole, so send the old text with your addition.
- A staged secret can be changed while still staged (pass its `id`). Once the DM has pushed
  it, it is part of the table's history: draft a new secret that complicates it instead.
- An item's lore can't be changed here after it has been pushed; a beat can't be changed
  after it was shown. Say so and offer a new piece.
- If the new lore contradicts canon, stop and show the DM both versions. Retcons are theirs.

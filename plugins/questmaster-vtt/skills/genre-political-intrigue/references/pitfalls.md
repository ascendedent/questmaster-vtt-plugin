# Political intrigue: pitfalls and fixes

Each entry names a failure mode the assistant should watch for in the DM's prep or in its own drafts, then the fix.

## The fog of names

- **Symptom:** Players cannot remember who anyone is. Every session opens with "wait, which one was the duke?"
- **Fix:** No more than two or three new named NPCs per session. Give each faction one visual signature (a colour, a badge, a smell) and repeat it every time a member appears. Offer the DM a one-page cast list as a `save_monitor_preset` with their portraits (from the portrait tool where this connection has one, or the app), so the table screen can show who is who.

## The obvious villain

- **Symptom:** One faction is plainly evil, so the players' choice is made before the session starts.
- **Fix:** Give the villainous faction a grievance the players would sympathise with, and give the "good" faction a method they will find ugly. Rewrite each `realAgenda` until it reads as a defensible position.

## Intrigue by one roll

- **Symptom:** An Insight check reveals the traitor, or a Persuasion check wins the vote.
- **Fix:** Rolls reveal tells and open doors; they do not deliver verdicts. A good Insight roll tells the player that the envoy is afraid, not why. Leverage is earned through action: a document stolen, a witness found, a favour done.

## The static board

- **Symptom:** Factions wait politely for the party to act. Nothing changes between sessions.
- **Fix:** Run the between-session faction turn (beats.md) every time. Each faction moves once, and each move leaves a visible sign. Draft the moves as `upsert_plot_node` beats so the DM can see them on the plot board.

## Forgotten debts

- **Symptom:** The party does a duke a favour in session 2 and the duke never mentions it again. Players learn that favours are free.
- **Fix:** Log every favour as an `upsert_thread` the moment it happens, with who owes, what, and roughly when it will be called in. Schedule it to a session. Collect it, with interest.

## The scripted betrayal

- **Symptom:** The DM has decided an ally will betray the party on a fixed date, whatever the party does.
- **Fix:** Make betrayal conditional. Write the ally's breaking point ("if the Chapter calls in his debt and nobody else can pay it") and let the party see the pressure building. If they relieve the pressure, the betrayal does not happen. Offer the DM both branches.

## Everyone lies

- **Symptom:** Every NPC is deceptive, so the players trust nobody and stop engaging.
- **Fix:** Most people mostly tell the truth, and leave things out. Reserve outright lies for one or two NPCs per arc, and make them findable.

## Etiquette as a trap

- **Symptom:** Players are punished for not knowing court manners their characters would know.
- **Fix:** Characters know what their backgrounds teach them. Have a servant, a herald or a friendly NPC brief them, or let a successful check describe the expected form. Punish deliberate insults, not ignorance of the DM's rules.

## Nothing for the fighters

- **Symptom:** The barbarian sits out three hours of council debates.
- **Fix:** Give martial characters political weight: a bodyguard's presence, a duel of honour, a garrison that respects them, a veteran who will only talk to another soldier. Put a physical problem inside every social set piece: a door to hold, a messenger to intercept, an assassin to spot.

## Talk without decisions

- **Symptom:** Sessions are long conversations where nothing is decided.
- **Fix:** Every scene ends with a choice the players make: accept or refuse, deliver or burn, vote yes or no. If a conversation has run ten minutes without a choice on the table, an NPC puts one there.

## Information without consequence

- **Symptom:** The players discover a great secret, and nothing happens because nobody else knows they know.
- **Fix:** Secrets are only leverage when someone learns the party has them. When a secret is staged, also draft who notices the party asking, and what that person does.

## The DM's favourite wins

- **Symptom:** A beloved NPC always comes out on top, regardless of the party.
- **Fix:** When drafting faction moves, give the favourite a real cost every time it wins. If the assistant notices one NPC winning three arcs running, point it out and offer the DM an alternative.

## Real-world politics at the table

- **Symptom:** A faction is a thinly veiled version of a real party or movement, and the table argument stops being about the game.
- **Fix:** Build factions from interests (land, money, faith, safety), not from current headlines. If the DM wants a real-world resonance, keep it thematic and check with the table first.

## Too many hinge events

- **Symptom:** Every session has a vote, a wedding and a coronation. Nothing feels momentous.
- **Fix:** One hinge per arc. Everything else is pressure building toward it or debts falling from it.

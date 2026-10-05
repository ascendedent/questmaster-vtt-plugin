---
name: genre-political-intrigue
description: Genre pack for political intrigue campaigns, built on the faction web, the leverage economy, favours that are always debts, and three-sided negotiations, with concrete steps for drafting it in QuestMaster. Use when the campaign centres on courts, councils, succession fights, guild politics, spies or diplomacy, or when the DM asks for scheming nobles, shifting alliances, a vote or a summit, or a session where talking is the main event.
---

# Political Intrigue

Play feels like a crowded room where everyone wants something, nobody says it plainly, and every kindness is written down in somebody's ledger.

## Use this when

- The tone or setting text mentions a court, council, regency, succession, embassy, guild seat, election, treaty or spy network.
- The DM says the players love talking to NPCs, wants backstabbing or shifting loyalties, or asks "who would side with whom?"
- The party holds rank, has a patron, sits on a council, or is about to be offered a seat.
- The big moment of an upcoming session is a meeting, a vote, a wedding, a trial or a funeral rather than a fight.

## Tone pillars

- **Everyone is reasonable from where they stand.** No faction is cartoon evil; the danger is that each is right about something.
- **Information is currency.** Knowing who visited the chancellor at midnight is worth more than a magic sword.
- **Courtesy is armor.** Open violence is the failure state; when blood is spilled in the hall, someone has already lost.
- **Consequences compound.** A favour granted in session 2 is collected in session 9, with interest.
- **The party starts as a piece and learns to move the board.**

## The rules that matter most

1. **Build the faction web before any plot.** Draft 4 to 6 factions, each with a public mission, a real agenda, and a concrete tie (debt, marriage, hostage, shared crime, grudge with a date) to every other faction. Plot is what happens when someone pulls a tie.
2. **Run the leverage economy.** Every NPC with power has a want, a fear, and something they hold over someone else. Leverage is always a noun the party can steal, trade or burn: a letter, a witness, a signet, a vote. Never let a single Insight or Persuasion roll replace earning it.
3. **Every favour is a debt.** When an NPC helps the party, decide at that moment what they will ask in return and roughly when. When the party helps an NPC, that NPC owes them and pays in kind. Log every debt as a thread; never forget one, never forgive one silently.
4. **Make every important negotiation three-sided.** Two sides haggle; three sides scheme. Add a party with its own stake (a mediator with an agenda, a rival bidder, the people the deal lands on) so the players have something to play off.
5. **Factions move between sessions.** After each session, advance every faction one step on its agenda or have it react to the party, never both. Show moves as news, rumours, changed seating and new faces at the door.
6. **Offer moves, not verdicts.** When the DM asks what an NPC would do, give 2 or 3 moves that fit that NPC's want and fear, each with its consequence, and let the DM choose.

If the campaign's factions or the date of the hinge event (the vote, coronation or treaty) are missing, ask the DM that one question before drafting.

## Composing with other packs

- `genre-mystery`: a murder at court is a mystery where every suspect has political cover. Use the clue graph for the investigation and the leverage economy for what naming the culprit costs.
- `genre-heist`: a heist is intrigue's sharpest tool. Make the target a piece of leverage (a ledger, a seal, a hostage letter) and play the fallout as faction moves.
- `genre-gothic-horror`: a decaying noble house whose politics hide a curse. Keep the faction web and replace one faction's real agenda with something inhuman.
- `genre-war-campaign`: the politics behind the front. Make the hinge event a ceasefire, a treaty or a change of command, and let the garrison faction become the army in the field.

## Building it in QuestMaster

- Read `get_campaign_overview` and `get_table_safety` first, then `search_campaign` for every faction, NPC and thread you plan to touch, so you extend what exists instead of duplicating it. Check `get_party` for backstory ties the web can hook into.
- Draft each faction with `upsert_faction`: `publicMission` is what it says at court, `realAgenda` (DM-only) is what it wants. Write its ties into the record in plain terms: "owes the Ashen Scale 9,000 crowns", "holds the heir's gambling markers".
- Draft each power broker with `upsert_npc`, noting want, fear, tell, what they hold and what they owe.
- Log each favour and debt with `upsert_thread`. Raise its urgency as it nears collection and schedule it to the session where it comes due.
- Give each faction's agenda an `upsert_arc`; its steps are `upsert_plot_node` beats. Use `link_plot_nodes` to draw party actions into the faction responses they trigger.
- Plan a negotiation or council as `upsert_session_beat` entries: one beat per side's opening position, one for the third side's move, one for the close.
- Stage intercepted letters, rumours and overheard asides with `stage_secret`, aimed at the character whose contacts would plausibly hear them.
- Mark the council chamber with `annotate_map` labels (who sits where, guarded doors), hidden until shown, and offer a `save_monitor_preset` of the hall for the table screen. Finish with `get_changeset`, recap for the DM, and `request_approval`.

## References

- Read [references/beats.md](references/beats.md) when building the faction web, outlining an arc or session, or running the between-session faction turn.
- Read [references/npcs.md](references/npcs.md) when drafting courtiers, envoys, spies or any NPC who holds leverage.
- Read [references/encounters.md](references/encounters.md) when planning a council, banquet, trial, duel, assassination attempt or negotiation.
- Read [references/factions.md](references/factions.md) when drafting factions or deciding how two of them collide.
- Read [references/lore.md](references/lore.md) when describing a court, naming houses and offices, or writing letters, minutes and contracts.
- Read [references/pitfalls.md](references/pitfalls.md) when an intrigue plot feels stuck, confusing or decided by one roll.
- Read [references/safety.md](references/safety.md) before drafting torture, coercion, executions, forced marriage or betrayal of a player character, and whenever `get_table_safety` returns limits.

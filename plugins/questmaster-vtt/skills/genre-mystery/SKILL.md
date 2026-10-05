---
name: genre-mystery
description: Genre pack for mystery and investigation campaigns, built on the three-clue rule, a clue-to-scene graph, and red herrings that are still true about something, with steps for drafting clues, revelations and scenes in QuestMaster. Use when a campaign or session centres on a murder, disappearance, theft, conspiracy or secret to be uncovered, or when the DM asks for clues, suspects, an investigation that cannot dead-end, or help because the players are stuck.
---

# Mystery

Play feels like the table leaning over a pile of facts, arguing, until someone says "wait" and everything rearranges itself.

## Use this when

- The tone or setting text mentions an investigation, inquest, murder, disappearance, cult, conspiracy, or a town with a secret.
- The DM says "my players are stuck", "I need clues", "who did it?", or wants a murder mystery session.
- A player character is an investigator, a priest who hears confessions, or has a backstory built on an unsolved crime.
- The goal of an upcoming session is to find something out rather than to defeat something.

## Tone pillars

- **The truth is fixed; the path is not.** What happened is decided before prep. How the players reach it is theirs.
- **Fair play.** Everything needed to solve it can be found. Afterward, the players should feel they could have seen it sooner.
- **Everyone is hiding something, and most of it is not the crime.**
- **The culprit is alive.** Investigation provokes reaction. The mystery moves while the players think.
- **The click is the reward.** The moment the players connect two facts themselves is worth more than any reveal speech.

## The rules that matter most

1. **Write the truth first.** Before any clue, write one paragraph: who did what, when, how, why, and what they have done since to hide it. Every clue is a trace of that paragraph.
2. **Apply the three-clue rule to every revelation.** List each conclusion the players must reach. Give each one at least three clues, spread across different scenes and of different kinds (physical, testimony, document, behaviour). The players will miss one, misread one, and find the third.
3. **Build a clue-to-scene graph, not a corridor.** Each scene (a place, a person, an event) holds clues pointing to two or more other scenes. Give the players at least three ways in and several ways to reach the end. No single scene may be a chokepoint.
4. **Make red herrings true about something.** A false lead is a real secret pointed at the wrong crime: the suspect lied because of a debt, the blood is from a smuggled animal. Following it uncovers a true fact and a real NPC, never a dead end.
5. **Let failure cost, never block.** A failed check still finds the clue, at a price (time lost, a witness spooked, the culprit warned), or finds a different clue. If the players stall, the culprit acts, and that action is a new clue.
6. **Let the players be right.** If they reach the right answer early or by a route nobody planned, it is right. Never move the culprit to stretch the mystery; complicate the proof instead.

If the truth paragraph is missing and the DM has not said who did it, ask that one question before drafting clues.

## Composing with other packs

- `genre-political-intrigue`: suspects with political cover. Solving the crime is half the story; naming the culprit in public spends leverage and creates debts.
- `genre-heist`: a theft to reconstruct ("how did they get in?") or a final revelation that can only be proved by stealing the evidence back.
- `genre-gothic-horror`: the crime belongs to a family. Clues become diary pages, wills and repainted portraits, and the culprit is whoever still profits from the old sin.
- `genre-cosmic-horror`: an investigation into something that should not exist, where each revelation costs the investigators something to know. Keep the three-clue rule; let the final revelation be the one nobody wanted to reach.

## Building it in QuestMaster

- Read `get_campaign_overview` and `get_table_safety`, then `search_campaign` for suspects, places and threads already in play. Read `get_party` and `get_character` to learn who has the skills and backgrounds to find which clues.
- Draft the mystery as an `upsert_arc`, with the truth paragraph in its DM-facing description.
- Draft each **revelation** (a conclusion the players must reach) as an `upsert_plot_node` on that arc: "Garr was murdered", "the bell holds less bronze than was paid for".
- Draft each **clue** as a `stage_secret` aimed at the character most likely to find it: the herbalist identifies the poison, the noble recognises the seal. Write its text exactly as the player will receive it. The DM pushes it in the app when it is found.
- Give each clue a small `upsert_plot_node` as well, and `link_plot_nodes` from the clue to the revelation it supports. The plot board then shows at a glance which revelation has fewer than three incoming clues. Links cannot loop: draw clues into revelations and revelations into the scenes they open, and record backward pointers in the clue's text rather than as a line.
- Draft each **scene** as an `upsert_session_beat` in the session where it is most likely to be played. Mark the entry scenes and list which clues each beat holds; beats are available, not ordered.
- Draft suspects with `upsert_npc` (alibi, what they hide, what they lie about, tell). Draft the culprit's cover-up moves as an `upsert_thread` whose urgency rises each day: that is the proactive clock.
- Mark evidence on the crime scene with `annotate_map`, hidden until shown, and offer a `build_cue_list` of handouts and portraits (from the portrait tool where this connection has one, or the app) for the DM to fire. Finish with `get_changeset`, recap, and `request_approval`.

## References

- Read [references/beats.md](references/beats.md) when writing the truth, listing revelations, building the clue-to-scene graph, or outlining an investigation session.
- Read [references/npcs.md](references/npcs.md) when drafting suspects, witnesses, the victim, experts or the culprit.
- Read [references/encounters.md](references/encounters.md) when planning interrogations, crime scenes, the accusation, the culprit's clock, or investigation magic.
- Read [references/factions.md](references/factions.md) when deciding who else has a stake in the truth staying buried or coming out.
- Read [references/lore.md](references/lore.md) when describing evidence, naming people and places, or writing letters, ledgers and other found documents.
- Read [references/pitfalls.md](references/pitfalls.md) when the players are stuck, a clue chain has a single point of failure, or a red herring risks a dead end.
- Read [references/safety.md](references/safety.md) before drafting a crime's details, a motive involving abuse, a death that may be self-inflicted, or harm to children, and whenever `get_table_safety` returns limits.

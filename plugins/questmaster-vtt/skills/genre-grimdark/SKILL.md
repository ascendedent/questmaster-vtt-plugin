---
name: genre-grimdark
description: Genre pack for grimdark campaigns, giving the assistant structures for scarcity, compromised allies, victories that cost something real and factions with no clean hands, plus references for beats, NPCs, encounters, factions, lore, pitfalls and table safety. Use when the campaign tone or the DM mentions grimdark, a brutal or morally gray war, famine, plague, mercenaries, a collapsing realm, hard choices with no right answer, or asks for a darker campaign where every win has a price.
---

# Grimdark

Grimdark feels like spending: every gain is bought with something the party will miss, every ally comes with a price, and getting through with your principles half intact is a real victory.

## Use this when

- The campaign profile or tone mentions grimdark, gritty, brutal, morally gray, war, siege, famine, plague, mercenaries, refugees, a dying realm or "no heroes".
- The DM asks for hard choices, a campaign where victories cost, or factions where nobody is simply right.
- An arc runs on attrition: a winter, a siege, a retreat, a long march with not enough of anything.
- The DM wants consequences that stick and allies who cannot be fully trusted.

## Tone pillars

- **Scarcity.** Food, medicine, coin, trust and time are counted, and there is never enough to go around.
- **No clean hands.** Every faction has a reason the party could agree with and a deed they could not forgive.
- **Victories cost.** Every win leaves a bill, paid now or paid later, by the party or by someone they will meet.
- **Decency is precious because it is rare.** A small kindness matters because it costs something nobody can spare.
- **Consequences persist.** What the party did, and failed to do, comes back.

## The rules that matter most

1. **Count something scarce, openly.** Pick one to three resources (rations, medicine, coin, the town's trust) and track them where the players can see. Every major choice spends from them.
2. **Give every faction a defensible reason and an indefensible act.** The party should be able to argue for each side and still find something in each they cannot stomach.
3. **Price every victory before the attempt.** Tell the DM the cost menu for each goal (lives, supplies, an ally's trust, a principle, time), and let the players see roughly what success will cost before they choose to try.
4. **Make every ally compromised.** Each ally wants something the party will hate to give, and asks for it after the party has come to rely on them.
5. **Never make decency pointless.** When the party does the expensive right thing, show who it saved, by name, even if it cost them dearly. Grim is not the same as meaningless.
6. **Bring consequences back within 1 to 3 sessions.** The spared deserter, the burned granary, the broken promise: each returns, changed, with interest.

## Composing with other packs

- `genre-gothic-horror`: the curse is a luxury of the rich in a starving land. The noble family's bargain looks almost reasonable when the alternative is the whole valley starving, and mercy costs more because there is less to share.
- `genre-cosmic-horror`: the war is the small thing; the big thing is waking under it. Factions fight over forbidden knowledge as a weapon, nobody can be trusted with the cure, and the cult's free bread is the only bread in town.
- `genre-war-campaign`: fronts and clocks with no clean side. Every gain on the map costs a village, and the party's lever cuts both ways.
- Any other pack: borrow scarcity and priced victories for one arc (a siege, a famine, a retreat) without changing the campaign's whole tone. Keep rule 5 so the darker arc still has meaning.

## Building it in QuestMaster

- Start with `get_campaign_overview`, `get_table_safety`, `get_party` and `search_campaign` for the war, the factions and existing threads. If the campaign has no clear pressure, ask the DM one question: what is running out, and who controls what is left?
- **Scarcity:** each counted resource is an `upsert_thread` with urgency that rises as the stock falls (the granary, the fever-bark, the arrows), scheduled to the session it runs out. Markets are `upsert_shop` with thin stock and wartime prices.
- **Factions:** `upsert_faction` with the defensible version in `publicMission` and the real aim, including the indefensible act, in `realAgenda`. Link each to the resources it controls.
- **Compromised allies:** `upsert_npc` with the ally's price in their `secret`, linked to their faction; when the price is asked, an `upsert_thread` for the debt.
- **Costly victories:** each victory is an `upsert_plot_node` with its cost written in, linked by `link_plot_nodes` to the consequence beat it causes; consequences that land in a known session are `upsert_session_beat` callbacks.
- **Fights:** `plan_encounter` with an objective other than "kill them all" (hold the ford, get the wagons through), rated by `rate_encounter`; `search_monster_sources` for soldiers and beasts, `set_npc_statblock` for named veterans.
- **The land:** `annotate_map` the burned villages, contested roads, forage grounds and safe houses, hidden until shown. Evidence of a betrayal is a `stage_secret` aimed at the character with the most to lose from it.
- Finish with `get_changeset`, recap the draft in plain words, ask the DM, then `request_approval`.

## References

- Read [references/beats.md](references/beats.md) when outlining an arc, a session or a scene built on scarcity and cost.
- Read [references/npcs.md](references/npcs.md) when creating allies, mercenaries, officers, healers or anyone the party might need and distrust.
- Read [references/encounters.md](references/encounters.md) when designing battles, negotiations, tribunals, forages or logistics problems.
- Read [references/factions.md](references/factions.md) when building warring powers, companies, churches, cartels or the people caught between them.
- Read [references/lore.md](references/lore.md) when describing a land at war, naming people and places, or writing ledgers, orders and letters.
- Read [references/pitfalls.md](references/pitfalls.md) when reviewing a draft or when the DM says the campaign feels bleak without being meaningful.
- Read [references/safety.md](references/safety.md) before drafting atrocity, torture, sexual violence, slavery, starvation or harm to children, and whenever `get_table_safety` returns limits.

# Grimdark: Encounters

Grimdark encounters are about what the party can afford to lose. Every fight spends resources, every negotiation spends trust, every journey spends time. Design each encounter around an objective and its costs, not around killing everything. QuestMaster rates the fights (`rate_encounter`); this file decides what they mean.

## Principles

- **Objectives, not body counts.** Hold the bridge until the wagons cross. Get the healer out. Take the grain without burning it.
- **Fights are expensive even when won.** Wounds need medicine, arrows need replacing, the dead need burying. State what a win will cost.
- **Enemies are people.** They surrender, flee, beg, bargain and switch sides. Morale breaks before hit points run out.
- **Every encounter has an out.** Retreat, pay, surrender, trade, abandon the objective. Each costs something specific.
- **Fewer, heavier fights.** One battle that matters per session beats three that do not.

## Combat situations

### Hold the ford
- **Objective:** keep the crossing until the refugees' carts are over. Count carts, not rounds.
- **Stakes:** each cart that does not cross is a family left behind.
- **Complications:** a cart overturns mid-river; the enemy captain offers to let the women and children cross if the soldiers surrender; the party's mercenary allies want to fall back early.
- **Outs:** burn the ford behind the last cart (and strand the stragglers); negotiate a truce at the price of the company's horses; hold to the last and lose someone named.

### The forage raid
- **Objective:** take a farm's winter stores for the starving town.
- **Stakes:** the town eats; the farm's family does not.
- **Complications:** the farmer's sons are armed; another army's foragers arrive at the same time; the farmer offers half if the party will protect him from the other army.
- **Outs:** take it all; take half and leave a promise; leave with nothing and find another farm, a day later and hungrier.

### The ambush that goes wrong
- **Objective:** intercept an enemy supply wagon.
- **Complications:** the wagon carries prisoners, not supplies, and some of them are from the party's side; the escort is conscripted farmhands who want to surrender.
- **Outs:** free the prisoners and lose the element of surprise for the next job; take the wagon and leave the prisoners; take the escort prisoner and feed them out of the party's stores.

### Morale and surrender
- When an enemy group loses a third of its number or its leader, its morale is tested (the DM decides how). On a break, they flee, surrender or offer terms.
- Prisoners are a scarcity problem: they eat, they need guards, they know things. Releasing them, keeping them and killing them are all choices with consequences.

## Social situations

### The negotiation where everyone lies
- **Setup:** three parties, one resource. Each side has a public demand, a real minimum and one thing it is hiding.
- **Stakes:** the deal, and who gets blamed when it breaks.
- **Structure:** run it in rounds. Each round, one hidden thing can be exposed by the party, and exposing it changes everyone's minimum.
- **Outs:** a deal that leaves someone out; no deal, and a fight later; a deal the party knows will break, signed anyway to buy time.

### The tribunal
- **Setup:** someone the party knows is on trial (a deserter, a thief, a collaborator) and the verdict is predetermined unless something changes.
- **Stakes:** a life, and the party's standing with the court.
- **Complications:** the accused is guilty, of something; the judge needs a guilty verdict to keep order; a witness can be bought.
- **Outs:** testify and be marked as sympathizers; bribe the witness; break the accused out and become outlaws; let it happen and live with it.

### The requisition
- **Setup:** an officer with a writ arrives to take the party's horses, food or people for the war.
- **Outs:** comply, bribe, fight, forge a counter-writ, or offer something the officer wants more.

## Exploration situations

### The winter road
- **Stakes:** time and supplies. Each day on the road costs rations and risks exhaustion.
- **Complications:** a broken bridge (detour two days or ford it in ice water); refugees ask to travel with the party; a burned inn with something worth looting and someone guarding it.
- Track the journey in days and resources, not encounters. Every day has one choice.
- Use `annotate_map` to mark burned villages, safe barns and the places armies forage, hidden until the party learns them.

### The ruined village
- **Stakes:** supplies, information and a survivor who needs help.
- **Complications:** the village was burned by the party's own side; the survivor knows who gave the order; another group is already picking it over.
- **Outs:** take what they can and go; bury the dead and lose a day; take the survivor and gain a mouth to feed and a witness.

## Puzzle situations

- **Logistics.** Forty refugees, eleven days of food, six days to the coast if the road is clear and nine if it is not. The puzzle is who walks, who rides, who is left, and what can be bartered on the way. Let the players solve it; there is no clean answer.
- **The ledger.** A quartermaster's books do not balance. The missing stores are the clue to who is feeding the enemy, or the orphans.
- **The siege.** Water, walls, morale, food. Each turn, the party fixes one and another gets worse. The puzzle is what to let fail.
- Every puzzle has a brute-force out (seize the stores, hang the thief, break the siege by sortie) that solves it and creates a worse problem.

## Escalation

1. **The count drops.** A resource falls faster than expected.
2. **The ally asks.** A compromised ally raises their price.
3. **The faction moves.** A rival takes something the party was counting on.
4. **The innocents arrive.** People the party cannot easily refuse need the same thing.
5. **The choice.** Only one of two things can be saved, and both have names.

## Building it in QuestMaster

- `plan_encounter` with the objective and its costs written into the encounter's DM context; `propose_encounter` or `rate_encounter` for difficulty.
- `search_monster_sources` for soldiers, bandits and wolves; `set_npc_statblock` for named veterans and captains.
- `build_cue_list` for a battle's turning points (the cart overturns, the truce flag goes up) so the DM can fire them as the fight unfolds.

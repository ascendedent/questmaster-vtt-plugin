# War Campaign: Factions

In a war, every faction fights two wars: the one against the enemy, and the one over what the peace will look like. Each archetype has a public face (`publicMission`), a real agenda (the DM-only `realAgenda`), a method, and the factions it collides with. Run `search_campaign` first and extend the factions that already exist.

## The high command
- **Public face:** the realm's defenders, united behind the crown.
- **Real agenda:** three generals competing for credit; each wants the victories on their front and the defeats on someone else's.
- **Method:** reserves withheld, dispatches delayed, glory claimed in the broadsheets.
- **Collides with:** the prince at the front; the mercenary companies (hired by the wrong general).
- **Hook:** two generals give the party contradictory orders on the same morning.

## The invader
- **Public face:** liberators, avengers or a holy army, depending on the proclamation.
- **Real agenda:** something concrete and limited (a port, a river valley, revenge on one house) that a clever party could offer without a full conquest.
- **Method:** terror where resisted, generosity where welcomed, both on purpose.
- **Collides with:** the partisans; the neutral power, which wants the invader exhausted.
- **Hook:** an enemy envoy hints at exactly what would end the war, and it is something the party's own side refuses to give.

## The mercenary companies
- **Public face:** professionals for hire, loyal to the contract.
- **Real agenda:** the war must last; a quick victory ends the pay.
- **Method:** careful battles, negotiated retreats, captured nobles ransomed back to both sides.
- **Collides with:** the high command (late pay); the partisans (who hate hired swords).
- **Hook:** a company offers to switch sides for a sum the party could actually raise.

## The order of mercy
- **Public face:** healers who tend the wounded of both sides under sacred neutrality.
- **Real agenda:** their hospitals are the only places both sides meet, and the order carries messages for both. A faction inside wants to choose a side.
- **Method:** hospitals as embassies; truces brokered over beds.
- **Collides with:** whichever army loses a secret through them.
- **Hook:** a healer asks the party to escort a "patient" who is an enemy colonel wanting to defect.

## The partisans
- **Public face:** patriots resisting occupation.
- **Real agenda:** split between those who want the old lords back and those who want no lords at all, and both want the other gone after the war.
- **Method:** ambush, sabotage, and the reprisals those bring down on villages.
- **Collides with:** the invader; the high command, which wants them under its orders.
- **Hook:** the partisans ask for help with an ambush that will certainly bring reprisals on a village the party has protected.

## The merchant houses
- **Public face:** patriotic lenders financing the defense.
- **Real agenda:** they hold the war debt; whoever wins owes them, so they lend to both through cousins.
- **Method:** loans with conditions, grain held back to raise prices, insurance on caravans.
- **Collides with:** the quartermasters; the refugee assembly (whose land they want).
- **Hook:** a loan the realm desperately needs comes with a clause the party is asked to deliver: a border town as collateral.

## The refugee assembly
- **Public face:** displaced people asking only for passage.
- **Real agenda:** carve out a neutral territory that both armies agree to leave alone.
- **Method:** negotiation, information traded for safety, a growing militia of their own.
- **Collides with:** every army that wants their roads; the merchant houses that want their valley.
- **Hook:** the assembly will share what they saw on the enemy's roads in exchange for the party's word to back their claim at the peace table.

## The neutral power
- **Public face:** a concerned neighbor offering mediation.
- **Real agenda:** both sides exhausted, and one border province quietly annexed at the peace.
- **Method:** spies, loans, a mediator with a carefully balanced reputation.
- **Collides with:** everyone, eventually.
- **Hook:** the mediator's offer of peace is genuine, and it costs the province where a character was born.

## How they collide

- **Alliance clocks:** every coalition gets a 4-segment clock of its own. Missions can repair it (a shared victory) or strain it (a broken promise, reserves withheld). When it fills, an ally walks.
- **Every lever touches a faction:** each mission should help one faction and annoy another. Write both on the mission.
- **The peace table:** as the war nears an end, every faction's real agenda surfaces at once. Plan a peace conference as its own arc, with factions as the fronts.

## Building factions in QuestMaster

- `upsert_faction` for each side and power, with the war aims they announce as `publicMission` and what they want from the peace as `realAgenda`.
- One `upsert_npc` per faction as its face, tied to the front where the party meets them.
- Alliance clocks are `upsert_thread` records with urgency; schedule the moment an ally would walk.
- A faction's real agenda surfacing is a `stage_secret` aimed at the character best placed to overhear it.

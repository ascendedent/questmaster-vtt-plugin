# Grimdark: Factions

Grimdark factions are all partly right and all guilty of something. The party should be able to argue for any of them, and should find in each a deed they cannot forgive. Factions control scarce things (grain, roads, medicine, law), and their collisions are what make the scarcity bite.

## How to build one

- **Public face** goes in `publicMission`: the defensible version, the one their own people believe.
- **Real agenda** goes in `realAgenda`: what they actually want, including the indefensible act they have done or will do.
- **Method:** how they get what they want, and what they will spend to get it.
- **What they control:** the scarce resource the party will need from them.
- **Collision:** who they need, and who they are already at war with.
- Three or four factions are enough for an arc. Each one should hold something the party needs.

## Archetypes

### The mercenary company
- **Public face:** professionals. They keep contracts, pay their dead's families and do not loot without orders.
- **Real agenda:** survive the war as a company, which means being paid by whoever is winning and "taxing" whoever is not.
- **Method:** contracts written so that every clause favors the company. Villages that do not pay are made examples of.
- **Controls:** swords, horses and the only road that is safe this winter.
- Example: the Brindle Company, two hundred strong, whose banner is a plain brown field because they have changed sides too often to keep a device.

### The crown remnant
- **Public face:** the lawful government, the last order in a broken land.
- **Real agenda:** keep the capital fed and the throne held, by stripping the provinces of grain and men.
- **Method:** writs, conscription, hangings for desertion and hoarding.
- **Controls:** the law, the granaries and the right to pardon.
- **Indefensible act:** last autumn's requisitions emptied the eastern villages; the famine now is the crown's doing.

### The faith that feeds
- **Public face:** a church running soup kitchens, orphanages and hospitals.
- **Real agenda:** grow the faith while the crown fails, and buy the loyalty of the starving with bread.
- **Method:** charity with conditions. Converts eat first. Heretics are reported to the crown, or burned by the church's own wardens.
- **Controls:** the only functioning hospitals and a hidden grain reserve.

### The rebels
- **Public face:** liberators, the people's army, against the crown's cruelty.
- **Real agenda:** half of them want justice; the other half want to be the new lords. The leaders have not decided which half they are.
- **Method:** ambush, sabotage, and executing collaborators, a word that grows wider every month.
- **Controls:** the hills, the night roads, and the loyalty of burned-out villages.
- **Indefensible act:** they hanged a village's reeve and his family for paying the crown's tax under threat.

### The merchant cartel
- **Public face:** traders keeping commerce alive in hard times.
- **Real agenda:** profit from the war, and prolong it when peace would cost them.
- **Method:** loans to all sides, hoarding, price-fixing, and quiet payments to whoever is about to win.
- **Controls:** salt, medicine, debt and the river barges.

### The bandit-lord's free holding
- **Public face:** a bandit, a thief, a murderer. His people call him a lord who actually protects them.
- **Real agenda:** carve out a holding of his own, and get it recognized before the war ends.
- **Method:** tolls, raids on the armies' supply lines, and fierce loyalty to anyone under his protection.
- **Controls:** a ford, a depot, and a valley that is the only peaceful place in the province.
- Example: Hesk of the Ford, who hangs thieves from his own band and feeds any refugee who swears to him.

### The refugees' commons
- **Public face:** nobody. They are the people the war happened to.
- **Real agenda:** survive together, and they will do anything to anyone outside the group to manage it.
- **Method:** numbers, desperation, a prophet or an elected headwoman, and theft when it is needed.
- **Controls:** labor, numbers, and the sympathy of anyone who still has some.

### The plague wardens
- **Public face:** physicians and soldiers holding a quarantine line.
- **Real agenda:** keep the fever out of the capital at any cost, including the people on the wrong side of the line.
- **Method:** walls, burning, and the order to shoot anyone who crosses at night.
- **Controls:** the only cure, which they are keeping for the capital.

## Collisions

Use these to generate the middle of an arc:
- **Company vs. rebels:** the company is paid to hunt rebels and is quietly selling them arrows.
- **Crown vs. faith:** the crown wants the church's grain; the church wants a royal pardon for its wardens' burnings.
- **Cartel vs. everyone:** the cartel's barges carry food to whoever pays most, and the town that pays most is not the one starving.
- **Bandit-lord vs. crown:** Hesk will deliver the rebel leaders for a title, and the rebels are the people who sheltered the party.
- **Wardens vs. refugees:** the quarantine line runs through the refugees' camp, and the cure is on the other side.

## Faction clocks

Each faction advances one step per session if the party does nothing:
- The crown: issues a writ, sends a requisition, hangs a hoarder, burns a village.
- The rebels: strike a depot, name a collaborator, execute them, take a town.
- The cartel: buy up stock, raise prices, call in a debt, switch sides.
Store each clock as an `upsert_thread` with urgency, and draft the next step as an `upsert_session_beat` so the DM sees it coming.

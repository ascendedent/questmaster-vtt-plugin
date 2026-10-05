# Wilderness Hexcrawl: factions

In the wild, factions are spread thin and far apart, so they collide over the few things that matter: routes, water, title to land and who gets to draw the map. Give each faction a place on the map (a fort, a camp, a monastery) and a reason to care where the party goes next.

## How to use these

- Pick 3 to 5. Put each one's base in a different region so the map itself shows the politics.
- Draft each with `upsert_faction`: `publicMission` is what travelers hear, `realAgenda` (DM-only) is what it does. Set partyStanding and update it as expeditions return.
- Every faction should want the party's maps for a different reason. That is the hook that survives any route the players choose.

## Archetypes

### The chartered company
- **Public face:** brings roads, trade posts and order to the frontier, and pays well for surveys.
- **Real agenda:** a charter clause grants the land to whoever files the first survey. The company buys, steals or forges maps to claim country already lived in.
- **Method:** hires expeditions, funds rivals to race them, and pays waystation keepers for routes.
- **Example:** the Brennock Charter Company, whose seal is a compass rose with one point filed off.

### The herder clans
- **Public face:** keep the old grazing circuits, trade wool and cheese at the summer fair, avoid outsiders.
- **Real agenda:** they have been selling the company bad maps for years to steer surveyors away from the high valleys where the clans winter.
- **Method:** hospitality as intelligence: every guest is fed, questioned and remembered.
- **Example:** the Seven Fires, who mark boundaries with cairns that only make sense from horseback.

### The road wardens
- **Public face:** a sworn company that keeps the main road safe in exchange for tolls.
- **Real agenda:** a share of the bandits on the road are off-duty wardens. Danger keeps tolls high, so the wardens manage it rather than end it.
- **Method:** escorts for hire, a ledger of who paid, and very selective memory.
- **Example:** the Wardens of the Long Mile, who wear grey sashes and never ride alone.

### The lodge of rangers
- **Public face:** keepers of the old forest who guide lost travelers and hunt dangerous beasts.
- **Real agenda:** they are holding something in, not out. The forest is a quarantine around a site they will not explain, and they turn back anyone heading there.
- **Method:** misdirection, false trails, and kindness that always points the wrong way.
- **Example:** the Green Hand, whose members are never seen in groups larger than two.

### The explorers' society
- **Public face:** a learned club that funds scholarship and honors discovery.
- **Real agenda:** members bet heavily on which of them claims a site first, and sabotage is within the rules as long as nobody can prove it.
- **Method:** grants with strings, published accounts that take credit, a rival expedition always two days ahead.
- **Example:** the Society of the Far Lamp, whose medal the party's patron covets.

### The pass monastery
- **Public face:** shelter for any traveler on the high road, free of charge.
- **Real agenda:** the monks record every traveler, cargo and rumor, and sell the ledger each spring to whoever bids most.
- **Method:** hospitality, confession, and a library of every map left behind by guests who never came back.
- **Example:** the House of the Ninth Step, where guests write their names in a book chained to the gate.

### The free settlement
- **Public face:** none. Officially, it does not exist.
- **Real agenda:** escaped debtors and deserters built a village in a hidden valley. They need the frontier to stay unmapped.
- **Method:** child scouts, false smoke signals, a quiet arrangement with the herders.
- **Example:** Lantry's Hollow, which appears on no map and has a mill, a school and a gallows.

## How they collide

- **Company vs herders:** over title. The company needs a survey that ignores the cairns; the herders need a witness who will not. The party's map decides it.
- **Wardens vs company:** the company wants a cheaper road; the wardens want the old one kept dangerous. A new pass discovered by the party threatens the wardens' income.
- **Rangers vs everyone:** they will help the party anywhere except one direction, and the harder the party pushes that way, the stranger the rangers' methods become.
- **Monastery vs free settlement:** the monks' ledger mentions a traveler who went into the hidden valley and came back. Whoever buys the ledger finds Lantry's Hollow.
- **Society vs party:** every discovery the party makes, the society tries to publish first.

## Moving factions between expeditions

- On each return to base, advance one faction a step toward its real agenda and have one react to what the party found. Show it as news: a new fort, a burned cairn, a price on a map.
- Write each move as an `upsert_plot_node` on the faction's arc, linked from the discovery that triggered it with `link_plot_nodes`.
- When a faction's move would close a route or open one, update the region's area description and the affected location's dmNotes so the map stays true.

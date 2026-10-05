# High Fantasy Epic: Factions

Every faction in an epic has a stake in how the prophecy is answered, and most of them have a preferred answer that happens to crown themselves. Each archetype has a public face (`publicMission`), a real agenda (the DM-only `realAgenda`), a method, and its collisions. Run `search_campaign` first and extend what exists.

## The keepers of the word
- **Public face:** guardians of the prophecy, keepers of its true text, servants of fate.
- **Real agenda:** edited the prophecy three hundred years ago to protect a royal line that no longer exists, and now must defend the edit or lose everything.
- **Method:** controlling copies, licensing translations, declaring chosen ones.
- **Collides with:** the unwritten (who want the text destroyed); the archivist's own students.
- **Hook:** a junior keeper smuggles the party an older copy with one word different.

## The elder court
- **Public face:** wise, distant immortals who advise but do not interfere.
- **Real agenda:** they caused the ancient evil in the last age and are hiding it; their non-interference is fear of being found out.
- **Method:** gifts with conditions, riddles instead of answers, envoys who never quite lie.
- **Collides with:** the herald of the enemy, who knows their secret.
- **Hook:** the court offers the party a marvel in exchange for not visiting a certain valley.

## The order of the dawn shield
- **Public face:** knights sworn to protect the realm and the chosen one.
- **Real agenda:** they want the chosen one to be theirs, so the order inherits the victory and the crown's gratitude.
- **Method:** escort, guardianship, a little kidnapping when needed.
- **Collides with:** the rival company; the reluctant chosen, whom they guard like a prisoner.
- **Hook:** a knight asks the party to help their charge escape the order sworn to protect him.

## The congregation of the long night
- **Public face:** a mutual-aid society for those the kingdoms forgot (debtors, lepers, the displaced, veterans).
- **Real agenda:** the ancient enemy's congregation, though most members joined only for the soup and the roof.
- **Method:** charity, belonging, a promise that the coming night will be kinder than the day was.
- **Collides with:** the kingdoms, who would rather burn it than fix what made it grow.
- **Hook:** the party must stop a congregation ritual, and the hall is full of people they would rather feed than fight.

## The crowns
- **Public face:** allied kingdoms standing together against the dark.
- **Real agenda:** each wants to be the realm that survives the war intact, while its neighbors bleed.
- **Method:** late armies, conditional aid, marriages arranged for the age to come.
- **Collides with:** each other; the elder court (whose lands they covet).
- **Hook:** a queen offers the party her army in exchange for being named in the song that will be written.

## The wayfarers
- **Public face:** couriers, guides and road-wardens; friends of every traveler.
- **Real agenda:** they have mapped every hidden path in the world and sell the routes to whoever pays, including the enemy.
- **Method:** waystones, inns, codes chalked on milestones.
- **Collides with:** anyone who wants a road kept secret.
- **Hook:** a wayfarer sells the party a route to the sleeping mountain, and sells the same route to the enemy an hour later.

## The unwritten
- **Public face:** heretics who deny fate.
- **Real agenda:** destroy every copy of the prophecy so no one is ever chosen, or sacrificed, again.
- **Method:** burned libraries, rescued candidates, sermons that destiny is a lie told by the powerful.
- **Collides with:** the keepers; the order of the dawn shield; anyone who needs the prophecy to be true.
- **Hook:** they rescue a candidate the party was protecting, and ask the party to help them disappear.

## How they collide

- **The prophecy is the prize.** Write each faction's preferred answer to each line. When the party leans toward an answer, the factions that lose by it act.
- **Two factions per leg.** Each leg of the journey should feature two factions in tension; the others are rumors and envoys.
- **Make allies uncomfortable.** The best ally has a real agenda the party dislikes and needs anyway.
- **The war after the war.** When the ancient enemy falls, the factions' agendas become the next age's conflict. Seed it before the finale.

## Building factions in QuestMaster

- `upsert_faction` with the role they claim as `publicMission` and the truth (the edit, the cover-up, the price) as `realAgenda`.
- One `upsert_npc` per faction as its face, linked to the faction and to a place on the map.
- A faction's push for its preferred answer is an `upsert_thread` with urgency, linked to the prophecy thread's line nodes on the plot board.
- Discovering a faction's real agenda is a `stage_secret` aimed at the character whose path crosses the evidence.

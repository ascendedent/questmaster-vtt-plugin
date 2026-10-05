# Swashbuckling: Factions

Factions in this genre are loud in public and quiet in private. Each archetype has a public face (QuestMaster's `publicMission`), a real agenda (the DM-only `realAgenda`), a method, and the factions it collides with. Rename and reshape them to fit; run `search_campaign` first so you extend what exists instead of duplicating it.

## The Admiralty
- **Public face:** guardians of the sea lanes, hunters of pirates, servants of the crown.
- **Real agenda:** control the sale of letters of marque, so every privateer pays the Admiralty and every pirate is just a privateer who did not.
- **Method:** public hangings, private pardons, a ledger of who owes them.
- **Collides with:** the Free Compact (open war); the Chartered Company (they share bribes and resent each other).
- **Hook:** an Admiralty clerk offers the party a letter of marque with the target's name left blank.

## The Free Compact
- **Public face:** a terror of the seas; grinning flags, ransoms and raids.
- **Real agenda:** a vote-run commonwealth of ships with written articles, saving to buy an island and declare a free port.
- **Method:** fear as theater (they rarely kill; the reputation does the work), equal shares, elected captains.
- **Collides with:** the Admiralty; the Exiled Court, which has promised the Compact's island to someone else.
- **Hook:** the Compact needs an outsider to count the ballots in a disputed captain's election.

## The Chartered Company
- **Public face:** commerce, civilization, honest weights and warm warehouses.
- **Real agenda:** piracy keeps insurance premiums high and justifies the Company's private warships, so it quietly sells the Compact its rivals' routes.
- **Method:** contracts, debt, insurance, hired blades who never wear Company colors.
- **Collides with:** the Harbor Guilds over wages; the Admiralty over who rules the sea.
- **Hook:** the party is hired to guard a cargo the Company wants stolen for the insurance.

## The Fencing Schools
- **Public face:** sport and etiquette for the well-born.
- **Real agenda:** each school is a political party in disguise; court votes are settled by duels between their champions.
- **Method:** challenges, students placed as bodyguards, gossip gathered in the changing rooms.
- **Collides with:** each other, constantly; the Masked League, which humiliates their patrons.
- **Hook:** a school offers a character free training in exchange for one future duel, at a time and place of its choosing.

## The Masked League
- **Public face:** anonymous defenders of the poor who rob tax wagons and free debtors.
- **Real agenda:** split in two. Half want the debt laws reformed; half want revenge on one family and will burn a district to get it.
- **Method:** pamphlets, midnight rescues, theatrical robberies, a printing press that moves every week.
- **Collides with:** the Fencing Schools, the city watch, and itself.
- **Hook:** both halves ask the party for the same favor for opposite reasons.

## The Harbor Guilds
- **Public face:** honest dockworkers, pilots and chandlers.
- **Real agenda:** they decide which ships unload and which rot at anchor; a slowdown can starve the city in nine days.
- **Method:** lost paperwork, slow cranes, a pilot who runs a ship aground very politely.
- **Collides with:** the Chartered Company; anyone who hires labor from outside the guild.
- **Hook:** a pilot will not bring the party's ship in until they settle a guild grievance.

## The Exiled Court
- **Public face:** a gracious royal household in exile, hosting the best parties in port.
- **Real agenda:** retake a throne across the sea with pirate gold and a borrowed fleet.
- **Method:** titles, promised lands, marriages arranged for leverage, letters sealed with a crown they no longer hold.
- **Collides with:** the Admiralty (treason); the Free Compact (whose island they have promised away).
- **Hook:** the pretender offers a character a knighthood that becomes real only if the restoration succeeds.

## How they collide

- Every set piece should touch the interests of at least two factions, so its outcome tilts something beyond the party.
- Give each active faction one public move per session the DM can show as a broadsheet headline, a toast or a rumor in the breath scene.
- When the party openly helps one faction, another sends a rival. Write who, and what code they carry.
- Collisions to offer the DM:
  - The Admiralty hangs a Compact captain; the Compact kidnaps the Admiral's nephew; both hire the party within the same day.
  - The Guilds strike; the Company hires the party to break the strike; the Masked League asks them to protect the strikers.
  - The Exiled Court throws a masquerade, every faction sends someone, and one guest will be dead by midnight.

## Faction pressure between sessions

- Pick the two factions the party touched most and move each one step: a new hire, a public humiliation, a ship seized, a debt called in.
- Show the step through a person, not a summary: the clerk who now refuses to meet their eyes, the pilot who waves them in early.
- If a faction's real agenda is about to surface, plant one clue the next session.

## Building factions in QuestMaster

- `upsert_faction` with the public face as `publicMission` and the real agenda as `realAgenda`.
- Give each faction a face: one `upsert_npc` linked to it, ideally a rival with an honor code.
- A faction's running scheme is an `upsert_thread` with urgency; the party learning the real agenda is a `stage_secret` aimed at the character with the right contacts or the right enemies.

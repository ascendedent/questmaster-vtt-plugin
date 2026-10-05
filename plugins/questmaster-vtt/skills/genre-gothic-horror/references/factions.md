# Gothic Horror: Factions

In gothic horror, factions are small and close: a family, a household, a parish, a village council. Their power is not armies but silence, money, land and memory. Every faction below either profits from the curse, fears it, or wants it for itself.

## How to build one

- **Public face** goes in `publicMission`: what the village says about them.
- **Real agenda** goes in `realAgenda`: what they do when nobody is looking, and how it touches the curse.
- **Method:** how they get what they want without anyone raising a voice.
- **Collision:** which other faction they need, and which one could ruin them.
- Two or three factions are enough for an arc. Every one should have something the party wants.

## Archetypes

### The family
- **Public face:** benefactors. They pay for the bridge, the school and the harvest festival.
- **Real agenda:** keep the curse fed and the fortune intact, while each member privately looks for a way to be the one who escapes it.
- **Method:** hospitality as control. Guests are flattered, fed, given rooms near the family and far from the exits.
- **Weak point:** they are not united. Find the member who wants out.
- Example: the Ashlades of Harrowmoor, wool and slate money, a chapel bigger than the village church.

### The household staff
- **Public face:** loyal servants, some of them third generation.
- **Real agenda:** protect the house and each other. They know more than the family thinks and less than the family fears.
- **Method:** small obstructions. Keys mislaid, messages delayed, a guest's room moved to the cold wing.
- **Weak point:** one of them was hurt by the family and has been waiting for an ally.

### The parish
- **Public face:** comfort, burial, the bell rung for every death.
- **Real agenda:** hold the family's sins in a ledger, which keeps the church funded and the priest safe.
- **Method:** absolution offered on conditions; records kept and selectively lost.
- **Weak point:** faith. The priest believes, and a true believer can be shamed into acting.
- Example: the Chapel of the Quiet Bell, whose bell has not been rung for a third daughter in sixty years.

### The village council
- **Public face:** grateful tenants, plain people.
- **Real agenda:** complicit. They chose, long ago, that the curse is cheaper than poverty, and they choose again every generation.
- **Method:** the vote. They will decide together, in a closed room, whether the party is a guest or a threat.
- **Weak point:** someone on the council lost a child to the bargain and voted for it anyway. That guilt is a door.

### The hunters' lodge
- **Public face:** protectors. They kill wolves, and worse things, for a fee.
- **Real agenda:** collect trophies, which are sometimes the afflicted and sometimes their innocent relatives. They profit when the curse spreads.
- **Method:** fear. A rumor of a beast in the woods doubles their fee.
- **Weak point:** their founder was once afflicted and cured; proof of that would destroy them.

### The learned society
- **Public face:** physicians and natural philosophers studying the region's "remarkable longevity".
- **Real agenda:** reproduce the curse in a form they can sell to rich patrons in the city.
- **Method:** subscriptions, specimens, polite letters asking to examine the family crypt.
- **Weak point:** they need a living subject, and they have started asking about the party.

### The rival house
- **Public face:** neighbors, suitors, old friends of the family.
- **Real agenda:** transfer the curse onto the family completely, or take the bargain for themselves.
- **Method:** marriage. A betrothal binds two families, and the curse follows the blood.
- **Weak point:** they do not fully understand what they are asking for.

### The dead
- **Public face:** none. They are the dead.
- **Real agenda:** some want rest, some want revenge, a few want to be remembered more than either.
- **Method:** pressure on the living through the house itself: cold, sound, dreams, the slow rearrangement of rooms.
- **Weak point:** they keep promises, and can be bound by them.

## Collisions

Gothic factions collide quietly. Use these pairings to generate an arc's middle:
- **Family vs. staff:** the housekeeper hides the family's next victim; the family dismisses her; she takes the keys with her.
- **Parish vs. council:** the priest's ledger proves the council chose every victim; the council needs it burned.
- **Hunters vs. family:** the hunters want the patriarch's head; the family pays them to hunt something else instead, and that something else is innocent.
- **Learned society vs. the dead:** the society digs up a grave for study and releases a ghost who wants the family, not the scholars.
- **Rival house vs. family:** a betrothal is the battlefield, and the bride or groom is the only person who does not know.

## Faction clocks

Give each faction a thing it will do if the party does nothing, one step per session:
- The family: chooses the next payment, prepares it, delivers it.
- The council: hears a rumor, meets in private, votes to remove the party.
- The hunters: arrive, find a scapegoat, burn the wrong house.
Store each clock as an `upsert_thread` with urgency, scheduled to the session it lands in.

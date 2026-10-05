# Fey Fairytale: factions

Fey factions are courts, circles and old agreements. They rarely fight openly; they compete through bargains, guests, gifts and wagers, and they use mortals as pieces because mortals are not bound by fey rules. Mortal factions in this genre are defined by how they trade with or ward against the fey.

## How to use these

- Pick 2 fey factions and 1 or 2 mortal ones. Give the two fey factions a feud with a specific origin (a stolen guest, a broken betrothal, a wager over a mortal).
- Draft each with `upsert_faction`: the courtesy they show the world is `publicMission`; what they want from mortals is `realAgenda`.
- Every fey faction should have one rule it must obey as a body (cannot act in daylight, must accept any duel, cannot refuse a mortal's gift) and it should be learnable.

## Archetypes

### The Court of Long Evening
- **Public face:** gracious hosts of the twilight halls, patrons of music and mortal artists.
- **Real agenda:** they feed on mortal grief, and cultivate tragic artists the way gardeners grow roses.
- **Method:** patronage with terms, gifts of talent that cost a loved one, invitations to revels.
- **Rule:** must grant sanctuary to any mortal who arrives weeping.
- **Collides with:** the Hollow Court, over a mortal composer both claim.

### The Hollow Court
- **Public face:** the old powers under the hills, strict and fair, keepers of the boundaries.
- **Real agenda:** reclaim land lost to mortal farms, field by field, through lapsed bargains.
- **Method:** contracts with village founders, collected generations later.
- **Rule:** cannot act except through a written or spoken contract.
- **Collides with:** the church and the border villages, over the deeds to the land.

### The Riding
- **Public face:** a procession seen on certain nights, horns and lanterns across the moor. Best not to look.
- **Real agenda:** hunt down oath-breakers of any kind, fey or mortal, and they are not careful about whose oath.
- **Method:** chase, capture, judgment at dawn.
- **Rule:** cannot cross running water; must release any quarry who answers their challenge in verse.
- **Collides with:** everyone, since everyone has broken something.

### The Moonlit Fair
- **Public face:** a market that appears at crossroads three nights a year, selling wonders.
- **Real agenda:** trade in things that cannot normally be sold: years, voices, luck, a first kiss. The traders take the price and keep it.
- **Method:** fair-seeming prices with fine print; credit offered freely.
- **Rule:** no violence within the fair's lanterns; every sale must be agreed aloud.
- **Collides with:** the border witches, who buy back what desperate villagers sold.

### The border witches
- **Public face:** midwives, herbalists and charm-sellers in the villages near the woods.
- **Real agenda:** keep the worst bargains from being made by making them first, and keep a register of every debt owed to the fey in the district.
- **Method:** charms, warnings, intervention, and bargains of their own at terrible prices.
- **Collides with:** the church (who call them collaborators) and the Moonlit Fair (whose trade they undercut).

### The bell-keepers
- **Public face:** a religious order that rings bells against the fey at dusk and blesses thresholds.
- **Real agenda:** the order's founder made a bargain to protect the region, and the order's bells are the price being paid, not a defense. Stop ringing, and the debt falls due.
- **Method:** bells, salt, iron, sermons, and burning anything that smells of glamour.
- **Collides with:** the witches; and, unknowingly, with the Hollow Court they are paying.

### The changeling network
- **Public face:** none. Its members live as ordinary people.
- **Real agenda:** protect each other from exposure and from being recalled by the courts.
- **Method:** forged baptism records, a code of knocks, mutual favors.
- **Collides with:** the bell-keepers, who hunt them, and the courts, who want them back.

## Collision patterns

- **The proxy contest:** two courts each sponsor a mortal (one may be a party member) in a wager. The prize is a valley, a voice or a person.
- **The lapsed deed:** an old founder's bargain expires, and the court reclaims a mill, a road or a family's luck. The witches try to renegotiate; the church tries to fight.
- **The sold thing:** a villager sold something at the fair (their voice, their child's luck) and now the witches, the church and the fair all want the party to fix it their way.
- **The hidden payment:** a mortal faction is paying a fey debt without knowing it. Revealing it unbalances everything.

## Moving factions between sessions

- Each court makes one move through a bargain, a guest or a gift, never an open attack.
- Write each move as an `upsert_plot_node` linked from what the party did with `link_plot_nodes`, and update the faction's partyStanding.
- Each mortal faction reacts to the court's move, often by asking the party to fix it in a way that helps them.

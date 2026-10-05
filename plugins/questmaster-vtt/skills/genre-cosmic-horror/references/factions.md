# Cosmic Horror: Factions

Cosmic horror factions are humans organized around something they cannot fully understand. Some want to open the door, some want to keep it shut, some want to sell the key. None of them has the whole picture, and all of them are partly right. The thing itself is never a faction; it has no agenda the party could negotiate with directly.

## How to build one

- **Public face** goes in `publicMission`: what it looks like from outside, usually harmless or admirable.
- **Real agenda** goes in `realAgenda`: what they actually want from the edge.
- **Method:** how they work, and what they are willing to spend.
- **What they know:** one true piece of the picture, and one wrong belief they act on.
- **Collision:** which faction they need, and which one would destroy them.

## Archetypes

### The cult
- **Public face:** a mutual aid society. Free bread on market day, a burial fund, a choir.
- **Real agenda:** open the door, because they believe what comes through will end suffering. Some believe it will end them too and have made peace with that.
- **Method:** kindness to the desperate, then small rites, then large ones. Recruits are never lied to; they are told the truth slowly.
- **What they know:** the rite works. **Wrong belief:** that it will be merciful.
- Example: the Ninefold Choir of Ebbing Cross, who sing at every funeral and never sing the last verse in public.

### The learned institution
- **Public face:** a university, a guild of mapmakers, a royal society. Respectable, old, well-funded.
- **Real agenda:** preserve and study the knowledge, which in practice means keeping it alive and growing. A few senior members are feeding it on purpose.
- **Method:** grants, commissions, expeditions, sealed archives. Inconvenient researchers are given promotions far away.
- **What they know:** more than anyone else. **Wrong belief:** that studying it is neutral.

### The suppression office
- **Public face:** customs inspectors, a sanitation board, a minor department of the crown.
- **Real agenda:** contain it by any means. Burn the books, quarantine the town, silence the witnesses, sometimes permanently.
- **Method:** paperwork and fire. They are thorough and almost never wrong about the danger.
- **What they know:** how bad it gets. **Wrong belief:** that everyone who has touched it is lost.
- Collision: they will treat the party as contaminated once the party carries a mark.

### The town with a custom
- **Public face:** a quiet, odd, insular village with charming festivals.
- **Real agenda:** keep the bargain or the custom that holds it back. They are the only faction succeeding, at a terrible local cost.
- **Method:** tradition, marriage, silence, and the occasional disappearance of an outsider who asked too much.
- **What they know:** exactly what keeps it asleep. **Wrong belief:** that the custom will hold forever.

### The rival cult
- **Public face:** a reform movement, a new church, a secret society of the young and angry.
- **Real agenda:** wake something different, or wake the same thing for a different purpose.
- **Method:** stealing the first cult's rites and texts; recruiting its disillusioned.
- **Collision:** the party can play the cults against each other, and both will try to use the party.

### The profiteers
- **Public face:** antiquarians, collectors, a respectable auction house.
- **Real agenda:** sell fragments (pages, idols, maps) to the highest bidder, with no interest in what happens next.
- **Method:** money, forgery, discretion. Their catalogue is a list of every dangerous object in the region.
- **What they know:** where everything is. **Wrong belief:** that selling it does not count as using it.

### The small faith
- **Public face:** an ordinary parish, a roadside shrine, a lay order of nurses.
- **Real agenda:** none beyond their ordinary work, which turns out to hold something back, slightly.
- **Method:** prayers, wards, care for the marked.
- **Why they matter:** they are the party's best ally and the most fragile one. Losing them is a defeat the party feels.

## Collisions

Use these to drive the middle of an arc:
- **Cult vs. town:** the cult needs the custom broken; the town needs it kept. The party's investigation is what breaks it.
- **Institution vs. suppression office:** the office wants the archive burned; the institution wants the party to help move it.
- **Profiteers vs. everyone:** the auction is in three days, and every faction is bidding for the same book.
- **Suppression office vs. party:** once a character carries a mark, the office sees a contaminated asset, not an ally.
- **Small faith vs. cult:** the cult feeds the same poor the parish feeds, and some parishioners have started going to both.

## Faction clocks

Each faction advances one step per session if the party does nothing:
- The cult: recruits, gathers a component, performs a minor rite, prepares the major rite.
- The suppression office: arrives, quarantines, burns, silences.
- The profiteers: acquire, advertise, auction, deliver.
Store each as an `upsert_thread` with urgency, and draft the step that lands next session as an `upsert_session_beat` so the DM sees it coming.

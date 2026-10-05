# Dungeon Crawl: NPCs

In a dungeon, every NPC is a source of information and a reason to talk instead of fight. Give each one a stake in the layout: a room they guard, a route they know, a door they want opened or kept shut.

## How to use these

- Seed 1 or 2 talkers per level, plus faction leaders. Monsters that can talk count.
- Draft each with `upsert_npc`, linked to their faction and their lair room (a location). Twist in `secret`, tell in their notes. Give the ones who might fight a `set_npc_statblock` so QuestMaster computes their numbers.
- Every NPC knows one route the party does not. That knowledge is the currency.

## Archetypes

### The torchbearer who knows too much
- **Twist:** the cheap local hire grew up inside the dungeon's top level and ran away at twelve. She knows the old shortcuts and is terrified of being recognized by the faction that raised her.
- **Want:** wages, and never to go below the second stair.
- **Fear:** a particular whistle she hears in the walls.
- **Tell:** takes the left fork before anyone asks, then pretends she guessed.
- Example: Dilly Fairweather, fourteen, who carries the torch too high, like someone used to low ceilings.

### The freelancing envoy
- **Twist:** comes to negotiate on behalf of his faction, which has no idea he is here. He is trying to stop a war his side would lose.
- **Want:** a truce he can present as his chief's idea.
- **Fear:** his chief finding out before the truce is signed.
- **Tell:** keeps glancing back the way he came, and keeps his voice lower than the room needs.

### The delver who never left
- **Twist:** not trapped. He found a safe room with a working door years ago and lives by selling directions to whoever pays, monster or adventurer.
- **Want:** to keep the arrangement exactly as it is.
- **Fear:** anything that changes the balance of the factions.
- **Tell:** offers food before anyone asks, and charges for it later.

### The caretaker
- **Twist:** still sweeping halls, lighting lamps and logging visitors for builders dead two centuries. Bound by duty, not magic, and lonely.
- **Want:** someone with authority to report to.
- **Fear:** being told the job is over.
- **Tell:** quietly sets right whatever the party knocks over and notes it in a book.
- Use: treat them as an employee and you get a guided tour; insult the dead masters and the doors stop opening.

### The merchant of the deep
- **Twist:** runs a stall on neutral ground with credit for everyone. Collects on the way out, and has a debt ledger covering every faction in the place.
- **Want:** neutral ground to stay neutral.
- **Fear:** one faction winning outright.
- **Tell:** quotes prices in candles, never coin.

### The prisoner who wants to stay
- **Twist:** taken by a faction a year ago, now its translator and the closest thing it has to a diplomat. "Rescue" is a kidnapping from her point of view.
- **Want:** recognition, and a letter delivered to her family.
- **Fear:** being dragged home to a life she had outgrown.
- **Tell:** uses the faction's word for "we".

### The rival delver
- **Twist:** has a map of level 3 and no way past level 2. Offers a partnership, and will betray the party only if they betray her first.
- **Want:** the heart's treasure, for a sick sibling's cure.
- **Fear:** being the last of her crew alive.
- **Tell:** shares her map in halves, one half per promise kept.

### The mapmaker
- **Twist:** sells maps of the dungeon in town, accurate except for one deliberate error per map, to protect his own private route.
- **Want:** steady customers who come back alive enough to buy level 2.
- **Fear:** a customer who survives the error and returns to ask about it.
- **Tell:** won't meet anyone's eyes when they point at one particular corridor.

### The captive beast
- **Twist:** chained in a pit as a guard or a power source, it is intelligent and it remembers the builders. It knows why the place was sealed.
- **Want:** out, and the light kept away from its eyes.
- **Fear:** the faction that feeds it deciding it is no longer worth feeding.
- **Tell:** answers questions only in the voice of the last person who spoke to it.

### The boss with a reason
- **Twist:** the warlord at the bottom is not hoarding; it is holding a door shut against something worse, and its raids on the surface are for supplies to keep holding it.
- **Want:** reinforcements, or someone else to take the watch.
- **Fear:** the door, more than death.
- **Tell:** fights with its back to the same wall every time, and never lets the party past it.

### The builder's heir
- **Twist:** arrives from outside with a legal claim to everything inside, and hires the party, but secretly wants the dungeon kept sealed so the family's crime stays buried.
- **Want:** proof that nothing in there can embarrass the family, or that nobody else will ever get in.
- **Fear:** the records room.
- **Tell:** asks more about what the party read than what they carried out.

### The guardian with old orders
- **Twist:** a talking statue, door or construct bound to its maker's orders to the letter. The orders are centuries out of date and can be argued with using the maker's own rules.
- **Want:** a valid instruction.
- **Fear:** contradiction (it freezes for a turn when given one).
- **Tell:** recites its standing orders verbatim whenever challenged, including clauses that no longer make sense.

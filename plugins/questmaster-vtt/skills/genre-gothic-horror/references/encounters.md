# Gothic Horror: Encounters

Gothic encounters are situations, not set pieces. Each one has stakes (what is lost if the party does nothing), complications (what the house does when they act) and outs (ways to end it that are not "kill everything"). The difficulty numbers come from QuestMaster (`rate_encounter`); this file is about what the encounter means.

## Principles

- **Fight the place, not just the monster.** Every gothic fight has a terrain feature that matters more than the enemy's hit points: a staircase, a burning gallery, a flooded crypt, a chandelier, a mirror.
- **The monster should be able to leave.** A monster that can retreat, return and remember is scarier than one that fights to the death.
- **Every fight has a talk option.** The monster, the ghost or the family member can be reasoned with at a price. Put the price on the table.
- **Fewer, heavier encounters.** One real fight per session is plenty. The rest of the time is dread, which is cheaper and works better.

## Combat situations

### The thing in the crypt
- **Stakes:** a captive (a servant, a sibling) is being drained or drowned; every round costs them.
- **Complications:** candles gutter one by one (each round, a zone goes dark); the coffins are full and some of the occupants stir when touched.
- **Outs:** carry the captive out and seal the door; offer the monster the name it lost; destroy the shrine that binds it here instead of the monster itself.
- **Escalate:** the crypt door swings shut and the family is on the other side, choosing whether to open it.

### The wedding feast
- **Stakes:** the bride is the curse's next payment and the vows are the trigger.
- **Complications:** forty innocent guests; the family's guards believe the party are the danger; the groom does not know.
- **Outs:** stop the vows without a weapon (a forged objection, a revealed bloodline, a fire alarm); get the bride out through the kitchens; let the vows finish and break the curse afterwards at a higher price.
- **Escalate:** the dead ancestors take their reserved seats at the high table.

### The stair at night
- **Stakes:** something is between the party and the room they need, and it is between them and the exit too.
- **Complications:** the stair is narrow (single file), the banister is rotten, the portraits on the wall turn to watch and one of them reaches out.
- **Outs:** go through a servants' passage the housekeeper mentioned; wait until the hour turns, when the thing returns to its rest; burn the portrait it lives in.

## Social situations

### The dinner party
- **Setup:** the family hosts. Six courses, and each course is a chance to learn or lose something.
- **Stakes:** an invitation to stay (access to the house) or an excuse to remove the party.
- **Complications:** the seating plan separates the party; one guest is a plant; a toast demands that every guest name what they came for.
- **Structure:** give each family member one thing they want to learn about the party and one thing they will trade for it. Run it as a round of exchanges, course by course.
- **Outs:** leave politely (they will be watched), stay and play along, or make a scene that forces a secret into the open.

### The confession
- **Setup:** an NPC who knows part of the truth is ready to talk, but not here, not now, not without something in return.
- **Stakes:** the information, and the NPC's life once the family learns they talked.
- **Complications:** someone is listening at the door; the NPC's price is protection the party cannot easily give.
- **Outs:** promise protection (a thread with urgency now exists); take the truth and leave them exposed; find the same truth elsewhere, more slowly.

### The bargain with the dead
- **Setup:** a ghost or a monster offers terms.
- **Rule:** state its terms plainly, and state what it will do if refused. Gothic monsters keep their word, which is the horror.
- **Outs:** accept, counter, refuse, or trick it (a trick works once, and the monster remembers forever).

## Exploration situations

### The house at night
- Map the house as a loop, not a tree: every wing connects to two others, so the party can be cut off and rerouted.
- Each area gets one tell and one secret. Use `annotate_map` to mark them hidden until shown.
- Track the hour, not the turns. Each hour the house changes one thing (a door locks, a corridor floods with cold, a room is now furnished differently).
- **Outs:** a room that is safe (the chapel, the kitchen fire, the invalid's chamber) and a known cost to rest there.

### The sealed wing
- **Stakes:** the answer is inside, and so is whatever the family sealed in.
- **Complications:** the seals are signed by family members, some still living, and breaking one tells them.
- **Outs:** go in by the roof, by the old dumbwaiter, or by persuading someone to unseal it officially.

## Puzzle situations

- **The family logic.** The house's locks obey family rules: portraits in birth order, keys named for the dead, a lullaby whose verses are directions. Solving it means understanding the family, which is the real revelation.
- **The will's conditions.** The inheritance can only be claimed by someone who meets three conditions written by a dying, frightened man. The conditions are clues about what he feared.
- **The mirror room.** Reflections act a few seconds ahead of their owners. The puzzle is reading the future in them before it happens.
- Every puzzle has a brute-force out (smash the lock, burn the door) and the brute-force out always wakes something.

## Escalation ladder for a single encounter

1. A sign (sound, cold, light change).
2. A cost to the environment (a candle out, a door shut, a path lost).
3. A cost to a person (a captive hurt, an NPC taken, a character frightened).
4. The house takes a side (doors open for the monster, close on the party).
5. The family arrives, and they have to decide whose side they are on.

## Building it in QuestMaster

- Use `plan_encounter` for the situation, `propose_encounter` or `rate_encounter` for the fight's difficulty, and write the outs into the encounter's DM context.
- Search `search_monster_sources` for a base creature, then `upsert_bestiary_monster` to re-skin it (a ghost that remembers its name, a hound made of hedge).
- `build_cue_list` for the escalation ladder so the DM can fire each step as the fight turns.

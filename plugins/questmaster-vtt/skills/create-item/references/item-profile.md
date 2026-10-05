# Item profile template

Write this in chat first, then draft it with `upsert_magic_item`. "Goes to" names the field.
Remember the split: `name`, `description` and `lore` reach players; `secret` never does.

## Header

| Field | Value | Goes to |
|---|---|---|
| Name | what people call it | `name` |
| Type | weapon, armor, wondrous, ring, staff, wand, rod, potion, scroll, gear | `itemType` |
| Rarity | common to artifact | `rarity` (`very_rare` with an underscore) |
| Attunement | none, required, or required by a class or condition | `requiresAttunement`, `attunementRequirement` |
| Creator | a name, a faction, an era | `creatorNpcId` if the maker is an NPC; otherwise `lore` or `secret` |
| Age | how old it is | `lore` |
| Current holder | an NPC, a hoard, a ruin | `secret`, or that NPC's `notes` |

## Appearance (`description`)

3 to 5 sentences: the base object; what marks it as unusual at a glance; how it feels in the
hand or on the body (weight, temperature, vibration, smell, sound). Then one line on what
handling or identifying it reveals, leaving the hidden parts out.
- Generic: "An ornate silver dagger that glows faintly."
- Specific: "A narrow silver knife wrapped in fishing twine that stays damp however long it
  sits in the sun. Held point-down over water, the blade shivers toward the deepest spot."

## Lore (`lore`, the world's version)

- **Origin**: who made it, when, and why. A name, a place, a conflict, a need. Vague
  origins make forgettable items.
- **History**: 1 to 3 events, each discoverable (a chronicle, a lore check, a witness).
- **Reputation**: what people believe. The myth goes in `lore`; the correction in `secret`.

## Mechanics (`weaponStats` or `itemStats`; effects checked with `validate_effects`)

- **Base item**: for a standard weapon or armor, take the category, damage, type and
  properties from its rules entry (`search_rules`, `get_rules_entry`).
- **Enhancement bonus**: only when the rarity calls for it (see rarity-and-power.md).
- **Each property**:
  - Trigger: an action, a hit, a spoken word, dropping to 0 hit points, sunset.
  - Effect: what happens, its range and duration, and any saving throw. A save's DC comes
    from the wielder unless the item itself fixes one; let the effects block say which.
  - Action economy: action, bonus action, reaction, or passive.
  - Limits: charges, once per dawn, only underground.
- **Charges**: the maximum, the recharge (dawn, dusk, the new moon, a drop of the wielder's
  blood: match the theme), and what happens when the last one is spent (it cracks, it
  sleeps, it wakes).

Common items usually have one simple property; legendary ones three or four. Write each as a
plain line, then its effects block; run `validate_effects`; where the rendered prose and your
line disagree, the block is wrong. Describe it to the DM using the rendered prose.

## Sentience (`isSentient: true`; details in `secret`)

- INT, WIS and CHA scores.
- Senses: hearing, sight to a range, darkvision.
- Communication: emotions, speech in named languages, or telepathy.
- Personality: 2 to 3 sentences on how it behaves.
- Purpose: what it was made to do. This drives every conflict.
- Conflict: when it fights the wielder's will, what it demands, and what it does if refused.

## Curse (`isCursed: true`; all of it in `secret`)

- Type: possession, compulsion, transformation, dependency, or other.
- Effect: as an effects block when it is mechanical, as play when it is not.
- Trigger: what starts it or makes it worse.
- Discovery: when the wielder notices. The best curses surface at a dramatic moment.
- Removal: what it takes (a spell, a rite at a named place, giving it away willingly).
- The hook: why a player keeps using it anyway. The power must be worth the cost.

## Artifact (`rarity: "artifact"`; costs and destruction in `secret`)

- Minor beneficial properties: 2 to 3. Major beneficial: 1 to 2.
- Minor detrimental: 1 to 2. Major detrimental: 1, a cost that forces hard choices.
- Destroying it: a specific, difficult, story-based method. Never "it can't be destroyed".

## Story integration (`secret`, plus threads)

- Why it exists, and why it survived to now.
- What it wants (if sentient) and how it uses its wielder to get it.
- How it changes the wielder over time: a mark, a reputation, a habit. Every item of power
  leaves one.
- Three hooks, each a candidate `upsert_thread`: its origin as a quest; someone else who
  wants it; its curse or cost.

## Worked example (compressed)

**Vellin's Tally-Knife**: dagger, uncommon, requires attunement.
- `description`: "A plain steel penknife with a bone handle notched forty-one times. It
  never needs sharpening. While attuned, once per dawn when you hit a creature with it, you
  learn exactly how many coins it carries."
- `lore`: "Auditors of the old Counting House carried knives like this. Merchants said a
  notch was cut for every thief the knife found."
- `secret`: "Vellin cut a notch for every auditor she killed. The forty-first notch is the
  guild's current master, who believes Vellin is dead. The knife warms within 30 feet of
  him." Hooks: the forty-first notch; the guild buying back every tally-knife; the
  wielder's growing urge to count other people's coins.
- `weaponStats`: the dagger's category, damage, type and properties from its rules entry;
  1 charge, recharging at dawn; one effects block for the coin count, validated first.
- `creatorNpcId`: Vellin, if she exists as an NPC; `isCursed` false (the urge is flavor in
  `secret`, played at the DM's discretion).

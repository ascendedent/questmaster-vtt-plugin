# Balancing homebrew against the rules

Balance is a comparison, not a formula. Read real entries first, then place the homebrew between them and say why. Never balance from memory; name what you read.

## The method

1. **Pick three comparables** with `search_rules`, then read each with `get_rules_entry`:
   - one entry that is clearly a bit weaker, one about the same, one a bit stronger;
   - same kind and the same slot: spell level and casting time, item rarity, feat category, the subclass feature level, monster CR.
2. **Compare on every axis below**, in a small table. Most broken homebrew wins on one axis while matching on the rest.
3. **Pay for every win.** If it beats the "same" comparable on one axis, it must lose on another.
4. **Write the verdict** in one line plus levers: "Between A and B. If it plays too strong, drop the rider; if too weak, add the per-slot scaling."

## Axes

| Axis | Ask |
|---|---|
| Output | How much damage, healing or bonus, on average? |
| Reach | How many targets, how large an area, what range? |
| Reliability | Attack roll or save? Anything on a miss or a success? |
| Duration | One hit, one round, a minute, until a rest, forever? |
| Cost | Action, bonus action, reaction? Slot level, charges, attunement, concentration, a rest? |
| Riders | Conditions, forced movement, advantage, denial of reactions? |
| Scaling | Does it grow with slot level, character level or proficiency? |
| Opportunity | What does the player give up to take it (another feat, another subclass, a slot)? |

Concentration, attunement, a once-per-rest limit and a bonus-action casting time are real costs. Count them.

## By kind

### Spells
- Compare at the same level AND the same action cost. A bonus-action spell is weaker than an action spell of the same level.
- An area spell rolls fewer dice than a single-target spell of its level; a save-for-half spell fewer than a save-negates one.
- A condition that removes turns (paralyzed, stunned, incapacitated) needs a save, a repeat save to end it and concentration. Without all three it is too strong.
- Upcasting: copy the step size of the nearest comparable (`scaling` `per-slot-level`). Cantrips use `cantrip-tier`.
- A spell must not do the job of a higher-level spell for a lower slot.

### Feats
- Compare inside the same category and prerequisites. A feat that also raises an ability score gets a smaller benefit.
- Prefer situational or resource-gated benefits ("once per short rest", "when you are bloodied") over flat, always-on bonuses to attack rolls or AC.
- A repeatable feat must stay fair when taken three times.

### Classes and subclasses
- Put features at the same levels the parent class's other subclasses get theirs, and compare level by level.
- Resources scale with proficiency bonus or recharge on a rest, like the comparables. Model them in `resources`.
- A whole homebrew class is a large project: compare its hit die, proficiencies and level 1 to 5 features with two existing classes before writing level 6 and up.

### Species
- Count traits against two existing species. A movement mode, a damage resistance, darkvision and an innate spell each count as one.
- Flight or at-will invisibility at level 1, immunity to a common damage type, or a free feat on top of everything else are red flags.

### Magic items
- Find two items of the target rarity, and one of the rarity below, with `search_rules`.
- Higher rarity buys a bigger bonus, more charges, a stronger daily effect, or a more powerful passive. Attunement is the main lever for a strong passive.
- Charges: say how many and how they come back (`charges`, `chargesRecharge`). Infinite uses of a spell-like effect are a rarity jump or two.
- A curse is not a discount; it is a story hook. It lives in the item's DM-only `secret`, and `isCursed` marks it.
- If a rules item already does the job, `import_catalog_item` it and reflavor in `description`; it is free and already balanced.

### Monsters
- QuestMaster rates fights and computes NPC numbers. Use `set_npc_statblock` (custom: CR, abilities and plain dice) or adopt a bestiary or rules monster, and let `rate_encounter` judge the fight.
- Compare a homebrew monster with two rules monsters of its CR (`search_monster_sources`, `get_rules_entry`) for hit points, AC, the number of attacks and the strongest single effect.

## Red flags

- Stacking flat bonuses to attack rolls, AC or saves from several sources.
- Extra attacks or a second action through a bonus action, with no limit.
- A condition that removes turns with no save, or with no way to end it.
- Anything permanent, unlimited or recharging every turn that a comparable limits per rest.
- Auto-success on checks: it removes a pillar of play (no more lock to pick, no more lie to detect).
- Immunity to a common damage type or condition below the highest rarities.
- A low-level option that copies a high-level one.

## Verdict format

```
<Name> (<kind>): balanced / slightly strong / too strong / too weak
Compared with: <A> (weaker), <B> (similar), <C> (stronger), all read from the rules.
Why: <the one or two axes that decide it>.
Levers: stronger -> <change>; weaker -> <change>.
```

## Worked example

A DM wants "Briar Snare": a 1st-level action spell, a 10-foot square of thorns within 60 feet; creatures inside make a STR save or are restrained; 2d4 piercing at the start of each of their turns; concentration, 1 minute.

- Comparables (read with `get_rules_entry`): a 1st-level area spell that restrains on a failed save with no damage (similar); a 2nd-level spell that damages each turn in an area (stronger); a 1st-level single-target damage spell (weaker).
- Finding: it matches the 1st-level restraining spell AND adds damage every turn. It wins on output and matches on everything else.
- Fix options for the DM: drop the damage to "1d4 when a creature tries to break free", or keep the damage and shrink the area to one creature, or keep both and make it 2nd level.
- Effects, once the DM chooses: a `condition` "Restrained" with `save` STR from `spell-save-dc`, `endSave` STR `end-of-turn`, `duration` minutes 1 with `concentration`; plus a `damage` with `trigger` `start-of-turn` and the agreed dice. Run both through `validate_effects`.

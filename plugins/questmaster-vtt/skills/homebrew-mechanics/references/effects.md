# Structured effects: shapes and recipes

QuestMaster runs homebrew at the table from effects blocks, not from prose. Prose is what players read; the block is what the app rolls, applies and tracks. Check every block with `validate_effects` before it goes into a draft.

## The block

```json
{ "effects": [ ...up to 24 effects... ], "noMechanicalEffect": false, "flavor": null }
```

| `effects` | `noMechanicalEffect` | Means |
|---|---|---|
| empty | false | Not filled in yet. The app flags it in prep. |
| empty | true | Deliberately nothing to track (a language, a flavor trait). Ready. |
| filled | any | Ready, if it validates. |

- `flavor`: an optional line kept beside the mechanics.
- `unresolved`: never send it. Only QuestMaster's rules parser sets it, and the tools refuse it.

## The envelope (every effect has it; all optional)

- `trigger`: `immediate` (default), `on-hit`, `on-crit`, `on-failed-save`, `on-successful-save`, `start-of-turn`, `end-of-turn`, `on-enter-area`, `passive` (while held, worn or active).
- `targeting`: {`mode`: `self`, `creature` (default), `creatures` (with `count`), `area`, `all-in-area`, `object`, `point`; `shape`: `sphere`, `cube`, `cone`, `line`, `cylinder`, `emanation`; `sizeFt`; `widthFt` for lines}. `all-in-area` hits everyone inside; `area` is a place.
- `save`: {`ability`: `str` `dex` `con` `int` `wis` `cha`; `dcSource`: `spell-save-dc` (default), `weapon-save-dc` or `flat`; `dc` only with `flat`; `onSuccess`: `none`, `half`, `full`}.
- `duration`: {`unit`: `instantaneous`, `rounds`, `minutes`, `hours`, `days`, `until-dispelled`, `permanent`, `special`; `amount`; `concentration`}.
- `scaling`: {`mode`: `none`, `per-slot-level` (with `amount` per step and `baseLevel`), `cantrip-tier` (fixed steps)}.
- `applyIf`: {`mode`: `none`, `simple` or `pro`; `subject`: `target` or `self`; `predicate`: `has-condition`, `lacks-condition`, `is-creature-type`, `hp-below-half`, `hp-at-full`, `is-concentrating`, `is-within-range`, `custom`; `value`; `text` (required in simple and pro: the line a DM reads when it applies)}.
- `note`: anything the structure cannot say, rendered after the mechanics.

## Categories (`category` picks one)

| Category | Its own fields |
|---|---|
| `damage` | `dice` ("2d6", "1d8+2"), `damageType` (bludgeoning, piercing, slashing, acid, cold, fire, force, lightning, necrotic, poison, psychic, radiant, thunder), `critRule` (`double-dice`, `max-dice`, `none`), `split` (`per-target`, `shared`) |
| `healing` | `dice`, `mode` (`hp`, `temp-hp`, `max-hp`), `cap`, `revives` |
| `condition` | `condition` (a condition name like "Prone"), `endSave` {`ability`, `cadence`: `end-of-turn`, `start-of-turn`, `once`} |
| `movement` | `kind` (`teleport`, `speed`, `grant`, `forced`, `terrain`), `distanceFt`, `requiresSight`, `direction` (`push`, `pull`, `slide`), `op` (`bonus`, `penalty`, `set`, `multiply`), `factor`, `movementMode` (`walk`, `fly`, `swim`, `climb`, `burrow`, `hover`), `terrain` (`ignore-difficult`, `create-difficult`) |
| `roll-mod` | `rollTarget` (`attack`, `damage`, `ac`, `save`, `check`, `initiative`), `which` ("dex", "Stealth"), `value` ("+1", "+1d4"), `advantage` (`none`, `advantage`, `disadvantage`), `who` (`self`, `target`, `allies`, `enemies`) |
| `narrative` | `text`: prose the app shows but does not track |
| `resistance` | `level` (`resistance`, `immunity`, `vulnerability`), `against` (`damage`, `condition`), `value` (a damage type or condition) |
| `senses` | `sense` (`darkvision`, `blindsight`, `tremorsense`, `truesight`, `detect`), `rangeFt`, `detail` |
| `resource` | `op` (`restore`, `drain`, `grant`), `resource` (`spell-slot`, `charge`, `hit-die`, `class-resource`, `action`, `bonus-action`, `reaction`), `amount`, `detail` |
| `summon` | `what` (`creature`, `object`, `terrain`, `light`), `count`, `statblockRef`, `radiusFt`, `detail` |
| `control` | `effect` (`invisibility`, `shapechange`, `telepathy`, `dispel`, `counter`, `banish`, `plane-shift`, `other`), `detail` |

The condition that resists (`save` in the envelope) is not the save that ends it (`endSave`). A hold-style effect has both.

## Where blocks live, per homebrew kind (`data`)

- `spell`: {`level` (0 is a cantrip), `school`, `castingTime`, `range`, `components` {`v`, `s`, `m`}, `duration`, `concentration`, `classes`, `description`, `higherLevel`, `effects`}.
- `feat`: {`prerequisites`, `category`, `repeatable`, `benefits`, `abilityIncrease` (abilities), `effects`}.
- `species`: {`size`, `speed`, `darkvision`, `languages`, `traits`: [{`name`, `text`, `effects`}], `description`}.
- `class`: {`hitDie` (6, 8, 10, 12), `casterType` (`none`, `full`, `half`, `pact`), `spellcastingAbility`, `featuresByLevel` {"1": [feature names]}, `multiclassPrereq`, `multiclassProficiencies`, `resources`, `featureEffects` {feature name: block}, `description`}.
- `subclass` (needs `parentClass`): {`featuresByLevel`, `resources`, `featureEffects`, `description`}.
- `monster`: {`cr`, `type`, `size`, `alignment`, `ac`, `hp`, `speed`, `abilities`, `traits` and `actions`: [{`name`, `text`, `effects`, plus on actions `attackKind`, `reachFt`, `rangeNormalFt`, `rangeLongFt`, `recharge`}], `description`}. Leave `attackBonus` out unless the DM gives one or it is copied from the comparable rules monster.
- `language`: {`description`, `rarity`}. `tool`: {`description`, `category`}. Usually `noMechanicalEffect`.
- `resources` entries: {`name`, `kind` (`slot`, `pool`, `charge`, `hitdie`), `recharge` (`short`, `long`, `dawn`, `none`), `baseMax`, `perLevel`, `minLevel`}.

Gear and items carry one block in `effects` (homebrew weapon or armor) or in `weaponStats.effects` / `itemStats.effects` (a magic item).

## Recipes

Area damage, save for half (a 1st-level spell, 15-foot cone):
```json
{ "effects": [ { "category": "damage", "dice": "3d6", "damageType": "fire",
  "targeting": { "mode": "all-in-area", "shape": "cone", "sizeFt": 15 },
  "save": { "ability": "dex", "dcSource": "spell-save-dc", "onSuccess": "half" },
  "scaling": { "mode": "per-slot-level", "amount": "1d6", "baseLevel": 1 } } ] }
```

Damage plus a condition on a failed save (two effects, one save):
```json
{ "effects": [
  { "category": "damage", "dice": "2d8", "damageType": "thunder",
    "save": { "ability": "con", "dcSource": "spell-save-dc", "onSuccess": "half" } },
  { "category": "condition", "condition": "Deafened", "trigger": "on-failed-save",
    "save": { "ability": "con", "dcSource": "spell-save-dc", "onSuccess": "none" },
    "duration": { "unit": "rounds", "amount": 1 } } ] }
```

Weapon rider on a hit, with a condition only against one creature type:
```json
{ "effects": [ { "category": "damage", "dice": "1d6", "damageType": "radiant", "trigger": "on-hit",
  "critRule": "double-dice",
  "applyIf": { "mode": "simple", "predicate": "is-creature-type", "value": "undead",
    "text": "Only against undead." } } ] }
```

Item that grants passive resistance (use `special`, not `permanent`, with `passive`):
```json
{ "effects": [ { "category": "resistance", "level": "resistance", "value": "cold",
  "trigger": "passive", "targeting": { "mode": "self" }, "duration": { "unit": "special" } } ] }
```

Feat bonus to initiative, and a species trait with darkvision:
```json
{ "effects": [ { "category": "roll-mod", "rollTarget": "initiative", "value": "+2", "who": "self",
  "trigger": "passive", "targeting": { "mode": "self" } } ] }
{ "effects": [ { "category": "senses", "sense": "darkvision", "rangeFt": 60, "trigger": "passive",
  "targeting": { "mode": "self" } } ] }
```

Something the app should not track: `{ "effects": [ { "category": "narrative", "text": "You can speak with ravens about the weather." } ] }`.

## Reading `validate_effects`

- `valid: false` with `issues`: each line names the path that failed (`effects.0.save.ability`). Fix and re-check.
- `warnings`: each is `incomplete` (something missing: an area with no size, upcasting with nothing to increase, a `flat` save with no DC) or `odd` (legal but probably not meant: concentration on an instantaneous effect, a self-targeted save). Fix every `incomplete`; fix each `odd` or tell the DM why it stays.
- `readiness`: whether the block is ready for the table, and why not.
- `rendered`: the prose the app will show. If it does not say what the entry's text says, change the block, not the text.

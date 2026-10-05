# Rarity, attunement and power

This page is judgment, not arithmetic. QuestMaster runs the mechanics; your job is to say
plainly what an item does at the table and what it could break, and let the DM decide.
Never tell the DM an item "is balanced".

## Rarity at a glance (5e 2024 defaults)

| Rarity | `rarity` | Usually appears from | What it can do |
|---|---|---|---|
| Common | `common` | any level | one small, flavorful trick; little or no combat edge |
| Uncommon | `uncommon` | level 1 | one useful property, or a +1 weapon or shield |
| Rare | `rare` | about level 5 | one strong property or two moderate ones |
| Very rare | `very_rare` | about level 11 | strong, reliable power, or several properties |
| Legendary | `legendary` | about level 17 | 3 to 4 properties; it shapes a character's story |
| Artifact | `artifact` | when the story says | benefits and costs; a quest to destroy |

Rarity is where the item sits in the world, too: a rare item has a known name, a price
nobody can pay openly, and people who would kill for it.

## Enhancement bonuses

| Bonus | Weapon or shield | Armor |
|---|---|---|
| +1 | uncommon | rare |
| +2 | rare | very rare |
| +3 | very rare | legendary |

A weapon's bonus goes in `weaponStats.attackBonus`. An armor or shield bonus is a modifier
to AC in the effects block, checked with `validate_effects`; `itemStats.armorAcBonus` and
`shieldBonus` describe the base armor or shield, not the enchantment. These are the item's
own printed numbers. The wielder's total to-hit and AC are computed by QuestMaster from the
character; never write those.

## Power checks before drafting

Read the intended owner with `get_character`, then ask:
- Does it replace a class feature someone at the table paid for (a rogue's sneak attack, a
  ranger's tracking)? Then it steals a spotlight.
- Does it remove a pressure the game relies on: light, rest, travel time, food, a lock?
- Does it answer a mystery with no roll or choice?
- Does it stack with what the owner already has into something the DM didn't intend?
- Does it make one character's turn longer every round?
- Would the DM be happy to see an enemy use it against the party?

Report the answers as risks ("this makes the rogue's lockpicking redundant"), not as a
verdict, and offer a weaker or more costly variant alongside.

## Attunement

- Require it for persistent power, refreshing charges, sentience, or anything that stacks.
- Skip it for consumables and common oddities.
- A creature can attune to three items at once, so attunement is itself a cost. Check what
  the owner already has attuned.
- `attunementRequirement` can be a story gate, not just a class: "by a creature that has
  never struck a sleeping foe", "by a member of the Ferry Guild".

## Consumables

Potions, scrolls, single-use charms: one dramatic use, so a lower bar than permanent items.
A good consumable creates a decision about *when*, not *whether*.

## Story gear with no mechanics

A mayor's chain of office, a dead mentor's map case, a letter of passage. Draft it with
`upsert_magic_item`, `rarity: "common"`, no `weaponStats` or `itemStats`, and put the weight in
`description`, `lore` and `secret`. Its power is social: doors it opens, people it angers.

## Curses that work

A curse is a deal, not a trap. The player should understand the bargain by the time it bites.
- **Price**: the power is real and so is the cost ("you can't be surprised, and you can't sleep
  more than four hours").
- **Hunger**: the item wants something and gets stronger when fed (it must taste blood daily).
- **Hitchhiker**: something rides along (a voice, a debt, a pursuer who can always find it).
- **Slow change**: it reshapes the wielder a little per use, visibly and cumulatively.
- **Wrong owner**: it works perfectly for someone else and spitefully for the wielder.

Fixes for bad curses:
- "You can't remove it and it does nothing good" is a punishment. Give it a real benefit.
- A curse discovered on identification has no drama. Let it surface at a key moment.
- A curse that takes control of a player character for long stretches takes the game from
  that player. Prefer pressure, temptation and costs over control.

## Sentient items

- Give it a purpose narrow enough to conflict with the wielder sometimes ("guard the river
  crossings" pulls against a party heading inland).
- It speaks rarely and at the worst moments. A chatty item crowds the table.
- Give the DM its demands in advance, in `secret`, with what it does when refused.

## Artifacts

- Every major benefit has a major cost; the cost should grow with use.
- Destruction is a quest, not a footnote: "melt it in the forge that made it, which now lies
  under a lake", "give it freely to the one person it has wronged", "let a child spend it
  as a coin".

## Items that grow

An heirloom that wakes over the campaign: draft the dormant version now, and plan each stage
(what wakes it, what it gains) in `secret`. Each stage becomes a later patch when the DM says
so. Plan the `lore` with care, because once the DM pushes it, it can't be changed here.

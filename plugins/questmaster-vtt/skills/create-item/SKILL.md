---
name: create-item
description: "A workflow for making magic items, cursed objects, artifacts and story-heavy gear for a QuestMaster campaign, with origin, history and costs, player-visible description and lore kept apart from the DM-only secret, mechanics as structured effects checked by validate_effects, and rules items imported rather than rewritten. Use when the DM asks for a magic item, a reward, a cursed trinket, an artifact, a new weapon or armor type, or wants a rules item in the campaign's library."
---

# Create Item

The DM gets an item that feels earned and belongs to the world: who made it, what it has
done, what it costs, and mechanics QuestMaster can run at the table, drafted into the
campaign's item library.

## Use this when

- "A reward for the paladin", "a cursed ring for the auction", "an artifact the cult wants".
- A rules item should be in the campaign's library, for a hoard or a shop shelf.
- A new kind of weapon or armor (a new base type, not a magic version of an existing one).

## Steps

1. **Read.** `get_campaign_overview`. `get_party` for levels and classes, and `get_character`
   for the intended owner (what they carry, their attuned items, weapon masteries).
   `list_entities` with kind `item` and `search_campaign` for the name, to avoid duplicates.
   `search_rules` for the concept: if the rules already have the item as wanted, import it.
   `get_entity` on the creator NPC or faction.
2. **Parse** item type, power level (rarity), thematic intent, origin and how the party
   gets it. If the request is open-ended ("make a cool sword"), ask: "What class or role is
   this for, and what story moment should it create?"
3. **Write the profile** from [references/item-profile.md](references/item-profile.md),
   with rarity and costs judged by [references/rarity-and-power.md](references/rarity-and-power.md).
   Show it in chat. Offer a second option where power level is a judgment call.
4. **Build the mechanics.** Write each property as one plain line, then as an effects block.
   Run `validate_effects` on each block, fix what it reports until it is valid and ready,
   and show the DM the rendered prose it returns. That prose is what the table will run.
5. **Draft it**: `import_catalog_item` for a rules item as written; `upsert_homebrew_gear`
   first if the base weapon or armor is new; then `upsert_magic_item`.
6. **Recap and ask.** `get_changeset`, a plain summary that separates what players see
   (name, description, lore once pushed) from the DM-only secret, then ask, then
   `request_approval`. Nothing is saved until it returns `applied`.
7. **Hand back.** Handing the item to a character, pushing its lore, and opening a shop that
   stocks it are the DM's moves in the app. `intendedForCharacterId` only notes who it's for.

## What to produce

Name, type, rarity, attunement (and who may attune), creator, age, current holder.
Appearance in 3 to 5 sentences (the object, what marks it as unusual, how it feels in the
hand). Lore: an origin with a name, a place and a need; 1 to 3 events in its history;
its reputation, fact and myth apart. Mechanics: base item, each property (trigger, effect,
action, limits), charges and recharge and what happens at zero. Sentience, curse and
artifact sections only when they apply. Story integration: why it exists, what it does to
its wielder over time, three hooks (its origin, someone else who wants it, its cost).

## Drafting it

- `import_catalog_item {kind, srdId}` with kind `magic`, `equipment`, `weapon` or `armor` and
  the id from `search_rules`. Free. Editing it later with `upsert_magic_item` makes it the
  DM's own content, which counts toward the free plan's allowance.
- `upsert_homebrew_gear {gear: "weapon" | "armor", ...}` adds a new base type to the
  campaign's catalog (name, category, damage, damageType, properties, mastery; or baseAc,
  strengthReq, stealthDisadvantage). The magic version still carries its own stats.
- `upsert_magic_item`:
  - `name`: what people call it. No curse or twist in the name.
  - `itemType`, `rarity` (common, uncommon, rare, very_rare, legendary, artifact),
    `requiresAttunement`, `attunementRequirement` ("by a creature that has sworn an oath").
  - `description` (player-visible): appearance and what handling or identifying it reveals.
  - `lore` (player-visible once the DM pushes it): origin, history and reputation as the
    world tells it, partial or wrong where the world is. `style-in-world-documents` sets the voice.
  - `secret` (DM-only): the curse, the true origin, a sentient item's purpose, what it does
    to the wielder, how an artifact is destroyed, the hooks.
  - `isSentient`, `isCursed`, `creatorNpcId` (an id or a draft ref), `intendedForCharacterId`.
  - `weaponStats` for a weapon (category, damage, damageType, properties, an `attackBonus`
    only for a +1 to +3 weapon, charges, chargesRecharge, activationNotes, effects) or
    `itemStats` for anything else (armorAcBonus, shieldBonus, charges, chargesRecharge,
    activationNotes, effects). Never both. A purely narrative item can have neither.
- On a shop shelf: `upsert_shop` with `addStock: [{itemId: "item:1", displayName, priceCp}]`.
  The price is the DM's call.
- Its hooks: one `upsert_thread` each. The text players might find about it: `generate-lore`.

## Don'ts

- Don't compute numbers the engine resolves: a wielder's attack total, a save DC that should
  come from the wielder, damage with modifiers. Write effects and let `validate_effects` and
  the table do it. Don't call an item "balanced"; describe what it does and what it could break.
- Don't put the curse, the true origin or a sentient will in `name`, `description` or `lore`.
- Don't rewrite a rules item from memory; find it with `search_rules` and import it.
- Don't draft an effects block `validate_effects` reports as invalid or not ready, and never
  mark one unresolved.
- Don't hand the item over or promise it to a player; that is the DM's action in the app.
- Don't say anything is saved before `request_approval` returns `applied`.

## Pairs well with

- `homebrew-mechanics` for effects blocks and any homebrew spell or feat the item grants.
- `generate-lore` for the in-world text about the item, `generate-npc` for its maker or
  hunter, `design-encounter` for where it is won, `style-handouts` for an item card.
- The campaign's `genre-*` pack: a cursed item in gothic horror and a heist's prize read differently.

## References

- Read [references/item-profile.md](references/item-profile.md) when writing the profile:
  the template with field mapping, sentience, curses, artifacts and a worked example.
- Read [references/rarity-and-power.md](references/rarity-and-power.md) when choosing rarity,
  attunement, an enhancement bonus or a curse, or judging whether an item is too strong.

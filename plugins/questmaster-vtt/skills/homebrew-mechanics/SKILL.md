---
name: homebrew-mechanics
description: A procedure for authoring homebrew rules content in QuestMaster with structured effects the app can use at the table (classes, subclasses, species, spells, feats, monsters, languages, tools, homebrew weapons and armor, and magic item mechanics), checked with validate_effects and balanced against comparable rules entries. Use when a DM wants to create, convert, fix or balance homebrew, or make prose homebrew work at the table.
---

# Homebrew Mechanics

The DM gets homebrew that reads well to players AND works at the table: every mechanic carried as a structured effects block that QuestMaster has checked, balanced against real rules entries, drafted for approval.

## Use this when

- "Make a homebrew spell / feat / subclass / species", "turn this house rule into something the app can use".
- A homebrew entry exists as prose and the DM wants it to roll at the table.
- A DM asks "is this balanced?" or wants a magic item's or weapon's mechanics wired up.

## Steps

1. **Read first.** `get_campaign_overview`. Then `list_entities` kind `homebrew` (or `search_rules`, which includes the campaign's homebrew gear) so you never draft a second entry with the same kind and name. For an edit, `get_entity` kind `homebrew` and work from its current `data`.
2. **Find the yardstick.** `search_rules` for 1 to 3 comparable entries (same kind, same spell level, rarity, feat category or CR) and read them with `get_rules_entry`. Balance against those, using [references/balance.md](references/balance.md).
3. **Ask one question if essential**, usually the power target ("Should this sit beside an uncommon item or a rare one?") or, for a subclass, which class it belongs to.
4. **Write the prose, then the effects.** Prose first (what players read), then one effects block per action, feature, trait or rider. Shapes: [references/effects.md](references/effects.md).
5. **Validate every block.** Call `validate_effects` on each block before it goes into any draft. Fix every `issues` line, read `warnings`, and compare `rendered` with the prose: if the rendered reading says something the prose does not, the block is wrong. Never set `unresolved`.
6. **Draft.**
   - Rules entries: `upsert_homebrew` {`kind`, `name`, `parentClass` for a subclass, `data`}. Its reply says whether every effects block is ready for the table.
   - Prose entries already saved: `structure_homebrew` {`homebrewId`} shows the parser's suggestions, each with a key and how it reads. Show them to the DM, then call again with `accept`: only the keys whose reading matches the text. Author the rest by hand and validate. It works on a saved entry (a real id, not a ref from this draft), so a prose entry drafted in this conversation is approved first.
   - Weapons and armor: `upsert_homebrew_gear` {`gear`: `weapon` or `armor`, ...}.
   - Magic items: `upsert_magic_item` with `weaponStats` or `itemStats`, each carrying `effects`. If a rules item already does the job, `import_catalog_item` instead (imports are free).
   - Monsters to fight: prefer `upsert_bestiary_monster` or `set_npc_statblock` (see `design-encounter`). A homebrew `monster` entry is for a reusable rules entry; `add_monsters_to_bestiary` with `homebrew` puts it in play.
7. **Mind the allowance.** On the free plan, authored homebrew entries, homebrew gear, equipment packs, and authored or edited library items count toward the owner's custom content allowance; imports don't. If a draft is refused because the allowance is full, say so plainly and offer options: import a rules entry and reflavor it in prose, fold two entries into one, or let the DM free a slot.
8. **Recap and approve.** `get_changeset`; for each entry show the player text, the `rendered` reading of each effects block, readiness, and the one-line balance verdict. Ask, then `request_approval`. Never call it saved before `applied`.
9. **Hand over.** Giving a character a feature, feat, spell or item, stocking a shop, and handing items over are the DM's actions in the app.

## What to produce

Per entry: name and kind; player-facing text in the house style of the comparable entries; the effects, listed as their `rendered` reading; readiness; a balance line ("Sits between Comparable A and Comparable B: same damage as A, smaller area, adds a rider"); open questions for the DM. Keep design notes in chat.

## Drafting it

- `upsert_homebrew`: `kind` one of class, subclass, species, spell, feat, monster, language, tool; `name`; `parentClass` (subclass only: the class's name); `data` in the kind's shape. `data` replaces the whole entry: read it, change it, send all of it.
- `structure_homebrew`: `homebrewId`, then `accept` as the list of approved keys. Without `accept` nothing is drafted.
- `upsert_homebrew_gear`: weapon {`name`, `category`, `damage`, `damageType`, `damage2h`, `properties`, `thrown`, `rangeNormal`, `rangeLong`, `mastery`, `description`, `effects`}; armor {`name`, `category`, `baseAc`, `strengthReq`, `stealthDisadvantage`, `description`, `effects`}.
- `upsert_magic_item`: `name`, `itemType`, `rarity`, `requiresAttunement`, `attunementRequirement`, `description` and `lore` (players see), DM-only `secret`, `isCursed`, `isSentient`, `creatorNpcId`, `intendedForCharacterId`, plus `weaponStats` or `itemStats` (both carry `effects`, `charges`, `chargesRecharge`, `activationNotes`).
- Leave a field out to keep it; `null` clears it; list fields replace the whole list.

## Don'ts

- Don't draft a block `validate_effects` hasn't passed, and never set `unresolved` (only the rules parser sets it).
- Don't compute to-hit, save DCs or damage modifiers. Saves use `dcSource` `spell-save-dc` or `weapon-save-dc` so the app resolves them per character; a `flat` DC only where the design truly is fixed (a trap, a cursed item) and the DM agrees the number.
- Don't accept every `structure_homebrew` suggestion. Accept only keys whose reading matches the text.
- Don't hide twists in homebrew `data`: players can read all of it. A curse or secret belongs in a magic item's `secret`.
- Don't balance from memory. Name the comparable entries you read and say how this differs.
- Don't upsell. State the allowance limit once when it matters, then help within it.

## Pairs well with

- `create-item` for an item's story and lore, `design-encounter` and `generate-npc` for stat blocks, `generate-lore` for the in-world origin.
- `style-in-world-documents` for item lore and spell scrolls, `style-handouts` for a feat or species write-up the DM hands out.
- The campaign's `genre-*` pack for flavor (a `genre-fey-fairytale` boon should bind; a `genre-grimdark` one should cost).

## References

- [references/effects.md](references/effects.md): read before writing any effects block; the block shape, every category, the per-kind `data` shapes, and worked blocks.
- [references/balance.md](references/balance.md): read when picking comparables or when the DM asks if something is balanced; axes, rarity and level ladders, red flags.

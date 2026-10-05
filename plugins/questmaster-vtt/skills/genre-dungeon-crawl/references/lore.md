# Dungeon Crawl: lore

A dungeon's lore is written into its walls. Every level should tell the party something about who built it, why they stopped, and who moved in after. Players should be able to reconstruct the place's history from what they touch, not from what they are told.

## Lore textures

- **Purpose shows through.** An assay house has scales, ventilation and locks everywhere. A prison has doors that only open from outside. A temple has sight lines toward one altar. Pick the builder's purpose and let every room obey it.
- **Repurposing.** The current inhabitants use rooms for things they were not built for: the chapel is a kitchen, the vault is a nursery, the drainage channel is a highway. The gap between built use and current use is the most efficient storytelling in the genre.
- **The moment it stopped.** Every dungeon has a last day: tools left mid-task, a meal on the table, a door barred from the wrong side. Find it and show it once per level.
- **Layers of visitors.** Delvers' chalk arrows over the builders' carvings over an older cave painting. Each layer is a clue to another era.
- **Rules of the place.** The builders had rules (no flame below the third stair, silence in the archive). The rules still matter, even if nobody remembers why.

## Sensory palette

**Sights**
- Soot streaks on the ceiling showing where torches were mounted, and one clean stretch where something blocked them.
- Grooves worn into a stone threshold by centuries of the same footstep.
- A doorway bricked up in a different color of brick.
- Fresh tallow drips on a stair nobody should be using.
- Chalk arrows from three different crews, pointing three different ways.

**Sounds**
- Water dripping in a rhythm too regular to be natural.
- A door slamming somewhere far below, then a long pause.
- Chains settling in a draft.
- Distant hammering that stops whenever the party stops.
- Your own breath, loud in a room with dead acoustics.

**Smells**
- Wet stone and rust in the lower halls.
- Old smoke, rancid fat and unwashed bodies: a faction's living quarters ahead.
- Sweet rot: something dead and large, upwind.
- Ozone near a working ward or a wizard's leftovers.
- Fresh bread, impossibly, from the market hall.

**Textures**
- Walls slick with condensation, cold enough to numb fingertips.
- Grit underfoot that is actually ground bone.
- A banister polished smooth by hands, then sticky with something new.
- Cobwebs that are too thick and too warm.
- Air that pushes back: a draft from a passage not on any map.

## Naming guidance

- **Name the site for what locals call it, not what it was.** Locals see the outside: the Nine Weights (for nine iron weights over the gate), the Yawn, the Bell Hill, Coldmouth.
- **Name levels by function or feel:** the Weighhouse, the Furnace Floor, the Under-Cistern; the Dry Halls, the Wet Halls, the Bottom.
- **Name rooms for what the party will remember:** the Scale Room, the Hall of Boots (dozens of boots, no bodies), the Kitchen That Was a Chapel. Players will use these names, so put them in the location name and the code in locationIdCode.
- **Builders' names sound different from inhabitants' names.** Give the builders a formal, carved naming style (Master-Assayer Ulbrecht Vonn, Second Seal) and the inhabitants a practical one (Big Nob, Cuts-the-Rope, Mother Soot).
- **Leave one thing unnamed.** The thing at the bottom is scarier as "what the miners stopped digging toward".

## In-world documents

- **A dead delver's chalk map:** scratched on a wall, with a skull drawn over one room and the words "not again" underneath.
- **A work roster:** names, shifts and a final shift where every name is crossed out except one.
- **A faction's tally wall:** marks for kills, trades and debts, readable once the party learns the symbols.
- **A builders' safety notice:** carved at the stair top, warning in formal language about a hazard that is still active.
- **A kitchen ledger:** how much food the squatters buy, which reveals how many of them there really are.
- **A letter never sent:** from someone sealed inside on the last day, explaining why the doors were shut.
- **A delvers' guide sold in town:** cheerful, illustrated, and wrong about exactly one room.

## Making the history land

- Plant the truth about why the place was sealed in at least three different documents or rooms, each partial. Stage each find as a `stage_secret` aimed at the character most likely to read it.
- Let the deepest level confirm or overturn what the upper levels implied.

# Wilderness Hexcrawl: safety

Wilderness play leans on hunger, cold, isolation and the bodies of animals and people. Random tables make this riskier than scripted play, because a table can surprise the DM. Safety work in this genre mostly happens before the dice: filter the tables, then play the dice honestly.

## Always first

- Call `get_table_safety` before drafting tables, encounters or set pieces. If the owner has not shared limits, ask the DM once whether there are any topics to keep off the table.
- **Hard limits (lines) are absolute.** Remove matching entries from every table. Do not soften them, imply them or keep them as an off-screen fact.
- **Soft limits (veils) stay off-screen.** The event can be part of the world; the description fades out, and the consequence is reported, not shown.
- A table entry that touches a veil gets rewritten to its aftermath: not "the wolves bring down the mule", but "in the morning, the mule's lead rope is chewed through and the mule is gone".

## Themes that commonly need a line or veil

### Starvation and thirst
- **Risk:** slow, grinding misery, or echoes of real food insecurity or disordered eating.
- **On-screen:** the supply count, hard choices about who eats, the relief of a good forage roll.
- **Off-screen:** detailed physical decline, eating things people do not eat, survival cannibalism (treat this as a default line unless the table opts in).

### Exposure, frostbite and injury
- **Risk:** body horror through realism (blackened fingers, amputations in the field).
- **On-screen:** the cold as a pressure and a reason to choose shelter; exhaustion as a mechanic.
- **Off-screen:** wound detail. Report the outcome ("Garrick will not hold a bow again this season") instead of the process.

### Harm to animals
- **Risk:** mounts, pack animals and pets are often the first casualties, and many players care about them more than about NPCs.
- **On-screen:** animals in danger, rescues, the muleteer's grief.
- **Off-screen:** suffering. If the table veils it, let animals flee or go missing rather than die. Ask before a party animal is killed at all.

### Hunting
- **Risk:** detailed butchery, trophy hunting, cruelty to beasts.
- **On-screen:** tracking, the chase, a clean result.
- **Off-screen:** dressing and gutting.

### Isolation, being lost, tight spaces
- **Risk:** players with real anxiety about being lost, trapped in caves or crevasses, or abandoned.
- **On-screen:** the tension of fog and the relief of a found landmark.
- **Off-screen:** extended scenes of being trapped with no agency. Always give a visible way out within the scene.

### Drowning and deep water
- **Risk:** a common phobia, and river crossings are a staple encounter.
- **On-screen:** the current, the struggle, the rescue.
- **Off-screen:** a character's drowning described from inside. Narrate from the bank.

### Creeping and stinging things
- **Risk:** spiders, insects, leeches, snakes and swarms are common table phobias, and swamps and caves are full of them.
- **Fix:** if any are lines, swap them out of every table now. A swamp can be dangerous with sucking mud, cold and alligator-like predators instead.

### Settlers, displacement and land theft
- **Risk:** frontier stories easily repeat real histories of colonization, with the original inhabitants as obstacles or set dressing.
- **On-screen:** the herders and hill clans as people with names, title, politics and their own wants; the company's claim as a choice the party can oppose, help or bargain over.
- **Avoid:** inhabitants presented as savage, primitive or monstrous; "empty land" that was never empty. If the table wants this theme handled lightly, keep the land disputes legal and political rather than violent.

### Abandoning companions
- **Risk:** leaving the injured behind can hit hard, and players can feel forced into it by supply math.
- **Fix:** never make abandonment the only way out. Offer a costly alternative (lose the cargo, lose the deadline, signal for help) every time.

## Tables and the dice

- Filter every table against `get_table_safety` when drafting it, and again whenever limits change.
- Keep a note on each region's table listing which entries were changed for safety, so a co-DM does not restore them.
- If a roll lands on something that turns out to be uncomfortable mid-session, the DM can drop it; dice never outrank the table.

## Player characters

- Backstories from `get_character` are player-written. If a character comes from a displaced people or lost family to the wild, ask the DM before using that history as a hook, and never kill or harm what the player wrote without the DM saying so.

---
name: genre-fey-fairytale
description: Genre pack for fey and fairytale campaigns, giving the assistant bargain logic with exact wording and prices, binding rules that tie fey and mortals alike, hospitality as a system, and beauty with teeth, plus references for beats, NPCs, encounters, factions, lore, pitfalls and table safety. Use when the campaign tone or the DM mentions fey, fairies, an otherworld, enchanted woods, courts, curses, changelings, glamour or fairytales, or asks for a bargain, a trickster, a riddle, a curse with a key or a court that runs on etiquette.
---

# Fey Fairytale

Play feels like a lovely, courteous party where every gift is a contract, every rule once spoken binds the speaker too, and the cake is a little too sweet.

## Use this when

- The campaign profile or tone mentions fey, fairies, the otherworld, enchanted forests, courts of seasons or twilight, curses, changelings, glamour, wishes or fairytale.
- The DM asks for a bargain, a deal with a price, a trickster NPC, a riddle contest, a curse and how to break it, or a court where manners are the danger.
- A character's backstory involves a fey patron, a promise made by a parent, a lost sibling or a name traded away.
- One region or one session inside another genre should turn strange: a ford where time slips, a feast in a hill, a stranger who will not say thank you.

## Tone pillars

- **Courtesy is armor and weapon.** Manners decide who leaves. Insults are wounds and thanks are debts.
- **Words are law.** What is said aloud binds, exactly as said, and loopholes cut both ways.
- **Beauty with teeth.** Show the wonder in full, then one wrong detail: the banquet is perfect and nobody casts a shadow.
- **Every gift has a price.** The price is personal and specific: a memory, a color, an hour of every day, the sound of your own name.
- **Fair, not kind.** The fey keep their word to the letter. They are rarely cruel without a rule, and never break one.

## The rules that matter most

1. **Give every fey being 1 to 3 binding rules, decided before play.** It cannot lie; it must answer any question asked three times; it cannot refuse a gift; it cannot cross salt; it must count spilled grain. Write them down. Players can learn them and use them.
2. **Write every bargain as a contract.** Exact wording, the price, the due date, the loophole, and what happens if it is broken. Read the wording aloud at the table. A bargain without a loophole is a trap; one with only the fey's loophole is a gotcha.
3. **Make prices personal without taking agency.** Take a memory, a sense, a skill for a season, a name, a year, a shadow. Never take a player's ability to play their character as they choose, and never take a price the table's safety limits rule out.
4. **Run hospitality as a system.** Guest and host both bind on entry: eating, naming, thanking and leaving each mean something specific. State the house rules in-world before they can bite.
5. **Plant the rules before they bite.** Every rule the players could break must be findable first: in a rhyme, a warning, a superstition, a story an NPC tells. Fairness makes the danger delicious instead of arbitrary.
6. **Let the clever win.** A good loophole, a precise question, a well-chosen gift should beat a stronger fey. Reward wordplay with real outcomes.

If the campaign has no fey yet and nothing says what they want from mortals, ask the DM one question first: what do the fey need from this world that they cannot take for themselves?

## Composing with other packs

- `genre-wilderness-hexcrawl`: the wild is where the borders thin. Make one region a fey crossing where weather is time (a night that lasts three days) and every ford has a toll paid in something strange.
- `genre-dungeon-crawl`: a hollow hill whose halls are rooms with etiquette instead of traps. Rooms bind by rules (whoever speaks first must serve) and the faction war is a court feud.
- `genre-gothic-horror`: the fey without the glitter. A changeling in the cradle, a family that made a bargain three generations ago, a debt collected from the grandchildren.
- `genre-political-intrigue`: fey courts are intrigue where lying is impossible, so everything turns on omission, precise phrasing and debts of hospitality.

## Building it in QuestMaster

- **Read first:** `get_campaign_overview`, `get_table_safety` (fey stories often touch compelled behavior, stolen children and coercive deals), and `search_campaign` for any existing fey, patron or curse. Read `get_party` and `get_character` for backstory bargains, which are player-written and only hooked with the DM's say.
- **Fey beings:** `upsert_npc` for each. Binding rules, true name and real want go in `secret` (DM-only); the beautiful appearance with its one wrong detail goes in appearance (player-visible). Give a fey that might fight a `set_npc_statblock`.
- **Courts:** `upsert_faction` per court, with its etiquette as `publicMission` and what it wants from mortals as `realAgenda`.
- **Bargains:** each is an `upsert_thread` with the exact wording, price and loophole in its description, urgency rising as the debt nears, and plannedSessionId set to the session it falls due. Each bargain also gets an `upsert_plot_node` with `link_plot_nodes` to the consequences of keeping and breaking it.
- **Rules players can learn:** each rhyme, warning or story is a `stage_secret`, aimed at the character most likely to know it (the one raised on the border, the bard, the warlock's patron whispering).
- **The otherworld:** an `upsert_area` with areaType planar for each fey realm, and one `upsert_location` per hall, glade or crossing. The dmNotes of each location record its local law (in this hall, whoever eats must stay until dawn).
- **Encounters:** `plan_encounter` with encounterType social or puzzle for feasts, riddle contests and negotiations, with success, partial and failure consequences written out. For a hunt or a broken truce, `propose_encounter` with theme fey for a starting group and `rate_encounter` to check it.
- Finish with `get_changeset`, recap in plain words, ask the DM, then `request_approval`.

## References

- Read [references/beats.md](references/beats.md) when outlining a bargain arc, a session in the otherworld, or a single offer scene.
- Read [references/npcs.md](references/npcs.md) when drafting fey nobles, tricksters, debt collectors, changelings or mortals who deal with them.
- Read [references/encounters.md](references/encounters.md) when planning a feast, a riddle contest, a hunt, a maze, a dance that will not end or a fight when etiquette breaks.
- Read [references/factions.md](references/factions.md) when building courts, mortal circles that trade with the fey, or those who ward against them.
- Read [references/lore.md](references/lore.md) when describing the otherworld, naming fey and places, writing contracts, rhymes and charms.
- Read [references/pitfalls.md](references/pitfalls.md) when bargains feel unfair, whimsy feels random, or the fey feel like elves with wings.
- Read [references/safety.md](references/safety.md) before drafting compelled behavior, coercive bargains, stolen children, lost identity or seduction, and whenever `get_table_safety` returns limits.

# Cosmic Horror: Beats

The signature structure is the investigation spiral. It is a loop the party runs again and again, and each pass starts one ring further out than the last. The party can step off at any revelation; the spiral keeps turning without them.

## The investigation spiral

One loop has six steps:

1. **Hook.** A local, human-sized oddity: a missing person, a wrong number in a ledger, a fisherman who came back speaking a little differently. It must look solvable.
2. **Legwork.** Interviews, archives, field visits. The party gathers clues from at least three directions. This is most of the session.
3. **Brush with the edge.** A short, sharp contact with the real thing: a sound under the floor, a figure on the ridge that is too tall, a page that reads differently the second time. It is survivable and it is not a fight with the entity.
4. **Revelation.** The clues add up to an answer. The answer is true, and it is smaller than the question it opens.
5. **Cost.** The investigator who carried the revelation takes a mark (see "Knowledge costs" below) and gets something useful with it.
6. **Wider frame.** The answer points outward: to an older case, a larger organization, a second site, a pattern across a century. That is the next loop's hook.

### The rings
Each loop widens the frame. A typical spiral moves through:
- **The house or the person** (who is missing, what happened in this room)
- **The town** (who else knew, what the town has always done)
- **The region or the institution** (a guild, a church, a family line, a map)
- **History** (it has happened before, every generation, and someone recorded it)
- **The outside** (what it actually is, glimpsed, never fully)

Most campaigns only reach the fourth ring. That is fine. The fifth is for finales, and only as a glimpse.

## Knowledge costs

At each revelation, offer the investigator who learned it a choice of two or three marks. Each mark gives an edge and a cost:
- **The listening:** they hear it nearby (a sense of direction toward the threat) and cannot sleep well near water.
- **The arithmetic:** they can read the wrong geometry (an edge on puzzles and navigation in strange places) and keep counting things compulsively, out loud, when stressed.
- **The name half-learned:** one ward or ritual becomes possible for them, and something now knows their name too.
- **The changed hand:** a small physical change that grants a minor ability and cannot be hidden from careful eyes.
- **The certainty:** they know one thing absolutely, and nobody believes them when they say it.
Build each mark as homebrew so QuestMaster handles the mechanics; this file only decides what the mark means.

## The small win

Before every session, write down one concrete victory the party can earn tonight:
- Rescue these three people before the tide turns.
- Destroy this copy of the book before the auction.
- Close this site so the village above it stops dreaming.
- Prove to the magistrate that the drownings are murders, so the next one is investigated.
A small win does not end the threat. It ends one harm, and the players should feel it land.

## Arc structure (4 to 6 sessions)

- **Session 1:** one full loop at the first ring. Ends with the first mark and the first glimpse of the second ring.
- **Sessions 2 to 4:** one loop per session, each a ring wider. The small wins get harder and more important. A faction (the cult, the suppressors, the institution) starts pushing back.
- **Final session:** the closing. The party cannot defeat the whole, but they can close the door that is open now. Offer two or three ways to close it, each with a cost, and one way to profit from it instead.

## Session structure

1. **Normal life** (5 minutes): the world as it should be, so the wrongness has something to stand on.
2. **The hook or the callback:** this session's oddity, or the consequence of last session's mark.
3. **Legwork:** two or three scenes, each with clues pointing at the same conclusion from different directions.
4. **The turn:** the brush with the edge, at roughly two thirds of the session.
5. **The choice:** go deeper (revelation and cost) or close the door on what they have (small win, no new knowledge).
6. **Aftermath:** what the town, the NPCs and the investigators look like the next morning.

## Scene structure: the interview

1. **Ask:** the party asks a direct question.
2. **Observe:** the NPC answers, and something in the answer is off (the wrong tense, a detail they could not know).
3. **Notice:** the party presses on the detail.
4. **Cost:** the NPC tells them, and telling costs the NPC something visible (they weep, they forget the party's names, they ask the party to leave and lock the door).

## Worked example: The Survey of Marrow Fen

**Hook.** A survey party from the Cartographers' Hall of Brannock went into Marrow Fen to chart a drainage route and never came back. Their patron hires the party to find them, or their maps.

**Loop 1, the camp (ring: the person).** The camp is intact and tidy. The surveyors' field maps are perfect, more accurate than the land itself, and one shows a valley that is not there. Brush: at dusk, a surveyor's chain stretches tight into the reeds, held from the other end. Small win: the youngest surveyor, found alive in a reed-cutter's hut, babbling measurements. Mark offered: the arithmetic.

**Loop 2, the village (ring: the town).** Ebbing Cross, at the fen's edge, has never put the valley on any map, by custom, and hangs reed charms in every window. The headwoman, Orla Fenn, says the charms are "to keep it untidy". Revelation: the valley exists at night, and it is only there as long as nobody measures it. Small win: replace the charms the surveyors' work burned out before the next new moon.

**Loop 3, the Hall (ring: the institution).** The Cartographers' Hall has a sealed archive of fen surveys, two hundred years of them, each more complete than the last. Every survey was commissioned by the same anonymous subscriber. Revelation: each accurate map makes the valley more permanent; the Hall has been building it, one survey at a time. Small win: steal and burn this year's master map. Mark offered: the name half-learned (the subscriber's).

**Loop 4, the history (ring: the past).** The first map in the archive is not a map of the fen. It is a map of the valley, drawn before the fen existed, in the Hall founder's hand. Brush: the founder's portrait is unfinished, and the unfinished part is still being painted, slowly, by no one.

**Closing.** The party can unmake the valley (burn every survey, and the Hall loses two centuries of honest work and the livelihood of everyone in it); seal it (a perpetual duty for Ebbing Cross and one investigator who must stay); or chart it fully (the subscriber gets what it wants, and the party gets a door). The valley remains in the world either way, smaller or larger. The surveyors are not all coming back. One is, if the party asks the right way.

## Building it in QuestMaster

- One `upsert_plot_node` per revelation, linked outward with `link_plot_nodes`; the small win for each loop sits in that node's DM notes.
- Clues as `stage_secret`, three per revelation, each aimed at a different character.
- The waking (the valley growing) as an `upsert_thread` with urgency that rises each loop the party does not close.

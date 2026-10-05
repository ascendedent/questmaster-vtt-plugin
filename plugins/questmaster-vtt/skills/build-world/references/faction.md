# Faction template

Write this in chat first, then draft it. The split that matters: `description` and
`publicMission` reach players; `realAgenda` never does.

## Header

| Field | Value | Goes to |
|---|---|---|
| Type | guild, order, government, cult, criminal, military, political, religious | `factionType` |
| Scope | local, regional, national, continental, planar | `scope` |
| Operating style | how they act: secretive, bureaucratic, aggressive (not a moral verdict) | `description` (as seen), `realAgenda` (as it is) |
| Primary base | where their power is centered | `primaryBaseLocationId` (a location) |
| Standing with the party | hostile, unfriendly, neutral, friendly, allied | `partyStanding` |

## Purpose

- **Public mission** (`publicMission`): what they say they are for, in their own words.
- **Real agenda** (`realAgenda`): what they are actually working toward.

Four ways the two can relate (pick one, say which in `realAgenda`):
- Aligned but ruthless: they mean it, and will do anything for it.
- A cover: the mission is a mask for something else entirely.
- Drifted: they meant it once; the leadership now serves itself.
- Captured: the members mean it, a hidden inner circle does not.

Generic: "Public: protect trade. Real: control trade."
Specific: "Public: the Honest Scale certifies every weight in the market so no buyer is
cheated. Real: their master scales read light by a hair, and the difference has funded the
guild's private watch for thirty years."

## History

- Founded: when and by whom.
- Founding moment: the event or cause that made them (public version in `description`,
  the truth in `realAgenda` if they differ).
- Turning point: what changed who they are.

## Structure and leadership (`realAgenda`; leader and members as NPCs)

- Leadership: title and name. Search for an existing NPC; otherwise `upsert_npc` with
  `factionId` set, then patch the faction's `leaderNpcId`.
- Hierarchy: cells, ranks, councils, a family.
- Recruitment: volunteered, born into, tested, bought, pressed.
- Loyalty levers: ideology, fear, pay, blackmail, real community. Name the one that breaks
  first under pressure; that is how the party turns a member.

## Resources and power (`realAgenda`)

- What they control: land, money, information, force, magic.
- What they need right now: their current pressure or shortage. This drives their next move.
- Who owes them: other factions, nobles, institutions. Each debt is a lever the party can
  pull or cut.

## Relationships

There is no ally or rival field. For each existing faction worth naming:
- Ally: why, and how stable. Written in both factions' `realAgenda`.
- Rival: the specific point of conflict. One `upsert_thread` with both factions in
  `connectedFactionIds`, so the DM sees it on the board.
- Watched: who they monitor or could be swayed. A line in `realAgenda`.

## Internal tensions

- A faction within the faction: a splinter, an ideological divide, a succession struggle.
- The argument they keep having, which shapes their decisions. Give each side a named NPC
  when the DM wants depth.

## How the party meets them

- First contact: a job offer, an obstacle, a rumor, a recruiter.
- What they want from the party.
- What the party could want from them: money, information, protection, legitimacy.
- Starting `partyStanding`: usually neutral; say why if not.

## Story hooks (one `upsert_thread` each)

1. Asset: a reason to work with them.
2. Obstacle: a reason they stand in the way.
3. Surprise: something that shows them in a new light (often the internal split).

## Variant: a religion

- A faith is a faction (`factionType: "religious"`): doctrine and rites in `description`,
  what the clergy actually believe or hide in `realAgenda`, a holy site as its
  `primaryBaseLocationId`.
- Give it one rite a traveler notices, one schism, and one miracle that may not be one.
- Myths, scripture and prophecy come from `generate-lore`.
- Example: the **Keepers of the Second Hearth**, who tend a fire said to have burned since
  the first winter. Real agenda: it went out eleven years ago, and the high keeper relights
  it nightly in secret. The schism: the novices who suspect.

## Variant: a political landscape

- 3 to 5 factions, each with a leader NPC and a base.
- One sentence per pair that matters: who wants what from whom.
- One `upsert_thread` per live conflict, connecting both factions and the NPCs in the middle.
- A pressure that is changing the balance right now (a succession, a famine, a new trade
  road), so the board moves even if the party does nothing.
- Leave the party at least three sides to choose from, including "none of them".

## Variant: a cultural detail of a people

- A custom (`description` of their area or faction), what it really protects or hides
  (`dmNotes` or `realAgenda`), and what happens to someone who breaks it.
- Common knowledge as staged secrets, so the DM can hand it to a character who grew up there.

## Worked example (compressed)

`upsert_faction`: **The Honest Scale**, `factionType` guild, `scope` regional,
`publicMission` and `realAgenda` as above, `partyStanding` neutral.
`upsert_npc`: **Master Weigher Odran Pask**, `factionId: "faction:1"`; then
`upsert_faction {id: "faction:1", leaderNpcId: "npc:2"}`.
Thread: "Short weight" (asset: they hire the party to find a forger of their seals;
surprise: the forger is the faction's own reform wing).

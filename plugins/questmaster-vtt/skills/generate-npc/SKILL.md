---
name: generate-npc
description: "A workflow for creating a play-ready NPC in a QuestMaster campaign, with a performable voice, a want, a fear, a secret and hooks across the campaign, drafted with upsert_npc and linked to its faction and location, plus optional combat stats through set_npc_statblock and an optional portrait. Use when the DM asks for a new character, ally, villain, contact, quest-giver or background figure, a small cast for a location, or a fuller version of an existing NPC."
---

# Generate NPC

The DM gets an NPC they can play tonight: a face players remember, a voice the DM can
perform, a want, a fear, a secret and three hooks, drafted into QuestMaster and linked
to where they live and whom they serve.

## Use this when

- "I need a fence in the dock ward", "who runs this inn?", "give me a villain for the next arc".
- A location needs a small cast (3 to 5 people who already have opinions about each other).
- An existing NPC is only a name and a role and needs depth (read it, then patch it by id).

## Steps

1. **Read.** `get_campaign_overview` for tone, setting and active threads. `search_campaign`
   for the name you plan to use and for the role ("smuggler", "abbot"), so you don't
   duplicate someone who already does that job. `get_entity` on the faction and location
   the NPC will belong to. `get_party` when the NPC should matter to a particular
   character (backstories are player-written: hooks only). `get_table_safety` if shared.
2. **Parse the request** into role (story function), location, relationships (an NPC, a
   faction, a character) and a tone flag (straight, comic, tragic, menacing). If one
   essential piece is missing, ask one question with two or three suggested answers:
   "Is the harbormaster on the party's side, against them, or for sale?"
3. **Write the profile** from [references/npc-profile.md](references/npc-profile.md) and
   show it in chat. If the request was loose, offer one alternative take (softer or more
   dangerous) and let the DM pick.
4. **Draft it** as below. Link existing factions and locations by id. Create a new faction
   or place only if the DM asks (use `build-world` for it).
5. **Stats only if they might fight.** Adopt a monster's block or give a custom one with
   `set_npc_statblock`. A purely social NPC gets none.
6. **Recap and ask.** `get_changeset`, then tell the DM in plain words what is new, which
   fields players can see and which stay DM-only. Ask, then `request_approval`. Nothing is
   saved until it returns status `applied`.
7. **Portrait, if wanted.** `generate_image` reads the saved NPC, so call it with the real
   NPC id after approval, never a draft ref. It runs on the owner's own image key at their
   cost, a few per hour. The DM sees the picture before approving that second small draft.
8. **Hand back.** Introducing the NPC, performing the voice, pushing any staged secret about
   them and changing their status as play unfolds all stay the DM's.

## What to produce

One profile per NPC (full template and examples in the reference): name, role, species,
status, relationship to the party; appearance (3 to 5 visual sentences with one detail
that contradicts expectations); personality (demeanor, core trait, flaw, speech pattern);
motivation (immediate want, long-term drive, fear); a secret scaled to their weight, with
who else knows and what exposure costs; at least one relationship to an existing NPC or
faction; three hooks (immediate, mid-campaign, late payoff); a combat concept or "social
NPC, no stats".

The bar: the speech pattern is a habit the DM can perform in one line ("answers every
question with a price"), never an adjective ("gruff"). The flaw causes friction at the
table. The fear is tied to something that exists in this campaign.

## Drafting it

- `upsert_npc`, one call per NPC; keep the ref it returns (like `npc:3`):
  - `name`, `role`, `species`, `status`, `relationshipToParty`.
  - `appearance`: what the party sees. Player-visible, so no hidden identity and no tell
    that only makes sense once the secret is known.
  - `personality`: `{demeanor, coreTrait, flaw, speechPattern}`. Send all four; the block
    replaces as a whole. `motivation`: `{immediate, longTerm, fear}`, all three.
  - `secret` (DM-only): the secret, who else knows, what happens if it comes out.
  - `notes` (DM-only): relationships, playing tips, the reasoning behind the stats.
  - `plotHooks`: the three hooks as a list (a sent list replaces the old one).
  - `factionId`, `locationId`: existing ids or refs from this draft. `locationId` is a
    location (a room or site), not an area.
- `set_npc_statblock` with `npcId` (a draft ref works here):
  - `adopt: {kind: 'srd' | 'bestiary', ref}` for a stock fighter (a guard captain, a cult
    zealot). Find candidates with `search_monster_sources`.
  - `custom: {cr, hp, ac, speed, abilities {STR, DEX, CON, INT, WIS, CHA}, traits, actions}`.
    Each action names its kind (attack, save or other), its driving ability and plain
    damage dice with no modifier. QuestMaster computes to-hit, save DC and damage.
- A hook bigger than the NPC: `upsert_thread` with `connectedNpcIds: ["npc:3"]` plus the
  faction and location ids it touches.
- A clue players can learn about them: `stage_secret` with `subjectKind: "npc"`,
  `subjectId` the ref, and `audienceCharacterIds` aimed at the character most likely to notice.
- Patching an existing NPC: leave a field out to keep it, send `null` to clear it. `notes`
  and `secret` are replaced whole, so read them with `get_entity` and send the full new text.

## Don'ts

- Don't write a to-hit bonus, save DC or damage modifier anywhere, not even in `notes`.
  `set_npc_statblock` computes them from the abilities and CR.
- Don't leak the secret through a player-visible field: "Brother Cale (secretly the
  forger)" as a name, or "ink stains matching the forged seals" in `appearance`.
- Don't call `generate_image` with a draft ref or before the appearance is approved.
- Don't rewrite a player character's backstory as fact. A tie to a character's past goes in
  `notes` as an option for the DM to accept.
- Don't hang the NPC on a faction or place you invented without asking.
- Don't say the NPC is saved before `request_approval` returns `applied`.

## Pairs well with

- `style-npc-voice` to turn the speech pattern into sample lines the DM can read aloud.
- The campaign's `genre-*` pack: its NPC archetypes give twists that fit the tone.
- `build-world` for the faction or place they belong to, `design-encounter` if they will
  fight, `generate-lore` if they guard or seek knowledge, `develop-plot` to turn their hooks
  into beats.

## References

- Read [references/npc-profile.md](references/npc-profile.md) when writing the profile: the
  full template, generic vs specific examples, speech patterns, secret scaling, adopt vs
  custom stats, and building a cast for one location.

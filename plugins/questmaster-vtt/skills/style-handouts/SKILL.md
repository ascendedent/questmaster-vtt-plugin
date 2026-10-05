---
name: style-handouts
description: Style rules for player handouts written as physical objects in the world, such as letters, wanted posters, notices, map keys, receipts and manifests. Gives the assistant an object frame (what it is written on, its condition, who wrote it and how players can tell), a layout per handout type, a planted lead, and a separate DM note. Use when the party will find, receive or be shown something written or drawn that the DM wants to read out, show on screen or print.
---

# Handouts

A handout is an object before it is a text. The paper, the stains and the handwriting are clues the players can hold, so frame the object first and let the words sound like the person who wrote them.

## Use this when

- The party finds, steals, receives or is shown something written or drawn.
- The DM wants a prop to read out, put on the table screen or print: a letter, a wanted poster, a notice, a map key, a receipt, a manifest, a playbill.
- An in-world document is ready to hand over. Write its voice with `style-in-world-documents`; this skill makes it an object.

## The rules

1. **Frame the object first.** A short header for the DM: what it is written on (vellum, cheap rag paper, the back of a tavern bill, a strip of sailcloth), its size and condition (folded into eighths, water-stained along one edge, torn from a nail), its marks (a wax seal, an inky thumbprint, a stamp), and who wrote it and how the players can tell (a clerk's careful hand, a scrawl, someone writing left-handed in a hurry).
2. **The writer is a person.** Literacy, haste, trade and relationship to the reader shape every line. A frightened apprentice writes short and crosses things out; a magistrate's notice is formal and complete. Misspell only on purpose, once or twice, and keep it readable.
3. **Short enough to read at the table.** Letters under about 150 words, posters under about 60, map keys 5 to 10 entries, a notice one paragraph plus its penalty.
4. **Use the type's layout.**
   - Letter: a date in the world's reckoning, a greeting, the body, a signature (or a telling lack of one), and one personal detail that shows the relationship.
   - Wanted poster: headline, name or alias, two or three identifying features, the crime as the issuer tells it, the reward and its conditions, the issuing authority and date.
   - Map key: symbols, labels in the mapmaker's voice, one entry that is wrong or out of date, and a note in a later owner's hand.
   - Notice or decree: an opening formula, the rule, the penalty, the authority and the date.
5. **Plant at least one lead in plain sight.** A seal that matches someone's ring, a word only one NPC misspells, a date that breaks an alibi, a crossed-out line still legible. Name what it points to in the DM note.
6. **Two parts, never mixed.** The handout is what the players see. The DM note says who really wrote it, what is true, which lead is planted, and which character can notice or read what. Nothing from the DM note leaks into the handout, and the handout never knows more than its writer could.
7. **Make it survive copy and print.** Plain text, no wide tables, damage marked in square brackets ([torn], [ink run]), and any picture described in one bracketed line the DM can sketch or describe aloud.
8. **Respect the table.** Gore, threats and cruelty follow `get_table_safety`. Veiled content is implied by the object (a torn corner, a name scratched out), never depicted; lines never appear at all.

Hand it over in this shape:

```
**Handout: [type], [short name]**
Object: [material, size, condition, marks]
Written by: [who, and how the players can tell]

> [the handout text, exactly as the players see it]

**DM note (never shown to players)**
- Truth: ...
- Planted lead: ... (points to ...)
- Who notices what: ...
```

## Checklist before you hand it over

- [ ] Material, condition, marks and writer are all stated.
- [ ] The voice fits the writer's literacy, trade and haste.
- [ ] The length fits the type.
- [ ] At least one planted lead, with its target named in the DM note.
- [ ] No DM-only fact in the handout text.
- [ ] Damage and pictures are marked in square brackets.
- [ ] Names, dates and places match `search_campaign` and the campaign's maps.
- [ ] Content respects the table's lines and veils.

## Where it goes in QuestMaster

- Run `search_campaign` for the author, every name and every place on the handout. For map keys, check `get_map_outline` or `get_continent_gazetteer` so names and directions agree with the campaign's maps.
- Every handout is a staged secret via `stage_secret`: the handout text only, aimed at the character who finds or receives it (or the whole party). It waits until the DM pushes it in the app. The DM note never goes into the secret.
- Record where the handout turns up: in the location's DM notes via `upsert_location`, or in the beat where it appears via `upsert_session_beat`.
- A map key can pair with map labels via `annotate_map`, which stay hidden from players until the DM shows them.
- Then `get_changeset` and `request_approval`.

## References

- Read [references/registers.md](references/registers.md) when choosing what kind of object and writer fit the campaign's tone.
- Read [references/examples.md](references/examples.md) before the first handout for a campaign, and whenever a draft is text with no object or gives the answer away.

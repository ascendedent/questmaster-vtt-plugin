---
name: generate-lore
description: "A workflow for writing in-world lore for a QuestMaster campaign (histories, myths, prophecies, rumors, inscriptions, letters, doctrine) in the voice of a source inside the world, with a DM truth layer beneath it, and for placing each piece where QuestMaster keeps it, since lore has no table of its own. Use when the DM asks for history, legends, a prophecy, rumors, an in-world document or the background truth behind a place, person or object."
---

# Generate Lore

The DM gets lore that sounds like someone in the world wrote or said it, bias and gaps
included, plus a private layer saying what is true, what is distorted and why, with each
piece drafted where QuestMaster will surface it at the right moment.

## Use this when

- "What do the locals say about the hill where no birds land?"
- "Write the inscription on the vault door", "a prophecy the cult misreads", "the temple's
  official history of the war".
- Tavern rumors, a letter found on a body, the myth behind a monster, a faith's doctrine.

## Steps

1. **Read.** `get_campaign_overview`. `search_campaign` for the subject and for whoever would
   be the source or keeper; `get_entity` on each. Their existing `secret`, `dmNotes` and
   `realAgenda` are canon: the truth layer must agree with them. `get_plot_graph` when the
   lore should feed a thread or a reveal. `get_party` (and `get_character` for languages)
   when a particular character should be the one to find it.
2. **Parse** the subject, the form (history, myth, prophecy, rumor, document, doctrine), the
   delivery (book, NPC speech, inscription, dream, song, official record) and the source with
   its bias. If the subject or the delivery is unclear, ask: "What is this lore about, and
   how will the players find it?"
3. **Write both layers** from [references/lore-forms.md](references/lore-forms.md). For the
   voice of the in-world layer (diction, bias, damage, what the source assumes), follow the
   `style-in-world-documents` skill.
4. **Place it.** Decide where each piece lives (below) and tell the DM before drafting.
5. **Draft it**, linking each piece to its subject by id or ref.
6. **Recap and ask.** `get_changeset`, a summary marking which pieces players can come to
   see and which are DM-only, then ask, then `request_approval`. Nothing is saved until it
   returns `applied`.
7. **Hand back.** Pushing a staged secret, pushing an item's lore, showing a plot beat and
   handing out a printed copy are the DM's moves at the table.

## What to produce

- **Header**: subject, form, source, delivery, era.
- **In-world layer**, sized to its form: a rumor is 1 to 2 sentences, an inscription 1 to 4
  lines, a prophecy 4 to 8 lines, a myth 1 to 3 paragraphs, a chronicle or letter 2 to 5
  paragraphs. Plus what the form needs: variants (myth), interpretations and a dangerous
  reading (prophecy), what it gets right and wrong (rumor), legibility and script (document).
- **DM truth layer**: what is true, what is distorted, why the distortion persists,
  connections (a thread, the NPC who knows the real version, what digging uncovers), how
  to discover it (a skill and a difficulty; the DM sets the number), delivery notes.

## Drafting it

Lore has no table of its own. Split every piece by who may see it:

| Piece | Where it goes | Who sees it |
|---|---|---|
| Text players find, overhear or are told | `stage_secret`: `title`, `body` (the in-world text), `subjectKind` + `subjectId` (or `free` + `subjectLabel`), `audienceCharacterIds` | Nobody until the DM pushes it |
| The lore of an object | `upsert_magic_item` `lore` | Players, once the DM pushes it |
| The truth about an object | the item's `secret` | DM only |
| The truth about a place | `upsert_location` `dmNotes` | DM only |
| The truth about a power or faith | `upsert_faction` `realAgenda` | DM only |
| What one person knows or hides | `upsert_npc` `secret` or `notes` | DM only |
| The moment the party learns it | `upsert_plot_node` (`arcId`, `title`, `description`), clues joined by `link_plot_nodes` | Title and description, if the DM shows the beat |
| A mystery that runs for sessions | `upsert_thread` with connected NPC, faction and location ids | DM's prep |

- Aim each staged secret with `audienceCharacterIds` at the character most likely to find
  it (the one who reads the old script, the cleric in the temple archive). Empty means the
  whole party. Several rumors work best as several secrets aimed at different characters.
- A beat's `description` says what the party learns, never the deeper truth they won't.
- `dmNotes`, `realAgenda`, `secret` and `notes` are replaced whole: read the record with
  `get_entity`, add your part, and send the full text.
- Pushed secrets, pushed item lore and beats already shown to players can't be changed
  here; the tools refuse. Draft a new piece instead, or tell the DM to edit it in the app.

## Don'ts

- Don't write the truth into a player-visible field. The in-world text may be wrong on
  purpose; the correction lives in a DM-only field.
- Don't let the truth layer contradict canon. If a record disagrees with the request, flag
  it and offer a version that fits.
- Don't write a prophecy that can only mean one thing, or one that dictates what a player
  character will do. Prophecy offers readings; the players choose.
- Don't make the source explain its own world ("as everyone knows, the war began..."). It
  assumes its context; `style-in-world-documents` has the rest.
- Don't quote or echo published books, scriptures or settings. Invent.
- Don't say anything is saved before `request_approval` returns `applied`.

## Pairs well with

- `style-in-world-documents` for the in-world voice, `style-handouts` for a printable copy,
  `style-read-aloud` when an NPC speaks it.
- The campaign's `genre-*` pack for its lore textures, naming and sensory palette.
- `generate-npc` for a keeper or seeker of the knowledge, `build-world` for the place or
  faith, `create-item` for an object the lore is about, `develop-plot` for clue chains.

## References

- Read [references/lore-forms.md](references/lore-forms.md) when writing: the template for
  each form, the truth layer and the delivery notes.
- Read [references/placing-lore.md](references/placing-lore.md) when deciding where pieces
  go: a worked example split across tools, and clue chains that lead to a reveal.

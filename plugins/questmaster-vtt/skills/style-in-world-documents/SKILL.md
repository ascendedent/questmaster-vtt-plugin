---
name: style-in-world-documents
description: Style rules for texts that exist inside the game world, such as chronicles, sermons, decrees, ledgers, inscriptions, songs and letters between NPCs. Gives the assistant the voice-of-source discipline, a biased narrator writing in period diction, plus a separate DM truth layer that says what is true, what is distorted and who benefits. Use when the party will read, find or be told written lore, or when an item, a place or an event needs its history told from inside the world.
---

# In-world documents

Lore lands harder when someone in the world wrote it for a reason. The text the players read is a source with a slant and blind spots; the truth layer underneath tells the DM what actually happened.

## Use this when

- The party will read, find, steal or be told a history, a prophecy, a sermon, a decree, a ledger, a diary or an inscription.
- The DM wants lore delivered through a source instead of narration.
- An item, a monument or a ruin needs its story told the way the world tells it.
- Two factions should disagree about the same event: write both sources over one truth layer.
- For the physical object itself (paper, seal, condition), pair this with `style-handouts`.

## The rules

1. **Name the source before you write.** Who wrote or speaks it, when, for whom, and what they want the reader to believe. Put that in a one-line source tag. A text with no author has no bias, and a text with no bias is an encyclopedia entry.
2. **Give the narrator a slant and a blind spot.** Every source praises something, omits something and cannot know something. A conqueror's chronicle skips the burned villages; a temple record credits the god; a toll ledger counts a flood in lost fares. Show bias through word choice (the rebels, the Free Wardens, the rabble), not through confessions.
3. **Period diction, not costume.** Fit the words to the writer's era, trade and schooling: titles, formulas ("Let it be known", "Item:", "Here rests"), local measures (a day's ride, the third bell, a cask of salt). One or two old-fashioned turns per paragraph carry it. No thee-and-thou soup, no "olde" spelling; it must still read aloud cleanly.
4. **Fit the form to the medium.** An inscription is a dozen words; a ledger is entries and sums; a letter has a date, a greeting and a signature; a decree has a formula, a penalty and a seal. Most found texts run under 150 words. Mark damage with [torn] or [illegible], and put it where it hurts: on a name, a date, a number.
5. **Always write the DM truth layer, separately.** What is true; what is distorted and how; why the distortion exists (who benefits); what the text points to. The in-world text never contains a fact its author could not know.
6. **Canon first.** Run `search_campaign` on the subject. If canon settles what happened, the truth layer follows canon and the distortion belongs to the source. If canon is silent, offer the DM two possible truths and ask which to keep; never lock new canon unasked.
7. **Make it a clue, not a lecture.** Each document gives the party at least one thing to act on: a name, a place, a date, a detail that contradicts another source. A document the party can ignore without losing anything is decoration; keep those very short.

Hand it over in this shape:

```
**[Document type]: [title or opening words]**
Source: [who], [when], for [whom], to [purpose]
Found: [how the party meets it]

> [the in-world text]

**DM truth layer (never shown to players)**
- True: ...
- Distorted: ... (and how)
- Why: ... (who benefits)
- Points to: ... (thread, NPC, place or object)
```

## Checklist before you hand it over

- [ ] The source tag names an author, a date, an audience and a purpose.
- [ ] The text holds at least one slant and one omission.
- [ ] The author never knows something they could not have known.
- [ ] Diction fits the writer and reads aloud without stumbling.
- [ ] Length and layout fit the medium; any damage sits on something important.
- [ ] The truth layer is separate, marked DM-only, and agrees with canon.
- [ ] Any new truth was offered to the DM as a choice, not assumed.
- [ ] The document gives the party at least one lead.
- [ ] Every proper noun is original and matches `search_campaign`.

## Where it goes in QuestMaster

- Read `get_campaign_overview` for tone and setting, then `search_campaign` for the subject, the author and every name the text mentions.
- **Text the players receive:** stage the in-world text as a secret via `stage_secret`, aimed at the character who finds it or can read its script (or at the whole party). It stays staged until the DM pushes it in the app. The truth layer never goes into the secret.
- **An item's history:** put the in-world account in the item's lore via `upsert_magic_item` (players see lore once the DM pushes it) and the truth layer in the item's `secret`, which is DM-only.
- **Fixed texts in a place** (an inscription, a plaque, a mural's caption): put the text and its truth layer in the location's DM notes via `upsert_location`.
- If the truth layer opens a lead the DM wants to track, offer a thread via `upsert_thread` or a plot beat via `upsert_plot_node`, and ask before adding either.
- Then `get_changeset` and `request_approval`.

## References

- Read [references/registers.md](references/registers.md) when choosing which kind of source fits the campaign's tone, or when writing two sources that disagree about one event.
- Read [references/examples.md](references/examples.md) before the first document you write for a campaign, and when a draft sounds like an encyclopedia or gives the twist away.

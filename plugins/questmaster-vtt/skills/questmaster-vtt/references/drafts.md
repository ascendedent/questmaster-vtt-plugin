# Drafts, approval and undo

Nothing you write reaches the campaign until the campaign's owner approves it. Each
write tool checks your input and adds it to this connection's draft.

## Refs: linking things you just made

A create returns a ref like `npc:3` or `faction:1`. Use the ref anywhere an id goes in
later calls of the same draft:

```
upsert_faction {name: "The Salt Ledger", ...}            -> faction:1
upsert_npc {name: "Odile Marsh", factionId: "faction:1"} -> npc:2
upsert_thread {title: "Who skims the salt tithe?", connectedNpcIds: ["npc:2"], connectedFactionIds: ["faction:1"]}
```

At approval every ref becomes a real id. A patch to something you created in this
draft folds into its create.

## Patch semantics

- Leaving a field out keeps its current value.
- Sending `null` clears it.
- List fields (connected ids, links, an item list) replace the whole list when sent:
  read the record first and send the full list you want.
- Some blocks replace as a whole too (an NPC's `personality`, a monster's
  `statBlock`): send every key.

## Deletes

Run `delete_entity` with `dryRun: true` first. It reports what else the delete would
remove or unlink, and drafts nothing. Tell the DM before drafting the real delete.
Some deletes are refused on purpose (a played session's beats, a secret already
pushed, a fight that ran, a shop open at the table).

## The approval link, every time

Every draft call returns `approveUrl`, the page where the DM reviews and approves the
open draft (`request_approval` and `get_changeset` return it too). Any message that
says something is drafted, pending, or waiting for approval includes that link as a
clickable URL, in the same message. That holds mid-build too: if you stop to ask a
question with changes already drafted, the link goes in the question. The DM can press
Ready to approve on that page at any time; anything you draft after that starts a new
draft with a new link.

## Asking for approval

1. `get_changeset`: read your draft back.
2. Recap it for the DM in plain words: what's new, what changes (old and new), what is
   deleted, and anything players could come to see. Flag judgment calls you made.
3. Ask whether to send it. Adjust or `discard_changes` (with `changeSeqs` for only some
   changes) if they want.
4. `request_approval`. Two outcomes:
   - The client can show the DM a confirmation in the chat: their answer applies it.
     Report the status you get back.
   - Otherwise you get a link to the Agent changes page. Give it to the DM; they can
     approve all, approve some, or discard.
5. Only `status: applied` means saved. Until then say "drafted" or "waiting for your
   approval".

After `request_approval`, the draft is frozen. New writes start a new draft. If the DM
discarded a frozen change set, its drafts are gone; don't refer to their refs again.

## Undo

`undo_changeset` asks the owner to roll back a change set this connection drafted and
they approved. It changes nothing by itself: the DM confirms in the chat or on the
linked page. If something was edited since, the DM gets a second confirmation. Use
`list_agent_history` to find earlier change sets.

## When a write is refused

The error says why; it is usually a guard working as intended (a fight already
started, a map on the players' screens, a beat shown to players). Explain it to the DM
in one sentence, say what they can do in the app instead, and offer an alternative
draft. Don't retry the same call, and don't invent app features that would get around
it.

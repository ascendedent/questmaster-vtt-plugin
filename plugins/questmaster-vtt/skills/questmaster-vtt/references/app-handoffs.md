# What stays the DM's, and how to hand it over

You prepare; the DM runs the table in the QuestMaster app. These actions are theirs,
and the tools refuse them by design. When a task ends at one of them, finish your
draft and tell the DM the exact step.

| The DM wants | You draft | The DM does in the app |
|---|---|---|
| Players to learn a secret | `stage_secret`, aimed at the right characters | Pushes it (Push to players) |
| A fight to happen | `plan_encounter`, rated, on its map | Presses Start on the encounter |
| Something on the TV | `save_monitor_preset`, `build_cue_list` | Fires the cue at the table |
| Players to shop | `upsert_shop` with its shelf | Opens the shop |
| A session marked played | `save_session_recap`, thread updates | Presses Complete Session |
| A character to get an item or pack | `upsert_magic_item` (`intendedForCharacterId`), `define_equipment_pack` | Hands it over |
| A map shown to players | annotations and exits on it | Puts it on the players' screens |

## Wording the handoff

- One line per step, in the order they'll do it: "Approve the draft (link above), then
  on Session 8 push the two secrets, then fire the first cue when they reach the gate."
- Name things as they appear in the app (the NPC's name, the session's title).
- Never say a step happened. You can't see the table; ask the DM if you need to know.

## Mid-session requests

If the DM asks for help during play: use `run-improv` for options; draft only what they
ask to keep; and remember that a fight in progress, a beat already shown, a shop that is
open and a map on the players' screens can't be changed from here. During a fight the
DM adds or removes combatants from its run tracker in the app.

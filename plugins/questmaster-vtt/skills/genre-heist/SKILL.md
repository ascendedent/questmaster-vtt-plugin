---
name: genre-heist
description: Genre pack for heist campaigns and single jobs, built on target, crew, plan, complication and twist, with legwork sessions, the inside man, and concrete steps for drafting the job in QuestMaster. Use when the party is planning a robbery, infiltration, swap, con or extraction from a guarded place, or when the DM asks for a vault, a gala to crash, a crew of specialists, or a session where the plan is the main event.
---

# Heist

Play feels like a clock ticking under a plan the players are proud of, and the joy of watching it bend without breaking.

## Use this when

- The tone or setting text mentions thieves, a crew, a vault, a job, a score, a fence, a con, or a city full of locked doors.
- The DM says "they want to rob the bank", "the party has to steal it back", or "I need a gala they can infiltrate".
- The party has a rogue who keeps asking about floor plans, or the group already argued about a plan for twenty minutes and loved it.
- Something the party needs is held by someone who will not give it up, and fighting through is not an option.

## Tone pillars

- **Competence is the fantasy.** The crew is good at this. Complications test how they adapt, not whether they are clever enough.
- **Preparation pays.** Every hour of legwork shows up later as a door that opens, a guard who looks away, a uniform that fits.
- **The clock is always running.** Shift changes, the bell at midnight, the coach at dawn. Time pressure turns a puzzle into a heist.
- **Nobody is quite who they say.** The client, the mark, the inside man and sometimes the crew have a second story.
- **The getaway is part of the job.** Getting out, and living with the heat afterward, matters as much as getting in.

## The rules that matter most

1. **Start with the target, then its owner.** A target is a thing, a reason it matters, and a person who loses it. Write down what happens in the world the morning after it goes missing, before designing a single lock.
2. **Make legwork a session, not a montage.** Offer more legwork options than there is time for. Each one yields a concrete asset (a uniform, a guard rota, a key impression, a contact) and costs time, money or heat. The plan is built from what they found.
3. **Cap planning, then let preparation arrive late.** Give planning a time limit, then allow flashbacks during the job ("we bribed the cook last week") paid for with an asset from legwork or a check made now that costs something if it goes badly.
4. **One complication per phase, aimed at an assumption, never at competence.** The rota changed, a guest arrived early, the vault was moved. Each complication leaves at least two ways through. Never negate the plan outright.
5. **Plant a twist the crew can use.** The twist reframes the job (the client lied, the prize is a fake, someone else is robbing the place tonight). Seed it with 2 or 3 clues in legwork so it lands as a reveal, not a rug-pull, and make it an opportunity as well as a threat.
6. **The inside man is a person, not a key.** Give them a want, a fear, one reason to flip and one reason to stay loyal. Their loyalty is a thread that can break either way, and the crew's choices decide which.

If the target or the reason the crew wants it is missing, ask the DM that one question before drafting.

## Composing with other packs

- `genre-political-intrigue`: the prize is leverage (a ledger, a seal, a hostage letter) and the client is a faction. The fallout is political, and the debts the crew incurs are logged as favours.
- `genre-mystery`: run the clue graph backwards. Every trace the crew leaves is a clue an investigator NPC can follow; let the players see the investigation closing in during the fallout.
- `genre-gothic-horror`: rob the dead. The vault is a crypt, the security is a curse, and the inside man is a ghost with a price.
- `genre-swashbuckling`: the job with rooftops and rapiers. When it goes loud, let it go loud with style, and run the getaway as a chase across rigging, rooftops and market awnings.

## Building it in QuestMaster

- Read `get_campaign_overview`, `get_table_safety` and `search_campaign` for the target, its owner and any existing crew contacts. Read `get_party` to see who is the face, the burglar and the muscle, and which backstories connect to the target.
- Draft the target as an `upsert_location` (or an `upsert_module` with `upsert_area` entries for a large complex). Mark each security layer with `annotate_map`: guard posts, wards, alarm bells, the vault, all hidden until shown.
- Draft the owner, client, fixer and inside man with `upsert_npc`. Put the inside man's true loyalty, breaking point and price in the DM-only notes.
- Stage each legwork result with `stage_secret`, aimed at the character who did that legwork: the guard rota to whoever charmed the cook, the strongroom detail to whoever read the builder's plans.
- Draft guards and response teams with `plan_encounter`; let `rate_encounter` or `propose_encounter` set difficulty, and use `set_npc_statblock` for a named captain. Never hand-tune numbers in the skill.
- Plan the job as `upsert_session_beat` entries: briefing, entry, each layer, the prize, the complication, the getaway. Put the twist on the plot board as an `upsert_plot_node` and `link_plot_nodes` from each clue that seeds it.
- Log heat and fallout with `upsert_thread`, urgency rising, scheduled to the next session. Offer a `build_cue_list` for the reveal moments (the floor plan, the flashback, the empty vault) for the DM to fire. Finish with `get_changeset`, recap, and `request_approval`.

## References

- Read [references/beats.md](references/beats.md) when outlining a job, running a legwork session, or structuring the execution session and flashbacks.
- Read [references/npcs.md](references/npcs.md) when drafting the crew, the fixer, the client, the mark or the inside man.
- Read [references/encounters.md](references/encounters.md) when designing security layers, casing, infiltration, alert levels, or what happens when the job goes loud.
- Read [references/factions.md](references/factions.md) when drafting who owns the target, who hunts the crew, and who else wants the prize.
- Read [references/lore.md](references/lore.md) when describing the target, naming the job and the crew, or writing blueprints, rotas and forged papers.
- Read [references/pitfalls.md](references/pitfalls.md) when planning stalls, a plan fails too early, or a twist risks feeling unfair.
- Read [references/safety.md](references/safety.md) before drafting hostages, threats to the inside man's family, confinement, or harm to bystanders, and whenever `get_table_safety` returns limits.

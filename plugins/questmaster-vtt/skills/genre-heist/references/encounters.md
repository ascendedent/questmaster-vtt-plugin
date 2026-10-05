# Heist: encounters

A heist encounter is a situation with a clock. Design each one with **stakes** (what the crew gains or loses), **complications** (what changes without the crew's input), and **outs** (how they get clear if it goes wrong). QuestMaster handles numbers: when a fight is possible, draft it with `plan_encounter` and let `rate_encounter` or `propose_encounter` set the difficulty.

## Alert levels

Track one alert level for the whole site. Say in advance what moves it.

| Level | What the site looks like | Typical triggers |
| --- | --- | --- |
| Calm | Normal routine, bored guards | Nothing yet |
| Wary | A guard checks a noise, a door gets re-locked | A sound, a missed password, a face that does not fit |
| Searching | Patrols doubled, rooms checked in turn | A body, an open door, a tripped ward |
| Lockdown | Exits sealed, the prize moved or guarded in person | A visible intruder, an alarm bell |
| Pursuit | The crew is known and followed off-site | Escape with the alarm raised |

- Alert rarely drops during a job. A clever distraction can drop it one step, once.
- Each step should change what the crew sees, so players can feel the pressure rise.

## Exploration: casing the target

- **Stakes:** Each visit gives the crew one layer's details and one asset opportunity.
- **Shape:** Let the crew visit as customers, workers, petitioners or guests. Each visit answers two questions they ask.
- **Complications:** A clerk remembers a face from the last visit. The owner is on site unexpectedly. A guard asks a friendly question that needs a cover story.
- **Outs:** Leave with partial information; return in a different disguise (costing a day).
- **Recognition:** The same crew member visiting three times is remembered. Record it as heat.

## Social: the infiltration

### The gala
- **Stakes:** Reach the upper floor during the party, while the owner is distracted.
- **Shape:** An invitation (forged or earned), a host who wants to talk, guests with their own agendas, a timed event (the toast, the unveiling, the dance) that pulls everyone into one room.
- **Complications:** A guest knows the person a crew member is pretending to be. The toast is moved earlier. A rival crew member is also a guest.
- **Outs:** A staged argument, a spilled drink, a "sudden illness" that gets someone escorted out through the kitchens.

### The delivery
- **Stakes:** A cart through the service gate is the way in.
- **Shape:** A manifest, a gate clerk, a dog, a cargo inspection.
- **Complications:** The usual driver is known to the clerk. The manifest is a day out of date.
- **Outs:** Bribe, bluff, or abandon the cart and go over the wall.

## Puzzle and exploration: security layers

Each layer has one obstacle and three approaches. List which legwork asset bypasses it.

- **Locks.** A multi-key strongroom whose keys are held by people who never stand together. Approaches: steal both keys, copy both, or bring both people together for a reason.
- **Wards.** A glyph that marks whoever crosses it with a stain that shows under lamplight. Approaches: learn the passphrase, carry the owner's token, or accept the mark and plan around it.
- **Animals.** Dogs that smell rather than see. Approaches: a scent the dogs know, a meal the handler forgot to give, a route downwind.
- **Mechanisms.** A bell-wire through the gallery, a floor that creaks in one pattern, a door that locks when another opens.
- **Paperwork.** A clerk who checks names against a ledger. Approaches: be in the ledger, distract the clerk, or replace the ledger.
- **Magic countermeasures.** Owners who know magic exists plan for it: flour on floors against invisible intruders, bells that ring at any teleport within the walls, a lead-lined vault, a decoy prize that radiates magic. Let each spell be useful against some layers and blocked by others.

## Combat: when it goes loud

- **Stakes:** Get the prize and get out before reinforcements arrive. Winning the fight is not the goal.
- **Shape:** An objective, a route out, and a reinforcement clock (for example, more guards every few rounds). Draft the first wave and the reinforcements as separate encounters in `plan_encounter` so QuestMaster rates each.
- **Complications:** A guard who surrenders immediately and begs not to be hurt. A fire that spreads. The prize in a heavy case that slows whoever carries it.
- **Outs:** Retreat to a prepared exit, turn the building against the guards (bar a door, cut a hoist rope, flood a stair with lamp oil and smoke), or drop the prize to escape.
- **Bystanders:** Clerks, servants and guests are present. Draft how each reacts; the crew's treatment of them becomes heat or loyalty.

## The getaway

- **Stakes:** Get clear without being followed to the safe house.
- **Shape:** Three or four short chase beats: the street, a crowd, a bridge, the water. Each offers a choice (split up, hide, fight, bluff).
- **Complications:** The planned route is blocked by a procession. The boatman learns what is in the case.
- **Outs:** A pre-arranged hiding place earned in legwork, a change of clothes, a friendly door.

## The double-cross

- **Stakes:** The prize, the payment, or the crew's freedom.
- **Shape:** The client, fixer or rival makes a move at the handover. Seed it with at least two clues in legwork.
- **Outs:** A swapped prize, a backup buyer, leverage on the betrayer, or simply walking away with the job's true value.
- **Rule:** The double-cross is an opportunity for players who noticed the clues, not a punishment for players who did not. Offer the DM a version where the client keeps faith.

## Escalation after the job

- **Day 1:** The theft is discovered. Rumours, a reward notice, extra watch patrols.
- **Day 3:** An investigator interviews staff. The inside man is questioned.
- **Week 1:** The owner hires someone to find the crew. Their fence gets a visit.
- **Later:** The owner's allies act against the crew's patrons. Log each step as an `upsert_thread` with rising urgency.

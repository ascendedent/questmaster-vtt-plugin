# Heist: pitfalls and fixes

Each entry names a failure mode the assistant should watch for in the DM's prep or its own drafts, and the fix.

## Planning paralysis

- **Symptom:** The players plan for two hours and the session ends before the job starts.
- **Fix:** Give planning a hard limit and say it up front. Allow flashbacks during the job (beats.md) so the players do not need to anticipate everything. A plan with gaps is a plan; the flashback fills the gaps later.

## The plan works perfectly

- **Symptom:** Every layer falls exactly as planned. It feels like a checklist.
- **Fix:** One complication per phase, always. It breaks one assumption the players stated at the briefing and leaves two ways through. Competence shows in how they adapt.

## The plan fails at the door

- **Symptom:** One bad roll at the first layer brings the whole site down on the crew.
- **Fix:** Failure raises the alert level one step; it does not end the job. Let the first layer go mostly to plan, to reward preparation, and make the middle layers bite.

## Complications that negate preparation

- **Symptom:** The crew spent a session getting the guard rota, and the DM changes every guard on the night.
- **Fix:** Complications aim at one assumption, never at the crew's legwork as a whole. If the rota changed, the crew's contact still knows the new captain's habits. Preparation always counts for something.

## The gotcha twist

- **Symptom:** The client betrays the crew with no warning, and the players feel stupid for trusting anyone.
- **Fix:** Seed every twist with 2 or 3 clues in legwork. Make the twist an opportunity as well as a threat: if the client lied, the crew now holds something worth more than the fee. Offer the DM a version of the job without the betrayal.

## The inside man as a vending machine

- **Symptom:** The inside man exists to hand over a key and is never mentioned again.
- **Fix:** Give him a want, a fear and a breaking point (npcs.md). Track his loyalty as an `upsert_thread`. Bring him back in the fallout, questioned by the investigator, needing the crew's help.

## One character does everything

- **Symptom:** The rogue picks every lock, sneaks past every guard, and the rest of the table watches.
- **Fix:** Design layers that need different skills: a conversation, a feat of strength, a ward, a timed distraction, a disguise. Give every character a job only they can do on the night, and ask the DM which player has had the least spotlight.

## The default to combat

- **Symptom:** Every heist ends in a brawl because fighting is the familiar tool.
- **Fix:** Make fighting expensive. Reinforcements on a clock, bystanders who scream, a prize that can break. Make sure every layer has quiet and clever approaches, so fighting is a choice the players make, not the only option.

## Locks as single rolls

- **Symptom:** "Make a Dexterity check." "18." "It opens." Every obstacle is a roll.
- **Fix:** Treat an important lock as a small situation: where is the key, who carries it, when is the door open anyway, what happens if the lock is forced. Rolls resolve approaches; they do not replace them.

## No fallout

- **Symptom:** The crew gets away, splits the money, and the world forgets.
- **Fix:** Run the escalation after the job (encounters.md). The owner wants revenge, the underwriters want the prize, the watch wants an arrest. Log each as a thread, and let the fallout seed the next job.

## The players do not care about the prize

- **Symptom:** The job is just money, and the players treat it like a chore.
- **Fix:** Connect the target to a player character with `get_party`: a backstory enemy owns it, a lost relative is held there, the prize could clear a name. Or let the twist give them a reason mid-job.

## The prize nobody can sell

- **Symptom:** The crew steals a famous object and then realises no fence will buy it. The session stalls.
- **Fix:** Answer "who buys it?" before the job, as part of legwork. A famous prize needs a specific buyer: the underwriters, a collector, a client. If the players skipped this, offer the buyers as options in the fallout.

## The DM's plan versus the players' plan

- **Symptom:** The DM has an intended solution and steers the crew toward it.
- **Fix:** Design obstacles, not solutions. List what each layer is and what assets help; the players' plan is the answer. If the assistant catches itself writing "the crew should", rewrite it as "options for the crew".

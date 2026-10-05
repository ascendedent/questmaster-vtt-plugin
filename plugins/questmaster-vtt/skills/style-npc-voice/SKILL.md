---
name: style-npc-voice
description: Style rules for giving non-player characters voices a DM can perform at the table. Gives the assistant a compact voice sheet per NPC with pace, register, a physical tell, one or two verbal habits, three sample lines that each do a different job, and what the NPC never says and why. Use when creating or revising an NPC who will talk to the party, preparing a social scene, or when a DM says their NPCs all sound the same.
---

# NPC voice

A voice sheet gets the DM into a character in five seconds: how they sound, what their hands do, three lines to borrow, and the wall they will not cross.

## Use this when

- Creating or updating an NPC who will speak with the party.
- Preparing a social scene: a negotiation, an interrogation, a plea, a market haggle.
- Several NPCs share a location and need to sound different from one another.
- The DM says "give her a voice", "how does he talk?" or "my NPCs all sound like me".

## The rules

1. **Build the voice from levers the DM can pull, not adjectives.** Pace (clipped, rambling, long pauses), register (formal, street, trade jargon, child-plain) and one physical tell the DM can do in their chair (taps the table twice before a lie, polishes a spoon while thinking). "Gruff" is not a voice; "answers questions with questions, and calls everyone friend a beat too late" is.
2. **One or two verbal habits, no more.** A pet word, a filler, a sentence shape (lists things in threes, turns statements into questions, measures everything in loaves of bread). Three habits is a cartoon.
3. **Three sample lines, three jobs.** A first-impression line; a line under pressure (asked about what they hide, or threatened); a useful line that hands the party a clue, a price, a direction or a warning. Each fits in one breath.
4. **Say what they never say, and why.** One or two things the NPC will not say: a name, an apology, a number, a word their faith forbids. This tells the DM where the wall is when the players push. Give the reason (pride, fear, loyalty, a debt) so the DM can improvise around it.
5. **Tie the voice to the motive and the secret.** The tell fires near the secret. The pressure line strains against the secret without revealing it. No sample line hands the secret over.
6. **No caricature.** No phonetic spelling of accents, and no voice built on a real-world ethnicity, a disability or a speech impediment played for laughs. Use rhythm, word choice and attitude. If an accent matters, describe it once in neutral words ("long hill-country vowels") and write the lines in plain spelling.
7. **Make a cast distinct.** NPCs who share a scene differ on at least two levers. Check `search_campaign` for who else lives or works there before you settle a voice.
8. **The DM performs; you supply options.** These are lines to borrow, not a script. Never write what the NPC decides in answer to the players at the table; write how they sound while the DM decides.

Hand it over in this shape:

```
**[Name]** ([one-phrase role])
Voice: [pace], [register]; [one sentence on how to perform it]
Tell: [a physical action] (when: [the trigger])
Habits: [one or two]
Lines:
- First impression: "[...]"
- Under pressure: "[...]"
- Useful: "[...]"
Never says: [what] (because [why])
```

## Checklist before you hand it over

- [ ] Pace, register and tell are things the DM can do, not adjectives.
- [ ] No more than two verbal habits.
- [ ] Three lines, three different jobs, each one breath long.
- [ ] The useful line gives the party something concrete to follow.
- [ ] The pressure line brushes the secret without revealing it.
- [ ] "Never says" comes with a reason.
- [ ] No phonetic accent, and no voice built on a real group or condition.
- [ ] Different on at least two levers from other NPCs in the same scene.
- [ ] Name, role and loyalties match the NPC's existing record.

## Where it goes in QuestMaster

- Read `get_campaign_overview` for tone, then `search_campaign` for the NPC, so you update the existing record instead of creating a duplicate.
- The voice sheet goes on the NPC record via `upsert_npc`, alongside personality, motivation and secret. The tell's trigger and the reason behind "never says" touch the secret, so keep them in DM-only notes.
- For a planned social scene, copy the pressure line and the useful line into the encounter via `plan_encounter`, or into the scene's beat via `upsert_session_beat`, so they are on the page when the DM needs them.
- If the NPC writes something the party will read, use `style-handouts` and carry the same habits into the writing.
- Then `get_changeset` and `request_approval`.

## References

- Read [references/registers.md](references/registers.md) when fitting a voice to the campaign's tone, or when the DM wants the same NPC to sound grittier, lighter or bigger.
- Read [references/examples.md](references/examples.md) before writing the first voice sheets for a campaign, and when a sheet reads like a list of adjectives.

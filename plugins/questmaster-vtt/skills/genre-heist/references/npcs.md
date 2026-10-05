# Heist: NPC archetypes

A heist cast is small and every member of it has a second story. For each NPC write a **want**, a **fear**, a **twist** that the crew can discover, and a **tell** the DM can perform. Draft each with `upsert_npc`; keep the twist and any hidden loyalty in the DM-only notes, and stage what the crew learns about them with `stage_secret`.

## 1. The Fixer With a Backup Crew

- **Twist:** She has quietly sold the same job to a second crew as insurance. She will admit it if asked the right way, and she will tell the party where the other crew plans to enter.
- **Want:** The job done by somebody, on time.
- **Fear:** Her own patron, who has never been seen and never forgives.
- **Tell:** Eats throughout every meeting and never offers to share.

## 2. The Mark Who Wants to Be Robbed

- **Twist:** He has insured the prize for twice its worth with an underwriting house. His security is lax on purpose, and he will be furious if the robbery fails.
- **Want:** The payout, and nobody looking too closely at why.
- **Fear:** An investigator who notices the lax security.
- **Tell:** Explains his security to strangers in unnecessary detail.

## 3. The Loyal Inside Man

- **Twist:** Not disgruntled at all. He loves the place and its people, and is helping because the owner is about to ruin them all.
- **Want:** To save his coworkers' livelihoods.
- **Fear:** Being seen as a thief by people he respects.
- **Tell:** Polishes things that are already clean while he talks.
- **Breaking point:** If the crew harms a coworker, he flips and warns the guards.

## 4. The Retired Specialist Who Is Informing

- **Twist:** She retired because she was caught, and bought her freedom by informing for the watch. She hates it, and she is still the best lockbreaker in the city.
- **Want:** One job big enough to buy her way out of the deal.
- **Fear:** Her old crew finding out.
- **Tell:** Absently tests every lock she walks past.

## 5. The Rival Crew on the Same Night

- **Twist:** They are hitting the same building on the same night, for a different item. Cooperation, sabotage and a race are all possible.
- **Want:** Their own prize, and no witnesses.
- **Fear:** The party learning their real names.
- **Tell:** Their leader is unnervingly polite, and always arrives a minute early.

## 6. The Investigator Who Admires Good Work

- **Twist:** He works for the underwriters, not the watch. He would rather recover the prize than make an arrest, and he can be bargained with.
- **Want:** The item back by the end of the week.
- **Fear:** His employers learning how often he makes deals.
- **Tell:** Compliments the crew's technique aloud at the scene of the crime.

## 7. The Fence Who Loves the Objects

- **Twist:** A respected antiquarian who will refuse anything damaged and pay double for a good story of where it came from.
- **Want:** Beautiful things kept safe and properly catalogued.
- **Fear:** A forgery passing through her hands and ruining her name.
- **Tell:** Wears white cotton gloves to handle everything, including coins.

## 8. The Client Taking It Back

- **Twist:** The client is the original owner. The prize was taken from her legally, through a crooked lawsuit, and she cannot be seen to steal it.
- **Want:** The item home, and the thief who took it humiliated.
- **Fear:** Being exposed as the commissioner.
- **Tell:** Knows the target building's layout too well for a stranger.

## 9. The Night Warden With a Second Job

- **Twist:** She sleeps through part of every shift because she works days at a bakery. The gap is the crew's way in, and her dismissal is the job's real cost.
- **Want:** To keep both wages and feed her family.
- **Fear:** Losing the post that houses them.
- **Tell:** Yawns, apologises, yawns again.

## 10. The Forger Who Must Come Along

- **Twist:** He cannot forge anything he has not seen with his own eyes, so he has to be inside on the night. He has never been in danger in his life.
- **Want:** To see the original, just once.
- **Fear:** Everything outside his workshop.
- **Tell:** Describes people and rooms in terms of paper, ink and seals.

## 11. The Owner's Estranged Daughter

- **Twist:** She is the crew's best source on the house, and she wants her father ruined without harming the servants who raised her.
- **Want:** To hurt him, cleanly.
- **Fear:** Facing him.
- **Tell:** Uses the household's private nicknames for rooms ("the cold parlour", "Grandmother's stair").

## 12. The Boatman With Rules

- **Twist:** The best getaway pilot in the harbour refuses to carry stolen holy objects and will turn back mid-river if he learns he is.
- **Want:** Paid, and his conscience clear.
- **Fear:** Curses, which he believes in completely.
- **Tell:** Touches the prow before every departure and makes passengers do the same.

## Building the crew around the players

- **Fill gaps, never duplicate.** Hire NPC help only for a role no player character covers.
- **NPC crew members have opinions about the plan.** One objection each, voiced at the briefing, gives the players something to answer.
- **Every hired specialist has a price beyond coin:** a favour later, a share of something else, a promise.
- **The inside man's loyalty is a thread.** Log it with `upsert_thread`, and note what would raise or lower it.

## Inside man loyalty, quickly

| The crew... | Loyalty |
| --- | --- |
| Pays what was promised, on time | Holds |
| Protects his coworkers during the job | Rises |
| Shares the twist with him | Rises |
| Changes the plan without telling him | Falls |
| Lets him be suspected afterward | Falls sharply |
| Threatens his family | Breaks, and see safety.md |

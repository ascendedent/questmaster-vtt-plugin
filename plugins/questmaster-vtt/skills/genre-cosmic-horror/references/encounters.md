# Cosmic Horror: Encounters

Most cosmic horror encounters are not fights. They are contacts, confrontations with people, places that break rules, and rituals with a price. Fights happen against human-scale enemies (cultists, servants, the changed) and those can be won. The entity is never a combat. QuestMaster rates the fightable parts with `rate_encounter`; this file is about what the encounter is for.

## Principles

- **Survive and learn, not kill.** The goal of most encounters is to get out with something: a clue, a person, a fact.
- **Rules, not randomness.** Every strange site or manifestation follows consistent rules the party can discover and exploit. Consistency is what makes it frightening rather than silly.
- **Every encounter has an out.** Running, hiding, closing a door, giving it what it wants. State the cost of each out.
- **Scale the threat by attention.** Track whether the thing has noticed the party. Most encounters escalate by attention, not by adding monsters.

## The brush with the edge

A short contact with the real threat, used once per spiral loop.
- **Shape:** a manifestation (sound, shape, distortion) that is clearly beyond the party, followed by a choice: look, flee or interfere.
- **Stakes:** a mark offered to whoever looks too long; a person or object lost if they flee; a clue gained if they interfere.
- **Example:** in the reed-cutter's hut, the reeds outside lean toward the hut in a perfect circle, one ring closer every minute. A survivor inside is still alive. The party can carry her out (she slows them), measure the circle (a clue and a mark), or cut a gap in it (it notices them).
- **Out:** the circle stops at dawn, or when nobody inside is counting.

## Combat situations

### The cult at the ritual
- **Stakes:** the ritual completes and the door opens wider. Every round costs a step on a visible ritual track.
- **Complications:** the cultists are townsfolk the party has met; some will surrender, some will fight to protect the people they love; killing the celebrant may complete the rite.
- **Outs:** disrupt the ritual instead of the people (break the circle, douse the lamps, sing over the chant); turn a doubter; take the book and run.
- **Escalate:** the ritual's partial success manifests something small and wrong in the middle of the fight.

### The servants in the dark
- **Stakes:** a site the party must cross or hold until something finishes (a seal, a rescue, a copy burned).
- **Complications:** the servants follow rules (they can only step where something has been measured, they cannot cross unbroken thread, they flee from their own names spoken aloud) that the party learns in play.
- **Outs:** exploit the rule; hold until the hour turns; leave the site to them.
- Use `search_monster_sources` for a base creature and `upsert_bestiary_monster` to reskin it with its rule.

### The changed defender
- **Stakes:** a transformed NPC the party knows stands between them and the site.
- **Complications:** they do not want to hurt the party; they also will not let them pass.
- **Outs:** talk them down with something from who they were; trap them; accept their terms.

## Social situations

### The interrogation
- **Setup:** a captured cultist, a reluctant witness or a lying official.
- **Stakes:** the clue, and what the interrogation does to the party's own conscience and reputation.
- **Complications:** the subject tells the truth and it sounds insane; someone powerful wants them released; the truth costs the listener a mark.
- **Outs:** trade protection for the truth; let them go and follow them; find the clue another way, later.

### Convincing the authorities
- **Setup:** the party needs the magistrate, the guild or the temple to act.
- **Stakes:** official help (people, access, a closed road) versus being dismissed or arrested.
- **Structure:** the authority needs three things before acting: evidence they can see, a story they can tell their superiors, and a way to avoid blame. Each is a separate scene or clue.

### Bargaining with the changed
- **Setup:** someone partway gone offers help in exchange for help finishing.
- **Outs:** accept (a powerful ally, and one more servant later), refuse (a dangerous enemy who knows the site), or bargain for a delay.

## Exploration situations

### The site that breaks rules
- Give each site two or three laws: distances are longer going in than coming out; the same room appears twice; anything written down here changes when unread.
- Map it with `annotate_map`: mark the impossible spots, the safe spots and the exits, hidden until shown.
- **Stakes:** time. Each hour inside costs something (a supply, a memory, a step on the attention track).
- **Out:** every site has a known way out and a cost to use it.

### The archive
- **Stakes:** the clue is in here; so is something the party should not read.
- **Complications:** reading the right document takes time; the wrong document offers a mark; the archive's keeper is watching.
- **Outs:** copy and leave; take the original (theft); read it here and pay for it.

## Puzzle situations

- **The cipher with a cost.** Deciphering it is possible; finishing the translation imposes a mark. The party can stop at a partial, usable answer.
- **The ritual in reverse.** Closing a door means performing the opening rite backward, and each step requires something the cult used (a voice, a name, a willing participant).
- **The map that is true.** A map that shows things before they exist. Using it to navigate works perfectly and makes the places on it more real.
- Every puzzle has a safe partial answer and a complete answer that costs.

## The closing (finale)

- **Stakes:** the door that is open now, not the whole threat.
- **Offer two or three ways to close it,** each paid in something different (a person stays, knowledge is destroyed, a power is lost), plus one way to exploit it instead.
- **Complications:** the cult, the suppressors and the patron all arrive with their own plans.
- **Escalate** only by attention: the longer it takes, the more the thing notices, until something small and terrible steps through.

## Escalation ladder (attention)

1. Unnoticed: the party can act freely and quietly.
2. Stirring: small wrongs gather near them (birds silent, water rippling against the wind).
3. Noticed: a servant or manifestation moves toward the party specifically.
4. Attending: everything in the site turns to face them; outs start closing.
5. Reaching: one out remains, and it costs the most.

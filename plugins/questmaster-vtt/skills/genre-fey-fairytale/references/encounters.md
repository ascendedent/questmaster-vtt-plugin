# Fey Fairytale: encounters

Fey encounters are mostly contests of manners, wits and nerve, played under rules everyone at the table can learn. Violence is what happens when the rules break. Plan most encounters as social or puzzle situations, and let QuestMaster rate the fights that etiquette fails to prevent.

## Design principles

- **State the rules in-world first.** A host announces the house customs; a rhyme warns of the seventh stone. Players should be able to win by listening.
- **Courtesy has mechanical weight.** Thanks, names, gifts and refusals change outcomes. Write what each does in the encounter's dmContext.
- **Every contest has a clever out.** A precise question, a loophole, a gift that changes the frame. Reward it fully.
- **Wonder before danger.** Describe the beauty first, then the wrong detail, then the stakes.
- **Fights are a breach.** When combat starts, someone broke a rule. Decide in advance who would, and what the breach costs them afterward.

## Social situations

### The feast under the hill
- **Situation:** the party is welcomed to a banquet. The rules: guests who eat stay until dawn; guests who thank the host by name may leave at will; guests who refuse food insult the house.
- **Stakes:** leaving on time, and the host's favor.
- **Complications:** nobody tells them the host's name; one dish is a gift from a rival court, and eating it creates a debt to the rival.
- **Outs:** learn the name from a servant (for a price); eat only what they brought; offer a song as payment instead of thanks.

### The bargain table
- **Situation:** a fey offers exactly what the party needs, on terms. The negotiation is the encounter.
- **Stakes:** the thing they need, against a personal price.
- **Complications:** a second fey makes a counter-offer that is better on paper.
- **Outs:** negotiate the price down by offering something the fey values more (a story nobody has heard, a true secret); add a clause; walk away, which the fey respects.
- **Run it:** read each version of the terms aloud and let the players amend the wording. Every amendment the fey accepts adds a clause in its favor too.

### The court petition
- **Situation:** the party must ask a court for something (a captive back, safe passage) before an audience of rivals.
- **Stakes:** the petition, and the party's standing with every faction watching.
- **Complications:** petitions must be made in a form nobody explained (in verse; on bended knee; with a gift wrapped in a riddle).
- **Outs:** find a sponsor among the courtiers; challenge the form with a precedent; accept a task in exchange.

## Puzzle situations

### The riddle contest
- **Situation:** a guardian or rival proposes a contest of riddles; loser pays a forfeit named in advance.
- **Stakes:** the forfeit (a voice, a year, a weapon, passage).
- **Play:** do not make it a test of the players' riddle knowledge. Let each riddle be answerable from something they have seen in the session, and let skill checks earn hints.
- **Outs:** a riddle whose answer is something only the party saw tonight, which the guardian cannot know; a forfeit renegotiated before the contest begins.

### The maze of hedges
- **Situation:** the hedge maze rearranges whenever no one is looking at it.
- **Play:** someone must always be watching a wall. Splitting up is fast and dangerous; holding hands is slow and safe.
- **Outs:** a ball of thread left by a previous guest; a hedge that can be bargained with; burning, which is effective and a grave insult.

### The three gifts
- **Situation:** a host lays three gifts on a cloth (a silver comb, a seed, a song) and invites the party to choose one. One is freely given; the others are lovely and bind.
- **Play:** each gift is described with its one wrong detail. The true gift has no wrong detail, and is plain.
- **Outs:** refuse all three, which is allowed and earns respect.

## Exploration situations

### The crossing
- **Situation:** a ford, a bridge of moonlight or a door in a hillside with a rule for passing.
- **Stakes:** getting in, and whether time slips.
- **Complications:** the rule is ambiguous; two NPCs give different versions.
- **Outs:** follow the more specific version; pay the warden; find another crossing with a worse rule.

### The dance that will not end
- **Situation:** a revel in a ring of stones. Anyone who joins dances until someone outside the ring pulls them out by name.
- **Stakes:** time (each hour danced is a day outside) and companions.
- **Outs:** a rope tied before entering; a companion stays out and keeps count; a tune played backward breaks the ring.

## Combat situations

### The hunt
- **Situation:** the party has offended a noble and is declared quarry. The hunt rides at moonrise.
- **Stakes:** being caught means service for a year and a day.
- **Complications:** the hunters must stop at running water and cannot enter a dwelling uninvited.
- **Outs:** reach the river; be invited into a mortal home; offer a better quarry.
- Plan it with `plan_encounter` (exploration or hybrid) and use `propose_encounter` with theme fey to get a starting group, then `rate_encounter` to check it.

### The broken truce
- **Situation:** someone at the feast breaks hospitality. Every guest is now free to act.
- **Stakes:** escape, and whose side the court takes afterward.
- **Outs:** prove the other side broke it first; flee before the doors close; take shelter with the host, who must protect a guest who did nothing wrong.

## Escalation

1. **Courtesy:** rules stated, offers made, small debts accrue.
2. **Notice:** a rule was broken. A warning, a lost hour, a strange sign follows the party.
3. **Claim:** the debt is called. A collector arrives with terms.
4. **Breach:** the rules are off. A hunt, a curse, or the doors closing.
5. **Settlement:** a new bargain, a paid price, or a hard escape with a lasting mark.

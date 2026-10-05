# Heist: faction archetypes

In a heist, factions are the people who own things, the people who guard them, the people who want them, and the people who will hunt whoever takes them. Draft each with `upsert_faction`: `publicMission` is the face it shows, `realAgenda` (DM-only) is what it actually wants. Note its **method** and **how it collides** with the others, because the collisions are where the crew finds cover, buyers and enemies.

## 1. The Owner's House

- **Public face:** A respected family, guild or institution, proud of its collection and its security.
- **Real agenda:** Keep the prize because it proves something (legitimacy, wealth, a stolen past) or because losing it exposes something worse.
- **Method:** Guards, wards, insurance, and a reputation for ruining anyone who crosses them.
- **Collides with:** the Underwriters (who doubt its security claims), the Client (who wants what it holds), and its own servants (who know where the bodies are).
- **Example:** The Vantreyne Collection, a merchant family's private museum, whose prize exhibit was bought from a family that had no right to sell it.

## 2. The Watch

- **Public face:** Law and order, protection of property.
- **Real agenda:** Divided. The captain wants arrests that look good; the sergeants want a quiet beat; one constable wants the reward money.
- **Method:** Patrols, informants, rewards, and leaning on fences.
- **Collides with:** the Syndicate (who pay part of it to look away), and with the Underwriters (who make it look slow).
- **Use at the table:** The watch is a clock, not a villain. Its response time sets the getaway.

## 3. The Underwriters

- **Public face:** A sober counting-house that insures cargo, collections and lives.
- **Real agenda:** Pay out as little as possible. Recovering a stolen prize is cheaper than paying for it, and a fraudulent claim is worth exposing.
- **Method:** Private investigators, quiet deals with thieves, ransom of stolen goods back to their owners.
- **Collides with:** Owners who over-insure, and with the watch, whose arrests can destroy a prize the underwriters wanted returned.
- **Use at the table:** The underwriters are the crew's best possible buyer and their most patient pursuer. Both at once.

## 4. The Syndicate

- **Public face:** None in public. In the trade, "the people you pay before you work in this district".
- **Real agenda:** A cut of every job on its ground, and no jobs big enough to bring the army in.
- **Method:** Tribute, sanctioned crews, enforcers, and handing unsanctioned thieves to the watch.
- **Collides with:** Any crew that did not ask permission, and with the Owner, if the Owner has been paying them for protection.
- **Use at the table:** Asking the syndicate's permission is a legwork option. Skipping it is heat.

## 5. The Collectors' Circle

- **Public face:** A society of connoisseurs who meet monthly to discuss rare objects.
- **Real agenda:** Its members commission thefts from one another, and a few of them commission thefts of things that were already stolen.
- **Method:** Anonymous commissions through fixers, legitimate auctions as cover, and a private vault no member has ever seen in full.
- **Collides with:** Every owner, the underwriters, and itself.
- **Use at the table:** A source of clients, double-crosses and the next job.

## 6. The Client's Patron

- **Public face:** Whoever the client claims to represent, or nobody.
- **Real agenda:** The reason behind the job. Political leverage, revenge, an occult purpose, or proof of a crime.
- **Method:** Distance. The patron never meets the crew, and the client is expendable.
- **Collides with:** The Owner directly, and with the crew if the crew learns too much.
- **Use at the table:** This is usually where the twist lives.

## 7. The Fences' Market

- **Public face:** Pawnbrokers, antiquarians, a night market under a bridge.
- **Real agenda:** Buy cheap, sell dear, and never be holding a famous object when the watch arrives.
- **Method:** Price lists, layaway for crews, and selling information about crews to the underwriters when it pays better.
- **Collides with:** The watch and the underwriters, who both lean on fences after a big job.
- **Use at the table:** Who will buy the prize is a question to answer before the job. A famous object nobody can sell is a problem.

## How they collide around one job

Map the job before the session. For the prize, answer:

| Question | Faction it usually points to |
| --- | --- |
| Who owns it, and why does it matter to them? | The Owner's House |
| Who will notice it is gone first? | The Owner, then the Watch |
| Who pays if it is never found? | The Underwriters |
| Who expects a cut? | The Syndicate |
| Who would buy it, and for how much? | The Fences, the Collectors' Circle |
| Who really wants it, and why? | The Client's Patron |

## Example collision web: the Vantreyne job

- **The Vantreyne Collection** insured its prize, a carved jade astrolabe, with **the Underwriters of Saltmarket** for an inflated sum.
- **The Collectors' Circle** commissioned the theft through a fixer, on behalf of a member who claims it was stolen from her grandfather.
- **The Syndicate of the Low Wards** has been paid by Vantreyne for protection, and will feel insulted.
- **The Watch** captain dines with the Vantreynes monthly.
- **The fences** will not touch the astrolabe; it is too famous. Only the underwriters or the Circle can pay for it.

Options to offer the DM: the crew sells it back to the underwriters (profitable, angers the client); delivers it to the Circle member (honours the job, starts a feud with the syndicate); or proves the Vantreynes never owned it legally (a political win that pays nothing up front).

## Drafting checklist

- `search_campaign` for existing factions before creating new ones; a heist can often reuse the city's existing powers.
- One `upsert_faction` per faction, with public mission and real agenda separated.
- Each faction's response to the theft is an `upsert_plot_node` on the fallout arc, linked with `link_plot_nodes` from the job beat that triggers it.
- Each faction's pursuit is an `upsert_thread`, with urgency rising as days pass.

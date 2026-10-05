# Political intrigue: faction archetypes

A faction in intrigue is a group whose members share a public story and disagree in private. Give each one a **public face** (`publicMission` in `upsert_faction`), a **real agenda** (`realAgenda`, DM-only), a **method** (how it gets things done when nobody is watching), and a note on **how it collides** with the others. Then tie every pair of factions with something concrete (see beats.md).

Each archetype below names a few internal voices. Splitting a faction into two or three voices is the fastest way to give the party someone to recruit from inside it.

## 1. The Old Blood House

- **Public face:** Tradition, continuity, the family that has always held this seat.
- **Real agenda:** Survival. The money is gone; only the name and the charters remain.
- **Method:** Marriages, precedence, old favours called in, lawsuits that take a generation.
- **Internal voices:** the matriarch who remembers the glory, the heir who wants to sell the charters and leave, the cousin who would sell the family to keep the title.
- **Collides with:** anyone with new money, because it needs their coin and despises their manners.
- **Example:** House Merrowin of the salt marshes, whose ancestral right to tax every cartload of salt is the only income they have left.

## 2. The Guild or Compact

- **Public face:** The working people of the city, organised and proud.
- **Real agenda:** Its leaders want a seat on the council; its members want bread and safety. The two are drifting apart.
- **Method:** Strikes, slowdowns, controlling who can work, mutual-aid funds that double as war chests.
- **Internal voices:** the chair who has started taking meetings with nobles, the old firebrand who wants a strike tomorrow, the treasurer who knows where the fund money went.
- **Collides with:** the Old Blood (over wages and old grievances) and the Temple (over who feeds the poor).

## 3. The Temple With a Treasury

- **Public face:** Faith, charity, neutrality in worldly quarrels.
- **Real agenda:** It holds everyone's debts. It wants permanent influence, collateral it never has to return, and a new house of worship somewhere strategic.
- **Method:** Loans, mediation, sanctuary for people it finds useful, sermons that shift public mood.
- **Internal voices:** the prior who counts, the preacher who believes, the novice who keeps the ledgers and is starting to read them.
- **Collides with:** reformers (who want its books opened) and borrowers (who want their debts forgiven).

## 4. The Crown's Office

- **Public face:** The government itself: clerks, seals, the orderly business of rule.
- **Real agenda:** Its own continuity. Rulers change; the office endures, and it intends to.
- **Method:** Procedure. Delay, paperwork, agendas, the strategic loss of documents.
- **Internal voices:** the chancellor, the clerk who sets the agenda, the archivist who knows where every embarrassment is filed.
- **Collides with:** anyone who tries to rule by decree and skip the office, including the ruler.

## 5. The Foreign Power

- **Public face:** Friendship, trade, an envoy with excellent manners.
- **Real agenda:** Dependency. It wants this city to need it: for grain, for credit, for protection.
- **Method:** Gifts that become obligations, scholarships for noble children, subsidies that end the day they are relied upon.
- **Internal voices:** the envoy (who may have a conscience), the trade attache (who does not), and instructions from home that arrive late and contradict each other.
- **Collides with:** local producers it undercuts, and patriots who see the hook before others do.

## 6. The Reformers

- **Public face:** Clean government, open books, justice for the forgotten.
- **Real agenda:** Split. Some want reform; some want to be the next people in charge; one wants blood.
- **Method:** Pamphlets, public meetings, petitions, and eventually a demonstration that may become a riot.
- **Internal voices:** the idealist printer, the ambitious lawyer, the quiet one who has been buying lamp oil in bulk.
- **Collides with:** everyone who benefits from the current order, which is everyone else in the web.

## 7. The Shadow Network

- **Public face:** Officially, none. Unofficially, "the people who can get things done".
- **Real agenda:** To stay useful to every faction so that none can afford to destroy it.
- **Method:** Smuggling, blackmail, couriers, a fence for stolen documents, the occasional disappearance.
- **Internal voices:** the boss who never meets anyone, the go-between who meets everyone, the enforcer who has started freelancing.
- **Collides with:** the Captain loyal to the office, and with any faction that decides it has become too useful to the others.

## 8. The Garrison

- **Public face:** Defenders of the realm, above politics.
- **Real agenda:** Pay, promotion and a voice in who rules. Armies that are not paid start taking an interest in succession.
- **Method:** Presence. Where the soldiers stand on the day of the vote is an argument.
- **Internal voices:** the old general who swore an oath to the late king, the young colonel who swore nothing, the quartermaster who knows the treasury is short.
- **Collides with:** the Treasury holders over pay, and with any faction proposing to cut the army.

## How factions collide

Use these collision patterns when the between-session faction turn needs a move.

| Pattern | What it looks like at the table |
| --- | --- |
| Competing for the same prize | Two factions court the same councillor, heir or charter. The party is asked to carry gifts for both. |
| One holds the other's leash | A debt, hostage or secret. The leashed faction looks for a way to cut it, and the party is a knife. |
| Shared crime | Two factions did something together years ago. Exposure ruins both, so they cooperate while hating each other. |
| Proxy fight | Two factions cannot clash openly, so they back rival candidates, guilds or duellists. |
| Common enemy | Two rivals ally against a third. The alliance lasts exactly until the third is gone. |
| Defection | One faction's internal voice crosses to another. Bring it to the party first, so they can choose to help or stop it. |

## Drafting checklist

- Search before creating: `search_campaign` for existing factions and their members.
- One `upsert_faction` per faction, with public mission and real agenda in separate fields.
- Each internal voice is an `upsert_npc` linked by name in the faction record.
- Each tie between factions is written into both faction records, and the load-bearing tie is marked.
- Each faction agenda gets an `upsert_arc` with 3 to 5 `upsert_plot_node` steps, so the faction turn has somewhere to advance.

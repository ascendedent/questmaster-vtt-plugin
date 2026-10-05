# Grimdark: Beats

The signature structure is the bill. A want meets scarcity, the only ways to get it are compromised, the party picks one, and the cost arrives later with interest. Grimdark arcs are chains of bills, each one paid by the next choice.

## The bill (the core loop)

1. **The squeeze.** Something everyone needs is running out: food, medicine, a safe road, time before the army arrives.
2. **The options.** Three ways to get it, each compromised. Never one good option and two bad ones; three options that are each wrong in a different way.
3. **The deal.** The party picks, and agrees to a price, out loud, with someone who will remember.
4. **The job.** They do the thing. It is harder than the deal assumed.
5. **The bill.** The price comes due, plus whatever went wrong on the job. Sometimes it is paid by someone the party never met, and they learn that person's name.
6. **The interest.** One to three sessions later, the consequence of the choice returns in a new form.

## Victory cost menu

Before any goal, pick two or three costs the attempt can carry. Tell the DM which apply; the players should see roughly what success will cost before they commit.
- **Lives:** a named NPC, a band of soldiers, a handful of refugees.
- **Supplies:** rations, medicine, arrows, horses, the stock that was keeping something else alive.
- **Trust:** an ally's faith, a village's goodwill, the company's loyalty.
- **Principle:** a promise broken, a prisoner killed, a lie that must be maintained.
- **Time:** the delay lets something else go wrong, somewhere the party is not.
- **Standing:** the party's name becomes associated with the worst thing that happened.

## Arc structure (3 to 5 sessions)

1. **The need.** The scarcity becomes urgent and personal: someone the party cares about will suffer without it.
2. **The bargain.** The party chooses a compromised route and makes a deal with a compromised ally.
3. **The job and the cracks.** The plan meets the world. The ally asks for more. A faction notices.
4. **The reckoning.** The ally's real price, the rival faction's move and the scarcity all arrive at once. The party must choose what to save.
5. **The hollow win or the costly stand.** They get some of what they needed. Name what was saved, name what was lost, and turn the loss into the next arc's squeeze.

## Session structure

- **The count (opening):** state the resources. "Eleven days of food for forty people. The fever has two more."
- **The squeeze:** one new pressure that makes the count worse.
- **The options:** two or three compromised paths, each with an ally or faction attached.
- **The job:** the main play. One fight or one negotiation that matters, not three that do not.
- **The bill (closing):** update the count, show what the choice cost, and plant the interest for a later session.

## Scene structure: the scarcity scene

1. **Something everyone needs.** A wagon of grain, the last healer, a boat with six seats.
2. **More claimants than supply.** Each claimant has a name and a reason.
3. **A rule offered.** Someone proposes a fair-sounding rule (the strong first, the children first, those who paid first). Every rule leaves someone out.
4. **The party decides,** or refuses to and lets someone else decide, which is also a decision.
5. **Someone is left out,** and the party watches them go.

## Worked example: The Fever Winter at Grennick

**The squeeze.** Grennick, a walled market town on the old salt road, is snowed in with four hundred refugees and a lung fever. The healer, Sister Abra Vane, has fever-bark for twenty patients; there are ninety sick. More bark sits in a river depot two days south, held by whoever holds the ford.

**The options.**
- **The Brindle Company:** sellswords wintering outside town. Captain Odile Marsh will escort the party to the depot. Her price: the party rides with her company for one "collection" from a village that has not paid its war tax.
- **The temple granary:** the Chapel of Saint Hollis holds grain the town council does not know about. Selling it to a river trader buys the bark. The grain is the orphanage's winter food.
- **Hesk of the Ford:** the bandit-lord holding the depot will trade bark for a pardon signed by the town reeve, and for the name of the informer who sold his brother to the hangman.

**Session 1 (the need).** The count: twenty doses, ninety sick, eleven days until the first deaths among the children. A party member's ally, or someone they have come to like, is among the sick. The three options arrive in one evening.

**Session 2 (the bargain and the job).** Whatever they chose, they go south. The snow road, a forage gone wrong, deserters at a burned inn who could be recruited, robbed or left. They reach the ford.

**Session 3 (the reckoning).** The price is collected. Marsh's "collection" means taking a village's seed grain at sword point. The trader wants more grain than agreed. Hesk's informer is the reeve's son, and Hesk wants him delivered, not named.

**Session 4 (the hollow win).** They bring back bark for sixty, not ninety. Sister Abra must choose who receives it and asks the party to choose with her. Named survivors, named dead. The interest: the robbed village joins the rebels; the orphanage needs feeding; Hesk now holds a promise and a pardon.

**Possible outs the DM can offer:** split the price across two options to pay less of each; find a fourth route at higher personal cost (a character sells a treasured item, takes a debt, or makes a promise to a dangerous faction); refuse all deals and try to take the depot by force, which costs lives on both sides.

## Building it in QuestMaster

- The count as an `upsert_thread` per resource, urgency rising each session.
- Each option as an `upsert_plot_node` with its price, linked to its bill and its interest beats by `link_plot_nodes`.
- The interest as an `upsert_session_beat` scheduled one to three sessions ahead.

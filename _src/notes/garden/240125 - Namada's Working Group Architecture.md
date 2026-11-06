---
{
 "title": "Proposing a Namada community architecture based on RPGF funding",
 "date": "2024-01-25",
 "date_label": null,
 "folder": "1000 Living and Loving",
 "stem": "240125 - Namada's Working Group Architecture",
 "url": "https://forum.namada.net/t/proposing-a-namada-community-architecture-based-on-rpgf-funding/427",
 "related": []
}
---
Hi all -

Based on some recent conversations I've had with members of the community, I wanted to offer a proposal for a novel funding architecture for the Namada community, focused around the Public Goods Funding Stewards as detailed in the specs [here](https://specs.namada.net/economics/public-goods-funding/public-goods-stewards)

This structure is heavily informed by conversations with @cwgoes, @cryptopital, Apoorv and other members of the Community Builders who remained in the program after the first Community Builders Retroactive Public Goods Program.

Namada is built on a model of Retroactive Public Goods Funding, allocations of which are decided by the Stewards. The attraction of this model is that work done (either for or in agreement with Namada's values) can be awarded a retroactive grant based on an agreement over the impact of the work done determined Public Goods Funding Stewards.

The RPGF model can be evolved to provide a basic architecture for a funding mechanism to support the Namada community itself. With the launch of the network itself, the RPGF module will be active, meaning that Stewards can allocate funding to public goods that benefit the Namada Vision. A part of this continuous allocation could be apportioned to the Namada community on a recurring basis depending on the needs of the community's needs, as proposed by the community itself.

What follows is an architecture for how this funding could be apportioned at the community level, as well as a set of mechanisms for how this funding could be distributed among different parts of the community (here referred to as **Working Groups**) emerging at the community level.

## Namada's Working Group Architecture

As a part of this proposal, it is crucial to see how the community of Namada could be constructed to favor the model. In a post-launch architecture, there would be three tiers, from the most specific to the most general:
- **Public Goods Funding Stewards (PGFS)**
	- Those who determine apportioned quantities of Public Goods Funding to different Public Goods, including the **Namada Community**
- **Working Groups (WG)**, **Working Group Members (WGM)**, and **Working Group Leaders (WGL)**
	- **Working Groups** are separated on **Focus Areas** for **Working Group Members**
	- **Working Groups** elect **Working Group Leaders** on a recurring 6-week basis
	- This a period of time should recur as of launch but that can later be updated once there is less need for continuously changing **Working Group Leaders** and community expectations.
- **Community Builders**
	- A selected pool of candidates who accomplish **Community Bounties** in order to be vouched into **Working Groups**.

## Namada's Working Group Funding Mechanism

Having understood the architecture of the community itself, we can now use a combination of this architecture and an understanding of Public Goods funding to compose a framework for funding the community's efforts to support Namada.

On a recurring 6 week basis, the following could funding decision framework could be implemented:
### Decisions at the Steward Level*
* **Public Goods Funding Stewards** decide on a quantitative retroactive allocation for the **Namada Community** to decide on allocations for a 6 week period.
* This quantative allocation determines the pool of rewards available to the **Namada Community** to be used toward initiatives that to either:
	* Increase the userbase of Namada
	* Institute and sustain patterns of Maintenance for Namada as a whole
### Decisions at the Working Group Level
* In the last week of the preceding period, a **Working Group Committee** comprised of a **Working Group Leaders** and **Public Goods Funding Stewards**
	1. votes on the distribution of the Community allocation among Working Groups on the basis of
		1. The Namada Community's overarching needs
		2. The ambition of working groups to take on initiatives benefiting the Namada Vision and its values.
	2. Decides on **Working Group Bounties** to be taken to **Working Groups** for completion over the next 6 week period, Retroactive Funding for which is distributed at the end of the 6 week period.
* **Working Group Members** then commence each 6 week period in selecting **Bounties** within their **Working Group** to be completed.
* At the end of a 6 week period, **Working Groups** vote to elect the next proposed **Working Group Leader**, as well as any **Community Builders** that are **Vouched** into a **Working Group** for the subsequent 6 week period.
* * **Working Group Members** earn retroactive rewards as a result of completing **Bounties**, and those **Working Group Members** who have completed the most bounties have a high likelihood of being voted in as the next **Working Group Leader** who will decide funding quantities for the next 6 week period.
* **Working Group Members** who are inactive in completing **Bounties** over a 6 week period lose their right to vote on the next proposed **Working Group Leader**
### Opportunities at the Community Builder Level
* Uncompleted **Working Group Bounties** can be announced more widely to **Community Builders** who can choose to complete them, offering them a chance to be **Vouched** into a **Working Group**
	* **Community Builders** may also complete **Bounties** that are needed at the Community level but that are not specifically apportioned to **Working Groups** in order to prove their desire to join a **Working Group**
* **Community Builders** who are accepted into the pool and do not complete any **Bounties** are removed if they have not been active in **Bounty** completion over a 6-week period.

## What This Funding Mechanism Implies

The result of this community funding mechanism is set of feedback cycles that afford retroactive incentives toward community members to participate in maintaining Namada. The recursive nature of this proposed structure allows the community to make choices in rewarding activities within the community, while also providing a filtering mechanism for finding community members who are willing to lead their **Working Groups** through a social signaling mechanism such as voting.

Since those who are most active in the community are rewarded for increased activity and ownership, this also controls for worker churn throughout the growth of the community, as every 6 weeks it is possible for
- a **Working Group Leader** to be rotated out
- **Working Group Members** to be rotated out
- **Community Members** to be rotated out.

This means that over a given 6 week period, **Working Group Leaders** and **Public Goods Funding Stewards** will meet to decide on
1. What might be expected in the subsequent 6 week period from **Working Groups**
2. What practical sorts of **Bounties** for these **Working Groups** might be proposed (the expectations could also be shared with the wider community for both feedback and comment)
leading into the next 6 week period.
## Closing remarks, the proposal of tools, and a start date for implementation, and next steps.

I welcome the community's feedback on the use of this architecture to institute rewards and community mediation structures into the community, and would look forward to feedback from the community on whether this proposed structure should be used.

For voting, I think that community sentiment can/could be controlled through the use of just about any voting mechanism, but would propose that Coordinape be used at the **Working Group Committee** and **Working Group** level since the community is already familiar with this and the technology can be used to automatically prune people out on the basis of uncompleted bounties or vouch people in on the basis of completed ones.

As for a start date to implement this, I would propose that this structure be implemented on **Feb 12, 2024**, with an initial set of **Working Group Members** and **Working Group Leaders** selected by early leading members of the Namada Community.

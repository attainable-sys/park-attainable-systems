---
{
 "title": "Anoma",
 "date": null,
 "folder": "2000 Blockchain",
 "stem": "Anoma",
 "related": []
}
---
The Anoma protocol aims to do away with trades that require an underlying asset to facilitate transaction. It does so through a private gossip network that connects parties desiring a trade for any asset, then solves for the fullfilment of the connected trade desires of individual parties by creating groups of any computationally-limited arbitrary size necessary to facilitate the trade.

## What's cool about this protocol?
It would provide parties with the ability to post limit sells/buys on the Anoma protocol for settlement under a programatic [[validity predicate]] that would be gossiped for settlement whenever the trade terms are met.

## Calls
[[2022.1.12 support asks for Anoma]]
[[2021.12.15 call with Chris Goes]]
- 1.2  - centralized authority over issuance for fiat currencies leads to the abuse of these systems and monetary capture by those who control issuance
	- tie individuals to political and local economic systems
	- 1,2,2 - what are the causal reactions in the system for what your money facilitates?
	- the complexity of supply chains mean that you never know what chain of suffering you have triggered, or whose pocket the money you just spent went into.
	- largely due to the complexity of the supply chain, leading to subjugation by design as the supply chain fails to capture what happens within it
- 1, 3 - insufficient privacy and confusing UX have deterred adoption of p2p cash replacements
	- zk proofs greatly increased the level of privacy available, but current monetary systems are fixed or deflationary, which is not a stable form of payment.
	- [[von Neumann step-execution virtual machine]] doesn't work for cash or barter, and two-currency systems can somewhat solve the inefficiency, but you still are committed to holding one of the two currencies as a basis for incurring fees. This means you are still depending on the system itself.
	- MEV is also an issue
- 2 - Anoma aims to make any digital asset into the basis of exchange - meaning that you can choose any set of assets to facilitate a trade, or to barter services trustlessly (including those made on Anoma). Assets can be traded into Anoma via any type of interoperability protocol (s/a [[Axelar]])
	- 2,1 Anoma will create private, asset agnostic digital cash. Any invariance in a fully encrypted transaction process is secured by a zk proof, and the anonymity set is a unified shielded pool across all assets, instead of pools of separate assets. Any asset can be used privately to transact in Anoma
	- 2,2 all you need to barter is two people who want to trade
		- 2,2,2 bartering in Anoma is facilitated though n-party trades - facilitating trade through an equivalence of wants for trades, and this trade can scale to n parties only limited by computational trade
	- 2,3 most trading is localized, so markets for value should be localized
		- ledgers for different scales of locality (berlin<>berlin, berlin<>shanghai)
- 3 - a set of interacting sub-protocols
	- 3,1 Operates on [[Tendermint]] ([[Cosmos]]) over ABCI. There's no MEV due to distributed key generation and threshold encryption
		- 3,1,1 execution is not stepwise, contracts do not call subsequent contracts
			- 3,1,1,1 accounts decide on inclusion of transactions into their associated ledgers, code associated with an account is refered to as a 'validity predicate'
			- 3,1,1,2
				- arbitrary logic executed in a virtual machine, validity predicates are updated in the process of executing a trade and state changes are agreed upon on all associated accounts and the ledgers that associate them, only if agreed upon
				- multiparty trades don't require anyone knowing the parties - but I feel like finding people to use multiparty for trade emphasis requires people actually wanting to do the trade. I guess I don't really understand how people engage with it because it feels like it depends on users being available for the desired trades in order to execute.
				- **I guess the idea is for wallets themselves to be ledgers, in a way? #question **
			- 3,1,1,3
				- zk Sapling circuit modified to support arbitrary asset denomination so that all parties are shielded from visibility
					- all based on an Anoma standard validity predicate
		- 3,1,2 frontrunning prevention though alteration of block proposal mechanis
			- - game theoretical advantage is obvious
			- BFT key generation, but threshold decryption means that there is only aggregation, no interactions between nodes
			- threshold encryption means that validators have no information about the transaction and therefore no game theoretic reason to prioritize the tx
	- 3, 2 gossip networks mean that parties can find one another in order to facilitate an *n-party* transaction
		- 3,2,1 any surplus value from the trade is routed to peers who gossip the transaction across the network for completion, parties then engage in negotiation forwarded expressions of intent through other parties connected to the tx in terms of mutual liquidity ovoerall likely for tx bandwidth to be cheap as parties mutually agree on tx
		- 3,2,2 visibility limitation and/or token quanitity basis transfer without having to use the internet (woah)
			- basically, you could have people transact with one another without having to actually use the state of the blocks on the network to reflect the transaction
			- **wouldn't this mean that you could have malicious action when not connected to the network that would then be seen as not agreed upon when the network is connected? is this not trustless? #question **
		- 3,2,3 matchmaking algo that scans intent set for compatible counterparties, then executed on teh base ledger, where they are appropriately settled
			- sometimes a spread, sometimes a matchmaking fee. matchmaker is permissionless
	- 3,3 topologically localized intent gossip networks and trade settlement - as a result antifragile - the topology of the locality can be geographic, topical, or cultural - as a result all economy that happens between parties is locally defined
		- **doesn't this mean that you could do in-system local/cultural/macro arbitrage? #question **
	- 3,4 security of the protocol conflates with the issue of coordinated upgrading across the system
		- aperiodic and acyclic upgrades on protocol, with multiple versions working in parallel across localities
		- 3, 4, 1 the ledger needs to evolve across usage patterns
			- under current structures, all parties must be equally upgraded.
		- 3,4,2 upgrades are usually cyclic and require governance, and multiple versions can't be tested at once
		- 3,4,3 anyone can change the conditions of the software locally. local validation of versioning?
			- canonical account ledger, can be atomically switched by a two-thirds majority using threshold commitment. cross chain calidation allows inter-ledger tracking for accountability.
	- There is a paper on the tokenomics somewhere
	- there is a paper on the technical specifications
	- #question - How are you planning on getting enough people on the network simultaneously so that chain bartering can be accomplished?

### Calls

[[blockchain]],[[Privacy]],[[complexity of value]],[[MEV]], [[Cosmos]],

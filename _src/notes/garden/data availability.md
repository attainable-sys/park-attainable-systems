---
{
 "title": "data availability",
 "date": null,
 "folder": "2000 Blockchain",
 "stem": "data availability",
 "related": []
}
---
Data availability is a core tenet of the available space for a set of transactions - in that there must be sufficient space in a transactional environment for a number of transactions or computations to be authorized for the computational environment to proceed.

## In the context of Blockchain
In the context of blockchain, data availability is a limitation on blockspace - where the number of transactions in a block decreases as the complexity of the transactions increases. As a result, an inability to change the structure of the block environment or to displace portions of the transactions taking up a block to a difference scaling solution (such as [[rollup]]) becomes a scaling limitation on a particular block structure.

A good example of this is the [[Ethereum]] blockchain, whereing execution and smart contracts occupy the same block space and as a result the execution potential of the chain can become limited by smart contract execution, which on average takes up larger amounts of available data in a block.

A potential solution to this is the [[Celestia]] blockchain, which aims to remain an execution-only environment for blockchains, with independent rollups connecting with the execution layer and smart contracts (or other transaction types) remaining in the [[rollup]] environment.

	- [Celestia - ZK Knowledge Podcast](https://zeroknowledge.fm/208-2/)
	- [Fraud and Data Availability Proofs](https://arxiv.org/pdf/1809.09044.pdf) - Al Bassam, M
	- [Rollups, Data Availability, Modular Blockchains](https://polynya.medium.com/rollups-data-availability-layers-modular-blockchains-introductory-meta-post-5a1e7a60119d)

[[Celestia]],[[Ethereum]],[[Evmos]],[[IBC]],[[Cosmos]][[data availability]]

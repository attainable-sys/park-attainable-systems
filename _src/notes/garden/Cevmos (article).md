---
{
 "title": "A Case for Scaling the Ethereum Virtual Machine, but not Ethereum",
 "date": null,
 "folder": "2000 Blockchain",
 "stem": "Cevmos (article)",
 "related": []
}
---
### Or: How I stopped worrying and learned to love the EVM

* [An Open, Modular Stack for EVM](https://forum.celestia.org/t/an-open-modular-stack-for-evm-based-applications-using-celestia-evmos-and-cosmos/89) - Mustafa Al-Bassam
* [Introducing Cevmos](https://evmos.blog/introducing-cevmos-an-open-scalable-and-modular-stack-for-evm-based-applications-72930ce6b85c) - Tharsis
* [Digging into Data Availability](https://podcasts.apple.com/pw/podcast/episode-208-digging-into-data-availability-with-ismail/id1326503043?i=1000543620830) - Zero Knowledge
* [Rollups/Data Availability](https://polynya.medium.com/rollups-data-availability-layers-modular-blockchains-introductory-meta-post-5a1e7a60119d) - Polynya
* [Endgame](https://vitalik.ca/general/2021/12/06/endgame.html) - Vitalik
* [Why L2s will have a token](https://twitter.com/kaiynne/status/1475623723591815168) - kain.eth

## Outline
### 1. Introduction?
* What is the main problem with Ethereum, right now?
    * Understanding the trilemma - scaling, security, decentralization
    * There is another - data availability - and it ties into scalability.
        * Worse yet, it’s not something that can be solved for on the base chain itself. It’s more likely to be solved by changing the settlement layer altogether in order to provide the structure necessary to properly scale the EVM
* What is [[data availability]]?
    * explain that it's something that will probably stop Ethereum from growing
    * Data availability *sampling* vs data availability
    * Example:
        * Imagine the formula “2+2” is  on the blockchain, every time a validator is looking to run consensus they have to run the calculation to determine the answer is 4. The data availability layer will simply store “4” and the consensus layer will store the transaction data.
        * Most of the transaction costs incurred on proof of stake networks is associated with the computation of historical formulas such as 2+2=4 to prove the beginning balance for account ABC is in fact “4”.
        * By removing the validators obligation to prove 4 is the beginning balance and opting instead to call 4 as the beginning balance from the data availability layer (which was already proven and agreed upon), the computation load for validating transactions on the settlement layer  is much lower and cheaper.
## 2. How could the EVM grow, but not Ethereum?
 * Open source, anyone can fork the code, obviously
    * Plenty of examples of EVM clones out there - Solana, Avalanche, Near, and so on.
        * NEAR has sharding built in and touts itself as a data available chain, but the network doesn’t necessarily provide the structures necessary to scale the EVM with clear permissionlessness.
    * What they are not doing is creating single-purpose blockchains. They are looking to create entire new L1 ecosystems,
        * we're starting to realize that doing this is actually not that good of an idea, because L1 ossification and baseload congestion is a real problem, and these chains run up against the trilemma really quickly.
    * EVMs can also be implemented within the rollup environment, creating an execution environment for transactions that can then derive consensus from the settlement layer’s DA solution at minimal cost and with trustful security
* Other points:
    * Public goods - [[IBC]] is the closest thing to a public good that we have for scaling solutions, working within an environment like NEAR, Solana, or Avalanche provides a solution.
    * Polkadot offers a comparable solution, but it’s a completely new ecosystem with less adoption, and the need for Substrate chains to rent-seek in order to have shared security presents an issue that stands in the way of rapid scalability
1. Thinking more abstractly, what is an issue with monolithic transaction environments?
* adaptability issues
* you can't fix what was built broken
    * This is true of all systems - clawing back solutions to the problems that we want to solve means that you’re solving piecemeal.
* through put issues and mounting transaction cost are always going to be a problem on settlement layers that allow too much blockspace to L1-level transactions.
    * This is the reason that projects like Polkadot exist - the core tenet that Gavin Wood saw early on was that data availability was going to be a problem, so he created a technology that built the smart contract environment in a different space than the settlement layer and then created a communication format that allowed contract environments to communicate.
    * This meant that the settlement layer could be used to allow inter-blockchain communication, and to settle transactions against the relay chain that create shared security among all chains connected to the base chain.
## 2. So what's a potential solution to this problem?
* The only way that we’ll get a modular environment that we want is if it’s easy to participate.
    * That means the entire stack must be modular and easy to access, and effectively frictionless in deployment.
    * Any environment that causes structure to be non-modular, or makes it difficult to leave, is effectively not permissionless.
* Modular chain design means that the pieces of the stack are atomic - they can function as well as they need to, and if they don’t work, you can swap them out for pieces that do work
    * This biases toward success, because the atomic structure of each modular piece can be as good as it needs to be, and nothing more. An implementation can be purpose-built, set, seen as valuable, and then implemented across all utilities.

In order to understand what a solution could look like in practice, you can start [here](https://forum.celestia.org/t/an-open-modular-stack-for-evm-based-applications-using-celestia-evmos-and-cosmos/89), where Mustafa Al-Bassam describes what could turn out to be one of the most robust solutions for utilizing the flexibility of the Ethereum Virtual Machine within a data availability architecture.

Talk about each part of the stack

* Cosmos
* [Evmos](figment.io/resources/first-look-evmos)
* Celestia

### 3. Why do all of these work together?

* [Cevmos ](https://evmos.blog/introducing-cevmos-an-open-scalable-and-modular-stack-for-evm-based-applications-72930ce6b85c)- a scaling solution that seeks to combine all pieces of the stack in order to scale the Ethereum Virtual Machine, or EVM

However, in the abstract, there is a case for _anything_ to take this space, since the predominant logic for scaling Ethereum technology  is proceeding in a different direction than what was the initial logic - not that chains will connect to a base-layer chain that can also settle transactions, but rather that there will be interchain modularity in the tech stack. This will result in a (wait for it) cosmos of blockchains allowing for modular construction of purpose-built chains.

## 4. Why is this a big deal?

The future of the EVM is probably not on Ethereum, but it's probably not on any other Layer 1 solution that exists out there - mainly because every other chain that exists is likely to run into the same data availability issue as almost every other Layer 1.

Having a settlement layer that allows for collective consensus to be met quickly means that there is a way for networked growth among a set of rollups to happen quite rapidly, as well as securely at the hands a settlement layer - but this is just one solution.

Using this design logic allows us to reconsider the ‘layered’ approach that we have taken to building out the components of a functioning transactional system. We no longer have one component depending on any other, but instead have components that comprise pieces of the tech stack alongside one another that can be swapped in and out depending on whether or not they accomplish the purpose.

More importantly, it allows us to see the strongest implementation of Solidity within the EVM - single-purpose smart-contract rollups that can be permissionlessly plugged into a settlement layer for security and interoperating using a common message passing format, such as IBC.

In this context, Cevmos marks the first step toward Vitalik’s [‘Endgame’](https://vitalik.ca/general/2021/12/06/endgame.html) - an environment to scale shards of the Ethereum network, but without dealing with the congestion of smart contracts stored on the base chain. Effectively, a protocol like Cevmos moves us away from the dependency on Ethereum, while still leveraging the capabilities of the EVM environment within rollups.

[[Evmos]],[[Cosmos]],[[Ethereum]],[[blockchain]],[[interoperability]],[[Bitcoin vs Ethereum]],[[Cevmos]]

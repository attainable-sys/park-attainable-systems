---
{
 "title": "everyone needs ******",
 "date": null,
 "folder": "2000 Blockchain",
 "stem": "everyone needs ******",
 "related": []
}
---
### The utility of privacy
three fronts need to be grown in order to actually scale crypto:
1. Scalability
2. [[Privacy]]
3. [[User Experience]]
## Arguments against Privacy:
- 'why have privacy if you have nothing to hide' - this is wrong headed because privacy is normal.
- the most adopted privacy technologies are VPNs and adblockers.
things that can't be done due to monetary transparency on blockchains:
- institutional adoption - if transactions aren't private, the biggest participants won't transact
- transparency allows manipulation to pervade the space
## What makes privacy hard to build?
* Shared state models - a network hast o share state across the entirety of the chain, while privacy transactions require part of execution to be off-chain.
* Moving execution to the client-side introduces race conditions
* concurrent access-to-state vs privacy
### [[Tornado Cash]]
Shielded Pools on Tornado allow you to generate a note on your computer - hash is recorded in the Tornado contract to keep original depositor connected to action.
- Anonymity set is the collection of receipt owners engaging with a pool of assets that have 'notes' attached to them on a private account.
### [[Zcash]]
ZEC is not private by default, but tokens can be deposted into a shielded pool and transferred privately.
	Only 8% of supply is shielded. - This could be explained by a compination of supbar tooling/UX and a lack of in-protocol incentives for shielding - i.e. you are trying to get people to use something that they don't actually feel the need to use.

1. Adoption through shielded pools is crucian for privacy, as without adoption the value proposition is lost.

## [[Monero]]

'Shielding' of transactions is done through dummy inputs.

Information cascades and probabilistic re-association can be used to break this model, given time and AI/ML.

"Opt-in privacy 'simply doesn't work" - [[Aztec]], by contrast, doesn't offer anything short of a closed environment within which users operate.

## [[Namada]]
 - Will be using the [[MASP]] to allow for a pool that supports all asset types. -

*Of note here is the fact that both [[Tornado Cash]] and [[Zcash]] require you to use a native token and do not offer multi-asset transfer, in contrast to [[Namada]], which can purely be navigated through multi-asset pooling that encourages and increases security over use privacy through growth of the overall set of private assets.

- "Namada has a single MASP that supports all assets. This is very handy for exotic assets and NFTs, as they share and benefit from the same anonymity set with every other asset."
	"Namada’s Privacy as a Public Good allows users to earn shielded rewards in exchange for contributing to privacy. The subsidy model incentivizes participation regardless of the size of the pool while incurring finite costs"

## [[Aleo]]
* [[zero-knowledge execution environment]] build on WASM that defines a generic off-chain execution and on-chain verification model that can heterogenously secure [[ZKP]]s that are posted to the Aleo chain.
	* Encounters [[race conditions]] where concurrent [[ZKP]]s can seek to fill the same block, though this can/might be avoided using the [[prover]] role to sort and post transactions to the parent chain.

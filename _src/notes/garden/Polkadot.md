---
{
 "title": "Polkadot",
 "date": null,
 "folder": "2000 Blockchain",
 "stem": "Polkadot",
 "related": []
}
---
Polkadot is an industrial scale blockchain solution acts as a metaprotocol for the implementation of Web 3 applications, providing ease of interoperability, shared security, and infinite scaleability.
### Polkadot [[validator]] election
Validator election on Polkadot happens through use of the weighted[[Phragmén election]]algorithm, wherein the algorithm selects the winner of election cycles based on the number of tokens that a nominator holds, and the number of votes that a validator has received.

In practice, a nominator **can select up to 16 validators** with whatever number of tokens that they have bonded to an account for nomination. The nominations are then distributed relative to the number of validators available, the scores that they have in accumulated token votes, and a distribution of the votes that ensures the largest possible amount of validators are elected with the tokens available.

While this can seem quite confusing, the votes are distributed in a deterministic fashion, and it's possible to follow the logic once you've wrapped your head around the voting mechanism, known as the [[Phragmén election]] algorithm.

It's useful to understand this as an election mechanism that allocates votes based not solely on the number of votes that a particular validator has, but also the 'weight' of the other votes allocated by other parties to a validator in previous elections. In practice, this means that even if a validator has a higher amount of direct votes in a round, the weight of votes from previous elections can influence the current election, meaning that a less-allocated validator (in terms of cumulative votes) can be elected based on the distribution of votes from nominators.

#### What does this mean for getting validators elected?
If you're running a private validator set, chances are that we can arrange the election mechanism in a way that we'll be able to elect the maximal number of validators for the amount of DOT or KSM available. Assuming that there is enough of the asset to elect multiple validators, we will manage election through a controller account that we will rebalance on your behalf. However, there's no function on Polkadot or Kusama to permission only specific wallets - the only way we can do so is by setting commission at 100% for the validator and then settling rewards balances off-chain.

For public elections, the method for election becomes a little more chaotic to predict - but it's still deterministic within a certain threshold (otherwise, how would the validators get elected?).

####  Minimum Stake Required for Election

The primary determining factor for getting a validator elected is the minimum stake required in order to be in the 'active set'. This is the minimum amount of DOT tokens required for nomination on a particular validator is a factor of two variables:
- The number of available slots for validation (as of writing this, 297 slots for validation are available on Polkadot)
- The amount of DOT staked by lowest staked validator in waiting.

To simplify, let's posit that there are 5 slots available to validator and 10 validators hoping to fill the slots.
- The top five are elected based on each validator's total stake.
- The lowest staked validator *in the top five* determines the threshold for what is necessary in order for a validator to get elected
- if the 5th highest staked validator has 5 DOT nominating it
- if another validator is nominated with 6 DOT, this validator can take their place as the 5th highest in the next election.
In this situation, the 5 DOT limit would be considered the **Minimum Stake Required**.

In order for a validator to be elected into the active set, Minimum Stake Required threshold that must be crossed before a validator will be a part of the set of 297 validators
#### Rewards Distribution
Polkadot distributes rewards equally to all active validators, such that no matter the amount of tokens staked to a validator from nominators, the amount rewarded and distributed to all active validators is roughly^1 equal.

Validators are selected for block production using the NPoS consensus mechanism that rotates through all active validators Rewards are also not distributed on a constant basis per epoch (roughly ~1d) but rather per era (~4 hours) - so at times it can appear that a validator is not earning rewards. At the end of each epoch, all validators will have been selected for validation, roughly equalizing the total stake distributed to all elected validators.
### Oversubscription

1- It is 'roughly' because validators can also receive network fees and tips that accrue over time, resulting in variations.

Related to: [[canary network]], [[Kusama]], [[blockchain]][[protocol]]

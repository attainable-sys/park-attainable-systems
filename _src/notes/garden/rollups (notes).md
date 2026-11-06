---
{
 "title": "rollups (notes)",
 "date": null,
 "folder": "2000 Blockchain",
 "stem": "rollups (notes)",
 "related": []
}
---
## [new potential sharding design](https://notes.ethereum.org/@dankrad/new_sharding)
- data shards were originally to be arranged in $$n = 64$$ data shards to the beacon chain, n proposers propose shard blobs, confirmed by committees of validators.
- Alternative:
	- sharded data as calldata, block is then constructed by a single builder
	- better integrations with L1 from rollups
	- metablock builders are likely to come about because of MEV extraction anyway.
- advantages:
	- rollup data immediately visible to manager contracts
	- shard scanning logic doesn't need to be implemented
	- no separate PBS (?)
	- sharded calldata can be charged to the tx that is using the calldata
	- data can be confirmed by larger committees (1/32 of val set)
	- beacon and execution blocks can be immediately added to [[data availability]] set
		- light client preparedness and access to [[verkle trees]]
	- ZKR L1<>L2 synchronous calls
	- superlight clients will be possible due to ease of provability for rollups on the L1 layer
Sampling:
- 256 commits to data (up to 512)
- sampling a square of $$ 512\times512 = 2^{18} = 262144 $$ such that any 50% of the block can be sufficient to recrease the whole block, decreasing demands for proving - increasing efficient recovery.
- high bribe resistance
-  - dankrad
 - dankrad

related to: [[blockchain]],[[Ethereum]],[[rollup]]

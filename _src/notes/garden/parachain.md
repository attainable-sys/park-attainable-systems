---
{
 "title": "parachain",
 "date": null,
 "folder": "2000 Blockchain",
 "stem": "parachain",
 "related": []
}
---
A parachain is a sharded blockchain equivalent that earns the shared security of the [[Polkadot]] or [[Kusama]] networks, not having to engage in settlement in its own right through collation of transactions that are then validating by the [[Polkadot]] or [[Kusama]]base chain.

## [[data availability]] in [[Polkadot]] and [[Kusama]]
The great advantage of a sharded format is that the chains that connect to the relay chain can depend on the base chain for their security, and therefore do not need to exhibit their own consensus, while the base chain is able to validate transactions and keep the [[data availability]] of the base chain at a maximum while [[smart contracts]] are executed on the parachains themselves.

## How does one become a parachain?

In order to earn access to the [[relay chain]] for both message passing and execution, parachains must participate in [[slot auction]]s, wherein the parachain raises locked $DOT in order to secure slot access to the base chain.

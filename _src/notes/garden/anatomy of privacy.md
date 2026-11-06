---
{
 "title": "anatomy of privacy",
 "date": null,
 "folder": "2100 Privacy",
 "stem": "anatomy of privacy",
 "related": [
  "Privacy"
 ]
}
---
## Introduction

Now that we've understood the theory of privacy, that there's somewhere we should be looking at Privacy *from*, we need to start to ask questions around what needs to be private, and how, as well as the privacy guarantees that come from having privacy at each layer.

Additionally, for each layer, there should likely be the question of whether or not it should be private, or better at the value of keeping it public might be - since privacy is a question of the cultural safety around deciding what you disclose. If this is true, what should we feel societally compelled to disclose?

## Network level privacy
Where the transactions are happening and how operators on the network make themselves visible. There are schema here for how to maintain privacy, so what are they, how what are functions around how to make thing more or less transparent - what are the reasons for doing so?

e.g. in a ZEXE or in [[Taiga (Anoma)]], the bundles that are held at the network level can be managed in such a way that the contents are not immediately perceivable by an operator role, and the information from the payee who wants a tx to go through might be abstracted away. There are two things at work here - privacy on the layer of the account (who paid) and privacy on the layer of the transaction (what's in the transaction?).

Solutions here are NYM, but what are some reason that you might want to have the network exposed? Why might it be advantageous to think about a network being visible vs not visible? Who does it serve to have either?
## Account level privacy
[[account-level privacy]] is a question of where it is that your assets are being held - meaning, what identifiable information does a particular account hold on a particular user. Ideally, account-level privacy should be a question of the information that is being revealed to those with whom you transact, or at the least is an account of what it is that an individual stores and have the ability to decide that which is available to those who use the information held by an individual account.
## Transaction level privacy
This is the transaction-surface on which transactions are being declared in order for an operator role who settles them to include them in a block.

The issue here is that with something like [[MEV]], there are many who would argue that this makes for an efficient network and market, but the reality of this argument is likely a little bit more nuanced - MEV is only possible if you can see what is within a transaction.

## Runtime-level privacy
Where the transactions are being processed

Here's a question of 'how much do you need to put out in the open in order to get things done' and the fine line between asking if privacy is an ethical position, or if it's *efficiency saving*. Technology like [[ZEXE]] environments make it so that it's possible.

## Privacy makes things run more smoothly
The reason for this is that there's not that much information that needs to enter the system, so the minimum viable information necessary in order to have things work

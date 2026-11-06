---
{
 "title": "What is Quantum Computing?",
 "date": "2024-12-19",
 "date_label": null,
 "kind": "essay",
 "folder": "1125 Quantum Computing",
 "stem": "241219 - What is Quantum Computing",
 "notebook": true,
 "related": []
}
---
What is Quantum Computing?

In the complicated sense, quantum computing is a system of computation that takes advantage of relativistic physics to drastically increase the processing power of computers. In a simpler sense, quantum computers are several times faster than their predecessors, and importantly that when saying they are several times faster, it's by orders of magnitude. A quantum computer can process information that would take a normal computer several hundred years in just a few hours.

The implications is boggling, because that last sentence almost doesn't make sense. There's a law in computing (Moore's Law) that describes the accelerated growth of compute, also known as 'processing power'. In general, it had predicted the the speed of computation to increase substantially based on the silicon chips that had existed before, but quantum computing speed is essentially unprecedented to anyone other than those who literally work in the field of quantum computing.

What was the breakthrough that happened this week?

Historically, any time you have a massive increase in computing ability, you also have a required increase in the energy needed in order to use that processing power; faster processing speed means more things happening, and more things happening means more energy in the system. While breakthroughs in quantum computing over the last 15 years were astounding, they were generally tucked away as the success of energy-intensive laboratories at universities or the research division of companies. Recent historical quantum computers have been described as near-holy copper and glass artifacts extending several floors up into laboratories - not anything that could be described as accessible to the public.

This week, however, Google gave notice of progress on their quantum solution, a chip known as 'Willow'. Willow proclaims to be **10^42 times** more powerful than traditional silicon chips and is expected to be significantly more energy efficient, although precise comparative data on energy consumption has not been disclosed.

What this means is that Google has essentially transformed the trajectory of Moore's Law into a vertical spike. If, with Willow, Google has made progress toward what is known as 'practical quantum computing' (which often implies more stable and efficient quantum processing), then quantum computing could eventually become a consumer-accessible product — something that those with the resources might one day be able to purchase. While this is unlikely to happen in the immediate future, it significantly reduces the technological and energy-related barriers required to meet the processing demands of the chip.

What does it matter to [[2000 Blockchain|crypto]]? How is Crypto protected today?

While this is a significant achievement in the progress of computation, it makes so many things possible that it's important to examine and explore the effects it has on many other industries. In particular, it has implications for what happens to encryption.

In general, encryption is a technology based on code-breaking. It takes normal information and obfuscates, or 'encrypts' it using key information so that only a key holder can unlock it and understand the original contents. The point here is that the 'security' of encryption is mostly based on the time it would take to break a code - where 'breaking' a code essentially means 'trying things until you get the answer'.

Encryption helps you guarantee that what you are looking at is the thing you intend to look at: if you know that you were sent information from only the person you intended to receive it from (even if it's just yourself), you know you are receiving or viewing the same information that was input. If you know no one else could affect that information in any way, this also guarantees that the information can't be tampered with. These two points combine to how crypto benefits from and is built around encryption.

Crypto benefits from this on the principle that financial applications depend on an "agreed upon constant for unit value", or the idea that you can trust that your money is actually your money. Crypto was created because it turns out that if you trust a third party (banks) to hold your money and you don't retain control of what is done with it, they can go off and do things with it themselves. This is a component of what led to the 2008 financial crisis.

Crypto itself is protected by encryption standards, the "time it takes to break a code and reveal information" as a safeguard for showing that the money you own is tied to a set of keys providing the evidence that the money is only yours and that you are the only person who can use it. Most of crypto is protected by SHA256 encoding, which would take 12 "unvigintillion" years to break (that's 1.27 with 67 zeroes after it). This means that with modern computation methods it is practically impossible to reverse a 'hash' (the encoding) in order to get the original result.

It's this encoding that allows people to 'own' crypto - you can feel very certain that you are the only owner of information on the basis that you are the only person in control of the hash that secures your currency.

Where quantum computing matters to crypto is in what it offers as an accelerant for processing power. Even though the 1.27x10^67 year limit is an inconceivably large number for 'breaking' SHA256, if you have a computational system that can increase computational efficiency by 10^42 over traditional silicon chips, then it now only takes 1.27*10^25 years to break.

Without getting into the numbers, what this means is that you go from traditional silicon being able to break crypto's encoding in 10^52 times more time than the age of the universe to quantum computing being able to break it in 10^14 times the age of the universe. That _is_ a drastic improvement in computation; it means that Willow would take [data] less time to do the work.

Roughly speaking, it means that while yes, Willow can drastically increase the speed at which crypto could be broken, it would still take several times the age of the universe to do it. That _is_ a drastic improvement in computation; it means that Willow would take [data] less time to do the work, but at this end of the calculation, the time needed (orders of magnitude older than the age of the universe), there's almost no reason to deploy Willow on this technology in a way that could make tractable progress. It would simply still take too long.

- Could new Quantum Crypto emerge?

It could--there are projects working on this, remarkably--but it's not a real threat.. At least, not until Willow or some other even better technology figures out how to get the time needed to break down the encoding down to an order of time that actually means something to humans.

Humans have only been around for the last fraction of a millisecond that the universe has existed. Until Google can come up with something that can break encoding in a way that makes it a problem that we can worry about on our timescale (rather than the timescale of 'the age of the universe' then crypto will have to worry.

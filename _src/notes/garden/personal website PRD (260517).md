---
{
 "title": "personal website PRD (260517)",
 "date": null,
 "folder": "2266 Technology",
 "stem": "personal website PRD (260517)",
 "related": [
  "personal website"
 ]
}
---
**1. Purpose**
- What problem does the product solve?
	- It solves the problem of putting my art somewhere. I want to be able to take my writing, my thoughts, and my photography, and put them into a format that is interesting and that people will return to.
	- Specifically, I don't want to host my work somewhere that is at the whim of algorithms, and I think this is happening at at time that makes a lot of sense - I think people are tired of having their tastes made for them, and I want somewhere that I can put things that will intrigue people.
		- It will also act as a portfolio - I'd like to understand what it would take for me to set up some sort of backend architecture that would allow me to sell my art without having to manage a whole sale architecture
	- It solves the problem of managing a mailing list and sending something out without depending on these other sources to do it
	- It solves the problem of having to tell people what I'm working on
	- It solves the question of creating things with other people and having somewhere to do that with them
- Who will use it?
	- Me - I want it to be a place that *I* want to visit each day because I want to see how it grows
	- The people who I want to have in my life - whether or not I know them.
	- The people who ask me what I'm working on. This should be a site that people come back to because they want to keep learning what I'm doing and keep tracjk of it - ideall they don't look at their emails and think that it's something they read there, but rather that they *enjoy* reading on my site because of how visually appealing it is built, particularly with the intent to draw in a reader and make them feel comfortable in the context I've created.
	- The people I want to impress, but also who I care about
- How does it align with my strategic goals and initiatives?
	- I want to be more creative while still staying offline, yet I still want a way to show people my art.
		- Because of this. I think that the website needs to be a place where I can deposit things for people to look at and that makes people excited to go back to, a place that is as fun as it is interesting.
	- I want to create things *WITH* people and I think my own website is a place where I can do that
	- I want to show people that I am creative in every medium and I want to create across all of those mediums, and a website for myself will show this off
	- I want to make the internet fun again
		- I miss the period of MySpace that extended out of Geocities where people were learning how to code, and I want to show people that it's easy to do now
		- I want to have a political position about the moat falling down around what it takes to build a website or build technology, because I think it was an artificial moat to start with and it ended up getting a lot of people kicked out of the fun parts of the internet that were enabling people's creativity.

**2. Features**
- Requirements (which define each feature)
	- a gallery for photography that is immersive
	- Chatroom with blank entry (no logins required, usernames required)
		- unless you want to join a mailing list, in which case it should be possible to log in and 'secure a username' (which you are also allowed to change whenever you want to)
	- Blog-style posts that allow for photos to be placed within them and can be scaled across formats (desktop/mobile)
		- A way to subscribe to new posts
	- not necessarily mobile-friendly - desktop-first. I want people to feel like this is something they either want to read as soon as they sit down at their computer, or as they are closing out their day - a place both to catch up and to hang out.
		- mobile adaptable but that should not be the point - it should be better viewed on desktop, and will be feature-limited that way
			- (not a hard requirement, but something I'm interested in seeing how to have work - it would be interesting to wall off certain parts of the experience to 'keep people outside'
		- it would be possible to be in the chatroom and to read articles + render the images ONLY IN THE ARTICLES, but that's it - video should not be viewed on a phone because that's not how it's meant to be consumed
	- something that shows what I'm working on (e.g. where I am in training, etc)
- Context and rationale (that help explain the requirements)
	- A gallery:
		-  I want to display my photos in a better context than what I've been doing, because there are a lot of stories that I have worked on that didn't go anywhere
	- A chatroom
			- I want somewhere that people can drop in and say things, and where I can drop in and catch up on the backscroll (that's what we can call the chatroom!)
	- A blog / writing space
		- I want somewhere to share my unfiltered thoughts, particularly in an unselfconscious way. I harbor an elán for the time where we used to post to things like livejournals, and because this website will be self-hosted, I don't think I'll be worrying about erasure or storage, because everything will be on my personal server instead of someone else's.
	- A context that shows what music I've been listening to lately, what book I'm reading, how far I am into that book, and should take on a similar appearance to my obsidian library.

**3. Release Criteria (should cover five areas)**
- Functionality — minimum functionality required for release
	- A backend and a front end
		- the backend allows me to upload markdown formatted articles to a blog, manage subscriber-only content, host images in a carousel, or jump into the chat
	- Chatroom with non-persistent chat (1-week clear out of all chat logs)
		- BONUS if we can set up a way for someone to create a password for a username, e.g. if someone comes in and selects username 'Foo', they can create a password to hold onto the username. If the user does not log in for 3 months, the username is released and for the first week of anyone else using that username it has a (*newby*) tag next to the handle, to show that the old username has decayed. Chat should be e2ee however possible.
- Usability — how you will ensure the product is easy to use
	- It should work on mobile and desktop, with a bias toward desktop
	- It should have a tangible difference between a subscriber space (a v2 component) and the base access that anyone could have
	- Navigation should look archival - a grid of notecard-like boxes that someone can click on to progress to that section of the site
	- The backend should be accessible on mobile using a username and password
		- BONUS is if we can integrate a need for a ubikey in order to log into the website as admin for the posting backend
- Reliability — how you will determine that the system is sufficiently reliable
	- If it works on both mobile and desktop, that's great, but bias should be to desktop.
	- It runs on a local server. That's a separate issue.
- Performance — the benchmarks the product must achieve
	- It's a basic personal website. I wouldn't worry about this having to manage enormous traffic because I don't think it will have more than 10k hits a month, max. The goal should be to run this on an old computer I have lying around.
- Supportability — how you will ensure the product can be supported by your company
	- I mean it's my personal website, so I hope I'll be doing that.

**4. Timeline**

- Target release window
	- I want to have this done by the end of May
- Project milestones
	- 0.1
		- Blog site with unpopulated gallery and archival spaces
	- 0.2
		- photo carousel
	- 0.3
		- private chatroom that people can procure passwords for
- Release dependencies — known factors (beyond release criteria) that may affect release
	- Setting up a server on my own
	- Actually pinning down the basic requirements and the pathways that will let me post things

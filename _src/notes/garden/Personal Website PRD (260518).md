---
{
 "title": "Personal Website PRD (260518)",
 "date": null,
 "folder": "2266 Technology",
 "stem": "Personal Website PRD (260518)",
 "related": [
  "personal website"
 ]
}
---
**Last updated:** 2026.05.18
**Reference mockup:** `pantalaimon-mockup.html`

---

## 1. Purpose

### What problem does this solve?

It solves the problem of putting my art somewhere. I want to take my writing, my thoughts, and my photography and put them into a format that is interesting and that people will return to.

I don't want to host my work somewhere that is at the whim of algorithms. I think this is happening at a time that makes sense — people are tired of having their tastes made for them, and I want somewhere that I can put things that will intrigue people.

Beyond a creative home, this site needs to:

- Act as a portfolio. I'd like to understand what it would take to set up backend architecture that would allow me to sell my art without managing a full sales infrastructure.
- Solve managing a mailing list and sending things out without depending on third-party platforms to do it.
- Solve having to tell people what I'm working on — the site itself should be the answer.
- Create a space for making things *with* other people.
- Surface the intellectual work (systems thinking, network science, emergence research) that connects everything I do, not just the creative output.

### Who will use it?

- **Me.** I want it to be a place that *I* want to visit each day because I want to see how it grows.
- **The people I want in my life** — whether or not I know them yet.
- **The people who ask me what I'm working on.** This should be a site people come back to because they want to keep track of what I'm doing — ideally they don't look at their emails and think it's something they read there, but rather that they *enjoy* reading on my site because of how visually appealing it is, particularly with the intent to draw in a reader and make them feel comfortable in the context I've created.
- **The people I want to impress, but also who I care about.**

### Strategic alignment

- I want to be more creative while staying offline, yet still have a way to show people my art. The website needs to be a place where I can deposit things for people to look at, that makes people excited to go back to — a place as fun as it is interesting.
- I want to create things *with* people and my own website is the place to do that.
- I want to show that I am creative across every medium and a personal site will demonstrate this.
- I want to make the internet fun again. I miss the period of MySpace that extended out of Geocities where people were learning how to code, and I want to show people that it's easy to do now. I want to take a political position about the moat falling down around what it takes to build a website or build technology — it was an artificial moat to begin with and it ended up getting a lot of people kicked out of the fun parts of the internet that were enabling creativity.
- The throughline across photography, blockchain research, writing, and systems thinking is the same question: *how does information move through a system, and what does it change?* The site should make that throughline visible.

---

## 2. Features

### 2.1 Photography Gallery (0100)

An immersive gallery for photography. Full-width hero images, staggered grid with varied aspect ratios. Metadata (film stock, processing, date) on hover, not cluttering the view. Photos are presented as contact sheets with frame numbers — this is bach.photo work, and it should be treated with that seriousness.

I want to display my photos in a better context than what I've been doing, because there are a lot of stories I've worked on that didn't go anywhere. The gallery should include a photo carousel (distinct from the grid — an interactive, linear viewing mode) and the ability to organize by series.

Published in National Geographic, The New York Times. Three books. This needs to be visible.

### 2.2 Writing / The Notebook (0200)

Blog-style posts that allow for photos to be placed within them and scale across formats (desktop/mobile). I want somewhere to share my unfiltered thoughts, particularly in an unselfconscious way. I have an élan for the time where we used to post to things like LiveJournals, and because this site will be self-hosted, I won't be worrying about erasure or storage — everything will be on my personal server.

Writing entries should support:

- Inline images, scaled responsively
- Tags for categorization (identity, systems, photography, craft, etc.)
- Obsidian-style backlinks connecting entries to other entries, photo series, and systems notes — the thinking is non-linear and the site should reflect that
- A way to subscribe to new posts (RSS at minimum, email subscription as a goal)

Writing categories include essays, systems research, field notes, and process notes. These aren't separate blogs — they're all part of the same notebook, filterable.

### 2.3 The Private Library / Chatroom (0300)

A chatroom — somewhere that people can drop in and say things, and where I can drop in and catch up on the backscroll.

- No login required for entry. Usernames required (self-selected on arrival).
- Non-persistent chat: 1-week automatic clearing of all chat logs.
- Optional persistent identity: a user can create a password to hold a username. If the user doesn't log in for 3 months, the username is released. For the first week of anyone else using that released username, it has a `(*newby*)` tag next to the handle to show that the old username has decayed.
- E2EE however possible. Element/Matrix bridge or self-hosted IRC as backend candidates.
- Named "The Private Library" — a reference to the recurring discussion series I ran at Namada on privacy as social infrastructure. The name carries meaning.

### 2.4 Systems / Emergence & Networks (2222)

A dedicated space for research notes and thinking-in-public about complex adaptive systems, network dynamics, and the structures that hold worlds together. This is the intellectual core — nurse logs, scale-free networks, common pool resources, phase transitions, privacy as infrastructure, the Free Energy Principle.

Presented as a node grid with connection counts, like a public-facing Obsidian graph. Each node links to related writing, photos, and other nodes. This section didn't appear in the original PRD but it's essential — it's the connective tissue between everything else.

Toward a book on emergence and the growth of networks.

### 2.5 Status / What I'm Working On

A persistent, visible block showing current state: what I'm reading (and how far into it), what I'm listening to, training progress, current creative project, location. Should take on a similar appearance to my Obsidian vault's sidebar. This replaces having to tell people individually what I'm up to.

### 2.6 Index / Navigation

Navigation should look archival — the mockup uses a Dewey-decimal numbering system (0000 index, 0100 photography, 0200 writing, 2222 systems, etc.) borrowed from the actual Obsidian vault structure. The index is a grid of linked cells that someone can click to progress to that section. Desktop-first information density.

Additional navigation elements: a reading shelf (current + recent books), RSS feed, guestbook, and links to archived professional work (Figment, blockchain research).

### 2.7 Indie Web Layer

Subtle, not dominant. A few 88x31 badges (codex magna, sapere aude, indie web, no tracking, made by hand, encrypted). Webring membership in the footer. These signal community membership without defining the aesthetic.

### 2.8 Mailing List / Subscriber Space

- A way to subscribe to new posts (email-based, not just RSS)
- A tangible difference between a subscriber space (v2) and base access
- Managed without depending on third-party platforms

### 2.9 Commerce (Future)

Backend architecture that allows selling art (prints, etc.) without managing a full sales infrastructure. Not in scope for v1 but the architecture should not preclude it.

---

## 3. Design Direction

**Reference:** XXIIVV (Devine Lu Linvega). Brutalist, handmade, structure-is-ornament. Limited palette, information-dense, the whole thing feels like a tool you use, not a gallery you look at.

**Palette:** Chromatic, not neutral. Deep indigo-blue base (`#172040`), not black or white. Four to five colors maximum. Warm amber accent (`#f0a050`). The color has identity.

**Typography:** Single monospace family (IBM Plex Mono). No serifs, no display fonts. The text is the interface.

**Photography treatment:** Equal weight with writing and systems work — not subordinate, not dominant. Full-width hero images with breathing room. Staggered grid. Metadata on hover only.

**Platform bias:** Desktop-first. Mobile-adaptive but feature-limited. I want people to feel like this is something they either want to read as soon as they sit down at their computer, or as they are closing out their day. It would be possible to access the chatroom and read articles on mobile, but the full gallery and video should not render on mobile — that's not how the work is meant to be consumed. Walling off parts of the experience to keep people outside is interesting to explore, not a hard requirement.

**Privacy:** No tracking. No cookies. No third-party scripts. AI crawlers blocked via robots.txt. The chatroom is encrypted. Privacy is a practice, not a feature.

---

## 4. Release Criteria

### Functionality

- A backend and a front end.
- The backend allows me to upload markdown-formatted articles to a blog, manage subscriber-only content, host images in a carousel, or jump into the chat.
- The backend should be accessible on mobile using a username and password.
- **Bonus:** Yubikey integration for admin login.

### Usability

- Works on both mobile and desktop, biased toward desktop.
- Navigation is archival — Dewey-numbered grid.
- Subscriber vs. base access distinction (v2).

### Reliability

- Runs on a local server (an old computer I have lying around). That's a separate infrastructure concern.
- If it works on both mobile and desktop, that's great, but bias to desktop.

### Performance

- Basic personal website. Not expecting more than 10k hits/month, max. The goal should be to run this on modest hardware.

### Supportability

- It's my personal website. I'll be supporting it.

---

## 5. Timeline

### Target release

End of May 2026.

### Milestones

| Version | Scope |
|---------|-------|
| 0.1 | Blog site with unpopulated gallery and archival spaces. Dewey-numbered navigation. Status block. Systems node grid (unpopulated). Writing section with backlinks. |
| 0.2 | Photo carousel. Full gallery with series organization. Inline images in blog posts. |
| 0.3 | Private Library chatroom with password-optional usernames, 3-month decay, E2EE. |
| 0.4 | Mailing list / subscriber infrastructure. RSS feed. |
| 0.5 | Subscriber-only content gating. Commerce exploration. |

### Dependencies

- Setting up a local server.
- Pinning down the stack (SSG, backend framework, chat backend).
- Actually writing and photographing the content to populate it.

---

## 6. Open Questions

- What stack? Static site generator (Hugo, Zola, Eleventy) vs. small dynamic server (Go, Rust, Node)?
- Chat backend: Element/Matrix bridge, self-hosted IRC, or something like Chattable?
- Mailing list: self-hosted (Listmonk, Keila) vs. minimal paid (Letterloop)?
- Image hosting: local server storage vs. CDN for the gallery?
- How to handle the mobile feature-gating gracefully — CSS media queries with hidden sections, or actual server-side detection?
- Commerce layer when the time comes — Snipcart, Ecwid, or something lighter?

# codex magna: how this site is built

park.attainable.systems is plain HTML generated from a published slice of the Obsidian vault.

```
_src/
  build.py        renders everything below into the repo root
  notes/
    notebook/     writing: essays, field notes, poems, fiction, craft
    garden/       vault notes: 2222 systems, 2000 blockchain, 2100 privacy, ...
  site.json       the status block on the index (form, location, writing, ...)
  shelf.json      the reading shelf
```

Each note is markdown with a small JSON header (title, date, kind, folder, stem).
`[[wikilinks]]` resolve against published notes by file name; links to notes that
aren't published show as dimmed text. Backlinks, connection counts and Dewey ids
(`2222.056` = 56th note in 2222) are computed at build time.

## Change something

- Edit a note in `_src/notes/…`, or the status in `site.json`.
- `python3 _src/build.py` from the repo root (needs Python 3 and `markdown`).
- Commit and push to `main`. GitHub Pages serves the root.

`deck/` and `drafts/` are never touched by the build. Folders the build owns and
rebuilds from scratch: notebook, notes, systems, vault, photography, library,
about, shelf, figment, guestbook (plus index.html, 404.html, rss.xml, sitemap.xml).

## Publishing more from the vault

The notes here were copied out of the vault by an import script that lives with
the project files (Website Arch), not in this public repo. To publish a new piece,
add it to that script's list and re-run it, or drop a cleaned markdown file into
`_src/notes/notebook/` with the same header shape and rebuild.

# LANE G2 worker F: Gallica scout round 4 (Sonnet, cap $6, Gallica + archivesetmanuscrits fetcher)

Read .claude/briefs/scout.md, QUEUE.md's three Gallica passes (the "M" rows, and "Third pass, 24 September 2026 (M17-M21)" for method,
noise filters and the dc.source corrections), and STATUS.md's lane table. Never promote, never solve.
Controls first: before each new source, show that your query finds one known item (e.g. clair1067 Brienne to the Queen of Poland in
archivesetmanuscrits, 'Lettre avec chiffres', Clairambault 1067 fol.226; or fr.5160 in Gallica SRU). A query that misses its control is
fixed before its zero counts.
Sources not yet swept (each: raw, kept, digitised count):
1. archivesetmanuscrits.bnf.fr item-level descriptions ("lettre avec chiffres", "en chiffre", "chiffrée", "déchiffrement", "chiffre" +
   lettre/dépêche) across Français, NAF, Clairambault, Cinq Cents de Colbert, Mélanges de Colbert, Dupuy, Baluze, Italien, Espagnol,
   Portugais: the item level is where round 3's summary-level SRU sweep was blind (clair1067 was found this way).
2. Bibliothèque de l'Arsenal manuscripts on Gallica (incl. Archives de la Bastille), Mazarine and Institut (Godefroy) partner manuscripts,
   through SRU dc.source scoping.
Drop anything already in QUEUE.md, CATALOG.md, a ciphers/ folder, or either solver repo (grep the ark and shelfmark). Keep only digitised,
un-deciphered, correspondence cipher. Score per the rubric; write new rows M22 onward in a "Fourth pass, 24 September 2026" section of
QUEUE.md and QUEUE-scores.json (rebase first), and sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv. At most ~200 requests per host.
Report per source: raw, kept, digitised; the list of new M rows with ark and folio.

COMMON (every LANE G2 worker, 24 Sept 2026). Parent: LANE G2 orchestrator session_015NqJ9uu5Ef3Bo6QaRiGcGp.
- Read CLAUDE.md in full, then this brief, then the target's NOTES.md sections named below; the last 30 lines of ROOM.md.
- First action: `python3 tools/room.py --start`, then a claim line with `python3 tools/room.py "<role> (<model>, cap $N, for LANE G2)" "claim: <target> -- files: ..."`.
  Last action: a `done:` line with the commit hash and a two-line result. Push with `python3 tools/room.py --push <paths>`; stage by explicit path.
- Run every long job in the FOREGROUND (never background a solver or a fetch loop; two workers went idle that way). Commit and push after each
  pass or step, so a rate-limit stop loses nothing.
- Stop at your cap (the session metadata's cost figure). At the cap, push what you have, write a 'progress' paragraph in NOTES.md, post done.
- Rule 4 grades per token, rule 7 a script that regenerates any reading (prefer tools/decode_key.py with decode.json), rule 3 matched controls for
  any negative. Rule 10: no "new", "first", "unpublished", "previously unread"; say "read at grade X" and "not found in <source>, searched <date>".
  Absolute dates; read `date -u` before writing any time.
- Good-citizen rule: one request at a time per host, >= 1.5 s apart, UA `cipher-lab research script (contact via repository)`, IIIF images only on
  gallica.bnf.fr (.texteBrut is altcha-walled), stop a host on 429/403/challenge and log it. Report requests per host in your done line.
- Keep committed images under 30 MB per folder; above that, keep a manifest and put working copies in your scratchpad.
- End: a short report paragraph in the target's NOTES.md (what was found, where it was not found); do not classify novelty.

# LANE G2 worker X: Gallica scout round 5, the broad archivesetmanuscrits terms that round 4 could not page (Sonnet, cap $6, fetcher)

Read QUEUE.md "Fourth pass, 24 September 2026" (M22-M34: method, the plain POST search resultatRechercheSimple.html, control, and the
pagination cap that left 'chiffre', 'en chiffre(s)', 'avec chiffres' unswept) and the LEDGER lessons of 24 Sept for M22-M34: 8 of 13 rows were
not digitised, and 4 of the digitised ones held no ciphertext ('déchiffrement' items and register copies).
1. Control first: your bucketed query must find clair1067 (Clairambault 1067 fol.226, 'Lettre avec chiffres').
2. Sweep the three broad terms bucketed so each result set stays under the cap: per fonds (Français by thousand ranges, NAF, Clairambault,
   Cinq Cents de Colbert, Mélanges de Colbert, Dupuy, Baluze, Italien, Espagnol, Allemand) and, if still capped, per century.
3. Keep only items that are (a) digitised (DAO link), (b) correspondence cipher by the item text, (c) not already in QUEUE.md, CATALOG.md,
   ciphers/, either solver repo or DECODE's catalogue CSV, and then (d) confirmed to hold ciphertext by ONE 600 px image of the item's leaf
   (canvas from the ark's labels). Prefer items where the text says the decipherment or a clear copy is present (recovery).
4. Rows M35 onward in a "Fifth pass" section of QUEUE.md and QUEUE-scores.json (rebase first), sources/solver-diffs/2026-09-24-lane-g2-gallica5.tsv.
   Report raw, kept, digitised, ciphertext-confirmed. At most ~200 requests per host. Never promote, never solve.

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

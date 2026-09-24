# LANE G2 worker W: other BnF volumes of the Servien (Turin) embassy and Brienne 1659-1661 correspondence with ciphers (Sonnet, cap $3, archivesetmanuscrits + Gallica SRU only, <= 40 requests)

key_1659_ext.tsv (ciphers/fr5160-letellier-1653) is Brienne's table for Ennemond Servien at Turin, Oct-Nov 1659. Find other digitised BnF
volumes holding letters in that table's period and correspondence: Servien (Ennemond or Abel) papers, Brienne's outgoing registers 1658-1661,
Turin/Savoy embassy volumes (fonds français, NAF, Clairambault, Mélanges de Colbert, Baluze), and any "chiffre de M. Servien" key leaf.
Use archivesetmanuscrits' plain POST search (resultatRechercheSimple.html, see QUEUE.md 'Fourth pass' for the method; control: a query that
finds fr.5160 itself) and Gallica SRU with dc.source scoping. For each hit: shelfmark, ark if digitised, dates, cipher note, and whether the
catalogue says deciphered. Output sources/solver-diffs/2026-09-24-lane-g2-servien.tsv and a short NOTES.md section in
ciphers/fr5160-letellier-1653 "Sibling volumes (24 Sept 2026)". No image fetches beyond one thumbnail per hit to confirm ciphertext.

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

# LANE G2 worker D: clair1108-duvergier, Marine key search (Sonnet, cap $5, NOT gallica.bnf.fr)

Target: ciphers/clair1108-duvergier. Read NOTES.md "Key leads and print check (24 Sept 2026)" first: do not repeat what it logged.
Question: does a cipher key (table de chiffre, clef) for the Marine secretariat's correspondence with Dunkerque / Vergier / the commissaires
of the 1690s survive or appear in print?
Search, logging each as searched or unreachable:
1. Archives nationales, fonds Marine: the printed inventory of série B (Didier Neuville, État sommaire / Inventaire des archives de la Marine,
   série B, 1885 onward) on archive.org full text (be-api fts, advancedsearch) and HathiTrust bibliographic API; the SIV
   (siv.archives-nationales.fr) and FranceArchives (francearchives.gouv.fr) for "chiffre" within Marine B2, B3, B7, and Marine G (mémoires et
   documents), where cipher tables are sometimes filed.
2. Service historique de la Défense (Vincennes, Marine) catalogues for "chiffre" 1690-1700.
3. Tomokiyo's pages in sources/cryptiana (local mirror): every page covering 1680-1710 French ciphers (Louis XIV, Pontchartrain,
   Seignelay, Marine, Dunkerque, Jean Bart, privateers); list what each gives (a key table? whose?). Also the DECODE catalogue CSV grep for
   'Marine' 1680-1710.
4. If a key table on Gallica looks likely (e.g. a Marine or Pontchartrain chiffre in fonds français, Clairambault or NAF), do NOT fetch it:
   write its ark and folio in NOTES.md for the orchestrator (LANE G2 owns gallica.bnf.fr).
Output: NOTES.md section "Marine key search (24 Sept 2026)" with a table source | query | result, and any candidate key locations ranked.

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

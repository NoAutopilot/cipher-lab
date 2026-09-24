# LANE G2 worker O: are the open M rows digitised? (Sonnet, cap $3, Gallica + archivesetmanuscrits, about 20 requests)

Rows: M22 arsenal-ms6829-1708, M24 arsenal6334-longueville-1650-59, M25 arsenal-dallion-lanmary-1744, M26 clairambault296-paget-1713,
M28 clairambault528-bouillon-1713, M29 portugais33-saovicente-1667, M30 fr2967-duprat, M34 espagnol142-mercy-1648 (folders under ciphers/).
M23 (Arsenal Ms-6314) turned out not to be digitised. For each row: the finding-aid page on archivesetmanuscrits (DAO / "document numérisé"
link) and, if none, one Gallica SRU query by shelfmark. Record in each NOTES.md a line "Digitised: yes, ark ..., item at canvas ~N (label
checked)" or "Digitised: no (finding aid without DAO; SRU '<query>' 0 records), 24 Sept 2026", and if no, write REQUEST.md (microfilm cote if
the finding aid gives one; no personal data) and set the status word to blocked. One request per URL, >= 1.5 s apart, stop on resets.
Report a table row | digitised | ark | canvas in your done line. Nothing else: no crops, no passes.

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

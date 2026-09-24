# LANE G2 worker T: does the item hold ciphertext? M26 Paget 1713, M30 Duprat, M34 Mercy 1648 (Sonnet, cap $4, Gallica fetcher, <= 60 requests)

Direct image endpoint at 600-1000 px only; one retry per URL, then stop that URL. Lesson today: 'déchiffrement' items and register copies often
carry no ciphertext (M29, M32, M33). For each target, find the item's leaves and say in one line whether there is ciphertext, how much
(lines), whether a decipherment is beside it, and the canvases. Record in NOTES.md; set status closed-negative if the item has no ciphertext.
1. clairambault296-paget-1713 (ark btv1b9000759b): the finding aid's page numbers did not map to the ark's stamps (worker P). Sweep
   thumbnails (e.g. /full/200,/0/default.jpg) in steps of 10 canvases to find English/French letters in a hand and a cipher; then narrow.
   Compare hand and cipher with clairambault1225-paget-1714 (M4) from its images on disk, one line.
2. fr2967-duprat (ark btv1b9059840r): the Duprat 'Autre Dechiffrement de despesche' items: is any ciphertext in the volume beside them?
3. espagnol142-mercy-1648 (ark btv1b10035717h, actually Espagnol 144 tome III): pin the 6 Jun 1648 'instruction chiffrée' and describe it.
   Rename nothing; note the correct shelfmark in NOTES.md.
Report per target: ciphertext yes/no, lines, canvases, decipherment beside.

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

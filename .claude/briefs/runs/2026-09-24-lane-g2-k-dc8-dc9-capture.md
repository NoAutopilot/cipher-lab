# LANE G2 worker K: DECODE nominations DC8 (Baluze 156 f.157-158, 1636) and DC9 (Mélanges de Colbert 127 f.349-350, 1665): pin, capture, passes (Sonnet, cap $7, Gallica fetcher)

Targets: ciphers/decode-2754-bnf-baluze156-1636 (DC8) and ciphers/decode-2678-bnf-colbert127-gravel-1665 (DC9). Read both NOTES.md (LANE N
check-solved verdicts: both open; DC8 has a sibling-key lead, Sabran's cipher broken by Tomokiyo/Lasry, sources/cryptiana/web/GL.htm "Melchior
de Sabran (1631)"; DC9 already transcribed by Bourdeau, colbert/NOTES.md item a: read that transcription, do not copy code; Bourdeau's text is
CC BY 4.0, credit it).
1. Find each volume's Gallica ark (SRU dc.source / archivesetmanuscrits, one or two queries) and pin the folio to a canvas with
   tools/gallica_folio.py; fetch the natives of the cipher leaves only; record images/manifest.json.
2. DC8: crops + two blind Sonnet passes (passA.tsv, passB.tsv); then a mechanical trial of the published Sabran key (typed from GL.htm into
   key_sabran_1631.tsv, cited) on pass A with a shuffled-key control, trial.tsv. DC9: compare Bourdeau's transcription with the image line by
   line (one pass of your own, passA.tsv) and report agreement.
3. NOTES.md section in each folder "Capture and passes (24 Sept 2026)". gallica.bnf.fr and archivesetmanuscrits only; you are one of two
   fetchers. No DECODE login.

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

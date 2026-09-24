# LANE G2 worker L: recovery captures M23 (Arsenal Ms-6314, Hanau 1635) and M32 (fr.2751, De Diou to Mayenne), plus three lookups (Sonnet, cap $8, Gallica fetcher)

Targets: ciphers/arsenal6314-hanau-1635 and ciphers/fr2751-dediou-mayenne (check-solved CS1: open, cipher AND its own decipherment named in
the catalogue). Read both NOTES.md and sources/cryptiana/web/mayenne.htm (two published Mayenne-De Diou tables, other volumes).
1. For each: find the Gallica ark (archivesetmanuscrits item -> Gallica link, or SRU), pin the item's folios to canvases with
   tools/gallica_folio.py, fetch 1000 px views to find the ciphered copy and the decipherment, then natives of those leaves only
   (images/manifest.json; under 30 MB per folder). Record in NOTES.md: folio, canvas, which leaf is cipher, which is decipherment, layout
   (interlinear, facing, separate), date line.
2. Cut line crops (tools/iiif_lines.py --debug) of the cipher and run two blind Sonnet passes (passA.tsv, passB.tsv); one Sonnet pass of the
   decipherment as plain text (dechiffre.txt). Do not align or decode: an Opus aligner follows.
3. Lookups, one or two requests each, reported in ROOM for the other lanes: (a) Gallica arks and canvases for BnF fr.20506 f.136 and fr.2988
   f.9 (LANE R2's DC1; post "for LANE R2: ..."); (b) clair1108-duvergier canvas 251 (fol.247v) native to ciphers/clair1108-duvergier/images
   if it fits under 30 MB, else scratchpad + manifest.
NOTES.md section "Capture and passes (24 Sept 2026)" in each target. gallica.bnf.fr and archivesetmanuscrits only.

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

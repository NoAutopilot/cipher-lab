# LANE G2 worker C: clair1108-duvergier, reconcile passes A and B on the image (Opus, cap $10, disk only)

Target: ciphers/clair1108-duvergier (Clairambault 1108, cipher on f.253 both pages and f.265 both pages; 26 Mar 1696; probably Vergier,
Marine, Dunkerque, to Pontchartrain). Read NOTES.md in full ("Du Vergier leaves", "Key leads", "Passes").

The two passes agree 58.6%, mostly from segmentation: pass A stacks caption/gloss tiers as separate tokens, pass B keeps the dominant layer.
1. Settle the tiers first, from the crops (images/*_s1.jpg, *_s2.jpg): for each line decide what the layers are (main cipher row, clear text,
   caption above/below, a fainter second layer on f.265). Critical question: is any clear text written ABOVE or BELOW numeral groups a
   contemporary decipherment (interlinear gloss), as in clair1067 and fr5160 f.87? Answer with examples.
2. Write ciphertext.tsv (leaf, line, pos, token, conf H/M, layer, alt, note) and, if there are glosses, dechiffre.tsv (line, words, conf),
   via reconcile.py with --check (rule 7). Flag the out-of-range values (601, 700, 1917, 722) after checking them on the image.
3. Describe the structure (number range, frequencies, repeats, where clear and cipher alternate) for a solver. If glosses exist, align
   them to the groups and write key_1696.tsv with a shuffled-pairing control (as clair1067's align_1646.py did) and a decode.json for
   tools/decode_key.py --check, grading per token (C only where the gloss confirms).
4. Report: NOTES.md section "Reconciliation (24 Sept 2026)". No network.

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

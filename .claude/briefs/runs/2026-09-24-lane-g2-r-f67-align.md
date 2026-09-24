# LANE G2 worker R: fr5160 f.67 aligned to its clear text on f.68r: C grades and key_1659 extension (Opus, cap $7, Gallica: 1 native)

Target: ciphers/fr5160-letellier-1653. Read NOTES.md 'Folio 67: reconciled and read' and 'f.68r and f.66r checked' (worker P: f.68r is the same
letter in clear, sentence for sentence), AUDIT.md 'f.67 re-class (V5b)' (N0), and how align_f86.py / joint_key.py built key_1659 from f.87.
1. Fetch canvas 131 (f.68r) native once to your scratchpad (direct image URL; one retry). Transcribe the clear text yourself (dechiffre_f68.txt)
   and have one blind Sonnet subagent do a second pass (dechiffre_f68_B.txt); settle differences on the image. Note any heading or docket.
2. Align ciphertext_f67.tsv to the f.68r text (align_f67.py, in the style of align_f86.py): every group gets the plaintext it stands for.
   Grade per token: C where key_1659's value agrees with the aligned clear text, or where a code missing from key_1659 is fixed by the
   alignment (and consistent at every occurrence); M where they conflict or the alignment is uncertain. Record conflicts with key_1659.
3. Write key_1659_ext.tsv (key_1659 plus codes the f.67/f.68 pair adds, each with its evidence), update decode_f67.json (--check), and rerun
   the f.86/f.88 readings with the extended key only if it changes them, grading unchanged tokens as before.
4. NOTES.md section 'f.67 aligned to f.68r (24 Sept 2026)': grade counts before/after, codes added, conflicts. Update status.json's f.67
   results row grade. No novelty wording (class is AUDIT.md's).

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

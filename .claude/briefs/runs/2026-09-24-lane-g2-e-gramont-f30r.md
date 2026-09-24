# LANE G2 worker E: fr2980-gramont f.30r lines L01, L02, L11, L12 (Opus, cap $6, disk only)

Target: ciphers/fr2980-gramont. Read NOTES.md from the f.30 extended reading to the end (the section ending "Still not French: L01, L02, L11,
L12" and "Inferred from sense only"), atlas/README.md, key.tsv, key_extension_f30.tsv, reading_f30_extended.txt, unkeyed_f30.tsv.
f.29r and f.30 are at N4 (LANE V); do not touch AUDIT.md.
Task: read the four lines that still do not give French. For each: look at the crops (crops/, images/, atlas sheets), test the three
hypotheses NOTES names (nomenclator words; different values for the arch ss2 and the barred zb rather than nulls; the doubtful Af=M, E=B,
Tb=P), and the five sense-only values (eh=T, CROSS=C, q=P, nn=V, A2), each against the whole of f.29r and f.30 (a value that helps one line
and breaks others is rejected). Use infer_unkeyed.py-style hidden-sign scoring with a control (the same test on shuffled positions).
Output: an updated key_extension_f30.tsv only for values with a control behind them (grade S), a regenerated reading (rule 7, via the
existing script and --check), per-token grade counts before and after, and a NOTES.md section "f.30r L01, L02, L11, L12 (24 Sept 2026)"
that says per line: now French (with the reading), French with gaps, or still not, and why. No network.

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

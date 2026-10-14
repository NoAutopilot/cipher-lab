# LANE DEFAULT-account-4-20261014-2135 jobs (account 4, lane orchestrator session_01YKHyJh33ZuzWxzp9J88xTL) -- 14 Oct 2026 21:4x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 21:37 UTC 14 Oct - 07:37 UTC 15 Oct. Gate 0a: no SESSION-SWEEP-account-4 row.
VERIFY-BACKLOG.tsv regenerated 21:40: high rows Birago/ceppo (off limits), low rows birago (off limits) and sachsstaatsarchiv N0 (register
disagreement only, skipped by the two previous account-4 lanes). Backlog = `next_steps.py --hot-only` runnable rows checked against the
14 Oct handoffs' "next" lists (LANE DEFAULT-A4-0935-14, -A2-0911-14, -A1-1840-14); none of their jobs is repeated. Keyed googleapis 503 at
21:4x UTC: the Google Books steps wait for wave 2. Excluded: Birago family, Armstrong, Debosnys, VIV-KEYSTONE (fr16104/fr16106), BNF-FOCUS
holdings (fr3982, fr3985-3990, no.60), clair1161 (Lasry key failed twice: rule 3), fr2933 (waits on a person), cipher-lab-private.
Intake gate 21:4x UTC (tools/intake_gate_check.py, exit 0 each): colbert26-lathuillerie-1644, fr4735-monluc-lansac-poland-1573,
baluze167-davaux-1637, sforza-duke-1447-f15, fr4712-nevers-duchesse, fair-game-2010.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-14-acct1-default-1840-jobs.md` (read it in full, and the
files it points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A4-2135-14 (account 4)"; export `CIPHERLAB_ACCOUNT=account-4` before any tools/room.py call;
- first actions: `git fetch origin && git checkout -B main origin/main`, `date -u`, read the last 40 ROOM.md lines, post a claim line with
  your box end time; fetch and rebase immediately before every push;
- every other rule there holds unchanged (shared-host take/release lines, halfway line, no images in git, gaps_check on `partial`, no
  novelty words, no AskUserQuestion, stop at 80% of cap or box, `date -u` before any time, "cost not visible to this session").

## Wave 1 (21:5x UTC 14 Oct)

### VER-COL50 (Opus, verifier, cap 3.5, box 60 min, no network beyond the print families named): colbert26-lathuillerie-1644 canvas 50
You are a verifier, not the solver (COL26-C50 was an account-1 session). CLAUDE.md "Verifier brief (template)", steps 1-5, on the canvas 50
reading (reading_c50.txt, decode.json job 4, siblings/c50_reading_inputs.py; 442 tokens C 65 / M 343 / U 34; judge FAIL -1.401 vs real_p05
-0.879). Read COL26-C50, A2-COL15 and COL26-SIB first. Your two jobs: (1) rule on the C licence -- for each of the 65 C tokens, is C backed by
known plaintext (a gloss/print on the same leaf or a licensed sibling unit that cleared its own control, CLAUDE.md rule 3 per-unit paragraph)?
regrade any that are not; (2) a rule-7 re-derivation (`tools/decode_key.py ciphers/colbert26-lathuillerie-1644 --check`, and the job-4 inputs
script) and the depth per rule 4a with `tools/depth_check.py`. Novelty: search per template families (a)-(g) as far as the reachable hosts
allow (googleapis 503 counts as unreachable: log it), add JSTOR-QUEUE rows only if a phrase is distinctive. Write/append AUDIT.md (class,
key source, depth, safe/unsafe sentences), carry any regrade into NOTES.md's gaps/Verdict, and the SECOND-OPINIONS-QUEUE row only if N3+.
Do not decode beyond the re-derivation, do not touch other targets.

### MONL-EYE (Opus, cap 2.5, box 50 min, disk only): fr4735-monluc-lansac-poland-1573 the two cheapest gaps
Verdict: "eye check of the 4 doubtful K04 relabels (L05:12, L04:6/8/23) and an i/y fold in align_c268.py, ~$1". Read MONL-ALIGN, MONL-K12 and
MONL-SORT first. (a) look at sort/win/s268_win_04.png and _05.png (and the line crops) for the 4 tokens; revert any relabel the image does not
hold (transcription edit, logged per token). (b) write PREREG-MONL-IY.md before running: an `--fold-iy` option in align_c268.py, confirm count
with and without it, and the shuffled-clear control re-run with the same option (200 shuffles); the option is kept only if the control max stays
under the registered line. NOTES "## MONL-EYE", gaps + Verdict, gaps_check. If the renders are not on disk, regenerate them from the folder's
recorded regen commands (openapi.bnf.fr <= 8, take/release) rather than skip.

### BAL-C275WL (Opus, cap 3.5, box 60 min, openapi.bnf.fr <= 25): baluze167-davaux-1637 the c275 hand's letter signs
Gap: "167 f.135r (c275) bare run ... 13 tokens are unmarked numerals or letter signs the key does not cover in this hand; next: settle this
hand's letter signs (7, 5, i, d-l ...) from the f.127 Memoire's glossed runs". Read BAL167-C275, BAL-WL (the method), BAL22-SHAPE first. Collect
the glossed runs of the same Memoire (canvases already mapped in BAL167-FIN), list each letter sign/unmarked numeral of this hand with the gloss
letter beneath it (>= 3 occurrences to call a value S, else M), then re-read the c275 run with only those additions through decode.json job 5
(`--check` exit 0). Shuffle control: the same value assignment against glosses shuffled within each run, 200 times. NOTES "## BAL-C275WL",
gaps + Verdict, gaps_check. Price looks at ~0.15 each.

### SFZ-R5323B (Opus, cap 3, box 60 min, de-crypt.org: one browser login, <= 15 requests): sforza-duke-1447-f15 R5323 split-label re-test
Verdict: "R5323 blind check with a split label table and value-free exemplar crops, fresh PREREG, ~$1.5". Read SFZ-DEC2 and SFZ-R5323 (gate 4 of
7 FAIL at 3/7, above every control; the label table could not express cu). Write PREREG-SFZ-R5323B.md (gate, controls, the same other-key
controls as SFZ-R5323) and commit it before any blind call. Two blind Sonnet passes, one label group per call, value-free crops only. This is the
second blind attempt with a changed instrument: if it FAILs its registered gate, log R5323 as "untested-by-this-tool" for the eye-pairing
method (CLAUDE.md rule 3, third-attempt clause) and name a different instrument, not a third pass. Take/release de-crypt.org in ROOM (SFZ-DEC3
uses it too: whoever takes first, the other works from disk and waits). NOTES "## SFZ-R5323B", gaps + Verdict, gaps_check.

### SFZ-DEC3 (Opus, cap 3.5, box 60 min, de-crypt.org: one browser login, <= 60 requests): sforza-duke-1447-f15 scat. 1597 nos. 36-114 by heading
LANE DEFAULT-A1-1840-14 next item 1: "nos. 36-114 by heading (~3)". Same method as SFZ-DEC/SFZ-DEC2 (read both). Per record: heading, date,
correspondent, whether a Visconti/Barbavara/Aragon or 1446-47 key; for any 1446-47 key, an overlap count of its sign stock with the f.15/f.5/f.8
inventory against a shuffled control (no decode). Scrub the account name from anything saved. If the request limit is reached before no. 114,
stop and record the band done. Take/release de-crypt.org (see SFZ-R5323B). NOTES "## SFZ-DEC3", known-keys rung + Verdict (and whether the ASMi
REQUEST.md is still needed), gaps_check. Never edit SFZ-R5323B's NOTES section; append yours after it.

### F4712-C95 (Opus, cap 2, box 45 min, openapi.bnf.fr <= 20): fr4712-nevers-duchesse census canvases 95-106
Verdict: "census of canvases 95-106 (f.83v onward) at 600 px via openapi.bnf.fr, ~$1.5". Same method as F4712-C71/F4712-C83 (read both).
For each canvas: clear / cipher / glossed cipher / key sheet; a glossed sibling of the target's sign stock is the thing looked for. Take/release
openapi.bnf.fr (BAL-C275WL shares it). NOTES "## F4712-C95", census table row, gaps + Verdict, gaps_check.

## Sessions (wave 1, spawned 21:43 UTC 14 Oct)
VER-COL50 session_01PQfztoBqpT8NzrcHk4CQUX; MONL-EYE session_018NX2u1xWYxaHxiEBmNMDXY; BAL-C275WL session_01LN7L52uXbFptg9RZUoSxgc;
SFZ-R5323B session_017TMxTsnr48MLUs2Zx6yoBD; SFZ-DEC3 session_01HM8Vw4zHfWwTyQFoqHGp2c; F4712-C95 session_0195WHL8CB2VguvQgemdBnVz.

## Wave 2 candidates (not yet briefed)
MONL-C268B (next c268 band, after MONL-EYE, ~4); BAL169-F22 (numeral-mark image check, after BAL-C275WL, ~2.5); FAIR-LANG (fair-game-2010
per-language letter-count rank + transposition --langs, ~2); GB steps (eckert E591-592, thurloe Verbael, fr4735 phrases) when googleapis answers.

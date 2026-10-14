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

## Wave 1 results (ledgered 22:0x UTC): VER-COL50 3.05 D, BAL-C275WL 2.88 D, SFZ-R5323B 6.25 D (2.08x), SFZ-DEC3 4.66 N, F4712-C95 2.35 N; MONL-EYE live.

## Wave 2 (22:1x UTC 14 Oct). Same common rules. googleapis still 503 at 22:02.

### SFZ-G1 (Opus, cap 4, box 60 min, disk only; de-crypt.org <= 15 only if the R5323 PDFs are not reproducible from r5323/regen.sh): sforza-duke-1447-f15
Verdict: "key_r5323.tsv from two blind passes and decode_key.py on f.5/f.8 against their glosses, ~$2". Read SFZ-R5323, SFZ-R5323B and
PREREG-SFZ-R5323B first. Write PREREG-SFZ-G1.md and commit it before any decode: the gloss-agreement statistic on f.5/f.8 (letters agreeing
with the period gloss), the null (the same key with values permuted within its alphabet, 1000x, and the 11 other-key controls), and the gate.
Build key_r5323.tsv only from what both blind passes agree on (each row graded from the passes; disagreements M or left out), decode with
`tools/decode_key.py` (decode.json job), `--check` exit 0. Price any further blind call at ~0.6 each (SFZ-R5323B: 8 calls = 2x cap): at most 4.
A PASS licenses a key test on f.15 only in a later job; do not read f.15 here. NOTES "## SFZ-G1", gaps + Verdict, gaps_check.

### BAL171-TAIL (Opus, cap 3.5, box 75 min, openapi.bnf.fr <= 230): baluze167-davaux-1637 Baluze 171 canvases 251-464
Verdict item "Baluze 171 canvases 251-464 (~$3)". Same method as BAL171-SWEEP / BAL168-TAIL (read both): 300 px per canvas (~1 request each),
1000 px looks only on candidate cipher canvases (<= 10, ~0.15 each). Release openapi.bnf.fr between batches of ~65 so BAL169-F22 can take it.
NOTES "## BAL171-TAIL", sweep table rows, gaps + Verdict, gaps_check.

### BAL169-F22 (Opus, cap 3, box 60 min, openapi.bnf.fr <= 15): baluze167-davaux-1637 169 f.22r numeral-mark image check
Gap: "169 f.22r name and remaining signs ... next: an image check of the 1-bearing numeral marks on f.22r (the four acutes VER-BAL22 saw: 71',
51', 41', 13') against glossed exemplars of the same hand, BAL-WL method, ~$2.5". Read BAL169-F22, VER-BAL22, BAL22-SHAPE and BAL-C275WL (its
shuffle-control form). Native crops of the four marks beside >= 3 glossed exemplars each; a mark call is S only with a within-run gloss shuffle
control (200x) as in BAL-C275WL; re-read f.22r via its decode job, `--check` exit 0. Take/release openapi.bnf.fr (BAL171-TAIL shares it).
Append NOTES "## BAL169-F22B" after BAL171-TAIL's section if it lands first (rebase; never edit another job's section). gaps + Verdict, gaps_check.

### F4712-C107 (Opus, cap 2.5, box 45 min, openapi.bnf.fr <= 20): fr4712-nevers-duchesse census canvases 107-118
F4712-C95's next: "canvases 107-118 (f.95v on, 36 left), ~1.5". Same method as F4712-C95. Take/release openapi.bnf.fr. NOTES "## F4712-C107",
census rows, gaps + Verdict, gaps_check.

### FAIR-LANG (Opus, cap 2.5, box 45 min, disk only): fair-game-2010 per-language letter-count rank + transposition --langs
Verdict: "per-language letter-count rank and transposition --langs, ~$1". Read FAIR-CRED and FAIR-TRANS. For each language with a corpus in
tools/data (list them), rank the target's letter counts among windows of the same N; then the transposition family with `family_run.py --langs`
(one matched control per language first; a language whose control misses its gate is CONTROL BELOW GATE, not a negative). Both numbers per
language in HYPOTHESES.md. NOTES "## FAIR-LANG", gaps + Verdict, gaps_check.

## Sessions (wave 2, spawned 22:04 UTC 14 Oct)
SFZ-G1 session_01B9oowW1x1EA7S93Et928a9; BAL171-TAIL session_01B6ALuUj7fzQC9wmomjU7cF; BAL169-F22 session_01Y42nNr4JeNdgn8mdQPMjGj;
F4712-C107 session_015VLdSojpDv9svHyMFbNfTq; FAIR-LANG session_01KcK5ciU7cmeVRFGVRKdMWD.

## Wave 2 results (ledgered 22:2x UTC): MONL-EYE 3.48 D, F4712-C107 2.54 N, FAIR-LANG 1.91 N, BAL169-F22 4.76 D, SFZ-G1 3.27 N (gate FAIL,
blind-read R5323 retired); BAL171-TAIL live. Workers so far 35.15.

## Wave 3 (22:3x UTC 14 Oct; last wave). Same common rules. googleapis 503 at 22:25.

### SFZ-DEC4 (Opus, cap 3.5, box 60 min, de-crypt.org: one browser login, <= 60 requests): sforza-duke-1447-f15 scat. 1597 nos. 79-114, 169-171
Verdict: "DECODE scat. 1597 nos. 79-114 and 169-171 by heading, one login (~45 requests), ~$2" (R5323 failed its gloss gate in SFZ-G1). Same
method as SFZ-DEC3 (read it; it hit its limit at no. 77 with ~1.4 requests per record: plan for that). Per record: heading, date, correspondent,
Visconti/Barbavara/Aragon or 1446-47 key; for any such key, the SFZ-DEC3 stock-overlap test against random stocks (no decode, no blind reads:
blind reading of R5323 is retired). Scrub the account name from anything saved. NOTES "## SFZ-DEC4", known-keys rung + Verdict, gaps_check.

### MONL-C268B (Opus, cap 4.5, box 75 min, openapi.bnf.fr <= 10 only if the line crops are not on disk/regenerable): fr4735-monluc-lansac-poland-1573
Gap: "rest of c268 (about 870 signs) ... next: two blind cipher passes of the next c268 band plus reconciliation, then align_c268.py on the longer
stream, ~$3 per 5-10 lines". Read MONL-ALIGN, MONL-SORT, MONL-EYE first. Band: c268 L06-L10 (5 lines). Crop step as a command
(`tools/iiif_lines.py --image ...`) pasted before the first subagent call; one line per subagent call; 2 passes x 5 lines = 10 calls + 1
reconciliation, priced ~0.35 each (stop before a unit that would cross 80% of cap). Then `align_c268.py` (with the MONL-EYE --fold-iy default) on
L01-L10 against ff.140r-141r, with its shuffled-clear control (200x); report confirm counts for L06-L10 alone and for L01-L10. NOTES
"## MONL-C268B", gaps + Verdict, gaps_check.

### F4712-C119 (Opus, cap 2.5, box 45 min, openapi.bnf.fr <= 20): fr4712-nevers-duchesse census canvases 119-130
F4712-C107's next: "canvases 119-130, ~1.5 (24 left)". Same method. NOTES "## F4712-C119", census rows, gaps + Verdict, gaps_check.

### FAIR-IC (Opus, cap 2.5, box 45 min, disk only): fair-game-2010 substitution-invariant profile per language, then masc --langs
Verdict: "substitution-invariant profile rank per language, then masc --langs on what survives, ~$1". Read FAIR-LANG first (and its PREREG).
Write PREREG-FAIR-IC.md before any score: IC and sorted-frequency profile of the target ranked among same-N windows of each tools/data corpus
(and of homophonic-free random strings as the floor); languages above their own p01 survive; then `family_run.py --family masc --langs` on the
survivors only (matched control per language first; CONTROL BELOW GATE is not a negative). HYPOTHESES.md rows. NOTES "## FAIR-IC", gaps + Verdict,
gaps_check.

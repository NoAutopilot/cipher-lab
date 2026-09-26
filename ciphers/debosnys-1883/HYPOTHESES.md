# Debosnys cryptograms -- hypotheses and prior attempts

Working file for the four Debosnys cryptograms (1883, Essex County jail; NOTES.md holds the check-solved verdict, the
image manifest, and the GOLD-0D/B2/4A/4B/4C/4E sections this summary rests on). Everything below the first `##` is
append-only, dated and signed by the job that wrote it; `tools/family_run.py` appends its rows under its own
marker at the end. This top block is rewritten once per cycle by the lane's consolidator and by nobody else.

**Summary, cycle 3** (GOLD-CONS3, Fable, session_01UBBcnhMmQEpPpdNQgDfsTE, 25 Sept 2026 23:08 UTC; replaces the
cycle-2 block of 21:12 UTC, whose target facts are unchanged and restated here)

**Where the target stands.** Six page images on disk (c1, c2a, c2b, c3, c4a, c4b), 1251 signs over **160 ids** after
GOLD-4C's by-eye split (29 `_` and 35 `MULTI` boxes excluded), pooled IC 0.0391 against uniform-at-K 0.0063 and French
0.0697. X is 201 of 1251 (16.1 pct), self-adjacent 28 times. 73 ids occur under three times; twenty singletons are
pictograms. At base level (GOLD-D1, mechanical from GOLD-4C's composite names) the inventory folds to **K_base 128**
with 16 mark classes (DASH 63, TILDE 61, O 31, DOT 21, DASH2 16, BAR 10, six classes under 7; 233 marked boxes of
1251, 18.6 pct); IC rises to 0.0489 pooled (c1 0.0549, c2 0.0535, c3 0.0528, c4 0.0377). Transcription agreement is
unchanged since cycle 1: c4 22.4 pct at 68 ids (GOLD-4A), c1 62.3 pct full-id / 66.4 pct family-level at 160 ids
(GOLD-4E, 52 columns unsettled); the settled ceiling on the image is about 91 pct (GOLD-4C on c4). No cryptogram is at
the 80 pct gate; `ciphertext.txt` still holds LANE B2's k=90 draft. Check-solved: open (GOLD-0D).

**The measured base-level curve replaces every working assumption** (GOLD-D1 and GOLD-D2, `tools/family_run.py
--family homophonic`, fr19, `profile=target`, `noise=p`, seeds 1-3, restarts 8, controls only; the target was never run):

| design | N | K | type noise | CONTROL mean plaintext letters recovered (range) |
|---|---|---|---|---|
| BM base level, all four | 1251 | 128 | 0 | 0.859 (0.802-0.966) |
| BM base level | 1251 | 128 | 0.025 | 0.816 (0.713-0.942) |
| BM base level | 1251 | 128 | **0.05** | **0.385 (0.199-0.483)** |
| BM base level | 1251 | 128 | **0.075** | **0.322 (0.090-0.517)** |
| BM base level | 1251 | 128 | 0.10 | 0.314 (0.245-0.378) |
| BM c2 alone | 734 | 102 | 0 | 0.669 (0.456-0.898) |
| BM c2 alone | 734 | 102 | 0.05 | 0.433 (0.256-0.533) |
| H, K 160 | 1251 | 160 | 0 | 0.440 (0.034-0.822) |
| H, K 160 | 1251 | 160 | 0.05 | 0.421 (0.219-0.693) |
| H, K 160 | 1251 | 160 | 0.10 | 0.325 (0.310-0.349) |
| H, K 160 | 1251 | 160 | 0.20 | 0.230 (0.204-0.258) |
| H, K 160 minus every X | 1050 | 159 | 0 | 0.230 (0.101-0.305) |

The cliff sits between 2.5 and 5 pct type noise at this N and K (0.816 to 0.385) and the curve is flat from 5 to 10
pct. A settled two-pass transcription carries 5-10 pct type noise (GOLD-4C's 91 pct ceiling), i.e. it lands on the flat
part. Committing to c2 alone (the only cryptogram long enough to read on its own) buys nothing at the same noise (0.433
vs 0.385). **The gate written before the numbers (base-level mean >= 0.5 at 0.05 AND >= 0.4 at 0.075) fails on both
conditions: (c) for the letter families.** The settlement pass is not bought. The statement of record, now also in
`specs/debosnys-1883.json` `cheap_test_done` "3-control-2" (`status_cycle3`): transcription-limited at K 128/160 -- no
letter-substitution control reads above 0.4 past 5 pct type noise at N 1251 (or at N 734 for c2 alone).

| family | status after cycle 3 | CONTROL | TARGET | what is left |
|---|---|---|---|---|
| T transcription | **partial, below gate**; no pass bought | settled ceiling about 91 pct (c4); the curve says 5-10 pct noise reads 0.31-0.39 | c1 62.3 / 66.4 pct; c4 22.4 pct | nothing until a key sheet or a clear-poem crib fixes type identity (ASKS 52) |
| H homophonic, K 160 | **parked with numbers** | 0.440 clean, 0.421 at 5 pct, 0.325 at 10 pct | never run (single-pass draft is about 20 pct noise) | nothing at this K |
| BM base + mark, K_base 128 | **parked with numbers, (c)** | 0.859 clean, 0.816 at 2.5 pct, 0.385 at 5, 0.322 at 7.5, 0.314 at 10 | never run | reads only below about 3 pct type noise, which no eye-settled pass reaches; reopen on a key sheet or a second base fold that drops K well under 100 |
| NC nomenclator / code (incl. a syllable code, base = consonant, mark = vowel) | **parked; no test the draft supports** (below) | none | -- | museum key sheet (ASKS 52) |
| V verse form | **parked with numbers** (GOLD-4B r 0.44, 93.6th percentile of the shuffle null) | shuffle null | -- | the Greek poem on the c4 reverse (not on disk) |
| L language | **open**, French first | fr19 (2.66M letters) | -- | en, la, pt only after a French control reads on a gated transcription |

**NC: does any test exist that a single-pass draft supports?** No. A code or syllable-code control at N 1251 needs the
same type identity a letter-substitution control needs, and has more types per token (a syllabary's K is larger than a
letter alphabet's), so its noise tolerance can only be worse than the curve above; the `syllabary` family in
`family_run.py` (LANE R8, DSN) lays its control on a measured error mix of 5 pct, which is already on the flat part of
this curve. The draft is at about 20 pct and the settled ceiling at about 9 pct. One observation with a number, recorded
and not briefed: under the syllable-code shape (a mark on a consonant base = the following vowel) roughly half of the
tokens should carry a mark, and 233 of 1251 (18.6 pct) do; the mark share does not fit that shape unless vowels are
mostly written as standalone bases, which is a nomenclator again. An exact type identity is therefore not reachable
from the images alone at this K and N; it is reachable only from the museum (a key sheet, or the clear poems as a
crib that pins types by position, ASKS 52).

**NEAR.md row: none, and why.** Rule 5's amendment gives a NEAR row to a target where a solver beat its matched
control by a reproducible margin, or where a control showed the negative was not a real test. Neither happened here:
no solver has run on the target at all, and the controls measured the transcription's ceiling, not a solver's
failure. There is no control-backed gap to report. The register is this block and the spec's `cheap_test_done`;
status stays `open` (rule 5: never closed-negative, since no family has been run on the target with a passed control).

**Recommendation on the lane's Debosnys spend: park.** Spend nothing until the museum answers ASKS 52 (a key sheet
settles the question; the clear poems give a crib). What would reopen it without the museum: a second base fold that
drops K_base well under 100 with a documented rule (GOLD-D1 kept O-SLASH, DAGGER-O and the BAR variants standalone),
re-priced by one $2 control box on the same curve before any image work; or higher-resolution images of c2 that lift
the settled ceiling above about 97 pct, which the Schmeh copies cannot. No cycle-4 Debosnys brief.

Rule 10: nothing in this file is a reading; status stays `open`; the lane never writes solved, new, first or
unpublished.

*Cycle 4, GOLD-CONS4 (Fable, session_01CSQuomCj5Simbsx6r6VVcK), 26 Sept 2026 00:47 UTC: unchanged, parked on ASKS 52 (Adirondack History Center Museum: key sheet or clear poems). Nothing ran on this target in cycle 4; the cycle-3 block above stands as the numbers of record (base-level control 0.816 at 2.5 pct type noise, 0.385 at 5; no target run, no NEAR.md row); no cycle-5 Debosnys brief.*

## GOLD-D1, noise-matched controls (25 Sept 2026, session_01Qcv68Pn46JNXkktRXTv6DL, Sonnet)

Brief: `.claude/briefs/runs/2026-09-25-lane-gold-c2-debosnys-noise-control.md`. Cap $5 / 60 min, started 19:57
UTC. Intake gate at launch: `debosnys-1883: open (line 1) -- edition/page or full-text-search citation found
within 6 lines` (exit 0). Controls only throughout: the target ciphertext is never solved (Do item 6). No
images, no decoding, no transcription.

**1. Base + mark recount** (`scripts/base_mark_recount.py`, mechanical, from GOLD-4C's own composite naming --
no image work; the composite/standalone split is this session's own name-based judgement, documented in the
script's docstring): **K_base = 128** from the 160 sign ids, **16 mark classes** (plus "none" for the 113 ids
that fold to themselves): DASH=63 boxes, TILDE=61, O=31, DOT=21, DASH2=16, BAR=10, BAR-X=6, DASHBELOW=6,
BAR-CC=6, DOTS=3, PLUS=2, BRACKET=2, BAR-O=2, DOT-STEM=2, II=1, DASH-DOTS=1 (none=1018). This session's
composite table settles on 46 composite ids covering 233 boxes, not GOLD-4C's own descriptive "36 ids / 267
boxes" (HYPOTHESES.md summary above) -- the gap is mostly the two GOLD-4A resplit ligatures O-SLASH (27 boxes)
and DAGGER-O (18) that end in an "-O"/"-DASH"-like suffix but that NOTES.md's GOLD-4C section describes in
prose as one merged shape (a loop with a diagonal stroke; a cross over a loop), not a base carrying a separately
stacked mark, so this table keeps them standalone. IC by cryptogram, base level vs the existing 160-id numbers
(`scripts/base_mark_recount.py`'s own IC, not compute_ic.py's controls):

| group | N | K_base | IC_base | K_160 | IC_160 |
|---|---|---|---|---|---|
| c1 | 132 | 48 | 0.0549 | 58 | 0.0397 |
| c2 (2a+2b) | 734 | 102 | 0.0535 | 123 | 0.0465 |
| c3 | 116 | 46 | 0.0528 | 59 | 0.0352 |
| c4 (4a+4b) | 269 | 72 | 0.0377 | 85 | 0.0282 |
| combined | 1251 | 128 | 0.0489 | 160 | 0.0391 |

**2. Two new `tools/families/homophonic.py` params**, offline tests in `tools/tests/test_homophonic_family.py`
(3 cases, all passing): `--param profile=target` allots the K homophones by a fair-share greedy (reserve the L
smallest target buckets one per present letter so no letter starves, then hand out the remaining K-L buckets
largest-first to whichever letter's running share is furthest below its own corpus frequency) so the control's
own sorted sign-count profile tracks the target's shape, including one lopsided top sign; `--param noise=p`
redraws a share p of control tokens post-encipherment, weighted by the target's own counts by rank (the
Salviati recipe, `ciphers/fr2933-salviati-1525/control/codemark_curve.py`). Default behaviour (no params) is
byte-for-byte the old `homophonic_anneal.make_control`, checked by the test suite. First implementation attempt
(committed, then corrected within this same job before any control numbers were reported) built the per-letter
homophone COUNT by the plain frequency largest-remainder rule and only used target buckets as within-letter
weights: that spreads a frequent letter's occurrences over many similarly-sized homophones and could not
reproduce a single dominant sign (L1 946 against the target's own profile, see below); the fair-share version
fixes it (L1 152).

**3. Controls only**, fr19 corpus, `--seeds 3 --restarts 8`, `--tokens space`, scratch ciphers filtered of `_`
and `MULTI` rows (Do item 3 forbids running the target):

| configuration | N | K | noise | CONTROL mean (range) | gate 0.6 |
|---|---|---|---|---|---|
| A: K160 (`ciphertext_draft.tsv`) | 1251 | 160 | 0 | 0.440 (0.034-0.822) | no |
| A: K160 | 1251 | 160 | 0.1 | 0.325 (0.310-0.349) | no |
| A: K160 | 1251 | 160 | 0.2 | 0.230 (0.204-0.258) | no |
| B: base level (`ciphertext_draft_base.tsv`) | 1251 | 128 | 0 | **0.859 (0.802-0.966)** | **yes** |
| B: base level | 1251 | 128 | 0.1 | 0.314 (0.245-0.378) | no |
| C: K160 minus every X row | 1050 | 159 | 0 | 0.230 (0.101-0.305) | no |

(Realised K per run is at or a little below the nominal K -- a low-weight homophone can go undrawn across only
~1,050-1,251 positions; not a defect, see the test suite's own note.) Full rows with corpus files and exact
seeds are in the family_run.py table below, labelled `GOLD-D1 homophonic fr19 control, ...`.

**4. Side output**, sorted sign-count profile vs the target's own (seed 1, config A, `profile=target`):
target top-5 `[201, 63, 48, 42, 39]` (K=160, N=1251); control top-5 `[219, 60, 54, 52, 49]` (K=135 realised,
N=1251); **L1 distance between the two sorted profiles = 152** (of a possible 2*1251=2502 if the two profiles
shared no mass at all) -- so letter-homophonic at K 160 does reproduce a sign at about the target's own top
share (219/1251 = 17.5 pct here, against X's 16.1 pct) once profile=target is used; the earlier, uncorrected
allotment (per-letter count set first, target buckets only as within-letter weights) could not (top control
sign 59/1251 = 4.7 pct, L1 946) -- see point 2.

**5. Branch: (b).** Clean (noise=0) control mean is 0.440 at K160 (config A) but **0.859 at K_base=128**
(config B) -- at or above the 0.6 gate only at base level, so per the top block's decision rule: **BM (base +
mark) has headroom, H (full 160-id homophonic) does not.** Neither design clears the gate once any transcription
noise is added (10 pct: A 0.325, B 0.314; 20 pct: A 0.230), consistent with the Salviati curve's own warning
that Debosnys' higher K/N can only read worse than Salviati's code+mark at 10-20 pct noise (24-43 pct there,
vs the letter-substitution numbers here, a different design so not directly comparable, but the same direction).
Dropping X (config C) does not help at K160 (0.230, actually below the K160 baseline, likely just fewer tokens
per remaining sign with the same K). Per the top block's own cycle-2 wiring: **the next transcription settlement
pass, if the orchestrator books one, should target base-level ids (fewer confusable classes, per NOTES.md's own
c1 base-vs-full agreement, 66.4 vs 62.3 pct), not the full 160-id inventory**, and only a clean (near-zero-noise)
transcription is worth annealing at either level -- a single pass at ~20 pct noise (T family's own measured
floor) reads below both configs' 10-pct-noise numbers already.

Rule 10: nothing here is a reading; grade S throughout (no H, no C); status stays `open`. Files: `glyphs/base_mark.tsv`,
`ciphertext_draft_base.tsv`, `scripts/base_mark_recount.py`, `tools/families/homophonic.py`,
`tools/tests/test_homophonic_family.py`, this section, `specs/debosnys-1883.json` (`cheap_test_done` "3-control"
entry). Requests: none (disk and CPU only). Subagents: none.

## GOLD-D2, base-level noise curve (25 Sept 2026, session_019a43vGLshPA8EZvcuNjGCG, Sonnet)

Brief: `.claude/briefs/runs/2026-09-25-lane-gold-c3-debosnys-base-curve.md`. Cap $3 / 30 min, started 21:39 UTC.
Intake gate at spawn: `debosnys-1883: open (line 1) -- edition/page or full-text-search citation found within 6
lines` (exit 0). Controls only throughout, exactly D1's procedure (`tools/family_run.py --family homophonic`,
fr19 corpus, seeds 1-3, restarts 8, `--tokens space`, `--param profile=target`): scratch copies of
`ciphertext_draft_base.tsv` and `ciphertext_draft.tsv` with the `_` and `MULTI` rows dropped, made and kept in
this session's scratchpad, never in the tree; `base_mark_recount.py --check` exited 0 before any run (the
committed base-level files were fresh). The target was never run.

This job fills the two points D1's curve did not have between clean and 10 pct noise, at the noise level a
settled two-pass transcription is expected to carry (about 5-10 pct, GOLD-D1/GOLD-4C), and prices settling one
cryptogram (c2, the longest, N=734) alone before the whole four-cryptogram inventory.

**A. Base level, all four cryptograms** (N=1251, K_base=128 nominal; `ciphertext_draft_base.tsv` scratch copy):

| noise | CONTROL mean (range) | realised K per seed |
|---|---|---|
| 0 (D1) | 0.859 (0.802-0.966) | -- |
| 0.025 | **0.816 (0.713-0.942)** | 108, 111, 106 |
| 0.05 | **0.385 (0.199-0.483)** | 109, 109, 107 |
| 0.075 | **0.322 (0.090-0.517)** | 107, 110, 108 |
| 0.10 (D1) | 0.314 (0.245-0.378) | -- |

The curve drops sharply between 0.025 and 0.05 (0.816 -> 0.385), then is roughly flat from 0.05 to 0.10 (0.385,
0.322, 0.314) -- consistent with a control that is already past its noise-tolerance knee by 5 pct and has little
further to lose by 10 pct. There is no point above the 0.5 line at or past 0.05.

**B. c2 alone, base level** (N=734, K_base=102 realised -- matches D1's recount table; `ciphertext_draft_base.tsv`
rows with line id `c2*` only, same scratch filtering):

| noise | CONTROL mean (range) | realised K per seed |
|---|---|---|
| 0 | **0.669 (0.456-0.898)** | 82, 85, 88 |
| 0.05 | **0.433 (0.256-0.533)** | 82, 85, 88 |

Settling c2 alone buys a higher clean mean than the four-cryptogram base level did at 0.025 (0.669 vs the
all-cryptogram curve's own 0 pt of 0.859 is not comparable design-for-design, but c2 alone's own 0.05 point,
0.433, is close to the all-cryptogram 0.05 point, 0.385 -- committing to one long cryptogram does not buy
materially more headroom than committing to all four at the same noise level).

**C. K160 (full 160-id inventory), for the record** (N=1251, K=160 nominal; `ciphertext_draft.tsv` scratch copy,
same filtering):

| noise | CONTROL mean (range) |
|---|---|
| 0.05 | 0.421 (0.219-0.693) |

Sits between D1's own 0 and 0.10 K160 points (0.440, 0.325) as expected; base level is still the better design at
this noise level (0.385 vs 0.421 is within range overlap, no clear separation at N=1251, K~128 vs K~160 once noise
is added -- the base-level advantage D1 found is a clean-signal effect that narrows once noise dominates).

**Gate (written before these numbers existed, top block "Summary, cycle 2"): settlement licensed only if the
base-level mean is at or above 0.5 at noise 0.05 AND at or above 0.4 at noise 0.075.** Measured: **0.385 at 0.05
(below 0.5) and 0.322 at 0.075 (below 0.4)** -- both conditions fail, so the verdict is **(c) for the letter
families**: no letter-substitution design (base level, K160, or c2 alone) reads above the gate at the noise a
settled transcription is expected to carry, so a c1 or c2 image-settlement pass is not licensed by this job's
numbers. The target is parked as transcription-limited at K160/K_base128; no letter-substitution control reads
at N=1251 (or at N=734 for c2 alone) at 5-10 pct noise. Per rule 5, this keeps the register `open`/`partial`, not
`closed-negative` (BM still has real headroom at 0 and 2.5 pct noise, and no control has been run below 2.5 pct
except D1's own clean point).

Rule 10: nothing here is a reading; grade S throughout (no H, no C); status stays `open`. Files: this section,
`specs/debosnys-1883.json` (`cheap_test_done` "3-control-2" entry), `ciphers/debosnys-1883/NOTES.md` (GOLD-D2
paragraph). Scratch cipher copies lived only in this session's scratchpad, never committed. Requests: none (disk
and CPU only). Subagents: none.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 20:15 | homophonic | N=1251 K=160 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0 | 1-3 | 0.261 (0.177-0.357) | not run (control-only) | - | no | GOLD-D1 homophonic fr19 control, K160 profile=target noise=0 |
| 25 Sept 2026 20:16 | homophonic | N=1251 K=160 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0.1 | 1-3 | 0.216 (0.142-0.256) | not run (control-only) | - | no | GOLD-D1 homophonic fr19 control, K160 profile=target noise=0.1 |
| 25 Sept 2026 20:17 | homophonic | N=1251 K=160 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0.2 | 1-3 | 0.147 (0.137-0.165) | not run (control-only) | - | no | GOLD-D1 homophonic fr19 control, K160 profile=target noise=0.2 |
| 25 Sept 2026 20:17 | homophonic | N=1251 K=128 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0 | 1-3 | 0.755 (0.366-0.974) | not run (control-only) | - | yes | GOLD-D1 homophonic fr19 control, base level profile=target noise=0 |
| 25 Sept 2026 20:18 | homophonic | N=1251 K=128 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0.1 | 1-3 | 0.318 (0.186-0.479) | not run (control-only) | - | no | GOLD-D1 homophonic fr19 control, base level profile=target noise=0.1 |
| 25 Sept 2026 20:19 | homophonic | N=1050 K=159 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0 | 1-3 | 0.346 (0.284-0.449) | not run (control-only) | - | no | GOLD-D1 homophonic fr19 control, K160 minus X (N1050 K159) profile=target noise=0 |
| 25 Sept 2026 20:22 | homophonic | N=1251 K=160 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0 | 1-3 | 0.440 (0.034-0.822) | not run (control-only) | - | no | GOLD-D1 homophonic fr19 control, K160 profile=target noise=0 |
| 25 Sept 2026 20:23 | homophonic | N=1251 K=160 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0.1 | 1-3 | 0.325 (0.310-0.349) | not run (control-only) | - | no | GOLD-D1 homophonic fr19 control, K160 profile=target noise=0.1 |
| 25 Sept 2026 20:23 | homophonic | N=1251 K=160 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0.2 | 1-3 | 0.230 (0.204-0.258) | not run (control-only) | - | no | GOLD-D1 homophonic fr19 control, K160 profile=target noise=0.2 |
| 25 Sept 2026 20:24 | homophonic | N=1251 K=128 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0 | 1-3 | 0.859 (0.802-0.966) | not run (control-only) | - | yes | GOLD-D1 homophonic fr19 control, base level profile=target noise=0 |
| 25 Sept 2026 20:25 | homophonic | N=1251 K=128 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0.1 | 1-3 | 0.314 (0.245-0.378) | not run (control-only) | - | no | GOLD-D1 homophonic fr19 control, base level profile=target noise=0.1 |
| 25 Sept 2026 20:25 | homophonic | N=1050 K=159 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0 | 1-3 | 0.230 (0.101-0.305) | not run (control-only) | - | no | GOLD-D1 homophonic fr19 control, K160 minus X (N1050 K159) profile=target noise=0 |
| 25 Sept 2026 21:41 | homophonic | N=1251 K=128 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0.025 | 1-3 | 0.816 (0.713-0.942) | not run (control-only) | - | yes | GOLD-D2 homophonic fr19 control, base level profile=target noise=0.025 |
| 25 Sept 2026 21:42 | homophonic | N=1251 K=128 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0.05 | 1-3 | 0.385 (0.199-0.483) | not run (control-only) | - | no | GOLD-D2 homophonic fr19 control, base level profile=target noise=0.05 |
| 25 Sept 2026 21:42 | homophonic | N=1251 K=128 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0.075 | 1-3 | 0.322 (0.090-0.517) | not run (control-only) | - | no | GOLD-D2 homophonic fr19 control, base level profile=target noise=0.075 |
| 25 Sept 2026 21:43 | homophonic | N=734 K=102 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0 | 1-3 | 0.669 (0.456-0.898) | not run (control-only) | - | yes | GOLD-D2 homophonic fr19 control, c2 alone base level profile=target noise=0 |
| 25 Sept 2026 21:43 | homophonic | N=734 K=102 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0.05 | 1-3 | 0.433 (0.256-0.533) | not run (control-only) | - | no | GOLD-D2 homophonic fr19 control, c2 alone base level profile=target noise=0.05 |
| 25 Sept 2026 21:44 | homophonic | N=1251 K=160 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target,noise=0.05 | 1-3 | 0.421 (0.219-0.693) | not run (control-only) | - | no | GOLD-D2 homophonic fr19 control, K160 profile=target noise=0.05 |

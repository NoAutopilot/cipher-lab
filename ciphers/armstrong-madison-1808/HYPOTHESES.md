# armstrong-madison-1808 -- hypothesis families (append-only below the summary)

LANE ARM, opened 26 Sept 2026 06:49 UTC (owner's decision 06:40). One section per family; CONTROL and TARGET
numbers side by side (CLAUDE.md rule 3). The top block is rewritten only by a cycle consolidator; everything
below "## ARM-CODES corpus" is append-only and is the record the summary is drawn from.

## Summary, cycle 1 (consolidator ARM-CONS1, Fable, 26 Sept 2026 09:44 UTC; replaces the orchestrator's "Ladder" block of 06:49)

**Status: open.** Cycle 1 ran 13 jobs (TOMO-REPLY intake, ARM-CODES, ARM-EN18, ARM-REC, ARM-A2, ARM-REC2, ARM-DESIGN,
ARM-IMG, ARM-TR, ARM-C1, ARM-POOL, ARM-S1; ARM-TR2 still running at 09:44). **No family beat its matched control by
any margin, so no NEAR.md row (rule 5);** two families were negatives with both controls on file (A2) or non-tests
whose control fell below its gate (C); nothing read the target. Every number below is copied from the sections
beneath this block; nothing here is new.

| Family | Jobs | CONTROL | TARGET | Status | Reason |
|---|---|---|---|---|---|
| A1 crib hunt (the ladder's A, re-scoped after QUEUE row 27's "Krajcovic crib from the 15 Feb letter to Jefferson" proved a scout mix-up: no Krajcovic connects to Armstrong; the 15 Feb 1808 Armstrong-to-Jefferson letter exists at loc.gov `mtjbib018243` = Founders 99-01-02-7420 but is wholly in clear, a personal recommendation, not a crib) | ARM-REC, ARM-REC2 | n/a (a search, not a test) | no crib, no decode, no later summary of the letter's content found (Kreider: "no evidence that it ever was decoded"; the LC abstract volume `mss31021a016` skips from 4 May 1805 to 30 Aug 1808) | **park** (as a crib source) | Nothing left to place; the Founders fetch list it left (13 document ids) belongs to E below. |
| A2 direct table transfer | ARM-A2 | A: 200 within-block plaintext permutations per table, target percentile 23.5-70.0; B: 200 shuffled orders of the target under the real table, 40.0-96.0; positive control THE972 round-trip on the 15 Feb letter 241/276 (87.3%) | WE028 covers 328/369 tokens but judge FAIL (-1.082 vs real_p05 -0.800); THE972 tables cover 14-108/369, all FAIL; WE028's 96th percentile is coverage-driven, not language-driven | **park** (negative with both controls) | Every published sibling table is exhausted; only an unpublished one (WE027, Weber 1979 p.154/188) could reopen it, and no copy is reachable (IA print-disabled, no HathiTrust volume). |
| B code design (one-part vs two-part; what the units digits are) | ARM-CODES, ARM-DESIGN, ARM-TR | four sibling tables and four real THE=972 letters (N=28-243, pooled 474) plus 60 simulated 369-token letters per design; ms check ARM-TR: two blind passes, 89.8/87.8/89.0% agreement, first 332 of 369 groups | units top1 0.388 / entropy 2.57 bits (contiguous designs 0.14-0.17 / 3.23-3.27, target p100); decade/units dependence z=2.76 (independent homophones p98-100); digit-order rho refutes insertion and lazy-homophone models (p0-2); Q1 one-/two-part undecidable (0.06 shift vs 0.07-0.09 spread) | **continue as the premise** (verdict stands; precondition 90% checked) | Two-level code: ~99-entry particle list at 1-99, family book above 100 with fixed-meaning unit slots (0 >> 1 > 4,6,7 >> 2,3,5,9). ARM-TR confirmed the digit shape on the manuscript (ms 76/56/14/12/33/10/27/39/39/6 vs Founders 81/63/16/10/35/11/30/41/39/6 over the same 332 groups) with ONE H-grade units disagreement (1843 vs Bourdeau's 1841); the last 37 groups (frame 0033) and the page-1 L6-13 span (54 Founders groups with no clean ms counterpart) are ARM-TR2's, running now. |
| C nomenclator solver (`tools/families/nomenclator.py`) | ARM-C1 | 1 (matched design, held-out Jefferson IX, cold particle block, 3 seeds): blended 0.201 / 0.176 / 0.027, mean **0.135** vs gate 0.6, book class 0.006 / 0.011 / 0.005; 2 (design-mismatched, 15 Feb THE=972 blind): 12/173 = 0.069; 3 (shuffled target, floor): -1467.8, -3.633/token | **not run** (control below gate; the tool refused it) | **park at N=369; pivot to more ciphertext** | Diagnostics: from the TRUE key the objective drifts to 0.856 particles / 0.274 book; with every anchor true the singletons come back at 0.113; the blind sampler's best (-1345) beats the truth-anchored state (-1454). The information is not in 369 tokens with 119 singleton book values (see "C2 rejected" below); more restarts or a stronger annealer cannot supply it. |
| D model-in-the-loop | none | none | none | **not licensed** | Rule 3's gain gate: D runs only after C's control clears and the target reads partially; neither happened. |
| E recovery (key, decode, sibling letter) | ARM-REC, ARM-REC2, ARM-IMG, ARM-POOL | n/a (searches; ARM-POOL's signature screen is a screen at 12-14 groups, not a control) | no key or decode anywhere reached; manuscript found and fetched (NARA M34 roll 14 frames 0030-0033, keyless IIIF v3); roll 14 sampled 1-in-6 (111/664 frames): 2 other coded letters, both THE=972 by signature (coverage 58%/64%, digit-2/3/5/9 share 50%/43% vs the target's ~13%), no pool candidate; Founders editors' notes and 13 located document ids still unread (web.archive.org reset for both workers, founders.archives.gov answers scripts with an empty 202) | **continue** (cheap, and the only route that lowers C's singleton share) | Madison to Jefferson, 15 May 1808: "No such Cypher is in the office, and must be one concerted with another correspondent" -- so a sibling letter, if one exists, is filed with that correspondent (Kreider's candidates: Pinkney, Monroe, Erving, Livingston, the New York circle), not necessarily on roll 14. Roll 14's 1-in-6 stride misses a 3-4-frame letter about a third of the time. ARM-POOL also saw a docket at frame 0645 listing several 1807-1808 dates for a batch of "confidentially sent" Armstrong letters, not followed up. |
| S shorthand passages | ARM-TR (crops), ARM-S1 | Pitman 1837/1890 (different period and script family) as the control system: shape-category score 2.5; Taylor 1786 (Tomokiyo's symbol-by-symbol negative) as a known answer: 7.5 | ten-category shape scores Taylor 7.5, Weston 7.0, Gurney 6.0, Mavor 6.0, Macaulay 5.0, Byrom 4.0 vs control 2.5 | **continue, one step** (family-level result only) | The control can and does score lower (rule 3 met), so the marks belong to the looped-cursive 18th-century family, not a geometric or flat-substitution one. But the known negative tops the table, so shape categories cannot pick a system; the next step is the symbol-by-symbol frequency/positional match Tomokiyo ran on Taylor, run on the other five with Taylor as the known-answer check. |
| Judge (en18) | ARM-EN18, ARM-C1 | leave-one-file-out false-negative 14.2%/15.1% at N=1000/1500, per-fold spread 0.270/0.260 (en: 58.6%/64.8%, spread 0.68-0.71); shuffled-target salad from family C PASSes | (no target decode exists) | **not a gate for family C at this N; a FAIL is of limited reliability** | The spread is above the 0.05 fold gate (Gallatin I and Jefferson IX are outlier folds), and the floor PASS means a PASS on any family-C decode licenses nothing; a judge line is reported beside a shuffled-null floor or not at all. |

**What the lane knows about the code (evidence in the sections named).** (1) It is not THE=972, Armstrong's office code with
Madison, nor any published sibling: Bourdeau's paired check (72% on 15 Feb vs 25%/noise on 20 Feb), Madison's own letter of
15 May 1808, and ARM-A2's four-table sweep with both controls. (2) Its digits are Bourdeau's transcription of Founders, now
90% checked against the manuscript (ARM-TR): one confirmed units-digit difference (1843 for 1841), the same 0/1-heavy,
2/3/5/9-poor shape on both sides. (3) On those digits the design is two-level (ARM-DESIGN): a ~99-entry particle list at
1-99 (132 tokens, 48 distinct, the top five values 17/18/38/1/14 carrying 14% of the letter, the rate of the/of/to/and/in)
and, above 100, a family book of up to 180 decades whose units digits are fixed-meaning member slots, about 900-1800
forms, 168 seen, with a 900-1099 trough that sparse occupancy explains; no usable alphabetical order; the siblings are
block-local alphabetical at best. (4) The graphic marks are not "a symbol here and there": ARM-S1 counted about 105 marks
(pass A, 15 crops) and 116-211 (pass B, 14 crops; its count column sums to 116, its prose says about 211 -- a discrepancy
for the reconciliation to settle) on the 29 cropped lines of pages 1-3, against 312 numeric groups on the same pages; they
sit in unbroken runs of several to 19 glued to line starts and ends, five lines are pure shorthand, and superscript ticks
sit above numerals on two lines. Their shapes number 35-47 (unreconciled across the two passes) with a sharply Zipfian
profile; both passes independently called the population syllable- or word-shorthand-like, and the shape family is
looped cursive (Weston/Gurney/Byrom/Mavor/Macaulay class), not geometric. (5) The AFIO reading is refuted by Bourdeau's
shuffled-ciphertext control (500 random keys fit better) and is not re-run here.

**What it does not know.** Whether the marks are Armstrong's own shorthand for out-of-vocabulary words (ARM-DESIGN's
premise), a published system, or part of the code's own spelling device; which correspondent the cipher was "concerted
with", and whether any second letter in it survives (none on roll 14's sampled frames; the other correspondents' papers
unsearched beyond loc.gov's Monroe collection, 0 hits for Armstrong); whether Founders' own editorial note on 99-01-02-2728
says anything a sweep has not (unread twice for host outage); the last 37 groups and the page-1 L6-13 span of the
manuscript (ARM-TR2); whether one-part or two-part (undecidable at this N, and irrelevant since the siblings are
block-local anyway); and what WE027 looks like.

**Cycle 2 (this consolidator's decision; briefs in `.claude/briefs/runs/2026-09-26-lane-arm-c2-*.md`), ranked by
P(first step moves it) x value / cost (CLAUDE.md Pipeline 3), all Sonnet, all with a control that can differ:**
1. **ARM-S2** (`-c2-s2-shorthand-symbols.md`, cap USD 12, 75 min): reconcile ARM-S1's two shape inventories into one
   list with exemplar crops and a mark-frequency profile, then a symbol-by-symbol match of the top shapes (by mark
   count) against each of Byrom, Gurney, Mavor, Weston and Macaulay, with Taylor as the known-answer negative (the method
   must reproduce Tomokiyo's rejection or it has no resolving power) and Pitman as the control system. P about 0.25 that
   it identifies a system or firmly excludes all six; value high either way (a readable system would give plaintext for
   a fifth or more of the letter plus cribs at every run boundary; an exclusion answers Tomokiyo's open question and
   settles that the marks are private).
2. **ARM-REC3** (`-c2-rec3-founders-correspondents.md`, cap USD 5, 50 min): the 13 located Founders ids and the editors'
   note on 2728 via Wayback if it answers, else one `tools/browser_fetch.js` attempt on founders.archives.gov (stop at
   any challenge); then, independent of either host, the loc.gov route that worked for ARM-REC: every Armstrong item
   1807-1809 in the Jefferson and Madison Papers collections at LOC looked at for numeral code, and the Livingston pair
   search that timed out. P about 0.15 (Kreider's team has read this correspondence for the edition and reports no
   decode; a note naming the correspondent or a coded letter outside RG 59 is the win); value high (a second letter in
   the code is the one thing that unlocks family C).
3. **ARM-POOL2** (`-c2-pool2-docket.md`, cap USD 5, 45 min): the frame-0645 docket's "confidentially sent" 1807-1808
   dates read at native size, each date located on roll 14 (Jan 1808-Sept 1810, chronological) or roll 13 (1807, NAID
   via ARM-IMG's browser step), and each located letter screened with `pool/signature_test.py` on one native line --
   a docket-led targeted fetch (about 40 requests), not the exhaustive pass. P about 0.1, value high, cost low.

**Rejected candidates, with reasons.** (a) exhaustive roll 14 (553 more frames, about 30 Sonnet classification calls on
top of fetching, about USD 20 on ARM-POOL's rate): the editors have read every Armstrong letter in M34 for the Papers of
James Madison and report none in this code, and Madison's own letter puts the sibling with another correspondent, so
P is low for the lane's most expensive job -- the docket-led POOL2 above takes the one concrete lead the survey left;
rolls 13/15 likewise only for a date the docket or REC3 names. (b) **C2, a stronger objective for family C: rejected
on paper.** The binding constraint is the singleton share, not the objective: the target has 20 singleton particle
values and 119 singleton book values (139 of 369 tokens). An oracle that reads every repeated value correctly scores
(132-20)+(237-119) = 230/369 = 0.62, and adding singletons at ARM-C1's all-anchors-true rate (0.113) gives 0.67 -- so
the 0.6 gate sits at the ceiling of any objective that has to infer singletons from context, and the matched control
(135-168 singleton book values, 0.135 blind, about 0.5 with perfect anchoring) cannot clear it by construction. A
word 4-gram term does not change this: en18 is 4.8M letters (under a million words), so 4-grams of a fresh despatch are
overwhelmingly unseen and the term is backoff noise; a larger era corpus does not make the truth a fixed point either
(ARM-C1 needed the control letter itself in training 300x to do that, and the blind sampler still stalled 600 nats
below). A model-in-the-loop proposal step is family D and stays not licensed. What lifts the control is fewer
singletons, i.e. more ciphertext in the same code (E's route). (c) more restarts or seeds on C1: the diagnostics show
the sampler's blind optimum already beats the truth under the objective; restarts converge to salad faster, not to the
key. (d) any judge-gated family-C run: the floor PASSes.

**Untouched by this cycle, deliberately:** `ciphertext.txt` (never edited; ARM-TR2's `ciphertext_ms.txt` is the
manuscript witness beside it), NEAR.md (no row), status (open), QUEUE row 27's broken cheap-test sentence (the parent's,
flagged by TOMO-REPLY).

## ARM-CODES corpus (26 Sept 2026, worker ARM-CODES)

No decoding or family run this pass -- corpus build only, per this job's brief. Full sourcing, licences and
unreachable items in `tools/data/uscodes-1800/README.md`; stats regenerate offline with
`python3 tools/data/uscodes-1800/stats.py`, reading only the TSVs there and this target's own
`ciphertext.txt`. Four value->word tables were built: `WE028.tsv` (1600 entries, Monroe<->Madison, H grade),
`THE972_bourdeau.tsv` (580 entries, Armstrong<->Madison except the target, H/C/M/I grades kept from
Bourdeau), `THE972_tomokiyo_partial.tsv` (227 entries, C/M) and `THE972_tomokiyo_clean.tsv` (95 entries, C)
-- the latter two are two different published renderings of the same underlying reconstruction (from
Armstrong's known-plaintext letter of 4 May 1806), kept separately since neither is a strict cleanup of the
other by inspection. No table exists for WE027 (Livingston<->Madison) or for any other WE-numbered code
Tomokiyo names -- his site publishes worked decoded-letter specimens for those, never a downloadable table
(see the README's "Not reachable" section). Weber 1979 itself is on Internet Archive
(`unitedstatesdipl0000webe`) but print-disabled-tier and unborrowable by this account; no HathiTrust volume
exists for its OCLC number either -- not chased further, per the brief.

**Target stats (`stats.tsv` row `armstrong-madison-1808_target_ALL_369_tokens` / `..._216_distinct`):** 369
tokens, 216 distinct, values 1-1900. Last-digit distribution over all 369 tokens: `0:93 1:66 2:17 3:10 4:41
5:12 6:32 7:46 8:45 9:7`. Hundred-block counts (distinct values): a trough of 3 values in 900-999 and 1 in
1000-1099 (4 total, matching the brief's own count), against 8-16 in every neighbouring block.

**No sibling shows the target's skew, in its table or its real usage.** All four tables' own defined-value
sets run 53-65 entries per last digit (WE028 is exactly flat, 160 per digit, by construction: one contiguous
1-1600 run). THE=972's real *usage* in Armstrong's other four 1808 letters (pooled, 474 tokens, rendered
into `decodes/`) is closer to flat-with-noise than to the target's shape: highest digit is 2 at 70 (15%), not
digit-0 (44, 9%) -- the target's digit-0/digit-1 dominance (25%/18%) is not a generic feature of this code
family's construction or of how Armstrong's own hand actually uses it. Likewise no table or usage instance
shows a comparable 900-1099 trough (all run 25-53 combined in that range, against the target's 4) -- the gap
is target-specific, not inherited from a codebook we already have.

**Construction: blockwise-alphabetical, all four tables, consistent with NOTES.md's qualitative read.**
Spearman rho (value order vs. plaintext alphabetical order) is near zero for every table (-0.09 to -0.25),
not the +1.0 a single alphabetical one-part code would give; alphabetical-run-block counts are 98 (WE028,
~16 entries/block), 99/48/18 for the three THE=972 tables (~5-6 entries/block on the denser ones) -- many
short ascending runs, i.e. a two-part-style code built in alphabetical blocks, the same convention across
Livingston's, Monroe's and Armstrong's own codes.

**Homophones concentrate on short common syllables in THE=972, are near-absent in WE028** (a near-1:1 word
code). Top of `THE972_bourdeau.tsv`: `re`=6, `tion`=4, `be`=4, `ta`/`con`/`pro`/`ne`=3 each -- the shape a
nomenclator solver (family C) will need to model when it gets to the target.

CONTROL: none run this pass (no family, per the brief). These are corpus-comparison numbers, not a
cryptanalytic test with a matched control -- rule 3 does not apply to a corpus-build job.

## Orchestrator structural note (LANE ARM, 26 Sept 2026 07:00 UTC; target only, no control yet -- an observation, not a result)

Values >= 100 (237 tokens, 169 distinct): last digit 0 on 92 tokens, 1 on 47, 4 on 26, 6 on 22, 7 on 22, 8 on 12,
2/3/5/9 on 9/3/2/2. Values < 100 (132 tokens, 48 distinct): last digit roughly flat (7 and 8 commonest: 17, 18,
38, 47, 48). Distinct big values sit in 99 decades, 45 with two or more variants, e.g. 1760/1761/1762/1764/1767,
1470/1471/1472/1476, 1840/1841/1842/1848, 160/161/162/164, 1350/1351/1354. Hypothesis H-DEC for the design
worker: a "decade" code -- root words at multiples of ten, units digit an inflection or derived form (0 root,
1 plural or -ed, ...), with a separate block 1-99 for particles; alternative H-HOM: units digit a homophone
choice with a writer's preference. Needs a sibling of either design as the control before it licenses anything.

## ARM-A2 transfer sweep (26 Sept 2026, worker ARM-A2)

Family A2 (ladder above): direct transfer of every published sibling table in `tools/data/uscodes-1800/*.tsv`
to the target, per-table. Script: `ciphers/armstrong-madison-1808/a2/transfer.py` (offline, seeded, reproduces
these numbers with `python3 ciphers/armstrong-madison-1808/a2/transfer.py`, ~40s). Word-bigram model built
directly from the en18 corpus (judge spec's own `language: en18`; en18 present, not en). CONTROL A: 200 tables
per T made by permuting T's own plaintext column within alphabetical (value-sorted) blocks of 20 -- keeps the
value range and blockwise-alphabetical structure, destroys the value->word pairing, so it CAN score differently
from the real table (rule 3). CONTROL B (reverse): 200 shuffles of the target's own 404-token order, decoded
with the real, unpermuted T -- bigram score depends on order, so this control can differ too.

**Positive control caveat (read before the target numbers): a faithful round-trip can still FAIL the judge's
character-4-gram language check on this code family, so the target FAILs below are not automatically weakened
by this.** THE=972 is a word-AND-SYLLABLE code (NOTES.md); several of its published entries are bare syllable
fragments ("ac", "ce", "mp", "t", "g", "s" ...). Re-encoding Bourdeau's own known-plaintext decode
(`decodes/armstrong_1808-02-15.txt`, the 72%-coherent 15 Feb letter) word-for-word under `THE972_bourdeau.tsv`
and decoding it straight back through the *same* table recovers 241/276 (87.3%) of its extractable word/
syllable tokens exactly (the mechanical proof the encode/decode pipeline is correct) -- but concatenating
syllable fragments without their original within-word joins ("ac ce mp t" for "accompt") reads as salad at the
letter level, so the judge's language check still FAILs (687 letters, length ok, language score below real_p05).
This is an artifact of testing a syllable code's *coverage* against a *letter*-level judge on a token stream
that drops uncovered in-between words, not evidence the transfer pipeline is broken.

| Table (entries loaded) | Positive control: known words covered / round-trip judge | Target coverage: tokens / distinct values | Word-bigram score (pairs) | Percentile vs 200 permuted-table controls | Percentile vs 200 shuffled-order controls | Judge verdict (length, language) |
|---|---|---|---|---|---|---|
| WE028.tsv (1600) | no Monroe-side decode file on disk -- skipped (README.md: none published) | 328/369 tokens (88.9%), 183/216 distinct (84.7%) | -4.433 (266 pairs) | 70.0 | 96.0 | FAIL -- length ok (1873 letters), language FAIL (score -1.082, null_p99 -2.199, real_p05 -0.800) |
| THE972_bourdeau.tsv (580) | 241/276 (87.3%) covered; round-trip judge FAIL (687 letters, length ok, language FAIL) | 108/369 (29.3%), 61/216 (28.2%) | -4.440 (33 pairs) | 23.5 | 40.0 | FAIL -- length FAIL (559<600), language FAIL (score -0.939) |
| THE972_tomokiyo_clean.tsv (94, README says 95 -- one value collision on load, not chased) | 97/276 (35.1%) covered; round-trip judge FAIL (230 letters, length FAIL) | 14/369 (3.8%), 10/216 (4.6%) | n/a -- no two adjacent covered tokens | n/a | n/a | FAIL -- length FAIL (64 letters); language sub-check itself PASSes (score -0.883 > real_p05 -0.899) but is meaningless at N=64 |
| THE972_tomokiyo_partial.tsv (227) | 159/276 (57.6%) covered; round-trip judge FAIL (381 letters, length FAIL) | 50/369 (13.6%), 29/216 (13.4%) | -4.442 (7 pairs) | 58.5 | 65.8 | FAIL -- length FAIL (204<600), language FAIL (score -1.108) |

**Reading the percentiles.** WE028's target decode scores at the 96th percentile against 200 shuffled-orders of
the target's own token stream under WE028 (only 4% of random re-orderings of the same 369 tokens score higher)
and the 70th against 200 within-block-permuted copies of WE028 itself -- the least flat of the four, but neither
is an extreme tail value, both n=200 distributions are well-populated (266 real bigram pairs), and the target
still FAILs the language judge outright (-1.082, below real_p05 -0.800, only above the shuffled-letters floor).
The other three tables' percentiles cluster near the middle of their control distributions (23.5-65.8) and are
built from far fewer adjacent-covered-pair bigrams (7-33) -- at that N a percentile is noisy (rule 3's
few-fold-spread lesson, extended here from fold counts to control-pair counts) and should not be read as a
result either way.

**Verdict: no table transfers.** None of the four published sibling tables reads the 20 Feb 1808 target above
its own judge gate, whether alone (all four FAIL) or relative to either control (no percentile is an extreme
tail value once WE028's own coverage-driven-not-language-driven 96th is set against its still-FAILing absolute
score). This is a negative with both controls on file (rule 3), not a closed target (rule 5): family B
(sibling-code *vocabulary*, ARM-DESIGN/family C) and family E (recovery) remain open in the ladder above.
`cheap_test_done.A2` in `specs/armstrong-madison-1808.json` carries this row's summary numbers.

Salad (first 30 decoded tokens per table, NOT a reading, rule 10):
- WE028: `vail six trust rive * Sunday arc {1752} {1841} bec {1840} six ** sub eligible arc ble {1628} ‐ whole fabruary ble lution ** suf bel has know {1780} fin`
- THE972_bourdeau: `{453} roc de ion * {35} {681} {1752} {1841} {1314} {1840} roc ** ward {18} {681} native {1628} {1267} pos {76} native {98} ** {388} like ct Monarch {1780} temp`
- THE972_tomokiyo_clean: `{453} {240} {760} {1480} * {35} {681} {1752} {1841} {1314} {1840} {240} ** {384} {18} {681} {1340} {1628} {1267} {1180} {76} {1340} {98} ** {388} {1320} {1254} {64} {1780} {341}`
- THE972_tomokiyo_partial: `{453} {240} {760} ion * {35} {681} {1752} {1841} {1314} {1840} {240} ** w...? {18} {681} {1340} {1628} {1267} pos {76} {1340} {98} ** {388} l...?? ct {64} {1780} temp`

## ARM-DESIGN (26 Sept 2026, LANE ARM worker ARM-DESIGN, Fable) -- family B: what kind of code is the letter in?

Scripts, tables and simulations: `design/` (`design_stats.py`, offline, stdlib; `stats_real.tsv` target and the four
real THE=972 letters; `stats_sim.tsv` 60 simulated 369-token letters per design with the target's percentile;
`table_layout.txt` the two sibling tables' alphabetical layout; `run_log.txt`). Simulated letters are en18 text
encoded under: `blockwise_WE028` (WE028 as published), `onepart` (WE028's 1596-entry vocabulary in one alphabetical
run), `twopart` (same vocabulary, values permuted), `the972_partial` (Bourdeau's 580 entries, syllable spelling),
`seq_pblock` (99-word particle block at 1-99 + 1800 content forms numbered 100-1899 at random, OOV dropped), `hdec`
(180 root lemmas at 100,110..1890, units digit = a fixed inflection slot, en18 inflection rates, OOV dropped as if
written in the shorthand), `hhom_lazy`/`hhom_flat` (same decades, units digit = a homophone chosen with weight
1/(d+1) / uniformly), `hinsert` (gapped numbering: roots at decades, 450 later additions filling units 1,2,3.. in
order). CONTROL = the sibling tables' known layout, the four real THE=972 letters (N=28-243, pooled 474) and the
simulations; TARGET = the 369 groups. Every statistic below can differ between the designs it is used to compare
(rule 3); where it cannot, that is said.

**Sibling layout (control side, needs plaintext).** WE028: 1596 entries, 94 maximal alphabetical runs, 27 runs of
20-100 entries covering 1392 entries -- one letter-block per run (B at 1301-1360, T at 1361-1400, I/J at 1401-1446,
R 1461-1500, A 1501-1550, O 1551-1600 ...), block order scrambled, alphabetical inside: a two-part-by-letter-block
code, not one-part. THE972 (580 of ~1600 published): 99 runs, median 3, only 4 runs >=20 (101 entries) -- more
fragmented than WE028 even allowing for the 36% density (ga..how at 901-932 interrupted by particular 910, o 934,
sue 939). The office convention is therefore block-local alphabetical order at best; no sibling is one-part.

**Q1 one-part vs two-part vs blockwise, plaintext-free: NOT DECIDABLE at N=369.** Three statistics tried.
`onepart_dist` (mean distance between the k-th most frequent token's position in the value range and the
alphabetical position of the k-th most frequent en18 word, k<=8): onepart sims 0.31+-0.07, twopart 0.37+-0.09,
blockwise 0.38+-0.06 -- a 0.06 shift against a 0.07-0.09 spread, so the designs overlap at this N; target 0.417 (p93
under onepart, p70 under twopart, p73 under blockwise), leaning away from one-part but weakly, and the target's top-8
tokens all lie in the 1-99 block, which behaves as a separate list (below), so the test barely applies to it.
`freqpos_jsd` (token-weighted vs distinct-weighted 19-bin value histogram): 0.019-0.022 for all three designs, no
separation; target 0.020. Successive-gap statistics: identical under all designs and equal to their own
shuffled-order value (0.02-0.03), order carries nothing. Verdict: the alphabetical-order question cannot be settled
from the ciphertext alone at this length -- a negative for the statistics, not for a design -- and the siblings say
the convention is block-local anyway. Family C gets NO alphabetical constraint.

**Q2 units-digit skew (values >= 100, 237 tokens): NOT a contiguously numbered code; slots with fixed meanings.**
Concentration: target `units_top1` 0.388 (digit 0), `units_top2` 0.586, entropy 2.57 bits. Every contiguous design
(blockwise/onepart/twopart/the972/seq_pblock, 60 sims each) sits at top1 0.14-0.17 +-0.02, entropy 3.23-3.27 +-0.03
(target percentile 100 / 0 on all five); the four real THE=972 letters: top1 0.16-0.20, entropy 3.11-3.26; pooled
0.151 / 3.27. `hdec` with en18 inflection rates over-concentrates (top1 0.76+-0.05, entropy 1.17, target p0);
`hhom_lazy` 0.34+-0.06 / 2.73+-0.17 (target p78 / p18) and `hinsert` 0.40+-0.05 / 2.35+-0.14 (p43 / p90) both match
the concentration -- but the lazy weight and the insertion model are chosen parameters, so this is consistency, not
support. Digit ORDER separates them: the target uses digits 1,4,6,7 (47,26,22,22 tokens) far more than 2,3,5,9
(9,3,2,2), the same digits in every hundred-block (`digits23_share` 0.083); `hinsert` (fill 1,2,3.. in order) gives
`digit_order_rho` 0.95+-0.04 and digits23 0.40+-0.07 (target p0 on both), `hhom_lazy` 0.75+-0.16 / 0.29+-0.07 (p2 /
p0): both refuted -- the units digit is a slot with a fixed meaning across the whole book and arbitrary popularity,
not a preference order or an insertion order (hdec's own rho is an artefact of my slot assignment and is not
evidence either way). Decade/units dependence (`decade_units_z`: modal-digit share in decades with >=3 tokens vs its
own digit-permutation null; target 0.570 vs null 0.501, z=2.76): `hhom_lazy` 0.02+-0.92 and `hhom_flat` -0.10+-0.93
(target p98 / p100) -- a homophone chosen independently of the word cannot produce the target's dependence, so pure
lazy homophony is out; the fair contiguous control `seq_pblock` (particles separate) 5.9+-2.6 (p13), `hinsert`
3.2+-1.7 (p45), `hdec` 1.3+-1.1 (p92); the function-word-carrying word codes give 14-20 because 'the' repeats inside
one decade, a mismatch of design, not evidence. Verdict: H-DEC-like -- decade = a family of related entries, units
digit = which member (0 the commonest, 1 the next, 4/6/7 middling, 2/3/5/9 rarely filled) -- but the members of a
decade are used more evenly than one root plus en18 inflections would give (170: 0x5 6x4; 1260: 7x4 4x1; 380 holds
five distinct digits), so each slot is best modelled as its own entry with a book-wide slot prior, not a
deterministic inflection. The 900-1099 trough (4 tokens; `block_pair_min` 18-25 under contiguous designs, p0-1;
6-8 under the sparse designs, p2-14) is what a sparsely occupied numbering produces, not an extra anomaly.
CAVEAT that outranks all of this: every digit here is Bourdeau's transcription of the Founders group list, never
checked against NARA M34 roll 14 images 29-32 (NOTES.md open item 4); a systematic misreading of Armstrong's
2/3/5/9 would turn this whole section back into a contiguous code. That image check is now the single most
valuable access step on this target.

**Q3 codebook size and the 1-99 block.** 1-99: 132 tokens, 48 distinct, 20 singletons; a Zipf(s=1) fit gives
K~100 (E[D]=48.4 at K=100) -- a ~99-entry list; its top five values (17, 18, 38, 1, 14: 13, 12, 10, 9, 8 tokens)
carry 14% of the whole letter, the rate of the/of/to/and/in in en18 despatches, and its digits are flat (7 and 8
commonest) -- a particle block, distinct in kind from the block above 100. Above 100: 237 tokens, 168 distinct, 119
singletons; en18 content-word streams of 237 tokens give 196 distinct (p05 170, p95 214), so the block reads as
content words with near-complete coverage of the letter's vocabulary, not syllable spelling (a Zipf fit over a
whole-language vocabulary cannot even reach D=168 at K=5000). Coverage of en18 content tokens by the top-K
entries: K=180 lemmas 0.29, 500 0.52, 1000 0.68, 1800 0.80 (forms 0.25/0.44/0.59/0.71). With 237 coded content
tokens and 35 short + 2 full-line shorthand passages as the only visible out-of-vocabulary route, coverage is
about 80-87%: a general 180-root x few-slot book (about 470 forms, coverage ~0.45, ~300 OOV words per letter) is
excluded; the book above 100 holds on the order of 900-1800 forms in <=180 decades x <=10 slots (99 decades, 168
forms seen in this one letter), which is either a purpose-built topical vocabulary or a full-size book whose slots
2/3/5/9 are mostly empty. Sibling low blocks for comparison: WE028's 1-99 is a proper-name/long-word block
(Maryland, West Indies, Parliament ...) and THE972's 1-99 holds 14 known entries (circumstance, commerce,
communica ...) -- neither is a particle block, so this too is target-specific.

**Verdict for family C.** Two-level numeric code: a ~99-entry particle list at 1-99 and, above 100, a family
book of up to 180 decades whose units digits are fixed-meaning member slots (0 >> 1 > 4,6,7 >> 2,3,5,9), about
900-1800 forms, English content words, no usable alphabetical order, OOV words probably in the shorthand.
Spec: `design/family_C_spec.md`. K: low ~100; high 900-1800 forms (168 seen). Not decoded to words here.

Orchestrator caveat on ARM-A2 (LANE ARM, 26 Sept 2026 08:12, answering V9-QA8's flag): the en18 judge FAILs quoted
in ARM-A2 carry ARM-EN18's reliability caveat -- leave-one-file-out false-negative 14-15 percent with a per-fold
spread of 0.26-0.27, above the 0.05 gate, so a judge FAIL on this target is of limited reliability by itself. The
A2 negative rests on the permuted-table and shuffled-order percentiles (WE028 70.0 / 96.0, THE972_bourdeau 23.5 /
40.0), not on the judge line alone; WE028's 96th percentile against shuffled order is the one number to re-check if
family C ever proposes WE028-like vocabulary.

## ARM-TR manuscript check (26 Sept 2026, LANE ARM worker ARM-TR): independent transcription vs Bourdeau, PARTIAL

Two blind passes per manuscript page (never seeing `ciphertext.txt` or each other), read from
`tools/iiif_lines.py` line crops of NARA M34 roll 14 frames fetched by ARM-IMG, reconciled with
`tools/reconcile_passes.py`, disagreements settled by this worker looking at the crop directly.
Full detail, layout correction and per-page numbers in `images/layout.md` and `NOTES.md`'s "ARM-TR"
section. Script and raw diff: `tr/diff_ms_vs_ciphertext.py`, `tr/diff_output.txt`.

**Coverage is partial, and this is the headline finding.** Frame 0030 = manuscript page 1; frames
0031 and 0032 are two independent photographic scans of the SAME two-page spread (pages 2-3),
verified by direct content/ink-stroke comparison -- corrects the job brief's assumption that 0030
and 0031 were the duplicate pair. 0029 is a different, unrelated document. This worker's own
`ciphertext_ms.txt` (numeric groups only, marks excluded) covers 312 tokens that align against only
the **first 332 of ciphertext.txt's 369 numeric groups** -- the remaining 37 groups (the letter's own
final ~10%) have no counterpart in the fetched frames at all (the alignment simply runs out, it does
not degrade first). Frames 29-32 do not contain the whole letter; frame 0033 (already flagged
"not_fetched" in ARM-IMG's own `images/manifest.json`) or a further frame is needed to check the
letter's last ~37 groups against the manuscript. **Nothing below is a claim about that uncovered
tail.**

**Pass agreement per page** (17/16/15 manuscript lines; page counts differ from ciphertext.txt's own
33 printed/wrapped lines because the manuscript's physical lines are narrower):
- Page 1 (frame 0030, both blind passes reading the SAME crops -- a transcription-reliability check,
  not a two-scan check, since this page has no second scan on file): 89.8% (17 lines, `tr/page1_reconcile/`).
- Page 2 (frames 0031L vs 0032L, genuine two-scan witnesses): 87.8% after correcting a one-line
  index offset this worker's own crop parameters introduced (`tr/page2_passA_shift.tsv`; page2's
  region for pass A's source crop included one extra faint top line pass B's crop did not).
- Page 3 (frames 0031R vs 0032R): 89.0%, no offset needed.

**Genuine settled digit disagreements (both blind passes independently transcribed the SAME position
differently, or one pass missed content the crop plainly shows), resolved by this worker looking at
the crop directly, all confirmed at the pixel level, not by consulting `ciphertext.txt`:**
- Page 1, manuscript line 2: **"Sir"** (the salutation, plain cursive word) -- pass B misread it as a
  shorthand mark. Bourdeau's `ciphertext.txt` does not carry a salutation line at all (it starts
  straight into the numeric groups after "The"), so this token has no counterpart to diff against;
  noted for completeness of the manuscript's own structure.
- Page 1, manuscript line 6: **"98" + 8 shorthand marks** -- pass B dropped "98" entirely and
  undercounted the marks at 6; a zoomed re-crop confirms 8 distinct strokes and the leading "98".
- Page 2, line (shifted) 13: **"1640"**, not "1620" as pass A read (a 4 misread as a 2).
- Page 2, line (shifted) 11: **"19"**, confirming pass B over pass A's uncertain leading digit.
- Page 3, line 1: **"760"** -- pass A read the opening group as an illegible blob; both scans show it
  plainly.
- Page 3, line 11: **"1461 740 ..."**, not pass A's "1461 74?" nor pass B's bare "740 ..." -- pass B's
  crop for this line was cropped with a slightly lower top margin than pass A's and clipped off the
  genuine leading "1461" (not bleed-through); the following group reads "740", not "74".
- Page 3, line 15 (the letter's last transcribed line before the coverage gap): **"...310 1900"** --
  pass A's crop cut off the final group; confirmed by this worker's own earlier full-page look too.

**The one clean units-digit finding, matching this brief's stated priority:** page 1, manuscript line
4, 10th group -- **both blind passes independently read "1843"**, H-graded, no disagreement between
them at all -- against Bourdeau's `ciphertext.txt` value **"1841"** at the same sequence position
(ciphertext.txt token #10). This is the ONLY substitution in the whole diff where both this worker's
passes agree with each other AND the corresponding ciphertext.txt token is unambiguous prose-numeral
(not inside the heavily-disputed shorthand region below). Grade: H (both passes agree, this worker's
own direct crop look at 08:38 UTC also read "1843" before either subagent ran -- see NOTES.md). This
does not by itself resolve ARM-DESIGN's Q2 caveat (a systematic 2/3/5/9 misreading would need to
recur across many tokens, not one), but it is one concrete, confirmed case of Bourdeau's transcription
differing from the manuscript on a units digit, in the direction ARM-DESIGN's own caveat worried about
(1 read where Bourdeau has a rarer digit; here 3<->1, not the 2/3/5/9 axis ARM-DESIGN singled out).

**A second, larger-scale finding that undercuts confidence in the whole covered comparison, not just
one digit:** a large block of ciphertext.txt tokens in the range corresponding to page 1's
manuscript lines 6-13 (the same lines both blind passes independently flagged as dense, hard-to-
segment shorthand-and-digit mixtures, `tr/page1_passA.tsv`/`page1_passB.tsv`'s own low-confidence
notes) does not align cleanly against this worker's ms reading at all -- roughly 40 of the 54
"in ciphertext.txt, not in ms" tokens and most of the 14 substitutions fall in this one span
(`tr/diff_output.txt`). This reads as EITHER this worker's passes under-transcribing real numeric
content as shorthand marks in a visually ambiguous run, OR Bourdeau's own transcription resolving
marks the manuscript itself does not clearly support as digits, OR (most likely, given both blind
passes independently flagged the SAME lines as their hardest) this whole span being genuinely
difficult to transcribe from the image at normal resolution and needing a dedicated higher-resolution
look before any per-token claim is made about it. **Not resolved here** -- flagged as the single most
valuable next step on this target's manuscript-verification thread, ahead of chasing frame 0033.

**Units-digit distribution, ms (H+M) vs ciphertext.txt, over the SAME covered range (ciphertext.txt's
first 332 of 369 groups), all values:**

| digit | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| ms (312 tokens) | 76 | 56 | 14 | 12 | 33 | 10 | 27 | 39 | 39 | 6 |
| ciphertext.txt (same 332-token span) | 81 | 63 | 16 | 10 | 35 | 11 | 30 | 41 | 39 | 6 |

Both distributions agree closely in rank order and shape (0 and 1 dominant, 2/3/5/9 rare, matching
ARM-DESIGN's Q2 finding) -- the alignment gap above thins both counts roughly proportionally rather
than concentrating on any one digit, so this comparison does **not** show a systematic 2/3/5/9
misreading of the kind that would collapse ARM-DESIGN's contiguous-code verdict; the caveat there is
not resolved, only not actively contradicted by what was checked here, and the still-uncovered final
37 groups and the unresolved shorthand-heavy span above are both real gaps in that reassurance.

**Shorthand passages**: 29 shorthand-bearing manuscript lines cropped to `images/shorthand/` (not
read, per this brief), indexed by page/line and this worker's own running sequence position in
`images/shorthand/index.tsv`, for a later family S job. This worker's finer per-mark counting
convention is NOT directly comparable to Bourdeau's passage-level `*`/`**` marking in
`ciphertext.txt` (see `ciphertext_ms.txt`'s own header) -- a family S job should re-derive mark
counts from these crops rather than trusting either transcription's count.

## ARM-C1 nomenclator (26 Sept 2026, LANE ARM worker ARM-C1, Fable) -- family C: control below gate, target not run

Family C of the ladder, built as `tools/families/nomenclator.py` (registered in `tools/family_run.py`, offline test
`tools/tests/test_nomenclator.py`) from `design/family_C_spec.md`: particle block 1-99 + family book >= 100 (decade =
family, units digit = member slot, book-wide slot order read from the ciphertext's own units-digit token counts),
word-trigram LM (interpolated absolute discounting, D=0.75) over en18 with ONE FILE HELD OUT, sibling-vocabulary
prior (WE028 + THE972 tables + Bourdeau's THE=972 decodes + top-2500 en18 content forms; a word outside it costs 3
nats, never a ban), soft same-decade stem tie (0.5) and slot-order term (0.3), duplicate-word penalty (2.0); Gibbs
anneal T 1.5 -> 0.25, two phases (repeated values alone with singletons held as an unknown word, then all values),
3 restarts. `*`/`**`/`<..>` tokens are OOV wildcards scored as an unknown word. Runs: `tools/family_run.py
specs/armstrong-madison-1808.json --family nomenclator --cipher ciphers/armstrong-madison-1808/ciphertext.txt
--tokens space ... --param sweeps=30 --param phase1=20` (the spec's `ciphertext` field is a path, hence `--cipher`);
logs in `families/control1_battery.log` (+ `control1_battery_prefix.log`), `families/control2_feb15-1.txt`,
`families/control3_floor.log`; controls 2 and 3 ran before the determinism fix and are reproducible only up to the
per-process candidate order they had.

**CONTROL 1 (spec control 1, matched design, rule 3), `--control-only --seeds 3 --restarts 3 --gate 0.6`, 08:53-09:02
UTC (a rerun after a determinism fix -- candidate lists were iterated in set order, which varies per process; the
pre-fix run of 08:33-08:41 read 0.198 / 0.179 / 0.046, mean 0.141, `families/control1_battery_prefix.log`, and
the tool's row for it stands below).** Letter cut from the held-out Jefferson Vol IX (`holdout=5`, removed from the LM's training texts), 369 coded
tokens, particle block = 30 commonest training words + 26 letters + words from rank 200 at a random permutation of
1-99 (cold: the solver never sees the key), book = 180 decades x 10 slots = 1800 forms built from the held-out
volume's own register outside the letter's window (stem families in decades, commonest member at slot 0, then 1,
4, 6, 7, 8, 2, 3, 5, 9; empty slots filled by the next commonest forms), OOV words kept in place as `*` marks.

| seed | control shape (coded / distinct: particle+book / particle tokens / book tokens / OOV words -> `*` tokens) | particles | book | blended | solver score |
|---|---|---|---|---|---|
| target (for comparison) | 369 / 216: 48+168 / 132 / 237 / ? -> 35 marks (24 `**`, 10 `*`, 1 `<..>`) | - | - | - | - |
| 1 | 369 / 177: 42+135 / 201 / 168 / 63 -> 54 | 73/201 (0.363) | 1/168 (0.006) | 74/369 (0.201) | -1344.9 |
| 2 | 369 / 184: 39+145 / 180 / 189 / 64 -> 56 | 63/180 (0.350) | 2/189 (0.011) | 65/369 (0.176) | -1391.6 |
| 3 | 369 / 187: 40+147 / 186 / 183 / 59 -> 51 | 9/186 (0.048) | 1/183 (0.005) | 10/369 (0.027) | -1459.4 |
| **mean** | | 0.254 | 0.007 | **0.135 (0.027-0.201); gate 0.6 NOT met** | |

The control is anchor-richer than the target (180-201 particle tokens against the target's 132; 135-147 distinct
book values against 168), so it is the *easier* side of the design, and it still reads under a quarter blended.
The blended figure is dominated by the particle class (rule 3's unbalanced-class paragraph): the book class, which
carries the letter's content, reads 0-2 percent on every seed.

**Why (diagnostics on the seed-1 control letter, blind LM, `_init` hook of the solver):** greedy sweeps started
from the TRUE key drift to particles 172/201 (0.856), book 46/168 (0.274), blended 0.591 -- the truth is not a fixed
point of the objective at this N. With every anchor given (all particles and all repeated values true, singletons
randomised) greedy recovers 19/168 book values (0.113); with true particles only, 5/168 (0.030). The sampler's own
blind best (-1345 to -1350) scores ABOVE the truth-anchored states (-1454 to -1462): the trigram LM prefers function-word
salad over the true letter at 369 tokens with 135-168 singleton book values, so more restarts cannot close the
gap. A deliberately non-blind check (the control letter appended 300x to the training text, machinery only) makes
the truth a fixed point (0.99 / 0.80) yet the blind-start sampler still stalls 600 nats below it (-1483 vs -860):
search and information are both short at this length. The realistic blind ceiling of this design at N=369 is about
0.5 blended even with perfect anchoring, under the 0.6 gate by construction -- the spec's own expectation ("well
under ceiling ... if the control lands under the gate, family C on the target is a non-test").

**CONTROL 2 (spec control 2, design-mismatched, label as such): Armstrong's 15 Feb 1808 letter (Founders
99-01-02-2703, THE=972), 243 groups, 135 distinct, run blind WITHOUT the THE=972 key by the same solver and
prior** (`families/control2_feb15.py --sweeps 40 --restarts 3 --seed 1`, group list from
`tools/data/uscodes-1800/stats.py`, truth = the 173 H/C-graded entries of `THE972_bourdeau.tsv`): recovery 12/173
(0.069) over all known groups, 12/87 (0.138) over known groups whose entry is a whole word of >= 3 letters in the
LM vocabulary; score -801.6 (-3.299/token). THE=972 is contiguously numbered, spells with syllables and keeps its
particles in the main list, so this shows only that the solver does not read Armstrong's idiolect blind at N=243
either; it licenses nothing about the target.

**CONTROL 3 (spec control 3, false-positive floor): `--shuffle-target 1 --gate 0 --seeds 1`, the target's 404 tokens
permuted, N/K/line lengths kept, the family's gate disabled for this floor run only (the tool would otherwise never
reach it once control 1 fails).** Solver score on the shuffled target -1467.8 (-3.633 per token; the control-1 letters scored -3.19 to -3.46 per
token at N=421-425); decode `families/nomenclator-1-shuffle1-sweeps=30,phase1=20-armc1control3shu.txt`, salad by
construction. **The en18 judge PASSes this salad** (row below: "PASS ... a PASS is a gate for a verifier, not a
reading"): the solver emits fluent function-word sequences whatever its input, so a judge PASS on any family-C
decode of this target is a false positive at the floor and licenses nothing -- the judge is not a gate for this
family at this N (rule 3, the shuffled-null floor must fail for a PASS to mean anything). This is the number a real
target run would have to beat; no target run exists to compare it with (below).

**TARGET: not run -- CONTROL BELOW GATE (0.135 < 0.6; 0.141 on the pre-fix run).** No decode, no judge line. Rule 5: a control that cannot read
its own design is a non-test, not a negative on the target; the target stays `open` and family C stays in the ladder
with the named next step from the spec: MORE CIPHERTEXT in the same code (a second Armstrong letter in this code,
ARM-REC's route), not more restarts or a stronger annealer -- the diagnostics above show the information is not in
369 tokens with 168 singleton values. Secondary: the spec's own precondition, the NARA M34 roll 14 units-digit
check against Bourdeau's transcription, which decides whether the family book collapses to a contiguous code -- ARM-TR
(same window, section above, seen by ARM-C1 only at merge time) covers the first 332 groups with one confirmed
units-digit disagreement (1843 vs 1841) and a matching 0/1-heavy shape, so the design premise stands for now but
the last 37 groups are unchecked (frame 0033 not fetched).

Deviations from `design/family_C_spec.md`, with reasons: (1) slot prior taken as fixed from the ciphertext's own
units-digit token counts (a ciphertext observable, same rule on control and target) rather than re-estimated each
sweep; (2) control OOV words kept in place as `*` wildcard tokens (runs collapsed to one mark) instead of dropped
silently -- the target shows its marks, and the realized 60-64 OOV words / 52-56 marks against the spec's "about 37"
and the target's 35 marks reflect that a `**` mark stands for several words, a count the ciphertext does not give;
(3) the control's particle block is the 30 commonest words + letters + words from rank 200, not the 99 commonest,
which would cover about 60 percent of tokens against the target block's 36 percent -- the block is still
anchor-richer than the target's; (4) the book is built from the held-out volume's own register (spec: "the letter's
own register") with a crude suffix-stripping stem for the families, the same stem function the solver's tie term
rewards (a mild coupling that favours the control, and it still fails); (5) the lemma-plus-inflections prior is
approximated by the top-2500 content forms (no lemmatizer offline); (6) interpolated absolute discounting in place
of Kneser-Ney; (7) control 3 needed `--gate 0` to run at all after control 1 failed. Judge caveat carried from
ARM-EN18: a judge line on en18 has a 14-15 percent false-negative rate with a 0.26-0.27 per-fold spread; no judge
line was produced here because no target decode exists.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 26 Sept 2026 08:41 | nomenclator | N=404 K=219 restarts=3 corpus=writingsjamesmo02unkngoog.txt.gz+writingsjamesmo11monrgoog.txt.gz+writingsalbertg01gallgoog.txt.gz+writingsofjamesm0007unse_s2a1.txt.gz+writingsofjamesm0008unse.txt.gz+writingsofthomas09jeffiala.txt.gz sweeps=30,phase1=20 | 1-3 | 0.141 (0.046-0.198) | not run (control-only) | - | no | ARM-C1 control 1 (held-out Jefferson IX, cold particle block) |
| 26 Sept 2026 08:48 | nomenclator | N=404 K=219 restarts=3 corpus=writingsjamesmo02unkngoog.txt.gz+writingsjamesmo11monrgoog.txt.gz+writingsalbertg01gallgoog.txt.gz+writingsofjamesm0007unse_s2a1.txt.gz+writingsofjamesm0008unse.txt.gz+writingsofthomas09jeffiala.txt.gz sweeps=30,phase1=20,shuffle_target=1 | 1 | 0.198 (0.198-0.198) | -1467.777 | PASS - armstrong-madison-1808 (a PASS is a gate for a verifier, not a reading; rule 10) | yes (gate 0.0) | ARM-C1 control 3 shuffled-target floor; gate disabled for this floor run only, NOT a target run |
| 26 Sept 2026 09:02 | nomenclator | N=404 K=219 restarts=3 corpus=writingsjamesmo02unkngoog.txt.gz+writingsjamesmo11monrgoog.txt.gz+writingsalbertg01gallgoog.txt.gz+writingsofjamesm0007unse_s2a1.txt.gz+writingsofjamesm0008unse.txt.gz+writingsofthomas09jeffiala.txt.gz sweeps=30,phase1=20 | 1-3 | 0.135 (0.027-0.201) | not run (control-only) | - | no | ARM-C1 control 1 rerun after determinism fix (held-out Jefferson IX, cold particle block) |

## ARM-S1 marks (26 Sept 2026, LANE ARM worker ARM-S1): shorthand mark inventory + period-system shape comparison

**Not a decode; shapes only, per the brief.** Two Sonnet subagents each read one batch of ARM-TR's line crops
(`images/shorthand/*.jpg`, 15 + 14 crops, split by file-sequence order rather than exactly by page since a per-page
split would have put 19 crops in one call against the brief's 15-crop cap) and independently catalogued every
distinct graphic-mark shape they saw, its count, and its position. Merged, unreconciled (each subagent's own
shape IDs kept, prefixed `A`/`B` for the two passes) into `images/shorthand/INVENTORY.tsv`, 27 + 20 = 47 raw shape
rows. The two passes were not shown each other's catalog, so the same real shape sometimes got two different
descriptions/IDs in the two batches (e.g. pass A's S5/S16/S18 "short/elongated/long wave" and pass B's Sh.1 "low
horizontal wave" are almost certainly the same underlying stroke) -- true pixel-level reconciliation was out of
this job's time box; the numbers below are reported per-pass and then combined into ten hand-merged descriptive
categories (C1-C10, covering the shapes that recur >=2 times in either pass; one-off "hapax" shapes, mostly
compound flourishes seen exactly once such as an ampersand-loop or a double vertical bar "II", are listed in
INVENTORY.tsv but excluded from the comparison since a single occurrence cannot be judged as a recurring
character).

**Inventory size and profile.** Combining both passes: roughly 35-47 distinct shapes depending on how generously
near-duplicate wave/hook variants are merged, but the *frequency* distribution is sharply Zipfian in both passes
independently -- pass A: three shapes (S4 "3-loop", S6 "backward-5/s hook", S12 "left-hook/2-shape") at 12 each,
plus S14 "dot" at 10, dominate; pass B: one shape (Sh.1 "low wave") alone accounts for 52 of ~211 marks in that
batch (roughly 45%), with Sh.2 "3-loop" (17) and Sh.3 "tall back-hook" (12) next, then a long tail of 15 shapes
seen 1-5 times each. Both subagents, independently and unprompted to agree, characterised this as "much more like
a syllable/word shorthand system than an arbitrary flat symbol-substitution alphabet" (pass A) and "looks more
like a syllable- or word-based shorthand system than an arbitrary flat letter/digit substitution" (pass B) --
convergent, not cross-checked.

**Placement.** Both passes agree, independently: marks overwhelmingly occur in unbroken RUNS of several to ~19
marks glued together (no periods or gaps inside a run), anchored at the start or end of a numeral-bearing line;
true single marks flanked by numerals on both sides (the shape the Founders `**` notation implies) were seen only
once or twice per batch, contra the general impression a bare `*`/`**` count gives. Several lines are pure
shorthand with no numerals at all (page1 L12/L13, page2 L03/L11 in part, page3 L13), matching ARM-TR's finding of
"two full lines" of pure shorthand. Pass B additionally found tiny superscript ticks sitting directly ABOVE a
numeral (not beside it) on two numeral-heavy lines (page2 L10, L13) -- a third placement mode neither the brief
nor pass A anticipated.

**Data-quality flag (pass A, not corrected here, out of this job's scope):** two crops, `page2_L02_seq198-212_15marks.jpg`
and `page2_L06_seq250-264_12marks.jpg`, show almost none of the marks their filenames' `_Nmarks` count claims (pass
A counted ~1 visible mark in each against 15 and 12 claimed). This is either a crop-region misalignment from
ARM-TR's line-detection pass or a filename/count bookkeeping slip in that pass's `index.tsv` -- flagged for a
successor, not fixed here (would need re-cropping from the source frame, outside this job's file list).

**Specimens fetched.** `images/shorthand/specimens/` + `manifest.tsv`: all 6 systems Tomokiyo names (Taylor 1786,
Byrom 1796 abridgement, Gurney 1752, Mavor 1792, Weston 1727, Macaulay 1747) plus Pitman 1837/1890 Phonography as
the control (a different period -- Victorian, not 18th c. -- and a different script family -- geometric
straight-line/simple-arc, not cursive loop-and-hook). Taylor's specimen is Tomokiyo's own crop (already the
known-negative comparison); the other four period systems and the control are full alphabet/consonant plates
fetched directly from Internet Archive full-view scans (archive.org's `fulltext/inside.php` search-inside endpoint,
not previously documented in this repo's Access playbook table, was used to jump straight to each book's alphabet
plate by searching for "alphabet"/"consonants" and reading the returned leaf number, rather than paging through
each book by trial and error -- worth adding to CLAUDE.md's IA routes if a future worker needs this again).
Gurney's own alphabet plate was not isolated in time (per the book's preface, all 11 plates are bound before the
title page as a set of un-paginated engravings; the fulltext search only locates *discussion* of a plate, not the
plate leaf itself, when the plate carries no OCR-able caption) -- a specimen page showing shorthand word-forms
embedded in running cursive text (page 6) was used instead, which is visually representative of the system's mark
shapes even though it is not a clean per-letter chart.

**Comparison, with a control that can differ (rule 3).** `images/shorthand/specimens/comparison.tsv`: ten
hand-merged shape categories (C1 wave/hump, C2 3-loop-with-tail, C3 back-curving hook, C4 left-opening hook, C5
isolated dot, C6 diagonal slash, C7 zigzag, C8 short bar/dash, C9 percent-like compound, C10 descender hook),
scored by eye against each system's fetched plate/specimen as yes(1)/partial(0.5)/no(0) -- this is a qualitative
"does a plausibly similar stroke-shape appear in this system's character set" judgment, not a symbol-by-symbol or
pixel match, and is graded accordingly (a cryptanalytic S/M-grade impression, not H/C). Scores: **Taylor 7.5,
Gurney 6.0, Weston 7.0, Mavor 6.0** (the four 18th-c. systems with the richest, loopiest character sets) >
**Byrom 4.0, Macaulay 5.0** (the two systems built mostly from single straight/simple strokes rather than
tailed loops) > **Pitman CONTROL 2.5** (geometric family: only the slash and short-bar categories, plus a
generous partial credit on two categories, find any counterpart at all; no wave, no tailed loop, no dot in this
specific consonant-only plate, no percent-compound). The control genuinely can and does score lower here (rule 3's
"a control must be able to fail differently" bar is met), so the gradient is a real, if soft, signal that the
target's marks as a population belong to the broad looped-cursive-shorthand family rather than to a
geometric/linear one.

**But this does not license picking a system.** The known negative, Taylor, scores at the TOP of the table (7.5,
tied for highest with Gurney/Weston close behind), not distinguishably below the four untested candidates --
Tomokiyo already ruled Taylor out by an actual symbol-by-symbol comparison (his article: "the symbols seem to be
different from those used by Armstrong"), yet a coarse shape-category check like this one cannot reproduce that
negative, because generic loops/hooks/waves recur across nearly every 18th-century longhand-derived shorthand
alphabet almost by construction (they are all built from the same small vocabulary of pen-strokes a period writer
already knew). The honest reading: this comparison shows the target's marks are the right STYLE of thing (a loopy
cursive personal shorthand, not a geometric one, not a flat arbitrary substitution code) but is too coarse an
instrument to identify WHICH of Byrom/Gurney/Mavor/Weston/Macaulay (if any) it is -- that would need the kind of
symbol-by-symbol frequency/positional match Tomokiyo ran against Taylor, run against each of the other five in
turn, which this job's brief did not ask for and this job's time box did not allow. Named as the next step in
NOTES.md.

Requests this pass: archive.org about 35 (advancedsearch x5, metadata x6, fulltext/inside.php search-inside x5,
page-image fetches ~19 across the trial-and-error Taylor search and the four other systems' plates, well under the
40-request cap); cryptiana.web.fc2.com 1 (Taylor specimen, already an established route). All >=1.5s apart,
descriptive User-Agent. No logins, no credentials touched.

## ARM-TR2 manuscript completion (26 Sept 2026, LANE ARM worker ARM-TR2)

Finished ARM-TR's manuscript-verification thread: frame 0033 transcribed, page-1 lines 6-13 re-read,
the page2 L02/L06 shorthand-crop bookkeeping issue diagnosed, `ciphertext_ms.txt` now covers the whole
letter. Full narrative in NOTES.md's own "ARM-TR2" section; this section is the numbers.

**Frame 0033.** Native image is a two-document spread: LEFT page is this letter's own final leaf
(4 numeral lines + closing + signature + address, confirmed by direct read against
`M. Madison Secretary of State` and the "I have the honor to be Sir..." close); RIGHT page is a
DIFFERENT, later letter ("Paris 27 february 1808"), not transcribed. Two fresh blind Sonnet passes
over the left page's 4 line-crops (`images/crops_0033/f0033P4_L01-04.jpg`), reconciled by this worker
from the crop directly on the two edge-of-crop digits both passes flagged. Result: **exact match**
against `ciphertext.txt`'s final 37 numeral groups (79 through 170), zero substitutions, zero gaps.

**Page-1 lines 6-13, control numbers.** BEFORE (ARM-TR, first 332-of-369 covered range):
substitutions=14, in_ciphertext_not_ms=54, in_ms_not_ciphertext=1 (own NOTES.md figures). AFTER (this
job, full 369/369 letter incl. frame 0033): substitutions=9, in_ciphertext_not_ms=12,
in_ms_not_ciphertext=3, match_ratio=0.957 (`tools/... tr/diff_ms_vs_ciphertext.py`, re-run pasted in
NOTES.md).

**Root cause of most of the 54, found this pass:** ARM-TR's own `crops_0030` L06-L11 bands were cut too
close to their top edge (`tools/iiif_lines.py`'s row-ink-profile band boundary), silently shearing off
each line's first 1-2 tokens and the tops of some digits -- this, not a shorthand-vs-digit ambiguity,
is why four independent blind passes (2 original + 2 fresh) all misread "61 45" as "43". Re-cropped
L06-L11 directly with ~90px extra top margin (PIL, this worker, not a subagent) and re-read: recovers
"76 1340" (L06 head), "341 1476" (L07 head), "88 1340" (L08 head), "61 45" (L09 head, corrects "43"),
and "143" (L11 head) -- all now matching `ciphertext.txt` exactly at those positions. One genuine digit
substitution survives in this span, confirmed 4/4 passes plus this direct check: line 7's ms "200"
where `ciphertext.txt` has "203".

**What is left unresolved, honestly, not force-classified:** L12/L13 (16 and 19 marks in ARM-TR's
original count) were re-cropped with the same extra top margin and show NO hidden digits -- these two
lines really are dense runs of shorthand marks, unlike L06-L11. Against this, `ciphertext.txt`'s own
notation at the same position is minimal ("2 ** 44" -- one digit, one "several-marks" passage, one
digit), a real density mismatch this job cannot resolve: either two of ARM-TR's mark-run digits ("31"
after L09's run, "13" newly found inside L10's run) are genuine content Bourdeau's transcription folded
into a "**" without preserving, or this worker's passes are over-reading structure into what are
genuinely just flourishes. Graded M, not resolved. `2` and `44` (ciphertext.txt, no ms counterpart)
most plausibly sit inside L12/L13's own dense mark runs, indistinguishable from the surrounding
flourishes at this resolution.

**Classification of the original "54 unmatched Founders groups"** (ARM-TR's own figure, page-1 L6-13
span, first-332 coverage): of the tokens accounted for by this pass's per-token opcode diff (see
NOTES.md for the full before/after list), the large majority -- 76, 1340, 341, 1476, 88, 1340, 143 (7
tokens) directly recovered as clean exact matches, plus 61/45 correcting what had been counted as a
2-token substitution against "43/31" -- are **present in ms under the correct reading**, previously
lost to a crop-geometry bug, not a genuine transcription gap. One token (200 vs 203) is a **confirmed
digit substitution**, not absent. Two ciphertext.txt tokens (2, 44) remain **most plausibly present in
ms but indistinguishable within a dense mark run** (not ms-illegible in the sense of no image existing --
the image exists and is legible as marks, just not resolvable to specific digit values at this
resolution). None of the original 54 resolve to "ms illegible" in the sense of image damage or an
unreadable leaf -- the whole span is on a clear, well-preserved page.

**Page2 L02/L06 shorthand-crop bug, diagnosed and the two named crops fixed.** `images/shorthand/
page2_L02_seq198-212_15marks.jpg` and `page2_L06_seq250-264_12marks.jpg` were pulled from
`crops_0031L`'s raw `L0N` filenames without applying the +1 line-index correction that
`tr/page2_passA_shift.tsv` already applies for the main transcription passes (crops_0031L has one
extra faint/blank line at its own top before its real content starts, so its "L02" is physical content
line 1, not line 2). Both named crops have been replaced with the correct line images (sourced from
`crops_0032L`, which is correctly indexed) and now show their claimed mark content: L02 the all-marks
line (`* * * * * * * * * * * * * * *`), L06 `* 45 147 1158` plus its trailing mark run. **Not fixed,
flagged for a successor:** the same bug most likely affects every other page2 shorthand crop
(`page2_L01,L03,L04,L07,L10,L11,L13`), which this job's brief did not name and time did not allow;
spot-checked L04, confirmed same one-line shift. A full page2 shorthand-crop re-derivation is the
next cheap step before any family-S job trusts that folder.

Units-digit distribution, full letter, ms vs ciphertext.txt (`tr/diff_ms_vs_ciphertext.py` output,
covering all 369 positions): both distributions agree closely in shape (0/1 dominant, 2/3/5/9 rare,
matching ARM-DESIGN's own finding) -- full table in NOTES.md. No systematic 2/3/5/9 misreading found
anywhere in the now-complete comparison.

No network this job (all work against images already on disk). 2 Sonnet subagent calls (frame 0033,
2 concurrent blind passes) + 2 Sonnet subagent calls (page-1 L6-13, 2 concurrent blind passes) = 4
subagent calls total; all further settlement (page 4 edge digits, the L06-L11 crop-top fix, the page2
shorthand-crop diagnosis) done directly by this worker against the images, not delegated.

## ARM-S2 symbol match (26 Sept 2026, LANE ARM worker ARM-S2): per-system symbol-by-symbol comparison, not a decode

Full detail: `images/shorthand/INVENTORY_reconciled.tsv`, `images/shorthand/profile_check.py`,
`images/shorthand/specimens/symbol_match.tsv`, `images/shorthand/specimens/score_summary.py`. Runs the finer,
symbol-by-symbol method (the way Tomokiyo actually ran it against Taylor) that ARM-S1's own coarse shape-category
comparison could not.

**Reconciliation (2 subagent calls, visual crop verification, not just numeric coincidence).** ARM-S1's own
qualitative C1-C10 categories turned out to sum exactly against the raw pass-A/pass-B counts, but a visual
crop-by-crop check (two Sonnet subagents, given both passes' rows, crops, and position indices) found the
numeric coincidence overstated some merges: pass-A S16/S18 are only "partial" matches to pass-B Sh.1's dominant
wave (a compound double-hump and a stretched-flat variant, not pixel-identical to a single Sh.1 unit), and
pass-A S6 vs pass-B Sh.3 (both "back-curving hook") "may represent two different size classes rather than one
shape." Confirmed exact merges: S4==Sh.2 (3-loop-tail), S3==Sh.16 (slash), S9==Sh.11 (percent-compound), and
S28==Sh.6==Sh.5's stroke-shape (the superscript tick above a numeral is the SAME physical dash stroke as the
baseline dash/bar, just repositioned -- not a distinct character). Confirmed distinct (not mergeable): pass-A S2
(open cup, opposite curvature from the wave family) and pass-B Sh.9 (a large closed loop, confirmed NOT the same
as pass-A S12's small open hook) -- both get their own category, neither in ARM-S1's original C1-C10. Result:
**12 reconciled shapes covering 189 of ~221.5 total catalogued marks (85.3%)**, `INVENTORY_reconciled.tsv`.
Several page-2 exemplar crops used the corrected `images/crops_0032L/f0032L_L0N.jpg` files per ARM-TR2's flag
(content-line N = that file directly, verified by md5sum match against the already-fixed L02/L06 pair), not the
still-buggy `images/shorthand/page2_L0N_*.jpg` files for L01/L03/L04/L07/L10/L11/L13.

**Profile check (script, `profile_check.py`).** Top shape (R1, the wave/filler stroke) = 33.9% of all marks
(27.5% if only the visually-confirmed core is counted, excluding the two "partial" variants) -- 2.2-2.7x the
single most frequent English letter ("e" 12.7%) and 3.9-4.8x the single most frequent English word ("the" 7.0%).
**Fits neither the letter-alphabet hypothesis nor the Zipf word/syllable-sign hypothesis**; consistent with a
structural/connector stroke (a vowel mark, syllable joiner, or line-filler) rather than a phonetic letter or
lexical sign. Ranks 2-3 (13.1%, 10.8%) sit in the range of mid/high-frequency English letters but on the high
side; the low-tail shapes (0.9-2.3%) are individually untestable at these counts (rule 3).

**Seven-system symbol match, all numbers reported (rule 3's own instruction, "whatever they say"):**

| system | shape_score | freq_score | yes/partial/no |
|---|---|---|---|
| Taylor1786 (known negative) | 0.532 | 0.289 | 2/8/2 |
| Pitman_CONTROL | 0.429 | 0.295 | 3/4/5 |
| Byrom1796 | 0.585 | 0.218 | 4/6/2 |
| Gurney1752 | 0.659 | 0.506 | 6/6/0 |
| Mavor1792 | 0.653 | 0.389 | 6/5/1 |
| Weston1727 | 0.421 | 0.875 | 6/5/1 |
| Macaulay1747 | 0.529 | 0.135 | 2/9/1 |

(shape_score = mark-count-weighted fraction of yes/partial shape counterparts over the 12 shapes' 189 marks;
freq_score = mark-count-weighted fraction "consistent" among shapes that got any letter assignment at all,
excluding shapes graded "n-a" -- a punctuation/diacritic/ligature/page-furniture reading, not a letter claim.)

**Two of rule 3's own sanity checks come back honestly messy, not clean:**
1. Pitman (control) does **not** score lowest of all seven on shape_score -- Weston (0.421) scores below it
   (0.429). Weston's own subagent independently called R1 a flat "no" (not even "partial") and found no
   single-letter counterpart for the dominant filler stroke at all, which is the single largest driver of its
   low score; Pitman's control got partial credit on R1 (an arc) that Weston's own alphabet, checked more
   carefully, did not. This means shape_score has **no resolving power for Weston specifically** -- a real
   18th-c. cursive-loop system scoring below a Victorian geometric-line control is itself a finding (the method,
   not Weston, is what fails this comparison), not evidence against Weston.
2. Two of the five candidates' specimens are not clean alphabet plates, which inflates their letter-assignment
   counts without a real basis: **Gurney's specimen is running italic prose, not a stroke table** -- its own
   subagent found most of its "yes"/"partial" verdicts are matches to ordinary page furniture (scribal
   abbreviation tittles, an "&c." ampersand twice, i-dots/periods, a closing ornamental paraph), not to Gurney's
   actual shorthand alphabet; Gurney's high shape_score (0.659, the top of the table) is an artifact of this and
   is not a real symbol-by-symbol result. **Taylor's own specimen (the already-known negative) has the same
   problem** -- it is Tomokiyo's crop of a specimen of connected running shorthand, not a labelled alphabet
   chart either, so Taylor's letter assignments are equally best-effort guesses, not verified labels. Only
   Byrom, Mavor, Weston and Macaulay have genuine labelled alphabet/consonant plates; Taylor and Gurney's
   apparent scores are not on the same footing as those four and as Pitman's control.

**Verdict: exclusion of all five candidate systems, not an identification, on both scores together.**
Restricting to the four systems with genuine labelled plates (the only fair comparison against Taylor and
Pitman): Mavor (0.653) and Byrom (0.585) beat Taylor (0.532) on shape_score by a real margin; Macaulay (0.529)
ties Taylor almost exactly (no resolving power); Weston (0.421) scores below both Taylor AND the control (no
resolving power, method failure as above). But rule 3's second bar -- "a frequency-consistent profile" -- rules
out even Mavor and Byrom: both assign the two dominant shapes (R1 33.9%, R2 13.1%, 47% of all marks together) to
letters (m and f/j respectively) whose real English frequency is nowhere near that high, exactly the failure
mode Tomokiyo's own symbol-by-symbol check found against Taylor. No candidate clears both bars. This is
consistent with ARM-S1's own coarser conclusion (right family, wrong resolving power) but now earned by the
actual finer method the brief asked for, with the added, more useful findings of *why* it doesn't resolve:
R1's share rules out a letter-alphabet reading in every one of the seven systems tested including the control,
and two of the five candidate specimens (Gurney, and Taylor's own reused specimen) are not clean alphabet
charts, so their scores are not comparable to Byrom/Mavor/Weston/Macaulay's. The marks remain most plausibly a
private/idiosyncratic shorthand or the code's own device, not a match to any of the six systems checked
(Taylor + the five candidates).

**Superscript-tick finding, corroborated cross-system.** The tick above a numeral (pass-B Sh.5, positions
page2 L10/L13) is confirmed the same physical stroke-shape as the ordinary baseline dash (pass-A S28, pass-B
Sh.6), just repositioned -- not a separate character. Independently, both the Mavor and Weston subagents
(without being told about each other's finding or about ARM-S1's tick discovery) flagged that this baseline
dash matches those two systems' own vowel-position marking convention (a short stroke placed near a consonant
sign to indicate a vowel), which is one plausible functional reading of why the same stroke appears both on the
baseline and floating above a numeral in this manuscript -- offered as a lead, not a claim (M-grade, no H/C).

**NARA superscript-tick check (step 4, optional): attempted, inconclusive, request budget spent.** Frame
M34-014-0025 (continuing the already-known 15 Feb 1808 Armstrong-to-Madison THE=972 office-code letter, per
ARM-POOL's own roll-14 survey) was targeted via the same keyless `catalog.archives.gov` IIIF v3 route ARM-IMG
documented (confirmed working for frames 0029-0033 in `images/manifest.json`). Both allowed requests (info.json,
then a direct `full/full/0/default.jpg` fetch) returned the site's HTML app shell at HTTP 200, not the image --
the same "wrong/inaccessible object path" signature ARM-IMG and ARM-POOL both documented for invalid frames,
though ARM-POOL's own prior pass reported reading this same frame's native image directly (uncommitted scratch,
route not recorded). Did not retry a third time (this job's 2-request cap for this host, and the good-citizen
rule's one-retry limit, both already spent). The tick-as-office-convention question is untested, flagged for a
successor with the exact working fetch route recorded first.

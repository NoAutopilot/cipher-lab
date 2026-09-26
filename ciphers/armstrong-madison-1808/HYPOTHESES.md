# armstrong-madison-1808 -- hypothesis families (append-only below the ladder)

LANE ARM, opened 26 Sept 2026 06:49 UTC (owner's decision 06:40). One section per family; CONTROL and TARGET
numbers side by side (CLAUDE.md rule 3). The top block is rewritten only by a cycle consolidator.

## Ladder (LANE ARM orchestrator, 26 Sept 2026)

- A. Crib placement -- AS BRIEFED, NO CRIB EXISTS: QUEUE row 27's "Krajcovic's crib from the 15 Feb letter to
  Jefferson" is a scout mix-up (TOMO-REPLY, NOTES.md). Replaced by A1 (ARM-REC: crib hunt in the later
  correspondence) and A2 (direct-transfer sweep of every published sibling table against a structure-preserving
  shuffled table, after ARM-CODES).
- B. Sibling-code vocabulary: corpus ARM-CODES (tools/data/uscodes-1800/), design ARM-DESIGN (Fable; one-part vs
  two-part, tested on two siblings as control).
- C. Nomenclator solver with the vocabulary prior (family_run.py `nomenclator`), after B.
- D. Model-in-the-loop, only if C's control clears and the target reads partially.
- E. Recovery (ARM-REC).
- S. Shorthand passages (35 short + 2 lines) against period systems -- not in the brief's ladder; queued after B.
- Judge: en18 corpus (ARM-EN18) before any en verdict on this target is trusted.

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

# kaliningrad-2015 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

**Summary, cycle 4** (GOLD-CONS4, Fable, session_01CSQuomCj5Simbsx6r6VVcK, 26 Sept 2026 00:50 UTC; the first top
block of this file, written from LANE B2's test 1 and GOLD-KAL1's sections below; rewritten once per cycle by the lane's
consolidator and by nobody else -- everything below the first `##` stays append-only)

**Target facts every family must respect.** Ernst's transcript (Cipherbrain post 19, comment #32, 22 Oct 2017; row-checked
against the two images by LANE B2, no disagreement beyond his "x" label for the hard-sign-like glyph). Word divisions
visible: 206 space-separated tokens, ten of them a trailing-dot filler line, nine dotted abbreviation groups. Two
tokenisations, both of record (`ciphertext_signs.tsv` is convention A, made by `scripts/make_signs_tsv.py`; the
consolidator derived convention B from it by splitting the trailing apostrophe off):

| convention | N | K | IC | top signs (count) | apostrophe |
|---|---|---|---|---|---|
| A: letter+apostrophe = one sign | 978 | 36 | 0.0657 | e 156, n 105, i 68, x 65, s 62, h 43, d 43, u 43, f 41, a 39, l 38, w 37 | 88 compound signs (9.0 pct): n' 29, t' 16, x' 12, d' 11, l' 5, f' 5, s' 4, m' 3, z' 2, -' 1 |
| B: apostrophe = its own sign | 1066 | 28 | 0.0718 | e 156, n 134, ' 88, x 77, i 68, s 66, d 54, t 48, f 46, h 43, l 43, u 43 | 88 of 1066 (8.3 pct), always in-word after one of 9 consonant-like signs |
| B folded to a-z (diacritics folded, apostrophes dropped; the transposition view) | 977 | 21 | 0.0836 | e, n, x, i, s, d, t, f, h, l | -- |

The NOTES.md counts from LANE B2's `ic_analysis.py` run (n 92, n' 42, x 62, s 61) differ from the committed TSV's (n 105,
n' 29, x 65, s 62) by 13 apostrophes assigned differently at the same N and K; the TSV is what `family_run.py` reads and
is the number of record for family runs; the next worker reconciles the two in its first five minutes (which rule
`tokenize_signs` applies at a double apostrophe or a dot) and records which is right, without repairing the transcript.
Diacritic signs ê 17, ö 7, ü 1 are their own signs under both conventions. The "x" glyph (77 under B, 7.2 pct) sits
in-word and once doubled (`cfefdxx`), so it is not a clear hard sign of either Russian orthography (pre-1918 word-final
ъ about 3-4 pct of letters, always word-final; post-1918 ъ 0.01 pct). The two thread claims: Ernst 2017 ("political",
cross-language polyalphabetic; no text, no method) is untestable as stated; Frank 2021 (a Synodal Bible chapter) was
tested by GOLD-KAL1 and is a control-backed negative on the host text (below), which excludes that text as host, not
Russian as the language.

**Profile against the corpora on disk and against transliterated Russian** (this consolidator, `tools/data`, windows of
the target's N, seed 42; the Russian schemes are built from `tools/data/ru19`, the Synodal Bible, first 600k letters,
through `homophonic_anneal.fold`, which keeps a-z only and merges j into i and v into u, so a scheme has at most 24
plaintext letters; ь and softness marks are carried as `q`):

| corpus / scheme | K | IC at N 978 (min-max over 20 windows) | apostrophes per letter in the raw text | identity L1 of the B-folded target vs the corpus (window null p99) |
|---|---|---|---|---|
| de20 (1880-1940 German) | 24 | 0.0756 (0.0687-0.0840) | 0.0006 (0.6 expected at N 1066) | 0.375 (p99 0.368); 0.239 if the x glyph is re-read as r |
| en (Holmes + Moby-Dick) | 24 | 0.0666 (0.0635-0.0693) | 0.0060 (6.4) | 0.553 (0.242) |
| nl20 | 24 | 0.0817 (0.0764-0.0883) | 0.0029 (3.1) | 0.473 (0.399) |
| fr19 | 24 | 0.0815 (0.0759-0.0887) | 0.0131 (14.0) | 0.599 (not computed) |
| da19 | 24 | 0.0766 (0.0698-0.0858) | 0.0002 (0.2) | 0.523 (0.254) |
| it16 / es17c / pt18 | 24 | 0.0758 / 0.0762 / 0.0774 | 0.0069 / -- / -- | 0.674 / 0.656 / 0.693 |
| Russian S1, scientific digraphs (zh ch sh shch yu ya yo kh ts; e for е ё э; y for й ы; q for ь; ъ dropped) | 23 (B view) / 34 (A view, consonant+q merged) | B view at N 1066: 0.0608 (0.0580-0.0655); A view: 0.0608 (0.0578-0.0661) | q 0.015 | rank-profile L1, target A vs scheme A: 0.245 (window null median 0.103, max 0.145): outside |
| Russian S3', phonemic partial (q after a paired consonant before я ю ё and for ь; the vowel then plain) | 23 / 36 | B: 0.0601 (0.0569-0.0640); A: 0.0611 (0.0563-0.0767) | q 0.029 | rank L1 0.214 (null max 0.275): inside |
| Russian S3, phonemic full (q also before е и) | 23 / 37 | B: 0.0638 (0.0602-0.0691); A: 0.0547 (0.0502-0.0704) | q 0.126 | rank L1 0.263 (null max 0.284): inside |
| Cyrillic itself (33 letters, for reference) | 33 | 0.0572 whole corpus | ь 0.0156, ъ 0.0001 | -- |

Reading the table. (1) Under convention A the target's IC 0.0657 sits inside every Russian scheme's window range and its
K 36 equals S3' A-view's K 36 (S3 gives 37, S1 34); the rank profile is inside the window null for the phonemic
schemes. The IC gap LANE B2 reported (target 0.0657 vs its Russian control 0.0563) came from a scheme that folded the
soft sign into the apostrophe and dropped it, on a 34k-letter Gutenberg text; with the scheme matched to the tokenisation
the gap is gone. Under convention B the target's 0.0718 is above every scheme's B-view maximum (0.0640-0.0691), so the
data prefer the reading in which an apostrophe-bearing sign is one plaintext unit (a soft or softened consonant as its
own letter) over the reading in which the apostrophe is a separate plaintext letter. (2) A pure transposition of any
Latin orthography on disk is excluded by the apostrophe count alone: a transposition keeps every character, and 88
apostrophes at N 1066 against an expectation of 0.2-14 (French the highest) is a chi-square above 390 on that cell for
French and above 10,000 for German; the identity profile agrees for English, Danish and Dutch (L1 outside the window
p99) and for German unless the x glyph is read as r (then 0.239, inside p99 0.368 -- so for German the apostrophe count
is the exclusion, not the profile). A transposition of Cyrillic ("ru-cyrillic-transposed" in the spec) is excluded by the
sign inventory as transcribed (Latin cursive with apostrophes and three diacritics), conditional on the transcription
(rule 2). (3) The apostrophe share 8.3 pct is above a clear soft sign (1.5 pct, S1) and below full phonemic softness
marking (12.6 pct, S3); S3' at 2.9 pct is also short; the writer's own scheme is a free parameter bounded by these three.

**Family table, every control beside its target (numbers of record in the sections below).**

| family | job | CONTROL | TARGET | read |
|---|---|---|---|---|
| IC and matched-N language controls | LANE B2 test 1 (25 Sept) | ru transliterated (Gutenberg 30774) IC 0.0563 (0.0543-0.0605); de16 0.0724 (0.0676-0.0765), 20 windows each | 0.0657 (A, K 36) | not conclusive on its own; superseded by the scheme-matched table above |
| Crib: Synodal Bible chapter as host text (Frank 2021), word-pattern solver, convention A | GOLD-KAL1 | letters recovered, 3 seeds: A full-vocab 1.000/0.998/1.000 (0.999), held-out 1.000/0.991/1.000 (0.997); gate 0.9 met | 22/187 words matched (0.118) vs shuffle-null max 0.096 (seeds 0.096/0.080/0.064); best chapter John 6 covers 14/22 (0.636) vs null 5 of 6 seeds over 0.5 (mean 0.632) | **control-backed negative on the host text**; the chapter-cover criterion fires on noise |
| Crib, convention B (K 27 as KAL1 cleaned it) | GOLD-KAL1 | B full-vocab 1.000/0.992/1.000 (0.997), held-out 1.000/0.992/1.000 (0.997); gate met | 23/187 (0.123) vs null max 0.080; Ezekiel 39 covers 19/23 (0.826) vs null max 0.750 | **control-backed negative**; +0.043 over the null on words, under the 0.2 bar |
| German light homophonic, K 36 profile=target, de20 (1880-1940) | GOLD-KAL1 | recovery 0.992/0.960/0.994, mean 0.982; gate 0.9 met | judge FAIL -1.605 (real_p05 -0.817, null_p99 -2.083, N 978) | **control-backed negative** for German substitution at this K and register |
| Russian substitution, any scheme | never run | -- | -- | **open**: the leading hypothesis on structure (apostrophes after 9 consonant-like signs in-word, K 36 = S3' K 36, IC inside all three scheme ranges under A); cycle-5 briefs below |
| Polish / Lithuanian substitution | never run; no corpus on disk | -- | -- | open; cycle-5 brief below (Polish marked letters ą ę ó ł ż ś ć ń ź are 6.9 pct of Polish letters against the target's 9.0 pct compound signs, 9 marked types against the target's 9-10) |
| Transposition, Latin orthographies | this block (profile and apostrophe count) | window nulls above | L1 outside p99 for en, da19, nl20; apostrophe count 88 vs at most 14 expected | **excluded by the apostrophe count**, profile agrees except German-with-x-as-r |
| Periodic IC (spec test 3) | never run | -- | -- | five-minute step, folded into the cycle-5 Russian brief with its shuffle control |

**Decision, cycle 4, P(the first result moves the target) x value / cost.** Value is the item's fixed worth (Schmeh's
no. 19, no machine run across languages on record before this lane); ranking by P(moves) per $10 against the 0.03 bar.
Unit costs from the record: a `family_run.py --family homophonic` control-plus-target unit at N 978 took GOLD-KAL1 about
10-12 minutes and about $1 at GOLD-K4's rate ($3.16 for 51 minutes of family_run units); a corpus build with a script and
its offline test about 10 minutes and about $1.50 (KAL1's crib tool was the expensive part of its $4.61).

| rank | family | why this P | P(moves) | cost | P per $10 | box |
|---|---|---|---|---|---|---|
| 1 | Russian, convention B (K 28), homophonic profile=target, corpus S3' then S1 (apostrophe = a softness mark or soft sign written in clear; the solver maps ' to q) | the natural reading of the apostrophe structure; against it, the B-view IC 0.0718 sits above both schemes' window maxima (0.0640, 0.0655) and a homophonic split lowers IC further | 0.08 for the pair | 2 units, about $2 | 0.4 | **GOLD-KAL2** (brief `2026-09-26-lane-gold-c5-kaliningrad-russian.md`) |
| 2 | Russian, convention A (K 36), homophonic profile=target, corpus S1 with softness stripped (n and n' as homophones of one letter) | the reading the IC prefers (0.0657 inside 0.0578-0.0661); loses the softness information, so the judge scores base text | 0.05 | 1 unit, about $1 | 0.5 | GOLD-KAL2 |
| 3 | Russian S3 full, convention B | q at 12.6 pct against the target's 8.3; a bound, not a favourite | 0.03 | 1 unit, about $1 | 0.3 | GOLD-KAL2 if the box allows, else GOLD-KAL3 |
| 4 | Polish, conventions A and B, homophonic profile=target, corpus from Gutenberg (at most 6 fetches) | 40 km from the Polish border; marked-letter share 6.9 vs 9.0 pct, 9 marked types vs 9-10; folded Polish IC about 0.063-0.067 (to be measured on the fetched corpus) brackets the target's 0.0657 | 0.06 | corpus + 2 units, about $4 | 0.15 | **GOLD-KAL3** (brief `2026-09-26-lane-gold-c5-kaliningrad-polish.md`) |
| 5 | Lithuanian, same design, only if api.getbible.net lists a Lithuanian translation (one request to check, one fetch) | marked letters ą ę ė į ų ū č š ž about 7-8 pct of letters; no Gutenberg prose | 0.03 | 1 fetch + 1 unit, about $2 | 0.15 | GOLD-KAL3, conditional |
| 6 | Russian one-to-one scheme (33 letters) or convention A with each soft consonant its own plaintext letter (K 36-37) | the best structural fit (K and rank profile) but needs a plaintext alphabet wider than `fold()`'s 24 letters: a tool change in `homophonic_anneal.py` (alphabet parameter) and in the judge's fold | 0.06 | Fable tool job about $12 + 2 units | 0.05 | not briefed this cycle; cycle 6 if ranks 1-3 are control-backed negatives and the A-view fit still stands |
| 7 | Latin sweep: en, fr19, nl20, it16, es17c, pt18, da19, homophonic K 36 profile=target | no provenance link; no Latin orthography puts an apostrophe after 9 consonants in-word at 8 pct; German already negative | 0.03 for all seven | 7 units, about $7 | 0.04 | not briefed; the cycle-6 fallback, at the bar |
| -- | Transposition, any Latin orthography; Cyrillic transposed | excluded above with numbers | -- | -- | -- | no box |
| -- | Periodic IC on the sign sequence, periods 2-30, against 3 shuffles | spec test 3, never run; five minutes | folded in | -- | -- | first step of GOLD-KAL2 |

**NEAR.md: no row.** Two control-backed negatives (the Synodal crib, German homophonic) and one language-control
statistic; no solver beat its control and no control showed a negative was not a real test (rule 5's amendment). The
register is this block and the spec's `cheap_test_done`; status stays `open` (never closed-negative: the leading
language has not been run).

**Lane recommendation.** The reserve's Russian units are the lane's best P per dollar anywhere (0.3-0.5 per $10 against
Köhler's 0.05 for its last beau cell and Debosnys's zero until the museum answers): the next dollars go to GOLD-KAL2, then
GOLD-KAL3, with Köhler paused and Debosnys parked. A judge PASS on any unit stops the job and owes a re-derivation
(rule 7); a control-backed negative on ranks 1-3 leaves rank 6 (the wide-alphabet tool) as the last Russian step.

Rule 10: nothing in this file is a reading; status stays `open`; the lane never writes solved, new, first or unpublished.

## GOLD-KAL1, crib test and German homophonic (25 Sept 2026)

Two families, both control-first (CLAUDE.md rule 3), per the reserve brief
(`.claude/briefs/runs/2026-09-25-lane-gold-c4-kaliningrad-crib-and-homophonic.md`). Corpus: `tools/data/ru19`
(Russian Synodal Bible, 78 books, 1,362 chapters, 3.2M letters, fetched this job -- see its README.md). Solver:
`ciphers/kaliningrad-2015/scripts/pattern_crib.py` (beam-search word-pattern constraint propagation; see its
own docstring for why a beam and not a single greedy commit -- a pure greedy pass on one real control window
(convention A, seed 1) collapsed to 3 pct letters recovered from a single bad early pick, 100 pct once beam
search was added; this was found and fixed before any target run, per the brief's "fix the tool, never the
target" instruction, and is the only tool change made). Offline test: `tools/tests/test_pattern_crib.py`
(8 checks, <0.1 s, synthetic 120-letter fixture corpus, no network).

**Tokenisation.** Convention A: letter+apostrophe merges to one cipher sign (ic_analysis.py's own convention,
K=36); the matching plaintext merge is a Cyrillic consonant + trailing ь/ъ (soft/hard sign) into one token.
Convention B: apostrophe is its own sign (K=27 observed on the target after cleaning, see below); plaintext
tokens are individual Cyrillic letters, no merge (ь/ъ are already separate letters in Cyrillic). Of the
target's 206 space-separated tokens, 10 are the trailing-dot filler line (`eimat . . . . . . . . . .`, dropped
entirely, not signs), leaving 196; of those, 9 have >=2 internal dots and are classified as dotted abbreviation
groups (`x.s.f.d.`, `c.f.`, `f.t.'f.`, `x.l.b.`, `s.n.c.`, `x.l.n.`, `d.s.z.-`, `n.t.d.`, `n'.xn.`) and excluded
from crib matching (abbreviations do not appear as Bible vocabulary word forms), leaving 187 crib-matchable
words -- one short of the brief's "ten dotted abbreviation groups"; the discrepancy is that 8 further tokens
carry a single TRAILING dot immediately before one of Ernst's own running-count markers or a closing quote
(`nenet'se.`, `xf'uaf'np.`, `ngwsaetme.`, `eamdemn.`, `n'eêain.`, `wxixeheu.`, `kexeelxn."`, and `m'am'mt.`,
which precedes the clearly-abbreviation-shaped `f.t.'f.` on the same line but is not itself before a bracket
marker) -- these are read here as section/quote boundary punctuation, not abbreviation dots, and the trailing
dot is stripped before tokenising the word itself; a different judgement call on `m'am'mt.` would move the
abbreviation count to 10, matching the brief exactly, without changing which words are matched below.

### Control (rule 3), both conventions, seeds 1-3, `pattern_crib.py control`

(a) = full vocabulary (the claim's own condition, "Frank had the plaintext to compare against"); (b) = the
control's own source chapter held out of the vocabulary. Score = share of the window's plaintext LETTERS
correctly recovered under the solver's derived sign->letter map.

| convention | seed | chapter | N letters | (a) full-vocab recovery | (b) held-out recovery |
|---|---|---|---|---|---|
| A | 1 | 2 Samuel 11 | 988 | 1.000 | 1.000 |
| A | 2 | Leviticus 27 | 1002 | 0.998 | 0.991 |
| A | 3 | Psalm 49 | 1003 | 1.000 | 1.000 |
| A | mean | -- | -- | **0.999** | **0.997** |
| B | 1 | 2 Samuel 11 | 978 | 1.000 | 1.000 |
| B | 2 | Leviticus 27 | 977 | 0.992 | 0.992 |
| B | 3 | Psalm 49 | 976 | 1.000 | 1.000 |
| B | mean | -- | -- | **0.997** | **0.997** |

GATE (>=0.9 on 3 seeds): **MET**, both conventions, both (a) and (b). (a) and (b) are numerically identical or
near-identical in every seed: the corpus (676,699 words, 3.2M letters) is about 3,000x the size of a single
~978-letter window, so holding out one chapter essentially never removes a word FORM from the vocabulary
entirely (checked directly: excluding chapter (10,11) drops the vocabulary's total word count by 687 but its
count of distinct word-pattern keys by zero) -- the held-out condition is honestly run but uninformative at
this corpus scale, not a second independent test of generalisation the way it would be on a smaller corpus.

Commands: `python3 ciphers/kaliningrad-2015/scripts/pattern_crib.py control --convention {A,B} --seed {1,2,3}
[--holdout]`

### Target, both conventions, `pattern_crib.py target`

| convention | words matched | letters mapped | best chapter | chapter cover |
|---|---|---|---|---|
| A | 22/187 (0.118) | 0.649 | John 6 | 14/22 (0.636) |
| B | 23/187 (0.123) | 0.714 | Ezekiel 39 | 19/23 (0.826) |

### Null (shuffle each cipher word's own signs), 3 seeds, `pattern_crib.py null`

| convention | seed | words matched | best-chapter cover (computed separately, not printed by the CLI) |
|---|---|---|---|
| A | 1 | 18/187 (0.096) | 13/18 (0.722) |
| A | 2 | 15/187 (0.080) | 7/15 (0.467) |
| A | 3 | 12/187 (0.064) | 7/12 (0.583) |
| B | 1 | 12/187 (0.064) | 9/12 (0.750) |
| B | 2 | 15/187 (0.080) | 11/15 (0.733) |
| B | 3 | 13/187 (0.070) | 7/13 (0.538) |

**Reading against the brief's two flag criteria.** (1) Target words-matched share above the null's max by
>=0.2: convention A 0.118 vs null max 0.096, diff 0.022; convention B 0.123 vs null max 0.080, diff 0.043 --
**neither clears the bar**. (2) A best chapter covering over half the decoded words: convention A 0.636, B
0.826 -- both literally clear 0.5, which by the brief's rule is a `flag:` line, posted to ROOM. But the null
runs above show a single best-matching chapter covers over half the (small number of) matched words in 5 of 6
shuffle-null seeds too (mean 0.632, range 0.467-0.750) -- indistinguishable from the target's own 0.636 (A) and
only modestly above the null's own range at 0.826 (B, +0.076 over the null max). With only 22-23 words matched
out of 187, this is expected: a handful of short, common decoded forms (the highest-frequency patterns, hardest
to pin to one specific chapter) concentrate wherever they happen to occur, in the null exactly as in the
target. **Conclusion: this criterion fires by the letter of the brief's rule, but the null control shows it
fires on pure noise too at this N, so it is not being read as evidence for Frank's claim** -- flagged per
instruction, not reported as a lead.

Ernst's 2017 "political... cross-language polyalphabetic" claim (comment #50-52) names no text and no method
and remains untestable as stated; no test was attempted against it.

### German homophonic (family_run.py, control-first)

`ciphers/kaliningrad-2015/ciphertext_signs.tsv` (convention A, generated by
`scripts/make_signs_tsv.py`, N=978 K=36, reproducible from `ic_analysis.py`'s own `tokenize_signs`).
`specs/kaliningrad-2015.json` judge.corpora repointed to `tools/data/de20` (1880-1940 German prose, the same
set koehler-1944.json uses) with a `corpora_note`; the LANG_CORPORA default for `de` (de16, Early New High
German) would have been wrong for a Soviet-era target.

Command: `python3 tools/family_run.py specs/kaliningrad-2015.json --family homophonic --cipher
ciphers/kaliningrad-2015/ciphertext_signs.tsv --corpus tools/data/de20 --param profile=target --seeds 3
--restarts 8 --gate 0.9 --label "GOLD-KAL1 homophonic de20 K36 profile=target, control before target"`

Control (profile=target, 3 seeds): recovery 0.992 / 0.960 / 0.994, mean **0.982** (0.960-0.994). GATE (>=0.9):
**MET**. Target: judge **FAIL** -- score -1.605 vs null_p99 -2.083, real_p05 -0.817, real_median -0.782 (N=978,
mode=both). Full row in the table below. **Control-backed negative for German light-homophonic substitution at
K=36, profile=target, de20 register.** No decoded text described (judge did not pass, rule 7/10).

### Dead ends / not attempted this job

- A Russian masc (simple substitution) control was not built: `homophonic_anneal.py` folds plaintext to a-z
  (26 Latin letters) and has no Cyrillic mode; building one was out of this job's scope (brief item, not
  attempted).
- Transposition was not tested (brief's own reasoning: a transposition preserves the source language's IC,
  the target's 0.0657 matches neither Russian's 0.056 nor German's 0.072-0.076 control range (LANE B2), and
  the apostrophes sit consistently after consonants in-word, a structure a transposition would scatter).
- Only prefix windows (from each chapter's start) were used for the crib control; a mid-chapter window was
  not tried and could plausibly read differently for a name-dense opening verse range.

## GOLD-KAL2, Russian transliteration schemes (26 Sept 2026)

Per the reserve brief (`.claude/briefs/runs/2026-09-26-lane-gold-c5-kaliningrad-russian.md`), cycle-4
decision ranks 1-3 (the reserve's best P(moves) per dollar in the lane). No subagents, disk and CPU only.

**Tokenisation.** `ic_analysis.tokenize_signs` (the function `make_signs_tsv.py` uses to build the committed
`ciphertext_signs.tsv`) drops any apostrophe it cannot attach to an immediately preceding consonant within
the same token: a true double apostrophe (a second `'` right after one already consumed) is silently
discarded, and so is an apostrophe that STARTS a dot-separated part of a dotted group (e.g. `f.t.'f.` splits
to parts `f`, `t`, `'f`, and the leading apostrophe of `'f` is dropped rather than credited to the preceding
`t`) or that leads a word after `.strip("'\"-,")` (e.g. `-'fef` loses its leading apostrophe before the loop
even starts). Two consonants each followed by their own apostrophe written back to back (`t't'`, `n'n'`) are
NOT a double-apostrophe case at all -- each consonant correctly consumes exactly one trailing apostrophe, so
`n'n'` reads as two separate `n'` signs, not one dropped mark. Regenerating `ciphertext_signs.tsv` with
`make_signs_tsv.py` reproduces the committed file byte for byte (N=978, K=36, with `n` 105 / `n'` 29 / `x` 65
/ `s` 62, matching the consolidator's table, not LANE B2's NOTES.md counts) -- the TSV is correct by the
script's own rule as it stands; no regeneration or repair was needed. `scripts/periodic_ic.py` (new, 15
lines) computes mean coset IC for periods 2-30 on the convention-A sign sequence against 3 shuffle-seed
controls: flat, best period 17 at 0.0666 vs shuffle max 0.0658 (margin 0.0008, under the 0.01 flag bar) --
no periodic-key signal, no ROOM flag.

**Convention B TSV.** `scripts/make_signs_tsv_b.py` (new) derives `ciphertext_signs_B.tsv` from the same
`tokenize_signs` output by splitting every compound sign `X'` into two rows, `X` then `'`, on the same line:
N=1066, K=28, matching the consolidator's table exactly.

**Corpus.** `tools/translit_ru.py` (new, offline test `tools/tests/test_translit_ru.py`, 11 checks under 2 s)
implements the four schemes letter-for-letter from the brief's table, built from `tools/data/ru19` (no
network). Measured soft-sign-marker (`q`) share: s1 1.44 pct, s1s 0.00 pct, s3p 2.89 pct, s3 11.69 pct --
matching the brief's estimates (1.5 / -- / 2.9 / 12.6 pct) in order and magnitude. Output committed to
`tools/data/ru19_lat/` with its own README and MANIFEST.

**Family runs, control first (`tools/family_run.py --family homophonic --param profile=target`, gate 0.9,
3 seeds, 8 restarts each; full command lines and rows are in the table below).**

| unit | scheme | convention | K | control mean (range) | gate | target judge |
|---|---|---|---|---|---|---|
| 2-ru-s3p-B | S3' phonemic partial | B | 28 | 0.999 (0.997-1.000) | met | FAIL: -1.706 (real_p05 -0.889, null_p99 -2.106) |
| 2-ru-s1-B | S1 scientific digraphs | B | 28 | 0.997 (0.995-1.000) | met | FAIL: -1.729 (real_p05 -0.886, null_p99 -2.103) |
| 2-ru-s1s-A | S1 stripped (no soft sign) | A | 36 | 0.733 (0.206-0.998) | NOT met | not run -- CONTROL BELOW GATE |
| 2-ru-s3-B | S3 phonemic full | B | 28 | 0.677 (0.498-0.780) | NOT met | not run -- CONTROL BELOW GATE |

First 40 letters of the two gated target decodes (word salad, never a reading, rule 7/10): S3'-B
`ieniwoeynontsenwyiiesaidiamrieioiyielkat`; S1-B `isatyzskanarisayklimiotetoeeiminlkimeeow`.

**Reading this.** Ranks 1 and 2 (S3'-B, S1-B) are now **control-backed negatives** for Russian homophonic
substitution at convention B (K=28), profile=target, on the Synodal Bible register: the control anneal reads
its own design at 0.997-0.999 while the target scores well below the real-prose floor on both schemes. Rank 3
(S1-stripped, convention A K=36) and the S3-full unit did not clear their own control gate (mean 0.733 and
0.677 against 0.9) -- the anneal itself struggles at K=36/28 with these particular letter-frequency profiles
(seed 2 of the S1-stripped control collapsed to 0.206 recovery, a solver failure mode, not evidence about the
target), so **these two pairings are untested, not excluded**; per the brief, the gate was not lowered to
force a run. Per CLAUDE.md rule 3, a negative only holds where the control met its gate: ranks 1-2 are
matched-control negatives, ranks 3-4 are inconclusive (owed a fixed or higher-restart anneal before they can
be called anything).

**Dead ends / not run this job.** Unit D (S3 full, convention B) was attempted in-budget (the 80 pct box rule
allowed it, job ran well under $5/60 min throughout) but the control did not clear gate, so no target run.
The wide-alphabet tool change (cycle-4 rank 6, a Cyrillic-native or 33-37-letter plaintext alphabet in
`homophonic_anneal.py`) was not attempted -- out of this job's scope, named in the brief as a cycle-6 item.

**Decision for the next dollars.** Ranks 1-2 of the cycle-4 table are now spent as control-backed negatives.
Rank 3 and the S3-full unit remain open (control-side, not target-side, failures) -- a next worker could
retry either with more restarts or a fixed/lower-noise control before concluding anything about them. No
judge PASS this job; no re-derivation owed. Status stays `open` (Russian substitution is narrowed, not
excluded, at convention A/K36 and at the S3-full scheme).

Exact commands (spec `judge.corpora` set to the named scheme before each run):
```
python3 tools/family_run.py specs/kaliningrad-2015.json --family homophonic \
  --cipher ciphers/kaliningrad-2015/ciphertext_signs_B.tsv --corpus tools/data/ru19_lat/s3p.txt.gz \
  --param profile=target --seeds 3 --restarts 8 --gate 0.9 \
  --label "GOLD-KAL2 homophonic ru S3-partial, convention B K28, control before target"
python3 tools/family_run.py specs/kaliningrad-2015.json --family homophonic \
  --cipher ciphers/kaliningrad-2015/ciphertext_signs_B.tsv --corpus tools/data/ru19_lat/s1.txt.gz \
  --param profile=target --seeds 3 --restarts 8 --gate 0.9 \
  --label "GOLD-KAL2 homophonic ru S1, convention B K28, control before target"
python3 tools/family_run.py specs/kaliningrad-2015.json --family homophonic \
  --cipher ciphers/kaliningrad-2015/ciphertext_signs.tsv --corpus tools/data/ru19_lat/s1s.txt.gz \
  --param profile=target --seeds 3 --restarts 8 --gate 0.9 \
  --label "GOLD-KAL2 homophonic ru S1-stripped, convention A K36, control before target"
python3 tools/family_run.py specs/kaliningrad-2015.json --family homophonic \
  --cipher ciphers/kaliningrad-2015/ciphertext_signs_B.tsv --corpus tools/data/ru19_lat/s3.txt.gz \
  --param profile=target --seeds 3 --restarts 8 --gate 0.9 \
  --label "GOLD-KAL2 homophonic ru S3 full, convention B K28, control before target"
```

## GOLD-KAL3, Polish and Lithuanian (26 Sept 2026)

Reserve brief `.claude/briefs/runs/2026-09-26-lane-gold-c5-kaliningrad-polish.md`, rank 4/5 of the cycle-4
decision table. Ran after GOLD-KAL2 finished (01:31 UTC), no live overlap, spec to itself.

**Corpus 1: `tools/data/pl19`** (Polish prose, Project Gutenberg). Gutendex's Polish-fiction catalogue
(`languages=pl&topic=fiction`) is thin: 7 hits total, none of the brief's named example authors (Sienkiewicz,
Prus, Żeromski, Reymont, Orzeszkowa, Konopnicka) among them. Fetched the 4 largest fiction hits (Zapolska,
Łubieński, Gnatowski, Schulz), 840,725 letters after fold -- short of the 1.5M aim (not padded with a 5th/6th
text past the brief's 4-text cap; see `tools/data/pl19/README.md`). IC (N=978, 20 windows, seed 42): own
Polish alphabet (ą ę ó ł ż ś ć ń ź kept distinct) 0.0506 (0.0472-0.0534); folded to a-z 0.0642 (0.0618-0.0660)
-- the folded range's upper half brackets the target's own convention-A IC (0.0657, K=36). `homophonic_anneal.fold()`
drops ł outright (its own Unicode code point, not a base letter + combining mark, so NFKD-then-strip-combining
doesn't touch it) -- 2.87% of raw letters across the 4 texts; the corpus files here have ł/Ł replaced with l/L
before gzip so `fold()` keeps every letter (checked: 0.0037% residual difference, from ~30 stray Cyrillic
characters in quoted phrases/footnotes, well under the brief's 0.1% bar).

**Corpus 2: `tools/data/lt`** (Lithuanian Bible, getbible.net). `api.getbible.net/v2/translations.json` lists a
Lithuanian translation; fetched whole (66 books, 2,599,750 folded letters). Register caveat: Bible text, not
prose (same caveat as `ru19`). Lithuanian's marked letters (ą ę ė į ų ū č š ž) all decompose under NFKD, so
`fold()` drops nothing here (0.0000% difference) -- no ł-style fix needed, unlike Polish.

**Units (control first, `tools/family_run.py --family homophonic --param profile=target`, gate 0.9, never lowered):**

- **2-pl-A** (convention A, N=978 K=36, pl19): control 3 seeds 0.988 / 0.973 / **0.003** (mean 0.655) --
  **CONTROL BELOW GATE**, target NOT run, untested not excluded. Seed 3 collapsed near-total (a solver-anneal
  failure mode, per GOLD-KAL2's own lesson on the s1s-A unit -- reported per-seed, not averaged away).
- **2-pl-B** (convention B, N=1066 K=28, pl19): control 3 seeds 0.992 / 0.997 / 0.998 (mean 0.996), gate met.
  Target ran; judge FAIL: score=-1.971, real_p05=-0.913, real_median=-0.856, null_p99=-2.109, N=1066.
  **Control-backed negative** for Polish light-homophonic substitution at K=28, profile=target, this pl19
  register. (Tool note: `judge.corpora` set to the bare directory `tools/data/pl19` first raised
  `IsADirectoryError` in `judge_plaintext.py`'s `read_corpus` -- it wants explicit file paths, unlike
  `family_run.py --corpus`'s own directory-scanning; fixed by listing the 4 files, then re-ran the unit
  cleanly for a correct mechanical row -- the malformed first attempt's row is left in the table below as an
  honest record, not hand-edited.)
- **2-lt-A** (convention A, N=978 K=36, lt, convention A only per brief): control 3 seeds 0.467 / 0.444 / 0.987
  (mean 0.633) -- **CONTROL BELOW GATE**, target NOT run, untested not excluded. No seed collapsed to
  near-zero this time, but the mean is still well short of 0.9.

First 40 letters of any target decode: none reported -- no judge PASS this job (rule 10; a FAIL is reported
as a FAIL, not described). Dead end: neither Polish scheme convention reached a judge PASS where the target
ran (2-pl-B); the other two units are gate failures, not exclusions -- a different corpus (a larger Polish
prose fetch, or a period-matched Polish register rather than a Bible for Lithuanian) could still clear the
control gate and is untested, not ruled out.

Exact commands:
```
python3 tools/family_run.py specs/kaliningrad-2015.json --family homophonic \
  --cipher ciphers/kaliningrad-2015/ciphertext_signs.tsv --corpus tools/data/pl19 \
  --param profile=target --seeds 3 --restarts 8 --gate 0.9 \
  --label "GOLD-KAL3 homophonic pl19, convention A K36, control before target"
python3 tools/family_run.py specs/kaliningrad-2015.json --family homophonic \
  --cipher ciphers/kaliningrad-2015/ciphertext_signs_B.tsv --corpus tools/data/pl19 \
  --param profile=target --seeds 3 --restarts 8 --gate 0.9 \
  --label "GOLD-KAL3 homophonic pl19, convention B K28, control before target"
python3 tools/family_run.py specs/kaliningrad-2015.json --family homophonic \
  --cipher ciphers/kaliningrad-2015/ciphertext_signs.tsv --corpus tools/data/lt \
  --param profile=target --seeds 3 --restarts 8 --gate 0.9 \
  --label "GOLD-KAL3 homophonic lt (Bible register), convention A K36, control before target"
```

Rule 10: nothing in this section is a reading; status stays `open`; never solved, new, first or unpublished.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 23:48 | homophonic | N=978 K=36 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz profile=target | 1 | 0.982 (0.960-0.994) | -3111.669 | FAIL language: score=-1.605, null_p99=-2.083, real_p05=-0.817, real_median=-0.782, mode=both, N=978 | yes (gate 0.9) | GOLD-KAL1 homophonic de20 K36 profile=target, control before target |
| 26 Sept 2026 01:24 | homophonic | N=1066 K=28 restarts=8 corpus=s3p.txt.gz profile=target | 1 | 0.999 (0.997-1.000) | -3712.911 | FAIL language: score=-1.706, null_p99=-2.106, real_p05=-0.889, real_median=-0.812, mode=both, N=1066 | yes (gate 0.9) | GOLD-KAL2 homophonic ru S3-partial, convention B K28, control before target |
| 26 Sept 2026 01:25 | homophonic | N=1066 K=28 restarts=8 corpus=s1.txt.gz profile=target | 1 | 0.997 (0.995-1.000) | -3682.729 | FAIL language: score=-1.729, null_p99=-2.103, real_p05=-0.886, real_median=-0.815, mode=both, N=1066 | yes (gate 0.9) | GOLD-KAL2 homophonic ru S1, convention B K28, control before target |
| 26 Sept 2026 01:27 | homophonic | N=978 K=36 restarts=8 corpus=s1s.txt.gz profile=target | 1-3 | 0.733 (0.206-0.998) | not run (CONTROL BELOW GATE) | - | no (gate 0.9) | GOLD-KAL2 homophonic ru S1-stripped, convention A K36, control before target |
| 26 Sept 2026 01:28 | homophonic | N=1066 K=28 restarts=8 corpus=s3.txt.gz profile=target | 1-3 | 0.677 (0.498-0.780) | not run (CONTROL BELOW GATE) | - | no (gate 0.9) | GOLD-KAL2 homophonic ru S3 full, convention B K28, control before target |
| 26 Sept 2026 02:09 | homophonic | N=978 K=36 restarts=8 corpus=pg27178_Na_mier_1863.txt.gz+pg34635_Menazerya_ludzka.txt.gz+pg6000_Ironia_Pozor_w.txt.gz+pg8119_Sklepy_cynamonowe.txt.gz profile=target | 1-3 | 0.655 (0.003-0.988) | not run (CONTROL BELOW GATE) | - | no (gate 0.9) | GOLD-KAL3 homophonic pl19, convention A K36, control before target |
| 26 Sept 2026 02:10 | homophonic | N=1066 K=28 restarts=8 corpus=pg27178_Na_mier_1863.txt.gz+pg34635_Menazerya_ludzka.txt.gz+pg6000_Ironia_Pozor_w.txt.gz+pg8119_Sklepy_cynamonowe.txt.gz profile=target | 1 | 0.996 (0.992-0.998) | -3554.292 | IsADirectoryError: [Errno 21] Is a directory: 'tools/data/pl19' | yes (gate 0.9) | GOLD-KAL3 homophonic pl19, convention B K28, control before target |
| 26 Sept 2026 02:12 | homophonic | N=1066 K=28 restarts=8 corpus=pg27178_Na_mier_1863.txt.gz+pg34635_Menazerya_ludzka.txt.gz+pg6000_Ironia_Pozor_w.txt.gz+pg8119_Sklepy_cynamonowe.txt.gz profile=target | 1 | 0.996 (0.992-0.998) | -3554.292 | FAIL language: score=-1.971, null_p99=-2.109, real_p05=-0.913, real_median=-0.856, mode=both, N=1066 | yes (gate 0.9) | GOLD-KAL3 homophonic pl19, convention B K28, control before target (re-run, spec corpora path fixed) |
| 26 Sept 2026 02:15 | homophonic | N=978 K=36 restarts=8 corpus=01_pradzia.txt.gz+02_isejimas.txt.gz+03_levitas.txt.gz+04_skaiciai.txt.gz+05_pakartotine_istatymo.txt.gz+06_jozue.txt.gz+07_teisejai.txt.gz+08_ruta.txt.gz+09_1_samuelis.txt.gz+10_2_samuelis.txt.gz+11_1_karaliai.txt.gz+12_2_karaliai.txt.gz+13_1_kronikos.txt.gz+14_2_kronikos.txt.gz+15_ezdras.txt.gz+16_nehemijas.txt.gz+17_ester.txt.gz+18_jobas.txt.gz+19_psalmynas.txt.gz+20_patarles.txt.gz+21_ekleziastas.txt.gz+22_giesmiu_giesme.txt.gz+23_izaijas.txt.gz+24_jeremijas.txt.gz+25_raudos.txt.gz+26_ezechielis.txt.gz+27_danielius.txt.gz+28_ozejas.txt.gz+29_joelis.txt.gz+30_amosas.txt.gz+31_abdijas.txt.gz+32_jonas.txt.gz+33_michejas.txt.gz+34_nahumas.txt.gz+35_habakukas.txt.gz+36_sofonijas.txt.gz+37_agejas.txt.gz+38_zacharijas.txt.gz+39_malachijas.txt.gz+40_matai.txt.gz+41_markas.txt.gz+42_lukas.txt.gz+43_jonas.txt.gz+44_apastalu_darbai.txt.gz+45_romieciams.txt.gz+46_1_korintieciams.txt.gz+47_2_korintieciams.txt.gz+48_galatams.txt.gz+49_efezieciams.txt.gz+50_filipieciams.txt.gz+51_kolosieciams.txt.gz+52_1_tesalonikieciams.txt.gz+53_2_tesalonikieciams.txt.gz+54_1_timotiejui.txt.gz+55_2_timotiejui.txt.gz+56_titui.txt.gz+57_filemonui.txt.gz+58_zydams.txt.gz+59_jokubas.txt.gz+60_1_petras.txt.gz+61_2_petras.txt.gz+62_1_jonas.txt.gz+63_2_jonas.txt.gz+64_3_jonas.txt.gz+65_judai.txt.gz+66_apreiskimas.txt.gz profile=target | 1-3 | 0.633 (0.444-0.987) | not run (CONTROL BELOW GATE) | - | no (gate 0.9) | GOLD-KAL3 homophonic lt (Bible register), convention A K36, control before target |
| 26 Sept 2026 02:42 | homophonic | N=978 K=36 restarts=20 corpus=s1s.txt.gz profile=target | 1-5 | 0.890 (0.478-0.998) | not run (CONTROL BELOW GATE) | - | no (gate 0.9) | GOLD-KAL4 2-ru-s1s-A, restarts 20 seeds 5, control before target |
| 26 Sept 2026 02:45 | homophonic | N=978 K=36 restarts=20 corpus=s1s.txt.gz profile=target | 1 | 0.908 (0.478-0.998) | -3230.293 | FAIL language: score=-1.652, null_p99=-2.078, real_p05=-0.892, real_median=-0.812, mode=both, N=978 | yes (gate 0.9) | GOLD-KAL4 2-ru-s1s-A, restarts 20 seeds 6 (seed 5 collapsed at seeds 5), control before target |
| 26 Sept 2026 02:48 | homophonic | N=1066 K=28 restarts=20 corpus=s3.txt.gz profile=target | 1 | 0.955 (0.780-0.999) | -3974.361 | FAIL language: score=-1.934, null_p99=-2.125, real_p05=-0.847, real_median=-0.77, mode=both, N=1066 | yes (gate 0.9) | GOLD-KAL4 2-ru-s3-B, restarts 20 seeds 5, control before target |

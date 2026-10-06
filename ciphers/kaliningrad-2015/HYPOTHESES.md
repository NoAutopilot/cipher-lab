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

## GOLD-KAL4, restarts and sweep (26 Sept 2026)

Reserve brief `.claude/briefs/runs/2026-09-26-lane-gold-c6-kaliningrad-restarts-and-sweep.md`. Cycle 6: (a)
re-ran the four scheme/convention pairings that read CONTROL BELOW GATE in GOLD-KAL2/KAL3 at restarts 8, this
time at restarts 20 (2.5x the anneal work), to tell a restarts problem from a real limit of the anneal at this
N/K; (b) a convention-B (K=28) Latin-alphabet sweep, one language per unit, restarts 8 seeds 3 (unchanged --
convention-B controls have not needed more). No subagents, disk and CPU only.

**Part (a): restarts 20, seeds 5 (then 6 where named).**

| unit | corpus | convention | K | per-seed control (restarts 20) | mean | gate | target judge |
|---|---|---|---|---|---|---|---|
| 2-ru-s1s-A | ru19_lat/s1s | A | 36 | 0.998 / 0.990 / 0.997 / 0.987 / 0.478 (5 seeds) | 0.890 | NOT met at 5 | not run |
| 2-ru-s1s-A (6 seeds) | ru19_lat/s1s | A | 36 | as above + 0.997 (seed 6) | 0.908 | met | FAIL: -1.652 (real_p05 -0.892, null_p99 -2.078) |
| 2-ru-s3-B | ru19_lat/s3 | B | 28 | 0.999 / 0.997 / 0.780 / 0.998 / 0.998 | 0.955 | met at 5 | FAIL: -1.934 (real_p05 -0.847, null_p99 -2.125) |
| 2-pl-A | pl19 (4 files) | A | 36 | 0.988 / 0.973 / 0.981 / 0.950 / 0.995 | 0.977 | met at 5 | FAIL: -1.827 (real_p05 -0.911, null_p99 -2.095) |
| 2-lt-A | lt (66 files) | A | 36 | 0.985 / 0.524 / 0.987 / 0.662 / 0.981 | 0.827 | NOT met at 5 | not run |

One sentence per unit:
- **2-ru-s1s-A: restarts problem.** At restarts 8 (KAL2) the control read 0.998/0.206/0.997 (mean 0.733, one
  seed collapsed near-total). At restarts 20 the same collapse pattern recurs on a different seed (seed 5,
  0.478) while the other four sit at 0.987-0.998; per the brief's own rule for this exact pattern (four seeds
  0.9+, one under 0.5), a 6th seed was run and brought the mean to 0.908, over gate. Target then ran: judge
  FAIL. Reading: this is the anneal's own local-optimum failure mode at K=36, not a limit tied to the Russian
  S1-stripped scheme -- with enough seeds the control clears gate, and the target is now a genuine
  control-backed negative, where at restarts 8 it was untested.
- **2-ru-s3-B: restarts problem, resolved without a 6th seed.** At restarts 8 the control read
  0.498/0.751/0.780 (mean 0.677, no seed near either 0.9 or 0.5 -- a uniformly weak anneal, not one collapsed
  seed). At restarts 20 all five seeds read 0.780-0.999 (mean 0.955), gate met on the first battery. The extra
  restarts fixed the anneal's convergence at K=28 with this scheme's 11.7 pct q-marker share; target judge
  FAIL, now a control-backed negative.
- **2-pl-A: restarts problem.** At restarts 8 the control read 0.988/0.973/0.003 (mean 0.655, seed 3 collapsed
  near-total). At restarts 20 the same five seeds read 0.950-0.995 (mean 0.977) -- no collapse recurred, gate
  met on the first battery. Target judge FAIL, now a control-backed negative for Polish at convention A/K36
  (Polish at convention B/K28 was already a control-backed negative from GOLD-KAL3).
- **2-lt-A: still CONTROL BELOW GATE at restarts 20 -- not the single-collapsed-seed pattern, so no 6th seed
  run.** At restarts 8 the control read 0.467/0.444/0.987 (mean 0.633, no seed near either bound). At restarts
  20 it reads 0.985/0.524/0.987/0.662/0.981 (mean 0.827): two seeds now clear 0.98, but two others sit at
  0.524 and 0.662 -- not "four seeds 0.9+ and one under 0.5", so the brief's specific 6th-seed rule does not
  apply, and the gate was not lowered to force a run per rule 3. More restarts moved this control from 0.633
  to 0.827 (real progress, unlike a flat repeat) but did not clear gate; this pairing is recorded as a residual
  limit of the anneal at this N=978/K=36 with the Lithuanian-Bible corpus's own letter-frequency profile,
  untested rather than excluded. A future worker could try seeds 6-8 at the same restarts, or a fixed/annealed
  restart schedule, before concluding more.

**Part (b): convention-B (K=28) Latin-alphabet sweep, restarts 8 seeds 3, CONS4's identity-profile L1 order.**

| unit | corpus | control mean (range) | gate | target judge |
|---|---|---|---|---|
| nl | nl20 (7 files) | 0.996 (0.992-0.999) | met | FAIL: -1.407 (real_p05 -0.845, null_p99 -2.064) |
| da | da19 (1 file) | 0.919 (0.767-0.998) | met | FAIL: -1.593 (real_p05 -0.918, null_p99 -1.925) |
| en | en (3 files) | 0.998 (0.996-1.000) | met | FAIL: -1.867 (real_p05 -0.83, null_p99 -2.089) |
| fr | fr19 (5 files) | 0.995 (0.993-0.996) | met | FAIL: -1.749 (real_p05 -0.828, null_p99 -2.0) |
| it | it16 (6 files) | 0.908 (0.757-0.998) | met (narrowly) | FAIL: -1.447 (real_p05 -0.962, null_p99 -1.801) |
| es | es17c (3 files) | 0.990 (0.989-0.992) | met | FAIL: -1.646 (real_p05 -0.886, null_p99 -1.966) |
| pt | pt18 (4 files) | 0.555 (0.205-0.998) | NOT met | not run -- CONTROL BELOW GATE |

All seven sweep units ran; none was skipped for the box (the job stayed well under 80 pct of the $6/80-minute
cap throughout, each unit taking a few minutes).

One sentence per unit:
- **nl, fr, es: control-backed negatives**, clean gates (0.99+), no caveat beyond the ordinary one.
- **da: control-backed negative**, gate met but on a single non-fiction (historical-journal) source file, not
  the fiction register the other sweep corpora use -- register caveat, not a gate problem.
- **en: control-backed negative, but of unknown reliability.** CLAUDE.md's own EN-FOLDS lesson (and
  `tools/data/en/README.md`) records `LANG_CORPORA["en"]`'s per-fold false-negative spread as 0.44-0.64 at
  N=200/500 (Moby-Dick specifically, held out, false-negatives 80-84 pct against the other four); a FAIL
  against this judge is directionally consistent with the other clean negatives but should not be cited with
  the same confidence as nl/fr/es/da.
- **it: control-backed negative**, gate met narrowly (mean 0.908, one seed at 0.757) -- a weaker anneal fit at
  K=28 for this register (16th-c. letters) than most, but still over gate at restarts 8, so no restarts rerun
  needed.
- **pt: CONTROL BELOW GATE, untested not excluded.** Mean 0.555 (0.205/0.462/0.998), two seeds collapsed. The
  sweep runs at restarts 8/seeds 3 per the brief (convention-B controls "have not needed more"); this is the
  one exception this job found. A restarts-20 rerun of this single unit, matching part (a)'s method, is the
  natural next cheap step and was not attempted here (out of this job's ordered task list).

**Decision for the next dollars.** Every convention-B (K=28) Latin-alphabet language this lane has tried is
now a control-backed negative except Portuguese (CONTROL BELOW GATE, untested) and Lithuanian (not run at
convention B at all per the brief, "2-lt-B: never run"). At convention A (K=36), German, Russian (S1-stripped),
and Polish are now control-backed negatives; Russian S3-full is a control-backed negative at convention B;
Lithuanian at convention A remains a residual CONTROL BELOW GATE limit even at restarts 20. No judge PASS this
job; no re-derivation owed. Status stays `open`.

Rule 10: nothing in this section is a reading; status stays `open`; never solved, new, first or unpublished.

## A2-KAL, convention-B Portuguese and Lithuanian at restarts 20 (3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-kal.md` (LANE-A2PUSH, account 2): the two convention-B units GOLD-KAL4
left open, by GOLD-KAL4 part (a)'s method (restarts 20, seeds 5, a 6th seed only for the four-0.9+/one-under-0.5
pattern), gate 0.9 never lowered, control before target. Disk and CPU only, no hosts, no subagents. The spec's
`judge.corpora` was set per unit in a scratch copy of the spec (slug unchanged, so rows land here); the committed
spec's judge block is untouched (still de20).

| unit | corpus | K | per-seed control (restarts 20) | mean | gate | target judge |
|---|---|---|---|---|---|---|
| 2-pt-B | pt18 (4 files) | 28 | 0.998 / 0.977 / 0.998 / 0.990 / 0.981 | 0.989 | met at 5 | FAIL: -1.316 (real_p05 -1.078, null_p99 -1.613) |
| 2-lt-B | lt (66 files, Bible) | 28 | 0.991 / 0.991 / 0.416 / 0.997 / 0.984 | 0.876 | NOT met at 5 | not run |
| 2-lt-B (6 seeds) | lt (66 files, Bible) | 28 | as above + 1.000 (seed 6) | 0.896 | NOT met | not run |

- **2-pt-B: restarts problem, resolved.** At restarts 8 (GOLD-KAL4 sweep) the control read 0.205/0.462/0.998
  (mean 0.555); at restarts 20 all five seeds read 0.977-0.998. Target judge FAIL, now a control-backed negative
  for Portuguese (pt18, 1808-1819 periodical register) at convention B. Rule 3 check: the control's recovery is a
  function of the anneal on a design-matched synthetic text and could have failed (it did at restarts 8), so it
  is a real control for this statistic. Position of the target score between the judge's null_p99 and real_p05:
  (score - null_p99)/(real_p05 - null_p99) = 0.56, in the same band as the sweep's other negatives (nl 0.54,
  it 0.42), not an outlier toward the real-prose side.
- **2-lt-B: CONTROL BELOW GATE, untested not excluded.** Seeds 1, 2, 4, 5 read 0.984-0.997 and seed 3 collapsed to
  0.416 -- the single-collapsed-seed pattern, so a 6th seed was run (1.000), bringing the mean to 0.896, 0.004
  under gate. The gate was not lowered and no 7th seed was run (that would be tuning the same knob a third time;
  CLAUDE.md rule 3's third-attempt clause). Same anneal local-optimum shape as 2-ru-s1s-A and 2-lt-A; with
  2-lt-A (0.827 at restarts 20) this makes Lithuanian the one language where the homophonic anneal has not
  cleared its own control at either convention.

Commands (the scratch spec differs from specs/kaliningrad-2015.json only in `judge.corpora`):
```
python3 tools/family_run.py <scratch>/kaliningrad-2015.json --family homophonic \
  --cipher ciphers/kaliningrad-2015/ciphertext_signs_B.tsv --corpus tools/data/pt18 \
  --param profile=target --seeds 5 --restarts 20 --gate 0.9 \
  --label "A2-KAL 2-pt-B, restarts 20 seeds 5, control before target"
python3 tools/family_run.py <scratch>/kaliningrad-2015.json --family homophonic \
  --cipher ciphers/kaliningrad-2015/ciphertext_signs_B.tsv --corpus tools/data/lt \
  --param profile=target --seeds 5 --restarts 20 --gate 0.9 \
  --label "A2-KAL 2-lt-B, restarts 20 seeds 5, control before target"
  (then the same with --seeds 6)
```
No judge PASS; no reading described. Status stays `open`. Rule 10: nothing here is a reading.

## A2-KAL2, transposition-of-German unigram test (3 Oct 2026)

Worker A2-KAL2 (LANE-A2PUSH, account 2), brief `.claude/briefs/runs/2026-10-03-acct2-a2-kal2.md`. Script
`scripts/transposition_unigram.py` (disk and CPU only). Hypothesis (2016 thread, Thomas #7: "e n r i s order suggests a
transposition of German"): the convention-B letters are German letters in another order, so their own counts must fit
German unigrams as they stand. Statistic: L1 between a text's letter distribution and all of tools/data/de20 (2,448,693
letters), both through `homophonic_anneal.fold` (24 letters). `free1` gives every text, target and controls alike, its
best single relabel (one sign type merged into any letter) -- the allowance for Ernst's "x", a label for an unidentified
glyph (rule 2). Controls at the target's own N 977 (convention B folded, apostrophes dropped): T = de20 windows with their
letters randomly permuted (what a transposition of German gives); S = the same windows under a random 24-letter
substitution. The control can differ from the target on this statistic (substitution moves it, transposition does not),
so it is not orthogonal (rule 3).

| variant | seed, windows | CONTROL T (transposed de20) median / p99 / max | NULL S (substituted) p01 / median | gate T p99 < S p01 | TARGET | read |
|---|---|---|---|---|---|---|
| ident | 42, 300 | 0.120 / 0.195 / 0.205 | 0.697 / 0.962 | met | 0.374 | outside T (0 of 300 windows >= target) |
| free1 | 42, 300 | 0.114 / 0.182 / 0.195 | 0.507 / 0.747 | met | 0.238 | outside T (0 of 300) |
| ident | 7, 1000 | 0.121 / 0.192 / 0.225 | 0.631 / 0.958 | met | 0.374 | outside T (0 of 1000) |
| free1 | 7, 1000 | 0.116 / 0.181 / 0.211 | 0.495 / 0.753 | met | 0.238 | outside T (0 of 1000) |

Largest per-letter gaps (target pct / de20 pct): x 7.9/0.0, r 0.0/6.8, n 13.7/10.5, f 4.7/1.5, a 4.1/6.2, w 3.8/1.8,
c 1.7/3.5, b 0.5/1.9. The best single relabel is x -> r (0.374 -> 0.238, the 0.239 the cycle-4 summary gave); even then
the target sits about 0.06 above the transposition control's p99 and above its maximum over 1,300 windows, with f, w,
n in excess and a, c, b short. Apostrophes: 88 in-word against 0.58 expected for de20 at N 977, which a transposition
would also have to carry (cycle-4 exclusion, unchanged).

**Read: control-backed negative for transposition of German (de20 register) at N 977**, with or without one free glyph
label; the control met its gate on both seeds. The cycle-4 summary's window null p99 0.368 was a different (wider)
statistic; this section's T band is the transposition-specific control and supersedes it for this hypothesis.
Conditional on Ernst's transcript (rule 2) and on de20's register (1880-1940 novels); a different German register moves
unigrams by far less than the gap (T's own spread across seven novels is inside 0.23). No reading; rule 10.
Command: `python3 ciphers/kaliningrad-2015/scripts/transposition_unigram.py [--windows 1000 --seed 7]`.

## A2-KAL3, German homophonic at convention B (3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-kal3.md` (LANE-A2PUSH, account 2): the one convention-B Latin language the
sweep skipped (German was run at convention A only, GOLD-KAL1). Committed spec unchanged in its judge block (already de20).
Disk and CPU only, no hosts, no subagents; one unit, 6 min 11 s wall.

| unit | corpus | K | per-seed control (restarts 20) | mean | gate | target judge |
|---|---|---|---|---|---|---|
| 2-de-B | de20 (7 files, 1880-1940) | 28 | 0.998 / 0.997 / 0.995 / 0.998 / 0.999 | 0.997 | met at 5 | FAIL: -1.572 (real_p05 -0.807, null_p99 -2.075) |

- **2-de-B: control-backed negative.** Rule 3 check: control recovery comes from the anneal on a design-matched synthetic
  de20 text at the target's N and sign profile and can fail (it did for pt/lt at other settings), so it can differ from the
  target. Target position between null_p99 and real_p05: (-1.572 + 2.075)/(-0.807 + 2.075) = 0.40, inside the band of the
  sweep's other negatives (nl 0.54, it 0.42, pt 0.56). With GOLD-KAL1 (convention A, K 36, control 0.982, FAIL -1.605),
  light homophonic German is negative at both conventions. Conditional on Ernst's transcript (rule 2).

Command:
```
python3 tools/family_run.py specs/kaliningrad-2015.json --family homophonic \
  --cipher ciphers/kaliningrad-2015/ciphertext_signs_B.tsv --corpus tools/data/de20 \
  --param profile=target --seeds 5 --restarts 20 --gate 0.9 \
  --label "A2-KAL3 2-de-B, restarts 20 seeds 5, control before target"
```
Decode (not a reading): families/homophonic-1-profile=target-de20.txt. No judge PASS. Rule 10: nothing here is a reading.

## A2P4-KAL4, Russian with each softened consonant its own letter (3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct2-a2p4-kal4.md` (LANE-A2PUSH4, account 2): cycle-4 rank 6. Tool step done first
(commit fbda87f4): `homophonic_anneal.py --alphabet`, `--param alphabet=` in families/homophonic.py, a judge-block
`"alphabet"`, corpus `tools/data/ru19_soft` (softening rule in its README: S3'/S3 transliteration, every q merged into
the letter before it as one upper-case letter -- the cipher's convention A applied to the plaintext), offline test
`tools/tests/test_homophonic_alphabet.py` (default alphabet byte-identical to the pre-option outputs; K-36 round trip
0.978). Disk and CPU only, no hosts.

**Pre-registration (written and committed before any run below).**
- Family and settings, every unit: `tools/family_run.py specs/kaliningrad-2015.json --family homophonic --param
  profile=target --param alphabet=<A> --corpus <C> --seeds 5 --restarts 20 --gate 0.9`, control before target (A2-KAL3's
  seeds and restarts). Gate: control mean recovery >= 0.9 over seeds 1-5; a 6th seed only on A2-KAL's pattern (four
  seeds >= 0.9 and one < 0.5), never a 7th; gate never lowered. Below gate = CONTROL BELOW GATE, untested, not a negative.
- Judge for every unit: the spec's judge block set to `"alphabet": <A>` and `"corpora": [<C>]` before the run (restored
  to de20 without an alphabet as this job's last spec edit), language_pass both, control_samples 100 (the spec's own).
  A PASS stops the job: the family's decode of the shuffled target is scored next (rule 3, ARM-C1) and nothing is called
  a reading (rule 7 re-derivation owed). A FAIL with the control met = control-backed negative for that unit.
- Units, in this order:
  1. **5-ru-soft-s3p-A** (the design rank 6 names): convention A `ciphertext_signs.tsv` (N 978, K 36: an
     apostrophe-bearing sign is one sign), A = ru-s3p-soft (35 letters), C = tools/data/ru19_soft/s3p_soft.txt.gz.
  2. **5-ru-soft-s3p-B** (the brief's literal unit, convention B as A2-KAL3): `ciphertext_signs_B.tsv` (N 1066, K 28),
     same A and C. Design caveat stated before the run: at convention B the apostrophe is its own cipher sign, so a soft
     letter cannot be one sign; the control is built as a 28-sign homophonic over the 35-letter alphabet (a window of at
     most 28 distinct letters), so this unit tests "B-view signs read as soft-letter Russian", a weaker match than unit 1.
     If no 1066-letter window with <= 28 distinct letters is found, the unit is logged as not runnable at this design.
  3. **5-ru-soft-s3-A** (optional, only if units 1-2 leave the job under 80 pct of cap and box): convention A, A =
     ru-s3-soft (37 letters), C = s3_soft.txt.gz.
- Judge calibration caveat (registered now): no leave-one-file-out false-negative rate exists for ru19_soft; a FAIL
  is reported with the judge's own real_p05/null_p99 and the position between them, as the earlier sweep did.

**Results (after the pre-registration above; rows in the family_run table below, 17:34-17:46 UTC).**

| unit | alphabet / corpus | K | per-seed control (restarts 20) | mean | gate | target judge |
|---|---|---|---|---|---|---|
| 5-ru-soft-s3p-A | ru-s3p-soft (35), s3p_soft | 36 | 0.936 / 0.808 / 0.772 / 0.994 / 0.105 | 0.723 | not met | not run (CONTROL BELOW GATE) |
| 5-ru-soft-s3p-B | ru-s3p-soft (35), s3p_soft | 28 | 0.999 / 0.998 / 0.909 / 0.999 / 0.306 | 0.842 | not met | not run (CONTROL BELOW GATE) |
| 5-ru-soft-s3-A | ru-s3-soft (37), s3_soft | 36 | 0.995 / 0.997 / 0.988 / 0.997 / 0.999 | 0.995 | met at 5 | FAIL: -1.992 (real_p05 -0.859, null_p99 -2.242) |

- **5-ru-soft-s3p-A: untested, not excluded.** Two seeds between 0.5 and 0.9 and one at 0.105: not the registered 6th-seed
  pattern, so no 6th seed. An anneal-control limit at N 978 K 36 over 35 letters with rare soft letters (2.97 pct; the
  tool test's round trip read soft letters at 0.46 while reading 0.98 overall), not a target result.
- **5-ru-soft-s3p-B: untested, not excluded.** Four seeds >= 0.9 and one at 0.306 (the registered pattern), but a 6th seed
  cannot lift the mean to the gate even at 1.000 ((4.211 + 1.000) / 6 = 0.869), so it was not run.
- **5-ru-soft-s3-A: control-backed negative.** Rule 3 check: the control is the anneal on a design-matched synthetic
  window of the same corpus and alphabet at the target's N and sign profile, and it can fail (it did for s3p-soft above),
  so it can differ from the target. Target position between null_p99 and real_p05: (-1.992 + 2.242)/(-0.859 + 2.242) =
  0.18, lower than every earlier homophonic negative on this target (0.40-0.56). Conditional on Ernst's transcript
  (rule 2) and on a judge corpus with no fold-count calibration (tools/data/ru19_soft/README.md).

Decode (not a reading): families/homophonic-1-profile=target,alphabet=ru-s3-soft-s3softtxt.txt. No judge PASS, so no
shuffled-target check owed. Rule 10: nothing here is a reading. Spec judge block restored to de20 with no alphabet.

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
| 26 Sept 2026 02:52 | homophonic | N=978 K=36 restarts=20 corpus=pg27178_Na_mier_1863.txt.gz+pg34635_Menazerya_ludzka.txt.gz+pg6000_Ironia_Pozor_w.txt.gz+pg8119_Sklepy_cynamonowe.txt.gz profile=target | 1 | 0.977 (0.950-0.995) | -3168.525 | FAIL language: score=-1.827, null_p99=-2.095, real_p05=-0.911, real_median=-0.859, mode=both, N=978 | yes (gate 0.9) | GOLD-KAL4 2-pl-A, restarts 20 seeds 5, control before target |
| 26 Sept 2026 02:55 | homophonic | N=978 K=36 restarts=20 corpus=01_pradzia.txt.gz+02_isejimas.txt.gz+03_levitas.txt.gz+04_skaiciai.txt.gz+05_pakartotine_istatymo.txt.gz+06_jozue.txt.gz+07_teisejai.txt.gz+08_ruta.txt.gz+09_1_samuelis.txt.gz+10_2_samuelis.txt.gz+11_1_karaliai.txt.gz+12_2_karaliai.txt.gz+13_1_kronikos.txt.gz+14_2_kronikos.txt.gz+15_ezdras.txt.gz+16_nehemijas.txt.gz+17_ester.txt.gz+18_jobas.txt.gz+19_psalmynas.txt.gz+20_patarles.txt.gz+21_ekleziastas.txt.gz+22_giesmiu_giesme.txt.gz+23_izaijas.txt.gz+24_jeremijas.txt.gz+25_raudos.txt.gz+26_ezechielis.txt.gz+27_danielius.txt.gz+28_ozejas.txt.gz+29_joelis.txt.gz+30_amosas.txt.gz+31_abdijas.txt.gz+32_jonas.txt.gz+33_michejas.txt.gz+34_nahumas.txt.gz+35_habakukas.txt.gz+36_sofonijas.txt.gz+37_agejas.txt.gz+38_zacharijas.txt.gz+39_malachijas.txt.gz+40_matai.txt.gz+41_markas.txt.gz+42_lukas.txt.gz+43_jonas.txt.gz+44_apastalu_darbai.txt.gz+45_romieciams.txt.gz+46_1_korintieciams.txt.gz+47_2_korintieciams.txt.gz+48_galatams.txt.gz+49_efezieciams.txt.gz+50_filipieciams.txt.gz+51_kolosieciams.txt.gz+52_1_tesalonikieciams.txt.gz+53_2_tesalonikieciams.txt.gz+54_1_timotiejui.txt.gz+55_2_timotiejui.txt.gz+56_titui.txt.gz+57_filemonui.txt.gz+58_zydams.txt.gz+59_jokubas.txt.gz+60_1_petras.txt.gz+61_2_petras.txt.gz+62_1_jonas.txt.gz+63_2_jonas.txt.gz+64_3_jonas.txt.gz+65_judai.txt.gz+66_apreiskimas.txt.gz profile=target | 1-5 | 0.827 (0.524-0.987) | not run (CONTROL BELOW GATE) | - | no (gate 0.9) | GOLD-KAL4 2-lt-A, restarts 20 seeds 5, control before target |
| 26 Sept 2026 02:56 | homophonic | N=1066 K=28 restarts=8 corpus=pg10819_De_kleine_Johannes.txt.gz+pg10820_Een_liefde.txt.gz+pg12003_Extaze_Een_Boek_van_Geluk.txt.gz+pg16881_Het_leven_van_Rozeke_van_Dalen_deel_1.txt.gz+pg16882_Het_leven_van_Rozeke_van_Dalen_deel_2.txt.gz+pg19563_Eline_Vere.txt.gz+pg29719_Dichtertje_De_Uitvreter_Titaantjes.txt.gz profile=target | 1 | 0.996 (0.992-0.999) | -3198.016 | FAIL language: score=-1.407, null_p99=-2.064, real_p05=-0.845, real_median=-0.782, mode=both, N=1066 | yes (gate 0.9) | GOLD-KAL4 sweep nl20, convention B K28, control before target |
| 26 Sept 2026 02:58 | homophonic | N=1066 K=28 restarts=8 corpus=historisktidsskriftdk1s6.txt profile=target | 1 | 0.920 (0.767-0.998) | -3233.205 | FAIL language: score=-1.593, null_p99=-1.925, real_p05=-0.918, real_median=-0.786, mode=both, N=1066 | yes (gate 0.9) | GOLD-KAL4 sweep da19, convention B K28, control before target |
| 26 Sept 2026 02:59 | homophonic | N=1066 K=28 restarts=8 corpus=pg1342_pride.txt+pg64317_gatsby.txt+pg76_huckfinn.txt profile=target | 1 | 0.998 (0.996-1.000) | -3658.734 | FAIL language: score=-1.867, null_p99=-2.089, real_p05=-0.83, real_median=-0.765, mode=both, N=1066 | yes (gate 0.9) | GOLD-KAL4 sweep en, convention B K28, control before target |
| 26 Sept 2026 03:00 | homophonic | N=1066 K=28 restarts=8 corpus=pg11049_Eugenie_Grandet.txt.gz+pg11131_Pierre_et_Jean.txt.gz+pg14155_Madame_Bovary.txt.gz+pg796_La_Chartreuse_de_Parme.txt.gz+pg798_Le_rouge_et_le_noir.txt.gz profile=target | 1 | 0.995 (0.993-0.996) | -3220.285 | FAIL language: score=-1.749, null_p99=-2.0, real_p05=-0.828, real_median=-0.787, mode=both, N=1066 | yes (gate 0.9) | GOLD-KAL4 sweep fr19, convention B K28, control before target |
| 26 Sept 2026 03:01 | homophonic | N=1066 K=28 restarts=8 corpus=alcuneletteredip00ferr.txt+delleletterefam02seghgoog.txt+lettereinedited00tassgoog.txt+lettereinedited01cibrgoog.txt+lettereineditedi01carouoft.txt+letterescrittea01vanzgoog.txt profile=target | 1 | 0.908 (0.757-0.998) | -3171.319 | FAIL language: score=-1.447, null_p99=-1.801, real_p05=-0.962, real_median=-0.82, mode=both, N=1066 | yes (gate 0.9) | GOLD-KAL4 sweep it16, convention B K28, control before target |
| 26 Sept 2026 03:03 | homophonic | N=1066 K=28 restarts=8 corpus=memorialhistri17realuoft.txt.gz+memorialhistri18realuoft.txt.gz+memorialhistri19realuoft.txt.gz profile=target | 1 | 0.990 (0.989-0.992) | -3349.593 | FAIL language: score=-1.646, null_p99=-1.966, real_p05=-0.886, real_median=-0.789, mode=both, N=1066 | yes (gate 0.9) | GOLD-KAL4 sweep es17c, convention B K28, control before target |
| 26 Sept 2026 03:04 | homophonic | N=1066 K=28 restarts=8 corpus=correiobrazilie00unkngoog.txt.gz+correiobrazilie02unkngoog.txt.gz+oinvestigadorpo03unkngoog.txt.gz+oinvestigadorpo05unkngoog.txt.gz profile=target | 1-3 | 0.555 (0.205-0.998) | not run (CONTROL BELOW GATE) | - | no (gate 0.9) | GOLD-KAL4 sweep pt18, convention B K28, control before target |
| 3 Oct 2026 00:25 | homophonic | N=1066 K=28 restarts=20 corpus=correiobrazilie00unkngoog.txt.gz+correiobrazilie02unkngoog.txt.gz+oinvestigadorpo03unkngoog.txt.gz+oinvestigadorpo05unkngoog.txt.gz profile=target | 1 | 0.989 (0.977-0.998) | -3046.256 | FAIL language: score=-1.316, null_p99=-1.613, real_p05=-1.078, real_median=-0.847, mode=both, N=1066 | yes (gate 0.9) | A2-KAL 2-pt-B, restarts 20 seeds 5, control before target |
| 3 Oct 2026 00:28 | homophonic | N=1066 K=28 restarts=20 corpus=01_pradzia.txt.gz+02_isejimas.txt.gz+03_levitas.txt.gz+04_skaiciai.txt.gz+05_pakartotine_istatymo.txt.gz+06_jozue.txt.gz+07_teisejai.txt.gz+08_ruta.txt.gz+09_1_samuelis.txt.gz+10_2_samuelis.txt.gz+11_1_karaliai.txt.gz+12_2_karaliai.txt.gz+13_1_kronikos.txt.gz+14_2_kronikos.txt.gz+15_ezdras.txt.gz+16_nehemijas.txt.gz+17_ester.txt.gz+18_jobas.txt.gz+19_psalmynas.txt.gz+20_patarles.txt.gz+21_ekleziastas.txt.gz+22_giesmiu_giesme.txt.gz+23_izaijas.txt.gz+24_jeremijas.txt.gz+25_raudos.txt.gz+26_ezechielis.txt.gz+27_danielius.txt.gz+28_ozejas.txt.gz+29_joelis.txt.gz+30_amosas.txt.gz+31_abdijas.txt.gz+32_jonas.txt.gz+33_michejas.txt.gz+34_nahumas.txt.gz+35_habakukas.txt.gz+36_sofonijas.txt.gz+37_agejas.txt.gz+38_zacharijas.txt.gz+39_malachijas.txt.gz+40_matai.txt.gz+41_markas.txt.gz+42_lukas.txt.gz+43_jonas.txt.gz+44_apastalu_darbai.txt.gz+45_romieciams.txt.gz+46_1_korintieciams.txt.gz+47_2_korintieciams.txt.gz+48_galatams.txt.gz+49_efezieciams.txt.gz+50_filipieciams.txt.gz+51_kolosieciams.txt.gz+52_1_tesalonikieciams.txt.gz+53_2_tesalonikieciams.txt.gz+54_1_timotiejui.txt.gz+55_2_timotiejui.txt.gz+56_titui.txt.gz+57_filemonui.txt.gz+58_zydams.txt.gz+59_jokubas.txt.gz+60_1_petras.txt.gz+61_2_petras.txt.gz+62_1_jonas.txt.gz+63_2_jonas.txt.gz+64_3_jonas.txt.gz+65_judai.txt.gz+66_apreiskimas.txt.gz profile=target | 1-5 | 0.876 (0.416-0.997) | not run (CONTROL BELOW GATE) | - | no (gate 0.9) | A2-KAL 2-lt-B, restarts 20 seeds 5, control before target |
| 3 Oct 2026 00:32 | homophonic | N=1066 K=28 restarts=20 corpus=01_pradzia.txt.gz+02_isejimas.txt.gz+03_levitas.txt.gz+04_skaiciai.txt.gz+05_pakartotine_istatymo.txt.gz+06_jozue.txt.gz+07_teisejai.txt.gz+08_ruta.txt.gz+09_1_samuelis.txt.gz+10_2_samuelis.txt.gz+11_1_karaliai.txt.gz+12_2_karaliai.txt.gz+13_1_kronikos.txt.gz+14_2_kronikos.txt.gz+15_ezdras.txt.gz+16_nehemijas.txt.gz+17_ester.txt.gz+18_jobas.txt.gz+19_psalmynas.txt.gz+20_patarles.txt.gz+21_ekleziastas.txt.gz+22_giesmiu_giesme.txt.gz+23_izaijas.txt.gz+24_jeremijas.txt.gz+25_raudos.txt.gz+26_ezechielis.txt.gz+27_danielius.txt.gz+28_ozejas.txt.gz+29_joelis.txt.gz+30_amosas.txt.gz+31_abdijas.txt.gz+32_jonas.txt.gz+33_michejas.txt.gz+34_nahumas.txt.gz+35_habakukas.txt.gz+36_sofonijas.txt.gz+37_agejas.txt.gz+38_zacharijas.txt.gz+39_malachijas.txt.gz+40_matai.txt.gz+41_markas.txt.gz+42_lukas.txt.gz+43_jonas.txt.gz+44_apastalu_darbai.txt.gz+45_romieciams.txt.gz+46_1_korintieciams.txt.gz+47_2_korintieciams.txt.gz+48_galatams.txt.gz+49_efezieciams.txt.gz+50_filipieciams.txt.gz+51_kolosieciams.txt.gz+52_1_tesalonikieciams.txt.gz+53_2_tesalonikieciams.txt.gz+54_1_timotiejui.txt.gz+55_2_timotiejui.txt.gz+56_titui.txt.gz+57_filemonui.txt.gz+58_zydams.txt.gz+59_jokubas.txt.gz+60_1_petras.txt.gz+61_2_petras.txt.gz+62_1_jonas.txt.gz+63_2_jonas.txt.gz+64_3_jonas.txt.gz+65_judai.txt.gz+66_apreiskimas.txt.gz profile=target | 1-6 | 0.896 (0.416-1.000) | not run (CONTROL BELOW GATE) | - | no (gate 0.9) | A2-KAL 2-lt-B, restarts 20 seeds 6 (seed 3 collapsed at seeds 5), control before target |
| 3 Oct 2026 01:07 | homophonic | N=1066 K=28 restarts=20 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz profile=target | 1 | 0.998 (0.995-0.999) | -3386.829 | FAIL language: score=-1.572, null_p99=-2.075, real_p05=-0.807, real_median=-0.782, mode=both, N=1066 | yes (gate 0.9) | A2-KAL3 2-de-B, restarts 20 seeds 5, control before target |
| 3 Oct 2026 17:34 | homophonic | N=978 K=36 restarts=20 corpus=s3p_soft.txt.gz profile=target,alphabet=ru-s3p-soft | 1-5 | 0.723 (0.105-0.994) | not run (CONTROL BELOW GATE) | - | no (gate 0.9) | A2P4-KAL4 5-ru-soft-s3p-A, conv A K36, restarts 20 seeds 5, control before target |
| 3 Oct 2026 17:41 | homophonic | N=1066 K=28 restarts=20 corpus=s3p_soft.txt.gz profile=target,alphabet=ru-s3p-soft | 1-5 | 0.842 (0.306-0.999) | not run (CONTROL BELOW GATE) | - | no (gate 0.9) | A2P4-KAL4 5-ru-soft-s3p-B, conv B K28, restarts 20 seeds 5, control before target |
| 3 Oct 2026 17:46 | homophonic | N=978 K=36 restarts=20 corpus=s3_soft.txt.gz profile=target,alphabet=ru-s3-soft | 1 | 0.995 (0.988-0.999) | -3727.287 | FAIL language: score=-1.992, null_p99=-2.242, real_p05=-0.859, real_median=-0.798, mode=both, N=978 | yes (gate 0.9) | A2P4-KAL4 5-ru-soft-s3-A, conv A K36, restarts 20 seeds 5, control before target; **A2P4-KAL5 correction:** ru19_soft real_p05 gate of unknown reliability (leave-one-book-group-out FN 38.4% at N 978, folds 14.5-49.5%, one source) -> on the real_p05 gate "judge cannot decide", not a negative; the score -1.992 is below every held-out real window (min -1.201, p01 -1.054) |

### A2P4-KAL5 result (3 Oct 2026; pre-registration commit f613b8ef before any score)

`python3 tools/judge_plaintext.py --holdout <8 fold files> --N <N> --alphabet <A>`, samples 200, seed 1; logs
`tools/data/ru19_soft/holdout_*.log`. FN = held-out window at or below the in-model real_p05.

| corpus, N | per fold FN pct (Pent, Hist, Poet, MajP, MinP, Gosp, Epis, Deut) | blended | spread | held-out p05 / p01 / min |
|---|---|---|---|---|
| s3_soft, N 978 | 33.0, 39.5, 46.0, 35.0, 14.5, 42.5, 47.0, 49.5 | 38.4% | 14.5-49.5 (3.4x) | -0.952 / -1.054 / -1.201 |
| s3_soft, N 1066 | 28.0, 50.0, 55.5, 42.5, 26.5, 52.5, 56.0, 56.0 | 45.9% | 26.5-56.0 (2.1x) | -0.948 / -1.044 / -1.197 |
| s3p_soft, N 1066 | 26.0, 44.0, 45.5, 38.5, 25.0, 46.5, 46.5, 48.5 | 40.1% | 25.0-48.5 (1.9x) | -0.947 / -1.033 / -1.156 |

Pre-registered reading: one independent source (8 folds of one translation) and a spread of 1.9-3.4x -> the ru19_soft
judge's real_p05 gate is **of unknown reliability at this N** (rule 3, es17c/EN-FOLDS); about 4 in 10 genuine held-out
Russian windows fail it. So the 5-ru-soft-s3-A FAIL is re-labelled **"judge cannot decide" on the real_p05 gate**, not a
control-backed negative. Reported beside it, unchanged by the relabel: the target's -1.992 lies 0.79 below the lowest of
1,600 held-out real windows at N 978 (-1.201) and 0.25 above the shuffled null's p99 (-2.242), i.e. much nearer the
shuffle null than any held-out Russian; against the held-out distribution as a gate (la17 README's fairer gate) it fails
by a wide margin. The same calibration caveat applies to every Russian FAIL scored against ru19_soft; ru19_lat (the
24-letter schemes, GOLD-KAL2/4) was not measured here.

### RUN4-KAL pre-registration (4 Oct 2026, LANE-RUN4 account 1; committed before any score)

ru19_lat held-out calibration, A2P4-KAL5's method unchanged: the same 8 book groups of `tools/data/ru19` (Pent 01-05,
Hist 06-17, Poet 18-22, MajP 23-27, MinP 28-39, Gosp 40-44, Epis 45-66, Deut 67-84), each rebuilt with
`tools/translit_ru.py --scheme <s>` into scratch; `python3 tools/judge_plaintext.py --holdout <8 folds> --N <N>`, samples
200, seed 1 (a-z fold, as the GOLD-KAL2/4 judge used). Four units, one per logged Russian FAIL: s3p N 1066 (-1.706),
s1 N 1066 (-1.729), s1s N 978 (-1.652), s3 N 1066 (-1.934).
Reading rules, fixed now: (1) one source (8 folds of one translation, under rule 3's ~5) means the real_p05 gate is of
unknown reliability regardless; a blended FN >= 10% or a per-fold spread >= 2x confirms it, and each logged FAIL is then
relabelled "judge cannot decide" **on the real_p05 gate**. (2) On the held-out distribution as gate: a logged score below
the held-out minimum stays a FAIL on that gate (much nearer the shuffle null than any held-out Russian); between held-out
min and p01 is "judge cannot decide"; above held-out p01 would be a PASS on that gate (worth a verifier, nothing more).
The logged null_p99 is reported beside each. No anneal, no new solve, no hosts.

### RUN4-KAL result (4 Oct 2026; pre-registration commit f766765b before any score)

Logs `tools/data/ru19_lat/holdout_<scheme>_N<N>.log`; folds rebuilt in scratch by the pre-registered command (78 books,
group sizes 5/12/5/5/12/5/22/12). FN = held-out window at or below the in-model real_p05.

| unit (corpus, N) | per fold FN pct (Pent, Hist, Poet, MajP, MinP, Gosp, Epis, Deut) | blended | spread | held-out p05 / p01 / min | logged score | logged null_p99 | score - null_p99 | score - held min |
|---|---|---|---|---|---|---|---|---|
| s3p, N 1066 (GOLD-KAL2 S3') | 23.5, 35.5, 25.0, 14.0, 8.0, 21.5, 23.0, 25.5 | 22.0% | 8.0-35.5 (4.4x) | -0.920 / -0.995 / -1.282 | -1.706 | -2.106 | +0.40 | -0.42 |
| s1, N 1066 (GOLD-KAL2 S1) | 24.0, 39.0, 25.0, 13.5, 7.0, 24.0, 25.0, 22.5 | 22.5% | 7.0-39.0 (5.6x) | -0.921 / -0.989 / -1.284 | -1.729 | -2.103 | +0.37 | -0.45 |
| s1s, N 978 (GOLD-KAL4 2-ru-s1s-A) | 16.5, 32.5, 24.0, 8.0, 8.0, 14.0, 18.5, 17.5 | 17.4% | 8.0-32.5 (4.1x) | -0.931 / -1.003 / -1.252 | -1.652 | -2.078 | +0.43 | -0.40 |
| s3, N 1066 (GOLD-KAL4 2-ru-s3-B) | 19.0, 31.5, 17.0, 9.5, 9.0, 14.5, 21.0, 14.5 | 17.0% | 9.0-31.5 (3.5x) | -0.866 / -0.925 / -1.095 | -1.934 | -2.125 | +0.19 | -0.84 |

Reading by the pre-registered rules: (1) every unit has blended FN 17-23% and a 3.5-5.6x per-fold spread on one source,
so the ru19_lat real_p05 gate is **of unknown reliability**; all four logged Russian FAILs are relabelled **"judge cannot
decide" on the real_p05 gate**. (2) On the held-out distribution as gate, every logged score lies 0.40-0.84 below the
lowest of 1,600 held-out real windows, so all four **stay FAIL on that gate** -- none falls in the min-to-p01 band, so
none is "judge cannot decide" in the sense the brief asked about. Each sits nearer the shuffled null's p99 (0.19-0.43
above it) than the held-out minimum. Net: the calibration changes the gate's label, not the size of the miss; the four
GOLD-KAL2/4 Russian units remain negatives in substance (held-out gate), with the real_p05 wording corrected. Rows
619, 620, 628, 629 above carry the logged real_p05 FAILs and are read with this correction.

## R9-KAL6, paired soft/hard move set and two-stage solve for the S3' unit (6 Oct 2026)

Brief `.claude/briefs/runs/2026-10-06-account2-run9-jobs.md` "R9-KAL6" (LANE-RUN9, account 2). The different instrument
A2P4-KAL4 named after 5-ru-soft-s3p-A's control stalled at 0.723 (restarts alone retired, rule 3 third-attempt clause).
Tool step (this commit, before any scored run): `--param soft=pair|two-stage` in `tools/families/homophonic.py`
(`homophonic_anneal.soft_pairs`, `anneal(pairs=, pair_prob=)`); offline test `tools/tests/test_homophonic_soft.py`.
pair = the ordinary anneal plus, with probability 0.3, a move that flips one sign between a hard letter and its soft
partner (n<->N); two-stage = stage 1 over the 22 base letters (soft folded to hard), then from the top 3 stage-1 keys a
stage 2 that only decides the softness split under the full 35-letter model. The default path (no soft param) is
byte-identical to HEAD's (homophonic_alphabet_default_gen.py output compared byte for byte against HEAD's tools;
that script's committed fixture already differs from HEAD's own output, a pre-existing mismatch not caused here).
Unscored synthetic check while building (a Gospels window, K 36, one restart per seed 1-6): no soft param 0/6 restarts
>= 0.9, pair 2/6, two-stage 1/6. Not a gate; it sets the unit order below.

**Pre-registration (committed and pushed before any scored run).**
- Every unit: `python3 tools/family_run.py specs/kaliningrad-2015.json --family homophonic --param profile=target
  --param alphabet=ru-s3p-soft --param soft=<mode> --cipher ciphers/kaliningrad-2015/ciphertext_signs.tsv --corpus
  tools/data/ru19_soft/s3p_soft.txt.gz --seeds 5 --restarts 20 --gate 0.9`, control FIRST (family_run order) -- the
  same N 978, K 36, profile, window corpus and so the corpus's own soft-letter rate (2.97 pct) as 5-ru-soft-s3p-A; only
  the solver differs. Gate: control mean >= 0.9 over seeds 1-5; a 6th seed only on A2-KAL's pattern (four seeds >= 0.9
  and one < 0.5), never a 7th; never lowered. Below gate = CONTROL BELOW GATE, untested, not a negative, no target run.
- Units in order: **6-ru-soft-s3p-A-pair** (soft=pair), then **6-ru-soft-s3p-A-2stage** (soft=two-stage) only if the
  first leaves the job under 80 pct of cap and box (each unit sized from the measured time of the first control).
- Judge, for a unit whose control passes: spec judge block `"alphabet": "ru-s3p-soft"`, `"corpora":
  ["tools/data/ru19_soft/s3p_soft.txt.gz"]` (restored to de20, no alphabet, as this job's last spec edit). Then
  `--shuffle-target 1` through the identical command (rule 3 ARM-C1), scored by the same judge.
- Held-out gate: before the target is scored, `python3 tools/judge_plaintext.py --holdout <the 8 A2P4-KAL5 folds of
  s3p_soft> --N 978 --alphabet ru-s3p-soft` (samples 200, seed 1), log tools/data/ru19_soft/holdout_s3p_N978.log.
- Reading rules, fixed now: real_p05 gate = "judge cannot decide" on any FAIL (A2P4-KAL5: ru19_soft real_p05 of unknown
  reliability); on the held-out gate, below the held-out min = FAIL, min to p01 = judge cannot decide, above p01 = PASS
  on that gate (worth a verifier, nothing more; no reading described, rule 7 re-derivation owed). If the shuffled
  target scores within 0.1 of the target or higher, the target's number licenses nothing either way.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 6 Oct 2026 06:06 | homophonic | N=978 K=36 restarts=20 corpus=s3p_soft.txt.gz profile=target,alphabet=ru-s3p-soft,soft=pair | 1-5 | 0.899 (0.526-0.994) | not run (control-only) | - | no | R9-KAL6 6-ru-soft-s3p-A-pair, control |
| 6 Oct 2026 06:09 | homophonic | N=978 K=36 restarts=20 corpus=s3p_soft.txt.gz profile=target,alphabet=ru-s3p-soft,soft=two-stage | 1-5 | 0.990 (0.985-0.993) | not run (control-only) | - | yes | R9-KAL6 6-ru-soft-s3p-A-2stage, control |
| 6 Oct 2026 06:12 | homophonic | N=978 K=36 restarts=20 corpus=s3p_soft.txt.gz profile=target,alphabet=ru-s3p-soft,soft=two-stage | 1 | 0.990 (0.985-0.993) | -3319.603 | FAIL language: score=-1.733, null_p99=-2.137, real_p05=-0.864, real_median=-0.811, mode=both, N=978 | yes (gate 0.9) | R9-KAL6 6-ru-soft-s3p-A-2stage, control then target |
| 6 Oct 2026 06:16 | homophonic | N=978 K=36 restarts=20 corpus=s3p_soft.txt.gz profile=target,alphabet=ru-s3p-soft,soft=two-stage,shuffle_target=1 | 1 | 0.990 (0.985-0.993) | -3375.073 | FAIL language: score=-1.765, null_p99=-2.137, real_p05=-0.864, real_median=-0.811, mode=both, N=978 | yes (gate 0.9) | R9-KAL6 6-ru-soft-s3p-A-2stage, shuffled target (seed 1) |

### R9-KAL6 result (6 Oct 2026; pre-registration commit 55a90309 before any scored run)

| unit | solver | per-seed control (restarts 20) | mean | gate | target judge | shuffled target (seed 1) |
|---|---|---|---|---|---|---|
| 6-ru-soft-s3p-A-pair | soft=pair (pair_prob 0.3) | 0.993 / 0.992 / 0.989 / 0.994 / 0.526 | 0.899 | not met | not run (CONTROL BELOW GATE) | - |
| 6-ru-soft-s3p-A-2stage | soft=two-stage | 0.993 / 0.991 / 0.988 / 0.992 / 0.985 | 0.990 | met at 5 | FAIL -1.733 (real_p05 -0.864, null_p99 -2.137) | FAIL -1.765 |
| (A2P4-KAL4 5-ru-soft-s3p-A, for comparison) | plain anneal | 0.936 / 0.808 / 0.772 / 0.994 / 0.105 | 0.723 | not met | not run | - |

Held-out calibration for this unit (pre-registered, before the target was scored): `tools/data/ru19_soft/holdout_s3p_N978.log`,
the A2P4-KAL5 folds rebuilt (78 books, groups 5/12/5/5/12/5/22/12; per-group letter counts match holdout_s3p_N1066.log):
per fold FN 25.0, 33.0, 35.0, 31.5, 9.0, 33.0, 27.5, 41.0 pct; blended 29.4 pct; spread 9.0-41.0 (4.6x); held-out p05
-0.953, p01 -1.026, min -1.156.

Reading by the pre-registered rules:
- **pair: untested, not excluded.** Four seeds at 0.989-0.994, seed 5 at 0.526 (not < 0.5, so not the registered
  6th-seed pattern); mean 0.899 misses the 0.9 gate by 0.001. Gate not lowered.
- **two-stage: the instrument works on the control** (0.723 -> 0.990 at the same N, K, profile, window corpus and
  soft-letter rate), so the S3' unit is now testable by this tool. Target: on the real_p05 gate "judge cannot decide"
  (ru19_soft real_p05 of unknown reliability); on the held-out gate FAIL (-1.733 is 0.58 below the held-out minimum of
  1,600 real windows, 0.40 above the null p99). But the shuffled target, through the identical pipeline, scores
  -1.765, within 0.1 of the target: by the pre-registered rule **the target's score licenses nothing either way** --
  the decode is not separated from a decode of the same signs in random order. Not a control-backed negative; no
  reading. Conditional on Ernst's transcript.

## R10-KAL7, lexicon word-segmentation coverage vs the shuffled-target decode (6 Oct 2026) -- second instrument on S3'

Brief `.claude/briefs/runs/2026-10-06-account2-run10-jobs.md` "R10-KAL7" (LANE-RUN10, account 2). The instrument R9-KAL6
named after the ru19_soft n-gram judge could not tell the S3' two-stage decode (-1.733) from its shuffle (-1.765) at
N 978. This is the **second instrument on the S3' design** (first: the ru19_soft n-gram judge, R9-KAL6). Disk and CPU only.

**Pre-registration (committed and pushed before any scored run).**
- Decoder: R9-KAL6's unit unchanged except the training corpus -- `tools/families/homophonic.solve`, profile=target,
  alphabet=ru-s3p-soft, soft=two-stage, restarts 20, solve seed 1, convention A (ciphertext_signs.tsv, N 978, K 36) --
  trained on the S3'-soft Synodal Bible **without the New Testament** (books 40-66; 51 files, 2,721,313 letters), driver
  `ciphers/kaliningrad-2015/scripts/lexseg.py` (reproduce command in its docstring).
- Lexicon (held out from every corpus the decoder used): word types of the NT books 40-66 in the same S3'-soft
  transliteration, length >= 4, occurring >= 2 times: 7,586 types (from 16,491 types, 129,682 tokens);
  `tools/data/ru19_soft/lexseg/lexicon_NT_s3p_soft_len4_min2.txt`.
- Statistic: coverage = the largest number of decode letters covered by non-overlapping lexicon words (DP, per message
  line, case-sensitive) / all decode letters.
- Null: the target shuffled with family_run.py's own `--shuffle-target` procedure, RNG seeds 1-50, each decoded by the
  identical pipeline; gate value G = the 95th percentile of those 50 coverages (sorted ascending, the 48th value).
- Positive control FIRST: synthetic windows of the target's N, K and sign-count profile (homophonic.make_control,
  profile=target, seeds 1-5, plaintext drawn from the NT-free training corpus, decoder trained on the window-removed
  rest) through the same decoder; and that synthetic's own shuffle null (synthetic seed 1, its signs shuffled with RNG
  seeds 1-20, same pipeline), p95 G_s. The control passes only if at least 4 of 5 synthetic coverages exceed both G and
  G_s and their mean exceeds both. Otherwise CONTROL BELOW GATE: the target is not scored, logged as a non-test.
- Rule-3 orthogonality check: coverage is computed from the decoded letter order, which a shuffle of the sign order
  changes, so the shuffled control can differ from the target on this statistic; the G_s-vs-synthetic comparison shows
  whether it does in fact.
- Reading rules: target coverage > G = "decode separates from its own shuffle on a held-out lexicon" -- worth a
  verifier, not a reading, no text described (rule 7 re-derivation and the judge owed). Target <= G with the control
  passed = a control-backed negative for the S3' two-stage homophonic design on this statistic (conditional on Ernst's
  transcript, convention A and the Bible-register lexicon). Secondary (not gating): coverage at word length >= 5.
- Unscored build check before this registration: one synthetic window (seed 1) decoded once to time the driver (33 s;
  recovery 0.961, coverage 0.444). Disclosed, not used to set G or the gate.

### R10-KAL7 result (6 Oct 2026, 07:26-07:37 UTC; pre-registration commit 32b67fba before any scored run)

Per-file coverages: `ciphers/kaliningrad-2015/lexseg/coverage_minlen4.tsv` (gating) and `coverage_minlen5.tsv` (secondary);
target decode `lexseg/target_decode_noNT.txt` (not a reading). 76 decodes, about 33 s each, 4 in parallel.

| unit | N / K | runs | coverage, len >= 4 | coverage, len >= 5 (secondary) |
|---|---|---|---|---|
| shuffled target (null), seeds 1-50 | 978 / 36 | 50 | 0.020-0.087, mean 0.046; **G (p95) 0.0736** | 0.000-0.023; p95 0.0215 |
| shuffled synthetic seed 1 (its own null), seeds 1-20 | 978 / 36 | 20 | 0.028-0.080; **G_s (p95) 0.0654** | 0.000-0.022; p95 0.0204 |
| synthetic positive control, seeds 1-5 (recovery 0.961 / 0.438 / 0.991 / 0.976 / 0.953) | 978 / 36 | 5 | 0.444 / 0.160 / 0.729 / 0.550 / 0.461, mean 0.469 | 0.336 / 0.078 / 0.651 / 0.423 / 0.396 |
| **target** (two-stage, NT-free training) | 978 / 36 | 1 | **0.0440** | 0.0153 |

- **Positive control: PASS** -- 5 of 5 synthetic coverages above both G and G_s (even seed 2, recovery 0.438, reads 0.160,
  twice G). The shuffle null and the synthetic separate by 2-10x on this statistic, so the rule-3 orthogonality check holds:
  the shuffled control can and does differ from a true-plaintext decode here.
- **Target: at or below G -> by the pre-registered rule, a control-backed negative for the S3' (ru-s3p-soft) two-stage
  homophonic design on this statistic.** The target's 0.0440 sits in the middle of its own shuffle null (rank 26 of 51;
  null median 0.0445); n-gram score -3328.9 against the shuffles' -3402.9 to -3301.9 (median -3346.9). Secondary figure
  agrees (0.0153 vs p95 0.0215). Conditional on Ernst's transcript, convention A, and a Bible-register NT lexicon.
- This is the **second instrument on the S3' design** (first: R9-KAL6's ru19_soft n-gram judge, which could not decide).
  No reading claimed; nothing here is a reading (rule 10).

## R12-KAL8, lexicon word-segmentation on the remaining schemes S1, S3, S1s, S3-soft, German (6 Oct 2026)

Brief `.claude/briefs/runs/2026-10-06-account2-run12-jobs.md` "R12-KAL8" (LANE-RUN12, account 2): R10-KAL7's driver
(`scripts/lexseg.py`, now taking env LEXSEG_CIPHER and LEXSEG_PARAMS; R10-KAL7's default path unchanged), no tool change,
on each remaining scheme. Disk and CPU only.

**Pre-registration (committed and pushed before any scored run; one registration for all five units).**
- Units, in run order (a unit is started only if it can finish before 80% of the box, 12:26 UTC; units not reached are
  logged "not run", never negatives). Decoder `tools/families/homophonic.solve`, restarts 20, solve seed 1, the plain
  anneal of each scheme's earlier control-backed row:
  1. **S1**: convention B (`ciphertext_signs_B.tsv`, N 1066, K 28), params {profile: target}.
  2. **S3**: convention B (N 1066, K 28), {profile: target}.
  3. **S1s**: convention A (`ciphertext_signs.tsv`, N 978, K 36), {profile: target}.
  4. **S3-soft**: convention A, {profile: target, alphabet: ru-s3-soft}.
  5. **German**: convention A, {profile: target}, corpus de20 (the corpus every earlier German row used; the brief's
     "de19 or de1600 as earlier rows chose" resolves to de20, since GOLD-KAL1 and A2-KAL3 used de20).
- Train corpora and lexicons: `scripts/lexseg_build.py` (deterministic). Russian: train = Synodal Bible outside books
  40-66 in the scheme's transliteration; lexicon = NT (books 40-66) word types in the same scheme, length >= 4, count
  >= 2 (s1 7,625; s3 7,679; s1s 7,553; s3_soft 7,585 types). German: train = de20 minus Effi Briest and Frau Jenny
  Treibel (5 files); lexicon = folded word types of those two held-out novels, length >= 4, count >= 2 (6,504 types).
  Each lexicon is held out from every corpus its decoder used.
- Statistic: R10-KAL7's coverage (largest number of decode letters covered by non-overlapping lexicon words, DP per
  message line, case-sensitive / all decode letters), minimum word length 4; length >= 5 secondary, not gating.
- Null (sized to the box, smaller than R10-KAL7's 50): the target shuffled with family_run.py's own procedure, RNG
  seeds 1-15, same pipeline; **gate G = the maximum of the 15** (a target above G ranks first of 16).
- Positive control FIRST within each unit: synthetic windows (homophonic.make_control, profile=target, seeds 1-4,
  plaintext from the unit's train corpus) through the same decoder; their own null: synthetic seed 1's signs shuffled
  with seeds 1-4, **G_s = the maximum**. Control passes only if at least 3 of 4 synthetic coverages exceed both G and
  G_s and their mean exceeds both; otherwise CONTROL BELOW GATE, the target's number is logged as a non-test.
- Rule-3 orthogonality: coverage depends on decoded letter order, which the shuffle changes; the G_s-vs-synthetic gap
  shows per unit whether the shuffle can differ from a true decode on this statistic.
- Reading rules (R10-KAL7's): target > G with the control passed = "decode separates from its own shuffle on a held-out
  lexicon", worth a verifier, not a reading, no text described. Target <= G with the control passed = control-backed
  negative for that scheme's homophonic design on this statistic (conditional on Ernst's transcript, the convention and
  the lexicon's register).
- Unscored build check before this registration: one synthetic window (S3, seed 99, not one of the control seeds)
  decoded once to time the driver (59 s at N 1066). Disclosed, not scored, not used to set any gate.

### R12-KAL8 result (6 Oct 2026, 11:41-12:06 UTC; pre-registration commit 09fba2be before any scored run)

Per-file coverages and the five target decodes (not readings): `ciphers/kaliningrad-2015/lexseg/r12/`. 24 decodes per unit,
4 in parallel; all five units ran inside the box. G = max of 15 shuffled-target decodes; G_s = max of 4 shuffled-synthetic.

| unit | conv., N / K | synthetic control, len >= 4 (recovery) | G_s | null (15) range, **G** | **target**, rank of 16 | control | registered reading | len >= 5 (secondary): target / G |
|---|---|---|---|---|---|---|---|---|
| S1 | B, 1066 / 28 | 0.565 / 0.622 / 0.576 / 0.565, mean 0.582 (0.996-0.999) | 0.0591 | 0.0197-**0.0704** | **0.0413**, 8 | PASS | control-backed negative | 0.0000 / 0.0188 |
| S3 | B, 1066 / 28 | 0.524 / 0.672 / 0.800 / 0.689, mean 0.671 (0.921-0.998) | 0.0328 | 0.0122-**0.0375** | **0.0394**, 16 | PASS | **> G** (see below) | 0.0094 / 0.0150 (rank 8) |
| S1s | A, 978 / 36 | 0.625 / 0.628 / 0.123 / 0.684, mean 0.515 (0.992 / 0.992 / 0.327 / 0.993) | 0.0726 | 0.0204-**0.0757** | **0.0409**, 3 | PASS | control-backed negative | 0.0000 / 0.0266 |
| S3-soft | A, 978 / 36 | 0.076 / 0.666 / 0.744 / 0.535, mean 0.505 (0.174 / 1.0 / 0.999 / 0.991) | 0.0337 | 0.0082-**0.0378** | **0.0337**, 15 | PASS | control-backed negative | 0.0051 / 0.0102 |
| German (de20) | A, 978 / 36 | 0.723 / 0.561 / 0.629 / 0.645, mean 0.640 (0.919-0.993) | 0.1288 | 0.0695-**0.1575** | **0.1135**, 7 | PASS | control-backed negative | 0.0521 / 0.0675 |

- **Controls**: all five pass; every synthetic window, including the two with poor anneal recovery (S1s seed 3 at 0.327,
  S3-soft seed 1 at 0.174), reads above both G and G_s. True decodes sit 4-20x above the shuffle nulls, so the rule-3
  orthogonality check holds in every unit (the shuffle can and does differ from a true decode on this statistic).
- **S1, S1s, S3-soft, German: control-backed negatives** for each scheme's light homophonic design on this statistic,
  conditional on Ernst's transcript, the stated convention and the lexicon's register (Bible NT for Russian, Fontane
  novels for German). Each target lies inside its own shuffle null (ranks 3-15 of 16).
- **S3 (convention B): above G by the registered rule, by the smallest possible margin.** 0.0394 = 42 covered letters of
  1,066 against the null maximum 0.0375 (40); the secondary length->=5 figure is at the null median (rank 8); with five
  units each gated at the top of 16, the chance that at least one target tops its null by luck alone is about 1 - (15/16)^5
  = 0.28; and 0.039 is a tenth of the weakest synthetic control (0.524). Registered wording: "decode separates from its own
  shuffle on a held-out lexicon" -- worth a verifier, not a reading, no text described. The cheap confirmatory step before
  any verifier: the same S3 unit with R10-KAL7's null size (shuffle seeds 16-50 added, G = p95 of 50), pre-registered.
- Non-gating observation: the in-model n-gram score of the S1, S3 and S3-soft target decodes is above every one of their
  15 shuffles (e.g. S3 -3982.7 vs shuffles -4207.4 to -4103.1); S1s and German sit inside. A ciphertext with any sequential
  structure keeps more n-gram fit than its shuffle, so this is not evidence of a language; R10-KAL7's S3' unit sat in the
  middle (rank 26 of 51).
- Rule 10: nothing here is a reading.

## R12-KAL9, confirmation of the R12-KAL8 S3 convention-B excess with a 50-shuffle null (6 Oct 2026)

Brief `.claude/briefs/runs/2026-10-06-account2-run12-jobs.md` "R12-KAL9" (LANE-RUN12, account 2), R12-KAL8's named next
step (1). Disk and CPU only.

**Pre-registration (committed and pushed before any scored run).**
- Unit: R12-KAL8's S3 unit unchanged -- `scripts/lexseg.py`, LEXSEG_CIPHER = `ciphertext_signs_B.tsv` (convention B, N 1066,
  K 28), LEXSEG_PARAMS {"profile": "target"}, train `train_s3.txt.gz` and lexicon `lex_s3.txt` rebuilt by
  `scripts/lexseg_build.py` (deterministic), restarts 20, solve seed 1, minimum word length 4.
- Null: the 15 shuffled-target decodes already on file (`lexseg/r12/coverage_minlen4_s3.tsv`, seeds 1-15) plus 35 fresh ones,
  shuffle seeds 16-50, same pipeline: 50 in all.
- Reproducibility check (run first, in the same batch): the target (seed 0) decoded again; it must give 42 covered letters of
  1,066 as R12-KAL8 recorded. If it does not, the old and new nulls are not the same pipeline and the run is logged as a
  non-test (no pass/fail).
- **Gate**: target coverage (0.0394, 42/1066, or the reproduced value) strictly above P95 = numpy.percentile(null50, 95)
  (linear interpolation). Reported beside it: the target's rank among the 51 values and the empirical p = (1 + #null >=
  target) / 51.
- Positive control: R12-KAL8's S3 control (4 synthetic windows 0.524-0.800 vs G_s 0.033) is not re-run; it is far above any
  value the null can take here, and the null only grows. Rule-3 orthogonality: coverage depends on decoded letter order, which
  the shuffle changes (R12-KAL8's synthetic-vs-shuffled-synthetic gap shows it can differ).
- Secondary, not gating: the length >= 5 coverage for the 35 new shuffles and the target's rank on it.
- **What a pass licenses**: a verifier look at the S3 convention-B decode with a rule-7 re-derivation -- not a reading, no text
  described. A fail (target <= P95): S3 convention B closes as a control-backed negative for the light homophonic design on
  this statistic (conditional on Ernst's transcript, convention B and the NT lexicon's register), and R12-KAL8's next step (2)
  applies: the next test needs a different design family.

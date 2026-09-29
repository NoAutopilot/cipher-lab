# Debosnys swarm harness (DEB-SWARM-0, 29 Sept 2026)

FROZEN ed4a3743 (score.py blob d80e6baa) 29 Sep 2026 03:14 UTC

(The commit id is the one on origin/main after the rebase; the blob hash of score.py is the check: `git rev-parse HEAD:ciphers/debosnys-1883/swarm/score.py` must start d80e6baa.)

Owned by the harness. Groups read this file, run `score.py`, and write only in `swarm/G-<X>/`. Never edit
`score.py`, `make_controls.py`, `build_corpora.py`, `corpora/`, `vocab/` or `controls/`; a bug goes to ROOM as
"for the orchestrator: DEB-SWARM bug: ...". Never open `controls/sealed/` (only `score.py` reads it). PUBLIC COPIES
ONLY (`../RESTRICTED.md`).

## Texts

`score.py` reads the settled three-pass drafts (`../ciphertext_c1_draft.tsv`, `../ciphertext_c2_draft.tsv`), drops the
non-sign classes `_` and MULTI, drops the clear digits and capitals of `../clear_spans.tsv` (H43), and strips a
trailing `?`. That gives:

| id | lines | signs | notes |
|---|---|---|---|
| c1 | 6 | 132 | 58 sign types |
| c2 | 26 | 658 | c2a = page a, 17 lines, 456 signs; c2b = page b, 9 lines, 202 signs |
| pooled | 32 | 790 | K 136 |

Ids can be joined with `+` (`c1+c2a`). `score.py --list` lists every id.

## Language models (`corpora/`, built by `build_corpora.py`, sources in `corpora/MANIFEST.tsv`)

| lang | corpus (public domain) | years |
|---|---|---|
| fr | Flaubert, *Madame Bovary*; Maupassant, *Pierre et Jean*; Baudelaire, *Les Fleurs du Mal* (verse) | 1857-1888 |
| en | Twain, *Huckleberry Finn* (PG 76); Dickens, *A Tale of Two Cities* (PG 98) | 1859-1884 |
| pt | Camilo Castelo Branco, *Amor de Perdicao* (PG 16425), *Novelas do Minho* (PG 21406) | 1862-1875 |
| es | Valera, *Pepita Jimenez* (PG 17223); Alarcon, *El sombrero de tres picos* (PG 29506) | 1874 |
| la | Zaluski, *Epistolae historico-familiares* t.1 (tools/data/la18) | c.1709: no 1850-1900 Latin prose corpus was at hand; stated, not hidden |

Folding: lower case, accents stripped, a-z only. The verse used for the controls' plaintexts (Hugo, Tennyson,
Camoes) is kept out of these corpora so a control cannot be won by memorising the scorer's own corpus.
The languages are those Debosnys is reported fluent in (Bauer, *Unsolved!*, 2017, via Wikipedia).

**DEB-VOCAB** (`vocab/deb_vocab_base.tsv`, 122 words of 3+ letters): his public clear writing only -- the c3 clear
poem and the c4 title, banner and signature (`../clear_poems.tsv`), the Gaffney English rendering of the Greek verso
poem (`../verso_english_gaffney.txt`), and the signature forms in `../NOTES.md` (H.D. Debosnys, HENRY.D.DEBOSNYS,
Henecos Debosnostys). `score.py` also reads `swarm/G-E/CRIBS.tsv` (first column = word) whenever it exists. The
list may grow; the shuffled controls always use the same list as the real score, so the percentile stays fair.
Nothing from the museum's restricted scans is in it or may be added to it.

## Statistics and nulls

For each language: **quad** = letter-quadgram log10-likelihood per quadgram, counted only inside runs of read signs
(an unread sign breaks the run; a sign keyed to an empty value reads nothing and does not break it); **dict** = the
share of read letters inside a corpus word of 4-12 letters seen 3+ times. **vocab** = the share of read letters
inside a DEB-VOCAB word. Eleven statistics in all.

Each is set against 1000 shuffled keys (seed fixed from the key and text, so a run reproduces):
- `pct`: the brief's null -- the key's values permuted across its signs (value distribution kept);
- `pct_strat`: a **frequency-stratified** null -- values permuted only among key signs in the same band of 6
  consecutive frequency ranks in the scored text.

Why the second null (harness finding, before any group scored): a key made from sign frequency alone -- signs ranked
by count, handed French letters by French letter frequency, no language model at all -- scored **99.9 pct on fr_quad
under the plain null in both held-out directions on the NULL control** (and 97-99.5 in the other four languages).
The plain shuffle breaks the frequency match, so it rewards any frequency-matched key, language or not. Under the
stratified null the same key scores 93.9 and 83.5 on NULL, 77.3 on the real c1->c2. The planted key still scores 100
under both. `pct` = 100 x (shuffles strictly below the real value) / 1000; `beats_all` means 1000 of 1000.

## Controls (`controls/`, built by `make_controls.py`; answers sealed)

All are shaped like c1 and c2: 6 + 26 lines of the same lengths (c2 lines 1-17 = c2a, 18-26 = c2b), N 790, K 136,
signs `S001...` (never Debosnys's ids). Plaintexts: verse, sources in `controls/PLAINTEXT_SOURCES.json`, none in
the scoring corpora.

| id | design | plaintext | top-5 counts (real: 114 46 26 21 20) |
|---|---|---|---|
| FR-HOMO | homophonic letters, count curve = the real pooled curve | Hugo, *Les Contemplations* (1856) | 114 46 26 21 20 |
| EN-HOMO | homophonic letters | Tennyson, *Idylls of the King* | 97 47 26 22 21 |
| PT-HOMO | homophonic letters | Camoes, *Os Lusiadas* (modernised spelling) | 114 46 26 21 20 |
| FR-SYLL | 17 function words + frequent syllables as signs, rarer syllables spelled in letters, one sign per unit | Hugo, a later stretch | 55 51 46 37 34 (flatter top: a syllabary does not reach a 14 pct top sign) |
| NULL | no language: the real pooled sign multiset shuffled into the real line lengths; in about half the couplets the second line ends on the first line's final sign (h8: 5 of 10 couplets agree) | none | 114 46 26 21 20 |
| *-N15 | the same four language controls with 15 pct of tokens replaced by a sign drawn from the curve | as above | see SHAPE.json |

Profile (h3_unit_profile.py's statistics, pooled N 790):

| text | K | hapax | top1 | top5 | IC | doubled | bigram repeat |
|---|---|---|---|---|---|---|---|
| real c1+c2 | 136 | 0.412 | 0.144 | 0.287 | 0.034 | 0.030 | 0.338 |
| FR-HOMO | 136 | 0.412 | 0.144 | 0.287 | 0.034 | 0.018 | 0.357 |
| EN-HOMO | 136 | 0.404 | 0.123 | 0.270 | 0.029 | 0.006 | 0.350 |
| PT-HOMO | 136 | 0.412 | 0.144 | 0.287 | 0.034 | 0.011 | 0.370 |
| FR-SYLL | 136 | 0.353 | 0.070 | 0.282 | 0.026 | 0.010 | 0.482 |
| NULL | 136 | 0.412 | 0.144 | 0.287 | 0.034 | 0.032 | 0.279 |

`score.py KEY --control <id>` gives recovery pct (tokens whose key value equals the sealed unit, folded) on each part
and pooled; it never prints the sealed text. `--fit <id>.c1 --test <id>.c2` runs held-out on a control and adds
`recovery_pct_test`.

**Blind set for group D.** `controls/B1..B5.tsv`: fresh instances of the five designs (other passages, other keys;
the language ones with 15 pct noise, like the real drafts), order sealed in `controls/sealed/BLIND.tsv`. D writes
`swarm/G-D/BLIND_VERDICT.tsv` (`id<TAB>verdict`, verdict NULL or LANGUAGE for each of B1-B5), commits it, and only
then runs `score.py --blind-check swarm/G-D/BLIND_VERDICT.tsv` (refuses an uncommitted or modified file). One check
per verdict file; a second file after seeing the first result is logged as a second attempt.

## The bar (written before any group scored)

**Phase 1 (stepping stone).** The group's method, run blind by a committed script that reads only the control's
ciphertext, reaches **recovery_pct >= 70** on its matching control with `score.py KEY --control <id>`:
A FR-HOMO, B EN-HOMO, C FR-SYLL, G PT-HOMO; F the control of the design its key assumes; H its own Copiale
known-answer control (its brief), and FR-HOMO or the design-matched harness control for any key it scores here. Report the same method on
the `-N15` variant beside it (rule 3: a control must bracket the target's measured 14-18 pct noise); a group may
log a negative on c1/c2 only with its -N15 number beside it. **Group D**: 5 of 5 on `--blind-check`, with the same
test it applies to c1/c2.

**Phase 2 (a claim).** Two key files committed with their scripts before scoring: `KEY_fit_c1.tsv`, made by a script
that reads only c1, and `KEY_fit_c2.tsv`, made reading only c2. Run
`score.py G-X/KEY_fit_c1.tsv --fit c1 --test c2` and `score.py G-X/KEY_fit_c2.tsv --fit c2 --test c1`
(the scorer drops every key sign that does not occur in the fit text). A key passes when, for ONE statistic among
the eleven (fr/en/pt/es/la quad or dict, or vocab), in BOTH directions:
`beats_all` AND `beats_all_strat` (1000 of 1000 under both nulls, i.e. above 99.9), `coverage_test >= 0.50` and
`read_letters >= 60`; and the group's Phase 1 is met. (Under the null, the chance that one of eleven statistics
does this by luck is about 11 x 10^-6.) A pass is a candidate, not a reading: ROOM "candidate" line, stop tuning,
two audits by separate sessions.

**Reachability, measured (read before planning).** A plain homophonic hill-climber (`selftest_climb.py`, French
quadgrams, 6 restarts x 60000 steps) on FR-HOMO:
- fit on c2 (658 signs) -> recovery 25.8 pct; held-out on c1: fr_quad 100.0 / strat 99.6 (just short of beats_all);
- fit on c1 alone (132 signs, 58 types) -> recovery 1.1 pct (pure overfit); held-out on c2: fr_quad 70.9 / 47.5.
So the c1 -> c2 direction is out of reach for a homophonic letter key fitted on c1 alone at this length (h17's
unicity result says the same), even where the answer is known. A correct key does pass it (self-test below). The bar
stays as briefed; if the orchestrator wants a reachable fold bar, `score.py` already takes
`--fit c1+c2a --test c2b` and `--fit c2b --test c1+c2a` (and the same on controls), and that change is the
orchestrator's to make in this file before any group relies on it.

## Self-test (`score.py --selftest`)

Planted key (the sealed FR-HOMO answer, one value per sign) vs a random permutation of it, held-out both ways:

| key | fr_quad pct c1->c2, c2->c1 | recovery on test | passes the bar |
|---|---|---|---|
| planted | 100.0, 100.0 (strat also 1000/1000) | 74.5, 94.7 | yes |
| random | 23.1, 64.1 | 0.9, 0.8 | no |

Further checks (numbers in `SELFTEST.md`): the frequency-only key on NULL (above); the hill-climber on NULL.

## Where this agrees and differs with the earlier runner's controls

- **h17_planted.json** (planted letter keys at c1 size, N 132, K 58: S1 1.0 / 0.96 / 0.65 at noise 0 / 5 / 15 pct,
  each clearing its null p97.5): agrees that a *correct* key at c1 size is detectable -- our planted key beats all
  1000 shuffles at N 132. Differs in strictness: h17's gate is p97.5 on one statistic; ours is 1000/1000 on two
  nulls in two held-out directions.
- **h9_controls.json** (plain letter substitution, K 22-25): those controls fall outside the real K, hapax, top-5, IC
  and bigram-repeat values; ours match K, hapax, top-1, top-5 and IC by construction (homophones spread to the real
  curve), so h9's profile mismatch does not carry over to these homophonic controls. Both show real doubled-sign
  rate (0.030) above the homophonic controls (0.006-0.018) and near NULL (0.032).
- **h13_noise.json** (noise models on the pooled text): our -N15 variants use h13's "coarse" style (replacement by a
  sign drawn from the curve) at 15 pct, inside the measured 14-18 pct band; clean controls are a ceiling, not the
  real case.

## Files

`score.py` (the scorer), `make_controls.py`, `build_corpora.py` (need the Gutenberg texts in a scratch dir, listed
with URLs in the two manifests), `selftest_climb.py` (harness self-test only), `corpora/`, `vocab/`, `controls/`.

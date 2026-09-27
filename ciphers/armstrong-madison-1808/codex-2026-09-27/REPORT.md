# Armstrong, 20 February 1808: reattack, 27 September 2026

**Result: unsolved. No plaintext or target key is claimed.** This work checked the suggested sibling-code route, reconciled specific transcription defects, tested three classes of renumbering, and evaluated a published opening hypothesis. It supplies reproducible research, not a decipherment or an exclusion of nomenclator designs.

## What Bourdeau actually published

[Daniel Bourdeau's Armstrong page](https://dbourdeau.github.io/cyphersolver/armstrong.html) offers a **580-entry reconstructed table** for the regular Armstrong code, conventionally THE=972, with data in `targets/armstrong/pairs.txt`, a decoder, and confidence grades. It is not a complete original codebook. That regular system has roughly 1,600 groups, combining words, syllables, letters and homophones. The author explicitly distinguishes it from the unknown system of 20 February. Its vocabulary is a useful prior; its number-to-word assignments cannot simply be transferred.

This repository already held the 580-entry table, the complete numbered Monroe/John Quincy Adams table WE028, and earlier direct-transfer and vocabulary-prior experiments. Several earlier solvers failed their own controls. Those failures do not exclude a relationship. The present test asks a narrower, independently reproducible question: could the target be a simple systematic renumbering of one of these tables?

## Transcription findings

The source is the [Papers of James Madison target page and manuscript images](https://pjm.as.virginia.edu/john-armstrong-jr-james-madison-20-february-1808), also held under `../images/M34-014-0030.jpg` through `0033.jpg`. Original source files were preserved.

`../ciphertext.txt` has 369 numeric tokens. Three are editorial line counts, not cipher symbols:

| Numeric context in the stored text | Editorial text that introduced it | Correction |
|---|---|---|
| `14 2 ** 44` | 2 lines of symbols | remove this `2` |
| `1801 ** 1 ** ** 78` | 1 line of symbols | remove this `1` |
| `141 ** 1 ** 1130` | 1 line of symbols | remove this `1` |

`ciphertext_editorial_clean.txt` makes only those three deletions: **366 numeric tokens, 216 distinct values**. The companion `target_clean.seq` treats each nonnumeric token as an opaque break. It does not mistake the asterisks for a literal alphabet. This remains an editorially cleaned transcription, not a certified complete reading of the manuscript.

The older `../ciphertext_ms.txt` is not safe as an authoritative replacement: visible groups missing from it include `1840 240` at the start of manuscript page 1 line 2, `44` before `176`, `1761` before `13`, and `671` before `48`. The first stored `1841` appears to read `1843` on the manuscript. The stored `203` near `56 … 38` is also uncertain: a preceding handwritten mark must not silently be absorbed into a number. These issues are flagged, not silently repaired in the clean file. This limits every target experiment below.

## A real crib, but not a verified reading

The earlier repository statement that Krajčovič's Armstrong hypothesis could not be found is outdated/incorrect. It is in his August 2026 comments on [Klaus Schmeh's article](https://klausschmeh.net/can-you-decipher-this-letter-sent-to-u-s-president-james-madison/). Its proposed opening describes the bearer as active, sober, industrious and brave. A genuine [Armstrong-to-Jefferson letter of 15 February 1808](https://rotunda.upress.virginia.edu/founders/default.xqy?keys=FOEA-print-04-01-02-7420&mode=deref) supplies essentially that opening.

That establishes the source of the suggestion, not its truth. The early numeric groups are distinct until `240` repeats. Assigning ten different groups ten plausible words supplies almost no repetition check. The proposed alignment makes `240` mean **of**; immediately after **man**, the real 15 February letter instead has **and**. Thus the unknown letter is not an exact word-for-word copy under those assignments. A paraphrase, spelling components, nulls or a changing key could evade this contradiction, but each needs independent evidence. No target assignment from this crib is promoted to a known-key grade.

The same comments suggest zero-padding equivalences. There are indeed 26 distinct observed pairs `(x, 10x)`. A naive uniform-number baseline understates their chance frequency because both occupied decades and last digits are highly uneven. `padding_test.py` uses 2x2 swaps of occupied decade/units cells, preserving both margins. Across 2,000 retained MCMC draws after burn-in, the mean is **21.58**, the 95th percentile **26**, and the estimated upper-tail probability **0.075**. This is modest evidence at most under this particular null, not proof of plaintext equivalence. The chain is approximate and its draws are dependent. Nor does this test refute equivalence.

## Controlled renumbering screens

The score uses boundary character n-grams learned from the repository's historical English corpus, excluding the Jefferson volume, and the published codebook values. It sums evidence across adjacent numeric tokens; unknown table entries and graphic runs contribute no bridge evidence. It is a ranking score, not a probability that text is correct.

Three transform families were enumerated:

* `digits`: all 10! common decimal digit permutations × 4! position permutations of zero-filled four-digit groups: **87,091,200 candidates per run**.
* `affine`: invertible mappings `a*(c-1)+b mod N`, for N in {1600,1700,1900,2000}, requiring N at least the largest input group. For the target this leaves N=1900 or 2000.
* `grid`: row/column transpositions of rectangular tables of those sizes, columns 2–200 dividing N, both coordinate reversals, and cyclic input offsets. Again no input is wrapped from outside the modulus.

For each table and family, the target was compared with 20 independently shuffled orders preserving all numeric frequencies and graphic-break positions. Each shuffle underwent the full same optimization; this comparison accounts for selecting the best transform. The positive control consists of the first 366 numeric groups from Armstrong's regular 15 and 22 February letters, transformed synthetically. These numbers are independently reproducible from `tools/data/uscodes-1800/stats.py`. The returned transform recovers all original control groups for each of the three families.

| Table | Family | Target score | Shuffle mean | Shuffle range | Shuffles ≥ target | Control exact group recovery |
|---|---|---:|---:|---:|---:|---:|
| THE972_bourdeau | digits | 12.1649 | 13.2657 | 11.6713–15.7613 | 16/20 | 100% |
| THE972_bourdeau | affine | 10.0763 | 10.3994 | 9.0408–12.4787 | 14/20 | 100% |
| THE972_bourdeau | grid | 16.5191 | 13.7555 | 11.5323–18.2528 | 1/20 | 100% |
| WE028 | digits | 12.7011 | 15.7651 | 10.2869–20.9754 | 16/20 | not run |
| WE028 | affine | -1.5114 | 3.5783 | -2.4069–12.1975 | 19/20 | not run |
| WE028 | grid | 14.5336 | 8.4053 | 4.2261–17.4958 | 1/20 | not run |

**No target maximum lies above all shuffled maxima. No coherent target reading emerged.** The controls show the implementation can recover these deliberately applied transforms on ordinary Armstrong code. They have 189 distinct groups versus the target's 216, higher known-table coverage, and no graphic breaks; they are not fully design-matched controls. WE028 has no separate positive control here. Consequently these results do not exclude any historical code family or every renumbering of the sibling books.

The screen also prunes candidates mapping more than 20 token occurrences outside 1–1600, or matching fewer than 120 occurrences to known entries. That deliberately narrow assumption, uncertain manuscript readings, partial THE972 coverage, language-model mismatch, and neglected glyph information all limit the result. A different vocabulary ordering, a much larger table, separate low-number alphabet, variable width, or changing key remains untested by this screen.

## Reproduce

From the repository root, with Python 3, NumPy and g++ available:

```sh
python ciphers/armstrong-madison-1808/codex-2026-09-27/prepare.py
python ciphers/armstrong-madison-1808/codex-2026-09-27/run_screen.py
python ciphers/armstrong-madison-1808/codex-2026-09-27/padding_test.py
```

Generated 16 MB score matrices and the executable are ignored. `clean_screen_results.json` contains every final run's score, key and search counts; the `target_clean_*` and `control_THE972_*` TSVs retain the top 20 candidates. `manifest.json` records input hashes. No high-scoring word salad is offered as plaintext.

## What would materially change the evidence

The handwritten passages still need a stable, image-grounded token inventory; earlier shorthand-family eliminations in the repository should not be treated as universal exclusions. The already-recorded archival lead to Irving Brant's reconstruction of Livingston's cipher (LOC Irving Brant Papers, Box 37) could supply an independent key or vocabulary. This session has not retrieved that item and has not sent any archival request. At present neither a complete sibling codebook for this particular system nor a validated opening is available. The task remains an open decipherment problem.

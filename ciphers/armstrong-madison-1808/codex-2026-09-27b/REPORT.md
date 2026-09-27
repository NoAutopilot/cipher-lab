# Armstrong, 20 February 1808: glyph attack

**Result: unsolved. No plaintext or target key is claimed.** This continues the numeric-key tests in `../codex-2026-09-27/REPORT.md` by attacking the graphic passages as a possible alphabet. The deliverable is a provisional transcription and a reproducible experiment, not a recovered letter.

## Image-grounded transcription

`glyphs.tsv` records 25 graphic passages, their neighbouring numeric groups, and a tentative sequence of shape labels. It was read against the manuscript images `../images/M34-014-0030.jpg` through `0033.jpg`, with [S. Tomokiyo's shape inventory](https://cryptiana.web.fc2.com/code/madison_armstrong_graphic.png) and [two](https://cryptiana.web.fc2.com/code/madison_armstrong_graphic1.png) [passage sheets](https://cryptiana.web.fc2.com/code/madison_armstrong_graphic2.png) as references. Labels are Tomokiyo's inventory numbers, not plaintext values. The source manuscript is also available through [the Madison project](https://pjm.as.virginia.edu/john-armstrong-jr-james-madison-20-february-1808).

The working transcription has **257 glyph tokens, 36 types, and 28 fragments** after splitting at three tentative punctuation boundaries. Dots and several changes of shape are retained rather than merging all waves or curves. This is one reader's **M-grade provisional inventory**. It is not independently reconciled, complete with respect to every pen mark, or certified at the level of symbol boundaries. Some marks may be compounds rather than indivisible symbols. A missing dot, split sign, or mistaken allograph could materially affect a substitution attack. None of the original transcriptions was changed.

`glyph_prepare.py` derives the solver input from the TSV. The labels `00` and `02` in Tomokiyo's chart are treated as punctuation rather than alphabet members where the transcription uses `|`. This is an explicit assumption, not an established feature of the cipher.

## Alphabet experiment and controls

The hypothesis is that each graphic type represents one normalized English letter, with at most two graphic types per plaintext letter. The 24-letter alphabet folds j/i and v/u. A simulated-annealing search uses historical English character n-grams through order four, excluding the Jefferson volume used for the controls. Fragment boundaries reset the score; the numerical portions supply no guessed plaintext.

Each synthetic control has the same 257 tokens, 36 observed types and fragment lengths as the transcription. It is generated from held-out text with at most two homophones per letter. The actual target's design, symbol frequencies, possible transcription errors, and selection of passages for graphic encoding are not known to match these controls. In particular, clean arbitrary slices of prose are easier to model than passages selected for names or unusual words.

| Known-answer control | Text | 150 restarts × 30,000 steps | 1,000 restarts × 60,000 steps |
|---|---|---:|---:|
| 0 | English prose | 255/257 (99.22%) | 255/257 (99.22%) |
| 1 | English prose | 257/257 (100%) | 257/257 (100%) |
| 2 | English, French and Latin book titles | 90/257 (35.02%) | 136/257 (52.92%) |
| 3 | English prose, added after inspecting control 2 | 255/257 (99.22%) | 255/257 (99.22%) |

The initial third sample was not ordinary English: it lists philosophical works, including French and Latin titles. Its weak recovery was initially described as a solver limitation without noticing this language mismatch. It remains recorded as a stress test; control 3 was added after that inspection. This is a disclosed post hoc correction, not a pre-registered four-control suite. An earlier unsorted set iteration in control generation was also fixed, and all retained results were rerun against the deterministic inputs.

**Neither target run produces readable text.** Its best scores are -314.753033 in the smaller run and -308.524927 in the larger run. Three position-shuffled target controls, each given the smaller search budget, score -323.156835, -321.148521 and -317.689658. Three shuffles are too few to establish separation; their scores must not be compared as equal-budget tests against the larger target run. These are optimization scores, not probabilities of decipherment. The top candidate strings are retained only for audit, explicitly not as plaintext.

The controls demonstrate that this program can recover three clean English samples at this size. They do **not** rule out an alphabet with different homophone counts, shorthand, mixed word-and-letter signs, transcription errors, or a different language/register. Nor do they validate any of the previous shorthand-family exclusions.

## Exploratory variants

Four smaller-budget variants also produced no identified reading: a French language model; an English model with vowels deleted; treating shape 65 as a separator; and an explicitly ad hoc merger of seven shape distinctions. These variants have **no dedicated matched positive controls** and establish no negative result. Vowel deletion is only a crude surrogate, not an implementation of Taylor or another historical shorthand. The `coarsemerge` variant combines some multi-stroke shapes as well as dotted forms, so it must not be described as merely ignoring dots. Word signs, syllable signs, and variable-length compounds remain untested by this solver.

## Additional sibling-key check

[Bourdeau's Pinckney–Erving notes](https://github.com/dbourdeau/cyphersolver/blob/main/targets/erving1807/NOTES.md) provide partial readings and explicitly leave a full Pinckney key unfinished. Six published anchors are 1651=the, 133=of, 1343=and, 244=to, 1578=that and 69=in. None of these six numbers occurs in the editorially cleaned Armstrong target. `pinckney_anchors.json` records the check and the source blob hash. This supplies no anchor for direct transfer; it does not exclude renumbering or a related vocabulary.

The regular Armstrong THE=972 reconstruction remains the 580-entry partial table documented in the previous report. No complete sibling key for the anomalous 20 February system was found in this pass.

## Reproduce

From the repository root, with Python 3, NumPy and g++:

```sh
python ciphers/armstrong-madison-1808/codex-2026-09-27b/run_experiments.py
```

The model binaries and executable are generated locally and ignored. `results.json` records the measured recoveries and scores; `manifest.json` hashes the inputs. The manuscript images and historical-language corpora are already in this repository. Tomokiyo's three reference PNGs are linked above and can be downloaded with `fetch_sources.py`; they are not necessary to rerun the solver on the recorded transcription. No claimed reading, archive request, or solved-status promotion results from this work.

# Armstrong: variable-length glyph search, 27 September 2026

**Unsolved. No target plaintext or new key assignment recovered.** This
pass checked primary Annet manuals and tested whether the graphic signs
could represent individual letters or common pairs of letters. The
controlled search recovers substantial text in known messages but does
not produce a coherent Armstrong passage.

## What changed

The preceding run treated each provisional glyph type as a single letter.
Here each type can represent one letter or one of the forty most frequent
letter pairs in the training corpus. The search permits two glyph types
per plaintext piece. It uses the existing historical English character
model, normalizing j/i and v/u, with at most four-letter context.

This is a bounded substitution model, **not an implementation of Annet or
Taylor shorthand**. There are no word signs, nulls, phonetic rules,
context-dependent values or arbitrary-length syllables. The inherited
transcription still has 257 tokens, 36 provisional types and 28 fragments;
uncertain class boundaries and segmentation remain a material limitation.

## Controls and scoring correction

Five known messages were drawn from the held-out Jefferson corpus, which
was excluded from model training. Encoding produced the same token count,
type count and fragment-length sequence as the target. Depending on the
message, 34–42 tokens represent digraphs. This matches those structural
dimensions, not Armstrong's unknown encoding design or actual frequency
distribution. Control generation and complete answers are in `controls.json`.

The initial score added a reward for each decoded character. Rewards of
1–2 produced almost entirely digraphs and failed the controls. Expanding
the diagnostic grid to -0.5, 0 and 0.5 showed substantial search failures
as well as length bias. The next stage removed the character reward
(bonus 0, raw conditional log likelihood) and increased the budget to
1,000 restarts × 120,000 iterations, seeding half the restarts from earlier
candidates with five random perturbations. No target output was used to
select this setting. All diagnostic failures are retained.

| Control seed | Role | Exact token pieces | Recovery |
|---|---|---:|---:|
| 0 | tuning | 240/257 | 93.39% |
| 1 | tuning | 221/257 | 85.99% |
| 3 | tuning | 239/257 | 93.00% |
| 4 | fresh validation | 219/257 | 85.21% |
| 5 | fresh validation | 251/257 | 97.67% |

Recovery compares each decoded piece with the known piece at that cipher
token, without elastic character realignment. The search scores its
approximate answers higher than the actual plaintext in all five strong
runs. Thus its capability is partial recovery, not exact reconstruction.
Before fresh validation finished, `VALIDATION_PLAN.md` set an 80% floor
on both fresh controls for an exploratory target run. Both passed.

## Target and scrambled comparison

The target and three position-shuffled copies received identical two-stage
budgets: 120 × 45,000 iterations followed by 1,000 × 120,000 iterations,
bonus 0. Shuffling preserves each symbol's count and all fragment lengths.

| Input | Best total log10 score | Assessment |
|---|---:|---|
| target | -294.031441 | unreadable |
| shuffle 0 | -300.026775 | unreadable |
| shuffle 1 | -297.181649 | unreadable |
| shuffle 2 | -301.153413 | unreadable |

The target scores above these three scrambled copies but yields no
coherent passage. Three shuffles do not establish statistical significance.
Both real and scrambled candidates contain occasional English-looking
pieces; none is an accepted word assignment. Full candidate pools, keys,
and fragment readings are retained in `results/` and `target_results.json`.
There is no defensible crib to transfer to the numerical groups or confirm
across repeated passages. No numeral value was changed or promoted.

**Inference permitted:** this implementation did not find a reading of
this provisional transcription under this letter/digraph model.
**Inference not permitted:** Armstrong's symbols cannot be shorthand,
cannot contain digraphs, or have been proved unbreakable.

## Primary-source finding

`MANUALS.md` documents inspected Annet editions from 1752 and 1770. They
include alphabets, word meanings, word parts and composition rules. The
earlier characterization of Annet as simply a nonalphabetic sign index
is not adequate. The 1761 manual itself was not retrieved, and the inspected
editions cannot be silently substituted for it. A dotted-cup resemblance to
1770 WITH remains a visual hypothesis, with no accepted Armstrong reading.

The primary Madison-to-Jefferson transcription of 15 May 1808 was also
located and opened; it corroborates the historical possibility of an
unavailable private key. It supplies no decipherment.

## Reproduction

From this directory, using Python with NumPy and a C++17 compiler:

```sh
python prepare.py
python run_experiments.py initial
python run_experiments.py revised
python run_experiments.py strong
python run_experiments.py validation
python run_experiments.py target
```

Preparation uses `tools/data/en18/` and the preceding run's `glyph.seq`.
`evaluate.py` regenerates the control metrics and checks the C++ scores
against an independent Python scorer. `manual_sources.json` and
`download_manuals.py` identify and verify the primary scans. Large model
binaries and downloaded scans are excluded from Git; source and result
hashes are recorded in `manifest.json`.

The earlier sibling-table findings are unchanged: Bourdeau's regular
Armstrong table is partial, the full WE028 table is for a different code,
and neither is a demonstrated key to this letter. See the preceding two
reports for those comparisons and their limitations. No solution claim,
public comment, archive request or message to a researcher was made.

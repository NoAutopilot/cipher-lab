# Pre-registration: GAPS3-matignon-mayenne-1586 (3 Oct 2026, account-4), written and pushed before any scoring

Step (Verdict line, gap 1, verbatim): "commit them [the per-leaf beam's M choices] as S candidates on
f143r/f143v/f154/f173 in a scratch reading and re-judge per leaf against `judge_leaves.py`'s shuffle controls,
committing only if every leaf rises and stays above its shuffle max".

**Scratch reading.** For each of the 4 leaves, `mu_leaf_beam.beam` (unchanged: catheri01+marg 6-gram LM, U held as
TOK, exact per-line Viterbi) picks one alternative per M token; the leaf is rendered exactly as `judge_leaves.py`
renders it (H value, chosen M alternative, U/'*'/'+' dropped, `fold`) except that the chosen alternative replaces the
first. Baseline = the committed rendering (first alternative), i.e. `judge_leaves.py`'s own letters.

**Judge.** The spec's fr16 model (`specs/matignon-mayenne-1586.json`, corpus catheri01), mean log10 4-gram per letter.

**Gate, per leaf (the Verdict line's two conditions).**
- G1 rises: score(scratch) > score(baseline).
- G2 above shuffle max: score(scratch) > max of 20 within-line letter shuffles of the scratch letters
  (`judge_leaves.py`'s control: seeds from random.Random(1), 20 draws).

**Rule-3 power clause (pre-registered, can only void a pass, never create one).** The beam's LM and the judge share
catheri01 (GAPS gap 1 lesson), so G1 can hold by construction, and G2's letter-shuffle floor (about -1.8) sits far below
any decoded text. Therefore also:
- P1 shuffled-target rise (CLAUDE.md rule 3, shuffled-target paragraph): the same beam is run on 20 within-line
  token shuffles of the leaf (seeds 1..20, `random.Random(s).sample` per line, as `mu_leaf_beam.gain_test`), and its
  rise score(beam on shuffled) - score(first on shuffled) is computed each draw. The leaf's real rise must exceed the max
  of those 20 rises; otherwise G1 is non-discriminating on that leaf.
- Recorded beside, not re-run: the known-answer power of this same gain on each leaf's control (`mu_leaf_beam.json`:
  control gain above its shuffle-null max on 1/3 seeds f143r, 0/3 f143v, 0/3 f154, 0/3 f173).

**Verdict rule.** COMMIT iff all 4 leaves pass G1, G2 and P1 (then the choices go into exceptions as S, with this
control beside them, and `tools/decode_key.py --check` must exit 0). FAIL iff any leaf fails G1 or G2. NON-TEST iff
every leaf passes G1 and G2 but P1 fails on at least one leaf. In FAIL and NON-TEST nothing is committed to key.tsv,
exceptions.tsv or the reading; grades stay H 10,074 / M 1,648 / U 1,272. This is the beam's third target attempt
(bMAT1C, GAPS gap 1, now): a FAIL or NON-TEST retires the judge-based commit of this beam for this target (rule 3,
third-attempt clause), logged "untested-by-this-tool", not refuted.

Script: `mu_scommit.py` (deterministic, `--check`), results `mu_scommit.json`.

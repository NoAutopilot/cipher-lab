# PREREG-COL26-SIB (account 1, LANE DEFAULT-A1-1840-14, 14 Oct 2026): key_f23 C on one glossed sibling leaf at word grain

Registered before stage 0 is run, before any pairing of the leaf exists and before any score on it. Script: `siblings/word_sib.py` (its
docstring is the full rule; this file summarises it). Brief: `.claude/briefs/runs/2026-10-14-acct1-default-1840-jobs.md` job COL26-SIB.

**Why.** The Verdict's cheapest next and the open gap "the other La Thuillerie-Servien Jan-Feb 1648 leaves ... no reading yet": apply the
f.23 key and the sibling gloss values to one glossed sibling leaf at word grain, with a shuffled-key control and a synthetic code control
at the leaf's N. Word pairing is not retired in this folder (its instrument cleared on c33, COL26-C33, and on DA1-COL/COL3's canvases);
it was retired only for canvas 20-21 (mixed system, COL26-11B). This is a different question from COL26-C33/C51 (one code, 20 = i): here
the whole C key is scored on a leaf held out from its value choices.

**Leaf.** canvas 51 (rows 51L01-06, siblings/c5051_reconciled.tsv; images/crops/canvas51_full.jpg on disk, A2-COL15's region). Held out
from every C value choice except 30 = s (D2-COL26 used c51 4/4), so 30 is excluded from the scored key K on c51. Fallback canvas 32 (K
minus 23 and 12, R9-COL26's units include c32) only if c51 is TOO-SHORT at stage 0. canvas 30 not eligible (failed its own control).

**Statistic.** word_da1.py / word_c33.py hit rule unchanged (value at the predicted offset +-1 in the paired gloss word); H = hits over
the K-code occurrences in paired spans.

**Controls.** SK: K's values permuted among K's codes (10000 draws); W: gloss words permuted over the spans (10000 draws). Both can differ
from the target on H (SK changes which value is tested at each occurrence; W changes which word each span is scored against).
Synthetic (stage 0, before any vision): a two-digit code built from key_f23.tsv's own code -> value map plus one code per uncovered
letter, enciphering period French gloss text from the other sibling units, at the leaf's gloss words per row and the leaf's ideal N
(+-3), with reader boundary noise q = 0.25 per internal boundary, two independent noisy pairings per synthetic leaf, scored with the
same K, statistic, controls and gate; power = share of 300 synthetic leaves that PASS. Sensitivity q = 0 / 0.4 printed, not gated.

**Gate.** Stage 0: power >= 0.5 -> live; else TOO-SHORT (fallback leaf; both TOO-SHORT -> stop, no vision). Stage 1, per blind pass:
H > p95(SK) and P_SK < 0.05 and P_W < 0.05; leaf PASS iff both passes PASS; else FAIL (FAIL-LOWPOWER if stage-0 power < 0.5).

**Passes.** Line crops cut with `tools/iiif_lines.py --image images/crops/canvas51_full.jpg` (command pasted in NOTES.md; crops not
committed, this lane's no-image rule: manifest + regen command). Two blind Sonnet calls, neither sees the other's spans or any key
value; groups with indices and gloss words per row; horizontal placement only. Mechanical reconciliation -> siblings/
word_pairs_sib_c51_p1.tsv, _p2.tsv. One reconciliation unit = this worker checking the two files' format against the crops, no edits to
spans after scoring.

**Merge rule.** The script edits no key file. PASS -> the worker adds a decode job for the leaf (key_f23.tsv; K codes at their key grade,
every other token M via an exceptions file) and runs `tools/decode_key.py ciphers/colbert26-lathuillerie-1644 --check`; FAIL -> no key or
reading file is touched. No grade on f.23/f.24 changes in either case.

# PREREG TXE3-9 PINS (account 3, worker TXE3-9, 11 Oct 2026 05:5x UTC by date -u; committed BEFORE any decode is scored)

One of ten TXE3 experiments the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M) launched on 11 Oct 2026 at the owner's
request ("build off what we learned"). Read-free: no vision call, no network, no reader; every arm is a computation over the
two blind passes already on disk. Work folder `benchmark-tx/txeng3/9/`. Eval item `birago1572-no87` (BENCHMARK-TX.tsv,
split eval); the parent's brief names it as the item to score, and nothing here is tuned on it (lam is fixed at the TX-DECODE
dev value below; a hard pin has no weight to tune). No frozen confirm item is opened. BENCHMARK-TX truth is never edited.

## Hypothesis
The key-constrained lattice decode (`tools/key_decode_lattice.py`, TX-DECODE 3 Oct 2026; no.87 err_true falls at lam 4) and
the label rulings applied after decoding (today's L output, NO87-LABELS 3 Oct 2026) have each lowered no.87 error but have
never been combined with the decisions held fixed INSIDE the decode. Hypothesis: pinning the decided signs before the
Viterbi pass (the language model then sees the decided letter in context at those positions and cannot override it)
lowers err_true below both the unpinned decode (a) and the post-hoc relabel (c).

## Nearest prior and what differs
Register ids: TX-DECODE (the lattice, lam 1 pre-registered then lam 4 tuned on dev; TRANSCRIPTION.md row 5), TXE-E / M5
(learnt confusion matrix in the same lattice, dev-FAIL), TXE-J / M11 (jitter stability as a per-position prior, dev-FAIL),
X20 (TXE2-SORT: the owner's 4 Oct 2026 decisions applied on top of L -- 6 positions move, dev fixed 0 / broken 3),
NO87-LABELS (the X_CE relabel map, value-blind re-read + verifier ruling, L = C + 7 relabels). What differs: TXE-E and
TXE-J changed the lattice's soft priors; nothing has yet replaced a position's candidate set with ONE fixed sign (a hard
pin), and X20 applied the owner's decisions after the decode, never inside it. A hard pin is a new option on the shared
tool (`--pins FILE`), with an offline test (CLAUDE.md Usage 8). Not a re-run of a retired instrument: MARKS-DEV2b (the mark
rule, retired) and the transcribe-and-decode crossword (4 attempts, retired) are not touched; a hard pin inside the decode is a
different instrument from either, and no new material is claimed.

## Fixed inputs (none chosen after a score)
- Lattice: exactly TX-DECODE's recipe as `benchmark-tx/txeng/conf/run_conf.py` builds it (imported, not copied): blind
  passes A/B of f178v (passA/passB + the L11-23 files) and f179r from the harvest, committed passC as the position skeleton
  only (its signs are not candidates), `confusion_1572.tsv`, no learnt matrix, no stability prior, no --keep-alts.
  Lines: all 26 lattice lines f178v L01-23 + f179r L01-03 (dev_tune = f178v L01-12, eval_heldout = f178v L13-23 + f179r
  L01-03, the units of benchmark-tx/txeng/units/). f178r (3 lines, no lattice in TX-DECODE either) is taken from L in
  every arm, so every whole-no.87 output file is complete and the fixed scorer counts no missing line.
- Key: `harvest/key_1572_sheet.tsv` (T42 = m as on file) plus one row `X_CE s` (the off-sheet curled Ce, value s from the
  clerk sheet 7/7, as build_birago87.py already treats it), written to `benchmark-tx/txeng3/9/key_pins.tsv`. Arm (a) never
  has X_CE as a candidate, so this row cannot change (a); check: (a) on dev_tune must be byte-identical to the committed
  `passL_lattice_dev_tune_lam4.tsv`.
- Language model it16dip, beam 64, lam 4 (TX-DECODE's dev-tuned value; lam 1 reported beside as the original
  pre-registered value, not a second tuning), unk_cost default.
- Pin sets (a pin replaces the position's candidate set by {sign: 1.0}; the lattice may not change it):
  - P_L, the brief's (b): the 7 NO87-LABELS relabels (X_CE at f178v L01.23, L03.4, L04.4, L05.25, L07.29, L08.10,
    L10.5), i.e. exactly the positions where L differs from C. All seven lie on dev_tune lines, so on eval_heldout arms
    (a) and (b) are identical BY CONSTRUCTION; the headline is the whole-no.87 figure with the dev/eval split shown.
  - P_O, the owner's own 4 Oct 2026 decisions on no.87 as X20 reads them: settled_no87.tsv `moved` rows whose final
    pile is a T family and whose tile maps 1:1 to a position (18: 10 dev, 8 eval; 13 of them agree with L and 5 change
    it) plus the one family-sort cluster decision (f178v L01.8 T95 -> T65). Pinned sign = the owner's family.
  - P_LO = P_L + P_O (arm b2, about 26 pins; where both touch a position the owner's sign wins, as in X20).
  - P_S (exploratory arm b3, declared now): P_LO + the owner's `kept` tiles at their pile family (179 mapped: 77 dev,
    102 eval; 37 of them carry a machine seed that differs from L -- a kept tile is the owner leaving a seeded pile, not
    a decision, so this arm pins machine seeds too; it is here only because it is the one pin set large enough for the
    Wilson gate to be reachable in principle).
- Arms, each a whole-no.87 TSV (line, pos, sign) written to `benchmark-tx/txeng3/9/outputs/` and committed BEFORE any
  tx_bench call: (a) lattice lam 4 no pins; (b) lattice + P_L; (b2) lattice + P_LO; (b3) lattice + P_S; (c) = L
  (`outputs/birago1572-no87/labels.tsv`, today's output, the X_CE relabels applied after the committed reconcile);
  (c2) = passX20_owner (the owner's decisions applied after, X20's file); plus (a1), (b1) at lam 1.

## Endpoint and gate
- Primary endpoint: err_true from `tools/tx_bench.py` on birago1572-no87, as measured AND flagged-excluded, each with
  its Wilson 95% interval, never the latter alone (TRANSCRIPTION.md rule).
- Gate (the brief's question): (b) beats BOTH (a) and (c) when err(b) + its Wilson 95% half-width < err(a) and < err(c)
  on the as-measured whole-no.87 figure. Stated now: with 7 pins the largest possible move is 7 positions plus their
  n-gram neighbours, about 1% of 803, while the Wilson half-width at 4-5% on 803 signs is about 1.5%, so this gate
  cannot be met by (b) unless pins repair far more than their own positions; a null here is the expected result and is
  reported as one.
- Secondary (the repository's paired standard): `tx_bench --paired` position McNemar fixed / broken with its exact p, (b)
  vs (a) and (b) vs (c), on the whole file and on the unit where the pins lie; and the error count on the UNPINNED scored
  positions of the lattice lines per arm (the only positions a pin can change through context).
- Every position where an arm's chosen sign differs from the lattice top-1 is listed with right/wrong against truth;
  such a sign is grade S at best (rule 4; never H). A pinned position carries the pin source's own grade (C for X_CE,
  the owner's label for P_O), not S, and is listed separately.

## Controls (rule 3), each with its proof that it can vary on the statistic
1. Shuffled-key decode, which must not help: 100 value-shuffled keys (seed 1; the X_CE row's value is permuted with the
   rest), the SAME lattice and the SAME pins (P_L; also P_LO), scored as err on the unpinned scored positions and as the
   tool's own mean 4-gram rank/z. Can vary: at an unpinned position the Viterbi choice depends on the letter values the
   key assigns to the candidates, so a shuffled key changes which candidate wins and the error there. Pass condition:
   the real key's unpinned err ranks 1 of 101 and its 4-gram z is above the shuffled max; if a shuffled key's decode
   reads as well as the real one, the pinned gain (if any) is the language model inventing text and the arm is a
   non-result.
2. Random pins, which separate the owner's quality from the effect of pinning itself: for each pin-set size n (7, |P_LO|,
   |P_S|), 20 seeds, n scored lattice positions drawn at random outside the owner/labels set, each pinned to pass A's
   sign at that position (pass A aligned to the skeleton by the tool's own difflib rule; a position pass A does not
   cover is redrawn). Can vary: the drawn positions and pass A's signs there differ per seed (pass A is wrong at about
   6.6% of positions), so the pinned-arm err differs per seed. Reported: mean, min, max err over seeds, and the share of
   pins that are right (pass A at the drawn positions vs the owner/labels at theirs). A real pin set that does no
   better than the random band shows the effect is pinning, not the owner.
3. Identity check (not a control, a rule-3 shape check): on eval_heldout, (b) == (a) by construction for P_L; this is
   stated here so it is not read as "pins did nothing on eval".

## Stop rule and cost
Cap USD 15 of usage, box 05:48-07:48 UTC 11 Oct 2026, stop before any unit that would cross 80% (USD 12 / 07:24 UTC).
Units: tool option + test (1), harness + arms (1), controls (shuffles 100 x 2 pin sets, random 20 x 3 sizes; each
Viterbi pass over 26 lines takes seconds), scoring, RESULTS.md. If the shuffled-key control would take more than 10 min
it drops to 50 shuffles and says so. Cost per run is reported as wall-clock per Viterbi pass; the dollar figure of the
session is the orchestrator's to read (get_session), not mine.

## Register check
`python3 tools/tx_register.py --check benchmark-tx/PREREG-txeng3-9.md` output pasted in RESULTS.md.

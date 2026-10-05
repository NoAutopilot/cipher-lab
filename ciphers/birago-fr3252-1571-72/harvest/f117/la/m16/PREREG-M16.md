# PREREG D2-B117M (5 Oct 2026, account-1 worker for LANE-D2PUSH), written and pushed before any read or score

## Step 1: one value-blind window read of the 16 plain-M tiles of f.117r (la/kapc/m_to_s.tsv, kind=base, new_grade=M)
Tiles: la/m16/m16_in_tiles.tsv (8 passC-only, 4 look-alike UNSETTLED, 1 unaligned, 3 where the look-alike reader's firm 2-of-3
chose another sign: L02.27, L06.18, L06.26). Instrument: `tools/lookalike_pass.py windows` (per-tile windows from the existing
iiif_lines crops, candidates alphabetical, the tile's own label never shown, ids only, no values) + a candidate-only cut of the blind
1572 sheet; ONE Sonnet subagent call. Owner's sorter and its 12 focus tiles untouched.
Rule (the existing BIR-APPLY rule, two independent blind instruments agree -> S), fixed now:
 a. S iff the new read is firm (conf H or M, not SPLIT/X_NEW unless X_NEW is the top-1 sign) AND its label == the top-1 sign AND no
    firm earlier third read (look-alike 2-of-3 / confirms) carries a different sign. So L02.27, L06.18, L06.26 cannot become S
    here (2 vs 2); their reads are logged only.
 b. Anything else stays M. Values never change; only grades move. No second call, no re-prompt after reading answers.
Echo control (rule 3, can differ): the 3 tiles where a firm earlier blind read disagrees with top-1 -- an echo reader would match
top-1 on all 3; the read is reported with its agreement there. If the read matches top-1 on 16/16 the step is logged as possible
echo and nothing is promoted.

## Step 2: T88 = q, pre-registered on another 1572 leaf
Leaf: no.86 (BnF fr.3251 ff.174-175, 27 Aug 1572), sign pool `../../../nevers-birago-fr3251-1572/harvest/offsheet/pool_no86.tsv`
(column sign_id; 7 T88 tokens counted before scoring, nothing else looked at). Key: la/../map_printed.json (printed 1572 key;
T88 printed g; no q cell; u/v cells T33, T49).
Statistic F(c) = share of a cell's occurrences whose next token in the same passage is a u cell (T33 or T49) -- the q-word
signature (que, qui, quand, quelque...: q is followed by u in French and Italian of the period).
Control: 200 draws with replacement from the other letter cells (map kind 'letter', not T88, T33, T49) with >= 3 occurrences in
the pool, F of each drawn cell. The control can differ from the target (different cells have different u-follow rates).
PASS iff F(T88) >= 0.6 AND F(T88) is strictly above >= 190 of the 200 draws. Otherwise FAIL, logged in HYPOTHESES.md.
Secondary, reported but not gating: the same F on the no.87 and no.90 pools (no.87 is the leaf the printed key was rebuilt from).
One test, no re-tuning after scores.

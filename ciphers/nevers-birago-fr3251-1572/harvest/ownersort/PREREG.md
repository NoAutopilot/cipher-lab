# PREREG BIR-OWNERSORT (4 Oct 2026, account-3 worker) -- written and pushed before any score

Input: `sorter/owner-sort-2026-10-04/settled_labels.tsv` (owner's complete sort, 488 tiles, f.117r fr.3252 / f.144r / f.168;
kept 277, moved 203, aside 5, bad-cut 3; 52 -> 105 piles). The owner is a THIRD READER, never ground truth.
Scorer: `harvest/ownersort/ownersort.py` (run from the repo root). Disk only; no vision calls, no network.

## Tiles -> positions and the three readers
Tile -> (leaf, line, pos) by the BIR-OWNER rule (`harvest/tx_decode/eye/open/sorter/score_owner.py`, imported unchanged: identity where
tile and position counts agree, difflib otherwise). Reader A / reader B = the blind passA / passB sign at that position (f.144r, f.168:
`harvest/<leaf>/pass{A,B}.tsv`; f.117r: `../birago-fr3252-1571-72/harvest/f117/pass{A,B}.tsv`), aligned to the transcription line by
the same identity-or-difflib rule. Owner = final pile; owner family = pile name with any `-b/-c/...` suffix stripped.
Agreement per sign family (transcription sign): A=B, A=owner family, B=owner family, all three. Written to `three_reader.tsv`,
`agreement_by_sign.tsv`.

## The 52 -> 105 split test (step 2)
Unit = each new pile P whose family X is a sheet sign in `harvest/key_1572_sheet.tsv` and has >=1 tile left in pile X. Off-sheet families
(X_NEW, X_S, X_K, UNREAD) have no key value: untestable by the key, reported as owner-only distinctions.
Statistic G(P) = best LM gain from giving all P's tiles one free value v (any key letter value) instead of key[X], the rest of the
reading fixed at the base: G = max_v S(text | P->v) - S(text | P->key[X]), S = judge_plaintext NgramModel mean log10/letter on the
pooled three-leaf text weighted by letters (each leaf scored with its own spec model: f.117r fr, f.144r/f.168 it16dip), summed as
sum(score x letters).
Control (matched, rule 3): 200 random re-splits (seed 20261004): draw |P| tiles at random from the union P + pile X (same sizes),
compute G the same way. Split SUPPORTED iff G(P) > p95 of its control AND G(P) > 0.
Power control (run BEFORE the target piles): synthetic merges of two real sheet signs Y, Z with different key values (pairs from the
owner's own kept tiles, both >= 3 tiles); "split" = k tiles of Z drawn into a pile beside Y's tiles, Z taken as the parent; same G and
same random re-split control; k in {1, 2, 3, 5}. Power at k = share of 50 synthetic merges that pass. If power at the pile's own size
is < 0.5 the verdict for that pile is "untestable at this N" (neither supported nor merged).
Verdicts: SUPPORTED (real distinction; the tiles are U in the reading, the LM-best value listed as a proposal only, never applied --
it is chosen by the LM); NOT SUPPORTED with power >= 0.5 -> recorded as a merge the data supports (tiles take key[X]); untestable ->
owner-only distinction, flagged, tiles take key[X] (the owner's family call) with grade M at most.
Secondary, reported not gated: leaf concentration of P (share of P's tiles on its modal leaf vs the same for random re-splits).

## Re-decode (step 3)
Owner value at a tile: key[family] for a sheet family (moves between sheet piles = relabels; split piles per the verdict above),
U for off-sheet families. A change = owner value differs from the base value. Base (a) = BIR-OWNER's base (f.117r/f.168 BIR-APPLY tokens;
f.144r BIR-OPEN-144 tokens); the committed f.144r owner144 reading is also diffed.
Grades (BIR-OWNER rule, unchanged): S where the owner's sign equals a blind instrument read at that position (VERIFY, OPEN, OPEN144);
M owner-only; U for no value. Aside / bad-cut / kept = no change.
Gate per leaf and pooled (BIR-OWNER rule): apply the owner's changes on a leaf only if (b) > (a) AND (b) > p95 of (c), (c) = 200
draws of the same number of value changes at random positions from the lattice top-k look-alikes + same number of U removals
(seed 20261004). A leaf that fails keeps its base reading. decode_key.py --check must pass on what is written. Judge it16dip
(f.144r, f.168) and fr (f.117r) on the applied text. Rule 4a depth noted; no novelty (rule 10).
## Step 4: aside / bad-cut tiles listed for a recut, no value guessed.

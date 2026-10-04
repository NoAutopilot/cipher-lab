# RUN2-NXTB -- two blind passes of c516 (cipher part) and c515 L01-L20 (LANE-RUN2, account 1, 4 Oct 2026, 02:46-03:00 UTC)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run2-wave1.md` RUN2-NXTB. No decode, no alignment, key.tsv not applied (wave 2 stays blind).

## Crops (`crops/`, JPEG q40; `regen.sh` re-cuts the q90 originals the passes read)
- c516 has cipher in two blocks: 3 lines at the head of the leaf (c516a_L01-L03, before the clear lead-in "Sire quelques jours
  avant recevoir vre depesche ... me mander") and 15 lines after it (c516b_L01-L15); c516b_L15 ends in clear ("... qui sera
  Loudrou[?]"), followed by the clear close "ou je prieray Dieu ... de Pera lez Constantinople ce vij(?)e de Juillet 1574".
- c515 is cipher throughout: 40 lines (c515_L01-L40).
- Commands: `regen.sh` (iiif_lines `--follow-slope 300 --slope-margin 15 --overlap 100 --centres ...`, centres from the row ink
  profile of the block's left 500 px). Deviation: `--max-width 1850`, not 1800 -- at 1800 a 3600 px block cut into 3 segments
  overlapping by 900 px; 1850 gives 2 segments with the intended 100 px overlap. The _s2 overlap end is marked by corner ticks at
  x=100 (`tick_s2.py`). c516b_L04 was tracked onto the ink smear (line 5) by `--follow-slope` twice; re-cut by hand as a straight
  shear between its neighbours' slopes (`shear_L04.py`, manifest entry says so). Overlays and every crop checked by eye: one row each.

## Passes and agreement (err_2reader = 1 - agree / aligned columns, `tools/reconcile_passes.py`, nw)
Each pass is 2 Sonnet calls (9-10 lines, 18-20 crops, ~250-300 signs), blind, crop paths + Tomokiyo's table image + the
NX-RECUT label convention only. 8 calls in all.

| leaf | lines | signs A / B | raw agree | err_2reader raw | after recon_rules.py | err after rules |
|---|---|---|---|---|---|---|
| c516 (cipher part) | 18 | 515 / 504 | 226/525 = 43.0% | **57.0%** | 377/522 = 72.2% | **27.8%** (rules fitted here) |
| c515 L01-L20 | 20 | 608 / 610 | 335/621 = 53.9% | **46.1%** | 339/621 = 54.6% | **45.4%** (rules frozen, held out) |
| c515 L21-L40 | 20 | -- | not read (cap) | | | |

`recon_rules.py` (committed in 459392b1 before any c515 pass ran) settles splits two ways: TABLE rulings from one look at
c516b_L01 beside the table (swash zp = n1, cursive 4 = p1, crossed triple bar = r1, cup-on-stem psi = s2, epsilon = p2, 8 = W:de,
alpha = t1, omega-hook = u1 ...) and CLASS merges of two readers' descriptions of one unnamed shape (X:2+, X:hbar, X:Lhook).
On c516 that lifts agreement 43% -> 72%; on c515 it adds 0.7 points, because the c515 readers named the same shapes in new words
(`?{2p-loop}`, `?{2f}`, `?{flag-4}`, `?{Y-fork}`, `i2` for the 2+). So the c516 gain is in-sample vocabulary fitting, not a
settled inventory: **the held-out number (45%) is the honest error of this instrument on this hand.** Compare c262 (NX-RECUT):
31% after its convention. No rule was added after seeing c515.

## Outputs
- `passA.tsv`, `passB.tsv` (c516), `c515/passA.tsv`, `c515/passB.tsv` (wide format; spaces inside `?{...}` hyphenated, nothing else changed).
- `reconciled.tsv`, `c515/reconciled.tsv` (leaf, line, pos, label, grade): H only where both blind passes wrote the same label with no
  `?` and no rule touched it (c516 169 H / 353 M; c515 279 H / 342 M); split columns keep both readings `A|B`, grade M. Not settled
  from the image: at 28-45% the next reader is the person in the sign sorter (TRANSCRIPTION.md), not a third machine pass.
  Regenerate and check: `python3 build_recon.py --check` (in this folder and in `c515/`).
- `focus.tsv`, `c515/focus.tsv`: the split pairs ranked by column count with one example line:col each, for the sorter. Top on c515:
  X:2+ vs i2 (18), 2p-loop vs n1 (15), flag-4 vs f1 (13), 2f vs n1 (13), X:2+ vs n1 (11), Y-fork vs s1 (10), m1 vs s1 (9).
  Top on c516: o1/e2 vs r1 (8), X:2+ vs n1 (8), e3 vs u1 (6). The "2 with a cross" sign, the swash zp and the hash family
  (# / H-hash / triple bar) are the three shapes every reader named differently on every leaf.
- `tools/lookalike_pass.py` not run: RUN2-NXATL's atlas sheet had not landed in `run2/nxatl/` when this job reached step 3.
- err_true: not measurable -- no benchmark item of this hand exists.

Requests: gallica.bnf.fr 2 (native canvases 516, 515; HTTP 200); cryptiana.web.fc2.com 2 (one 302 to https, then the table PNG; kept
in scratchpad, not committed). Subagent calls 8 (Sonnet). Reconciliation: rule-based, one look at a crop beside the table.

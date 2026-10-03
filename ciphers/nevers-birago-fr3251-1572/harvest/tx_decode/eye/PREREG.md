# A1-BIR-EYE pre-registration (3 Oct 2026, 12:0x UTC, account-1 worker for LANE-A1)

Brief `.claude/briefs/runs/2026-10-03-acct3-a1-wave7.md` job 4 (Wave 8). Written and pushed **before any crop is shown to
any reader**. Question: does the page image support the signs the TX-DECODE lattice decode (printed 1572 key, lam 4, beam 64,
`../{f117,f168,f144r}_lam4.decode.tsv`, column `changed`) substituted for the two-reader top-1?

## Positions (fixed by `prereg_positions.py`, seed 20261003; `positions.tsv` holds the hidden truth)
- **Changed**: every lam-4 position with `changed = 1`: f.117r 32, f.168 11, f.144r 12 (55). Candidates: the original
  top-1 and the key-implied `chosen` sign.
- **Decoys**: an equal number per leaf (32 / 11 / 12), drawn at random from unchanged positions whose lattice carries a
  second candidate. Candidates: the top-1 and the lattice's best non-top-1 candidate ("swap").
- Each question shows the two candidates as A/B in random order (seeded). Changed and decoy questions are interleaved in
  random order; the reader file `blind_<leaf>.tsv` carries only qid, passage, pos, A, B. Orientation `orient_<leaf>.txt`:
  the top-1 label sequence per passage with **every** question position masked as `[qid]` (changed and decoy alike).

## Reader (one blind Opus subagent per leaf; order f.117r, f.168, f.144r; at most 4 vision calls in all)
Sees only: line crops cut by `tools/iiif_lines.py --image` from the leaf's committed native region (command pasted in
RESULTS.md before the first call; crops to the scratchpad, never the repo), `harvest/sign_sheet_blind_1572.png` (ids only,
no values), `blind_<leaf>.tsv` and `orient_<leaf>.txt`. Never told about a key, a decode, or which candidate is which kind.
Answers per qid: A, B or U (cannot tell), with confidence H/M/L.

## Gate (per leaf, and pooled over the three leaves)
c = changed questions answered with the key-implied sign; d = decoy questions answered with the swap sign; U counts as
neither. Rates r_c = c/n_c, r_d = d/n_d.
**PASS iff r_c > r_d AND one-sided binomial P(X >= c | n_c, p0) < 0.05 with p0 = (d+1)/(n_d+2).** Fisher exact one-sided
on the 2x2 reported beside it, descriptive only.
- PASS on a leaf: the changed positions on that leaf answered key-implied at H/M are listed as **S candidates for a
  verifier**; no grade is applied here, no reading committed, nothing above S, no novelty.
- FAIL on a leaf: logged "lattice changes not supported by the image" for that leaf.
- Pooled result reported; it licenses nothing on a leaf that fails its own gate.

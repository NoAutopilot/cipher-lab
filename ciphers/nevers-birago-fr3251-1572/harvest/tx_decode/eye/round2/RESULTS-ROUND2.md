# BIR-ROUND2 results (3 Oct 2026, account-3 worker)

Pre-registration `PREREG-ROUND2.md` + `prereg_round2.py`, `score_round2.py`, `r2posnull.py` pushed at 923a783f before any score or crop.
0 vision calls, 0 network requests.

## Step 1: round-2 lattice on the M tokens
Base (`r2_<leaf>_topk.tsv`): f.117r S 19 / H 191 / M 69 positions; f.168 S 5 / H 95 / M 22; f.144r S 0 / H 43 / M 47.
Viterbi at lam 4, beam 64 (`r2_<leaf>_lam4.decode.tsv`):

| leaf | changed | not asked before | asked before (re-proposed) | mdecoy pool (unasked, ratio >= 0.3) |
|---|---|---|---|---|
| f.117r | 13 | **0** | 13 | 0 |
| f.168 | 6 | **0** | 6 | 0 |
| f.144r | 13 | **0** | 13 | 3 |

**Result: untestable at this N on every leaf (pre-registered rule: fewer than 3 changed questions).** With the 24 S corrections pinned
and look-alike partners added, the lattice proposes nothing new. Every position it changes is one that A1-BIR-EYE or A1-BIR-VERIFY
already asked and did not keep, usually because the readers preferred the top-1 or answered at L. Nothing cascades from the 24.
No reader call was made, so steps 3-4 did not run. No exception was added, and the reading and grades are unchanged
(decode --check exit 0: f.117r M 74 S 179 U 26; f.168 M 22 S 90 U 10; f.144r M 36 S 40 U 14; H 0, C 0, I 0 on all three).
The judge lines are unchanged from A1-BIR-VERIFY.

Descriptive only, not a gate: `r2_reproposed.tsv` lists the 32 re-proposed positions with the earlier blind answers. The earlier
reads picked the key-implied sign there 16 of 26 times (f.117r), 7/12 (f.168) and 9/23 (f.144r), mostly at L. That is the
ambiguity-level rate (the matched decoys flipped about half the time), so it adds nothing.

Position-shuffled-lattice null on the round-2 base (`r2posnull.json`): PASS on all three: real key rank 1/201 and real S above every one of 200 shuffled lattices (f.117r -1.081 vs p95 -1.521, z 4.97 vs shuffled p95 1.42; f.168 -1.019 vs -1.425, z 3.61 vs 0.96; f.144r -0.998 vs -1.197, z 3.08 vs 1.56; 111 s). Pinning the 24 S and H positions keeps the key separable from the null (A1-POSNULL z on the unpinned lattices: 3.66 / 2.77 / 3.10), but this gate licenses nothing without reader questions

Reading: the A/B lattice instrument has reached its limit on these leaves at lam 4. Round 1 found the 24 corrections that the image supports,
and the remaining M error is not where the key-plus-LM objective disagrees with the top-1. A different instrument is needed:
an **open-choice** blind re-read of the M positions against the whole sign sheet (not A/B between two lattice candidates), which adds
new candidates, and then the lattice again. This is not a further tuning of lam (rule 3, third-attempt clause).

## Step 2: U tokens (`u_tokens.tsv`, report only, no value applied)
U per leaf (token files): f.117r X_NEW 23, X_S 1, X_K 1, X_EQ 1; f.168 X_NEW 8, X_K 1, X_EQ 1; f.144r X_NEW 14.
The printed key (`keys/key_nevers_birago_1572.tsv`; sheet `key_1572_sheet.tsv`) has **no null** and 8 word or name codes: che T89,
per T26, qual T78, quello T84, et T29, and the digit codes carmagnola 85 (T11), turino 86 (T46), bugonotti 89 (T15). Reader shape
notes (both passes, 91 off-sheet rows) compared with the printed descriptions:
- **digit pair "4 7"** on two leaves (f.117r L02.28-29 "4 with crossbar" + "7"; f.144r L04.1.9-10 "digit 4" + "digit 7", both readers),
  and **"1 6"** (f.144r L05.13, both readers). Shape class = the printed plain-digit name codes (85/86/89), but 47 and 16 are not in
  the printed key. A recurring two-digit group like this is consistent with an unprinted name code. Value unknown.
- **lone 8** (f.117r L01.19, L03.25): not a printed code (85/89 carry a tick over the 8); earlier fits weak (NOTES, offsheet).
- **"up triangle over cross/stem"** (f.144r L03.10/11, L06.20, readers' alt T84): nearest printed shape is quello (downward triangle
  pierced by a vertical stroke), but the orientation the readers saw is the reverse. Two blind A/B reads chose X_NEW over T84 at L06.20.
- "epsilon with dot" (f.117r L08.27) is near et (backwards-3 joined to a small circle); "big curl with 9 inside" (f.117r L10.8) is near che. Each is a single occurrence.
- The other 73 rows match no printed word code, name code or null by description.
Next for U: the owner's sign sorter on the X_NEW tiles (already the route for off-sheet shapes), then a pooled 47/16 occurrence
count across the fr.3251/fr.3252 1572 leaves (disk only, ~$1).

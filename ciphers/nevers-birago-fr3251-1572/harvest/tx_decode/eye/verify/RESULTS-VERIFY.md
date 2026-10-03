# A1-BIR-VERIFY results (3 Oct 2026, 12:2x UTC, account-1 verifier for LANE-A1; a session other than A1-BIR-EYE's)

Pre-registration `PREREG-VERIFY.md`, `prereg_verify.py` and `score_verify.py` were pushed at 594c0f26 before any crop was shown, and `build_decode.py` at
f7c063b2 before any answer existed. 3 vision calls (one fresh blind Opus reader per leaf), 0 network requests; crops in the scratchpad only.

## (b) Decoy-draw audit
The seed reproduces: prereg_positions.py re-run gives byte-identical positions/blind/orient files, and score.py re-run gives a byte-identical
score.json. No A/B option-order leak was found. **Confound:** the decoys came from unambiguous positions (median lattice
ratio of second candidate to top-1: 0.12 / 0.11 / 0.18 for decoys against 0.68 / 0.28 / 0.34 for changed positions on f.117r / f.168 / f.144r), so A1-BIR-EYE's gate
compared ambiguous positions with easy ones. Added arm 'mdecoy': unchanged positions at lattice ratio >= 0.3. Gate G2 tests it.

## (a) Re-read: f.117r re-cut at the original band height (30/30 boxes identical to the committed manifest); f.168, f.144r replication
| leaf | G1 (brief's gate, unchanged): changed key-implied vs decoy swap | G2 (ambiguity-matched): changed (ratio>=0.3) vs mdecoy swap | S candidates kept |
|---|---|---|---|
| f.117r | 27/32 vs 5/32, p 3.6e-16, PASS (A1-BIR-EYE: 27/32 vs 3/32) | 24/26 vs 15/30, p 5.2e-06, PASS | 19 of 19 |
| f.168 | 10/11 vs 1/11, p 7.0e-08, PASS (A1-BIR-EYE: 7/11 vs 1/11) | 5/5 vs 3/7, p 0.017, PASS | 5 of 5 |
| f.144r | 6/12 vs 0/12, p 8.4e-05, PASS (A1-BIR-EYE: 5/12 vs 0/12) | 5/8 vs 6/12, p 0.36, **FAIL** | 0 of 4 |

On the matched decoys the reader flips the two-reader top-1 about half the time (15/30, 3/7, 6/12). The original transcription is that
weak at ambiguous positions, so most of A1-BIR-EYE's margin came from the easy decoys. On f.117r and f.168 the key-implied sign still beats
matched ambiguity (92% and 100% against 50% and 43%). On f.144r it does not: its 4 candidates are dropped and stay at their current grade.

## (c) 24 survivors applied at S (exceptions path, `decode_verify.json`; f.117r/f.168 skeleton = lam-4 top-1, conf H where prior >= 0.85)
    $ python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --config harvest/tx_decode/eye/verify/decode_verify.json --check
    ciphertext_f117_top1.tsv: tokens 279: M 74, S 179, U 26      (without exceptions: M 74, S 179, U 26; 19 values changed at S)
    ciphertext_f168_top1.tsv: tokens 122: M 22, S 90, U 10       (without exceptions: M 20, S 90, U 12; 5 values changed)
    harvest/ciphertext_f144r.tsv: tokens 90: M 36, S 40, U 14    (no exceptions)
    reading up to date   (exit 0; main decode.json --check also exit 0)
H 0 and C 0 on every leaf, so this is a cryptanalytic result. The printed key itself is graded S.
    f.117r  FAIL language: score=-1.294, null_p99=-1.797, real_p05=-0.907, real_median=-0.791, mode=both, N=266   (before exceptions -1.588)
    f.168   FAIL language: score=-1.238, null_p99=-1.64, real_p05=-0.975, real_median=-0.821, mode=both, N=114    (before -1.399)
    f.144r  FAIL language: score=-1.454, null_p99=-1.6, real_p05=-0.955, real_median=-0.828, mode=both, N=94      (unchanged)
The judge gain is partly circular, because the lattice picked these signs for key fit. It is not independent evidence. No reading is claimed and no novelty classed.

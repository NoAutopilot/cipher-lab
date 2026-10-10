# TXV-GROEN: the f.103r closing stretch's clerk-split flags against Groen's clerk-independent text (PREREG-txeng2-21 WIT-FLAGS)

Verifier session (account-4, Opus 5.5) for LANE TX-ENGINEER-2, 10 Oct 2026, 02:15-02:3x UTC by date -u. Steps 1-5 of WIT-FLAGS;
step 6 (run_audit.sh on the new item) is the lane's and was not run here. **Openings of eval truth: 1 (the verifier's own, this item)**:
the --offsets dump of vivonne1573-f103r-confirm2 and the truth-column identity check of the new item against it.
Not opened: any reader pass on f.103r (outputs/vivonne1573-f103r-confirm2/*, tx/f103r_passA/passB.tsv, passA_S2/passB_S2/passZ_S2b),
any f.103r line crop, any cipher sign. The six frozen outputs were byte-copied by the build and checked by hash only.

## Step 1: build options
`build_vivonne_confirm2.py` gains `--witness FILE` (new item vivonne1573-f103r-confirm2-w) and `--offsets OUT.tsv` (dump, exits).
`--check` on the frozen item, before the edit: `ok: truth, sha256 and outputs current (5d228b454ef556fa1e6d23cc7dca9fa3c58f332035792e0454b9f156ad2cfe7f)`;
after the edit: `ok: truth, sha256 and outputs current (5d228b454ef556fa1e6d23cc7dca9fa3c58f332035792e0454b9f156ad2cfe7f)`;
`--witness ... --check` on the new item: `ok: truth, sha256 and outputs current (3523f652bebc846430ffcb609be0c6212747cdb6365abf244a3390448a44da51)`.
No offline test exists for this build file (none in tools/tests or benchmark-tx). Identity check of the new item against the frozen
one (script, 2033 rows): columns differing `{'flag': 84}`; line, pos, ref_sign, truth, plain and status identical (True); flag
transitions `clerk-split -> '' : 76`, `clerk-doubtful,clerk-split -> alignment-doubtful : 8`. Outputs dir: the six frozen files,
`diff` against txeng2/s2score/SHA256SUMS.prescore: identical (HASHES-MATCH-PRESCORE).

## Steps 2-3: alignment, controls (written to controls.json before any verdict), verdicts
Re-derived windows (wit_groen's best()): p.90* clean 8937-9307 ratio 0.7865 (WIT-GROEN 8937: 0 letters apart); p.91* damaged 9270-9459
ratio 0.6508 (WIT-GROEN 9270: 0 apart). Window 8937-9459: 323 scored raw positions, **182 clerk-split**, 141 clerk-agreed.

| control | value |
|---|---|
| (a) ceiling: clerk-agreed positions with witness == clerk inside a block >= 4 | **125 / 141 = 0.8865** (gate >= 0.60) |
| (b) null, clean part, 200 letter-shuffled copies at their own best windows | max 6, p95 0, mean 0.18 |
| (b) null, damaged part, 50 copies | max 3, p95 0, mean 0.10 |
| gate null max (declared before the run: clean max + damaged max) | **9** (paired clean i + damaged i mod 50: max 6, p95 3) |

| part | CONFIRM | CONFLICT | NO-EVIDENCE |
|---|---|---|---|
| p.90* clean | 65 | 0 | 49 |
| p.91* damaged | 19 | 0 | 49 |
| total (182) | **84** | **0** | **98** |

Gate: 84 > 9 AND 0.8865 >= 0.60 -> **INFORMATIVE**.

Limits, stated not changed: (i) under the declared evidence rule (letters inside matching blocks >= 4 only) a witness letter equals
dec_norm's letter by construction, so CONFLICT cannot occur; a disagreeing witness lands in NO-EVIDENCE. The pass can confirm a merged
clerk letter, never contradict one. (ii) clerk-split is word-level (cmask): of the 182, 134 sit where both blind clerk reads have the
same letter at that offset (the word, not the letter, split); 48 differ or are unmapped in one read, and 6 of the 18 confirmed among
those are a real letter disagreement (e/a, e/t, i/e, r/t, t/z x2; one y/i pair is the fold) -- the rest are a letter one read's alignment did not map.
(iii) a CONFIRM says the clerk letter stands; it says nothing about the cipher sign or the key value at that position.

## Step 4: new item (applied by the build from the witness file)
vivonne1573-f103r-confirm2-w: scored 1068; **flagged 492, unflagged 576** (frozen 568 / 500). 84 clerk-split flags removed; 8 of those
positions keep their TXV-VIV class re-labelled alignment-doubtful; no align-conflict flag touched; nothing outside 8937-9459 changed.
The truth of record stays vivonne1573-f103r-confirm2; adopting the -w mask is the orchestrator's decision before any comparison.

Observation for the lane (not changed here): BENCHMARK-TX.tsv row 11 notes cite truth sha256 936a489f...; the frozen item's
.sha256 and `--check` give 5d228b45... (the TXV-VIV flag rebuild); the row's note is stale.

## Files and hashes
| commit | file | sha256 |
|---|---|---|
| a67d3b028 | benchmark-tx/build_vivonne_confirm2.py | d998a8f08a0044fcdab431c3f780e3ccc0e6ed2fad4758819f74eb747bcfcae8 |
| a67d3b028 | benchmark-tx/txeng2/witflags/wit_flags.py | d3febb531ba9c4559d5f6a9cb50315bf7ffe1385e09f3c6684c0b29a08bb264c |
| a67d3b028 | benchmark-tx/txeng2/witflags/offsets.tsv | 099e789ff7360cd97ce81b05adb8723c5de299aae68bf0fd71d1bac1faf8b66e |
| 206ec284d | benchmark-tx/txeng2/witflags/controls.json | ddb2ef0804eb6e1513781a32b56ad2d6b09f1929e45a2e952e0a1d9ccb1205e7 |
| 206ec284d | benchmark-tx/txeng2/witflags/ceiling.tsv | b8c63bb4fc4a4e9be5ee64916164bca969fe06878088bfaff45ac13ce5bd3f68 |
| 206ec284d | benchmark-tx/txeng2/witflags/result.json | dccc479ce63175faa151fc05aed82d530beb78d9410cb72cfb577791ece7e470 |
| 206ec284d | benchmark-tx/vivonne1573-f103r-confirm2.witness.tsv | bdea44f9da63017b2b824e74572566453dd2fa265ab564732b7dea7bd13ae445 |
| da6b4abb2 | benchmark-tx/vivonne1573-f103r-confirm2-w.truth.tsv | 3523f652bebc846430ffcb609be0c6212747cdb6365abf244a3390448a44da51 |
| da6b4abb2 | benchmark-tx/vivonne1573-f103r-confirm2-w.truth.tsv.sha256 | 936f3a19dd67636b9e4aacdf97bd32e6e4fec4132f18d094ad2886ba8487b496 |
| da6b4abb2 | benchmark-tx/outputs/vivonne1573-f103r-confirm2-w/*.tsv (6) | = SHA256SUMS.prescore |
| da6b4abb2 | BENCHMARK-TX.tsv (row vivonne1573-f103r-confirm2-w) | 183ce158c5b6cf2eb61023b98c4531aa9d6b62ff4b12b19001b2982f69c03b8f |

Verdict: measured: INFORMATIVE (84 confirmed)

# BIR-APPLY (account-3 worker, 3 Oct 2026 13:2x UTC)

Targets: birago-fr3252-1571-72 (f.117r), nevers-birago-fr3251-1572 (f.168). Opus 5.5. Cap USD 3, box 30 min. Vision calls 0.
Claim in ROOM.md first; done line at the end.

Orchestrator grade policy (account 3, 3 Oct 2026, answering BIR-OPEN's flag): a lattice correction is graded S only where two
independent blind instruments agree on the same sign -- A1-BIR-VERIFY's two-option check (with ambiguity-matched decoys) AND
BIR-OPEN's open-choice re-read (with H-decoy calibration). That is the 11/19 on f.117r and 2/5 on f.168 BIR-OPEN reports as
replicated. The others (incl. the 11 T95/T51 and T83/T24 conflicts and BIR-OPEN's 16 new single-instrument values) stay M.
tools/decode_key.py now has 'exception_grade_overrides_conf' (decode.json) so an exception's explicit grade survives the
low-confidence downgrade; test tools/tests/test_decode_key_exc_grade.py.

1. Write the exceptions files so only the replicated positions carry S (others M, reason column naming the instrument(s)); set
   'exception_grade_overrides_conf': true in the decode config used for these readings; regenerate with tools/decode_key.py, then
   --check exit 0. Report H/C/S/M/I/U per leaf.
2. Judge each leaf (fr f.117r, it f.168) and paste the lines in both NOTES.md.
3. Sorter focus: write a focus.tsv (format of tools/sign_sorter.py --focus) listing the conflicting sign pairs T95/T51, T65/T51,
   T83/T24 with their crop paths, under ciphers/nevers-birago-fr3251-1572/harvest/tx_decode/eye/open/sorter/, and say in your done
   line that it is ready for the orchestrator to publish (the orchestrator builds and publishes the sorter page; you do not).
4. gaps_check; file_shrink_guard; commit by explicit path; push. Report what was found and where it was not found; no novelty.

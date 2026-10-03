# FT4g pre-registration (3 Oct 2026, account-4), committed before any gate re-run

Eye check of 253 / 242 / 66 on f.249 (group crops images/eye249/c01-c07, decoys c08-c12; reads in images/eye249/READS.tsv):
two blind Opus reads + one Opus reconciliation. Every occurrence of 253, 242 and 66 is confirmed as transcribed
(c03 = f.249r L03 "253" at medium: passes split 253|255, reconciliation 253, flat-top 3 form).
Transcription change: NONE to ciphertext_f249.txt. (Decoy c09 605 -> recon 603 medium against both blind passes 605;
not a target group, left as 605; noted only. c12 33|35 stays a|b, first used.)
Gates re-run exactly as registered, no parameter change:
  python3 align/gate_pair.py --cipher ../ciphertext_f249.txt --slip ../slip_f250.txt --n 200 --limit 5   (from align/)
  python3 align/pooled_gate3.py   (n 100, limit 5, seed 7, defaults)
Expected under an unchanged transcription: identical to FT4e (H 0; Hp 0, FAIL by rule = non-test). A different
number would mean nondeterminism, reported as such.

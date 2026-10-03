# PREREG A1-VILL-HOMO (3 Oct 2026, ~11:33 UTC, written and pushed before any run)

Hypothesis family: homophonic substitution over every sign and figure in Bourdeau's one-token-per-sign
transcription (bourdeau/ct_*.txt), each token type an unknown code for one letter, K (13 tokens) removed as
the f159 null N3. Cipher: homo/cipher_noK.txt, 25 lines (one per transcribed line), N = 740, K = 53 types.

Command (tools/family_run.py, control first):
  python3 tools/family_run.py specs/fr3993-villeroy-1595.json --family homophonic --cipher ciphers/fr3993-villeroy-1595/homo/cipher_noK.txt
      --tokens space --param profile=target --seeds 3 --restarts 8 --gate 0.6 --corpus tools/data/fr16
Control: fr16 window of N=740 under a homophonic key with the target's own K=53 and sign-count profile (profile=target).

Decision rule:
- control mean < 0.6 -> CONTROL BELOW GATE: target not run; logged "untestable by homophonic_anneal at N=740 K=53"
  (non-test, not a negative). No second tuning of the same knob in this job (rule 3, third-attempt clause).
- control mean >= 0.6 -> target runs once on seed 1, plus one --shuffle-target 1 run (false-positive floor).
  Target counts as "worth a reader" only if the judge PASSes the real decode AND FAILs the shuffled decode;
  otherwise logged as a control-backed negative for this family at this transcription, conditional on
  Bourdeau's single unmeasured pass (rule 2). Either way no token is graded above M.
Transcription error: unmeasured (one pass); a negative is conditional on it and noted so.

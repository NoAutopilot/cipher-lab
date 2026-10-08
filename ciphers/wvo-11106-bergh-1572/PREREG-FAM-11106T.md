# PREREG-FAM-11106T (written and pushed 8 Oct 2026 before any family score was computed)

Target: ciphers/wvo-11106-bergh-1572/ciphertext.txt (N=820, K=41 provisional labels, err_2reader 0.10).
Design prior (tools/design_prior.py, pasted in NOTES.md): letter-for-letter `plausible` (d 0.46, envelope 0.83, null p05 0.88);
multi-sign nearest (d 0.21) but `not above null`. masc cannot build a control here (it needs a plaintext window with exactly
K=41 distinct letters; folded French has at most 26), so the letter-level design at K=41 is tested as `homophonic`.

Run: `python3 tools/family_run.py specs/wvo-11106-bergh-1572.json --family homophonic --seeds 3 --gate 0.6 --param profile=target
--param noise=0.10 --measured-error 0.10` (corpus = the spec's judge language fr -> tools/data/fr16).
Gates, fixed now:
1. Control first: mean recovery over 3 seeds >= 0.6, else CONTROL BELOW GATE -> the target is not run and the row reads
   "untestable by this family at this N/K/noise", not a negative.
2. If the control passes and the target's fr judge says FAIL: a control-backed negative for single-letter homophonic
   French at this transcription (conditional on the provisional inventory and on French).
3. If the target's judge says PASS: nothing is claimed until `--shuffle-target 1` runs on the same settings; a PASS there
   voids the judge for this family at this N.
No crib, no historical text, no year assumption is used.

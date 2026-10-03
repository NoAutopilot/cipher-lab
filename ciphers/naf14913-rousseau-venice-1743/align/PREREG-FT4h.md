# FT4h pre-registration (3 Oct 2026, account-4), committed before the f.213r-v passage is transcribed or scored

Pair: cipher passage f.213r (after "...plus puissante en Italie", 5 numeral lines) + f.213v (3 numeral lines, before
"Le passage en France du fils aine de Mr le Chevalier de St George") <-> pasted slip f.214r ("M. Lorenzi. du 1er fevrier
1744", about 9 lines, "Par la conqueste des 2 Siciles ... par la meme Rep."). FT4b located 213v only; FT4h's 1000 px view
of 213r (canvas 439) shows the passage starts there.
Gate: FT4b's registered gate, unchanged (NOTES.md "Pre-registered gate for the f.206 key"), via
  python3 align/gate_pair.py --cipher ../ciphertext_f213.txt --slip ../slip_f214r.txt --n 200 --limit 20 --seed 1   (from align/)
H >= 5 AND H > p95(a value permutation) AND H > p95(b pairing shuffle); fewer than 5 occurrences of the ten C codes =
non-test; MAXLEN 12 as FT4c. No parameter is changed after the transcription is seen.
Transcription: native crops (images/ft4h/f213r_*, f213v_*, f214r_*); pass A = the worker's own read, pass B = one blind
Opus subagent read of the same crops, reconciled with tools/reconcile_passes.py and the image. Slip: worker read of the
f214r crops (clear French). If the cap or box stops the job before both passes are reconciled, the gate is not run.

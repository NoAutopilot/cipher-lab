# blitz-ciphers

open

Minimal check-solved (25 Sept 2026, bBLZ, LANE B3 breadth intake step): read in full the Cipherbrain
post (Schmeh, 14 Mar 2017, `sources/schmeh/posts/41-blitz.txt`, fetched by bSPEC2 25 Sept 2026) and its
32-comment thread (both pages' worth of content present in the fetched text) -- the post itself states
"To my knowledge, the Blitz Ciphers have never been solved," and every comment is about authenticity
(Pelling vs. SantaColoma et al.), none claims a decipherment. Grepped both solver repositories (shallow
clone, grep, delete, 25 Sept 2026): dbourdeau/cyphersolver's `TARGETS.md`/`top50/NOTES.md` lists Blitz
among items where "provenance or authenticity unresolved," not solved, "Blitz has only 8 of an unknown
number of pages released"; aaymeloglu/unsolved-ciphers's `SHORTLIST.md` lists Blitz under "Hoax risk, no
context, or no real system" -- neither repo carries a reading. OpenAlex query (`search=Blitz Ciphers
solved decrypted`, keyed, 25 Sept 2026): 7 hits, all irrelevant (steganography/IoT/genomics papers, no
match on subject). Semantic Scholar: 429 (Too Many Requests) on the keyed call and on one retry after a
3 s pause per the good-citizen one-retry rule -- not reached this pass, logged as unreachable, not
treated as a search result either way.

## Spec

See `specs/blitz-ciphers.json` (written 25 Sept 2026 by bSPEC2). Ciphertext (2 of 8 pages, Pelling's own
partial transcription) is already on file in the spec; no image fetch needed for cheap test 1.

## Intake gate

```
$ python3 tools/intake_gate_check.py blitz-ciphers
blitz-ciphers: open (line 3) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## Cheap test 1 (25 Sept 2026, bBLZ): IC/frequency profile vs three matched controls

Ran `cheap_tests_in_order[0]` exactly as specified: letter-frequency and index-of-coincidence
profile of the two transcribed pages (folded to letters-only, N=581 both readings), case-sensitive
(K=48) and case-folded (K=25), against English monoalphabetic, periodic-polyalphabetic (coset-IC
scan p=2..20) and homophonic-substitution matched controls of the same N and K, per Pelling's own
three-hypothesis framing. Disk-only, no network. English corpus: `tools/data/pg1661_holmes.txt`
(same corpus used elsewhere in this repo, e.g. mlh-1976, for an English IC baseline).

Script: `specs/cheap-tests/blitz-ciphers/ic_profile.py`, output in
`specs/cheap-tests/blitz-ciphers/ic_profile_output.txt` (50 samples per control design, mean +
[min,max] reported per rule 3). Plus `tools/family_run.py --control-only` for masc, homophonic and
periodic_vigenere as calibration (recovery power of this repo's own solvers at this N/K, English
corpus) -- rows in `HYPOTHESES.md`. **Note on HYPOTHESES.md row order**: the first `homophonic` row
(19:57 UTC, labelled case-sensitive but K=25) is a labelling mistake -- `--tokens letters` folds
case via `judge_plaintext.fold` regardless of the input file's own case, so it silently re-ran the
case-folded K=25 cipher a second time under the wrong label. The corrected case-sensitive K=48 run
(19:58 UTC, `--tokens space` on a space-token-per-character file, which does preserve case) is the
one that answers the case-sensitive question; the mis-labelled row is left in place (HYPOTHESES.md
is append-only, rule: never edited by hand) but should not be read as the case-sensitive result.

**Target statistics** (case-folded, K=25, treating case as not meaningful):
pooled IC = 0.0628. Periodic scan p=2..20 stays flat, 0.0580-0.0662, no period stands out from the
noise floor (nominal peak at p=16, IC 0.0662, barely above the pooled value).

**Target statistics** (case-sensitive, K=48, treating upper/lower as distinct signs):
pooled IC = 0.0351. Periodic scan p=2..20 also flat, 0.0326-0.0380 (nominal peak p=16, IC 0.0380).

**Matched controls, N=581** (mean [min,max], 50 samples unless noted):
| design | K=25 (case-folded) | K=48 (case-sensitive) |
|---|---|---|
| monoalphabetic English (pooled IC) | 0.0647 [0.0592,0.0705] | 0.0614 [0.0541,0.0697] |
| homophonic English, freq-flattened (pooled IC) | 0.0421 [0.0400,0.0447] | 0.0213 [0.0200,0.0228] |
| uniform random (pooled IC, theory 1/K) | 0.0385 [0.0378,0.0399] (theory 0.0400) | 0.0192 [0.0186,0.0204] (theory 0.0208) |
| periodic-Vigenere English, period 20 (pooled IC / scan-peak) | 0.0397 [0.0383,0.0417] / 0.0649 [0.0599,0.0729] | 0.0219 [0.0200,0.0253] / 0.0622 [0.0567,0.0696] |

The periodic-Vigenere control's own scan recovered the true period 19-20/20 trials at every period
2-20 tested, both K settings -- confirming the scan has power to detect a real period at this N even
at period 20, i.e. the target's flat scan is not an artefact of the test lacking power at this length.

**family_run.py control-only calibration** (matched-corpus anneal/solver recovery, this repo's own
solvers, N=581, 3 seeds each, gate 0.6):
| family | K | CONTROL mean recovery (range) |
|---|---|---|
| masc (simple substitution) | 25 | 0.999 (0.998-1.000) |
| homophonic | 48 | 0.996 (0.995-0.998) |
| periodic_vigenere (period auto-scanned on the target's own coset IC) | 25 | 1.000 (1.000-1.000) |

All three controls solve near-ceiling at this N -- these solvers have real power here, so an
inconclusive result on the target is not explained by the test lacking power at this length (unlike
e.g. rubin-1953/mccormick-1999 at shorter N). No target decode is claimed or scored: the spec
deliberately has no judge language (no known plaintext, no crib), so there is nothing to grade a
target "recovery" against -- per brief, this reports control recovery and target statistics only.

**Reading of the profile, following Pelling's own framing:**
- Case-folded (K=25) pooled IC (0.0628) sits inside the monoalphabetic-English control's range
  (0.0592-0.0705) and well above the periodic-Vigenere-at-period-20 control's pooled IC
  (0.0383-0.0417) or the homophonic control's (0.0400-0.0447) -- i.e. the raw letter statistics of
  the transcribed pages, if case is disregarded, read as ordinary English-level IC, not as either
  flattened design.
- Case-sensitive (K=48) pooled IC (0.0351) sits between the homophonic-English control's range
  (0.0200-0.0228) and the monoalphabetic-English control's range (0.0541-0.0697) -- it does not
  clearly match either; it also does not match the periodic-Vigenere control's flattened range at
  this K (0.0200-0.0253).
- Neither reading shows the period signature (a scan peak clearly separated from the pooled IC) that
  the same scan reliably recovers on real periodic ciphers at this N, even at period 20 -- no
  evidence for periodicity under a simple coset-IC test.
- No single one of the three classical designs Pelling names is confirmed or excluded outright:
  the case-folded reading looks closest to plain/monoalphabetic-level statistics; the case-sensitive
  reading looks like partial but not full frequency-flattening; nothing here contradicts the
  transcribed pages simply being closer to plaintext-level letter statistics than any of the three
  disguising designs at full strength (consistent with, but not proof of, Pelling's and
  SantaColoma's authenticity concerns; also consistent with a genuine but under-flattened
  homophonic or partial substitution design; N=581 from 2 of 8 known pages cannot rule out any of
  these). This is a statistics-only read, not a solve or a decode.

**Requests**: 0 hosts this stage (disk-only; the intake step above made the only network calls).

**Next step** (not run, per brief -- do not run test 2): the spec's own test 2, fetching and
blind-transcribing the six untranscribed pages, would raise N well past 581 and let the periodic
scan and both substitution controls run with much more power, and would show whether the
case/punctuation pattern is internally consistent across all 8 pages.

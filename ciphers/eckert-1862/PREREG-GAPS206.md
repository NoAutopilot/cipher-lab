# PREREG-GAPS206 (eckert-1862, gap 3): 1864 sent-ledger pilot against Cipher No. 1, text route

Written and pushed 4 Oct 2026, 01:5x UTC (clock read 01:52), by worker GAPS206 (STALE4 for account 4, account 1 worker),
before any page text is fetched or any statistic computed. Script: pilot1864/pilot.py (written after this file is pushed).
0 vision, 0 subagents. Requests: hdl.huntington.org, 3 dmQuery calls (one per ledger), >= 1.6 s apart.

## Premise found before writing this
Gap 3's "pilot one 1864 sent ledger (mssEC 18 or 19) against mssEC 41-46" was already done by image on mssEC 19:
ciphers/eckert-1864 (19-20 Sept 2026) transcribed mssEC 41 (Cipher No. 1) in full into key.md and read 20 entries of mssEC 19
at H 298, C 8 (decode.py --check). What is not done: (a) the *text route* -- reading the volunteer transcriptions (Decoding
the Civil War, 2016-17) of a whole 1864 ledger with that key, without new image transcription; (b) mssEC 18 (object 10074),
the parallel 1864-65 sent volume, never opened. This pilot does both, as measurements; it reads no entry as a claim.

## Data (one CONTENTdm dmQuery per ledger, field "transc"; not committed, re-fetch URL in pilot1864/manifest.tsv)
- T  = mssEC 18 (target; never opened).
- R  = mssEC 19 (positive reference; known Cipher No. 1 from March 1864, eckert-1864 section 2). Pages titled before
  "Page 21" (Jan-Feb 1864, old Stager vocabulary) are excluded from R by the page-number rule fixed here: R = pages whose
  title number is >= 21.
- N  = mssEC 15 (null: Feb-Jul 1862, Stager template vocabulary, before Cipher No. 1 existed).
- Key = ciphers/eckert-1864/key.md read with eckert-1864/decode.py's own load_key() and its stem rule (ed/ing/s).
  K* = key code words minus the 1000 most frequent words of tools/data/en (three novels), so plain English words that the
  book also prints (for, this, the ...) do not count.

## Statistics (fixed now)
- S(page) = tokens in K* per 100 alphabetic tokens; pages with < 30 tokens are dropped from every set.
- S1 (gate, positive control first): median S over R pages must exceed the 95th percentile of S over N pages. If not:
  stop, "text route non-test at this key", T is not scored. This control can fail: N uses a different printed vocabulary,
  so its K* rate is not equal to R's by construction.
- S2 (known answer, decode correctness through the volunteer text): for each of eckert-1864's 20 reconciled entries, the
  multiset of keyed meanings that decode.py derives from ciphertext.txt (the image-reconciled H/C reading) is compared
  with the multiset of keyed meanings derived from the volunteer transc of the same CONTENTdm pointer. Recall = shared /
  reconciled, pooled over the 20 entries. Control S2c: the same recall computed against the transc of a mismatched R page
  (each entry paired with 20 random other R pages, seed 206), mean and p95. Gate: pooled recall >= 0.85 AND > S2c p95.
  The control can differ (different page text gives different meanings).
- S3 (target classification): T is "in the Cipher No. 1 vocabulary" if median S over T pages > N p95 (the S1 rule); the
  share of T pages above N p95 is reported beside R's share, by 25-page stretches.
- S4 (is T a duplicate copy of R?): for each T page, the best count of distinct shared word 5-grams with any R page
  (5-grams present on >= 3 pages of either set dropped as boilerplate). Null: the same for each N page against R (1862 vs
  1864, no real shared entries possible); threshold = max(3, null p99 + 1). Report the share of T pages with a twin.
  Positive check for S4: R pages against R itself minus the page (must find no self-hit; skipped) -- instead, the N-vs-R
  null is the only control; a T share near 0 means T carries entries R lacks, near 1 means T duplicates R.

## Outcome wording (fixed now)
- S1 and S2 pass: "the volunteer text of mssEC 19 decodes through Cipher No. 1 with recall X against the image reading
  (control p95 Y)"; S3/S4 as numbers. Nothing is read as a claim, no grade above the key's own row grades, no novelty.
- S1 or S2 fails: non-test; log and stop.

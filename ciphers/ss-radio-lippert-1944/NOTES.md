open

Intake (25 Sept 2026, LANE B3 worker bSSR, minimal check-solved per breadth.md's intake step):
Cipherbrain post "The Top 50 unsolved encrypted messages: 25. The SS radio message" (7 Aug 2017)
and its full 28-comment thread read in full from `sources/schmeh/posts/25-ss-radio.txt` (already
on disk); the post's own text states "The cleartext is unknown" and no commenter claims a
solution -- comments 9-27 instead argue the item is a probable forgery (wrong Fraktur-s usage,
misspelled "Lublin" on the rank stamp, mismatched unit/location, non-standard rank abbreviations,
eagle facing the wrong way; a near-identical forged item later sold on eBay, comment 28). Both
solver repositories grepped (shallow clone, `grep -ril lippert`, deleted after): dbourdeau's
`top50/NOTES.md` and `TARGETS.md` (row 25) both read "probably a forgery ... Treat as
questionable before spending anything on it", no claimed solution of any standing; no match
anywhere in aaymeloglu/unsolved-ciphers. One OpenAlex query
(`search=SS radio message Lippert cipher decrypted`) returned 0 results. One Semantic Scholar
query 429'd twice (one retry after a pause, per the good-citizen rule); not reachable this pass.

Verdict: open, unsolved by any source checked, probable forgery per Bourdeau and the post's own
comment thread (consistent with UNSOLVED-SURVEY.md row 22 and specs/ss-radio-lippert-1944.json).
No Latin-letter transcription of the ciphertext exists anywhere on disk or in either repo; cheap
test 1 (image fetch + blind transcription) is the first thing that can be run.

## Status
open

## Gate check
`python3 tools/intake_gate_check.py ss-radio-lippert-1944` -- pasted below before proceeding.

```
ss-radio-lippert-1944: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

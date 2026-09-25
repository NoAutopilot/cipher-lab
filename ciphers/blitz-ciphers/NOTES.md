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

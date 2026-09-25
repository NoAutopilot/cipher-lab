open

Minimal check-solved (25 Sept 2026, LANE B2 worker bRUB, intake step per `.claude/briefs/breadth.md`, no `ciphers/rubin-1953/` folder existed before this session): Cipherbrain post "The Top 50 unsolved encrypted messages: 9. The Rubin cryptogram" (Klaus Schmeh, 16 May 2018) and its full 7-comment thread read from `sources/schmeh/posts/09-rubin.txt` (already on disk, no fetch needed) -- the post itself states "This cryptogram has never been deciphered" and "unsolved to date"; none of the 7 comments (Thomas, Jemand, Davidsch, farmerjohn, porpen petfukfiri, Klaus Schmeh, KOKO) claims a solution. Both solver repositories grepped for "rubin" (dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers, shallow-cloned to /tmp and deleted after): cyphersolver/top50/NOTES.md and TARGETS.md both carry the row "Rubin, 1953 | low | One typewritten slip ... No claimed solution of any standing"; unsolved-ciphers has zero hits for "rubin". One OpenAlex query (`works?search=Rubin cryptogram solved decrypted`, keyed) returned 7 results, all unrelated (wireless-security/e-voting surveys, none mentioning this case). One Semantic Scholar query (`paper/search`, same terms, keyed) returned 2 results, both unrelated Playfair-cryptanalysis papers. No source consulted claims or shows a solution.

## Status

- **open**. No transcription existed on disk before this session (`specs/rubin-1953.json` `ciphertext_pending`); this pass fetches the better (2018 Bauer) reproduction image and runs a single blind transcription pass (test 1 of `specs/rubin-1953.json`'s `cheap_tests_in_order`). Counts below are single-pass, unreconciled (rule 2); a second pass and reconciliation are test 2, not run here.
- Source: Klaus Schmeh, "The Top 50 unsolved encrypted messages: 9. The Rubin cryptogram", scienceblogs.de/klausis-krypto-kolumne, 16 May 2018 (`sources/schmeh/posts/09-rubin.txt`). Image: https://scienceblogs.de/klausis-krypto-kolumne/files/2018/05/Rubin-Cryptogram.png (Craig Bauer's reproduction for his book *Unsolved!*).
- Established (per Schmeh's post, H-grade from the printed source, not re-verified against the image pixel by pixel this pass): the clear words "Dulles" and "Conant" appear; three pronounceable non-words visible ("frodoscolmn", "astereantol", "matel"); lines of only 0/1/./x characters are present, possibly Morse-like; case is the 20 Jan 1953 death of Paul Rubin, Philadelphia.

## Test 1: image fetch + blind transcription (25 Sept 2026, bRUB)

Fetched `images/rubin-cryptogram-2018.png` (the 2018 Bauer reproduction; manifest in `images/manifest.json`; the
older 2013 photo was not fetched, per the brief, since no line of the 2018 image was unreadable) and ran one
blind transcription pass into `ciphertext.txt`, grade S (cryptanalytic transcription, not from any key), single
pass, UNRECONCILED (rule 2/7: a second pass and reconciliation are test 2, not this session's).

**Discrepancy against Schmeh's post:** the post's prose quotes the pseudo-word as "frodoscolmn", but this pass
reads the image (line 4 of Block A) as **"fodroscolmn"** -- no "r" after the initial "f" -- confirmed on a
2.3x crop (`images/rubin-cryptogram-2018.png` region ~150,90-420,125). Rule 2 (image over transcription):
treating the image as the primary source here since it is directly legible, but flagging the post's wording as
a possible OCR/typo in Schmeh's own transcription of that one word, not corrected without a second pass.

**Line/word structure** (as transcribed; full text in `ciphertext.txt`):
- Block A (letter/word passages), 7 text lines (6, then a blank line, then 1 more): word counts per line
  6, 2, 6, 4, 4, 4, 5 = 31 words total. Case is irregular throughout (e.g. `digIs`, `mathUlley-Dulles`,
  `dzhjellEiE`) -- not normalised, since Bauer's null-letter hypothesis could turn on which letters are
  capitalised.
- One unclear glyph, Block A line 7 (`newtdo sfoatzdexklagh 2pont [SYM1]ly asgestaltverbensdi`): an overstruck
  mark before "ly", crop saved as `images/sym1_crop.png`, catalogued as `[SYM1]` in `ciphertext.txt` and
  excluded from the letter count below. Best guess by eye: a typewriter 1/4-fraction key struck over "l" or
  similar overstrike; not resolved to a specific character this pass.
- Block B: one line of plain digits, `7469921` (7 digits, not 0/1-only, kept separate from Block C per the brief).
- Block C: three lines of only `0`, `1`, `.`, `x` (Schmeh: "might represent a Morse-like code"), lengths 60, 37,
  39 characters; per-line counts (0/1/x/.) are 18/23/7/12, 12/15/4/6 and 10/19/3/7. Pooled across the three
  lines: 40 zeros, 57 ones, 14 `x`s, 25 periods -- ones noticeably outnumber zeros (not close to a 1:1 split).
- Block D: three closing lines -- `Want: datum Tywood Janossey Ketelle` (5 words, plain English "Want:" plus
  four capitalised words that read as invented proper names), `R-QR6` alone, and `aliacaui PER` set to the right
  on the same visual line as `R-QR6` (2 words) -- `aliacaui` is the word a 2018 comment (Thomas, comment #1,
  already on disk in `sources/schmeh/posts/09-rubin.txt`) says Nick Pelling traced to Poul Anderson's short
  story "The Helping Hand" (same 1949 *Astounding Science Fiction* issue as the source for "Deadline"); `PER`
  the post glosses as Paul E. Rubin's own initials (comment #3, Davidsch).
- Bottom-right of the image: an opaque, unpatterned dark rectangular region with no legible marks -- not
  transcribed as text; could be photographic damage/shadow or genuine obscuring, not established which.

**N, distinct K, IC** (`scripts/stats.py`, letters only A-Z case-folded, Blocks A+D pooled, Block B/C and
`[SYM1]` excluded -- reproducible, no network fetch for the controls):
- target: N=305 letters, distinct K=26, IC=0.0612
- English control (`tools/data/pg1661_holmes.txt`, same N=305, 10 random windows): mean IC=0.0621, range
  0.0599-0.0671
- uniform-random control (same K=26, N=305, 5 seeds): mean IC=0.0387, range 0.0376-0.0396 (closed-form
  expectation 1/K=0.0385)
- The target's IC sits inside the English control's range and well above the uniform-random control -- a
  single-pass observation, not a plaintext or cryptanalytic claim (rule 10): consistent with either genuine
  English-letter statistics somewhere in the text (the clear words "Dulles"/"Conant" and Block D's "Want:
  datum..." line already are literal English) or with pronounceable-nulls padding that itself mimics English
  letter frequencies (Bauer's own hypothesis), and this test cannot distinguish the two. No further
  cryptanalysis run this pass (breadth test 1 is transcription + IC only, per the brief).

**Not run this pass** (spec `cheap_tests_in_order` 2-3, left for a future worker): a print-check of Craig
Bauer's *Unsolved!* for an existing transcription or reading; a literal-Morse or simple-binary test of the
Block C 0/1/./x lines.

Hosts: scienceblogs.de, 1 request (the 2018 image fetch; the reachability probe before it does not count per
the good-citizen rule's "test reachability" step). Subagents: 0.


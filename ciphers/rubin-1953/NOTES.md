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

## Test 2: masc family via family_run.py at N=305 (25 Sept 2026, LANE B3 worker bRUB2)

Intake step re-checked: `python3 tools/intake_gate_check.py rubin-1953` -> `rubin-1953: open (line 1) --
edition/page or full-text-search citation found within 6 lines` (exit 0, no change needed).

**Judge block repair** (specs/rubin-1953.json): the placeholder `letters_min`/`letters_max` (20/400, a wide
placeholder written before any transcription existed) is now 280/330, matching the real letter-passage size
(N=305, scripts/stats.py). Added `min_word_cover: 0.5`. `language: "en"` was already set. Checked against a
dummy: a real 305-letter English window from `tools/data/pg1661_holmes.txt` (random offset, seed 42) scores
PASS on all three checks (length, language score=-0.761 vs null_p99=-1.98/real_p05=-0.882, words cover=0.905
vs min 0.5) -- confirms the repaired judge block is not failing closed on genuine English at this N.

**Letters_AD.txt**: Blocks A+D pooled, written to `ciphers/rubin-1953/letters_AD.txt` as the same 9 lines as
`scripts/stats.py`'s `LETTER_LINES` (SYM1 marker and the digit `2` excluded, matching the existing N=305 K=26
IC stats already on file); `tools/family_run.py`'s own letter-fold (`--tokens letters`) strips the remaining
punctuation and the stray digits in `R-QR6`/`2pont` per line. `--tokens auto` was tried first and mis-detects
this text as "space" mode (word-tokens), because `R-QR6` and `2pont` still carry a digit after auto_mode's own
punctuation-stripping regex -- `--tokens letters` was passed explicitly to get N=305 signs, not the word-token
N=39 that auto mode produced on the first attempt (kept as the first HYPOTHESES.md row, labelled accordingly,
so the mode mistake is on the record rather than silently discarded).

**Run 1** (`python3 tools/family_run.py specs/rubin-1953.json --family masc --seeds 3 --gate 0.6 --cipher
ciphers/rubin-1953/letters_AD.txt --tokens letters`): N=305 K=26. CONTROL mean **0.989** (range 0.974-0.997,
English `pg1661_holmes.txt`+`pg2701_mobydick.txt`, 3 seeds) -- **near-ceiling per rule 3's own warning**
(>=95%), so this run has little headroom to show any *gain* from a technique, though it is a plain blind
solve-vs-control comparison, not a gain-gate. TARGET best score -844.061; judge **FAIL** (language:
score=-1.475, null_p99=-1.98, real_p05=-0.882, real_median=-0.809, N=305) -- decode reads as letter salad
(`ciphers/rubin-1953/families/masc-1.txt`... see naming note below).

**Run 2, DULLES/CONANT removed** (`--cipher ciphers/rubin-1953/letters_AD_noclear.txt`): both clear words sit
inside Blocks A+D (DULLES in line 1's "mathUlley-Dulles", CONANT in line 5's "driEk Conant"), so this checks
whether the two known-plain fragments were propping up the first run's result either way. N=293 K=26. CONTROL
mean **0.974** (range 0.928-0.997, same corpora, 3 seeds) -- also near-ceiling. TARGET best score -815.390;
judge **FAIL** (language: score=-1.618, null_p99=-2.0, real_p05=-0.879, real_median=-0.815, N=293) -- same
outcome, decode is letter salad (`ciphers/rubin-1953/families/masc-1-noclear.txt`, preserved by renaming
before it could be overwritten by a same-seed run -- see below).

**File-naming note**: `family_run.py`'s decode file is `families/<family>-<seed>.txt`, fixed by family+seed,
not by `--label` or `--cipher`; both runs used the same default `--seed 1`, so run 2's decode overwrote run 1's
file in place before it could be copied. Run 2's decode was preserved by renaming to `masc-1-noclear.txt`
immediately after; run 1's raw decode text is lost, but its score, control numbers and judge line are on
record in `HYPOTHESES.md` and `cheap_test_done.2`, which is what the brief asks for. A future worker re-running
this family on this target should pass distinct `--seed` values per run to keep both decode files.

**Verdict** (rule 3/brief step d): the target decode is judge FAIL while the control passes (in both the
with- and without-clear-words runs) -- a control-backed negative for simple substitution of English on this
transcription (Blocks A+D pooled, N=305/293). Per rule 5 as amended (LANE B3, 25 Sept 2026): a control above
gate with a target FAIL is a genuine negative, not a "control below gate" case, so this does not by itself
require a NEAR.md `partial` row -- flagged for the orchestrator anyway because both controls are near-ceiling
(0.989 and 0.974 mean), which rule 3 calls out as leaving little headroom; nothing here suggests the masc
exclusion itself is wrong (a near-ceiling control that still finds a language-scoring FAIL on the target is a
sharper negative than a marginal control would be, not a weaker one -- the caveat matters for *gain* gates,
which this is not).

Rows in `ciphers/rubin-1953/HYPOTHESES.md` (both runs, control and target numbers side by side, per rule 3).
`cheap_test_done.2` written in `specs/rubin-1953.json`. Neither NEAR.md, LEDGER.md, ASSIGNMENTS nor status.json
touched (orchestrator's, per LANE B3 common rules).

Hosts: none (no network this test). Subagents: 0.


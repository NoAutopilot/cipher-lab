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


## Web and blog check (GF4-BATCH17 (account-4), 3 Oct 2026)

Plain web searches (WebSearch): (1) `Paul Rubin 1953 cryptogram Dulles Conant solved` -- history.com "When Killers Leave Ciphers", Cipher Mysteries (2015, 2018), Futility Closet (8 Jan 2019), Cipher Foundation page, Grunge listicle, Wikipedia "Unsolved!"; every one says unsolved, none gives a reading; (2) `"fodroscolmn" OR "frodoscolmn" OR "astereantol" Rubin cipher` (the most distinctive pseudo-words) -- Cipherbrain Top 50 no. 9, Cipher Mysteries 2018 posts, Cipher Foundation; no reading; (3) `Rubin cryptogram Philadelphia 1953 Bauer "Unsolved!" decipherment claim 2026` -- Bauer's book pages and the same posts; no 2026 claim found; model-solve family covered by (3) and by klausschmeh.net (the Sept 2026 AI-solve announcements are posted there) below.
Google Books API (`country=US`, keyed, 1 call, `"Rubin" "Conant" "Dulles" cipher`): Bauer, *Unsolved!* (l8iXDwAAQBAJ, 2019 pbk) snippet "...Rubin cipher as the greatest challenge he faced..." with the cipher's DULLES/CONANT lines (FBI cryptanalyst's account, Bauer's chapter); LIFE, 2 Feb 1953 (KUIEAAAAMBAJ), the contemporary report ("Dulles" and "Conant", "apparently a reference to the new Secretary..."). Neither prints a solution in the snippet; Bauer's chapter is the standard modern account and calls it unsolved (Cipherbrain no. 9 quotes it so).
Blog site searches: Cipherbrain (Top 50 no. 9, 16 May 2018, live re-fetch: 7 comments, 16 May 2018 - 31 May 2021): Thomas (Manhattan Project / Astounding Science Fiction idea), Davidsch and farmerjohn ("I saw ... Ulley-Dulles ... met Elli", "today at 2pm fly east") -- fragment guesses, no method, no response from Schmeh; klausschmeh.net `?s=Rubin`: Nothing Found (no 2026 solve post); Cryptiana blog `?q=Rubin`: no posts; Cipher Mysteries `?s=Rubin` (one 406 with a browser UA, one 200 with the descriptive UA): 4 Rubin posts -- "The cipher on Paul Emanuel Rubin's abdomen" (15 Feb 2015), "The Secret History of Paul Rubin, perhaps?" (22 Feb 2015), "Paul Rubin's cipher, revisited" (3 Jan 2018: 160-page FBI FOIA file obtained by Craig Bauer, FBI linguists' languages and methods tried; 2 comments, no reading), "Cracking the Paul Rubin Cipher" (5 Jan 2018: Pelling reads "aliacaui" as a word from Poul Anderson's 1950 story "The Helping Hand", the signature as "aliacaui PER" = Paul Emanuel Rubin, and 7469921 / R-QR6 as codebook-style indices -- a partial interpretation, explicitly not a decipherment; 12 comments 6 Jan 2018 - 23 Jul 2023: Rafal (invented language, "saw thing"), Charlotte and Hassan Boyouk ("aliacaui" as element symbols Al-I-Ac-Au-I), Amos G. -- none accepted by Pelling). Reddit r/codes (OAuth search `Rubin`): one thread, "The Cipher of Paul Emanuel Rubin, 18." (7 Jun 2022, flair Unsolved, 2 comments: a transcription from the linked PDF, nothing else).
Solver repos (fresh shallow clones, 3 Oct 2026): dbourdeau/cyphersolver HEAD 841111b (2 Oct 2026) -- research/top50/NOTES.md row 9 "low ... No claimed solution of any standing", hcportal index entry only, no targets/ folder; aaymeloglu/unsolved-ciphers HEAD d2800bb (27 Sept 2026) -- no "rubin" anywhere. DECODE: no hit in the on-disk listings (sources/decode/*.tsv, 0 for "rubin"); a 1953 typewritten item is outside DECODE's usual scope.
Requests: klausschmeh.net 1, cryptiana.blogspot.com 1, ciphermysteries.com 4 (incl. the 406) + 2 WebFetch, scienceblogs.de 1 WebFetch, oauth.reddit.com 1 (thread), googleapis.com 1, github.com 2 (clones, shared with yogtze-1984); all >=1.5 s apart.

## Premise check (GF4-BATCH17 (account-4), 3 Oct 2026)

(a) Folder's own mentions of a decipherment or clear copy: not found -- NOTES.md and the spec mention only the clear words Dulles/Conant and pseudo-words; nothing called a decipherment.
(b) Other solvers' working files: not found -- Bourdeau has only a list row ("no claimed solution of any standing"), no working folder; Aymeloglu nothing; Pelling's 2018 partial interpretation ("aliacaui" from Poul Anderson, PER signature, codebook-index-like strings) is the nearest thing to working files and is not a reading.
(c) Physical neighbours: the slip is a single typewritten sheet; its "neighbours" are the 2013 photo and Bauer's 2017 reproduction (images/rubin-cryptogram-2018.png on disk). No clear copy or decipherment is reported beside it in any source read.
(d) Recipient/investigator side: found but not a decipherment -- the FBI FOIA file (~160 pp., obtained by Craig Bauer, described by Pelling 3 Jan 2018) records the FBI's own failed attempts (languages tried, frequency counts); LIFE 2 Feb 1953 reports the case. The file itself was not located online in this pass (Pelling's post links only the Cipher Foundation page); reading it is the next zero-dependency step.
Result: no premise find; status stays open.

## Verdict (GF4-BATCH17 (account-4), 3 Oct 2026)

**open (unchanged).** No published or accepted decipherment located in Bauer's *Unsolved!* (Google Books snippet, chapter on the Rubin cipher), Cipherbrain no. 9 and its full 7-comment thread, klausschmeh.net, Cryptiana, Cipher Mysteries' four Rubin posts and their threads, Reddit r/codes, DECODE listings, or either solver repository, searched 3 Oct 2026. Claimed-but-unaccepted interpretations: Pelling 2018 (partial: "aliacaui", PER signature); comment-thread guesses 2018-2023 (Davidsch, farmerjohn, Rafal, Charlotte, Boyouk) -- recorded as claimed, none accepted.

## While waiting (GF4-BATCH17, 3 Oct 2026)

Nothing here waits on a person; the one zero-dependency step is to locate and read the FBI FOIA file on Rubin (Bauer's ~160 pp.; try the FBI Vault search for "Rubin", Cipher Foundation's page, and Bauer's *Unsolved!* notes for its citation) for the FBI's transcription of the original slip, which would settle the 2013-photo vs 2018-reproduction letter disagreements before any second transcription pass.

## Intake gate (GF4-BATCH17, 3 Oct 2026)

$ python3 tools/intake_gate_check.py rubin-1953
rubin-1953: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0

$ python3 tools/next_steps.py --wait-only | grep rubin-1953
(no line)

## Next step (NO-CRACKS, 5 Oct 2026)

next: locate and read the FBI FOIA file on Rubin (FBI Vault search "Rubin", Cipher Foundation page, Bauer's Unsolved! notes for its citation) for the FBI's transcription of the slip, settling the 2013-photo vs 2018-reproduction disagreements, ~$1. Who acts: agent. Source: this file's "## While waiting (GF4-BATCH17)"; written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.

## FBI file located and read (D2B-RUBIN, LANE DEFAULT-account-2-20261005-2217, 5 Oct 2026)

**Located.** The FBI file is hosted by the Cipher Foundation: page http://cipherfoundation.org/modern-ciphers/paul-rubin-cipher/ ("This 142-page file was provided by the FBI in response to a request for information by Craig Bauer for his book 'Unsolved!'") links http://cipherfoundation.org/wp-content/uploads/sites/4/2017/12/Paul-Rubin-FBI-file.pdf (142 pp., 8,937,411 bytes, sha256 97f7e115...bf18a; stamped "NW 42555 DocId:32608295", the NARA JFK-collection release numbering; FBI file 65-61458). Route: Cipher Mysteries 3 Jan 2018 post -> Cipher Foundation page -> PDF. The PDF is not committed (re-fetchable; manifest in images/manifest.json); the four pages carrying a copy of the slip are rendered at 120 dpi in images/fbi-file-p-{050,051,067,138}.png. The PDF has no text layer; OCR'd locally with tesseract (scratch only) to find the pages, then the pages read by eye.

**What the file holds about the slip (FBI specimen Q5; page numbers are PDF pages):**
- p.132: Philadelphia SAC letter, 20 Jan 1953, sending "one piece of white unruled paper, 7" X 3½" ... undecipherable typewritten letters and numbers" for cryptographic examination. p.140/86: Laboratory work sheet, Q5 "Document composed of letters and digits".
- p.88: memo of 21 Jan 1953 to R. T. Harbo: the Cryptanalysis-Translation Section "did not disclose any valid translation or decryption ... Although there appear to be possibilities of small segments of several different languages in Q5, no comprehensible translation could be effected"; a name check on TYWOOD JANOSSEY KETELLE found nothing on the first two and nothing connecting the KETELLE references to Q5.
- p.64: report: "no decipherments were effected. If a secret message was actually intended, it would appear that the 'system' was either irrational or too complex to permit successful analysis of such a limited amount of text."
- pp.45-48: typewriter comparison. K1 (Royal, serial AG 2088346, property of a friend) was not the machine that typed Q5; K2 (Rubin's own Underwood) could be neither identified nor excluded ("a number of typewriting characteristics ... common to the typing on Q5 and K2 and ... no significant differences").
- **No photograph of Q5 itself is in the PDF** (searched by OCR for the slip's words; only the copies below carry its text). The FBI's own transcription exists in three forms: K1 (p.51) and K2 (p.50), agent-typed copies of Q5's text made as typing exemplars on 29 Jan 1953 (with false starts and retyped lines), and p.67, the cryptanalyst's hand-lettered capitals working copy with pencilled glosses; p.138 is a second, rougher hand copy.
- p.67 glosses (the FBI examiner's guesses, recorded as claimed, not readings): DIGIS "EIGHT?", KKIQTU "QUIT", DESCETH "DEATH?", ALBAWMNABS "(Albany)", MEIKTRENE "(MIKE)", OIER "(Pier)", IELLI "(Kelly)", METEORE "(meet)", MALZBOURGNION "(SALSBURG?)", 2PONT "DUPONT", 1/4LY "QUARTERLY", ASGESTALT... "GESTALT (configuration)" and "Yiddish influence?", KETELLE "CATELLE? (jargon Catholic-psychologist?)", ALIACAUI PER "Paul E. Rubin", CRANCKLAVN' "(Jewish/Yiddish? influence)".

**Comparison with ciphertext.txt** (per position in `variants-fbi-1953.tsv`; ciphertext.txt NOT edited, rule 2). There is no 2013-photo transcription on disk to set against the 2018 one (bRUB never fetched the 2013 photo), so the comparison is ciphertext.txt (2018 reproduction) vs the three FBI witnesses, with the 2018 image re-checked by eye at 2x on each disputed word:
- **[SYM1] resolved:** all three FBI witnesses read the typewriter one-quarter key: `2pont ¼ly` (CR brackets [1/4LY], gloss QUARTERLY). Confirms bRUB's best guess. Grade: transcription evidence from three independent 1953 copies of the original slip.
- **`ungdreabozvmie` -> FBI 3/3 `ungdreabozvnie`** (K1 has `ungereabozvnie`, a retyping slip in the 4th letter). The 2018 image is blurred at that glyph. Candidate correction, held for a second image pass; the FBI copies were made from the slip itself, the 2018 image is a later reproduction.
- **Supported as transcribed:** `greA'Lltenmn` (CR LLTENMN; K1/K2 `Lternmn`/`Ltermn`/`Ltrrmn` are typing slips), `albawmnabs` (CR; K1/K2 transpose to `albawnmabs`), `meteore` (CR, K1; K2 `metore`), `7469921`, `R-QR6`, `fodroscolmn` (all witnesses; Schmeh's "frodoscolmn" is his typo, as bRUB said).
- **Leading mark in `'sawthn'g`:** visible in the 2018 image, absent from all three FBI copies -- possible blemish on the reproduction; grade M.
- Block C (0/1/./x lines): K1, K2 and the image agree in the parts compared by eye; not checked character by character this pass (CR's hand copy is too faint at 120 dpi for that).

Requests: ciphermysteries.com 1 (301 -> 200), cipherfoundation.org 4 (page, PDF, two images; one image was a 1953 vital-records document, not cipher material, not kept), all >= 1.5 s apart; web search 1. Subagents 0.

## Next step (D2B-RUBIN, 5 Oct 2026)

next: second blind transcription pass of the 2018 image (and the 2013 photo, scienceblogs.de/klausis-krypto-kolumne/files/2013/11/Rubin-Case.png) at the `vmie/vnie` glyph and Block C, then reconcile against variants-fbi-1953.tsv and update ciphertext.txt with the ¼ glyph and any settled letters, recorded in NOTES.md; ~$1.5. Who acts: agent.

## Second pass and reconciliation (D2B-RUBIN2, LANE DEFAULT-account-2-20261005-2217, 6 Oct 2026)

Intake gate (00:1x UTC 6 Oct): `rubin-1953: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.

**Crop step** (pasted): `python3 tools/iiif_lines.py --image images/rubin-cryptogram-2018.png --out images/crops2018 --prefix r18 --debug` -> 12 lines, centres 22 52 77 106 134 164 216 294 353 408 457 545; `python3 tools/iiif_lines.py --image <2013 photo as RGB> --out images/crops2013 --prefix r13 --debug` -> 5 bands (the 2013 slip is rotated about 12 degrees inside a newspaper photo, so the line finder cannot separate its lines). Targeted sub-crops were then cut with PIL into `images/crops2/`: the end of Block A line 3 at 5x, Block C lines at 3-4x (line 1 in two overlapping halves), and the 2013 slip deskewed with Block C at 4x. Subagents got only these crop paths, never a full image.

**2013 photo fetched** (scienceblogs.de .../2013/11/Rubin-Case.png, 1 request, `images/rubin-case-2013.png`). It is a newspaper (Bulletin) halftone of the slip held in a hand, with "Dulles" and "Conant" circled by the paper's artist. **It cannot witness the vmie/vnie glyph**: Block A line 3 runs to the slip's edge and is cut at "ungdreaboz". Block C is legible only in fragments.

**Blind passes** (two Sonnet subagents, crops only, made before variants-fbi-1953.tsv was opened in this session; the brief's order):
- 2018 image, end of Block A line 3: reads `gdreabozvmie oie`. The letter after `v` is read as **m at medium confidence**: "about 2 clear vertical stems plus a dark blob at the left joining the v", with **n or a v+n overprint not excluded**. Together with bRUB's pass 1 (m) and D2B-RUBIN's 2x re-check ("blurred; m or n"), the 2018 reproduction leans m but cannot decide.
- 2018 image, Block C: `100.011x100.10x.10011.1.xx0.101.x.001011.101x1011.1001..10x1` / `01.001011x10.1x.11101.x1.001x1.001001` / `0.101.x.101110.x101.1101101.0101x1.1011`. That is **identical to ciphertext.txt (bRUB pass 1) on all 136 characters** (60/37/39). The subagent placed the half-line join at medium confidence. The joined line is the same string as pass 1, made independently.
- 2013 photo, Block C: fragments only. The subagent itself graded every character M with ">=25% per-character error". The legible pieces are consistent with ciphertext.txt (line 1 begins `100.011x10`, the right of line 1 reads `1.x.001`, line 3 ends `101x1.1011`). Nothing there contradicts the 2018 reading, but it is not a per-position witness.

**Reconciliation against variants-fbi-1953.tsv and the FBI copies** (K1 p.51 and K2 p.50 Block C read character by character by eye this session; CR p.67 too faint at 120 dpi, not compared):
- **vmie/vnie -> ciphertext.txt changed to `ungdreabozvnie`, grade M on that glyph.** Witnesses for n: FBI K1, K2 and CR (3/3, all copied from the original slip in Jan 1953; K1/K2 are typing exemplars and may derive from one reading, CR is the cryptanalyst's own copy). Witnesses for m: the 2018 reproduction (three image passes, at most medium confidence, n never excluded). There is no 2013 witness. The image cannot decide, and the copies made from the original agree, so n is taken. The variant m stays in the tsv.
- **[SYM1] -> ciphertext.txt changed to `¼ly`**, from FBI 3/3 plus the 2018 image's overstrike shape (D2B-RUBIN). The ciphertext.txt header comment called this glyph "block C line 1". It is Block A line 7, and the comment is corrected in the same edit and named here.
- **Block C: no change.** The 2018 image (two independent passes) is supported at every position. K1 and K2 each drop a character the other copy and the image both have (K2: the period after `100.10x`, line 1 char 16; K1: the period after `10.1x`, line 2 char 16; K1: the `1` in `0101x1.1011`, line 3 char 34). These are single-copy typing slips of the same kind D2B-RUBIN found in Block A. Rows have been added to variants-fbi-1953.tsv.
- `scripts/stats.py` hard-codes its letter lines and does not read ciphertext.txt, so its N=305 figure is unchanged by these edits. The m->n swap does not change N (it is one letter for one letter). The IC moves trivially and has not been recomputed. The letter lines are not updated. No reading is claimed and no decode script exists, so rule 7 `--check` does not apply.

Hosts: scienceblogs.de 1 (2013 photo). Subagents 2 (Sonnet, blind crop reads).

## Next step (D2B-RUBIN2, 6 Oct 2026)

next: CR p.67 Block C character by character, from the PDF re-rendered at 300 dpi for that page only (re-fetch the PDF from cipherfoundation.org, 1 request; render p.67, rotate, crop Block C). This settles the last witness on the three single-copy K slips and checks the vmie/vnie glyph in the cryptanalyst's own hand at full resolution, ~$1.5. Who acts: agent. Transcription is otherwise reconciled. The letter-text is unchanged in substance, so any cryptanalytic test is unblocked.

## CR p.67 at 300 dpi (R8-RUBIN3, LANE LANE-RUN8-account-2, 6 Oct 2026)

Intake gate (03:1x UTC 6 Oct, pasted by the lane): `rubin-1953: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.

**Fetch and render.** The FBI file PDF was re-fetched once from cipherfoundation.org (HTTP 200, 8,937,411 bytes, sha256 prefix 97f7e1153505, identical to D2B-RUBIN's copy). It is not committed (manifest only). Page 67 was rendered with `pdftoppm -f 67 -l 67 -r 300` (3521x4963), rotated 90 degrees (PIL `rotate(90, expand=True)`), and Block C cropped to (0,2120)-(4500,2580). **Crop step** (pasted): `python3 tools/iiif_lines.py --image blockC.png --out cropsC --prefix crC --debug` -> 3 lines, centres 78 220 346, 2 overlapping segments each. The crops, plus the A3 `...vnie oie` strip, are in `images/crops300/` (248 KB, manifest entry `crops_300dpi_p67_2026_10_06`).

**Blind passes** (two Sonnet subagents, crops only, on-disk Block C not shown to them):
- Pass A: `100.011x100.10x.1.0.011.1.xx0.101.x.001.011.101x1011.1001.10x1` / `0.001011x10.1x.11101.x1.001x1.001001` / `0.101.x.101110.x101.1101101.0101x1.1011`.
- Pass B: `100.011x100.10x.10011.1.xx0.101.x.001.011.101x1011.1001..10x1` / `0.001011x10.1x.111101.x1.001x1.001001` / `0.101.x.1011110.x101.1101101.0101x1.1011`.
- Both passes read the A3 strip as `UNGDREABOZV.NIE OIE`, with N after the V, about 90% (two verticals joined by a diagonal, with a small dot between the V and the N).

**Reconciliation** (1 unit; worker's eye on 2-3x zooms of each disputed spot). The passes disagree with each other and with the disk at six spots. Five of them resolve in favour of ciphertext.txt:
- L1 `10011` and L1 `001011`: the extra marks the passes read as '.' are small pen specks at the baseline inside the group. The same speck appears inside `011` in group 2, which no reader splits. The deliberate separators are larger round dots. Disk stands.
- L1 `1001..10x1`: there is a round dot followed by a tick, so two marks. Disk stands (pass B).
- L2 `11101`: an eye count at 2x shows three bars, then 0, then 1. Pass B's `111101` double-counted the segment overlap. Disk stands.
- L3 `101110`: an eye count shows 1 0 1 1 1 0. Pass B's `1011110` added a bar. Disk stands.

One spot is a CR-only difference:
- **L2 char 2.** The disk reads `01.`, and so do the 2018 image (2 passes), K1 and K2. CR writes `0`, then a pencil circle drawn round an empty space, then `.`. This is the examiner's own mark, perhaps flagging a faint or doubtful character on Q5. It is recorded as variants row C2b. ciphertext.txt is not changed: four witnesses against one, and CR shows no letter there, only a circle.

**The three single-copy K slips (C1, C2, C3)** all read with the disk in CR: the period after `100.10x` is present, the tick after `10.1x` is present, and the `1` in `0101x1.1011` is present. Each slip position now has the 2018 image, CR, and the other K copy against one K copy. The variants rows are updated.

**vmie/vnie.** CR's own hand at 300 dpi shows a plain N: two blind reads at about 90%, plus the worker's eye. This confirms the CR witness behind D2B-RUBIN2's change at full resolution. The glyph stays **grade M**, because the 2018 reproduction still leans m and no image of Q5 itself exists in the file.

**Result:** ciphertext.txt is unchanged. Block C (136 characters) is supported at every position by the 2018 image (2 blind passes), CR at 300 dpi (2 blind passes plus reconciliation; 1 position is circled and blank in CR only), and K1/K2 (one single-copy slip each at 3 positions). No reading is claimed, so rule 7 does not apply.

Hosts: cipherfoundation.org 1 (PDF). Subagents 2 (Sonnet, crops only).

## Next step (R8-RUBIN3, 6 Oct 2026)

next: the transcription is reconciled against every witness in the FBI file. The remaining doubt is one M glyph (vnie) and one CR-circled position (L2 char 2), and both are settled only by an image of Q5 itself (FBI specimen, not in the released file), so no further transcription pass is useful. Cryptanalytic test: Block C as Morse-like or binary (0/1 as dot/dash or bits, x/'.' as separators) against an English decoder with a matched control of the same length and symbol design, ~$2. Who acts: agent.

## Block C as Morse-like or binary (R9-RUBIN4, LANE LANE-RUN9-account-2, 6 Oct 2026)

Intake gate (05:15 UTC 6 Oct, pasted by the lane): `rubin-1953: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Spec test 3 (`specs/rubin-1953.json`), not run before this session (cheap_test_done had only 1 and 2).

**Pre-registration.** `blockc/PREREG-blockc-morse-binary.md` and `scripts/blockc_test.py` were pushed in f8965389d (05:59 UTC) before
the scored run. Disclosure: a smoke run of the pipeline (50 shuffles, 20 controls) was made before that push, to check it executes. It
showed target numbers of the same shape. No encoding, statistic or gate was changed after it.

**Design.** Block C has 136 characters: 31 runs of 0/1 (97 bits) between '.'/'x' separators, with line breaks counted as separators.
There are k = 74 encodings:
- Morse in both polarities. Separator roles do not change the letter sequence, so they are not counted separately.
- Each run read as a binary number, A1Z26, in both polarities.
- 5-bit Bacon (26 and 24 letters), 5 offsets x 2 polarities.
- ITA2 letters shift, 5 offsets x 2 polarities x 2 bit orders.
- 7-bit and 8-bit ASCII bitstreams, every offset x 2 polarities.

The statistic T is the mean log10 4-gram probability from `tools/judge_plaintext.py`'s NgramModel (en corpus), with each undecodable token scored -3.0.
- The null is 3000 permutations of the 136 characters.
- The control is 200 English windows, encoded in the same design and cut to the same 31 tokens or 97 bits.
- Gate: p_shuffle < 0.05/74, T >= the control's p05, control power >= 0.8, and no more than 5% of shuffles reaching the control's p05.

**Result** (`blockc/results.tsv`; `python3 scripts/blockc_test.py --check` exits 0):

| | target | control | shuffle |
|---|---|---|---|
| encodings that are tests (control power >= 0.8) | 74/74 FAIL | power 0.995-1.000 on all 74 | 0/3000 reach control p05 on every encoding |
| best encoding, ITA2 p1 o3 lsb | T -1.477, p 0.0040 (alpha 0.00068) | median -0.823, p05 -1.036 | median -2.168, theta -1.397 |
| ITA2 p0 o0 lsb | T -1.503, p 0.0063 | p05 -1.029 | theta -1.415 |
| Morse p0 / p1 | T -2.273 / -2.373 | p05 -0.947 | median -2.43 / -2.38 |

- **No target decode reaches its control's p05, and none clears the Bonferroni threshold.**
- In Morse, 8 (p0) or 7 (p1) of the 31 runs (every run of length 6-7, plus some 5-element runs) decode to nothing in the table. The letter-only decode is `DWDN?TEK?KYXNTA?...` (p0) and `WDWA?ETR?...` (p1).
- All 74 target decodes are in `blockc/target_decodes.tsv`.
- **Reading:** this is a control-backed negative for direct Morse/binary-to-English readings of Block C under these 74 encodings, conditional on the transcription (rule 2: no image of Q5 itself exists in the FBI file).
- **What it does not test:**
  - a second layer on top of the Morse or bits, such as a substitution or a key: 31 tokens is far too short for a keyed search with a control that reads;
  - a language other than English;
  - a code-number meaning for the runs.

The ITA2/Bacon p-values near 0.004-0.01 do not survive correction across 74 encodings, and those decodes are not English-range.

Hosts: none (offline). Subagents: 0.

## Next step (R9-RUBIN4, 6 Oct 2026)

next: the cheap tests in `specs/rubin-1953.json` are all run (1-3; test 2's print check of Bauer's *Unsolved!* for a published transcription or reading is listed in the spec but its cheap_test_done "2" holds the masc run instead -- check whether the Bauer print check itself was ever run before any further cryptanalysis; ~$1, agent). Block C under a keyed second layer is too short to test with a control that reads.

## Bauer print check (R11-RUBBAU, 6 Oct 2026)

Question (R9-RUBIN4's next): was the Bauer, *Unsolved!* (2017), Rubin chapter ever checked for a published transcription or reading? Answer from the folder and ROOM.md: only as one Google Books snippet call (GF4-BATCH17, 3 Oct 2026, section "Web and blog check"); spec `cheap_test_done` "2" is the masc run, so test 2's print check had no entry (label corrected in the spec as `2_note`).

Run now (snippet searches only; no page was read, no loan taken):
- Google Books API (`country=US`, keyed, 6 calls): volume l8iXDwAAQBAJ (*Unsolved!*, 2019 pbk, PARTIAL view) answers the Rubin/Conant/Dulles query with a snippet from the chapter (p.300: the FBI cryptanalyst's account, DULLES / FEBRUARY 1953 / CONANT lines of the reproduced slip). Queries for `fodroscolmn`, `frodoscolmn`, `inauthor:Bauer intitle:Unsolved Rubin cipher` and "null letters ... pronounceable" returned 0 hits; `"Ulley-Dulles"` returned only unrelated volumes (Dept of State Bulletin 1956 etc.).
- Internet Archive: advancedsearch finds `unsolvedhistorym0000baue` (Bauer, *Unsolved!*, 2017; 1 request). be-api full-text search inside that item (7 requests): index entry "Rubin, Paul Emanuel, 289-304, 546n97"; "Rubin, Bessie, 294-297"; snippets on the Dulles/Conant names, the FBI contact, "died under circumstances presently unknown", and Bauer's "...the Rubin cipher as the greatest challenge he faced. At least I presume it was the Rubin cipher." The queries "Rubin message recovered", "Rubin solution unsolved", "Rubin Philadelphia Morse", "fodroscolmn" and "Ulley-Dulles" returned no hit in the book.
- What is shown: the chapter runs pp.289-304 (notes 546n97) and reproduces the slip; the snippets show no plaintext reading and no decipherment claim. What is not shown: the full chapter text (pages are not readable from the cloud: the IA copy is lending-only and the borrowed page images are obfuscated, CLAUDE.md access playbook), so the chapter's closing paragraphs and any partial reading in prose are unread. A snippet search with no hit is a search result, not a statement about the chapter.
- Requests: googleapis.com/books 6; archive.org advancedsearch 1; be-api.us.archive.org 7 (all >= 2 s apart, no 429/403).

Remaining unread piece: pp.289-304 of Bauer in full, owner-side only (reader view of the IA loan, a person's eyes); not queued here (no ASKS/LOCAL-QUEUE row written; probe not needed, the block is the documented obfuscation).

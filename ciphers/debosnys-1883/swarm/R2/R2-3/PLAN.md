# R2-3 CRIB-LENGTH: pre-registration (DEB-SWARM2-R2-3, written 29 Sept 2026 07:18 UTC, before any real-text score)

Brief: DIGEST-1.md "Round-2 prompts", R2-3. Public copies only. Grade S; nothing here is a reading.

## Target profile (fixed now)
- c4 verse = 20 lines in `ciphertext_c34_draft.tsv` (settled), order c4a0_L01, c4a_L01..L14, c4b_L01..L05 (verse 1-20, H7).
- Per line: sign count after dropping the H5 punctuation set {BLOB, HOOK-L, DASH-H, _, MULTI} (anywhere in the line) and
  any clear_spans.tsv position; trailing '?' stripped from ids.
- Line-final sign: last sign after dropping trailing punctuation (H5 rule), full id.

## Statistic (fixed now; same code for target, controls and decoys)
A window = 20 consecutive verse lines of a text (blank lines and title-like lines dropped; windows start on every line).
- Length term R = max(r_letters, r_syll): Pearson r of the 20 cipher line lengths against the window's per-line letter
  count and against its per-line vowel-group (syllable) estimate. Word count is not used.
- Rhyme term P = phi coefficient over the 190 line pairs between "cipher line-final signs equal" and "window rhyme keys
  equal" (rhyme key: lower-case letters of the last word, French trailing -s/-x/-nt/-e(s) dropped, then the last vowel
  group plus what follows).
- Score S = R + P. Also reported separately: R alone (the running-key and word-scramble safe part).

## Known-answer control (run first; the real search is run whatever it shows, but read only through it)
Source windows from the candidate pool (seeded pick, 5 per language, EN and FR), each enciphered three ways and passed
through 15 pct noise (replacement : insertion/deletion = 3 : 1, DIGEST-1 section 2):
 (a) homophonic letters (letter -> one of k homophones, k by frequency, about 60 signs), (b) running key (sign = letter +
 key letter mod 26, key from another pool text), (c) syllabic homophones (vowel-group syllable -> code; extra, not asked).
Rank of the true source window among all decoy windows (decoy texts only, disjoint from the pool), and among a 1,000
random subsample. **Control pass: median rank 1 among 1,000 decoys for (a) and (b)** (the brief's "must rank top").
If the control does not pass, the instrument cannot see a copied poem at this length and noise, and any real negative is
logged "untestable by this instrument", not a negative.

## Kill test (stated before looking)
Real: score every window of every candidate-pool text against the c4 profile. **Kill: the best candidate window's S is
not above the decoy windows' 99th percentile.** Because the best of many windows is compared, a second, stricter number
is also reported: the share of equal-size random draws from the decoy windows whose maximum is >= the best candidate
(max-corrected p). A hit needs both: above p99 and max-corrected p < 0.01; even then it is a crib for the scorer and two
audits, not a reading.

## c2
c2's line breaks are page layout (prose), not verse lines, unless the image shows otherwise; the length profile has no
meaning there. c2 is reported as not tested by this instrument unless c4 gives a candidate text to align.

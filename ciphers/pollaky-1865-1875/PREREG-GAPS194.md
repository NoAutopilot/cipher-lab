# PREREG-GAPS194 -- gap 2 (d): ad 2 group structure against period codebooks (pushed before any statistic is computed)

Written 3 Oct 2026 (clock read 18:3x UTC), worker GAPS194-pollaky-1865-1875 (account-4). Script only, 0 vision calls.

## Material
- Target: ad 2 (Times, 20 Feb 1871), the 36 digit groups of ciphertext.txt line 39, "9:77314" taken as two groups
  (9, 77314) as in the 36-count; sensitivity: one group 977314.
- Books: every IA item returned by the pre-set advancedsearch queries run 3 Oct 2026 for telegraph/telegraphic
  code, cipher or vocabulary, 1840-1871 (5 queries; requests logged). Two codebooks found, djvu text fetched once
  to scripts/codebooks/: F.O.J. Smith, *The Secret Corresponding Vocabulary* (1845, secretcorrespon00smitgoog;
  pre-1871) and R. Slater, *Telegraphic code, to ensure secrecy* (IA copy 1888, telegraphiccodet00slatuoft; first
  edition 1870, so this copy's numbering is a proxy for the 1870 one -- a caveat on every Slater number).
  The Mercantile Navy List "Commercial Code of Signals" items are flag-hoist letter signals, not number codes: out.

## Statistic (S0, group structure)
For book B with highest code number R_B (read by script from the parsed number column; Smith: naked numbers are
phrases per its own preface, word codes need a letter prefix that ad 2 lacks, so R_Smith = phrase count),
S0 = number of ad 2's 36 groups with 1 <= value <= R_B. A message written one group per code number, plain or with
an additive key that wraps inside the book (Smith's preface describes the reversal rule), has S0 = 36.

## Controls (both can differ from the target on S0 itself, rule 3)
- Positive (power): 2000 windows of 36 consecutive words of English prose (tools/data English corpus) encoded
  through B's own word->number list (words absent from B skipped), plain and with a random additive key mod R_B;
  S0 for each. Power = share with S0 >= gate.
- Null: 2000 synthetic 36-group messages with ad 2's own digit-length profile, each group uniform within its
  digit-length class (leading digit nonzero); S0 distribution, p95 reported.

## Gate and what it licenses
- Gate: S0_target >= 34 (two transcription/print errors allowed) AND positive-control power >= 0.8.
- PASS for B: ad 2 is structure-compatible with B; the next step (not run here) is a decode with B's list scored
  against the same null. A PASS is not a reading.
- FAIL with power >= 0.8: ad 2 is not a one-group-per-code-number message in B's numbering (plain or additive
  wrapping key). Licenses nothing about groups made of several concatenated codes, other books, or 1870 Slater
  numbering if it differs from the 1888 copy. Logged as excluded for B only, not a design-family negative.
- Power < 0.8: non-test.
- Note: the target's raw values are visible in the transcription, so the S0 outcome is predictable once R_B is
  read; this is a structural screen whose value is the named books, R_B and the controls, not a blind test.

## Rule-3 third-attempt clause
No earlier attempt used this instrument (codebook range/structure screen) on gap 2: GAPS156 (bigram IC),
GAPS164 (Boyouk alignment) and GAPS169 (digit-sum substitution) are different instruments. Not retired; runs.
Rule 5: target stays `partial` whatever happens. Rule 10 wording only.

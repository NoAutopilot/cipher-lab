# Pre-registration RUN3-ECK62 (4 Oct 2026, 08:50 UTC; committed before the guard or the book assignment is run)

Worker RUN3-ECK62 (LANE-RUN3, account 1). Committed before any guarded decode or book-assignment number is computed.

## (a1) Possessive option (ciphers/eckert-1864/decode.py, `possessive=True`)
A token whose core ends in `'s` (straight or curly apostrophe) and is not itself in the key is looked up without the
`'s`; a hit is rendered `[meaning]'s` with the row's grade. Off by default, so eckert-1864's reading.md is unchanged.

## (a2) Collision guard (ciphers/eckert-1864/decode.py, `guard=CollisionGuard(...)`)
Corpus: word unigram and bigram counts (lowercased `[a-z]+` after deleting apostrophes) of five 1862 OR ser. I volumes,
IA `warofrebellionco0007vari`, `warofrebellion09secrrich`, `...10secrrich`, `...11secrrich`, `...12secrrich` `_djvu.txt`.
None can print an mssEC 18 (1864-65) telegram, so the corpus is not the answer print.
Applies only to keyed tokens of kind `word` (numerals, time words, punctuation and signature are never guarded).
Let w = the code word as written (lowercase, with its ending), p = the previous word as read (the last word of the
previous token's meaning if keyed, else the plain word; none at entry start or after a brace), n = the next word as
read (first word of the next token's meaning if keyed, else the plain word). m1 / m2 = first / last lowercase word of
the meaning with parenthesised notes removed.
- Rule J (joined word): leave w plain when w joined with its plain left neighbour, its plain right neighbour, or both
  (the neighbour itself unkeyed) forms a word of >= 7 letters with unigram count >= 2.
- Rule B (bigram context): P = c(p,w) + c(w,n), K = c(p,m1) + c(m2,n). Leave w plain when P >= 3 and P > 2K.
A guarded token is written as the clerk wrote it, ungraded (not counted in H/C/I/M).

Known answer (before running): the 26 print-aligned entries' tokens in `align_tokens.tsv` as committed by A3V3-ECKC.
Report: COLLISION word-kind tokens caught (9 in align_tokens.tsv: whack, white, summit, animals, subject, opinion, passed,
John, Hotel; the tenth COLLISION row, persons, is a numeral and out of scope by construction) and AGREE word-kind tokens wrongly
guarded (false positives), both numbers. The guard is used in ec18.py's outputs only if FP <= 5% of AGREE word tokens;
otherwise it is reported and left off (`--guard` not used for the committed outputs).

## (c) Book assignment for the '?' entries (ec18.py `--assign`)
For each '?' entry (no marker words), decode with key.md and with key-no2.md (possessive on, guard as decided above).
Score per book = number of keyed word-kind tokens whose meaning's content words (ec18.meaning_words) occur in the OR
window of the entry's own print match (ec18.agreement window, j-150..j+450). Assign the book with the higher score
when the difference is >= 2; else stay '?'. Only print-matched '?' entries (all-entries matcher, OR vols. 32-49) can
be assigned; unmatched ones stay '?'.
Known answer first: the same rule on the print-matched entries whose book IS known from markers (book 1 and book 2),
markers ignored: accuracy reported; the rule is used on the '?' entries only if known-answer accuracy >= 0.85 with
>= 20 decided.
Control (rule 3 orthogonality: must be able to differ): the same score computed against a different matched entry's
OR window (rotation by one within the '?' set). Under the control the meanings are unrelated to the window, so the
share of entries decided (difference >= 2) should fall; a decided rate under the control near the real rate means the
assignment is reading window size or entry length, not content, and it is not used.
Grades: an assigned entry's tokens keep the key row's grade from the assigned book (H only where mssEC 41 / mssEC 47
gives the value), but the entry is flagged `book=1a`/`2a` (assigned by print) so the book itself is S, not H.

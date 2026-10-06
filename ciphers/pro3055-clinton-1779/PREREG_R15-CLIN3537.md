# PREREG R15-CLIN3537 (6 Oct 2026, written before any decode was scored)

Target: 3537 (PRO 30/55/30/26, Clinton to Haldimand, New York, 31 May 1781) as printed in VHS Collections II (1871) pp.339-341
(cipher specimen) and pp.341-342 (translation), archive.org `collectionsofver02vermuoft` djvu OCR text, fetched once.

Parse (fixed): stream from the line after the specimen heading "New York, May 31, 1781." to the line before "Sir Henry Clinton to
Gen. Haldimand." (translation heading). A line matching `^\D{0,2}(\d{1,2})\s*[—–~-]+\s*(\d{1,2})\D{0,2}$` is a full pair (line, pos); a
line matching `^\s*[—–~-]+\s*(\d{1,2})\s*$` is a continuation (the previous line number); every other line holding a digit is
unparsed and counted; alphabetic lines are clear words and close a segment. Page furniture ("The Haldimand Papers.", 340, 341)
is dropped. No hand repair of the OCR.

Decode (fixed): letter = position P of the letters-only (a-z, &) text of title line L of passes/title1778_reading.txt (the 1778 key);
a cell beyond its line's end gives "?".

Statistic S = LCS(decoded letters, translation letters) / len(decoded letters), translation = pp.341-342 body from "Your letters"
to "H. C.", letters only, lowercased. Control (can vary on S's own axis): the translation's letters shuffled, 1000 seeds, same S.
Gate: PASS if S_target >= 0.80 and S_target > the control maximum. Second number reported (not gated): decoded runs of >= 5
letters found verbatim in the translation, target vs control mean.
Key report: after a Needleman-Wunsch alignment (match +2, mismatch -1, gap -1), every cell whose decoded letter differs from the
aligned translation letter is listed with key_2894.tsv's letter for that cell; grade at most M (OCR figures), no key change.

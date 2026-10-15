# PREREG CLIN-3502 (15 Oct 2026, 13:0x UTC by date -u; written before any look at p.299 at reading size and before any pass or score)

Job CLIN-3502, LANE DEFAULT-A1-1140-15 (account 1). Item: **B.147 p.299** (H-1649 Image 945, IIIF c0222r583783), the OPENING page of
the cipher copy of item 3502 (PRO 30/55/29/83; New York, 8 May 1781; Discovery "Seven pages of coding"; the 1781 letter VHS Collections
II prints as Beverly Robinson to Haldimand, GAPS11). Text-known item (lane guardrail): a key-consistency check, no reading changes,
AUDIT.md not touched. Seen before this file: one 1000 px look at Images 945, 953, 954 side by side (to find the frames: 945 is p.299,
"N. York May 8th 1781", eight ruled figure columns, address "His Excellency General Haldimand"; 953 is p.306, an account; 954 is p.307,
the second letter in clear) and the three crops of Image 955 (p.308) read for the known answer. Nothing of p.299 at reading size.
Per the brief, only p.299 is done if it runs over; the rest of the seven pages is named, not done.
**Known answer:** passes/p308_reading.txt BODY..END (the first page of the period decipherment, B.147 p.308, read by this worker before
any pass; letters only, spaces, digits and punctuation removed, '&' kept, spelling as on the page). p.299 is the cipher's first page and
p.308 the decipherment's first page, so p.299's runs are expected inside p.308's text; p.309 is not read. A run whose text lies on p.309
counts as a miss; that is accepted as a bias against PASS, fixed now and not changed after scoring.
**Design:** PREREG-CLIN-3004.md (CLIN-SIB's design, reused by CLIN-3004/3004B/3004C) unchanged, with the known answer switched to p.308:
key title1778_reading.txt as printed (variant a) GATED, variant (b) reported; rule R0 cell classes; statistic B2 (a run = >= 3 all-H
letter cells, not crossing a column, ended by an underline or a non-letter cell; a hit when its decoded string is a substring of the
p.308 letters); page-permuted-key control (1000 seeds, seed 123); prechecks can-differ >= 0.99 and runs_ge3 >= 10, else NON-TEST;
**gate: B2 share >= 0.60 AND hits > control max.** Threshold not re-tuned.
**Method, as Addendum CLIN-3004C:** one 3200 px fetch; each figure column cut as ONE crop (tools/iiif_lines.py --image --region
--centres; command pasted in NOTES before the first subagent call); ONE blind Sonnet pass on the crops only (no key, no decipherment,
not told the question, asked to flag every unsure cell; struck rows as kind `struck`); one worker reconciliation unit on 2x zooms,
image only, BEFORE any decode or score; a cell still open is graded M (excluded from runs). No cell is changed after the scorer is
first run. Scorer passes/check_p299.py (check_p232.py with input, output and known-answer names changed; --check exits 1 when stale).
A PASS says only that the 1778 key reads these runs as the p.308 text beyond the permuted-key control. A FAIL or NON-TEST is logged
as such with both numbers.

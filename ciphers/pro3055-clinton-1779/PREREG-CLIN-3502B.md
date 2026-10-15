# PREREG CLIN-3502B (15 Oct 2026, 14:4x UTC by date -u; written before any look at p.300 at reading size and before any pass or score)

Job CLIN-3502B, LANE DEFAULT-A2-1410-15 (account 2). Item: **B.147 p.300** (H-1649 Image 946, IIIF c0x921d0fz0x), the SECOND page of
the cipher copy of item 3502 (PRO 30/55/29/83; New York, 8 May 1781). Text-known item: a key-consistency check, no reading changes,
AUDIT.md not touched.
**Screen (done before this file; one 600 px-per-frame montage of Images 946-952, nothing read at reading size):** 946 = p.300, eight
ruled figure columns (cipher); 947 = p.301 (cipher); 948 = p.301 again (a refilm of the same page); 949 = p.302 (cipher); 950 = p.303
(cipher, ends with initials and the endorsement "From Sir Henry Clinton ... 8th May ... in Cypher"); 951 = p.304, a second letter
headed "N. York May 8th 1781", figure columns with a clear left margin note, address "His Excellency General Haldimand"; 952 = p.305,
its end (figure cells, then a clear passage on money paid to Canadian officers, "H C", "P.S. The Messenger has received the Money
here", "fo. 255 blank", endorsement). So the 3502 cipher runs pp.299-303 (five pages, Images 945-947, 949-950) and pp.304-305 are a
second cipher letter of the same date. The brief allows the first two cipher pages after p.299 (pp.300, 301); by the per-unit cost
rule (start-up ~1 + ~1.4 per page against cap 4, 80% = 3.2) **only p.300 is run**; p.301 is named, not done.
**Known answer:** the period decipherment from where p.299's runs stopped: passes/p308_reading.txt BODY from the line "by extending
her breadth on both" to END, plus passes/p309_reading.txt BODY..END (read by this worker on two 2400 px crops of Image 956 before any
look at p.300 at reading size). Letters only, '&' kept, spelling as on the page. A run whose text lies before "by extending" on p.308
or on p.310 (not read) counts as a miss; accepted as a bias against PASS, fixed now.
**Design:** PREREG-CLIN-3502.md unchanged (key title1778_reading.txt as printed, variant a GATED, variant b reported; rule R0 cell
classes; statistic B2: a run = >= 3 all-H letter cells, not crossing a column, ended by an underline or a non-letter cell; a hit when
its decoded string is a substring of the known-answer letters; page-permuted-key control, 1000 seeds, seed 123; prechecks
can-differ >= 0.99 and runs_ge3 >= 10, else NON-TEST). **Gate: B2 share >= 0.60 AND hits > control max.** Threshold not re-tuned.
**Method:** Image 946 at 3200 px (already fetched); each figure column cut as ONE crop with tools/iiif_lines.py --image --region
--centres (command pasted in NOTES before the subagent call); ONE blind Sonnet pass on the crops only (no key, no decipherment, not told
the question, asked to flag unsure cells; same prompt and TSV columns as CLIN-3502's p299_passA.tsv); one worker reconciliation unit on
2x zooms of the flagged cells, image only, BEFORE any decode or score; a cell still open is graded M. No cell changed after the scorer
is first run. Scorer passes/check_p300.py (check_p299.py with input, output and known-answer names changed; --check exits 1 when stale).
A PASS says only that the 1778 key reads these runs as the period decipherment's text beyond the permuted-key control.

# PREREG BAL-E293 (15 Oct 2026, account 4, for LANE DEFAULT-A4-0645-15), written 07:5x UTC by date -u, before any image is fetched

Question (a): is the E-shaped sign at c293 (`41' 23' 6 E 4 γ 16 40' 16 y` under "le fort au dela du Rhin", BAL-C286) the same sign as the
ball-foot E of the c268 exemplars (R21 `20: 77' E 73' 8` "partie soit"; `42' E` garentis line) and as the c275 E (R17, "attendre", no letter left)?
Material: openapi.bnf.fr IIIF v3 btv1b9001489r f293, f268, f275 at full/2400, one at a time, >= 3 s apart, 3 requests (the folder's Verdict names
"regen from images/manifest.json"; the job line's "disk" could not be met, none of these canvases is on disk -- declared deviation, inside the job's
6-request host cap; the remaining 3 are kept for 169). Scratchpad only, never git.
Rule (a): one look per E on a 2-4x crop, the three side by side (one composite), compared on four features fixed now: (1) ball/loop foot present,
(2) number of strokes in the upper bowl(s), (3) a cross-stroke or bar, (4) relative height vs the same line's plain 6. "Same" = all four agree
between c293 and the c268 exemplars; "different" = (1) or (3) differs; otherwise "undecided". c275 is compared the same way.
--try (only if c293 E is "same" as the c275 E): `decode_key.py --try s:E=NULL` on the c275 run. Power control FIRST: --try's own rule makes
n = 1 undecided by construction; the c275 run holds one s:E. If the control shows --try cannot return accept/reject for a planted NULL at n = 1,
the target --try is logged "non-test at n = 1" and not run as evidence (rule 3, a control that cannot vary). Power control: a pseudo-code planted
at 1 position in the c275 run as a true insertion (NULL), and at 1 position replacing a key-H e; record both verdicts.
Gloss tally (C grade, no cryptanalysis): E rows with unit e vs unit '-' in c275g/glossed_pairs_g.tsv after this job; a value reaches key.tsv
only through --try at every occurrence (brief). Nothing enters key.tsv or exceptions in this job unless --try accepts.
(b) only if (a) finishes inside about half the cap: 169 f.36-38 / f.208-209 glossed 13: and plain 65, same rule as BAL-C275G (>= 3 glossed
occurrences at >= 3/4 for S; count_shuffle_g.py 200-seed shuffle). Stop before any step crossing 80% of $3 or of the box (07:54-08:54 UTC).

# PREREG SHERWOOD-PAGES (18 Oct 2026)

Hypothesis (named in the brief, .claude/briefs/runs/2026-10-18-acct4-research-director-14.md, before any page was fetched):
the Cossit/Summer cypher (BL Add MS 21838 pp.345-347) is the Haldimand-Clinton book cipher keyed to the title page of
*A List of the General and Field Officers* (1778), figure pairs = line (1-29) and letter-in-line.
Instrument: title_key_test.py (key from ciphers/pro3055-clinton-1779/passes/title1778_reading.txt).
Control: the same tokens with the key's line order shuffled, 20 seeds; metric share of pairs in range and English cover.
Note: this file was written after the run; the hypothesis, instrument and control are the brief's, fixed before it.

## Decision
Belief: the cypher is not the 1778 title-page system; it is a word code from an alphabetical dictionary (page-word), because first figures run to 472 and rise with the spelling of the words Sherwood's own sketch gives.
Would change it: the title key reading pairs at more than the shuffled control's in-range share (0.014-0.047) with any English cover above 0.
Observed: title key target in_range 9/214 = 0.042, English cover 0.000; 20 line-shuffles in_range 0.014-0.047, English cover 0.000 (mean 0.000); 197/214 pairs have a first figure > 29. Alphabetical-order check: sketch alignment rho 0.998 vs permuted control mean 0.003 (p<0.0001, N=34, alignment ours, M); p.347 period glosses rho 0.429 vs 0.004 (p=0.21, N=6, not significant).
Decision: stop -- the title-page key is excluded by range for this item; next is identifying the dictionary (page-word, >=472 pages, <=38 words a page) from the gloss and sketch values, a different instrument.
Lesson: before applying a line/letter title-page key, check the range of the first figure (max 29 here); a page-word dictionary code looks like figure pairs too.

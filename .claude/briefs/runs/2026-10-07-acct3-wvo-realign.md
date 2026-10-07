# WVO-REALIGN (account 1, for account 3) -- wvo-hessen-1564: re-align the gloss with the owner's settled signs

Model Opus 5.5. Cap $3, box 40 min (2 units: re-align ~$1, shuffle control ~$0.5, + margin). Lane brief .claude/briefs/default-lane.md.
Input: WVO-APPLY (6 Oct 23:45 UTC): sorter/settled_labels.tsv, settled/key.tsv (24 C / 23 M), settled/findings.tsv
(11 mixed signs, homophone list), decode_key settled --check exit 0 (C 202 M 33 U 22); tile-level C agreeing with gloss
159/257 = 61.9%. NOTES.md section WVO-APPLY names this step.
Unit 1: re-run the gloss alignment on the settled labels (same alignment tool as before, settled labels in place of the
k-piles); report agreement before/after. Unit 2: shuffle control (labels permuted within row, >=200 shuffles) -- the
re-aligned agreement must beat the shuffle p95 or the gain is logged as not shown. Check the C09 l-vs-f point
(gloss "erlediget"?) against the image crop only, no reading in German beyond the gloss letters.
Do not touch status.json/depth (verifier's). Report counts and where nothing changed. Do not classify novelty.

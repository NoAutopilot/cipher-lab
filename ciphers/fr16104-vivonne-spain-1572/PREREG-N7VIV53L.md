# PREREG-N7VIV53L (4 Oct 2026, N7-VIV53L, account 2 worker for LANE-NEAR7)

Written and pushed BEFORE any look-alike re-read, audit re-read or re-decode of ink 53 (fr.16104 ff.170r-171v). The N6-VIV53 /
N6-VIV53B readings (reading_piece53.tsv, piece53_decode*.txt) were on file and seen when this was written; the label rules below are
chosen from the brief and the key image, not from which reading decodes better. key.tsv unchanged. Nothing that regenerates
reading_piece53/54/63.tsv is edited. All new files carry `53L` in their name.

## Inputs (frozen)
tx/rec_<page>/ciphertext_draft.tsv for f170r f170v f171r f171v (tools/reconcile_passes.py on the _c passes, N6-VIV53/53B), the line crops
regenerated from images/p53/manifest.json's commands (NOTES N6-VIV53 / N6-VIV53B), tx/SIGNS.md. Reader A / reader B = the draft sign /
the `B:` alt; passC = the N6 reconciled sequence (tx/reconcile_vivk.py rules + RULES54 + MAP, i.e. exactly what tx/viv54_decode.py
page_tokens() decodes, before the "o o" -> "oo" join).

## (i) Label rules
1. **The ': :' pair is ONE sign.** Two consecutive ':' tokens in one line (after the look-alike fold-in) are joined into one token
   ':' before decoding = Tomokiyo key cell **col c, row 1** (the ".." two-dot sign, value c; key.tsv code ':'). Grade of the joined
   token: H only if both constituents would be H, else M. Applied mechanically to every such pair; a run of three ':' joins the first
   two only. Disclosed: N6-VIV53 saw the pair decode as "cc" ("dicct", "ccest"); the rule follows the key image's single ".." cell and
   SIGNS.md's own definition of ':' as one two-dot sign, not a re-score. The pair is not otherwise re-read; if it is a null + c (the key's
   null column carries a vertical dotted sign), that is a key question left M (listed in NOTES, not settled).
2. **a/u, 4/+/p, z/3, S/d (and every other split): settled only by tools/lookalike_pass.py's fixed 2-of-3 rule** (`reconcile`): a firm
   (H/M) look-alike re-read that matches reader A or reader B settles the tile; anything else keeps passC and stays M (flagged). Nothing
   is settled by "what decodes better". The re-read is value-blind (candidate ids and SIGNS.md shape descriptions only, no key values,
   no decode shown). '+' (one reader's token for the crossed-descender sign) and 'u' (not a SIGNS.md token) are candidates like any
   other; after the fold-in, tx/reconcile_vivk.py's MAP still applies ('{t}' -> 4, 'u' -> a, 'Y' -> y, 'q' -> @) and '+' -> 4 (the
   crossed-descender sign of SIGNS.md, as '{t}'), applied to the label after the vote, not as a vote.
3. Grades as tx/viv54_decode.py: H = settled (agree, N6 label rule, or look-alike 2-of-3 / confirm) AND code grade C in key.tsv; M =
   M code (S, y, b, A) or unsettled; U = code not in key.tsv. "o o" -> "oo" as before.
4. Planted-audit corrections (iii) are NOT applied to the primary reading; flagged agreed signs are listed only.

## (ii) D2-candidate statistic (listed by this worker; the auditor re-counts)
On the re-decode's letter string per line-joined page (unread codes shown as '_', breaking a stretch), a stretch = a maximal run that
splits into words of a vocabulary = tokens of tools/data/fr16 (the three PREREG-N6VIV63 files) with count >= 5, one-letter words only
'a' and 'y', u/v and i/j identified, by DP (tx/viv53L_stretches.py). The candidates are the longest such runs, in letters. For each of the
top 10 the list gives: letters, decoded string, word division, and every liberty as AUDIT 2 4a counts them -- word division (always),
each u/v or i/j identification, each M-graded token inside it, each look-alike-settled token inside it, each joined ': :' inside it, each
stretch crossing a line end. A stretch needing any letter substitution is not repair-free and is not listed as such (by-eye readings that
need repairs are listed separately with the repair count). The vocabulary is a liberty too: a short-word run of letter salad can split
into fr16 words by chance -- control: the same statistic on 200 letter-order shuffles of the re-decode (seed "20261053L"); report the real
top-1/top-3 lengths beside the null's median and p99. No gate: descriptive, for the auditor.

## (iii) Error measure
`tools/lookalike_pass.py audit` on signs both readers and passC agree on, whole piece, --sample 100 --plant 0.05 --seed 53 --k 3, ONE
Sonnet re-read call; `audit-score` with its fixed 0.80 planted-catch gate. If catch < 0.80 the audit is a non-test (reported as such).
If it passes: true-error estimate on agreed signs = flagged unplanted / unplanted sampled (with a binomial 95% interval), reported beside
the two-reader rate err_2reader (before) and the look-alike 2-of-3 residual (after), which are agreement, not accuracy.

## (iv) b2 + specificity, rule unchanged from PREREG-N6VIV53B
On the re-decode of the whole piece (ff.170r-171v): (b-ii) b2 (tx/viv63_test.run unchanged, fr16, 200 letter-order shuffles), pass = s >
null p99, controls C1 f.103r and C2 ink 54 run first at full length exactly as N6-VIV53B (fail or no headroom -> "not a gate"); (c) 200
wrong keys (key.tsv values permuted, unread set unchanged), each through b2; pass iff real margin > wrong-key margin p99. Seed string
"20261053L" (new seed, same draws). (b-i) is not repeated (no unseen page). "piece 53 ready for audit (depth re-check)" only if (b-ii) AND
(c) pass. The N6-VIV53 gloss gate (0.577) stands and is not re-run as a gate; if a label rule changes a glossed position, the six gloss
windows are re-scored descriptively only.

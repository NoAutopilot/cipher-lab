# PREREG-N7VIV54L (4 Oct 2026, N7-VIV54L, LANE-NEAR7 worker, account 2) -- ink 54 look-alike pass and re-decode

Target: ink piece 54, BnF fr.16104 f.173r-v (7 Sept 1572, Saint-Gouard to Charles IX). Written and pushed BEFORE any look-alike
re-read, audit re-read or re-decode exists. Inputs frozen at this commit: tx/f173r|f173v_pass{A,B}_c.tsv, tx/rec_f173r|f173v/
ciphertext_draft.tsv (N5-VIV54), tx/reconcile_vivk.py RULES + RULES54 + MAP, key.tsv (not edited), images/c187_f173r_*, c188_f173v_*.
The committed reading_piece54.tsv / tx/viv54_decode.py are not touched; the re-decode is tx/viv54L_decode.py -> reading_piece54_L.tsv.

Before this file: tx/viv54L_prep.py (adapter, changes no label) and `lookalike_pass.py confusion` over all 18 pages' alignments
(tx/lookalike54/confusion.tsv) were run. Neither is a decode. No decode of ink 54 other than N5-VIV54's committed one has been seen.

## (i) Label rules (fixed now; nothing is settled by what decodes better)
- **L1, the ': :' pair = ONE sign, key cell ':' -> c** (key.tsv row ':' = c, Tomokiyo col c, "two dots"; tx/SIGNS.md: ':' is "two dots
  side by side"). The two readers transcribed each dot as its own token (pass A ':' ':', pass B 'o' 'o' at the same places, f.173r L05;
  RULES54). Rule: in the line sequence after the existing label rules, every run of two consecutive ':' tokens is replaced by one ':'
  (greedy left to right: ': : :' -> ': :'). Its grade is M if either input token was flagged, else as usual. A lone ':' stays ':' (c).
  Known limit stated now: where BOTH readers wrote 'o o' for a dot pair it becomes 'oo' (u) and cannot be told from u by this rule.
- **L2, splits and one-pass gaps** (all pairs, including the named a/u, 4/+/p, z/3, S/d): settled only by `lookalike_pass.py
  reconcile`'s fixed 2-of-3 rule on one value-blind re-read per page (a firm H/M re-read equal to reader A or B wins; else UNSETTLED,
  pass A's committed label kept, graded M, written to focus.tsv). No split is settled by eye in this job.
- **L3, packet scope**: `packet --top 0` -- every unsettled split and every one-pass gap is a tile; candidates = A, B, committed label
  and the label's two commonest confusion partners (tx/lookalike54/confusion.tsv). Agreed signs are not relabelled by this job.
- **L4, the audit is a measurement only**: its flags are reported (and written as a pointer sequence) but never applied to the re-decode.
- **The a/u "qae" target, stated in advance**: in "to z m" (decoded q-a-e) both readers wrote z (key a) -- the confusion table holds no
  a/z or u/z split anywhere on 18 pages, so the 2-of-3 rule cannot produce u there. If the look-alike re-read gives no firm alternative
  that equals a reader's label, it stays z/a and goes to the NOTES section as a **key question** (is there a z-like u homophone in
  Tomokiyo's cell u, or does z stand for u after q?) -- never repaired to u in this job.
- Grades in reading_piece54_L.tsv: H = both readers agree, or an N5 label rule settled it, or look-alike 2-of-3 settled it, AND the
  code is grade C in key.tsv; M = code grade M (S, y, b, A), or unsettled, or L1 merged a flagged token; U = code not in key.tsv.

## (ii) D2-candidate statistic (listed, not judged; the auditor re-counts)
Vocabulary V = every word of length >= 2 occurring >= 3 times in tools/data/fr16 (the three PREREG-N6VIV63 files), plus "a", "y", "o",
lowercased, accents folded, letters only; u/v and i/j folded as the decode (key.tsv has no v, j). A **repair-free stretch** = a maximal
substring of a line-joined page decode (U positions break a stretch; M positions do not, and are counted) that a DP segments entirely into
words of V with at least 3 words. Ranked by letters. For the top 10 on the re-decode and on the committed N5-VIV54 decode, listed: letters,
word division as segmented, number of words, number of M letters inside, any ': :' collapses (L1) inside, and the number of 1-2 letter
words. Word division is always a liberty; nothing else is applied (no letter repairs). **Control on the same statistic:** the same DP on
200 letter-order shuffles of each page decode (seed "20261054L-stretch"); report the null's longest-stretch median and p99 beside the real
longest. AUDIT 2 4a's authentication distance (~42 letters) is the reference line; whether any stretch is a clause is the auditor's call.

## (iii) Error measure
`lookalike_pass.py audit` over the whole piece (lines prefixed f173r_/f173v_), A/B = the _c passes, C = the committed sequence,
--sample 80 agreed positions, --plant 0.05, --k 3, --seed 20261054, one value-blind Sonnet call; `audit-score`: catch >= 0.80 or the
audit is a NON-TEST. Reported: planted catch, unplanted flag rate (flags / unplanted items) as the true-error estimate on agreed signs,
beside the look-alike 2-of-3 residual (unsettled / all signs), which is agreement, not accuracy. err_2reader (1 - agreed/columns, as
N5-VIV54) is reported before and after.

## (iv) b2 + specificity on the re-decode, rule unchanged from PREREG-N6VIV53B
b2: s = mean log10 4-gram probability per letter (tools/judge_plaintext.py NgramModel on tools/data/fr16) of the key.tsv re-decode of
f.173r-v; null = 200 letter-order shuffles; pass = s > null p99. Positive controls first, same code path, committed sequences unchanged:
C1 = f.103r (tx/f103r_rec.tsv), C2 = ink 53 whole piece ff.170r-171v (tx/viv53_decode.py page_tokens). Control fails / headroom < 0.01 /
null median > s -> "not a gate". (c) specificity: 200 wrong keys = key.tsv's values permuted across its codes, each through b2 on the
re-decode; pass iff the real margin (s - p99) > the wrong-key margin p99. Seed base "20261054L". The same b2 + (c) is also run on the
committed N5-VIV54 sequence (before), descriptive. "piece 54 ready for audit (depth re-check)" only if b2 passes as a gate AND (c) passes
on the re-decode.

## Units (cap USD 4.5, box 12:17-13:36 UTC)
Scripts: prep, confusion, packet x2, audit, reconcile, decode, tests. Subagent calls: 1 re-read per page (f.173r, f.173v; crops of the
flagged lines only + the candidate sheet), 1 audit re-read, ~USD 1.2 each; 1 reconciliation by this worker (script + listing) = 4 units.

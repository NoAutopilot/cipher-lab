# PREREG-BAL-GSEQ (BAL167-GSEQ worker, LANE DEFAULT-A2-2013, account 2), written 13 Oct 2026 21:2x UTC by date -u,
# pushed in its own commit BEFORE balshape/gseq/settle_gseq.py is run on anything

Target: the gloss letter over the "gt" (g+) sign on Baluze 170 f.124r (2 tokens) and f.124v (1 token), the exemplars for the f.228v g+
class (3 tokens, value n, Tomokiyo channel, grade M). Brief: .claude/briefs/runs/2026-10-13-ytbiz-default-2013-jobs.md "BAL167-GSEQ".
Rule 3: PREREG-BAL-GPLUS (a)'s x-position rule was the first instrument (NOT SETTLED, BAL167-GVER); this word-level, key-anchored
sequence rule is the second, a different instrument. Data: ONLY BAL167-GVER's two blind reads already on disk
(balshape/gplus/glossA.tsv, glossB.tsv); no new subagent read. The f.228 value is not an input to the rule.

## Input (balshape/gseq/runs.tsv)
One row per gt token per read (6 token-reads). Per read: that read's own cipher-sign labels on the strip, left to right, and that read's
own gloss word over the token's run (word level, where both reads agree: c131 'consentent' / 'longues', c132 'conclusion'; read A gives
'consentent/consistent' as alternatives, read B spells 'consintent'). Transcription rules fixed here:
- M1: an unmarked numeral N is taken as N' (acute; the reads disagree on marks: A '76 with accent', B '76'); plain/diaeresis values unused.
- M2: read A's c132 sign 6 is 72', read B's is 42' -- each read keeps its own label.
- M3: letter-shape signs (h, q, K, u4/4u, crossed y, Z, 3i, partials) carry no value in this rule: each consumes exactly one letter. Their
  S values from BAL-WL (h n, q c, u4 a/t) are NOT used, so the result does not lean on earlier tile tests.

## Sequence rule (balshape/gseq/settle_gseq.py)
Per token-read: anchor = the first sign on the strip whose key.tsv H acute value is an exact prefix of the gloss word. From the anchor,
consume the word left to right: an H sign consumes len(value) letters; any other sign one letter (M3); the gt token consumes one letter, and
those letters are its leftover. Mismatches between an H sign's value and the letters it consumes count against a tolerance of TOL = 1 per
word (handwritten-gloss e/i slips, e.g. B 'consintent' vs 71' se). A word-internal token is valid only if the word is used up exactly with
no sign overrunning it. The line-final c131 token (under 'longues', the last sign on the strip) is valid if the consumption reaches the
strip's end after the token (the word continues on the next line, off the strip). With alternative words (read A), the token-read gives a
letter only if every alternative that aligns gives the same one.
**SETTLED** only if all 6 token-reads give exactly one letter and it is the same letter (all 3 tokens, both reads), AND the controls below
pass. Anything else: NOT SETTLED, g+ stays M, logged in HYPOTHESES.md, no tile read.

## Controls (same script, same run)
- C1 known answer (rule 3, a control that can fail differently): in each aligned word-internal run, each H-valued sign strictly between the
  anchor and the gt token is blanked to an unknown of its own value's length (its key value removed), gt becomes a one-letter wildcard, and
  the rule must return letters within TOL of the blanked value. Gate: recovery >= 0.80 of blanked signs.
- C2 shuffled key (false-settle): the H values of all acute codes in key.tsv are permuted (1000 permutations, seed 20261013) and the full
  settle rule is run per permutation. Statistic: how often a wrong key still SETTLES (all 6 token-reads one common letter), plus the
  per-token-read rate of a single word-consistent leftover. Gate: false-settle <= 0.05. This control can differ from the target: a wrong
  key moves the anchor and the consumed lengths, so alignment fails or the leftover letter changes.
- Stated limit: the lengths are fixed by the key and M3, so the leftover's position is arithmetic; what the rule tests is that the gloss
  letters opposite each H sign match its key value (within TOL) and what letter is left opposite gt. M3's one-letter assumption for
  letter signs is untested here.

## If SETTLED
If the settled letter is n: run PREREG-BAL-GPLUS (b) exactly as written (tiles with balshape/gplus/tiles_gplus.py [seed]; exemplar E-g+
f.124r first gt; T 3 f.228 g+; P+ the other two f.124 gt; P- within-key look-alikes crossed y = r (f.229, f.228 decoy), r-shape = g
(f.239r), bare g only if forced; gates G1 P+ >= 0.75, G2 P- <= 0.25 and <= P+ - 0.50; one second read only within the 80% line; adoption
of the 3 f.228 tokens M -> S only if all three T confirmed). If the settled letter is not n: value conflict logged, nothing regraded.
AUDIT.md not touched. Caps: USD 3.5, box 21:16-22:16 UTC (80% 22:04). Units: this settle (script, ~0.2), tile build + 1 tile read (~0.7),
+1 read if a gate fails.

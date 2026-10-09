# PREREG-MANT0290W (9 Oct 2026, 18:27 UTC by date -u; written before any score; LANE FAMILY-A2k account 2)

Leaf: HStA Dresden 10026 Loc. 694/08 frame 0290 (17 Sept 1712), right page. Disk only, no fetch. Inputs exactly as committed by MANT-UNG:
f0290_08/gloss_spans_A.tsv and gloss_spans_B.tsv (the two blind gloss passes' notes as written, by position; never settled by this worker),
key.tsv at origin/main as of this commit (unchanged). Script: f0290_08/word_gate.py (sha256 prefix 0ac08db2ebc17cbe), committed with this file.

## Why a new gate
MANT-UNG's gate (a) scores a letter-by-letter alignment; it FAILed 2/12 and 3/15 because codes 281-674 under 'Reve aux guerriers du nord'
are word/syllable codes, which a letter statistic cannot credit. A nomenclator's test is code-to-word consistency across leaves.

## Statistic (fixed now)
- Token = each code token inside a gloss span of the pass (span gloss g, all codes in the span carry g).
- Witnesses elsewhere: every gloss span containing the same code on another leaf, from exactly these files (frozen; 0290 excluded; files
  other jobs add after this commit are not read): f0136_08/gloss_spans, f0312_08/spans_G1+G2, f0314_08/spans_G1+G2, f0474_08/gloss,
  f0494_08/gloss (left and right page), f0089_08/gloss_spans, f0136_09/gloss_A, _B, _A1A, _A1B, f0007_09, f0008_09, f0056_09, f0063_09
  gloss.tsv; plus the CUC clear-under-code strips (mant0608/cuc/agreed.tsv + clear_blind.tsv, cuc3_agreed.tsv + cuc3_clear_blind.tsv).
  Print spans (0136, 0383) are not glosses and are not read.
- Words: lowercase, accents stripped, v->u, j->i, y->i, split on non-letters, length >= 3, a fixed French stopword list removed (in the
  script). Two words match if equal, one is a prefix of the other (abbreviation: mant/manteuffel), or they share the first 4 letters.
- A token is consistent if any word of its 0290 note matches any witness word of its code. S = consistent tokens; K = tokens whose code has
  at least one witness elsewhere.
- Control: the 0290 notes permuted across the pass's gloss-bearing tokens (the code-gloss pairing shuffled), 1000 draws, seed 2900.
- Classes (CLAUDE.md rule 3 per-class breakdown): letter (key.tsv first value <= 3 letters), keyed-word (longer key value: names, words),
  unkeyed (absent from key.tsv: the word/syllable codes the brief asks about). Per class and pooled: S, K, control mean, p99, min, max.

## Gate (fixed now)
- Per class: PASS if S > p99 and S >= 0.5 x K; K < 5 -> untestable (said so, neither PASS nor FAIL); control min == max -> non-test by
  construction (the shuffle cannot move the statistic for that class; rule 3 orthogonal-control paragraph). Deciding row = the LOWER of the
  two passes per class.
- Orthogonality, stated before scoring: the statistic depends on which note sits over which code; the control changes exactly that pairing,
  so it CAN differ from the target whenever a class has witnessed tokens and the notes differ across tokens. Checked numerically (min/max).
- Expected limits, stated before scoring: (1) the keyed-word class is dominated by name codes 160/155/257 whose meaning the key already gives;
  a PASS there is a known-answer check of the method, not evidence about 281-674 (AX-NAMES shape). (2) Letter-class tokens inside a phrase
  span have phrase witnesses unrelated to the letter; that class is expected near the control. (3) The unkeyed class answers the brief's
  question; if it has K < 5 it is untestable on disk, and the next step is more glossed witnesses of codes > 230, not a re-tuning of this gate.
- Grades (rule 4): nothing here moves a token above M, and key.tsv is not changed. An unkeyed code consistent under a PASSing unkeyed class
  would be listed in f0290_08/candidates.tsv as M with its witnesses.

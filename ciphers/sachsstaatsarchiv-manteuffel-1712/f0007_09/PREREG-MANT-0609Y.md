# PREREG-MANT-0609Y (9 Oct 2026, written before any 0007 score was computed; LANE FAMILY-A2d account 2)

Leaf: HStA Dresden 10026 Loc. 694/09, URL file 0007 (film Aufnahme 0008; sha256 prefix a663edb45ed902fa), "No 1. a Berlin ce 7 janv. 1713",
recto of the letter whose verso is file 0008 (f0008_09, MANT-0008 PASS 159/205 vs shuffled p99 46).
Question: on this leaf's own glossed code groups, does Krauske's table (key.tsv at origin/main 5674c2912) agree with the period gloss?
The gloss is the known answer (prior-work: text KNOWN from the gloss for these tokens).

Inputs fixed before scoring:
- codes: two blind Sonnet passes on two crops (f0007a: the run after "hasard."; f0007b: para 2, 9 lines) + worker reconciliation from the
  image -> f0007_09/ciphertext.tsv; gloss words and the codes they sit over -> f0007_09/gloss.tsv, by physical position.
- Disclosure: this worker had already looked up key.tsv values for the codes MANT-EYE listed (304 30 10 54 28 35 15 33 67 26 387 44 39 46)
  before the passes were read. Spans are set by where the gloss ink sits, never by what a decode needs.

Two pre-registered readings:
1. Letter run (the "cette cour" span): f0008_09/gloss_gate.py's statistic and control, run on f0007_09/gloss.tsv (same alignment, same
   1000-draw value-permutation control, seed 8). With ~10 tokens this has little power; reported as a number, not licensed as a gate on its
   own. Gate as MANT-0008: S > p99 and S >= 0.5 x keyed.
2. Per gloss pair (the brief's count): each glossed code is classed agree (key value, letters only, equals the gloss letters it is aligned
   to, or -- for a single code under a name gloss -- equals the gloss word's initial letter or the whole name), disagree (keyed, other value),
   or not-in-key. Counts reported; agreeing codes are C for this leaf. Name codes are compared on the initial letter only when key.tsv gives a
   single letter, and that is reported as "initial agrees", a weaker class than a full-value agreement (a 1-in-~20 chance hit).
No key.tsv change from this job (the brief asks for counts); any disagreement goes to HYPOTHESES.md with both witnesses (rule 4).

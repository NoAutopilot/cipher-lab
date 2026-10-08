# PREREG-DEPTH-MH: rule-4a depth re-check, f.410 lower block (DEPTH-MH, account 1, session_01LMs2EyN5RhSA1321cqQrnZ)

Written 8 Oct 2026 02:4x UTC (date -u), pushed before any statistic. Verifier, separate from every solver and from
DEPTH-REGRADE, R9-MANTV. Brief: .claude/briefs/runs/2026-10-08-acct3-scout-jobs.md "## DEPTH-MH". Nothing decoded.

## Item

SHStA Dresden Loc. 694/08 f.410 lower block (frame 0511), P.S. Manteuffel to Flemming, Nov 1712; N4, held D1 at 66.7%.
Tokens: reading_tokens.tsv rows whose line id starts `694-08_0511_f410_` (L.. and M1-M5; 216 tokens, the audited item; the
8 `f410u` rows are not in the audited count and are excluded). Key: key.tsv. Cipher class: codes 1-120 (Krauske's letter and
syllable table); code class: codes > 120 (nomenclator). Shuffle: VERIFY-MANT's design (b) extended -- values permuted within
the cipher class and within the code class separately (key classes kept). Candidates named by the brief: 217
'la reine d'Angleterre' (C x3), 390 Stettin.

## Depth bar (copied verbatim from .claude/briefs/runs/2026-10-08-acct3-depth-bar.md, which overrides the inline brief text)

- CLAUDE.md 4a governs where it differs from the research note.
- Cipher clause: a contiguous H/C/S stretch longer than the authentication distance (AD) for the design, about 1.5 x unicity.
  - H(K) = the design's key space plus every liberty the reading took: U wildcards, M tokens, r|re|ro and o|ou|ous choices, repairs.
  - An unfitted external or period key does NOT shrink H(K) to the liberties alone.
  - The zero-liberty (H_lib+20)/R reading (about 6-8 letters here) is not used.
- External check: an external check (key agreement with period glosses, a period key sheet) is a D3/D4 element under CLAUDE.md 4a. It does NOT replace the clause at D2, although research section 3 offers it as an alternative.
- Code clause: a code value that reads sensibly in >= 2 independent contexts.
  - An H or C grade on the value does not satisfy this on its own, although research section 3 says 'or carry H/C grade'.
  - A verbatim repeated phrase counts once (lodewijk precedent).
- D2 = one clause plus your own true, specific sentence about the content, written from the reading. Droysen or Fagel 5177 may confirm the sentence, never supply it. Otherwise hold D1.
- If you think the convention is wrong, post one ROOM flag for the parent and still rule under this bar.

## Statistics (script: tools/depth_stats.py, one run per item; outputs in depth_mh/)

Token stream = the item's rows of the committed reading-tokens file, in file order. Each keyed token's letters = its value
folded to a-z (accents folded, everything else dropped), first alternative of an `a|b|c` value. U (and any token not in
the key) is a gap.

1. **Grade runs (key-independent, reported, not controlled).** Longest contiguous run of H/C/S tokens, in letters, M/U/gap
   breaking the run; per line and over the item in file order. Primary: only cipher-class tokens (see item section) count,
   a code-class token breaks the run. Secondary: code-class H/C/S tokens are allowed through and their letters counted.
2. **AD.** R = log2(26) - H_model, H_model = per-letter cross-entropy (bits) of a held-out 10% of tools/data/fr18 (every 10th
   line) under an interpolated character 5-gram trained on the other 90%. H(K) = H_design + H_lib:
   H_design = (distinct cipher-class codes in the item) x log2(V), V = distinct cipher-class values in the key (the key
   space actually exercised; an unfitted key does not reduce it to H_lib); H_lib = sum over M tokens of log2(max(2, number of
   alternatives)) + U tokens x log2(V). unicity = H(K)/R; AD = 1.5 x unicity. Also reported (sensitivity, not decisive):
   AD at R = 3.4 bits (Shannon-style asymptotic redundancy, the most generous figure).
3. **Code recurrences (key-independent).** Code-class values occurring >= 2 times in the item. Two occurrences are the same
   context (a verbatim repeat, counted once) if the 3 codes before and the 3 codes after are identical.
4. **Control statistic (i), key-dependent.** Longest stretch of the decoded letter stream (gaps break it) that segments
   completely into fr18 words: word types of length >= 2 seen >= 5 times in fr18, plus 'a' and 'y'. Target vs 200
   value-shuffled keys.
5. **Control statistic (ii), key-dependent.** For each recurring code value and each independent context: mean 5-gram
   log-probability per scored letter of the window (8 decoded letters before + the value's letters + 8 after; n-grams
   spanning a gap are not scored). Target vs the same window under the same 200 shuffled keys.
6. Shuffles: seeds 8100-8299 (registered here, not used before in this folder). Report target, shuffle p95 and max.
   The control can differ from the target by construction: permuting values changes every decoded letter that (i) and (ii)
   score; grade runs and recurrence counts (1, 3) do not depend on the key and are not given a shuffle control.

## Decision rule (fixed before any statistic)

- Cipher clause met iff the primary longest grade run (1) > AD (2, model R). If it is <= AD the clause fails whatever the
  R=3.4 sensitivity says.
- Code clause met for a value v iff (a) v has >= 2 independent contexts (3); (b) in >= 2 of them the window score (ii) is
  above that window's shuffle p95; (c) the verifier, reading each window, can state what it says with v's meaning, listing
  every liberty (M, U, repair) in the window. (c) is a judgement and is written out in AUDIT.md for each context.
- Item control: (i) target > shuffle p95. If (i) fails, the decoded stream does not beat chance on the key-dependent
  statistic and the item holds D1 whatever (a)-(c) give.
- D2 iff (cipher clause or code clause) and item control and the verifier writes one true, specific sentence about the
  content from the reading alone (no edition supplies it). Otherwise D1. D3/D4 are not in scope (they need >= 80% H/C/S
  and more than this test can give).
- The fr18 judge FAIL near its gate (ZX-DEC349 shape) is "cannot decide" and is not used either way.
- N-class, key, ciphertext and reading are not touched.

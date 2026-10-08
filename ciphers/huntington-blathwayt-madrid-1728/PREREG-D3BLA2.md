# PREREG-D3BLA2 -- known-answer re-gate of the three-reader rule (D3-BLA's I1)

Written by D3-BLA2 (account 4, LANE DEPTH, session_01XGKh2TvfC6jR7LnNrtMPMf), 8 Oct 2026, time read with `date -u` (21:5x UTC),
BEFORE any crop is cut or read and before any score is computed. Brief: .claude/briefs/runs/2026-10-08-acct4-depth-2136-jobs.md
"## D3-BLA2". Why: PREREG-D3BLA's random-code control could not vary on the axis the rule claims (NOTES.md "D3-BLA", last paragraph).

## Universe (fixed by `d3bla2_universe.py`, output `d3bla2_universe.tsv`, committed with this file)
Columns of ciphertext.tsv that carry a gloss, in BLA179, 185, 188, 189, 190, 194 (BLA191/184/186 excluded), where passA.tsv conf is M
or passA and passB give different groups at the (line,pos) key. 185 candidates (more than 40), so a seeded sample of 40:
`random.Random(20261008).sample(range(185), 40)` over the candidates sorted by (line, pos). The `sampled` column of the TSV is the
list; it is read before any crop and not changed.

## Answer (leave-one-out)
For a sampled column with gloss g (normalised as settle.py `norm`): the set of codes that every OTHER ciphertext.tsv column with
conf H and the same normalised gloss carries (this column removed; columns of the sampled list stay in the pool only if conf H).
Answer = those codes (a gloss with several homophone codes has several). Gloss with no other H attestation: dropped, counted, not
scored. A settled/read group is correct iff it equals one of the answer codes.

## Rule (exactly as D3-BLA ran it)
Per column: A = passA group, B = passB group (raw tsv, as committed), Z = a fresh blind Sonnet pass on the crops (no key, no glosses,
no prior reads, one page's crops per subagent call, at most 4 calls). The reconciler (this worker, looking at the crop only, before any
score is printed) records `compete=1` if any digit of the column on the crop reads plausibly as something else (R17: ')' and '>' = 7
in this hand). Settle iff A == B == Z digits and compete = 0; the settled digits are then the rule's reading. Otherwise unsettled.

## Statistics
- Scored N (after dropping unattested glosses; dropped count reported).
- Rule: settled count S, settled-correct, precision = correct / S, settle rate = S / N.
- Single readers over all N scored columns: A alone, B alone, Z alone, precision = equal-to-answer / N (their coverage is 1).
  Also A, B, Z on the settled subset (equal to the rule by construction there, reported for completeness).
- Majority-of-three (any two of A, B, Z agree) precision, reported only.

## Gate (pre-registered)
PASS iff S >= 10 AND rule precision >= 0.90 AND rule precision > max(A, B, Z single-reader precision over all N scored columns).
(The comparison is over all N because on the settled subset the three readers are identical by construction and could never be beaten.)
PASS licenses moving D3-BLA's held 9 tokens (BLA191 p5 L12 pos 2-4, 6-12 minus the unread 5; d3bla_signs.tsv; 46 by the I2 tie rule)
through settle_image.tsv -> settle.py -> build_key.py -> `python3 tools/decode_key.py ciphers/huntington-blathwayt-madrid-1728 --check`.
FAIL: nothing promoted; log "rule not licensed at this precision" and stop.
Caveat declared in advance: these 40 columns are glossed siblings that pass A flagged M; L12 tokens are unglossed, so a PASS
licenses the rule on a related population, not on L12 itself (stated in NOTES, not hidden). If S < 10 the result is "untestable at
this N", not a FAIL of the rule (rule 3, third-attempt clause applies to a further attempt).

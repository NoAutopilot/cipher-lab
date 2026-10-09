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

## Amendment 1 (21:5x UTC by date -u, before any crop was cut or read, nothing scored)
The first d3bla2_universe.py (commit 3b8babd6, pushed 21:44 UTC; the header time "21:5x" above was typed ahead of the clock, the clock read 21:44) keyed passA/passB by raw (line,pos). That is wrong for BLA188_p3 (pass A is one line ahead from L10; see settle.fix_a) and wherever B has gaps against A. The script now uses settle.py's aligned columns (fix_a + Needleman-Wunsch), as ciphertext.tsv does: a candidate is an aligned, glossed column where A's conf is not H or A and B groups differ ('-' counts). 115 candidates, still > 40, same seed 20261008, same sampling call over the sorted list; `d3bla2_universe.tsv` replaced (now with A_group, A_conf, B_group columns, so the single-reader scores come from the same file). Nothing else in this file changes. The first sample is discarded unread.

## Amendment 2 (21:4x-21:5x UTC by date -u, before any blind pass ran, nothing scored)
- Crops: `tools/iiif_lines.py --image images/<page>.jpg --out <scratch>/crops --prefix <page> --debug` was run on all nine pages with sampled
  columns (BLA185_p5, 188_p3/p4/p5, 190_p5, 190_p7, 194_p1/p2, 179_p6): it found 0 or 1 lines on every page (the 1200 px copies have
  a ~72 px row pitch the profile detector cannot separate), so, as D3-BLA did, crops are cut with PIL: six overlapping bands per page,
  x 170-1100, 360 px tall, step 240, 2x upscale, kept out of the repo. The subagent is told to transcribe only numeral rows fully
  inside a band; I merge overlapping bands and align the blind rows to A's lines with settle.align (no y-position is needed).
- The brief caps the blind pass at 4 subagent calls, one page each. Pages are taken by number of sampled columns, ties alphabetical:
  BLA188_p3 (11), BLA188_p5 (9), BLA190_p7 (7), BLA188_p4 (4, tied with BLA194_p1 at 4). So the scored set is the sampled columns on
  those four pages (31 of the 40); the 9 on BLA185_p5, 190_p5, 194_p1, 194_p2, 179_p6 are not read (counted as "not covered").
- Reconciliation = one more unit by me, on the same bands, before any score is printed.

## Amendment 3 -- UNA2-BLA, a different instrument (9 Oct 2026, 09:4x UTC by date -u; before any tile is cut or read, nothing scored)
Worker UNA2-BLA (account 1; brief .claude/briefs/runs/2026-10-09-account4-orch-unassigned-2.md "## UNA2-BLA"). The re-gate above on the
1200 px copies is [retired] (S 2 < 10, untestable at N; a further attempt at that design would hit rule 3's third-attempt clause). This
amendment changes the instrument, not a knob: the Huntington IIIF server (hdl.huntington.org/iiif/2/p15150coll7:61005/info.json, read
9 Oct 2026) gives BLA191 p5 a native 8708 x 11608 px; the listed size 4354 x 5804 (3.6x the 1200 px copy) was fetched as
images/BLA191_p5_w4354.jpg (recorded in images/manifest.json).
- Tiles: `python3 tools/iiif_lines.py --image images/BLA191_p5_w4354.jpg` on the L11-L13 strip (command and output pasted in NOTES.md);
  if it does not separate the three lines, one PIL crop per line, x 1250-4000, eye-set y from the 1200 px positions x 3.628, no upscale.
- Blind read: one Sonnet subagent call on the three line tiles only (no key, no glosses, no prior reads), digits per group in order.
  Then one reconciliation by this worker on the same tiles, recording compete=1 for any L12 column where a digit reads plausibly as another
  (the hand's ')'/'>' = 7 rule holds), before any score is printed.
- Known-answer set (fixed now): the 14 columns of L11 and L13 whose sign is H and whose token is C in reading_tokens.tsv (L11 pos 4, 6, 7,
  9, 10, 11; L13 pos 1-8). Answer = the committed group. (The brief says "5 known-answer columns"; the strip carries 14 at no extra cost,
  so all 14 are used -- more power, same call.) Caveat declared: the committed groups were read at 1200 px and confirmed by context,
  not by an independent witness; a KA miss can be the old reading's error as well as the blind reader's -- either way it fails the gate.
- Gate (pre-registered): PASS iff the blind hi-res read equals the answer on >= 13 of 14 KA columns (>= 0.90). The control can fail: the
  blind reader may misread any KA digit at this resolution.
- On PASS: each held L12 column (pos 2, 3, 4, 6, 7, 8, 9, 10, 11, 12; d3bla_signs.tsv) becomes sign H iff the blind hi-res digits equal
  the committed group (= A = B = D3-BLA's blind Z) and compete = 0; pos 5 (1185) is reported, not promoted unless the same holds. Changes
  go only into settle_image.tsv, then `python3 settle.py && python3 build_key.py && python3 ../../tools/decode_key.py . --check`; values
  follow PREREG-D3BLA I2 (a key tie that is not one word in two spellings stays M; 585's value stays U). L11 pos 1 (46, key tie) is a
  key question, not an image one, and is untouched.
- On FAIL: nothing promoted; logged "hi-res KA FAIL" with the per-column table; the step goes [retired] for this instrument.

## Amendment 4 -- UNA3-BLA, same instrument as amendment 3 on the remaining sign-M columns (9 Oct 2026, 10:5x UTC by date -u; before any tile is cut or read, nothing scored)
Worker UNA3-BLA (account 1; brief .claude/briefs/runs/2026-10-09-account4-orch-unassigned-2.md "## UNA3-BLA"). This is the amendment 3
instrument (Huntington IIIF 4354 px, blind Sonnet read, one reconciliation, known-answer gate) applied to more columns, not a new knob.
- Universe, fixed now. Of the 14 M tokens in reading_tokens.tsv (C 138, S 3, M 14, U 17), 7 are key ties whose sign is already H
  (BLA184 p1 L02/L03/L04; BLA191 p5 L01 pos 8 665, L04 pos 4 1250, L11 pos 1 46, L12 pos 2 1018): an image cannot move them and they are
  out of scope (PREREG-D3BLA I2). The image universe is every column whose sign conf is M in ciphertext_targets.tsv: BLA191 p5 L01 pos 9
  941, L01 pos 11 386, L05 pos 10 1099, L06 pos 1 214, L07 pos 9 937, L11 pos 3 385, L12 pos 5 1185 (7 columns, all M tokens), and
  BLA186 p1 L01 pos 8 778 (sign M, token U: unkeyed, so no grade can move; read for the sign only).
- Pages and fetches: BLA191 p5 is on disk at 4354 px (images/BLA191_p5_w4354.jpg, UNA2-BLA): 0 requests. BLA186 p1 (pointer 61204):
  one info.json + one image at the largest listed size <= 4354 wide; 2 requests to hdl.huntington.org, >= 1.5 s apart, browser UA.
- Tiles: `python3 tools/iiif_lines.py --image <strip> --out <scratch>` first (command and output pasted in NOTES.md); if it does not
  separate the lines, eye-set PIL crops per line, two overlapping halves per line, no upscale, neutral names, kept out of the repo.
  BLA191 p5 lines L01, L05, L06, L07, L11, L12; BLA186 p1 L01.
- Blind read: one Sonnet subagent call per page on that page's tiles only (no key, no glosses, no prior reads), digits per group in order.
  Then one reconciliation by this worker on the same tiles, recording compete=1 for any universe column where a digit reads plausibly as
  another (the hand's ')'/'>' = 7 rule holds; an overwritten figure is compete=1), before any score is printed.
- Known-answer set (fixed now): on the read lines, every column whose sign is H and whose token is C, excluding the L12 columns UNA2-BLA
  itself promoted with this instrument: BLA191 p5 L01 pos 1,3,4,5,6,7,10; L05 pos 1,2,4,5,6,7,8,9,11; L06 pos 2-11; L07 pos 1,2,3,6,7,8,
  10,11; L11 pos 4,6,7,9,10,11; L12 pos 1 (41 columns); BLA186 p1 L01 pos 1,2,4,5,6,10,11 (7 columns). Answer = committed group. Same caveat
  as amendment 3: the answers are 1200 px reads confirmed by context, not an independent witness.
- Gate, per page (pre-registered): PASS iff the blind hi-res read equals the answer on >= 90% of that page's KA columns, rounded up
  (BLA191 p5 >= 37 of 41; BLA186 p1 7 of 7). Alignment: groups aligned per line by position; a read that drops or adds a group on a line is
  aligned by Needleman-Wunsch on groups and every KA column it cannot place counts as a miss. A page that FAILs promotes nothing.
- On PASS of its page: a universe column becomes sign H iff the blind hi-res digits equal the committed group and compete = 0. A blind read
  that gives a different group (e.g. 947 for 941) is reported, never written as a group change (no second witness). Changes go only into
  settle_image.tsv, then `python3 settle.py && python3 build_key.py && python3 ../../tools/decode_key.py . --check`; values follow PREREG-D3BLA
  I2 (a key tie that is not one word in two spellings stays M; unkeyed stays U). key.tsv unchanged.
- On FAIL: nothing promoted; "hi-res KA FAIL" logged with the per-column table.

# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261009-1815, "FAMILY-A2k") -- 9 Oct 2026 18:2x UTC, lane orchestrator session_01HjAHKrpYotLhWiRH8gMHxL

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 18:15 UTC 9 Oct - 04:15 UTC 10 Oct (80% 02:15). Eleventh
incarnation: started from STATUS.md "LANE FAMILY handoff (incarnation DEFAULT-account-2-20261009-1510)" next list items 1, 2, 3, 5, plus the
next_steps --hot-only parallel action for antt-msliv0638 (m0200 eye-check, m0277/m0278 crib). Gate 0a: SESSION-SWEEP-account-2 stale-claimed since
5 Oct (prior incarnations proceeded). Exclusions as the 1510 jobs file (eckert-*, Huntington ledgers, lodewijk/jan-van-nassau, decode-*, bne20211,
costabili, harley-287, fr16144, fr16045-pisany, fr4735-monluc, craven-rupert-1648, sforza-pusterla, baluze167, huntington-blathwayt,
ceppo-nevers-fr3251-1570s, pro3055-clinton-1779, birago-*, hellen-frederick-1752, ra-karlxi, Armstrong/Debosnys, Gallica fetches, any folder with a
ROOM claim < 6 h and no done).
Intake gate 18:2x UTC (tools/intake_gate_check.py, exit 0 each): sachsstaatsarchiv-manteuffel-1712 partial, antt-msliv0638-brochado-1712 partial.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE FAMILY-A2k (account 2)"; hosts this wave: www.archiv.sachsen.de ("sachsen": MANT-0490 first,
MANT-0309 second -- each waits for the previous "sachsen release" line and works from disk meanwhile); archive.org ("IA": take/release, for the
Acta Borussica BO I premise reads). No Gallica. Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before).
Lesson carried (1510 wave 1): inventory size estimates over-read; count tokens on the fetched image before planning vision calls.

## Wave 1 (18:2x UTC 9 Oct)

### MANT-0490 (Opus, cap 7, box 120 min, sachsen take FIRST): sachsstaatsarchiv-manteuffel-1712, Loc. 694/08 frame 0490 heavy glossed leaf
Handoff next 1. inv08g.tsv row 0490 (page no. 392, code runs in nearly every paragraph both pages, words above many groups, "beschaedigt"; the
stride-5 inventory called it CLEAR -- wrong). Exactly the MANT-0474 / MANT-0136B procedure (read both NOTES sections and PREREG-MANT0474 /
PREREG-MANT0136B): premise check first (Acta Borussica BO I by date/names -- the 1510 lane found BO I prints or paraphrases most dispatches; Berner
1901), fetch ONCE at native (manifest entry), COUNT code tokens on the image before planning; if > ~120 tokens, read ONE page only and say so.
Crops (gloss not in crop; `tools/iiif_lines.py --image ... --out ... --debug` pasted), two blind Sonnet code passes + one blind gloss read per
page, reconciliation (one more unit), PREREG-MANT0490.md pushed in its own commit BEFORE scoring, gloss gate (real vs key-shuffle p99). Codes > 401
and the held codes (321, 191, 254, 199, 42, 0494's 231-715) occurring here -> second witnesses reported in NOTES; key.tsv not above M without a
passed gate. Units: 1 GET + ~3-6 vision + 1 reconciliation, ~$6. Report what was found and where it was not found; do not classify novelty.

### MANT-0309 (Opus, cap 5.5, box 110 min, sachsen after MANT-0490's "sachsen release"; premise check from disk/IA meanwhile): 694/08 frame 0309
Handoff next 1. inv08f.tsv row 0309 (stamp 240, 16 Sept 1712, runs in the right-page lines, small words above some groups). Same date as the
0312+0314 Extrait pair (MANT-XTR): check whether 0309 is the covering dispatch of that Extrait (same codes, same names) before reading. Same
procedure and gate as MANT-0490 (PREREG-MANT0309.md before scoring; pool with 0312/0314 only if pre-registered as such). ~$4.5. Report what was
found and where it was not found; do not classify novelty.

### MANT-0290W (Opus, cap 3, box 70 min, disk only): 694/08 0290 word/syllable-code gloss gate
Handoff next 2. MANT-UNG found 0290 glossed (inventory wrong) and it FAILed the letter-statistic gloss gate (codes 281-674 are word/syllable codes).
Read the MANT-UNG section, PREREG-MANT-UNG.md and f0290_08/. Pre-register (PREREG-MANT0290W.md, own commit BEFORE scoring) a gate fit for a
nomenclator: for each gloss-bearing code token, does the gloss word recur with the same code elsewhere on disk (0136, 0312/0314, 0474, 0494, 0089,
CUC leaves) -- real consistency vs a shuffle of the code-gloss pairing (p99), with the per-class breakdown CLAUDE.md rule 3 requires (letters vs
word codes; a class with N < 5 is untestable, say so). Also check the control CAN differ from the target on this statistic (rule 3 orthogonal-
control paragraph). No fetch. Report numbers and grades; no key.tsv change above M.

### V-MANTH (Opus verifier, cap 3, box 70 min, disk only; a session that did not solve these leaves): held name/word codes
Handoff next 3. Codes 321 (= Stockholm, one witness), 191 (Stenbock, second witness), 254 (Ilgen), 199, 42 (rule-4 conflict). For each code list
every witness on disk (leaf, line, pos, gloss/value, direction, date, sender/recipient, source file) across 0136, 0312/0314, 0494, 0474, 0089,
0383, CUC leaves and key.tsv; eye the committed crops (no fetch). Rule 4: conflicting support is a data conflict, M where direction/date do not
match, logged in HYPOTHESES.md with witnesses, never settled by majority; a code that only sits on a leaf whose own control tied/failed is held
(rule 3, per-unit merge paragraph). Write AUDIT.md "## V-MANTH (9 Oct 2026)"; edit key.tsv only to add a held row at M or lower a grade, and say
exactly which row and why. Then `tools/decode_key.py ciphers/sachsstaatsarchiv-manteuffel-1712 --check` after regenerating if anything changed.

### DK-TESTS (Sonnet, cap 1.5, box 50 min, no network): tools/tests/test_decode_key.py 3 pre-existing FAILs
Handoff next 5. Run the test file, list the 3 FAILs (Danzay reading STALE etc.). For each: is the committed reading stale against its key (a target
data change since the test was written), or is the test wrong? Fix the test or regenerate the committed reading ONLY where the target's own
decode command with --check says the committed file is stale because of an already-committed key/exception change (name the commit); never edit
a key or a transcription. Then the whole tools/tests decode_key set passes or each remaining FAIL is explained in one line in the test's docstring
and in ROOM. Do not touch a target folder another lane holds (check ROOM last 600 lines).

### BRO-0200 (Opus, cap 3.5, box 75 min, disk only): antt-msliv0638-brochado-1712 m0200 eye-check + m0277/m0278 paraphrase crib
next_steps --hot-only parallel action. Check 1 first (grep NOTES and body_leaves.tsv for m0200, m0277, m0278). (a) Eye-check m0200 from disk
(images/full_PT-TT-MSLIV-0638_m0200.jpg.jpg, no fetch): cipher run y/n, where, approx tokens; record in body_leaves.tsv. (b) m0277/m0278: read the
NOTES lines that name them as a paraphrase crib for letter 134 (or its neighbours); if on disk, one blind Sonnet read of the clear lines (text
only; crop step mandatory and pasted), recorded as a crib source in a new NOTES section; grade nothing from it. If not on disk, digitarq take/
release, <= 6 requests, >= 3 s, via tools/digitarq_fetch.py, manifest entry. If m0200 carries a cipher run, transcribe it only if <= 60 tokens
(two blind passes + reconciliation + key gate as BRO-178 did); else record and stop. Report what was found and where it was not found; do not
classify novelty. Update Remaining gaps / Escalation, gaps_check.

Sessions wave 1 (18:20 UTC): MANT-0490 session_01JSQGXzU4jxaXKy8aZsseiy (Opus); MANT-0309 session_01BJv3LLv5CgyEAymkFzuH5U (Opus); MANT-0290W
session_01FHP39cf4RxHSXw7VXRQznX (Opus); V-MANTH session_01NSARMiUrmcgnS1tJmuWfq2 (Opus); DK-TESTS session_01LqfLtCUjVKDEVkf7HzG15B (Sonnet);
BRO-0200 session_01WZFYuJpRNbRKrR8HXzLs2C (Opus).

Wave 1 results (18:23-18:36): MANT-0490 right page 148 tokens, gloss gate PASS 61/92 vs p99 22, C61 M87, not in BO I; MANT-0309 = covering dispatch
of the 0312/0314 Extrait pair, gate PASS 35/40 vs p99 12, C35 M13, not in BO I; MANT-0290W keyed-word class PASS, 281-674 untestable (non-test);
V-MANTH 321 held (rule-4 conflict), 191 M, 254 folded to 259, 199 held, 42 C; DK-TESTS stale config snapshots synced, suite green; BRO-0200 already
done 6 Oct (check 1). Workers 17.29 by get_session. ledger_check exit 1 is pre-existing (duplicate ids at LEDGER lines 426-438, not this lane).

## Wave 2 (18:4x UTC 9 Oct)
sachsen order: MANT-0490L first, MANT-0317 second, MANT-0310 third (each waits for the previous "sachsen release"). Note: full-page images are
not committed (folder over 30 MB); a worker that needs a leaf already fetched by another session fetches it once again (1 GET) or reads the
committed crops.

### V-MANT16S (Opus first verifier, cap 6, box 100 min, disk + print/IA searches; a session that did not solve these leaves)
CLAUDE.md "Verifier brief (template)" in full, on sachsstaatsarchiv-manteuffel-1712 Loc. 694/08 0309 (MANT-0309) + 0312/0314 (MANT-XTR): one
dispatch pack, Berlin 16 Sept 1712 (covering letter + Extrait pair), none printed in Acta Borussica BO I by the solvers' search. Rule-7
re-derivation with each leaf's --check; independent search families (a)-(g) incl. BO I and II, Berner 1901, Bonnesen 1918, the Prussian/Saxon
editions, IA/HathiTrust EF/Google Books (country=US + key) phrase searches on the decoded text, JSTOR-QUEUE rows in both families (i) and (ii);
N-class and depth (rule 4a) per item in AUDIT.md "## AUDIT (V-MANT16S)", key source recorded; corrections to any over-claim. If N3+ D2+, append the
SECOND-OPINIONS-QUEUE.tsv row and name it in your done line (the lane adds the AUD2 row for account 3). Do not decode new material.

### V-MANT0490 (Opus first verifier, cap 4, box 80 min; a session that did not solve the leaf): 694/08 0490 right page (MANT-0490)
Same template on the 0490 right page only (mid-Nov 1712, page 392). AUDIT.md "## AUDIT (V-MANT0490)". Same SO-queue rule. MANT-0490L is reading
the left page in parallel: audit only the right page as committed at MANT-0490's commit eb4031655 (note in AUDIT if the left-page work lands first).

### MANT-0490L (Opus, cap 5, box 100 min, sachsen take FIRST): 694/08 0490 left page + gutter run
MANT-0490's named next. As MANT-0490 (read its NOTES section and PREREG-MANT0490), left page and gutter run; PREREG-MANT0490L.md own commit before
scoring; gloss gate vs key-shuffle p99; held codes reported as witnesses; key.tsv not above M without a passed gate. ~$4.

### MANT-0317 (Opus, cap 5.5, box 110 min, sachsen after MANT-0490L's release): 694/08 frame 0317
inv08f.tsv row 0317 (stamp 246, 17 Sept 1712, runs in numbered paragraphs 1-3, small words above groups). Day after the 0309 pack: check whether it
continues it. Same procedure and gate as MANT-0309 (PREREG-MANT0317.md before scoring). ~$4.5.

### MANT-0310 (Sonnet, cap 1.5, box 50 min, sachsen after MANT-0317's release): 694/08 0310/0311 look
MANT-0309's named next. Fetch 0310 and 0311 once each (manifest), classify per the inventory columns, say whether either belongs to the 16 Sept pack
(more code, a second Extrait, a decipherment). No transcription. Append to inv08f.tsv with a dated note.

### MANT-YCEN (Opus, cap 2.5, box 70 min, disk only): y-glyph 4|9 census per hand
V-MANTH's and MANT-0309's named next (254 vs 259, 9 vs 14/19 rest on the y-shaped digit). From committed crops of every 694/08 and 694/09 leaf read
so far: list each y-shaped digit token with leaf/line/pos/hand (clerk vs Manteuffel's own) and the key value it would give as 4 vs as 9; where a
token's value is fixed by gloss or by a known word, record it as a known-answer exemplar. PREREG the rule before applying it (own commit); report a
per-hand rule with its known-answer accuracy vs a shuffled-label control; no transcription edit unless both your eye and the rule agree, and then
regenerate readings with --check. Report what was found and where it was not found; do not classify novelty.

Sessions wave 2 (18:39 UTC): V-MANT16S session_01Xz3fF2N1zMfMY9kBWbP5Pn (Opus); V-MANT0490 session_01WA5jDsGmAzLqKDHNJvcVe1 (Opus); MANT-0490L
session_01Vonz3Lnjze8D87Ry7ayUZu (Opus); MANT-0317 session_01YP499gXR45w7Cf2v1d8ndw (Opus); MANT-0310 session_0112dGUYSmccoBkuoJrANaXr (Sonnet);
MANT-YCEN session_01CRPuhyAzoJNykjMhxo82fk (Opus). Wave 1 sessions archived.

Wave 2 results so far (18:50-18:57): MANT-YCEN y=9 rule PASS 20/21 vs null p99 7, six slots flagged for an eye check; V-MANT16S 0309+0312/0314 N0
(period interlinear gloss), D1, key period; MANT-0490L left page gloss PASS 24/42 vs p99 12, unglossed gutter run 38 letters judge PASS, C24 S36
M30, owed fixes. 10.56 by get_session. Lesson: a glossed leaf is N0 by its own period gloss -- the gloss-gated readings are key tests (known text);
the lane's unread material is the unglossed runs (0490 gutter, 0290 281-674) and unglossed leaves.

## Wave 3 (18:5x UTC 9 Oct)

### FIX-YEYE (Opus, cap 2, box 60 min, disk only; 1 sachsen GET only if a needed crop is not committed, after MANT-0310's release)
(1) MANT-0490L's owed fixes (its NOTES section and candidates_L.tsv): G01 r1.7/r2.4 29 -> 28 where both blind passes and your eye agree; 207 note
held; regenerate the 0490 left-page readings and gates with --check, report old/new numbers. (2) MANT-YCEN's six flagged slots: eye-check each on the
committed crop, record 4 or 9 or illegible beside the census row; a transcription edit only where your eye and the PREREG rule agree, then
regenerate that leaf with --check. You did not solve these leaves; do not raise any key grade. gaps_check, file_shrink_guard before push.

### MANT-0503 (Opus, cap 5.5, box 110 min, sachsen after MANT-0310's "sachsen release"): 694/08 frame 0503
inv08g.tsv row 0503 (page no. 403, left page code lines throughout with small words above many groups; right page German clear text; "re-photograph
of the leaf N9-MANT saw as..."). Check 1 FIRST: read n9mant/ and the N9-MANT NOTES section -- if the leaf is already read under another frame
number, one ROOM line and stop. Otherwise as MANT-0490 (PREREG before scoring, gloss gate vs key-shuffle p99, count tokens first, one page if > 120).
Prefer the UNGLOSSED code groups as the reading target: report glossed and unglossed tokens separately, and give the unglossed span its own
pre-registered gate (judge at its length with power reported, as MANT-0490L's gutter gate). ~$4.5. Report what was found and where it was not
found; do not classify novelty.

Sessions wave 3 (18:57 UTC): FIX-YEYE session_01AWL8VfLbJrUDE8CU3Erybd (Opus); MANT-0503 session_01J3MN194KgtMmcuKtNWCFwt (Opus). MANT-YCEN,
V-MANT16S, MANT-0490L archived. Still running from wave 2: V-MANT0490, MANT-0317, MANT-0310.

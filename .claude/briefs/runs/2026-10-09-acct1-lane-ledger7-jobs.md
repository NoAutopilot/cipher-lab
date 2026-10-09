# LANE LEDGER incarnation 7 worker jobs (account 1, session_01PkXfi2qevAQ4DhSpGJHhVb; written 9 Oct 2026 16:4x UTC)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261009-1640. Continues the **Next** list of the
"LANE LEDGER handoff (session_0112WrReDK9hPUT3z5o7jJGi ...)" (incarnation 6) in STATUS.md. Every ROOM line ends "for LANE LEDGER (account 1)".
seven_day allowed_warning has been on every session today (not a stop under lane-common-blast; say so in your done line if you see it).

Intake gate: `python3 tools/intake_gate_check.py eckert-1864` -> "eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within
6 lines" (exit 0, 16:4x UTC). Re-run it yourself before deep work and paste the line.

Since incarnation 6 closed (15:34): AUD2-LEDGER-22..25 all ran on account 4 (AUDIT.md "## AUDIT 2 (AUD2-LEDGER-22)" .. "-25"); FIX-FM10 (15:0x) carried
KEY-TW + FV-FM9a..d fixes, NOT FV-FM9e s.5 and NOT the AUD2-22..25 corrections.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-09-acct1-lane-ledger6-jobs.md (which points back to
the ledger5/4/3 blocks): CLAUDE.md; .claude/briefs/prior-work-step.md with one pasted line per check; `date -u` before every time you write; ROOM
claim/halfway/done via tools/room.py; push every two units; stop before a unit that would cross 80% of cap or box; rule 10 wording; no AskUserQuestion; no
credentials; file_shrink_guard before the final push; gaps_check after NOTES; hdl.huntington.org / CONTENTdm token (post `take`, re-read ROOM, wait for an
earlier un-released take by another worker; post `release` with the request count; at most 40 requests per take, under 300 per session). FOUR workers in
this wave use hdl: keep takes short and do disk work while waiting. Images to scratch, never committed. Rebase immediately before every write to AUDIT.md,
NOTES.md, ciphertext*.txt, status.json, WORK-QUEUE.tsv; on a conflict keep both facts. Solvers: report what was found and where it was not found; do not
classify novelty. Cost is read by the orchestrator from get_session.

---

## FV-FM10a, FV-FM10b (Opus 5.5, first verifiers, separate from every reader; cap $5 each, box 90 min)
Exactly "## FV-FM9a" of the ledger6 jobs file (= FV-FM8/FV-FM6 method: the all-pointer CONTENTdm clear-copy search FIRST -- readers missed holder clear
copies for E300 E310 E311; duplicate diff; OR I-III, ORN; Grant Papers via IA be-api; Butler III-V; press of the day; G3 with decoded phrases; rare-name OR
grep; eye-check every graded line on crops, tools/iiif_lines.py --image). Reading fixes go in AUDIT s.5 for the next FIX job, not into the reading.
- FV-FM10a: E314, E315, E318 (NOTES "## FM-R7a", "## FM-R7b"; E315 = ORN I/10 Lee to Welles per the reader: check as N1). AUDIT.md "## AUDIT (FV-FM10a)".
- FV-FM10b: E319, E320, E321 (NOTES "## FM-R7b"). AUDIT.md "## AUDIT (FV-FM10b)".
status.json/SO rows for N3+ only, audit_status "one audit"; depth_check; file_shrink_guard. On N3+ D2+ append WORK-QUEUE `AUD2-LEDGER-26` (FV-FM10a) /
`AUD2-LEDGER-27` (FV-FM10b) (account-3, Opus 5.5, cap 2.5 per entry; fetch first, take the next free number if taken) and name it in ROOM for the account-3
VERIFY lane. Unit ~1.4 per entry.

## FV-FM10c (Opus 5.5, first verifier; cap $7, box 100 min): the five Cipher No. 9 entries
Same method, on O9-BD (FM-R7a; = OR I/37 pt 2 Ord to Grant per the reader: check as N1) and O9-CA, O9-CB, O9-CC, O9-CD (NOTES "## NO9-R1"; ciphertext-no9.txt,
reading-no9.md, decode_no9.py). key-no9.md is a SAMPLE table from mssEC 67 (object 1750): re-derive every H token by looking the code word up on the key page
image itself (name the page), not from key-no9.md alone; untabled words stay U/M. Weigh NO9-R1's sense checks (Village/Vienna = Major before Mulford; OR II/6
Mulford, Brengle) as independent print only where the print says the same thing. AUDIT.md "## AUDIT (FV-FM10c)". On N3+ D2+ append `AUD2-LEDGER-28`.

## FIX-FM11 (Sonnet 5.5; cap $3, box 60 min, no network): FV-FM9e s.5 + AUD2-LEDGER-22..25 corrections
Exactly the FIX-FM7 method (ledger5 jobs file, Wave 1; FIX-FM10 is the latest example): entry-level notes through decode.py's existing mechanism; never
delete or hand-edit key rows; never hand-edit reading.md; `python3 ciphers/eckert-1864/decode.py --write` then `--check`, exit 0. Sources: AUDIT.md "## AUDIT
(FV-FM9e)" s.5 (E310-E313: season = Wallace, first Webster a stop not [signed], Georgia = Suffolk C, while horse wilby = White House will be, penfields =
ciphers, headers with clear-copy pointers 10291 10193), "## AUDIT 2 (AUD2-LEDGER-22)", "-23" (E305 "[Report] house" = White House if the audit says so), "-24",
"-25": every reading/header correction named there that is not yet in the reading (class changes are theirs; do not re-set them). Do NOT touch the Tulip /
Whiskey rows (KEY-BLIND is re-judging them). Propagate to status.json rows and second-opinions/PROMPT-chatgpt-e<NNN>.md (rule 10). NOTES "## FIX-FM11 (9 Oct
2026, account 1, for LANE LEDGER)": each change, grade before/after, decode --check output; depth_check; file_shrink_guard. Do not touch key.md.

## KEY-BLIND (Opus 5.5; cap $1.5, box 40 min, no network): the fresh blind re-judge FIX-FM10 left owed
Before reading anything else in ciphers/eckert-1864 except key.md's section headings, run `python3 ciphers/eckert-1864/fortmonroe/key_tw.py --blind` (seed as
its --help says; if it needs another path, find it with ls, not by reading NOTES "## KEY-TW"). Judge each of the 32 windows on its own: does the given value
read in context (yes / no / unclear), writing your verdicts to fortmonroe/key_blind_verdicts.tsv and committing it BEFORE you unblind. Then unblind with the
script's own key (or its --reveal option) and report candidate vs control counts for Tulip = stop and Whiskey = Troops, with a Fisher one-sided p. HYPOTHESES.md
one row per candidate ("KEY-BLIND re-judge"); NOTES "## KEY-BLIND (9 Oct 2026, account 1, for LANE LEDGER)". If either row fails (candidate not clearly
above control), say so and name the key.md row a FIX job should set back to M; do not edit key.md yourself.

## NO9-PAGES (Opus 5.5; cap $3, box 75 min): read the rest of the No. 9 key book
mssEC 67 (Huntington object 1750): key-no9.md sections 3-6 hold pp.[1]-[24]; the rest is unread. Fetch the remaining pages once (CONTENTdm IIIF, hdl token,
<= 40 requests, images/manifest.json entries, images to scratch), and for every untabled word in reading-no9.md and ciphertext-no9.txt (NO9-R1 names
`swindle`; grep for U/M tokens) find its page and row; add those rows to key-no9.md with the page named (grade H = handwritten meaning in mssEC 67). Record the
book's page layout (alphabetic sections, arbitraries, route words) so a later reader can look up any word. Then `decode_no9.py --write` and `--check` exit 0;
NOTES "## NO9-PAGES". Do not re-grade entries beyond what the new key rows change; no audit classes.

---

# Wave 2 (written 9 Oct 2026 17:2x UTC; seven_day allowed_warning on every session, continuing per lane-common-blast; lane ~24 of 60 at writing)
By get_session: FV-FM10a 5.94 (E314 E315 N1, E318 N3 D3; AUD2-LEDGER-26), FV-FM10b 5.36 (E319 E320 N3 D3, E321 N3 D2; AUD2-LEDGER-27), FV-FM10c 5.79 (all five
No. 9 entries N1), FIX-FM11 1.26, KEY-BLIND 1.30 (Tulip = stop 9/10 vs 2/10, Whiskey = Troops 7/7 vs 2/7: both S rows stand; E319 reads Open), NO9-PAGES 2.42
(mssEC 67 ends at p.[24]; 72 rows; No. 9 decode M 0). Wave 1 total 22.07. Opus verifiers ran 1.07-1.19x their $5 caps: size at 1.9 per entry.

## FIX-FM12 (Sonnet 5.5; cap $2.5, box 60 min, no network)
Exactly the FIX-FM11 method above. Sources: AUDIT.md s.5 of "## AUDIT (FV-FM10a)", "(FV-FM10b)" (E319 tulip = Open H as a per-entry note -- KEY-BLIND agrees;
pony plain; E321 = the FM-R4a "second text on 5781" gap, received copy 12319), "(FV-FM10c)" (O9-BD C 7 H 5 with OR I/37 pt 2 p.293, FM-R7a M 2 withdrawn;
O9-CC C 3 OR II/6 p.943; decode_no9.py notes through its own mechanism); NOTES "## KEY-BLIND" (E319 note); NOTES "## NO9-PAGES" (propagate the new No. 9
H counts into AUDIT "LS3-V18a" and NOTES "## NO9-R1" count lines for O9-BA O9-BB O9-CA as a dated correction note, never rewriting the old text). Propagate
to status.json rows and SO prompts (rule 10). decode.py / decode_no2.py / decode_no9.py --check exit 0; depth_check; file_shrink_guard; NOTES "## FIX-FM12".

## MS18-R2 (Sonnet 5.5, reader; cap $5, box 120 min): mssEC 18 (obj 10074), 10 more No. 1 rows of ms18/clean-ms18.tsv
Fort Monroe 1864 clean rows are spent; this is the incarnation-6 next item 4. Rows (lowest print cover first; a mechanical grep at 17:2x found none of these
pointers in ciphertext.txt/NOTES/AUDIT): 10009/1 (1865-05-17), 10010/2, 10058/0 (1865-10-13), 10024/2, 9889/0, 9889/2, 9813/1, 10016/2, 9864/1, 9873/1.
Method exactly "## MS18-R1" of .claude/briefs/runs/2026-10-08-acct1-lane-ledger2-jobs.md PLUS the FM-R6 additions (ledger6 jobs): the all-pointer CONTENTdm
clear-copy search on each row's clear words FIRST (readers missed holder copies three times), OR I/46-49 (1865) and I/39-43 (1864) by date + addressee and a
rare-name full-text grep, Grant Papers via IA be-api. The 1865 rows: paste the HEAD share for No. 1 against key-share-1865.tsv before decoding; a row no book
reads is recorded "no book in hand", not forced. Images: crops only (tools/iiif_lines.py --image), page text on disk in sources/mssEC18/ first; hdl token rules.
IDs from E322 (fetch first; take the next free one if taken). NOTES "## MS18-R2 (9 Oct 2026, account 1, for LANE LEDGER)" with a per-row line "in print /
holder clear copy / not located (sources searched)", Remaining gaps / Escalation, gaps_check, decode --check. Unit ~0.5 per row.

---

# Wave 3 (written 9 Oct 2026 18:1x UTC; seven_day allowed_warning, continuing per lane-common-blast; lane ~30 of 60 at writing)
By get_session: FIX-FM12 1.16, MS18-R2 3.68 (E322-E330 filed; E329 E330 printed OR I/39 pt 3 pp.253, 379; 10058/0 no book in hand; 7 not located; OR I/47
pt 3 on IA answered 503 twice and be-api 502 -- retry once each, then log unreachable). Wave 2 total 4.84.

## FV-MS18b, FV-MS18c (Opus 5.5, first verifiers, separate from the reader; cap $7.5 and $7, box 100 min each)
Exactly "## FV-FM9a" of the ledger6 jobs file (= FV-FM8/FV-FM6 method, the all-pointer CONTENTdm clear-copy search FIRST, mssEC 19 received-ledger diff, eye
check of every graded line on crops) with the 1865 sources: OR I/47 pt 3, I/49 pt 2, ser. III vol. 5, and the Wilson/Gillmore/Rosecrans correspondence in
print for May 1865; Johnson Papers (vol. 8) for May 1865 Washington traffic where reachable. NOTES "## MS18-R2" names the sources the reader searched.
- FV-MS18b: E322, E323, E324, E325. AUDIT.md "## AUDIT (FV-MS18b)". On N3+ D2+ append WORK-QUEUE `AUD2-LEDGER-28`.
- FV-MS18c: E326, E327, E328, and confirm E329, E330 as N1 against OR I/39 pt 3 pp.253, 379 on the page image of the print (IA leaf), not OCR heads (~0.4 each);
  test the reader's print-derived values Kearney = Burbridge, lavender = Washburn at every filed occurrence with `tools/decode_key.py --try` or a short script
  with a control, and propose them for key.md at C only if they read everywhere (do not edit key.md). AUDIT.md "## AUDIT (FV-MS18c)". On N3+ D2+ `AUD2-LEDGER-29`.
status.json/SO rows for N3+ only, audit_status "one audit"; depth_check; file_shrink_guard. Fixes in AUDIT s.5 for a later FIX job. Unit ~1.9 per entry.

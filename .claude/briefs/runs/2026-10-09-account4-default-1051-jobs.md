# LANE DEFAULT-account-4-20261009-1051 -- wave 1 jobs (written 9 Oct 2026, ~11:1x UTC by date -u)

Lane orchestrator: session_01XbUzdRL1vD2sD2Yec1P4FM (account 4, `CIPHERLAB_ACCOUNT=account-4`). Standing brief
`.claude/briefs/default-lane.md`; common rules `.claude/briefs/lane-common-blast.md` and `.claude/briefs/README.md` common tail.
Selection: VERIFY-BACKLOG.tsv had two actionable rows, both excluded (Birago off limits; Manteuffel 0436 under a live account-2
claim). Wave 1 is from `tools/next_steps.py --hot-only`: runnable rows and the `parallel` action of blocked rows, cheapest first,
skipping folders with a ROOM claim < 6 h, folders named in live lane briefs (account-2 FAMILY-A2h, account-1 LEDGER/SIG), and
every job that needs Gallica (403 to cloud sessions on 8-9 Oct; probed once 10:5x UTC, 403).

## Common to every job (read before the first action)

1. `git fetch origin && git checkout -B main origin/main`; `export CIPHERLAB_ACCOUNT=account-4`; `python3 tools/room.py --start`;
   `date -u`. Read CLAUDE.md, the target's NOTES.md (status lines, Remaining gaps, Escalation, While waiting) and the last 30 ROOM lines.
2. ROOM claim with `tools/room.py` (role "<JOB> worker (account 4, <model>)", box end time), "for LANE DEFAULT-account-4-20261009-1051".
   A halfway line at 50% of the box; a `done` line at the end. Cost in ROOM lines is "the orchestrator's get_session reading", never your own.
3. Prior-work step: `.claude/briefs/prior-work-step.md` by reference -- run `tools/prior_work.py <slug> --item <id> --step-type <type> --fetch`
   and paste the output into your NOTES section before the first priced step; obey its exit code.
4. Hosts: one request at a time, >= 1.5 s apart (stricter where CLAUDE.md's host table says so); post "<host> take" / "<host> release"
   ROOM lines and wait for another worker's release on the same host. Gallica: do not call it (403). On 429/403/challenge: stop that host,
   log it, one retry after a pause at most. Report requests per host in the done line.
5. **Images never go into the public repository.** Fetch and crop into your scratchpad (or a git-ignored path); commit TSV/MD/scripts only.
   Images already committed in a folder may be read from disk.
6. Subagents: at most 4 at once; a transcription call gets line crops only (`tools/iiif_lines.py --image <file> --out <scratch dir>`, the
   command pasted in NOTES before the first call), never a full page. Price: about USD 1.5 per Sonnet blind pass, and one more unit for
   your own reconciliation. Stop before starting a unit that would cross 80% of cap or box.
7. Grades per CLAUDE.md rule 4; any accepted nomenclature value goes through `tools/decode_key.py <t> --try` and stays M unless its
   control passed; never a direct key.tsv edit for a guessed value. Rule 3: every gate has its matched control, both numbers reported.
8. A target left `partial`: NOTES.md ends with "## Remaining gaps" and "## Escalation" (Verdict) and `python3 tools/gaps_check.py <t>`
   passes. Do not change the status line beyond rule 5. Run `python3 tools/file_shrink_guard.py <every path you touched>` before your
   final push; push with `tools/room.py --push <paths>` (or stage by explicit path, rebase, push).
9. Report what was found and where it was not found; do not classify novelty. Never the words solved, cracked, novel, first or new for
   anything this project did. Never name the owner. Never print credentials. Never call AskUserQuestion. Stop when the brief is met;
   follow-ups go in NOTES.md as one-line suggestions.
10. Final message: five lines max (what ran, numbers with controls, files/commit, requests per host, what is left).

## Jobs

### J1 MAT-F179 -- matignon-mayenne-1586 (NEAR row), Opus, cap USD 6.5, box 100 min
Intake gate: `matignon-mayenne-1586: partial` passes (lead line cited in NOTES). Two units from NOTES "## While waiting (9 Oct 2026, WAIT-PASS-4)",
neither touches f.110 or its sorter labels (ASKS 146 stays the owner's):
(a) Cipher-3 f.179: fetch Tomokiyo's henryiii_Matignon3.png (one cryptiana.web.fc2.com request; snapshot it to scratch, cite URL+date),
crop `images/f179_gallica_native.jpg` (on disk) with `tools/iiif_lines.py --image`, two blind Sonnet passes of the cipher lines + your
reconciliation (3 units, ~USD 4.5), then decode under whatever key the folder already holds for Cipher-3 (or Tomokiyo's table if that is
what his image is) with a shuffled-key control; grade per token. If the folder holds no key for Cipher-3, stop after the reconciled
transcription and say so. Read NOTES "## Cipher-3, fr.15571 f.179" first: the magenta letters on Bourdeau's 680 px copy look like
Tomokiyo's own working labels, so f.179 may already be read by him -- record that as prior work (prior_work.py `--record ... 'KNOWN: ...'`
if his page prints a reading) and then the decode is a key check, not a reading; key source `published` (Tomokiyo), credited.
(b) Nomenclature: test Tomokiyo's 76/82/84/98 (roi de Navarre, Condé, Turenne, Montauban; henryiii.htm on disk) at every occurrence with
`tools/decode_key.py ciphers/matignon-mayenne-1586 --try 76=...` etc.; accepted values M; log in HYPOTHESES.md. (~USD 1)
Do (b) first if time is short. Never touch NEAR.md's status; update its row's numbers only if (a) or (b) moves one.

### J2 JVN-104 -- jan-van-nassau-1572-75, Sonnet subagents / Opus worker, cap USD 3, box 60 min
From NOTES "## While waiting (9 Oct 2026, WAIT-PASS-5)": (a) a third blind pass on the two glyphs around code 104 (long-s, ch?), the reader
told only that Kurrent ch and long-s occur by numerals: does L2 read 'offentlich sich'? Crops from images on disk (D3-5551's), one Sonnet
call, ~USD 1; state the pre-registered question before the call. (b) align the 4613/4615-circle siblings for any occurrence of 140, 145 or
146 with `tools/interlinear_align.py` (D3-5551's Remaining gaps), ~USD 1. Disk only unless a sibling's text is missing; then the
Huygens host row in CLAUDE.md, <= 20 requests.

### J3 JMAN-CSP -- rah-juan-manuel-1521, Sonnet, cap USD 2.5, box 60 min
NOTES "## While waiting": map the Calendar of State Papers, Spain, vol. II, 1522 Juan Manuel entries to the folder's 28 records, using
British History Online pages pp.384-470 (no key, no image, no owner). Output `ciphers/rah-juan-manuel-1521/csp_map.tsv` (record id, date,
CSP page/entry no., what CSP prints -- summary or deciphered text -- and whether the CSP entry says "in cipher"/"deciphered"), and a NOTES
section. This is a record/known-text step: it tells which records already have printed text and which stay unread. BHO: <= 40 requests,
>= 2 s apart; if BHO challenges, try the archive.org copy of CSP Spain II (`_djvu.txt`) instead.

### J4 SALAZ-KEY -- rah-salazar-soria-sanchez-1524-28, Opus, cap USD 4, box 75 min
NOTES "## While waiting (9 Oct 2026, WAIT-PASS-4)": (a) locate the pages of BRAH t.98 (1931), Soria catalogue, HathiTrust osu.32435013919725,
with `tools/htrc_ef_headwords.py` (cifra, Salazar, Sánchez) -- page numbers only, write them to NOTES; (b) build `key.tsv` (+ decode.json for
`tools/decode_key.py`) for the Alonso Sánchez cipher from Tomokiyo's reconstruction (sources/cryptiana/web/AlonsoSanchez.htm, on disk; keep
Soria's two-cipher caveat from spanish2C.htm), and check it against the CSP-printed items 1/3 as a known-answer crib (items 1, 3, 5 are
text-known, AUDIT.md) with a shuffled-key control, so items 2 and 4 decode on arrival. Key source `published` (Tomokiyo), credited.
If items 1/3 have no ciphertext on disk, build the key and stop at that; say so.

### J5 E62-STALE -- eckert-1862, Sonnet, cap USD 2.5, box 60 min
NOTES "## Remaining gaps (E62-9660, 8 Oct 2026)": (a) rerun `residue_decode.py --check` alone and diff pages.tsv to explain the stale report
(~USD 0.3); fix the cause if it is in a script/input, never by `--write` alone without the explanation; (b) Merlin = Maryland (print) vs
key.md Virginia: read the 5021 page image at that line (~USD 0.5) and log the conflict per rule 4 in HYPOTHESES.md (both witnesses), not
resolved by count; (c) if time remains: select printed residue entries by Myrtle, Mary, Ingress, Camden, Humboldt in the other OR volumes
(~USD 1). hdl.huntington.org: LANE LEDGER (account 1) is using it today -- follow the ROOM "hdl take/release" lines, <= 15 requests,
>= 3.2 s apart; IA `_djvu.txt` for OR volumes. Do not touch eckert-1864 (LANE LEDGER's).

## Wave 2 (written 9 Oct 2026, ~11:3x UTC by date -u, after wave 1 closed: 5 workers, 12.29 by get_session)

Same "Common to every job" as above. Register lines can be stale (JMAN-CSP found its step already done on disk): check the
folder's own files and prior_work.py check 1 before any priced step, and stop with a ROOM flag if the step is already done.

### J6 D1411-R21 -- decode-1411-hhsta-vienna-1600, Opus (Opus subagents for the passes), cap USD 6.5, box 100 min
NOTES line ~114 (GAPS157): pre-register r at residue 21 as an alternative table beside the frozen one (a PREREG file committed before
any read), then cut the unused numerals (p.2 left lower half, p.2 right page) from the images on disk with `tools/iiif_lines.py --image`,
two blind Opus passes + your reconciliation (3 units), and test both tables against the shuffled-target and shifted-rule controls only
(controls-vs-decode, no language-judge gate: the judge is retired for this leaf). The language reading waits on ASKS 120; do not attempt it.

### J7 VIVX-KEYS -- fr16106-vivonne-longlee-1579, Opus, cap USD 2.5, box 60 min
NOTES line ~96: the known-keys rung -- read Mousset 1912 pp.lviii-lix (the printed Longlee/Vivonne table) from the IA djvu text and page
images into a key table on disk, and apply it to f.101v (transcription on disk) as a published-key check with a shuffled-key control.
Key source `published` (Mousset), credited. IA: post "IA take/release", <= 20 requests, >= 1.5 s.

### J8 BNE-DECODE -- bne20211-ferdinand-1478, Sonnet, cap USD 1.5, box 45 min
NOTES line ~244: one DECODE browser login (`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js` with `--guess-fullsize`, the
A2-HDK route) to re-test whether R1172 (/123) and the Decrypted sibling R1180 (/126) serve full-size images or plaintext documents.
One login only; "DECODE take/release" in ROOM; images to scratch, never committed; scrub the account name from any saved page. Record
what each record serves (HTTP, content-type, size) in NOTES. If R1180's plaintext document is served, save its text (not images) and
note it as prior work for the target; no decode.

### J9 E62-CHECK2 -- eckert-1862, Sonnet, cap USD 3, box 75 min
Finish E62-STALE's (a) and (c): rerun `residue_decode.py --check` with the 58 page re-fetches it needs (hdl.huntington.org, follow the
"hdl take/release" ROOM lines -- LANE LEDGER uses the host today -- >= 3.2 s apart, one token block), diff against pages_manifest.tsv /
pages.tsv and name the cause of the stale report; fix only with the cause explained. Then (c): select printed residue entries carrying
Myrtle, Mary, Ingress, Camden, Humboldt in the other OR volumes (IA `_djvu.txt`), ~USD 1. Do not touch eckert-1864.

### J10 CS-1162 -- decode-1162-modena-ambung-1492, Sonnet, cap USD 3, box 60 min
`tools/intake_gate_check.py decode-1162-modena-ambung-1492` FAILs (partial, no standard-edition citation within 6 lines). Run a
check-solved per `.claude/briefs/check-solved.md` (all six source families, the Required web/blog step and the "## Premise check"
section), write the verdict at the top of NOTES.md in the gate's format, and re-run the gate; paste both outputs. Do not do the F19
key-constrained check (that is the next lane's, once the gate passes).

## Wave 3 (written 9 Oct 2026, ~11:4x UTC by date -u; wave 2: 3 of 5 register lines were already done on disk)

Same "Common to every job" and Wave 2 preamble. Each step below was checked by the orchestrator against the folder's own latest
Remaining gaps / Verdict before briefing; still re-check with prior_work.py check 1 and stop with a ROOM flag if it is done.

### J11 SALAZ-HTRC -- rah-salazar-soria-sanchez-1524-28, Sonnet, cap USD 1.2, box 40 min
J4's part (a), not run at 11:04-11:07 (HTRC EF API MongoError); the API answered HTTP 200 at 11:4x. Locate the pages of BRAH t.98
(1931), the Soria catalogue, HathiTrust osu.32435013919725, with `tools/htrc_ef_headwords.py` (cifra, Salazar, Sánchez); page numbers
only, into NOTES under SALAZ-KEY's section. "htrc take/release", <= 10 requests, >= 1.6 s. One retry after a pause if it errors, then stop.

### J12 SFZ-READ2 -- sforza-pusterla-1447-f13, Opus worker with Sonnet subagents, cap USD 4.5, box 90 min
NOTES Verdict (SFZ-NEXT, 8 Oct): a second, blind Sonnet reader on the key slips f.81 and f.42 (level crops on disk; one subagent call
per slip, crops only), reconciled under the f.71/f.67 sign-label convention (2 passes + 1 reconciliation = 3 units), then rerun
`g1p.py` and `lattice_decode.py` (both corpora) and report the before/after numbers beside their controls. Do not touch the owner-sorter
gap (label convention) beyond noting which pairs still split.

### J13 MONLUC-K07 -- fr4735-monluc-lansac-poland-1573, Opus, cap USD 2, box 45 min
NOTES Verdict (MONLUC-2, 7 Oct; then FRESH-0914's K01 sort): count form-A vs form-B '2/Z' (K07) on the c268 lines 1-5 crops on disk
(`images/c268cipher_L0*_s*.jpg`) against the c268 decode (reading_c268.txt / results_c268.json), and say whether the form split tracks a
plaintext value (e.g. one form per letter) with a permutation control on the form labels. Disk only.

### J14 SP106-KEY -- sp105-paget-1693, Sonnet, cap USD 1.5, box 45 min
NOTES Verdict (D2-PRINT4): check SP 106 key templates for Stepney's 1693-94 cipher against the f.123 cipher words (the cataloguer's
readings in NOTES). Use what is reachable: TNA Discovery API descriptions of SP 106 pieces (<= 20 requests, >= 1.5 s), KEY-OFFICES.tsv /
KEY-DESIGN.tsv, and `tools/prior_work.py - --interceptor England --year 1693`. Record each piece checked and whether it names Stepney,
Paget or 1693-94. No images exist (not digitised); a negative is "not found in <pieces>", never a design negative.

### J15 CRAV-8450 -- craven-rupert-1648, Opus, cap USD 3, box 60 min
NOTES Verdict (CRAV-54): one DECODE login (`tools/decode_browser_login.js`, `--guess-fullsize`) for R8450 (Add MS 18982 ff.177-178),
"DECODE take/release" in ROOM (BNE-DECODE used one login 11:2x; one per session), images to scratch only; transcribe any glossed
pairs and run the A1 test exactly as CRAV-54 did on R8454 (same script, same control), then apply to the 40 legible groups only if A1
admits the table.

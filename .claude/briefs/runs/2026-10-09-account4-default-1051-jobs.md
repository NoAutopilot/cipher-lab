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

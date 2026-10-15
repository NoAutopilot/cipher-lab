# LANE DEFAULT-account-4-20261015-1735 -- jobs (account 4, 15 Oct 2026, written 17:4x UTC by date -u)

Lane orchestrator session_019zm77d2uvnsTF5QLW4AgMr; reports to the orchestrator (owner account). Brief .claude/briefs/default-lane.md.
Common tail for every job: .claude/briefs/README.md common tail applies. `export CIPHERLAB_ACCOUNT=account-4`; `python3 tools/room.py --start`;
`date -u` before any time. ROOM claim / host take+release / done lines via tools/room.py, each ending `usage: not readable here`.
PREREG-<ID>.md pushed before any fetch, read or score. Images and crops stay in the scratchpad, never committed. Good-citizen rule and the
CLAUDE.md host table. Stop before a unit that would cross 80% of the cap or box. Never call AskUserQuestion; never print credentials; never name
the owner; never the words solved, cracked, novel, first, new for anything this project did. Report what was found and where it was not found;
do not classify novelty. NOTES.md section `## <ID> (15 Oct 2026, ...)`; a partial target keeps Remaining gaps / Escalation / Verdict current
(`python3 tools/gaps_check.py <target>` passes). Push with `tools/room.py --push <paths>` (or stage by explicit path, rebase, push);
`tools/file_shrink_guard.py` on every touched file before the final push. One done line, then stop.
Intake gate (pasted 17:39 UTC): fr5761-election-1519 open, na-janssens-java-1811 partial, antt-msliv0638-brochado-1712 partial,
harley-287-1587 partial -- all "edition/page or full-text-search citation found within 6 lines" (exit 0).

## ELEC-27 -- fr5761-election-1519 (Opus, cap USD 3, box 60 min)
Named by DEFAULT-A1-1426's handoff (next 1) and ELEC-316's NOTES "Next": (1) settle the l.27 4|flag slot of f.84r image-to-image against
f.116r l.11/l.29/l.32 (openapi.bnf.fr: f142 at 2400 px, 1 request; f.84r c106 at 2000 as ELEC-356 fetched, 1 request); PREREG the decision rule
(which of 4 / flag, what counts as a match) before looking. A conflict with 4 = Palatin M is recorded, not resolved by frequency (rule 4).
(2) only if under 60% of cap: item 37 (between f.74r and f.81v; ELEC-39 Next 2), locate and say whether it carries name signs (~0.5).
Units: floor ~2.5 + 2 looks x ~0.3. No key value moves above M without the ELEC-PAIR rule unchanged. openapi.bnf.fr <= 4 requests, >= 3 s.

## JAV-CORR -- na-janssens-java-1811 (Opus, cap USD 3, box 60 min)
NOTES.md lines ~2266 and ~2297: `scripts/build_key.py` and `scripts/merge_leaf.py` do not read `corrections.tsv`, so a rebuild of key.tsv from
the keysource passes re-creates row 120 and re-opens 420 at M. Add corrections.tsv reading to both (rows whose `file` column names the pass
files they read; same (line,pos) keying as decode_key.py's exceptions), with an offline test (tools/tests/ or the folder's own test, following
what exists), then show: a rebuild from the passes reproduces the committed key.tsv byte-for-byte (or list every diff and why), and
`python3 tools/decode_key.py ciphers/na-janssens-java-1811 --check` is unchanged. No key value changes beyond what corrections.tsv already
records. Disk only, 0 requests. Units: floor ~2.5 + code ~0.5.

## BRO-PP08 -- antt-msliv0638-brochado-1712 (Sonnet, cap USD 1.5, box 40 min)
BRO-KK left one known-keys lead: QUEUE.md PP-08, ANTT PT/TT/MMIP/23, 'cifra que chamamos de Franca' (holders D. Luis da Cunha and Sebastiao Jose
de Carvalho), undated. Read its DigitArq catalogue record (`tools/digitarq_fetch.py`, the item detail and its dates/notes; <= 6 requests,
>= 3 s apart) and quote the record's date fields, extent, and whether images are online (quote the availability, with the record URL). If dated
outside 1700-1720, record it in the Escalation known-keys line as checked and closed for letter 134; if inside or undated, say so and whether
the images can be read from the cloud (do not read the key; a further job decides). No key edit.

## HAR-58 -- harley-287-1587 (Opus, cap USD 10, box 100 min)
Continues HAR-41R (NOTES.md l.900ff): f.41r (DECODE R8480 P1) cipher block lines 5-8 (R5-R8) and the second margin note beside them ("He is in
jelosye y^t your ho. ..."). Same design as HAR-41R exactly: one DECODE browser login (`node tools/decode_browser_login.js 8480 <scratch>
--guess-fullsize --delay 1600 --max-files 6`; check sha1 of P1 = 0f4896606b21...), crops recut from the same rotated region as tx/f41r_runs.tsv
(paste the crop command before the first reader call; never a full-page image to a reader), one Opus reader call per run blind to key, margin
and gloss, shapes named by Bourdeau's stroke descriptions, plus one blind reader control item as HAR-41R's (gate >= 17/19 equivalent stated in
PREREG); one call for the margin note from its crops. Score with the HAR-41R script or an option added to it (same S1/S2 and value-shuffled
null, outcome A/B/C as HAR-41R's PREREG), `--check` OK. Units: 4 runs + 1 margin + 1 control/reconcile = 6 calls x ~1.3 + floor 3 = ~10.8;
stop before a unit that crosses 8. Grades stay M unless the PREREG outcome A is met. de-crypt.org: one login, <= 8 requests, 1.6 s apart.
Credit Bourdeau's needham1587 table (MIT/CC BY 4.0) by name.

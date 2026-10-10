# LANE LEDGER-18 worker jobs (account 1, session_01CsuUMP4ArfnXJ2DQteMYEs; written 10 Oct 2026 17:4x UTC by date -u)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261010-1740 (blast 2 of 2). Second lane beside the
live LANE LEDGER-17 (session_012RUntsXtDcM9uQywtGBBXs), which holds the whole Fort Monroe ledger (mssEC 25, obj 5952, `ciphers/eckert-1864/fortmonroe/`,
IDs E578-E599, E622+). **This lane never touches Fort Monroe rows, fortmonroe/ files or those IDs.** Scope: the small non-Fort-Monroe residue named in the
LEDGER-14 and E62-CAM next lists. Objects 8472, 6254, 9660 stay blocked (no-key-material: the pre-registered 10-entry test ran, LEDGER handoff 8 Oct);
the Fort Monroe "print-likely" rows are known text by n-gram cover (control 12/12, shuffled 0/804) and are not this lane's.

Intake gate (17:46 UTC 10 Oct): `eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`;
`eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`. Re-run and paste.

---

## LR-RES (Sonnet 5.5; cap $2.5, box 90 min; three units, ~0.4 + ~1.0 + ~0.4, stop before starting a unit past 80% of cap or box)
Common: ROOM.md last 30 lines first; claim line with box end; `.claude/briefs/prior-work-step.md` (civil-war adapter) pasted per unit before its first priced
step (tools/prior_work.py if it runs on the folder, else by hand as E62-CAM did). Host tokens in ROOM for hdl.huntington.org and archive.org/be-api exactly as
"Common to every worker" of .claude/briefs/runs/2026-10-10-acct1-lane-ledger16-jobs.md: post `take`, re-read ROOM, wait for any earlier un-released take by ANY
session on that host (LANE LEDGER-17 workers use both), `release` with the count; <= 40 requests per take; one retry after 25 s on a dropped connection, then
stop. Good-citizen rule. Report what was found and where it was not found; do not classify novelty. Never edit key.md (open codes stay M; a value proposal goes
to HYPOTHESES.md with its witnesses, rule 4).
1. **eckert-1862, page 4998 Camden insertion (image check).** NOTES "## E62-CAM" item (1): 18 Feb 1862 arrest order "For William Rabe W S Marshall
   <deletion>Nugget</deletion> <insertion>Camden</insertion> a man named Harold ...". Fetch the page image once (hdl IIIF, manifest entry in
   ciphers/eckert-1862/images/manifest.json), cut the line with `tools/iiif_lines.py --image <file> --out <dir>` (paste the command), read the inserted and
   struck words on the crop, and say whether the key range for 16-21 Feb gives Camden a value that fits the sentence (Thomas cannot: object of "For"). Outcome
   line: confirms / contradicts / cannot tell the volunteer text; Camden stays one occurrence M unless a second witness appears.
2. **eckert-1862, ORN ser. I vols. 21 and 24** (`_djvu.txt` once each, title page checked before use, ids in NOTES): run the existing
   `print/residue_print/orn/longest_run.py` (extend with a volume argument, not a private copy) on all 124 residue entries with the same word-shuffled control
   (seed 1862), and a direct grep for the Myrtle / Mary / Ingress / Humboldt rows' rare words (14 Feb 2 PM Halleck p.4982; 16 and 19 Feb Scott; 14 Feb Humbolt).
   A run >= 7 that is not a formula sentence is a lead (entry | vol/page | printed line); change no grade.
3. **eckert-1864 E403** (NOTES "## E62-STALE": stays N3 D1, not located; next OR ser. II vol. 7 / ser. III vol. 4 by page, Ferry-Donohue commission record): grep
   the OR ser. II vol. 7 and ser. III vol. 4 `_djvu.txt` (cached under ciphers/eckert-1864/print/ if there; else fetch once, title page checked) for the entry's
   names and decoded phrases and the soldier-vote forgery (Ferry, Donohue, Maxon, Stevenson); a hit is a lead for a verifier, no grade change.
Write NOTES.md sections "## LR-RES (10 Oct 2026, account 1, for LANE LEDGER-18)" in ciphers/eckert-1862 (units 1-2) and ciphers/eckert-1864 (unit 3), each with
Remaining gaps / Escalation updated (`tools/gaps_check.py <target>` passes); `tools/file_shrink_guard.py` on every touched file; rebase before every push; ROOM
done line with request counts per host, "for LANE LEDGER-18 (account 1)". No audits, no Fort Monroe.

(17:47 UTC 10 Oct by date -u: LR-RES spawned with source_url, session_012Gf6kPFYtYJxaZLkLjpnvz.)

# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261009-1510, "FAMILY-A2j") -- 9 Oct 2026 15:2x UTC, lane orchestrator session_01EhykP6Ezpqa9BSqzwCGsB8

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 15:10 UTC 9 Oct - 01:10 UTC 10 Oct. Tenth incarnation: started
from STATUS.md "LANE FAMILY handoff (incarnation DEFAULT-account-2-20261009-1310)" next list items 1 and 2 (item 3 needs Gallica; item 4 cheap,
low prior, taken as one Sonnet unit), plus the SIBS-PREMISE "Next sibling round" item 4 (ceppo-nevers fr.4702 f.36r, BnF, crops on disk) whose
intake gate failed on 8 Oct -> its check-solved first. Gate 0a: SESSION-SWEEP-account-2 stale-claimed since 5 Oct (prior incarnations proceeded).
Exclusions: eckert-*, Huntington ledgers, lodewijk-van-nassau-1573-74, jan-van-nassau-1572-75, decode-*, bne20211, costabili, harley-287, fr16144,
fr16045-pisany, fr4735-monluc, craven-rupert-1648, sforza-pusterla, baluze167, huntington-blathwayt, ceppo-nevers-fr3251-1570s, pro3055-clinton-1779,
birago-*, hellen-frederick-1752, ra-karlxi, Armstrong/Debosnys, Gallica fetches, every folder with a ROOM claim < 6 h and no done.
Register rows re-checked by check 1 (15:2x): wallis-emus203 "grep Thurloe vols 2-5" already ran (6 Oct, ticked) -- dropped; august-van-saksen
"53 p2 unread cipher block" already read (R11A-AVS53, 6 Oct) -- dropped (KH1-D: 0 unread siblings).
Intake gate 15:2x UTC (tools/intake_gate_check.py, exit 0 each): antt-msliv0638-brochado-1712 partial, sachsstaatsarchiv-manteuffel-1712 partial,
heinsius-vanhaersolte-1703 open. ceppo-nevers-fr4702-f36: exit 1 on 8 Oct (CEPPO-4702) -> CS-4702 below is the check-solved it needs.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE FAMILY-A2j (account 2)"; hosts this wave: www.archiv.sachsen.de ("sachsen": MANT-0089 first,
MANT-CEN2 works from disk until MANT-0089 posts "sachsen release"); digitarq.arquivos.pt ("digitarq": BRO-178 only, >= 3 s, <= 30 requests);
resources.huygens.knaw.nl ("huygens": HEIN-SR3 only); archive.org ("IA": take/release). No Gallica at all (403 to the cloud on 8-9 Oct).
Halfway line: one ROOM line at half the box or half the cap, whichever first (skip it if done before).

## Wave 1 (15:2x UTC 9 Oct)

### BRO-178 (Opus, cap 3.5, box 75 min, disk first; digitarq take/release only if a leaf is not on disk): antt-msliv0638-brochado-1712
Handoff next 1. (a) m0178's second cipher run (BRO-SWEEP found it, 9 Oct) and (b) the clear prose on m0253-m0254 that the appendix omits (BRO-123
section). Read NOTES.md sections BRO-SWEEP, BRO-123, V-BRO24 and the Remaining gaps first; check 1 (grep NOTES/body_leaves.tsv for m0178 run 2
transcribed). Crop step mandatory and pasted (`tools/iiif_lines.py --image <leaf file> --out <dir> --debug`); two blind Sonnet passes on the cipher
crops of (a) (one call per pass), reconciliation (one more unit), decode under the folder's key.tsv with `tools/decode_key.py --check` (or the
folder's own decode script), matched control (key-shuffle permutation at the run's own N, as BRO-123 did; too-short if the control cannot
separate at this N -- say so). For (b) one blind Sonnet read of the clear lines (text only, a crib/context source; grade nothing from it).
Units: ~4 vision calls + 1 reconciliation, ~$3. Grades per rule 4 with counts. Report what was found and where it was not found; do not classify
novelty. Update Remaining gaps / Escalation, gaps_check.

### V-MANTC (Opus verifier, cap 2.5, box 60 min, disk only; a session that did not solve these leaves): sachsstaatsarchiv-manteuffel-1712 code conflicts
Handoff next 2 first item. Code 19 (read n twice on clear-under-code leaves vs Krauske's non-valeur), code 63 (Krauske null vs a gloss value, the
MANT-0474 rule-4 conflict) and code 54 (u on 0474 vs the 0494 c/et slot). For each code list every witness on disk (leaf, line, pos, value,
direction, date, sender/recipient, source file) from cuc_candidates.tsv, the gloss TSVs of 0474/0494/0398/CUC leaves and key.tsv; look at the
committed crops for each occurrence (no fetch). Rule 4: conflicting H/C support is a data conflict, graded M where direction/date do not match,
logged in HYPOTHESES.md with witnesses; never settled by majority. Also the 0176 r01 eye check '171' vs '17.1' from the committed crop (~$0.3).
Write AUDIT.md "## V-MANTC (9 Oct 2026)" and, if a key.tsv grade must change, say exactly which row and why (edit key.tsv only to lower a grade).

### MANT-0089 (Opus, cap 5, box 100 min, sachsen take/release FIRST): sachsstaatsarchiv-manteuffel-1712, 694/08 0089 heavy glossed leaf
Handoff next 2 second item. inv08d.tsv line 48 (0089, stamp 66, digit runs in most lines of both pages, small words above some). Premise check
first: check 1 (NOTES/inventories: never scored), check 2-4 per prior-work-step.md (is 0089 a printed letter -- Berner 1901, Bonnesen 1918 by date
and names via IA be-api, take/release "IA"). Then as MANT-0474 did: fetch 0089 ONCE at native (manifest entry), crops of the code lines with the
gloss NOT in the crop, two blind Sonnet code passes + one blind gloss read, reconcile, PREREG-MANT0089.md pushed in its own commit BEFORE scoring
(copy PREREG-MANT0474's gloss gate: real vs key-shuffle p99, per page), score; codes > 401 and 0494's held codes 231-715 occurring here as second
witnesses -> report, never key.tsv above M without a passed gate. Units: 1 GET + 3 vision + 1 reconciliation + CPU, ~$4.5. Stop before a second
leaf. Report what was found and where it was not found; do not classify novelty.

### MANT-CEN2 (Sonnet, cap 3.5, box 75 min, sachsen: wait for MANT-0089's "sachsen release"; read inventories meanwhile): 694/08 frames past 0130
Handoff next 2 third item. Read MANT-CENSUS (inv08d.tsv, 0003-0130) and inv08c.tsv first; list the 694/08 frames past 0130 that no inventory row
covers. Fetch the next 50 uncovered frames at the inventory's thumbnail size (the frames.tsv URLs, >= 2 s, manifest), classify each with the
inventory's columns (code-bearing y/n, glossed y/n/partly, density, stamp, one-line description), append to a new mant0608/inv08e.tsv. No
transcription. ~$3.5 per 50 frames; stop at 80% of cap or box.

### HEIN-SR3 (Sonnet, cap 1.5, box 60 min, huygens take/release): heinsius-vanhaersolte-1703, small_runs over Deel 2 pp.252-371
Handoff next 4. Exactly as HEIN-SR2 (read its NOTES section and the command it ran), next 120 pages. Report runs found (page, string) or none.

### CS-4702 (Sonnet, cap 3, box 75 min): ceppo-nevers-fr4702-f36, check-solved with Premise check
`.claude/briefs/check-solved.md` in full (six sources + "## Premise check" a-d), on fr.4702 f.36r (Ceppo to Nevers; Tomokiyo's printed incipit
"io sono avisato via di Milano"). Named unread: Gomberville 1665 (Mémoires de M. le duc de Nevers), the Italian Ceppo editions, web, Cipherbrain/
Cryptiana threads; also the solver repos. No Gallica (403): use IA, Google Books API (country=US + key), HathiTrust EF, OpenAlex/S2. Write the
verdict into NOTES.md, run `tools/intake_gate_check.py ceppo-nevers-fr4702-f36` and paste the output. Do not reconcile or decode.

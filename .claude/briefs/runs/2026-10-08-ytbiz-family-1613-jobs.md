# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261008-1613) -- 8 Oct 2026 16:2x UTC, lane orchestrator session_01XR227ra6tFXMey23e7ENgo

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 16:14 UTC 8 Oct - 02:14 UTC 9 Oct. First incarnation:
no earlier "LANE FAMILY handoff" in STATUS.md; started from LANE DEFAULT-account-2-20261008-0710's handoff and next_steps.py --hot-only.
Gate 0a clear (SESSION-SWEEP-account-2 done 5 Oct per that handoff). Exclusions: eckert-* (Huntington ledgers, other lanes), Gallica
fetches, Birago/Armstrong/Debosnys, every folder with a ROOM claim < 6 h and no done line.
Register rows re-checked by the orchestrator before briefing (prior-work check 1): STALE and dropped -- wvo-11008-certain-1572 (read and
audited 7 Oct), antt-msliv0638 m0200/m0277 (done 8 Oct), wallis-emus203 Thurloe grep (R8-SPLOOK 6 Oct), heinsius-vanhaersolte small_runs
(D2-HEIN 8 Oct), na-suriname inv. 373 (done 6 Oct). `tools/prior_work.py` does not exist yet: every job runs prior-work-step.md by hand.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE FAMILY (account 2)". If --start fails to push
  from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Prior work (`.claude/briefs/prior-work-step.md`): run checks 1-4 by hand and paste one line per check (route, query, result) into your
  NOTES.md section BEFORE the first priced step; check 5 after any decode. A check that did not run is "unchecked". If check 1 shows the
  step already done, write one ROOM line saying so and stop.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host. Prefer files already on disk. No Gallica.
- Rule 3 (matched control first; a control that cannot differ from the target on the statistic is a non-test), rule 4 grading, rule 7
  (`--check` scripts). Pre-register any new gate in a PREREG-<JOB>.md pushed before the score is computed.
- Rebase before writing shared files; keep both facts on conflict. Commit only your own paths. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the owner; never
  print credentials. Never call AskUserQuestion. Solver jobs: report what was found and where it was not found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. Opus session floor ~1.5.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR ...`); line or strip crops only, never a full
  page image to a subagent; one page (or half page) per subagent call; ~1.5 per vision call, reconciliation one more unit.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE FAMILY (account 2)",
  then a five-line final report.

## Wave 1 (16:2x UTC 8 Oct)
Intake gate 16:2x UTC (tools/intake_gate_check.py, each exit 0):
`sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`heinsius-hermitage-1704: open (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`wvo-hessen-1564: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.

### FAM-MANT15 (Opus, cap 9, box 150 min): sachsstaatsarchiv-manteuffel-1712, unglossed 694/09 frames 0015+0016, then 0052
The named next read of MANT-0609 (NOTES.md "MANT-0609" section, rank table): 694/09 0015 + 0016 (f.8 and verso, Jan 1713, ~70 code
tokens, eye-read Krauske coverage 0.98). Units: fetch the two frames once (www.archiv.sachsen.de, frames.tsv URLs, images/manifest.json);
`tools/iiif_lines.py --image` line crops; 2 blind Sonnet passes + 1 reconciliation (3 units ~4.5); `tools/decode_key.py` with key.tsv
(ciphertext rows for these frames in the folder's convention), grade per token; judge (`tools/judge_plaintext.py` with the spec's corpus --
check the spec's language/era first) WITH a shuffled-key control on the same tokens (does the real key beat shuffled keys on the 4-gram
score?). Prior-work check 2 matters here: look at 0014 and 0017 and the frames either side for a clear copy or a gloss; check 4: Krauske
1893 and NASG vols 14-19 (already grepped by A2-SAX) for this Jan 1713 report by date. Then, only if under 50% of cap and box: 694/09 0052
(one 32-group run, same pipeline, ~2.5). Write a dated NOTES section, Remaining gaps / Escalation, PROGRESS/status only as rule 5 allows.

### FAM-HERM (Sonnet, cap 3, box 60 min): heinsius-hermitage-1704, list every deciphered l'Hermitage letter in Heinsius Deel 10-19
The named next step of D2-HERM (NOTES.md tail): read the candidate pages that carry the "aan d'Alonne, die de gespatieerd gezette
gedeelten uit het cijfer heeft opgelost" formula (Deel 11 pp.202, 288, 433, 505; Deel 12 pp.400, 405; Deel 13 pp.299, 354; Deel 14 p.143;
Deel 15 p.13; Deel 16 pp.9, 112, 151, 317, 325, 414, 433; Deel 17 p.647; Deel 19 pp.240, 261, 360, 371, 377), one pages.json per volume +
one OCR page each (about 30 requests, resources.huygens.knaw.nl, >= 2.1 s apart, descriptive UA), and table each: letter no., writer,
place, date, H.A. number, footnote text quoted, which passages are spaced (deciphered). Output `deciphered_letters.tsv` and a dated NOTES
section; then say which H.A. volumes (earliest first) an archive order should add beside 946/1034/2317 so a key comparison with the 1704
letter becomes possible, and update REQUEST.md's list only (no ASKS row). No decoding. Positive control: Deel 10 p.528 (no. 1066) read by
the same route must show the formula.

### FAM-WVOH (Opus, cap 3, box 60 min): wvo-hessen-1564, reference-strip blind eye read of the 33 C tiles
The named next step (NOTES.md "Remaining gaps", D2-WVO/D4-WVO): one blind read of the 33 conflict/unaligned C tiles with a letter-form
reference strip (the k22 looped d in "worden"/"vnd" beside the k19 g in "nungen", plus h, i, s exemplars) and 10 fresh decoys, the same
PREREG gate as D2-WVO (pre-register in PREREG-FAM-WVOH.md before reading; decoys drawn from tiles whose letter is known, never shown
which); fold k11 "taush" (C07 idx 14) and C03 "voans sp" into the same read. Disk only, no host. This is a key-correction step on a
glossed leaf (known-text share): if the decoy gate fails again, log the instrument "[retired]" for this step per rule 3's third-attempt
clause only if it is the third attempt -- count the attempts in NOTES first.

### FAM-POOL (Opus, cap 4, box 75 min): pools and design priors for the next waves (supply c and d of lane-family.md), no reading
Disk only (plus at most 20 catalogue requests per host, one host at a time, if a row needs one count). (1) From KEY-OFFICES.tsv and
KEY-DESIGN.tsv, list every office/key family in this lane's scope (Dutch, German, Iberian, British/Irish, DECODE/Scandinavian, BnF with
images on disk) whose key is in hand AND which has letters on the same host not yet read (grep ciphers/*/NOTES.md, SIBLINGS-2026-10-08.tsv,
sources/wvo, sources/huygens, sources/decode listings, frame inventories). For each: the unread letters (shelfmark/record id), sign count
estimate, images on disk or host route, and the prior-work check 1 result per letter (our own work: grep the id in ciphers/, ROOM.md last
1,500 lines, WORK-QUEUE.tsv). (2) Run `python3 tools/design_prior.py` on the top unread letters that have no key in hand. (3) Rank by
expected value (P(first cheap test moves it) x value / cost; pools of 2,000+ signs and keys in hand first; BnF-on-disk wins ties). Write
`research/FAMILY-POOLS-2026-10-08.md` (table + the top 6 with a one-paragraph next step each, cost band, and whether a check-solved is owed
-- run `tools/intake_gate_check.py` on each existing folder and paste the line). Push; ROOM done line names the top 3.

Spawned 16:21 UTC: FAM-MANT15 session_01KPBKpmZqWfbkT1aviBKAhy (Opus), FAM-HERM session_012WzDikiwfPBMe8fx6Rb8MR (Sonnet), FAM-WVOH
session_01VJrv6UnrkT7hdhqsD4jAxg (Opus), FAM-POOL session_017eSeTNe93RXnLzuWvfzzwx (Opus). Wave 2 is drawn from FAM-POOL's ranked list.

## Wave 2 (16:5x UTC 8 Oct), from research/FAMILY-POOLS-2026-10-08.md and wave 1
Wave 1 ledgered (13.45 by get_session). FAM-MANT15 beat its shuffled-key control on 694/09 0015+0016 -> a separate first verifier.
The 694/08 frame reader (FAMILY-POOLS row 1) waits until FAM-MANTV is off www.archiv.sachsen.de (one worker per host).
Intake gate 16:5x UTC: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
(exit 0); `sachsstaatsarchiv-manteuffel-1712` exit 0 (wave 1). WVO 11106 and DECODE R4333-37 have no folder: check-solved first.

### FAM-MANTV (Opus, cap 5, box 75 min): FIRST VERIFIER, sachsstaatsarchiv-manteuffel-1712 694/09 0015+0016 (and 0052)
CLAUDE.md "Verifier brief (template)", steps 1-5, on the FAM-MANT15 reading (NOTES.md section "FAM-MANT15-...", folder f0015_09/ and
f0052_09/). You did not read it; do not protect it. Items: A = 0015+0016 (Gersdorff relation 3 Jan 1713, enclosed to Manteuffel 13 Jan),
B = 0052. Prior-work checks 1-5 again, in particular check 4 left "unchecked" by the solver: the Gersdorff-side edition and any print of
Saxon/Polish envoy reports of Jan 1713 (Krauske 1893 NASG; Acta Borussica; Sbornik RIO; Flemming/Manteuffel studies; Stanislas/Leszczynski
literature) by date and phrase ("ne desesperoit pas", "Stanislas pour roy", "Colliers"). Re-derive: `decode_key.py` / the folder's
decode.json with `--check`, re-run shuffle_gate_*.py with a fresh seed, and re-read 4 spot tokens against the frames (fetch only frames
0015, 0016, 0052 once from www.archiv.sachsen.de, <= 6 requests, 1.6 s apart). Depth per .claude/briefs/runs/2026-10-08-acct3-depth-bar.md
and rule 4a. Write AUDIT.md "## AUDIT (FAM-MANTV)", the status.json row (audit_status, depth fields) as the verifier template says, and,
at N3+ D2+, the SECOND-OPINIONS-QUEUE.tsv row and one WORK-QUEUE row `AUD2-FAMILY-1` for its second audit on account-3 (cap 5, box 60,
brief = this section's file + "second adversarial audit of AUDIT (FAM-MANTV)"), named in ROOM for the account-3 orchestrator. Do not decode
anything beyond the re-derivation; do not touch other targets.

### FAM-CS11106 (Sonnet, cap 2.5, box 60 min): check-solved + Premise check, WVO 11106 (Willem van den Bergh to Willem van Oranje, 19 Sep 1572)
`.claude/briefs/check-solved.md` in full, including its "## Premise check". Create `ciphers/wvo-11106-bergh-1572/` (NOTES.md with a status
line from rule 5, sources.tsv, images/ with the 3 WVO PDF images fetched once from resources.huygens.knaw.nl/media/wvo/... with a
manifest). Sources to name with pages: WVO record 11106 (Inhoud, Opmerkingen, print codes), Groen van Prinsterer Archives 1re serie III-IV
(Huygens retroboeken full text, by date 19 Sept 1572, "Berghe"/"van den Bergh", Sept 1572 letters to Orange), Japikse Correspondentie, the
Bergh family literature, DECODE listing, the two solver repositories (cached under sources/), Cryptiana. Premise check: look at all 3
images for any gloss, decipherment or clear copy, and at WVO letters from van den Bergh to Orange within +-30 days (are any deciphered or
in the same cipher?). Then run `python3 tools/intake_gate_check.py wvo-11106-bergh-1572` and paste it. No transcription. Huygens host
<= 60 requests, >= 2.1 s apart.

### FAM-CS4333 (Sonnet, cap 2.5, box 60 min): check-solved + Premise check, DECODE R4333-R4337 (Rusdorff to Axel Oxenstierna, 1628, Riksarkivet)
`.claude/briefs/check-solved.md` in full, including "## Premise check". Create `ciphers/decode-4333-rusdorff-oxenstierna-1628/` (NOTES.md,
sources.tsv; record pages from the login-free DECODE listing via `tools/decode_list.py`, de-crypt.org <= 30 requests, 1.5-2 s apart; NO
login in this job). Sources to name with pages: Rusdorff, *Consilia et negotia politica* (1725) and *Mémoires et négociations secrètes*
(ed. Cuhn, 1789) on IA/Google Books (country=US) full text, by date and "Oxenstierna"/"Oxenstiern"; AOSB (Rikskanslern Axel Oxenstiernas
skrifter och brefvexling) ser. II for Rusdorff letters of 1628; the Riksarkivet catalogue note (NAD) if reachable; DECODE's own record
documents list (any transcription/decryption document attached? "Non-decrypted" is not evidence); the two solver repositories; Cryptiana;
the DECODE key records R4104/R4120 metadata (dates, holders) as a key lead. Premise check per the template. Run
`python3 tools/intake_gate_check.py decode-4333-rusdorff-oxenstierna-1628` and paste it. No transcription.

### FAM-SUR373 (Opus, cap 3, box 60 min): na-suriname-map-1781 inv. 373 neighbour sweep (FAMILY-POOLS row 4)
600 px contact-sheet sweep of NA 1.05.03 inv. 373 scans 0697-0701, 0703-0729, 0731-0745, 0747-0757 (~55 scans) with the folder's existing
sweep scripts (passes/inv373_sweep_r13/), service.archief.nl IIIF, one at a time, >= 1.5 s apart, descriptive UA. Prior-work check 1 first
(grep each scan number in the folder and ROOM). Stop rule: list every scan carrying cipher, glossed or not, with a one-line description;
for each glossed find say which held-out class test in the Remaining gaps it could feed; for each unglossed find say whether the period
key (inv. 86) could read it. No reading. Update NOTES.md, Remaining gaps / Escalation, gaps_check.

## Wave 3 (17:2x UTC 8 Oct)
Wave 2 ledgered (11.82). FAM-MANTV: Manteuffel 694/09 0015-16 N2 D1 (its news in print in Colyer to Heinsius, Briefwisseling XIV), so the
694/08 frame reader is deferred (low value per dollar; next incarnation's call). Intake gate 17:19 UTC (each exit 0):
`wvo-11106-bergh-1572: open (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`riksarkivet-r4282-1628: open (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`decode-4333-rusdorff-oxenstierna-1628: blocked (line 1) -- already terminal, nothing to gate` (the login job below is the premise leaf
check its check-solved named, not deep work); `na-suriname-map-1781: partial (line 1) -- ...` (exit 0).

### FAM-11106T (Opus, cap 11, box 150 min): wvo-11106-bergh-1572, transcription of page 2 + design prior + first family test
Read `TRANSCRIPTION.md` first. Page 2 image from images/11106.pdf (extract at native 300 ppi once, add to manifest). Prior-work: checks 1-4
are in the folder's check-solved/Premise sections (FAM-CS11106, 8 Oct): re-run check 1 only and paste. Units (~1.5 each): crop with
`tools/iiif_lines.py --image <p2> --out images/crops ...` (paste the command and the debug overlay check), two halves of ~12 lines; per half
2 blind Sonnet passes (crop paths only, a shared provisional sign list drawn by you from the crops first, no meanings) + `tools/reconcile_passes.py`
+ your reconciliation from the native crops = 6 units ~9. If the passes split on more than a tenth of signs or the inventory is unsettled,
run `tools/lookalike_pass.py` once, then write the residue to a focus.tsv for the owner's sign sorter and stop transcribing (no third pass).
Output ciphertext.txt / ciphertext.tsv (per sign conf), sign inventory with counts. Then `python3 tools/design_prior.py` on it (paste), and
only if a family is above null and under 80% of cap: `tools/family_run.py` for the top family with its matched control (French 16th c.,
tools/data fr16; N and K from the transcription) -- control first, target only if the control passes its gate. Note the editorial year
(1572 vs 1574/76/77): no historical crib is used. Report what was found and where it was not found; do not classify novelty.

### FAM-4333L (Opus, cap 4, box 60 min): decode-4333-rusdorff-oxenstierna-1628 + riksarkivet-r4282-1628, one DECODE login
ONE real-browser login for the whole job (`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js ...`, with `--guess-fullsize`, the
A2-HDK route; CLAUDE.md DECODE row; scrub the account name from anything saved; never print credentials). In that session fetch, 2 s apart:
full-size images of R4333-R4337 (15 pages) and of DECODE key records R4104 and R4120, with images/manifest.json in each folder (R4104/R4120
images go to ciphers/riksarkivet-r4282-1628/keys_decode/). If full-size is refused, take the largest served size and say so. Then, disk only:
(1) Premise leaf check for R4333-37 (check-solved's (c)): any gloss, decipherment, clear copy or key on any of the 15 pages, one Sonnet call
per page at reduced size; (2) R4104/R4120: describe each table (layout, value range, symbol types) and compare it with riksarkivet-r4282's
expectation (NOTES.md ~line 1383: a 3-row 8-block letter table, 2-digit values 12-91) and with R4333's numeric groups (760 761 3230 853 953);
say plainly whether either is a candidate key for either target -- no key test in this job (name it as the next step with its control);
(3) one LOCAL-QUEUE.tsv row for the owner's runner: Google Books page view of Rusdorff, *Mémoires et négociations secrètes* (Cuhn 1789)
vol. II p.668 and a search inside for "Oxenstiern" 1628 (format per tools/local_runner_brief.md; run `tools/key_livecheck.py` first and
quote its Google Books line). Update both NOTES.md files (status stays as rule 5 allows).

### FAM-SUR729 (Opus, cap 3, box 60 min): na-suriname-map-1781, inv. 373 scan 0729 glossed row labels as a PREREG crib
FAM-SUR373's named ~$2 step (NOTES.md tail, Verdict): 0729 (glossed gun Staat, rows Nieuw Amsterdam / Zelandia / Leyden / Purmerent) row
labels as a pre-registered crib for the 2046/2077 map cartouches. Write PREREG-FAM-SUR729.md (what counts as a hit, the control: same crib
placed against shuffled/other cartouches or a permuted key, chosen so it CAN differ from the target on the statistic) and push it before
scoring. Fetch 0729 at native size once (service.archief.nl, <= 5 requests). Grade C only for values the gloss fixes; anything else M.
Update Remaining gaps / Escalation; a reading change after AUDIT.md -> say so and flag for a verifier in ROOM.

## Wave 4 (17:5x UTC 8 Oct), last of this incarnation
Wave 3 ledgered (12.48). Intake gate for wvo-11106-bergh-1572 as wave 3 (exit 0, 17:19 UTC).

### FAM-11106L (Opus, cap 5, box 75 min): wvo-11106-bergh-1572, homophonic family in other languages + a firmer French control
FAM-11106T's French homophonic control passed its gate by 0.016 (mean 0.616, seeds 0.332-0.856), so its target FAIL is a weak negative.
Prior-work check 1 only (paste). Then, with `tools/family_run.py` on the folder's spec (create specs/wvo-11106-bergh-1572.json if missing,
from ciphertext.txt, N 820, K 41): (1) fr16 again with more seeds (`--seeds 6`) so the control's mean and spread are known, same noise level
as FAM-11106T (0.10, which brackets err_2reader 0.10); (2) de16 and (3) la17 (Bergh's chancery could write German or Latin; Dutch has no
16th-c. corpus on file -- nl18 is era-mismatched, say so and skip it rather than run it), each control first, target only if its control
meets the gate. Also try a merged-inventory variant if FAM-11106T's focus.tsv names a clear look-alike merge set (merge only pairs both
passes split on; state the merge before scoring). Write every row to HYPOTHESES.md (family_run does this), a dated NOTES section, Remaining
gaps / Escalation; rule 3's third-attempt clause applies per hypothesis (count attempts). Report what was found and where it was not found.

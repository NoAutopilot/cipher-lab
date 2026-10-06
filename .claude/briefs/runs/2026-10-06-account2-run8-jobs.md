# LANE LANE-RUN8-account-2 jobs (account 2) -- 6 Oct 2026 03:1x UTC, lane orchestrator session_01Aeemo71BBJ5bPUjGtFFtM5

Lane brief: .claude/briefs/default-lane.md (cap 60, box 03:12-13:12 UTC 6 Oct). WORK-QUEUE row 241: RUN8, same tier as RUN7 --
tools/next_steps.py runnable rows (cost band S and M) and the `parallel` action of blocked rows, ranked by closeness to a counted result,
BnF tie-break; first RUN7's own named next steps in this split. Folders i-r (account 1 a-h, account 4 s-z). VERIFY-BACKLOG.tsv has no
row in i-r needing a verifier. Off limits: Birago (incl. nevers-birago-fr3251-1572), Armstrong, Debosnys; riksarkivet-r4282-1628 (account-4
private repo). Every worker: Opus 5.5, one job, then stop. Each solver job first checks that its named step is still undone (NEXT-STEPS.tsv
lags the folders): if a dated NOTES.md section already ran it, take the folder's own Verdict "cheapest next" instead if it fits this job's
cap and box and is not a machine transcription pass the TRANSCRIPTION.md / CLAUDE.md Usage 6 sorter rule hands to the owner; otherwise
stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN8-account-2".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host.
- Rule 3: any gate is pre-registered (a PREREG file committed and pushed before the scored run), with a matched control that can vary on
  the statistic tested; report both numbers. Rule 4 grades with counts. Rule 7: `tools/decode_key.py <folder> --check` (or the folder's
  own decode script --check) exit 0 before push if the reading or key changed. A reading change after AUDIT.md: say so in NOTES.md and
  flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md); keep both facts on conflict. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. Report what was found and where it was not
  found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call, never a full-page image. Price: ~1.5 per Sonnet subagent pass, reconciliation = 1 unit.
- Sorters (lane rule since RUN7): any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles
  opened against the line image before it is handed on; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never
  publish an artifact or edit ASKS.md yourself.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN8-account-2",
  then a five-line final report.

## Wave 1 (spawned 03:2x UTC 6 Oct). Intake gate output (03:1x UTC) pasted per job.

### R8-MATCUT -- matignon-mayenne-1586, deskewed re-cut of the f.110 sorter (cap 3.5, box 50 min; no vision subagent)
Intake gate: `matignon-mayenne-1586: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN7 named step (R7-MATQA, 6 Oct 02:00, commit 5cf05d341; ASKS 146): the f.110 sorter in `sorter/` cut flat 52 px bands across 5 sloping
lines, 6/6 random tiles off label. Fix: a deskewed re-cut with `tools/sorter_recut.py` and `--region` (the sorter's build lacks it). Read
tools/sorter_recut.py --help and tools/sorter_preflight.py --help first (if scipy is missing, `pip install scipy` once). Re-cut from the
D2B-MATF110 line crops / native image on disk, rebuild per sorter/README.md, then (1) `tools/sorter_preflight.py` must PASS (paste its
output), (2) open 5+ random tiles against the line image yourself and list them with their line labels. Only if both pass: one ROOM flag
"matignon f.110 sorter re-cut, preflight PASS, ready for the account-3 orchestrator to publish, path ..." and update NOTES.md Verdict /
ASKS-146 reference text in NOTES only. If either fails after one fix attempt, write why in sorter/README.md and stop. No reading change;
status stays partial; NEAR.md row unchanged.

### R8-POLL -- pollaky-1865-1875 (NEAR row), image-check of ads 1-2 (cap 5.5, box 75 min; 2 blind passes + 1 reconciliation)
Intake gate: `pollaky-1865-1875: blocked (line 3) -- already terminal, nothing to gate` (status line reads blocked; the Verdict and the
`parallel` column name this as the action that depends on nobody).
Verdict cheapest next (GAPS211, 4 Oct): "image-check of ads 1-2 (one blind pass each plus a reconciliation, crops first), ~$4.5". Use the
page images already on disk (images/manifest.json); if an ad's image is not on disk, say so and do only what is. Crop each ad first
(paste the command), one Sonnet blind pass per ad per reader (pass A, pass B) on crops only, then `tools/reconcile_passes.py` and one
reconciliation unit from the image. Compare the reconciled text with ciphertext.txt per sign/group; any disagreement goes into NOTES.md as
a transcription correction candidate graded per rule 4 (ciphertext.txt is never silently repaired: write a corrections file and say which
tests on disk would change). If passes split by more than a tenth, stop after reconciliation and log the signs for the owner's sorter.
Status line and NEAR.md row: say whether the NEAR row's numbers change; never closed-negative (rule 5). Then gap 3 only if cap/box allow
(it will not; leave it named).

### R8-RUBIN3 -- rubin-1953, CR p.67 Block C at 300 dpi (cap 3, box 45 min; 2 blind passes + 1 reconciliation on one block)
Intake gate: `rubin-1953: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Named next (D2B-RUBIN2, 6 Oct 00:20, commit e29f7ec5e): "CR p.67 Block C character by character, from the PDF re-rendered at 300 dpi for
that page only (re-fetch the PDF from cipherfoundation.org, 1 request; render p.67, rotate, crop Block C)". Do exactly that: 1 request,
render p.67 at 300 dpi (pdftoppm or PyMuPDF), rotate, crop Block C into line crops (paste command), one blind Sonnet pass per reader x 2 on
the crops, reconcile against the 136-char Block C on disk; settle vmie/vnie (graded M now) and the 3 K1/K2 slip positions if the image
allows. ciphertext.txt changes only with a logged witness table. Do not keep the PDF in the repo if over 5 MB (manifest + URL instead).

### R8-ROELL4 -- roell-vandedem-1809, inv. 348 scans 3-79 read in full (cap 4.5, box 60 min; scan triage by the worker, no subagent)
Intake gate: `roell-vandedem-1809: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Named next (D2B-ROELL3, 6 Oct 00:42, commit 80b13e33e): "read scans 3-79 in full (~USD 3-4)" of NA inv. 348 (Van Dedem -> Testa handover,
Dec 1808-Feb 1809), looking for (a) any cipher or key item, (b) the 9 Feb 1809 despatch or a minute of the Constantinople legation that
the target's ciphered letter answers or encloses. service.archief.nl IIIF at a size that shows ciphered figures (not thumbnails), >= 1.5 s
apart, <= 90 requests. Record per scan in a TSV: scan, date, sender/recipient, language, cipher yes/no, one-line content. Then the folder's
Verdict line. Search result only; no novelty words.

### R8-RAY2 -- rayburn-2004, second blind transcription pass then test 2 (cap 3.5, box 50 min; 1-2 Sonnet passes + reconciliation)
Intake gate: `rayburn-2004: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (D2B-RAY, 5 Oct): "Wayback retry ~$0.2 (DONE as a fallback by D2B-RAY: live upload byte-identical), then second
blind transcription pass ~$1.5, then test 2 ~$1". Skip Wayback. Crop the grid rows from images/Rayburn-Cryptogram.jpg (paste command),
one blind Sonnet pass on crops, reconcile against the transcription on disk with tools/reconcile_passes.py, log the agreement rate and
disagreements (the 7 white-out margin tokens from copy_condition.tsv flagged). Then the spec's cheap test 2 (specs/ file; read its
`cheap_tests`) with its matched control, both numbers into the spec's cheap_test_done and NOTES.md; family_run.py if the test is a
family it supports.

### R8-KARL2 -- ra-karlxi-fullmakt-1677, Bakes 2018 book on dk.upce.cz (cap 2, box 30 min; lookup only)
Intake gate: `ra-karlxi-fullmakt-1677: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (D2B-KARL, 5 Oct 23:39): "Bakes 2018 book and articles, dk.upce.cz bitstream check and grep, ~$0.3" (the 2014
thesis is login-gated, HTTP 401). Find the 2018 book's handle on dk.upce.cz (DSpace REST/OAI or the handle page), check whether the
bitstream is open, and if it is, grep its text for 1677 / Naas / fullmakt / Karl XI / chiffr / šifr. If gated, one Google Books API query
(&country=US, key) and one OpenAlex query for the book's other open copies. Update Remaining gaps / Verdict; gaps_check PASS.

## Wave 2 (spawned as wave 1 slots free). Intake gate output (03:2x UTC) pasted per job.

### R8-SUR3 -- na-suriname-map-1781, Opus blind look on 2-3-sign context tiles (cap 5, box 50 min; 1 vision call + worker check)
Intake gate: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (R7-SUR, 6 Oct): "re-ask L08:51 / L10:30 g|l and [sigma] L11:17 vs L10:66 with one Opus blind call on 2-3-sign
context tiles (GAPS37-style masking), reusing passes/signcmp_r7sur boxes and controls, ~$4, 1 vision call". NOTE: RUN7's R7-SUR2 also ran
2-3-sign context tiles (controls PASS, no token moved) -- read its NOTES.md section first; if R7-SUR2 already asked these exact questions
on context tiles with an Opus-grade reader, do NOT repeat: write "[retired] instrument: context-tile blind look (R7-SUR, R7-SUR2)" per rule 3's
third-attempt clause for these tokens and stop. Otherwise: pre-register what each answer changes, controls built from same-hand known tokens
that can fail, one Opus subagent call on crop paths only; apply only under GAPS23's rule; --check exit 0; 2077 H/C/M/U counts before/after.

### R8-OBRED -- oldenbarnevelt-brederode-1605, open DECODE record 2118 (cap 2.5, box 40 min)
Intake gate: `oldenbarnevelt-brederode-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Action that depends on nobody (NOTES.md): "open DECODE record 2118 (NA 1.01.02 inv. 6894, States-General key, '1620 -') ourselves --
RecordsView pages are public (N6-HEL81, 4 Oct 2026) and a full-size image has been served after one browser login (A2-HDK, 2 Oct 2026) --
and say whether it maps names to Arabic numerals in the 30-741 range; image to scratch, never committed; ~$1". One login per session
(`tools/decode_browser_login.js`, `--guess-fullsize` as in A2-HDK), scrub the account name from any saved page. Read the key image yourself
(crops if large); record what it maps (names -> numerals?, range, a few example rows by grade) in NOTES.md; if it plausibly fits the
target's numerals, pre-register a fit test before applying any value (do not apply in this job unless cap allows; name it as next step).

### R8-ROUS2 -- naf14913-rousseau-venice-1743, Hatzenberger fit check + f.206r phrase search (cap 2.5, box 40 min; no vision subagent)
Intake gate: `naf14913-rousseau-venice-1743: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next: "fit check of Hatzenberger 2015 p.326's ambassadeur = 404 at its two f.165 occurrences (and Sénat = 219 once on f.249)
in context, plus his source note, ~$1". Disk first (transcriptions of f.165, f.249 on disk): does 404 = ambassadeur read in context, does
219 = Sénat; grade per rule 4 (a published modern value is `published` key source, at most C if context confirms, else M). Then the
`parallel` S step: phrase-search f.206r's own quote ('venitiens en faveur de la Reine de Hongrie...') via Google Books API (&country=US, key)
and archive.org be-api (1.5 s apart). Update gaps / Verdict; gaps_check PASS.

### R8-LOPE2 -- lope-hurtado-1522, sibling check BNE MSS/18697/29 and MSS/20212/27 (cap 2, box 35 min; lookup only)
Intake gate: `lope-hurtado-1522: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (A4-RFLOPE, 6 Oct): "siblings, BNE MSS/18697/29 and MSS/20212/27 catalogue/digital-collections check, ~$1". Read the BNE
catalogue record for each (datos.bne.es / catalogo.bne.es / bdh.bne.es; quote the availability flag and URL), say whether each is
digitised and whether it is cipher, a key, or a decipherment by the same hand/office; if digitised in BDH, record the IIIF/manifest URL and
fetch one page image to scratch to confirm. Update gaps / Verdict; gaps_check PASS.

### R8-MORIL -- rah-morillo-1817, fetch RAH record 2240's leaf (cap 2, box 35 min)
Intake gate: `rah-morillo-1817: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next: "item 1, fetch record 2240's single leaf (Enrile to Morillo, 26 Jun 1817) once to exclude it as the carrier of the
f.33r passage's ciphertext, ~$0.5". Route per CLAUDE.md RAH paragraph: OAI-PMH GetRecord metadataPrefix=didl for the image id, then
`node tools/browser_fetch.js "<imagen_id.do URL>" OUT.jpg --binary` (Anubis intermittent; at most the tool's own 3 retries, then stop
the host). Read the leaf: cipher present? figures matching f.33r's? Record in NOTES.md, update gaps / Verdict, gaps_check PASS.

### R8-ORM -- ormond-arran-1678, read the 1871 Russell and Prendergast Carte report (cap 2, box 35 min; lookup only)
Intake gate: `ormond-arran-1678: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Parallel action (NOTES.md): "While L39 is pending, read the 1871 Russell and Prendergast report (The Carte Manuscripts in the Bodleian
Library, ...)" -- read the NOTES.md sentence in full for what to look for (MS. Carte 50 fols. 439-440 key sheet; Ormond-Arran 1678 cipher).
Find it on archive.org / HathiTrust EF / Google Books API, grep the full text for Carte 50, cipher/cypher, Arran, 1678, quote hits with page.
Update NOTES.md; search result only.

## Wave 3 (spawned as wave 2 slots free). Intake gate output (03:1x-03:3x UTC) pasted per job. Lookup jobs: no vision subagent.

### R8-ROELL5 -- roell-vandedem-1809, NA inv. 92 scans 176-230 for a minute to Van Dedem at Vienna (cap 3.5, box 50 min)
Intake gate: `roell-vandedem-1809: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Named next (R8-ROELL4, 6 Oct 03:23, commit 7d42805af): Van Dedem left Bucharest 31 Jan 1809 for Vienna, so the target letter fits a letter to
him on the road; read NA inv. 92 scans 176-230 for a minute/outgoing letter to Van Dedem (Jan-Mar 1809) and any cipher or key item. Same
method and TSV columns as R8-ROELL4 (na20108/), service.archief.nl >= 1.5 s apart, <= 70 requests. Search result only.

### R8-KARL3 -- ra-karlxi-fullmakt-1677, be-api full-text search of Actes/Dumont volumes (cap 2, box 30 min)
Intake gate: `ra-karlxi-fullmakt-1677: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Named next (R8-KARL2, 6 Oct 03:20, commit f37041348): "Internet Archive full-text search of Actes/Dumont volumes (~$0.5)". Identify the IA
items for Dumont's Corps universel diplomatique (vol. VII) and the Actes et memoires de Nimegue volumes; be-api fts per item for Naas /
1677 / plein-pouvoir / Charles XI terms (1.5 s apart, positive control: a term known to be in the volume). Quote hits; update gaps / Verdict.

### R8-NLA -- nla-heinrich-braunschweig-1519, Arcinsys Niedersachsen re-test (cap 2, box 30 min)
Intake gate: `nla-heinrich-braunschweig-1519: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Action that depends on nobody (NOTES.md): "GAPS129 step (3), the Arcinsys Niedersachsen re-test for NLA BU L 1 Nr. 548/562 (online
availability flag, quoted, before any copy order), ~$0.5". Read each record on arcinsys.niedersachsen.de (browser tool if JS-rendered),
quote the availability/digitisation flag and URL; if digitised, record the viewer/IIIF URL and fetch one image to scratch to confirm.
Update NOTES.md and REQUEST.md only as facts; do not file ASKS rows.

### R8-CELS -- ra-celsing-sillen-1755, archive.org meddelandenfrns05riksgoog check (cap 2, box 30 min)
Intake gate: `ra-celsing-sillen-1755: blocked (line 3) -- already terminal, nothing to gate`.
Action that depends on nobody (NOTES.md): "check archive.org availability of meddelandenfrns05riksgoog and, if its full text is open, grep its
_djvu.txt for Celsing/Sillen to read the accession entry naming the Riksarkivet volume; only if lending-only does the read become a
person's". Do that (metadata API, then _djvu.txt or be-api fts); quote the entry with its page context; update NOTES.md / REQUEST.md
volume number as a fact.

### R8-VELL -- ra-vellingk-1713, htrc_ef_headwords for 'Vellingk' (cap 2.5, box 40 min)
Intake gate: `ra-vellingk-1713: blocked (line 3) -- already terminal, nothing to gate`.
NOTES.md named step: "run tools/htrc_ef_headwords.py for 'Vellingk' against Sveriges traktater / Carlson's Karl XII letters (HTRC EF API
works from the cloud)". Read the tool's --help; find the volumes' htids via the HathiTrust bibliographic API; run it (>= 1.5 s apart);
report the pages carrying Vellingk / chiffre terms per volume, and whether any is full view (IA or Google Books copy) so a page can be read.
Update NOTES.md; search result only.

## Wave 4 (last; spawned as wave 3 slots free). Intake gate output (03:1x-03:5x UTC) pasted per job.

### R8-ROUS3 -- naf14913-rousseau-venice-1743, registered count-vector gate over the slip-backed pairs (cap 2.5, box 40 min; disk only)
Intake gate: `naf14913-rousseau-venice-1743: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (R8-ROUS2, 6 Oct): "a registered count-vector gate over the four slip-backed pairs (f.213/214, f.216v/217, f.249/250,
f.266r/265) for whole-word codes, starting with 605 = republique, 739 = venise, 52 = la, with a shuffle control, before any key.tsv entry,
~$1.5". PREREG pushed first (statistic, shuffle of slip words across pairs or codes across pairs that CAN change the count match, gate, and a
known-answer control from a value already at C if one exists); report per-pair contributions (rule 3 per-unit paragraph). Only on PASS enter
values at the prereg's grade; decode --check; flag a verifier in ROOM if the reading changes after AUDIT.md.

### R8-OBRED2 -- oldenbarnevelt-brederode-1605, screen in-window Palatine/Hessian DECODE keys (cap 3, box 45 min)
Intake gate: `oldenbarnevelt-brederode-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Action that depends on nobody (R8-OBRED, 6 Oct): "screen the in-window Palatine/Hessian DECODE keys (Munich BayHStA 102, Marburg HStAM 20)
from their public RecordsView pages for a numeral nomenclator reaching the 700s; ~2-3". Use tools/decode_list.py (login-free) to list the
candidate records; read RecordsView metadata and thumbnails; at most one browser login if a full-size image is needed (scrub account name;
images to scratch only). Table of records screened (id, holding, date, key type, numeral range, fit yes/no/unknown). No fit test unless a
record plausibly fits; then name it as next step with a cost.

### R8-KONS -- konstanz-talleyrand-sieyes-1798, Pallain's other volumes and Bailleu vol. 2 (cap 2, box 30 min; lookup only)
Intake gate: `konstanz-talleyrand-sieyes-1798: open (line 3) -- edition/page or full-text-search citation found within 6 lines`.
NOTES.md next: "search Pallain's other Talleyrand volumes and Bailleu vol. 2 for the 17 Jul 1798 Sieyes letter (the gap left by the 2 Oct
premise check), IA full text, ~$0.5". Identify the IA items, be-api fts per item with a positive control term, quote any hit with context.
Update NOTES.md; search result only.

### R8-NLA2 -- nla-heinrich-braunschweig-1519, fetch the 8 Arcinsys images with a manifest (cap 2, box 30 min; added 04:0x)
Intake gate: `nla-heinrich-braunschweig-1519: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Named next (R8-NLA, 6 Oct 03:57): "fetch 8 images with manifest ~0.5" -- NLA BU L 1 Nr. 548 and Nr. 562, 4 images each, free Arcinsys
viewer. Fetch each once (>= 1.5 s apart), write images/manifest.json (URL, size, sha1), keep the folder under 30 MB (JPEG at native size;
if over, keep manifest + sample per CLAUDE.md). Then look at each image yourself and record per image: recto/verso, cipher present
(signs/numerals, how many lines), clear text, hand. No transcription pass in this job; name it as the next step with a per-pass cost.

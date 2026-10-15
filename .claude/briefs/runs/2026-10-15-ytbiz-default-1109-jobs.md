# LANE DEFAULT-account-2-20261015-1109 jobs (account 2, lane orchestrator session_0177nygw3K3f1ZmuZumybKEf) -- 15 Oct 2026 11:2x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 11:11-21:11 UTC 15 Oct. Gate 0a: no SESSION-SWEEP-account-2 row.
Backlog: VERIFY-BACKLOG (Birago/ceppo `counted` rows off limits; eckert-1864 audit2 parked on googleapis 503 / L79-L80; sachsstaatsarchiv audit2
low and its y-glyph step retired to a person's eye) -> step b, `next_steps.py --hot-only` runnable rows checked against each folder's latest
Verdict line, plus the named nexts of LANE DEFAULT-A2-0810-15 (STATUS.md handoff).
Excluded: LANE DEFAULT-A4-1035-15 (lodewijk, clair1161, baluze167, fr2980-gramont, matignon, fr4735-monluc, fr5761-election), LANE
DEFAULT-A1-0740-15 just closed (pro3055), VIV-KEYSTONE (fr16104/fr16106), BNF-FOCUS (fr3982, fr3985-3990), Birago family/ceppo/nevers-birago,
Armstrong, Debosnys, cipher-lab-private; colbert26 11/81 [retired]; pisany head L04 tiles [retired].
Intake gate 11:2x UTC (tools/intake_gate_check.py, each PASS): oldenbarnevelt-brederode-1605, harley-287-1587, na-suriname-map-1781,
colbert26-lathuillerie-1644, sachsstaatsarchiv-manteuffel-1712.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-15-ytbiz-default-0810-jobs.md` (read it in full, and the
files it points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A2-1109-15 (account 2)"; export `CIPHERLAB_ACCOUNT=account-2` before any tools/room.py call;
- a worker pays ~1 of start-up before its first unit: stop before a unit that would cross 80% of cap or box;
- still no www.googleapis.com in this lane.

## Wave 1 (11:2x UTC 15 Oct)

### OBRED-CTRY (Opus, cap 3.5, box 75 min, disk only): oldenbarnevelt-brederode-1605 context-scored --try on the 20 word leads
Verdict (line ~2199): "a context-scored --try pass on the word leads with the same control (~$3)". Read OBRED-BAND and OBRED-SEG first (do not
repeat them). PREREG first: for each of the 20 nl16 word leads, test the implied interval-to-letter assignment at every occurrence of the
same codes in no. 92/187 (decode_key.py --try where it applies, else the OBRED-SEG lattice scorer), with (a) the shuffled-band null and (b) the
synthetic-band control from OBRED-SEG at the real error level, which must accept a known right word before any target lead counts. Units:
scoring runs, no vision. Report leads that hold at every occurrence vs those that break, control numbers; grade M, S only where the control
licenses it; no key.tsv edit beyond what the PREREG allows; --check script; gaps_check.

### OBRED-NA (Opus, cap 3, box 60 min, service.archief.nl / nationaalarchief.nl <= 20, ROOM take/release): oldenbarnevelt-brederode-1605 the no. 92 key's fate
Remaining gaps / known-keys line: "NA 1.01.02 inv. 9459 and secrete resoluties inv. 4562 (Oct 1619), ~$2". Read OBRED-MEM and OBRED-OCT2
first. Stride screen inv. 9459 (7 stukken) at low resolution for a key leaf, cipher alphabet or Brederode letter; in inv. 4562 locate the
Oct 1619 resolutions (by the inventory's own scan order; stride, not whole series) and read any entry naming Brederode, a memorie, cyfer or
sleutel (one Opus read per page, crops in scratchpad). Record every scan viewed and where nothing was found. gaps_check.

### HAR-39V (Opus, cap 2.5, box 60 min, de-crypt.org one browser login, ROOM take/release): harley-287-1587 f.39v line G word 3
Verdict: "Cheapest next: the f.39v line G sign check in R8479 (~$1.5)". Remaining gaps line ~187: `U ? ? ? ? O C` = b????ed; Bourdeau's
needham1587/NOTES.md l.75-76 says only one of the four cramped signs is blotted and the three-grid pigpen alphabet is closed. Fetch R8479's
f.39v at full size once (tools/decode_browser_login.js, `--guess-fullsize` as A2-HDK did; if full size is refused, say so and stop), crop line G
word 3, and read the four signs against the closed alphabet with a matched control (the same word-crop procedure on 3 already-read words of the
same line, which must come back right). PREREG first. Credit Bourdeau (MIT/CC BY 4.0). gaps_check.

### SUR-2046A (Opus, cap 3, box 60 min, disk only): na-suriname-map-1781 the 2046 [d-hook] = e wider-vocabulary anchor test
Verdict alternatives: "the 2046 [d-hook] = e wider-vocabulary anchor test, ~$2 (SUR-ALIGN, 13 Oct: the crib_2042 alignment PASSed ...)". Read
SUR-2046, V-SUR2046, SUR-ALIGN and SUR-TRY first (SUR-TRY retired --try for n = 1 questions). PREREG first, with a control that must accept a
known H value of the same frequency class on the same sheet. Report decided / undecided; key edits only where the PREREG licenses them, with
decode_key --check; gaps_check.

### COL26-PRINT (Sonnet, cap 2, box 60 min, archive.org / OpenAlex / Semantic Scholar / CORE, no googleapis): colbert26-lathuillerie-1644 print rung
Escalation `[ ] print: ... Danish/Swedish mediation editions not yet opened (GF-A2-3 premise (d))`. Find and full-text-search (IA djvu grep,
be-api fts) the printed editions of La Thuillerie's 1644-46 Danish-Swedish mediation papers (e.g. Danish Rigsarkivet editions, Swedish
Riksrådets protokoll / Oxenstiernas skrifter, French Négociations editions) for the dates and phrases of the deciphered canvas 20-21 / f.23 /
f.24 letters (folder's own phrases.txt or the readings). tools/print_check.py where it fits. Record each edition opened, query, hit or no hit.
No reading, grade or key change. Tick or keep the print rung; gaps_check.

## Wave 2 (from 11:2x UTC 15 Oct, refills)

### TH-VERB (Sonnet, cap 1.5, box 45 min, archive.org / delpher.nl / HTRC EF / OpenAlex; no googleapis): thurloe-printed the 1725 Verbael, No. 37 pp.252-253
Verdict (line ~4270): "a person reads the public-domain 1725 Verbael at No. 37 pp.252-253 (LOCAL-QUEUE row, for the lane orchestrator to file;
googleapis has 503'd ...)". Before filing that row, look for a second copy the cloud can read: archive.org advancedsearch + be-api fts
(Verbael / Verbaal, Beverning, Nieupoort, van de Perre, 1653-1654, 1725), Delpher (delpher.nl boeken, its own search API/pages), the HathiTrust
bibliographic API + HTRC EF page counts. If a readable copy exists, read No. 37 pp.252-253 and the 27 June / 22 Aug 1653 Beverning letters and
record what they print (dates, addressee, any cipher or "in cyfer" mention). If none, append the LOCAL-QUEUE.tsv row (format as rows L77-L80,
the Google Books ids vZzvg46MRdEC / T2JVAAAAYAAJ, exact pages, what to copy) and say so. No grade or key change; gaps_check.

### VIE-PC (Sonnet, cap 1.5, box 45 min, archive.org / OpenAlex / Semantic Scholar; no googleapis): fr3975-vieuville-1587 print check
"## While waiting" next: "run tools/print_check.py with the letter's readable clear phrases ("eschevins et maire de ville", "St Aignen",
30 Sept 1587) against IA, Google Books and OpenAlex, ~$0.5". Run it with Google Books skipped (say so), plus IA be-api fts on the Nevers
correspondence editions the folder names. Record hits / no hits in NOTES.md; status line unchanged (blocked: intake), no reading.

### OBRED-6020 (Opus, cap 4, box 75 min, service.archief.nl / nationaalarchief.nl <= 30, ROOM take/release; only after OBRED-NA releases the host): oldenbarnevelt-brederode-1605 inv. 6020 stride-3 screen
Remaining gaps: "the later liassen NA 1.01.02 inv. 6020-6024 and the 6019 stride-1 fill after 565 ... next: a stride-3 screen of inv. 6020
(~$4)". Same method as the 6019 screen (OBRED-552/-549 sections): low-res stride 3, flag any cipher, key leaf or Brederode hand; one Opus read
per flagged page. Record every scan viewed and where nothing was found. gaps_check.

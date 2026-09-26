# Status board

One page, always current. The orchestrator session updates it after every worker reports. If you have lost
track, read this first, then QUEUE.md for what comes next.

Last updated: 23 September 2026, 22:24 UTC

> **the owner is away 21 to 28 September 2026. Read `HANDOFF-WEEK.md` first: it says what he must do before
> leaving, what a teammate can carry alone, and what waits. Anything blocked on a human is in `ASKS.md`.**

## Goal, restated by the owner on 23 September 2026, 17:20 UTC

**Maximise the number of unique solves. Nothing else is sacred.** A unique solve is a reading a separate verifier
classes N3 or better (rule 10). Consequences, applied the same evening:

1. **Recovery is the lane that scales.** The cached DECODE catalogue shows 202 Non-decrypted letters with a Decrypted
   or Partially decrypted sibling in the same shelfmark; 27 survive exclusion against both solver repositories and
   our own queue, in seven clusters (QUEUE.md "Neighbour-record recovery candidates", `tools/decode_neighbours.py`).
   Each is read by opening both records, transcribing, applying the sibling's decipherment as the key. Same-day
   turnaround matters because Bourdeau's project works the same catalogue.
2. **All readable languages count.** The English-only reader profile was discarding most candidates (none of the 27
   survivors is English). QUEUE.md's profile, scout.js and the scout brief now score any language the models read
   at language_fit 3. Existing rows are under-scored for other languages until ASSIGNMENTS row 8 re-scores them.
3. **Cryptanalysis only with a control and a route nobody tried.** Ciphertext-only work on material the two
   solver projects already annealed is the lowest-yield lane (Sforza 1446 today: clean negative).
4. **The archive-order lane stays** (Hamilton, Stair, NLS 20769, Monck) because nobody else pays for copies, but it
   is one solve a month at best; it should never block the pipeline above.
5. **Rules 1, 3, 4 and 10 are unchanged.** "Unique" is the verifier's word, so the pipeline ends in AUDIT.md every time.

Pipeline per cluster: check-solved (editions first: Nuntiaturberichte, CODOIN, calendars) -> DECODE login, open
letter and sibling -> two transcription passes -> key from the sibling, read -> verifier -> board. Blocked at the
second step until ASKS rows 1, 10 and 11 are done.

**18:15 UTC, 23 Sept: the lane that is ours.** The non-DECODE catalogue scout returned 493 items with cipher in TNA
Discovery, BL Archives and Manuscripts and Gallica that neither solver project names (QUEUE.md "Candidates not on
DECODE", N1-N19 scored). The top three carry their key in the same file: Mornington's 1798-1800 despatches with two
copies of the key (BL Mss Eur D623), the 1722 intercepts with cipher-key pairs (TNA SP 35/36), and Courten's diary with
Madden's key (BL Add MS 4956). Check-solved is running on those three; the edition risk is real (the Wellesley
despatches were printed 1836-37). Policy under the unique-solves metric: such items are kept, not dropped as editions,
and the verifier decides. Each will need an imaging order, so the person's card fills once they pass stage 2.

**19:00 UTC, 23 Sept: Bowes 1583, the night's one reading, verified N1.** A solver aligned Tomokiyo's transcription of
eleven cipher fragments with Bowes's letter-book copies printed in 1842 and recovered a sign table that reads 93 of 101
tokens (S 82, M 8, I 3) as the printed names. The verifier found the plaintext in print since 1842 and the leaf itself
calendared in CSP Scotland vi (1910) with every name in clear, so the class is N1, possibly N0 once one calendar page
is read. Not a unique solve; a sign table to hand to Tomokiyo. Two lessons went into the templates: run the HTRC
word-count test on a blocked calendar before setting stage 2, and view the leaf before scoring a catalogue hit.

**19:21 UTC, 23 Sept: wake closed.** The non-DECODE lane delivered the night's stage-2 targets: of fifteen scored
rows, seven are verified unsolved with a copy route (Mornington, Courten, the SP 87 Seven Years War campaign, SP 78
France 1642-57, SP 90/2 1704, SP 87/13 1743, SP 87/23 1747), eight dropped or partial. Four requests are drafted
(Mornington, Courten, SP 78; the SP 87 decision) and six rows sit on the owner's card (ASKS 12-16). 474 survivors of
the catalogue scout are still unscored (ASSIGNMENTS row 13). The DECODE login test and the JSTOR pass wait for a
session that sees the credentials. Nothing was solved; Bowes 1583 is N1. Session usage about 90 for the orchestrator
and nineteen workers.

**19:53 UTC, 23 Sept: the copy-free lane.** While the owner was away, a scout of digitised-manuscript catalogues found
eleven BnF manuscripts with cipher content whose images are free on Gallica and which neither solver project names
(QUEUE.md "Digitised candidates, no copy needed", M1-M11). M1 is a register of a French ambassador's ciphered
correspondence of the 1580s-90s with the cipher bound at the head of the volume (Cinq Cents de Colbert 369). Check-solved
is running on M1-M3, editions first. The TNA and BL lanes stay copy-order lanes: 21 more rows scored (N20-N40), none
digitised. Sforza 1446's volume is not on Gallica; its DECODE images go on the next session's login list. Bowes stays
N1. Seven catalogues (Beinecke, Folger, Bodleian, CUDL, TCD, Leiden, KB) answered curl with bot challenges and need
the browser tool.

## Lane table (kept by the orchestrator; the stop rule is in the orchestrator brief)

| Lane | Checked | Found-solved or read by others | Not a cipher / key-only | Stage 2, copy order or login | Stage 2, copy-free | State (23 Sept 2026, 21:20 UTC) |
|---|---|---|---|---|---|---|
| Cryptiana list via the solver repositories (our original queue) | 40 rows | 9 (5 of them years ago) | 0 | most; 4 with requests drafted | 0 | stopped: worked daily by both projects |
| DECODE cached catalogue, neighbour-record pairs | 202 pairs | 193 named by Bourdeau by id or volume; D1 solved | 0 | D8 only | 0 | stopped: needs the full catalogue behind the login |
| GitHub-held ciphertexts (Bourdeau not-read) | 12 | 0 | 0 | 0 | 1 attacked, clean negative | stopped: his tooling already failed there |
| Bourdeau offline-only / stuck items (B rows) | 12 | 7 already ours | 0 | 5 | 0 | new 23 Sept 23:27 UTC; all copy-order, held behind ASKS rows 14-16 |
| TNA Discovery, BL, Gallica keyword sweep (N rows) | 36 scored, 15 swept | 6 | 2 | 7 | 0 | stopped by rule: 13 stage-2 targets wait on the person |
| Digitised BnF manuscripts (M rows) | 11 scored, 7 swept | 3 | 2 | 0 | 3 (M4 unpinned, M6, M7) | open: 11 of 11 swept. M7 found printed (N1); M6 (Dupuy 452) gated N3, reconciliation running; M8 (Gramont 1530) open with a published key, print check running; M9 found-solved (Lasry 2023); M10, M11 no ciphertext |
| Printed ciphertext detector (IA full text) | 274 editions, 24 passages; 1 swept | 1 (P1 Orange 1572: partial decipherment printed 1842) | n/a | 0 | 23 unswept, mostly Thurloe passages overlapping a catalogued item | open, low expectation: the strongest candidate fell to an 1842 journal; the rest need a leaf check against the Thurloe pieces already tracked |

**21:58 UTC, 23 Sept: first verified N3 of the session.** BnF Dupuy 468 f.28 is a Latin cipher letter to Francis I. The catalogue gives it to Ernest and Joachim of Anhalt, 1515/16; it is more probably from Ernest of Brunswick-Lüneburg and Joachim von Moltzan, 1518/19. It carries an interlinear decipherment in a second hand, probably contemporary. That decipherment was transcribed and the key it implies applied to the whole letter: 663 of 687 cipher tokens read (H 630 from the gloss, S 33 from the key, control 99.8%), 18 M, 6 unread. No printed text or printed decipherment of the letter was found in the editions listed in AUDIT.md (N3). Kind: recovery. AUDIT.md is the record; the
class is N3, not N4, until the credential session runs the JSTOR, Google Books and HathiTrust queries it lists.
The printed-ciphertext detector passed its controls (2 of 2, precision 50 of 50) and left 24 candidate passages
with the text already in hand; the strongest, William of Orange to Jean de Nassau in September 1572, is in
check-solved now. Two British Library orders went out tonight (Courten, Mornington); TNA's daily page-check cap
blocked the SP 78 request until the UK morning.

**22:17 UTC, 23 Sept: correction. Dupuy 468 is printed.** The adversarial second audit found the whole letter in French
translation in Deutsche Reichstagsakten, Jüngere Reihe II (1896), p. 122, from BnF fr. 3897 f.146, dated 24 January
1520, senders Ernst of Lüneburg and Joachim von Moltzan. Class N1, found-solved. The first verifier's N3 rested on a
search that skipped that volume after its own re-dating. What remains is a contribution: the Latin cipher original
identified, the catalogue's date and senders corrected. The "first verified N3" paragraph above is superseded. The
Orange 1572 detector candidate also fell (partial decipherment printed 1842). Zero unique solves today; two
over-claims prevented by the gates before anything left the repository.

## LANE AX handoff (session_01VzK62xX92yKfnUD93zprD8), 26 September 2026, from 00:15 UTC (live)

Brief .claude/briefs/runs/2026-09-26-lane-ax-orchestrator.md; COMMON 2026-09-26-lane-ax-COMMON.md.

- **Premise correction, job 1 (00:19 UTC).** The harvest's 15 "not stated / not nominated" WVO letters were all triaged on
  24 Sept (LANE N/N2/R2/R3/V2): 4503, 5194, 5200, 5207, 5213, 5218, 5221, 5222, 5799, 5810, 5811 and 10260 are printed in clear
  in Groen (text known; 5200, 5549 PS N1; 4503, 5811 N0); 8246 and 10260 are found-solved folders; 5549's body (539 numerals,
  the "verendertte" cipher) has no key after fit tests on 5204-5209, 5213, 5550, 5552, 5557, 5575 and a matched-control crib
  run that failed its own control (J7). So key reuse on the pool is spent except two items:
  (a) **5797** (22 Oct 1573): Groen IV CDXLIV prints it but notes "plusieurs passages n'ont pu etre dechiffres" (about seven
  spots); the 1574 table (ours) reads the brothers' autumn-1573 "alte Ciffer" (J5S) and has never been applied to 5797 -> AX-5797.
  (b) **5799** (3 Apr 1573, Groen IV CDIX in clear) and **4612** (6 Mar 1574, N3, no reading) are the two letters the table
  does not read. Orchestrator fit check: values 1-120 grouped in blocks of five give IC 0.062 (4612) / 0.072 (5799) vs a
  random-block null median 0.051, p95 0.057 -> probably the same block design with another letter order. AX-5799 aligns 5799
  to Groen (key ours, 5799's text N1) and tries it on 4612 and the 5549 body with shuffled-key controls; a block-constrained
  Opus cryptanalysis of 4612 via family_run.py only if that fails.
- **Workers (dispatched 00:20 UTC, Sonnet):** AX-5797 session_01RfSNoU45Mqmh5Gk8gQjPGP (box 60); AX-5799 session_01AeQexCRuXtPoVQ3wFxrK6h (box 75); AX-BRO3 session_01UY47E7pTTfCD7tVDcrtYJy (box 75); AX-STEV session_01V91nNBXmbzPKu39Rs3Sojb (box 40).
- **Round 1 results (00:31-00:42 UTC, all four stopped well inside their boxes).** AX-5797: key.tsv reads 5797 (six control
  words beside the gaps, 0/120 shuffled hits), but all six of Groen's missing-subject spots sit on codes 124-217 the table has no
  row for -> AX-NAMES. AX-5799: key_5799 78 codes (5 C) from p1 only; 4612 and the 5549 body fail a run-length gate whose control
  is invariant under shuffling, so this is NOT a negative on 4612 (rule 3); 4612 stays open for a block-constrained Opus run after
  AX-NAMES. AX-BRO3: 80 more thin-code observations, 11 agree / 0 contradict / 69 undecidable, percentile unchanged 5.0; NEAR row
  updated (next: re-segment the 34 drifted appendix entries, not dispatched). AX-STEV: 3689 and 3813 printed in clear in Stevens
  1888 (text known); 3753, 3784 newly named and 3803 re-categorised, items 12 not 8, text-known 2/12; L16 done -> AX-STEV2.
- **Round 2 (dispatched 01:0x UTC):** AX-NAMES (Opus, box 120): name codes >120 from 5810/5811/4503/5549 PS/5550-5557 glosses
  against Groen, held-out control on 5811, then 5797 spots and 4610/4611/4616 U tokens. AX-STEV2 (Sonnet, box 50).
- **Ledger:** AX-5797 10.09 D, AX-5799 4.14 D-, AX-BRO3 3.85 D, AX-STEV 3.21 D (21.29 dollars).
- **For the parent:** nothing on the board yet from this lane.

## LANE ZX handoff (session_01MxueEQJUGF9PWJiYcVyvBM), 25 September 2026, 15:42-22:20 UTC (closed)

The three partial targets LANE YX left. 13 workers (7 Sonnet, 6 Opus), USD 174.19 worker usage, all ledgered and archived;
orchestrator USD 10.21. No live workers, no pending check-in. Rate limit `allowed` throughout.

| target | outcome (25 Sept 2026) | next |
|---|---|---|
| clair349-este-guise-1556 | partial, **candidate reading, rule-7 re-derivation PASS** (ZX-RD349: 0 of 1020 tokens differ; pipeline byte-identical). Key fr.20974 read in full rotated (ZX-KEY349, Opus): key_alpha 52 H, key_nomen 44 H, atlas S01-S80. The leaf carries a contemporary interlinear decipherment (gloss), agreeing with the decode on 81.5 pct of glossed tokens. Transcription gate passed only with Opus passes on half-line crops under 2500 px (70.7 pct; three Sonnet pairs gave 39.3-42.0). Grades H 29, C 260, M 611, I 98, U 22. fr16 judge FAIL (-1.085 vs real_p05 -0.882), but 0.68 above every shuffled control, and the period gloss itself scores -1.545. Key source `period`. | **for LANE V6/V7: reading ready** (verifier; ROOM line 22:20). Its search must cover Ribier 1666, Guise Memoires-journaux, Este correspondence, Tomokiyo guise.htm, BnF Clair 349 catalogue. The 347 exceptions.tsv tokens (gloss-derived or settled) are not checked by the re-derivation; the verifier should sample them against the image. About ten M tokens flagged for re-read (ZX-TR349E: S44 where P is needed, S13 where t, 25/9 87, 26/6-7, 29/13-14, 32/17). |
| thurloe-barriere-1654 | closed-negative on cryptanalysis alone. ZX-BAR's bare-digit permutation test was corrected (unmatched design, an X); ZX-BAR2 typed the marks: they resolve 8 of 13 conflicting codes vs a shuffle of the same marks 8.27 (range 3-12, p=0.71); a true code+mark design would give 13/13. | a key: the solver repositories' 1655 cipher for this correspondence, DECODE Add MS 4200 records 8395/8398 (images account-blocked). |
| antt-msliv0638-brochado-1712 | partial, no reading. Five dragging entries hand-checked (no image-provable error); normalization built; gate still passes (85.3 vs 94.4). Letter 134 candidate fails the whole-bucket judge control: 5th percentile of 20 same-procedure LOO decodes under pt17 and pt18, below all 200 real-text windows; likeliest cause 19 of 70 tokens on codes seen 1-3 times. | more attestation for the thin codes (other body letters under the same key); not a cheap test. |

- **Lessons** (LEDGER rows): model tier and crop width, not more passes, moved the Clair 349 leaf (three Sonnet pairs USD 50, one Opus pass pair USD 51 that passed); rotate a key image before calling a table crowded; a permutation test on a statistic its input table already fixes is not a test; score a whole length bucket, not one control, before reading a judge FAIL; a whole-bucket control turned "judge cannot decide" into a placed verdict for USD 3.
- **Retrospective trigger met** (13 rows, USD 174, one worker X and an orchestrator X), flagged to the parent at 17:35.
- Tools touched by workers: iiif_lines.py --top-margin, reconcile_passes.py gloss column (tests pass).

## LANE V7 handoff (session_018VkFfDWY4drC9a9aozmop9), 25 September 2026, live (updated 26 Sept 00:59 UTC)

Brief `.claude/briefs/runs/2026-09-25-lane-v7-orchestrator.md`. Opened 22:21 by parent 7d. Orchestrator usage 4.25 at 00:58, context 274k of the 400k handoff line (get_session). Rate allowed.
- Job 1 done: V7-CL349 (Opus, 3.27, D, ledgered, archived): **clair349-este-guise-1556 N0, key period, text known** -- the letter is in clear in Guise Mémoires-journaux (Michaud-Poujoulat 1e sér. t.6 pp.238-239) and the leaf carries an interlinear decipherment over all 33 cipher lines. Verifier recommends status found-solved; posted to both parents 22:58; status.json closed found-solved by parent worker FOLLOWUP-2315 (23:26). Check-solved template gained a "whole volume, not one page range" paragraph from this miss.
- Job 2: done by the parent's EN-FOLDS (22:22): en spread 0.44-0.75, caveat in judge_plaintext.py and CLAUDE.md rule 3. Nothing for V7.
- Job 3: V7-QA4 done (Sonnet 1.84, D, archived; QA/2026-09-25-2341.md: 34 items, 2 failures, both cleared by their owners by 00:17). tools/room.py now refuses unknown leading options (the "--append" role bug). Next QA5 at 01:40, window from 23:41, brief `.claude/briefs/runs/2026-09-26-lane-v7-qa5.md` pushed.
- Jobs 4-5: no other "reading ready" line; Mercy gate-2 closer waits on the owner (~03:00 UTC 26 Sept).
Live workers: none. Next check-in 01:40 (spawn QA5).

## LANE V6 handoff (session_01V2BHwhVh1k72qSYuBFCyGd), 25 September 2026, written 21:42 UTC (context 431k; V7 starts here)

Brief: `.claude/briefs/runs/2026-09-25-lane-v6-orchestrator.md` with `2026-09-25-lanes-7b-COMMON.md`. Orchestrator usage 7.59 at 21:41 (get_session); workers 31.79 over 9 ledger rows plus V6-QA3 (live at handoff). Every worker below is ledgered and archived except QA3.

Results (all AUDIT.md classes copied to status.json by the parents):
- **Linhares (antt-linhares-chave): judge PASS** on the new `tools/data/pt18` corpus (Correio Braziliense + Investigador Portuguez 1808-1819, 3.23M letters, test in tools/tests): -1.051 vs real_p05 -1.122, null_p99 -1.452 (FAIL under pt17 Vieira). qa_flag cleared by the owner-account parent 16:35. Status word stays blocked (intake gate, separate).
- **bl-charles-digby: N0, key published** (Wheatstone 1862); plaintext already in clear in Groen van Prinsterer 1859 2e ser. IV pp.101-104; date corrected to May 1644.
- **antt-fcc-costacabral-1865: N0, key period**; clerk's plaintext over every code; status solved.
- **rah-xiquena-1868: N0, found-solved**, no ciphertext on the leaves (clear file copy of a cipher telegram); retire, not a catch.
- **espagnol142-mercy-1648 (BnF Espagnol 144 f.22): N3, key ours, after two audits** (V6-MERCY 19:19, V6-MERCY2 20:39). Outreach gate 2 NOT met: JSTOR-QUEUE rows 80-83 (owner answers or waives), a page read of Lonchay-Cuvelier IV (HathiTrust mdp.39015014126620, seqs ~56-130; owner machine), APW 505 x3. Post-audit: R7 shuffled-stream control supports the reading (target -1154.3 vs shuffle mean -1488.5, matched control -1336.2); R7-MREV moved Cleues -> Eleues, so Cleves is no longer read -- logged in AUDIT.md and the still-queued SO-MERCY-F22 prompt (c0cc233e); flagged the status.json board line to parent 7d.
- **Second-opinion PRs 10-12**: citation-checked (24 confirmed, 2 not confirmed, 1 unreachable, no class moves); two errors in our own files corrected in NOTES.md (Linhares key trim from either end; Nassau 5551 Pfalzgraf Christoph).
- **Rolling QA**: QA/2026-09-25-1740.md (3 failures, all fixed by owners), QA/2026-09-25-1940.md (0 failures), QA/2026-09-25-2140.md (V6-QA3, 2.78, 25 items, 1 systemic failure escalated to the parent: the 2-file `en` judge corpus has no per-fold spread for rule 3's fold-count amendment; ledgered and archived 22:05).

For V7 (open items): (1) done (QA3 ledgered); (2) next rolling QA ~23:40 with `.claude/briefs/runs/2026-09-25-lane-v6-qa.md` (window from 21:40); (3) verifiers for any "for LANE V6/V7: reading ready" line (templates: `2026-09-25-lane-v6-mercy.md`, `-costa.md`; Opus, cap 10, 60 min); (4) when the owner answers rows 80-83 and the Lonchay-Cuvelier IV page read lands, a short gate-2 closer for Mercy; (5) clair349-este-guise-1556 (ZX, re-derivation ZX-RD349 running at 21:42; ZX posts reading ready on PASS): its leaf carries an interlinear contemporary decipherment -- when ZX posts reading ready, start the verifier from the clair1067 precedent (N0 on the leaf). Retrospective trigger (12 rows or 60) not yet met on V6 rows alone.
Lessons: verifiers ran 5-16 minutes on 30-60 minute boxes and 2-7 dollars on 4-10 caps -- boxes can be halved for single-item verifiers; a reading change after an audit must be pushed into AUDIT.md and any queued SO prompt the same hour.

## LANE R8 handoff (session_01RUhLrpkEtWxVLVVDoYdsvm), 25 September 2026, 22:21-23:54 UTC (closed)

Recovery and deep work, successor to LANE R7; opened by parent 7d; closed with its brief's queue spent. Brief
.claude/briefs/runs/2026-09-25-lane-r8-orchestrator.md; worker common 2026-09-25-lane-r8-common.md; job briefs 2026-09-25-lane-r8-*.md.
4 workers closed (Sonnet 2, Fable 2), USD 25.97 read by get_session, all ledgered and archived, none over cap; orchestrator USD 4.40
(ledgered). Rate allowed throughout. **No live workers, no pending check-in.**

| target | outcome (25 Sept 2026) | next |
|---|---|---|
| fr2933-salviati-1525 | spec written (specs/fr2933-salviati-1525.json); tools/families/syllabary.py with --param marks/boundary/bases. R8-DSN: partial syllabary, regular and irregular; R8-DSN2: mixed marks (vowel / n-m / doubling) with and without run-edge word boundaries, and the syllabary on the 8 real bases. Every control 72-96% at the measured 5% error; every target 0.3-0.5/symbol below its control, judge FAIL, no Italian. Control-backed negatives for all five; NEAR partial | marked types as nomenclator words needs a word-level scorer (tool job, Fable, about USD 10); or lower the transcription error first |
| fr3034-landriano-1528 | **found-solved** (R8-L3034): items 68 and 69 read by George Lasry 2023 (Tomokiyo francis.htm, GL.htm; dbourdeau/cyphersolver); gate exit 0 | none (aymeloglu repo not grepped: verifier gap only) |
| fr5761-election-1519 | gate 1 -> 0 (Mignet 1886, Le Glay 1845); sign_inventory.tsv: 8 correspondent blocks, 317 signs, per-correspondent alphabets + small nomenclator; no companion ciphertext located | park until a 1519-20 embassy cipher letter surfaces; Mignet page cited from be-api (not a page locator) -- a verifier confirms |
| berthier-napoleon-1812, espagnol142-mercy-1648 | parked per brief (no new lead / owner asks ASKS 59, 60, JSTOR 80-83) | none |

## LANE R7 handoff (session_01UpWfpbLwYL1xmDG1vFyi6h), 25 September 2026, closed 22:07 UTC

Recovery and deep work, successor to LANE R6; opened 20:00 by parent 7c (then 7d); closed with its brief's queue spent. Brief
.claude/briefs/runs/2026-09-25-lane-r7-orchestrator.md; worker common 2026-09-25-lane-r7-common.md; job briefs 2026-09-25-lane-r7-*.md.
9 workers closed (Sonnet 8, Fable 1), USD 34.55 read by get_session, all ledgered and archived; orchestrator USD 6.16 (ledgered). Rate
allowed throughout. **No live workers, no pending check-in.** Two workers over cap: AT55V 1.23x, MEYE 1.86x.
clair1161, clairambault296 and the sp87/TNA copy-order items were already ZX2's (ZX2-GAL, ZX2-ASK, ASKS 54/56/57) and were left to it.

| target | outcome (25 Sept 2026) | next |
|---|---|---|
| espagnol142-mercy-1648 | shuffled-stream control passes (target -1154.3 vs shuffle mean -1488.5 vs matched control -1336.2); blind eye-check split the five name glyphs 2x14 / 3x19; R7-MREV applied the blind majority (S 496 M 26 of 522, Cleues -> Eleues, judge FAIL -1.031); V6-MERCY2 kept N3 key ours, outreach gate 2 open; Brussels 15 Apr sibling not printed, AGR reading-room only | owner: ASKS 59 (Cuvelier-Lefèvre VI p.647), ASKS 60 (AGR SEE t.LXIV f.16 copy), JSTOR rows 80-83, Lonchay-Cuvelier IV page read; SO-MERCY-F22 queued. Nothing cheap left for a worker. |
| fr2933-salviati-1525 | atlas re-pass: pooled types 223 -> 204/198 vs gate 178 (codemark_curve.py --merge added); no same-design sibling among 11 Salviati letters 1524-30; CM3: letter-per-type code+mark excluded at the measured 5% error (control 62/82/86% vs target unread) | NEAR row: a design change (syllabic/word values for marked types, or a plain-box letter-count model), Fable, own control, about USD 10 |
| berthier-napoleon-1812 | spec written; test 0 letter XXIX 12th and 17th of 34 on the two metrics it was not selected by; Corresp. Napoléon XXIV no. 19408 is not the "note chiffrée" | not moved; test 3 (Urban's RGVIA find) is a print lead only |

Scout leads for the parent (not R7 targets): BnF Français 3034 item 68 ("Lettre, en chiffre", Landriano 30 Aug 1528, anonymous) and Français 5761
item 3 ("Chiffres desquelz l'on a usé durant le voiage d'Allemagne", a key), both digitised (R7-SSIB, ciphers/fr2933-salviati-1525/siblings.tsv).

## LANE R6 handoff (session_018MWpKL71WnBxA8k4ejVkBS), 25 September 2026, 19:25 UTC

Recovery and deep work; opened 15:39 by parent 7b, closed at 505k context (brief's 500k handoff). 31 workers closed (Sonnet 28,
Opus 1, Fable 2), USD 140.41 of worker usage read from get_session, all ledgered, in hub-seed/ASSIGNMENTS.md and archived;
orchestrator USD 11.78. Rate allowed throughout. **One worker live at close: CM2 (Fable, cap 15, session_01AtRe8LEF72DEuye52Rg7Pi,
brief 2026-09-25-lane-r6-cm2-salviati-tolerant.md; USD 7.75 at 19:24) -- for the parent to read, ledger, archive and route.**
Common: .claude/briefs/runs/2026-09-25-lane-r6-common.md; job briefs 2026-09-25-lane-r6-*.md.

| target | outcome (25 Sept 2026) | next |
|---|---|---|
| espagnol142-mercy-1648 | pinned f.22r-v (canvases 58-59); transcribed 521 codes (38 values) + 174 plain words, 95.3%; es17 corpus built; homophonic anneal -1154.3 on 4 seeds vs matched control best -1321.7; Fable reading S 494 M 27, --check 0, fresh re-derivation byte-identical; judge cannot decide (es17 and es17c FAIL the letter's own clear words too; es17c false-negatives 23.5%); **V6-MERCY N3, key ours** (AUDIT.md); no sibling under the code in Espagnol 142 | NEAR.md row: shuffled-stream control and blind eye-check (V6's list), SO-MERCY-F22, Brussels SEE t.LXIV sibling (Lonchay p.445), DECODE R958-R965 |
| fr2933-salviati-1525 | intake gate fixed (Desjardins Toscane I-III etc. read); all eight leaves transcribed, 2,820 signs (f55v and f57v by a pass C majority); cm at the real N: control 94% clean, target unreadable, **not a negative** -- control falls to 27-43% at 10% type noise and the target sits between the 10% and 20% noise controls | CM2 (live): error-tolerant model on the noise controls first; else NEAR step 2 (atlas re-pass on the two weakest leaves) |
| antt-fcc-costacabral-1865 (PP-04) | folder, check-solved, 3 DigitArq images; self-glossed draft read as a key: C 63 M 19 U 2, --check 0; V6: N0, key period | none |
| berthier-napoleon-1812 | full 325-group ciphertext from Vilcoq 1969's plate (95.1%, 10 corrections to ciphertext.txt); Chuquet's 22 Dec letters do not fit (rank 3rd-30th of 34 controls); no petit-chiffre key found | a key of the office, or a spec + first cheap test |
| la-garde-1577 | WVO 6467 margin: glosses/insertions, not a solution (N) | none cheap |
| clairambault296-paget-1713 | 129/316 canvases checked, not found (canvas_sweep.tsv) | ASKS 51 (owner pages the Gallica thumbnails) |
| clair1161-avis-flandre-1688 | image on disk was a portrait; f.106 = canvas 128, ff.106-192 printed only | ASKS 54 (BnF, with 49) |
| rah-xiquena-1868 | all 8 leaves: a certified plaintext copy, no cipher on file; status found-solved; V6-XIQ classing | none |
| fr7129-villeroy-bongars-1604 (KT-01) | held: Tomokiyo's Bongars paper not in OpenAlex/S2, academia 403 | LOCAL-QUEUE L8 |

Not worked (no copy-free cheap step, or handed to ZX2 at 19:00 per parent 7c): ormond-arran (Tomokiyo tried Cipher 1 in full), birago,
sp53-22-f52, decode-4450, the BL four, courten, clair571, and the CX2 TNA SP copy-order items, destaing-gerard-1779 (217 tokens of a
600-entry code, key in AAE), hellen, maurice-rupert, harley-287, clairambault1225, wellington-maitland, decode-2754.

**Lessons (LEDGER rows carry each):** a pass-B subagent resumed over batches cost 9.6-16.5 USD a leaf against 3-5 USD for the worker
doing the blind pass itself -- brief passes without subagents; a leaf failing the gate at 77% is repaired by a pass C on the disagreement
rows for 2-3 USD; gate a model test on the transcription's measured error as well as on N (noise-injected controls); calibrate a language
judge on the target's own clear text before reading a FAIL; open an on-disk image before briefing a disk-only job; RAH "telegrama cifrado"
titles describe the transmission (twice now); five of 31 workers overran (P5 2.0x, Y4b 1.8x, L2 1.37x interrupted, L3 1.33x, L4 1.07x),
all with subagents or image bisection. Retrospective trigger met (31 rows, USD 140).

## LANE ZX2 handoff (session_015Bn675gy4Zx5pz8A9CXQzQ), 25 September 2026, 19:09-22:11 UTC (closed)

Opened by the owner-account parent for the CX/CX2 gate-passing hand-offs R6 did not hold. Closed at 22:11 because the copy-free pool is
exhausted. 10 Sonnet workers, USD 49.44 in total, all ledgered and archived; orchestrator USD 6.79. Rate allowed throughout.
**No reading, no AUDIT.md, no NEAR.md row, no target closed.** Every target stays `open`.

| target | what was done (25 Sept 2026) | next (not copy-free) |
|---|---|---|
| ormond-arran-1678 | ZX2-ORM: Cipher 1 table (162 codes, Tomokiyo's image, checked against HMC interlinear). Target 6/20 vs random-key control mean 3.79 (p99 8, p=0.148). All three printed Ormond-Longford ciphers now fail with controls. 4 cipher letters of 1680 in HMC vols 4-5; none pools with the target. | a sibling in the same cipher outside HMC |
| hellen-frederick-1752 | ZX2-HEL: all 8 despatches' ciphertext taken from Bourdeau's audit files (CC BY 4.0, credited). Three codes by date: 1752 846 signs, 1756 516, 1763 1,289 over 6 letters. 1763 one-key Jaccard 0.1456 vs split control 0.1372. Two-part code, values to ~3,900. Spec written, judge fr18. | DECODE images (ASKS 1/42); cipher originals of the Oct 1752-Jul 1753 letters deciphered in NA Fagel 5206 |
| destaing-gerard-1779 | ZX2-EST: 216 tokens, 104 distinct. Three marbois codes: target 22 vs control mean 18.17 [13,24], a control-backed negative for those codebooks. No siblings found (Clements 403; Meng negative). 2 crib positions. Spec written, judge fr18. | Clements copy (ASKS, ZX2-ASK); a retry of the Doniol IV crib text (archive.org 500 once) |
| la-garde-1577 | ZX2-LAG + LAG2: WVO holds 11 La Garde letters and only the target is in cipher; live query matches the harvest. Pool exhausted at 239 signs. | a non-WVO La Garde holding |
| clair1161-avis-flandre-1688 | ZX2-GAL: canvases 216-342 and 0-127 read; with R6 Y7's 128-216 the whole Gallica volume is covered and the cipher leaf is not there. | ASKS 54 (the BnF to locate it) |
| clairambault296-paget-1713 | ZX2-GAL + GAL2: 314/316 canvases read, all print or blank. The 14 Jan 1713 letter is not in the Gallica copy. | ASKS 51 (the BnF to locate it) |
| decode-4450-bnf-fr20506-1525 | ZX2-GAL2 found the fr.20506 copy continuing on ff.137-138 to Ranzo's signature. ZX2-4450T transcribed them (1,027 tokens; blind pass agreement 91.6/90.7/83.9 pct) and aligned them with Bourdeau's fr.2988 witness from index 752 to 1787 of 1789 (80.3 pct agreement): fr.20506 is a complete second witness of the letter. 32 z/d rows were settled against the witness. | none for this lane; a contribution note to Bourdeau once a verifier has looked |
| 15 copy-bound targets | ZX2-ASK: REQUEST.md for BL (bl-james, bl-sacchetti, bl-gualterio, maurice-rupert, sp90-raby-1704, harley-287), TNA (sp87 x4, sp90-raby-whitworth, sp35, sp54, sp53-22-f52) and Clements (destaing); ASKS rows 56 (BL), 57 (TNA), 58 (Clements). | the owner's copy orders |
| tools | ZX2-FR18: tools/data/fr18 (Torcy, Villars, Maintenon, Gazette de France 1786; 2.36M letters; judge language fr18). Held-out 18th-c. false-negative rate fr18 0.183 (N200) vs fr16 0.961 and fr19 0.983. So a fr16 or fr19 FAIL on 17th-18th-c. French is not a test. Flagged to every lane (ROOM 19:50); specs still on fr/fr19 with a 17th-18th-c. date: colbert26-lathuillerie-1644, thurloe-barriere-1654, moustier-altars. It has 6 source files: report the per-fold spread before trusting it (CLAUDE.md rule 3, es17c lesson). | an UPDATES.md row by a parent |

Not worked, and why: ra-karlxi (gated), clair571 (ASKS 49), wellington (library copies only), clairambault1225 (L11), decode-2754 (both published
Sabran keys already failed with controls), and birago (Bourdeau's glyph-level negative with controls; sibling keys fr.3315 already tried).
None of the pool fits a tools/family_run.py family: they are codes, not letter ciphers, and too short for a control to read.
Lead for a parent: WVO 6136 (Reinier Cant, Bremen 1576), a multi-page numeral cipher with no folder (ZX2-LAG flag, ROOM 19:23). Offered at
19:50; not routed. Lessons (LEDGER): a pool-sweep brief must name the minimum candidate count, not only the box (ZX2-LAG stopped after 6 min);
page-per-call transcription of ~400-token pages still costs 3-5x a search job (ZX2-4450T). No live workers, no pending check-in.

## LANE B5 handoff (session_01A4jfQZGS8SUuDamZK19KZq), 26 September 2026, opened 00:55 UTC (live)

Breadth lane, successor to LANE B4, opened by parent 7e (brief `.claude/briefs/runs/2026-09-26-lane-b5-orchestrator.md`, cap USD 25 own, hand off at 300k context). Common file `.claude/briefs/runs/2026-09-26-lane-b5-common.md`. Queue: QUEUE.md "Re-rank for LANE B5, 26 Sept 2026, 00:03 UTC" plus the B4 NEAR steps.

| Spec | Test run (worker) | Target | Control | Verdict |
|---|---|---|---|---|

Live (spawned 00:58): bMAT session_014KYurtmc7wddS3egpmxoBH (matignon, cap 6), bLOP session_011b3guH497ouaLXLXmBc5LT (lope-hurtado, cap 3), bCAS session_01A3aMhAvGEAaSCzMt9ajuKY (castelcicala, cap 4), bBLZ4 session_01VgGGXpAXLYGUh4c3ct4bHc (blitz de20, cap 1.5), bUNT6 session_01Md8yLR5sd5pEdzNNmuGSEv (untersberg joint, cap 5). Reserve wave not started.

## LANE B4 handoff (session_01V2WMavWGMeAUYELUpmyEcX), 25 September 2026, 21:31-23:57 UTC (closed at 308k context; restored 22:45 after commit a34cd00, a room.py 'update' merge, dropped this section and LANE B3's)

Breadth lane, successor to LANE B3, opened by parent 7d (brief `.claude/briefs/runs/2026-09-25-lane-b4-orchestrator.md`, cap USD 25 own, hand off at 300k context). Common file: B3's (`.claude/briefs/runs/2026-09-25-lane-b3-common.md`). Done at open: goldbar-1933 NOTES line 1 set to `open` (parent ruling; Bourdeau 15 Sept no-real-text determination cited); rayburn survey row written from bRAY.

| Spec | Test run (worker) | Target | Control | Verdict |
|---|---|---|---|---|
| sufi-fiddle | 1: intake, image, one blind pass, script checklist (bSUF) | N=165 K=21; RTL, cursive joining, dot diacritics | Arabic-script and Baybayin reference lines (from memory) | Arabic-script family, not Baybayin; image is a hand copy from the novel |
| blitz-ciphers | 2: en judge wired, family_run masc N=581 (bBLZ2) | judge FAIL -1.685 | 0.994 (0.985-1.000) | masc of English excluded; letter chi2 6270 vs English, not transposition; NEAR row, next homophonic K=48 / German (parent's yes) |
| untersberg-code | NEAR step 1: abbreviation expander (bUNT2) | 44 M / 17 I, judge FAIL (circular) | 0.321 vs gate 0.30, shuffled floor 0.289 | weak control, no reading; next the Hs. 2398 image |
| bullet-tuscany-1944 | NEAR step: indicator lookup in print (bBUL3) | M-209 in form only | 2/2 known headers classified | no test licensed at N=44; parked |
| ranks 31-41 | triage (bSPEC3) | 0 spec / 11 no spec | n/a | survey list exhausted for breadth |
| censorship-manual-stego | 1: intake, fetch manual + 4 images, captions read (bCEN) | manual pp.14,16,17 quoted; Morse reference counts | n/a (a fetch) | spec corrected (Illustration No. 11; the manual gives English captions only); Bourdeau 15 Sept already blocked on image resolution (TNA re-fetch pixel-identical); next test must not need sub-5px marks |
| untersberg-code | access: Hs. 2398 lookup (bUNT3) | Salzburg Museum BIB HS 2398 found, 1690-1710, Lazarus Gitschner; 28 IIIF leaves online, f.52v-53r fetched, match to the six lines unconfirmed | n/a | lead: Herzog 1929, Die Untersbergsage nach den Handschriften, pp.27-50 (a published transcription) outranks cryptanalysis |
| untersberg-code | access: Herzog 1929 + leaf (bUNT4) | Herzog p.28 prints Hs 1; 11 witnesses in the apparatus, Hs 12 plain Latin; leaf opening 11 confirmed | n/a | collation next (bUNT5) |
| blitz-ciphers | 3: homophonic K=48 case-sensitive; masc German (bBLZ3) | FAIL -1.518; FAIL -1.768 | 0.971; 0.956 (de20; judge de16) | both excluded with caveats (en fold spread; de register mismatch); next de20 judge rerun, then six-page fetch |
| sufi-fiddle | 3: read as Arabic script (bSUF3) | 165 signs transliterated, no formula or coherent line | none obtainable (stated) | no reading; one group near baraka(t), M |
| untersberg-code | collation vs Herzog witnesses (bUNT5) | Hs 12 initial letters 3/6 | shuffle mean 2.10 (1-3), 42.5th pct of 720 | at chance; next joint alignment with Hs 13/3/3a/11 |

At close (23:57): no live workers, no pending check-in. 14 Sonnet workers, USD 25.06, all ledgered and archived; orchestrator USD 6.78. Every survey rank 1-30 spec has its first test; ranks 31-41 give no specs (bSPEC3 triage). For a LANE B5 (the parent opens it after a scout re-rank of QUEUE.md): NEAR steps named in NEAR.md -- blitz German rerun with a de20 judge (USD 1) then the six-page fetch; untersberg joint alignment against Hs 13/3/3a/11 and a blind transcription of the confirmed leaf; bullet parked; McCormick needs a model whose control passes. Tool gap for the owner of tools/family_run.py: two runs of the same family and seed on different corpora write the same families/<family>-<seed>.txt (bBLZ3 flag); a corpus- or label-derived suffix would stop the overwrite.

## LANE B3 handoff (session_01VLtPMsqR2oWmZeKh2jxVga), 25 September 2026, closed 20:55 UTC (context about 250k; restored after commits 9a1e34b and a34cd00 dropped it)

Breadth lane, successor to LANE B2; opened about 19:10 by parent 7c (brief `.claude/briefs/runs/2026-09-25-lane-b3-orchestrator.md`, cap USD 25 own usage, hand off at 300k context). Common file `.claude/briefs/runs/2026-09-25-lane-b3-common.md`. bMLH was ledgered by B2 (19:20).

| Spec | Test run (worker) | Target | Control | Verdict |
|---|---|---|---|---|
| bullet-tuscany-1944 | 2: family_run periodic_vigenere, 93 indicator keys, crib drag (bBUL2) | Caesar FAIL; 0/93 PASS, 1/12 cribs; drag 59 hits | Caesar 1.000; true key rank 1 3/3; random 1/12 cribs; periods 2-8 5-6 pct (below gate); drag random 31-57 | Caesar and indicator keys excluded; periods 2-8 not a test at N=44: partial, NEAR row added |
| rubin-1953 | 2: family_run masc N=305 and N=293 w/o DULLES/CONANT (bRUB2) | judge FAIL both | 0.989 / 0.974 | simple substitution of English excluded (single-pass transcription) |
| mccormick-1999 | 3: family_run homophonic K=24, three controls (bMCC3) | FAIL -1.48 / -2.33 | English 0.998, vowel-dropped 0.652; shuffled target -1.81..-1.90 | both letter-substitution families excluded; target indistinguishable from its shuffle; NEAR row kept, next token/nomenclator test |
| cylob-c1995 | 1: post 50 fetch + intake (bCYL) | geometric-pattern rectangles, no letters/numbers; 11 of 20 images embedded | n/a (a fetch) | spec updated; survey "24 symbols / Torsten" not in post 50 (flagged); lead cloud.rotering-net.de partial transcription |
| ranks 21-30 | specs written (bSPEC2) | 6 with ciphertext on disk, 4 pending | -- | judge repair: pollaky, scorpion got min_word_cover; untersberg has a primary source (Salzburg Museum Hs. 2398) against the survey's "legend" |
| erba-2006 | 1: image + blind re-transcription (bERB) | 93.0 pct digraph agreement (106/114) with comment #3 | n/a (transcription check) | 8 me/ne ambiguities, possibly a 9th base token |
| blitz-ciphers | 1: IC/frequency, periodic scan (bBLZ) | case-folded IC 0.0628, N=581 | mono-English 0.059-0.071; homophonic 0.042; Vig p20 0.040 | inconclusive, points at masc (test 2 needs parent yes) |
| goldbar-1933 | 1: letter chi-squared (bGLD) | 1.25 / 1.18 | 1000 uniform draws, mean 24.9, min 8.2 | flatter than every draw; re-runs Bourdeau 15 Sept (credited); NOTES line 1 says found-solved -- needs a verifier's word, not a catch |
| yogtze-1984 | 1: initials search de/en (bYOG) | 12 / 18 phrases | random 6-letter strings 337-1879 / 57-825 | below every control; Bourdeau notes a 2025 police closure (uncited) |
| untersberg-code | 1: abbreviation shape (bUNT) | 36 period-closed short tokens | own-unigram synthetic 12.0 (5-20) | 100th pct: NEAR row, next an abbreviation expansion with a control |
| fair-game-2010 | 1: Halpin next-letter (bFAI) | judge FAIL -2.20, cover 0.46 | random marking -2.13..-2.26; planted name 3/3 | negative for this credit-order reconstruction |
| ss-radio-lippert-1944 | 1: image + one pass + IC (bSSR) | N=37 letters, K=18, IC 0.0631 | German 0.047-0.107; uniform 0.042-0.075 | too short to discriminate |
| mccormick-1999 | 4: token/nomenclator anneal (bMCC4) | -0.750, inside its own shuffles | control 0.8 pct vs gate 0.5 | not a test; NEAR row: next a code-word model that passes its control first |

At close (20:55): ONE LIVE WORKER, bRAY session_01ANaWjhm3ix6shRysby4hXb (rayburn-2004 first test, scienceblogs.de holder, cap 3, spawned 20:54) -- the successor or the parent reads its cost with get_session, ledgers, archives, writes its survey row. 14 workers, about USD 33.9 ledgered; orchestrator USD 4.65. For a LANE B4: (1) scienceblogs.de first tests, serial: sufi-fiddle, then censorship-manual-stego (copy the bRAY brief, 2026-09-25-lane-b3-rayburn-2004.md); (2) awaiting the parent: blitz-ciphers test 2 (family_run masc, en judge, USD 3); (3) NEAR steps open without approval: untersberg abbreviation expansion with a synthetic control (USD 3), bullet indicator-system lookup in print (USD 3), McCormick code-word model design (USD 6, strong model); (4) flags open with the parent: goldbar-1933 NOTES line 1 found-solved for a no-real-text determination (verifier's word), yogtze 2025 police-closure claim (uncited in Bourdeau); (5) the cylob survey row's "24 symbols / Torsten" needs a source or a correction. Briefs and the common file: .claude/briefs/runs/2026-09-25-lane-b3-*.md.

## LANE B2 handoff (session_01NS12APP1R55K6TGZrBbP97), 25 September 2026, 19:03 UTC

Breadth lane, successor to LANE B (whose bHAR/bLIM died on the 24 Sept limit unpushed). Opened 15:39 by parent 7b; handed
off at 425k context (brief: 300k), own usage about USD 10.3 at 19:02. 18 Sonnet workers, about USD 45.7, every one ledgered
and archived except bMLH (live at handoff, see below). All 17 first tests of the survey's top 20 specs that were unrun are
now run except cylob (brief on main). No judge PASS on any target; two first tests moved a spec; one worker's judge PASS
was a length-only judge block and is withdrawn (tool fixed).

| Spec | Test run | Target | Control | Verdict |
|---|---|---|---|---|
| harry-caroline-1863 | 1 MASC, word breaks | judge FAIL -1.442 | 16-34% letters right at N=74 | uninformative (control weak) |
| lima-1916 | 1 codebook grep, 4 books | 2/2/1/3 of 17 | random 2/1/1/3, positive 17/17 | negative, at chance |
| moustier-altars | 1 images, 2 passes (90.5%), IC | 0.0499 | Latin 0.072 / French 0.073 / random 0.0385 | not informative; intake open (bINT) |
| powers-1991 | 1 print check | no decipherment in print | n/a (search) | negative; Thomas 2006 queued L15 |
| debosnys-1883 | 1 images, machine sign inventory | IC 0.0125, K=90 over-split | random 0.0111 / French 0.070 | inconclusive; LANE GOLD holds the target |
| dorabella-1897 | 1 letter-text route | Powell 1937 open copy lacks the letter | n/a | blocked, ASKS row 50 |
| kaliningrad-2015 | 1 transcription check + IC | 26/26 lines, IC 0.0657 | translit. Russian 0.056 / German 0.072 | not informative; intake open (bINT) |
| bullet-tuscany-1944 | 1 forum claim vs 4 key families | no key maps it (44 vs 39 letters; MASC 37-39/39 violations) | every control key recovered | **moved**: claim closed with a control; next test 2 short-key Vigenere + crib, est. USD 2, awaiting parent |
| mccormick-1999 | 1 token profile; 2 family_run masc | IC 0.089, n-gram coverage above all controls; test 2 judge FAIL both corpora | English 0.067; controls 0.994 / 0.985 | NEAR row updated; masc excluded; next homophonic est. USD 3 if kept |
| copenhagen-1835 | 1 MASC da/de/en | no legible decode | da 0-74% erratic, de 81-86%, en 94% | not informative; da19 corpus built and wired |
| pollaky-1865-1875 | 1 images + pass; 2 pass B + diff | ads 3-4 IC 0.064/0.066; 72/72 vs Ernst/Bourdeau | English 0.059-0.066, random 0.04 | ads 3-4 are the Catokwacopa ads (known mechanism); NEAR row proposed exit |
| te-wood-1950 | 1 Gillogly attack, 4 key texts | best 12-16/21 | control true offset rank 1 every seed (19-20/21) | negative for these key texts |
| scorpion-1991 | 1 images + pass | S1 N=70 K=53 IC 0.0083 | English 0.066 / random-at-K 0.019 | homophonic-scale; S2 counted only |
| rubin-1953 | intake + 1 image + pass | letters N=305 IC 0.0612 | English 0.062 / random 0.039 | **moved**: English-like; next family_run masc at N=305, est. USD 3, awaiting parent |
| mlh-1976 | intake + 1 image + pass | N=33 K=26 IC 0.0189 | English 0.062 / random 0.039 | too short; line 1 'MLH => 7 symbols' a possible crib (bMLH, ledgered 19:21) |
| cylob-c1995 | not run | -- | -- | brief `.claude/briefs/runs/2026-09-25-lane-b2-cylob-c1995.md` |
| catokwacopa-1875 | (spec written, no test: partial, other lane's folder) | -- | -- | -- |

Changes made to shared files: `.claude/briefs/breadth.md` has an Intake step before any first test (QA 2026-09-25-1740 failure
3); `tools/judge_plaintext.py` fails closed on a judge block with no content check or an unwired language code
(`tools/tests/test_judge_plaintext_failclosed.py`), and `da19` is wired; `specs/mccormick-1999.json` and
`specs/copenhagen-1835.json` judge blocks repaired. Known effect on another lane: `specs/na-suriname-map-1781.json` (nl, no
corpus) now fails loudly. Spec writer bSPEC's ten specs (ranks 11-20) carry judge blocks without `min_word_cover` in most
cases; a successor should check each block before trusting a judge line.

For a successor (LANE B3): ledger bMLH (session_01PmhUa6TvpUCGWqnG13xbSh) if this session has not by the time you read
this (check LEDGER.md); run bCYL; run bullet test 2 and rubin test 2 once parent 7c says yes; the survey ranks 21-30 have
no specs yet. Host notes: every Cipherbrain image sits on scienceblogs.de (one worker at a time); Gutenberg was LANE GOLD's
today; an image-and-two-pass first test does not fit USD 3 with a subagent (bMOU 7.61), one pass with no subagent does.

## LANE GOLD2 handoff (session_013JXDgLDkW2y5Ldi2gWzTkY, Fable, closed 25 September 2026 23:37 UTC at about 385k context on the parent's 400k rule; GOLD3 starts here)

Standing lane on koehler-1944 then debosnys-1883, reserve kaliningrad-2015 (brief `.claude/briefs/runs/2026-09-25-lane-gold-orchestrator.md`; owner amendment: Fable for tool/family design and the consolidator at cap $15, Sonnet for swarms; families run through tools/family_run.py; NEAR.md koehler row is the lane's register). Both targets `open`, intake gates exit 0 at 23:35. This incarnation 20:05-23:37: 8 sessions, 52.88 dollars (workers D1 6.17, K2 6.55, K1 6.36, D2 1.61, B2D 9.46, K3 7.37; consolidators CONS2 7.90, CONS3 7.46), no F, none past 1.5x cap (D1 and K3 ran 23 percent over); own cost about 12.5 (get_session, last read 11.86 at 23:34).

**Running at handoff (GOLD3 reads get_session cost on each at its first check-in, interrupts at 1.5x cap or at the box, ledgers, archives, NEAR row):**
- GOLD-KAL1 session_01QR7XH9k8XQmzHPZRRwbVN7 (Sonnet, $5 / 45 min from 23:36): kaliningrad-2015 reserve -- word-pattern crib test of the Synodal-chapter claim (shuffle control first, gate 0.9, both tokenisations), then German light homophonic at N 978 K 36 through family_run.py; brief `2026-09-25-lane-gold-c4-kaliningrad-crib-and-homophonic.md`.
- GOLD-K4 session_01PYtPexePhLjYkgc8VsZ7Zn (Sonnet, $8 / 75 min from 23:36): Koehler B' owed runs -- plaincipher and keycipher placements, then the English keyword list, control first each; brief `2026-09-25-lane-gold-c4-koehler-bprime-owed.md`.

**Koehler (numbers in ciphers/koehler-1944/HYPOTHESES.md "Summary, cycle 3" by GOLD-CONS3):** the ladder has established (1) a non-uniform key stream (GOLD-2C: inside the keyed-tableau band 6/6, outside the uniform-OTP 99 pct band 5/6); (2) no keyword-mixed or cipher-side-mixed letter-arithmetic tableau reads above noise at 924 letters -- B standard tableau parked at two key registers (controls nl20 67.1 / nl_dev 84.3 pct vs target -3.57..-3.64 inside the one-time-key band), B' parked on six of seven placements (controls 72.6-89.6 pct vs targets -3.534 / -3.478 / -3.573 / -3.583 / -3.498 / -3.518 inside the ten-text beau band -3.548 / -3.531 / -3.494; K2's beau -3.478 sits 0.016 above that band's max, under the 0.1-nat flag line; judge FAIL throughout); (3) a free permutation is unidentifiable at this length (GOLD-B2D: control 7.4/12.9/8.1 pct, S3 letters correct 1/8/3 of 26, needs about 5000 letters). A recovery blocked on the owner (ASKS 55 NARA RG 65 105-9673 and Farago 1971; ASKS 53 Kahn/Cryptologia six groups, scan confirmed print-disabled 22:44). E untestable at this N, D excluded, D' unfalsifiable, C merged into B''. Devotional Dutch key corpus tools/data/nl_dev (Statenvertaling, 3.4M letters) on disk. CONS3's recommendation: after K4, PAUSE Koehler spend until family A material; the target stays partial/open with its NEAR.md row (rule 5, never closed-negative).
**Debosnys (ciphers/debosnys-1883/HYPOTHESES.md "Summary, cycle 3"):** transcription-limited by the measured curve -- base-level (K_base 128, 16 mark classes) homophonic control 0.859 clean, 0.816 at 2.5 pct type noise, 0.385 at 5, 0.322 at 7.5, 0.314 at 10; K160 0.440 clean; c2 alone 0.669 clean / 0.433 at 5 pct. The cliff sits between 2.5 and 5 pct and a settled two-pass lands at 5-10, so (c) for the letter families under the gate written before the numbers; no settlement pass bought; NC has no test a single-pass draft supports; V parked. NO NEAR.md row (no solver ran on the target, no control-backed gap). Park until the museum answers ASKS 52. Tools left behind: homophonic.py `profile=target` and `noise=p`, scripts/base_mark_recount.py, glyphs/base_mark.tsv.
**Reserve kaliningrad-2015:** LANE B2's first test logged (N 978, K 36, IC 0.0657 vs transliterated Russian 0.0563 and German 0.0724); CONS3 read word divisions, apostrophes after consonants and the one specific host-text claim (Frank 2021, Synodal 1876 chapter) as the highest lead class; a Russian masc is impossible without a tool change (homophonic_anneal folds to a-z, no ru corpus). KAL1 is running it.
**GOLD3 runs first:** first check-in on KAL1 (box 00:21) and K4 (box 00:51); ledger and archive each with the get_session cost; NEAR.md koehler row with K4's numbers. Then consolidator cycle 4 (Fable, $15, brief pattern `2026-09-25-lane-gold-consolidator-c3.md`): on KAL1's numbers decide whether kaliningrad gets a second box; on K4's whether the B' record is complete (seven of seven placements); then, if Koehler pauses and Debosnys is parked, either move the lane's spend to the reserve or tell the parent in ROOM ("for the parent: GOLD lane idle-standing, waiting on ASKS 52/53/55") -- the owner is away until about 03:00 UTC 26 Sept; anything for them goes to ASKS.md.
**Lessons for GOLD3:** a background noise band of ten decoder runs contends with the family runs and pushed K3 to 23 percent over cap -- brief a band as its own $2 box; a new control option needs a one-seed sanity check before the seeds (D1 rewrote profile=target mid-box); size family_run's external timeout to control plus target (K1); a Fable design job that measures an identifiability limit and stops is a good outcome (B2D, 26 of 90 min); check-ins on Fable cost about 35k context each at this transcript size, so an incarnation holds about eight check-ins before the 400k line -- keep this section current from check-in 4 on, not at the end; read `date -u` in the same command that writes a brief.

## LANE GOLD handoff (session_01DKDynpdEwZK5EokxtjCM3P, closed 25 September 2026 19:57 UTC at 438k context; GOLD2 starts here)

Standing lane on koehler-1944 then debosnys-1883 (brief `.claude/briefs/runs/2026-09-25-lane-gold-orchestrator.md`; owner amendment 16:51: Fable for tool/family design and the consolidator, cap $15; parent 18:18: families run through tools/family_run.py; NEAR.md koehler row is the lane's register). Both targets check-solved `open`, intake gate exit 0 (19:56). Orchestrator own cost about 8.7 dollars; workers 82.7 dollars over 13 sessions (one F: GOLD-4D).

**Running at handoff (GOLD2 must read get_session cost on each at its first check-in, interrupt at cap, ledger, archive):**
- GOLD-K2 session_0196VjuQaoVfdo8pYY9Avvm9 (Sonnet, $6/75 min from 19:56): Köhler B' untried variants (beau arithmetic, German key model, English-word keywords), control first via family_run gate 0.5.
- GOLD-K1 session_01WDJiUb1ijocbB3N3LtsLWk (Sonnet, $8/60 min from 19:56): tools/data/nl_dev devotional Dutch key corpus, then B and B' reruns against it.
- GOLD-D1 session_01Qcv68Pn46JNXkktRXTv6DL (Sonnet, $5/60 min from 19:56): Debosnys noise-matched homophonic controls at N 1251 K 160 and base level, noise 0/0.1/0.2, controls only; decision rule (a)/(b)/(c) in ciphers/debosnys-1883/HYPOTHESES.md top block decides whether more transcription is worth buying.

**Köhler families (numbers in ciphers/koehler-1944/HYPOTHESES.md, top block by GOLD-CONS1):** A recovery: TNA KV/HW empty; FBI HQ file RG 65 105-9673 box 156 and Farago 1971 are owner asks (ASKS 55); six-group Schmeh/Bourdeau transcription discrepancy, Kahn 1981 pp.65-66 (ASKS 53, variants in ciphertext-variants.tsv). Bourdeau 15 Sept: six families excluded with controls. B standard-tableau running key PARKED: control 60.4-79.1 pct vs target joint ll -3.57..-3.62 inside noise -3.57..-3.64 (GOLD-2A). B' keyword-mixed tableau corner PARKED: control 79.1/74.0/64.7 pct vs target -3.534 inside noise -3.507..-3.544, judge FAIL (GOLD-2C). Key fact: letter statistics inside the keyed-tableau band 6/6 and outside the uniform-OTP 99 pct band 5/6 -- uniform OTP excluded. Open: B' variants (K2), devotional key model (K1), B'' general permuted tableau (cycle 3 Fable design if K1/K2 flat), D' hand-made non-uniform key (only A resolves).
**Debosnys families (ciphers/debosnys-1883/HYPOTHESES.md):** transcription is the bottleneck: 160 ids (36 composites), blind pass agreement 62.3 pct on c1 (GOLD-4E) and 22.4 pct at 68 ids on c4 (4A); ciphertext.txt still B2's single-pass draft. Homophonic French: controls only until D1 prices noise. Base+mark: recount inside D1. Code: parked until transcription gated. Verse form: parked (r 0.44, 93.6th pct; Sektu 2017 rejected alexandrines). Museum ask ASKS 52.
**GOLD2 runs first:** read the three done lines above; ledger/archive; then consolidator cycle 2 (Fable, $15) on their numbers; if D1 says a homophonic control reads at the pass-noise level, the next Debosnys job is one cryptogram per worker, no subagent, cost read at 15 minutes (GOLD-4D ran to 3.3x cap through one subagent).
**Lessons for GOLD2:** read the solver repositories' own campaign before building a family (Bourdeau had excluded B standard for pennies); image passes cost signs x inventory size, not pages; read `date -u` before typing any time into a brief (this orchestrator slipped twice); never rebase while a decoder writes a log in the tree; at most two order-8 decoders per container.

## Parent handoff (owner account, session_01FXDfYR3CvGk7tcid1Aav1n), from 25 Sept 2026 00:30 UTC, kept current

Role brief: `.claude/briefs/parent.md`. Check-in: a self-bound send_later titled "Parent check-in: lanes LX, DX, OX",
hourly, re-armed at each firing (find the current id with list_triggers). Lanes on this account (briefs
`.claude/briefs/runs/2026-09-25-lane-{lx,dx,ox}-*.md`): LX antt-linhares-chave (session_01UXTpujdthrPiBDUG57oNwf;
book identified as Vieyra 1809 Part I, m0002 decoded in part), DX DECODE (session_01LgrmyB7HMcMaeLTRNbEqb4; login
works, full-size images and documents still permission-blocked, ASKS 42/43; see its handoff), OX orphaned open targets
(session_01BE3g8tWbS4T24KXMpShHt4). Owner's standing decisions, 25 Sept 2026: no history purge (name, emails and images
may stay; secrets may not); spend is not a restriction on the Max plan, the rate limit is; a missing credential never
blocks, route around it; all credentials fixed on this account at 00:47 UTC. The other account's parent (7b) and its
lanes (R5, N4, B, V2) are idle until its window resets 26 Sept 13:00 UTC; their targets are theirs.

Check-in 25 Sept 02:48 UTC: rate limit allowed on every lane. LX has its N3/N3 AUDIT.md synced to the corrected reading (H 25, M 1) and SO-LINHARES-M0002 queued for the ChatGPT runner (no [SO-] pull request open yet); maco 86 sibling sweep at 17 of 21 items, no further cipher; LX expected to write its handoff at its 03:09 check-in. DX closed on handoff 02:12. OX live with four workers (van Beuningen key, Hellen 1752, Paget 1714, Breda confirmed found-solved). No new lane opened: the queue holds no open, copy-free target outside OX's pool; the next unlocks are the owner's copy orders, the DECRYPT role upgrade (ASKS 42/43) and the other account's R5 intake when it resumes.

Check-in 25 Sept 03:52 UTC: LX closed on handoff 03:10 (reopens only for the SO-LINHARES-M0002 pull request, none open yet). OX live, next check-in 03:54: van Beuningen 1657 AUDIT.md, key N3 and letter N1; Paget attempt 1 negative with control; WVH 1069 under the transcription gate; La Garde editions checked; Hellen waits on DECODE images. Rate limit allowed. Still no open copy-free target outside OX's pool.

Check-in 25 Sept 04:25 UTC: LX-ED could not reach Textos Politicos 1993 by any cloud route; queued as LOCAL-QUEUE L10 for the owner's machine (Linhares stays N3). Second opinions queued: SO-LINHARES-M0002, SO-VANBEUNINGEN-1657. Intake had run dry (no open copy-free target outside a lane), so LANE PX opened (session_01KapVpHVzNpnnQce5C8c3LY): DigitArq past its ten-result search limit, dictionary and book codes copy-free, check-solved under the intake gate, then readings.

Check-in 25 Sept 04:55 UTC: OX closed on handoff 04:35 (ASKS 46 Heinsius request, LOCAL-QUEUE L11 AN Marine B7). PX live: PX-01 Brochado letterbook 1712-13 (cipher with in-volume decipherments) to check-solved at its 05:03 check-in; the dictionary-code scout found nothing new copy-free. No [SO-] pull request yet; L10 still queued. PX is the only live lane.

Check-in 25 Sept 05:56 UTC: PX live. PX-01 Brochado letterbook (antt-msliv0638-brochado-1712): check-solved went blocked (Doria 1944 unreadable) then open on a Google Books search-within of that edition with live hits elsewhere in it (cifra p.151, Londres in the preface), so the zero hits for the London-embassy vocabulary are a real negative; the intake gate held. A second DigitArq harvest (PX-SCDIGI4) is running. HOSTS wrote the 38-host table into the Access playbook. No [SO-] pull request; L10, L11 still queued on the owner's machine. ASKS 47 lists five optional discovery keys.

06:17 UTC, owner priority more solves: LANE TX (session_01UDxtM9Xv2dnPfoo5z9T6wA, printed ciphertext + WVO 5551), LANE KX (session_01JPoYAFvVfraJibxQdQfrqp, key reuse: our ~60 key tables against every unread ciphertext, and each key's office against unread letters), parent worker AUD2 (session_01NTKxpfXJHgtJsE3FsX7cKB, second audits of Linhares and the van Beuningen key); PX told to put Brochado first. The WVO Lodewijk/Jan van Nassau pool is mostly printed by Groen and already classed; one unclassed letter (5551) went to TX.

07:15 UTC check-in: AUD2 done (both second audits agree). Van Beuningen item 2 now counts (N3, two audits, key ours, text in print). Linhares N3 after two audits but held out of the totals by QA 06:38 flags (verdict word open->blocked pending L10; no fresh re-derivation of the H25/M1 reading): parent worker LX-QAFIX (session_013GbUJDKD4jsiEoYnuQoyxZ) is closing both; status.json field `qa_flag` holds a flagged result out of both board totals until cleared. Board: 11 entries at N3+ after two audits (16 letters), 2 with our own key (WVO 53, van Beuningen). AUD2 and QA baseline ledgered and archived. Lanes PX/TX/KX/VX all allowed, all with pending check-ins; KX-XMATCH control not yet reported. roell-vandedem-1809 (VX-E02 key sits in the same NA toegang 1.02.20) is LANE N4's nomination: parked for N4, not ours. Next QA run due ~08:40 (window from 06:38). No [SO- pull requests open.

08:25 UTC check-in: LX-QAFIX cleared both Linhares flags (verdict now blocked pending L10; fresh re-derivation 24/26, justa H->M, H24/M2); qa_flag removed, Linhares counted. Board: 12 entries at N3+ after two audits (17 letters), 3 with our own key (WVO 53, van Beuningen, Linhares). WVO 5551 (TX): N3 after one audit, key labelled ours; TX-AUD5551 on the second audit; SO-NASSAU-5551 queued; QA asked to check whether 'ours' should be 'period' (table rebuilt from 4613/4615's period decipherments). KX-XMATCH2: positive control 8/35 keys, 0 false positives on 8 negative pairs, partial; no new cross-match hit yet. PX: two Sonnet workers overran their alarm ($30.92, $14.42) with 'under cap' lines; orchestrators watch cost via get_session (ROOM 08:25); retrospective item for COMMON. Rolling QA run 2 spawned 08:18 (session_01LkyvEf8FXwnfxbjbXnP1kn, window from 06:38). LX-QAFIX ledgered, archived.

09:35 UTC check-in: WVO 5551 N3 after two audits (V-TX, V-TX2), key ours, QA run 2 clear -> counted (named gap: Glawischnig 1973 cites the letter; second copy Staatsarchiv Marburg 4f Nld. 165 unchecked). Board: 13 entries at N3+ after two audits (18 letters), 4 with our own key (WVO 53, van Beuningen, Linhares, WVO 5551). QA run 2 (QA/2026-09-25-0819.md) 0 live failures, ledgered and archived; its blank-$ finding fixed in CLAUDE.md ('Claim before you start'). Retrospective h spawned 09:27 (session_01A9iFETuHLYVJw7yyw4E2b5; 81 rows / ~$444 since retro f). Lanes: PX (Brochado: glyph settled, key 40 codes/29 C; BRODEC2 re-running the body control with a leave-one-out design), TX (Barriere negative with control; Brederode open, TX-KEYS hunting a key), KX (Colbert 26 La Thuillerie: every cipher canvas carries a period interlinear decipherment, so a period key, not a reading; last ROOM 09:03 -- verify it has a check-in scheduled), VX (Schonenberg, Suriname maps, Janssens Java 1811, Oldenbarnevelt 1605 in progress; no reading past judge yet). Next QA run due ~10:25 (window from 08:25).

10:35 UTC check-in: LANE TX closed 09:34 and LANE PX closed 09:55 on their handoffs (above). Parent opened LANE YX (session_01PHaEdHeQY2FtMHLo9yGeoe, left-open targets: Brochado letter 134 after PX's Carta 79 check, oldenbarnevelt-brederode-1605, triage of every open unclaimed target; brief .claude/briefs/runs/2026-09-25-lane-yx-orchestrator.md). RETRO-2026-09-25h: proposals 1-4 to RETRO-APPLY-H (session_01Aha4ppqZm3C1oioLbAqUo9); proposal 5 taken by the parent (cost per solve below). QA run 3 spawned (session_01Kfi8nWAJk4qJodF9mRLwF9, window from 08:25). KX retracted its 09:03 claim: colbert26 La Thuillerie carries topical paraphrases, not a decipherment. Board unchanged: 13 entries at N3+ after two audits (18 letters), 4 with our own key. Cost per counted solve today by lane (worker usage / solves, RETRO-H table): OX $95/1, LX ~$46-51/1, TX ~$62/1 (lane handoff figure), VX $102+/0, PX ~$90/0, KX ~$92/0 (incl. $44 on stalled KX-LATHKEY), DX $13/0. Rate allowed on every lane (five-hour window resets ~11:40 UTC). No [SO- pull requests open.

11:40 UTC check-in: KX closed 10:59 and VX closed 11:08 on handoff. YX live (session_01PHaEdHeQY2FtMHLo9yGeoe, 5 workers: pt17 judge corpus, Clair 349, van Hessen, Baluze 156, Wellington dictionary; Brochado letter 134 candidate decode after the Carta 79 fix, not yet a reading). Parent opened LANE CX (session_01SRJHk4mkeudAH4L39Kc9K6): formal check-solved on the ~36 copy-free open targets failing the intake gate (YX triage: 2 of 99 pass), passes to YX. QA run 3 (QA/2026-09-25-1036.md): 4 failures, none on a counted result, routed to YX. RETRO-APPLY-H done (tests pass). Both archived and ledgered (LX-QAFIX and QA run 2 recoded C->Q). Board: 13 entries (18 letters) at N3+ after two audits, 4 with our own key. Cost per counted solve today by lane: OX $95/1, LX ~$51/1, TX ~$62/1, VX ~$205/0, PX ~$90/0, KX ~$92/0, YX ~$21/0 so far (owner 10:38: cost is not a concern; reported for the record). Rate allowed; window resets ~11:40. No [SO- pull requests.

12:45 UTC check-in: Linhares held out of the totals (status.json qa_flag): with YX-PTJUDGE's new pt17 corpus the rule-7 language judge FAILs its committed reading (-1.559 vs real_p05 -1.014; word cover 0.758). Parent worker LX-JUDGE (session_01Gd5mq661tHULFJy88jew5S, brief 2026-09-25-parent-linhares-judge.md) tests with design-matched controls (period Portuguese fragments, random Vieyra headword sequences, shuffled reading) whether the judge can discriminate on a 26-word dictionary-code fragment; verdict A clears the flag with the evidence named, B means the reading's coherence is unsupported. Board: 12 entries (17 letters) at N3+ after two audits, 3 with our own key. CX round 1: 21 targets, 13 pass the gate (10 to YX), 3 blocked with local-runner rows (L8, L9, L13), 4 partial; bl-charles-digby found-solved (F1). YX: Brochado letter 134 FAILs language (no reading); Barriere pass B reconciled 90.5%; Hessen parked (1127 not imaged); TR349, LOC571, BARB running. QA run 4 (session_019SR3eNrE7asnrdpLuLphEY, window from 10:36). Cost per counted solve, for the record: OX $95/1, TX ~$62/1, others 0 so far; Linhares' LX $51 now 0 counted pending LX-JUDGE. Rate allowed (window resets 17:20 UTC). No [SO- pull requests.

13:55 UTC check-in: the seven-day window is at allowed_warning on every session (parent included; resets about 05:00 UTC 26 Sept): no new workers anywhere. YX closed 13:34 and CX closed 12:56 on handoff (their sections above), so every owner-account lane is closed. LX-JUDGE verdict C: Linhares stays held out (fixed judge: -1.147 vs real_p05 -1.102, wrong-key level -1.462; reading beats 183/200 wrong-key Vieyra strings, 5.5th percentile of real 1808 prose; real prose fails this threshold 8.5% of the time with a corpus 150 years older). Parent fixed tools/judge_plaintext.py (drops '#' header lines from --file input) and LOCAL-QUEUE.tsv (conflict markers; L13 catokwacopa, L14 sp53-16-78/79). QA run 4 (QA/2026-09-25-1245.md): 2 failures, both fixed. Board: 12 entries (17 letters) at N3+ after two audits, 3 with our own key. Cost per counted solve today, for the record: OX $95/1, TX ~$62/1; LX, VX, PX, KX, YX, CX, DX 0 counted. FIRST AFTER THE RESET (~05:00 UTC 26 Sept, before 13:00 when the other account resumes): (1) a Sonnet worker builds a Portuguese c.1780-1830 judge corpus (not Vieira, not target material; LX-JUDGE's 1808 source is a start), calibrates, re-runs Linhares -- a clean PASS with its control clears the qa_flag; (2) a verifier for bl-charles-digby's found-solved (Wheatstone 1862); (3) reopen a deep-work lane on the 13 gate-passing targets YX listed in its handoff.

15:55 UTC: owner 15:45 'keep going', window allowed again on this session. The other account's parent 7b came back 15:38 and opened LANE R6 (Salviati + the 13 gate-passing CX targets), LANE V6 (Portuguese 1780-1830 corpus + Linhares re-run, Digby verifier, verifiers, rolling QA every two hours) and LANE B2 (breadth); a closer ledgers its 24 Sept sessions. It took this handoff's three post-reset items, so the owner account does not duplicate them: my rolling QA is suspended while V6's runs. Opened LANE ZX (session_01MxueEQJUGF9PWJiYcVyvBM: YX's own partials antt-msliv0638-brochado-1712, clair349-este-guise-1556, thurloe-barriere-1654; readings go to V6 for verification), LANE CX2 (session_018cUWVBDyZzw2sgLAmZKL75: check-solved round 2 on the section D campaigns; passes go to R6) and parent worker TOOLS-GATE (session_015aESJVn3gguVTXN7sLtNJC: intake_gate_check.py found-solved and open-over-unread-edition). Owner: the ChatGPT second-opinion runner is live (three rows queued: SO-LINHARES-M0002, SO-VANBEUNINGEN-1657, SO-NASSAU-5551); no [SO- pull request open yet at 15:50. Board lanes list now carries both accounts' lanes. Linhares' qa_flag clears only on V6's reported PASS with its control.

16:55 UTC check-in: LINHARES COUNTED AGAIN -- V6-PTCORP built the pt18 corpus (Correio Braziliense + Investigador Portuguez 1808-1819, 3.23M letters) and the judge PASSes the reading (-1.051 vs real_p05 -1.122, null_p99 -1.452; V6 orchestrator reproduced it 16:17; held-out false-negative rate 4.0%); parent cleared the qa_flag 16:35. Board: 13 entries (18 letters) at N3+ after two audits, 4 with our own key (WVO 53, van Beuningen, Linhares, WVO 5551). bl-charles-digby N0 (Wheatstone 1862 deciphered Add MS 6912 itself; text printed Groen 1859). Second opinions: PRs 10-12 open (Linhares, van Beuningen, WVO 5551), rows marked posted, citation checks with LANE V6. Keys: EUROPEANA_API_KEY and DPLA_API_KEY set and probed (200; 1668 and 805 hits); APE dropped (no self-service registration on the redesigned portal); DDB and CORE still open (ASKS 47). Owner-account lanes: ZX round 1 (Brochado gate passes 85.3 vs 94.4 but the judge cannot decide at 40-70 letters, letter 134 at bucket percentile 5 -> no reading; Clair 349 atlas passes agree 39.3%, a quarter of tokens match no key sign; Barriere: ZX-BAR's closed-negative reversed by its orchestrator (X), ZX-BAR2 re-running with mark typing); CX2 round 1 (13 targets, 10 gate-passing handed to R6; 25 targets now pass the gate in all; berthier-napoleon-1812 found-solved test negative, stays open; catokwacopa, wellington, decode-2754 verdicts re-formatted). TOOLS-GATE done and ledgered. The other account: parent 7c succeeded 7b and opened LANE GOLD (public unsolved list, Fable for design work); R6 has costacabral-1865 (self-glossed draft) with V6 as found-solved; Salviati f.55v pass B gate 77.5% (fails 80). Cost per counted solve, for the record: unchanged. Rate allowed.

17:05 UTC: owner away until about 03:00 UTC 26 Sept ('keep going; check what the other account pushes and learn from it'). Unattended mode: hourly check-ins continue; anything he must decide goes to ASKS.md and this section. New standing duty parent.md item 9 (cross-account learning pass every third check-in); first pass running: parent worker LEARN session_01WfFuM22oxmaWEWn4Afbsej (brief 2026-09-25-parent-learn.md, output LEARN-2026-09-25-<hhmm>.md). Check-in counter for duty 9: 1 of 3 at 17:57.

18:15 UTC check-in (unattended, duty-9 counter 1 of 3 since LEARN pass 1 at 17:18): second opinions done -- V6-SOCHK traced every claim in PRs 10, 11, 12 to its page (Linhares 7 confirmed + 1 repo record, 1 unreachable; van Beuningen 8 confirmed with one misquote, 1 page-count discrepancy; Nassau 5551 9 confirmed), no prior print found; PRs closed with the files landed; two small corrections logged in NOTES (Linhares key trim from either end; Nassau's Christoph is Pfalzgraf Christoph). Board unchanged: 13 entries (18 letters), 4 with our own key. LEARN pass 1 (LEARN-2026-09-25-1718.md): 4 portable items, 2 diffs applied by parent 7c (lead-class order in LESSONS.md; wall-clock box also a minimum in the README tail), ledgered Q, archived. CX2 closed 17:06 (archived): 33 targets now pass the intake gate, copy-free pool exhausted, no successor. ZX: Barriere 1654 closed-negative with a control; Brochado at a named stop; Clair 349's key sheet read once turned 90 degrees (52 H / 10 M), ZX-TR349C re-passing the ciphertext with the gloss margin. V6-QA1 (window 12:45-17:52): 3 failures, none on a board result -- Digby key field fixed by the parent 18:10; TOOLS-GATE2 (session_01TRWXgDMBmsm7TmgLr67X6T) adds solved/closed-negative/offline-only to intake_gate_check.py; the breadth-brief intake gap is B2/GOLD's. Offered parent 7c (ROOM 18:10) that the owner account takes CX/CX2 hand-off targets R6 will not reach; decision at 19:05. Other account: Salviati all 8 leaves pooled (2,820 signs), cm control running; Mercy 1648 anneal gap 167-181 points over control, reproducible, Fable worker reading it; costacabral-1865 N0 solved (key period). Rate allowed on every session.

19:20 UTC check-in (unattended, duty-9 counter 2 of 3): parent 7c accepted the capacity offer (ROOM 18:18): every CX/CX2 gate-passing target without an R6 claim by 19:00 is ours; R6 claimed only Mercy 1648 and Salviati NEAR steps (keeps Berthier, Costa Cabral, Xiquena). LANE ZX2 opened (session_015Bn675gy4Zx5pz8A9CXQzQ, brief 2026-09-25-lane-zx2-orchestrator.md). New shared rules from the other account this window, all in UPDATES.md: tools/family_run.py (control first) for every cryptanalytic run; NEAR.md near-solve register (control-backed gap = partial, never closed-negative; six rows incl. Brochado letter 134); judge_plaintext.py fails closed on a spec without a language corpus or cribs; tools/room.py --start prints UPDATES and NEAR. ZX: Clair 349 Opus passes 70.7 pct (gate 60), settling. TOOLS-GATE2 done (19 terminal-status targets now exit 0), ledgered, archived. Other account: Mercy 1648 reading (S 494 / M 27, key by anneal, judge FAIL on both Spanish corpora with a 23.5 pct false-negative rate) with verifier V6-MERCY; Salviati cm untestable at current transcription noise (NEAR row); B2 handing off to B3; GOLD Koehler keyed-tableau family not excluded. Board 13 entries (18 letters), 4 with our own key. Rate allowed everywhere. Next: LEARN pass 2 at 20:07.

20:15 UTC check-in (unattended, duty-9 counter 3 of 3): LEARN pass 2 deferred one check-in on purpose -- parent 7d (the other account's successor of 7c, took over 20:03) wrote at 20:06 that its own LEARN pass is next; running ours in parallel would duplicate it, so at 21:10 the parent reads the other account's LEARN-*.md if landed and applies its owner-account diffs with a short Sonnet retro-apply worker, else runs pass 2 from .claude/briefs/runs/2026-09-25-parent-learn.md (window 17:18 onward). Lanes: ZX (session_01MxueEQJUGF9PWJiYcVyvBM, 413k context, 8.15 dollars) -- ZX-TR349D done, ledgered 50.68 (Opus): Clair 349 ciphertext settled, 1,174 rows with gloss, key vs gloss 54.1 percent exact, 82 lone 4s likely S36; ZX-DEC349 (Opus, 75 min) decoding now, ZX check-in 20:53. ZX2 (session_015Bn675gy4Zx5pz8A9CXQzQ, 232k context, 4.48 dollars) -- round 1: five workers done (ormond Cipher 1 162 codes, 6/20 vs control 3.79, negative; hellen pool 2,651 signs in three codes, one-key test at control; destaing marbois codes inside control band; la-garde 0 same-system siblings; clair1161 not in the whole Gallica volume, ASKS 54 stands); ZX2-ASK wrote 15 copy-order REQUEST.md files and ASKS rows 56-58; fr18 judge corpus wired (held-out FN 0.183 vs fr16 0.961 on 18th-c. prose: every earlier fr/fr19 FAIL on 17th-18th-c. French was not a test -- ZX2 flagged the affected specs). Other account: Mercy 1648 read with our key, V6-MERCY N3 (one audit; counts after the second, which 7c asked V6 to spawn), R6 closed 19:26 and R7 opened on its NEAR steps, B2 closed, B3 and GOLD2 live. Rate allowed on every session. Board: still 13 entries / 18 letters after two audits, 4 own key; Mercy would be the fifth own-key entry once the second audit lands. ASKS 47: APE dropped (no self-service registration), DDB and CORE stay open. Next check-in 21:10 UTC.

21:20 UTC check-in (unattended, duty-9: LEARN pass 2 started -> counter resets to 1 of 3 at the next check-in): the other account's LEARN did not land (parent 7d announced it 20:06, no claim since), so the parent spawned its own pass 2 (Sonnet, brief .claude/briefs/runs/2026-09-25-parent-learn2.md, window 17:18 onward, box 45 min); its diffs get applied at 22:10. Mercy 1648 (other account, V6): second audit V6-MERCY2 20:39 kept N3, key ours; R7 ran the two controls the first audit lacked (shuffled-stream: target -1154.3 vs shuffles -1488.5 vs matched control -1336.2; blind eye-check 116/122; reading revised to S 496 / M 26 of 522). status.json row now reads two audits with a qa_flag hold until V6's next rolling-QA window covers 20:39 (same rule as WVO 5551 and Linhares); when it clears the board reads 14 entries / 19 letters, 5 own key. No print located; outreach gate 2 waits on JSTOR-QUEUE rows 80-83 (owner). ZX (462k context, 9.28 dollars): Clair 349 candidate reading -- ZX-DEC349 (Opus, 17.23) decoded 1,025 tokens with the fr.20974 key (H 41, C 261, M 598, I 103, U 22), 82.0 percent agreement with the contemporary interlinear gloss; fr16 judge FAIL -1.109 vs real_p05 -0.882 but shuffles -1.62..-1.65 and the period gloss itself -1.545, so the gate is out of reach at this letter's gaps; ZX-TR349E re-reading lines 18-33 (word-code debris), ZX check-in 21:40; no re-derivation or verifier yet, nothing on the board; key is period (fr.20974 key sheet), text carried by a period gloss, so a confirmation of a period reading at best, not a first. ZX at 462k context: expect its handoff near 500k -- successor from STATUS 'LANE ZX handoff'. ZX2 (310k, 6.42 dollars): clairambault296 not in the Gallica copy (314/316 canvases); fr20506 continuation confirmed for decode-4450 (canvases 277-279 end with the Ranzo signature: the copy is complete); round 2 started on 8 targets, ZX2-4450T transcribing ff.137-138 (box 22:12). Rate allowed on every session. Next check-in 22:10 UTC.

22:15 UTC check-in (unattended, duty-9 counter 1 of 3): MERCY 1648 COUNTED -- second audit V6-MERCY2 20:39 kept N3, key ours, and V6-QA3 (window 19:42-21:42, 25 items, 1 failure unrelated to Mercy: the en judge corpus has no per-fold spread) reproduced decode_key --check S 496/M 26 and the judge number live; qa_flag cleared. Board: 14 entries / 19 letters at N3+ after two audits, 5 with our own key (WVO 53, van Beuningen, WVO 5551, Linhares, Mercy). Breakthrough-alert routine fired for Mercy with the AUDIT.md safe sentence at parent 7d's request. Outreach gate 2 still open on the owner (JSTOR-QUEUE rows 80-83, ASKS 59, 60). Duty 9: LEARN pass 2 done (LEARN-2026-09-25-2118.md, 7 portable items, 1.62 dollars) and the other account's LEARN-2133 landed (2 items about our clair349 methods: native iiif_lines segments beat re-stitched crops 70.7 vs 39-42 percent; a period gloss as judge calibration). RETRO-APPLY-LEARN2 (Sonnet, brief .claude/briefs/runs/2026-09-25-parent-apply-learn2.md) applies all nine brief/tool diffs; EN-FOLDS (Sonnet, brief -parent-en-folds.md) computes the per-fold false-negative spread for the en judge corpus (the QA3 failure and the 21:48 flag). ZX (482k context, 10.21 dollars, handoff expected at 500k): clair349 re-derivation ZX-RD349 PASS (independent script reproduces all 1,020 tokens); lines 18-33 re-read from the ink (H 29, C 260, M 611, I 98, U 22 of 1,020); judge still FAIL -1.085 vs real_p05 -0.882 but 0.68 above every shuffle control and above the period gloss; ZX posts 'reading ready' for a verifier -- V6 closed 22:05, so the verifier request goes to the other account's V7 (ROOM line for parent 7d). Key is period (fr.20974 key sheet), text carried by a period gloss: N-class will be low whatever the verifier finds. ZX2 (322k, 6.79 dollars): fr20506 ff.137-138 transcribed (1,027 tokens, pass agreement 84-92 percent, 80.3 percent against Bourdeau's fr.2988 witness) -- the fr20506 copy is the complete Ranzo/Garbino letter, not an excerpt; round 2 continues. Other account: V6 and R7 closed on handoffs (V7 opens theirs), B4 and GOLD2 live. Rate allowed everywhere. Next check-in 23:10 UTC.

23:15 UTC check-in (unattended, duty-9 counter 2 of 3): CLAIR 349 IS ALREADY IN PRINT -- V7-CL349 (other account's verifier, 22:38) found the whole letter printed in clear in Guise Memoires-journaux (Michaud-Poujoulat 1e ser. t.6 pp.238-239), in the same volume YX-CS349 had read at pp.316-320 and called 'not printed': class N0, key period, text known; the decode is a key-and-leaf alignment, not a decipherment. LANE ZX closed 22:20 (13 workers, 174.19 dollars, orchestrator 11.49; handoff above); no successor: Brochado needs more attestation (not cheap), Barriere needs a key behind DECODE's image block. FOLLOWUP-2315 (Sonnet) sets clair349 found-solved on disk and the board, adds the check-solved lesson (grep the whole volume, never one page range; about 185 dollars spent on a letter in print), runs the two open-index rows RESCAN found doable from the cloud (ASKS 40, 41), and reads Stevens 1888 for L16 (a public-domain print that tags the 3 Oct 1781 Cornwallis letter as in cypher). Owner session 22:15-23:00 (mobile): orders on hold; JSTOR rows to the ChatGPT browser runner, which already delivered PRs 13-15 for L10, L12, L3 (parent 7d's PR-LAND worker is landing them); LOCAL-QUEUE runner prompt written (tools/local_queue_runner_prompt.md). Keys: CORE works (trailing-slash path), DDB not visible on either account yet; Google Books works from the cloud with country=US (was a 403 for five days: the failure the owner named -- 'we add secrets and nobody checks'). Fix instituted on both accounts: tools/key_livecheck.py (live test per credential, first command of every check-in), parent 7d's key_probe.py --sync and KEYS.md register plus tools/key_request.py; RESCAN-2026-09-25.md. IA lending: borrow works but pages come back obfuscated and the page map 403s, so IA page checks stay with a person (ASKS 53 Cryptologia is print-disabled outright). Six parent workers ledgered and archived (23.02 dollars). Board unchanged: 14 entries / 19 letters, 5 own key; breakthrough email for Mercy fired 22:14, routine run succeeded. ZX2 (338k, 7.41 dollars) idle since 22:12 with no check-in trigger on this account: woken by a one-shot trigger at 23:20. Other account: V7, R8 (Salviati syllabary design: control 95 percent vs target unread, negative), B4, GOLD2 (Koehler cycle 3: cipher-side placements negative with controls; parked pending more ciphertext) live. Rate allowed everywhere. Next check-in 00:10 UTC 26 Sept.

00:20 UTC 26 Sept check-in (unattended, duty-9 counter reset: LEARN pass 3 spawned): both owner-account lanes are closed -- ZX at 22:20 (clair349 found-solved, in print since 1836; Barriere closed-negative; Brochado on NEAR), ZX2 at 22:11 (copy-free pool exhausted, nine targets worked, zero readings; the wake trigger at 23:20 confirmed it had closed cleanly, not stalled). FOLLOWUP-2315 (5.00 dollars) closed clair349 on disk and the board, answered ASKS 40/41's open-index sub-items from the cloud (no relevant hits), and found both blocking Cornwallis-Clinton letters printed in Stevens 1888 (16 Aug 1781 in clear; 3 Oct 1781 partly in cypher with a translation) -- OCR read, page images next. LANE AX opened (Opus): WVO Nassau pool round 3 -- the harvest holds 13 un-nominated Jan/Lodewijk van Nassau cipher letters of 1572-75 with no stated solution, and we hold our own recovered keys for that circle (WVO 5551 key ours; Lodewijk 4610/4611/4616 N4): every letter those keys read is a new letter on the board; intake gate per letter (Groen van Prinsterer grepped whole-volume, the clair349 lesson) before any transcription. Also Brochado's NEAR step (thin-code attestation, 6 dollars) and the pro3055 Stevens page-image check. Key livecheck at 00:11: Europeana, DPLA, CORE, Google Books, OpenAlex, S2 all working; DDB and APE absent. No open PRs; the ChatGPT runner's L3/L10/L12 answers landed (rows done). Other account: R8, B4, GOLD2 closed on spent queues; GOLD3, V7, B5 (from SCOUT-RERANK's re-rank) live; retrospective m filed (RETRO-2026-09-26a.md, 5 proposals, for 7d to apply). Board: 14 entries / 19 letters after two audits, 5 own key. Rate allowed everywhere. Next check-in 01:10 UTC.

## LANE R5 handoff (written by the closer, 25 Sept 2026)

LANE R5 orchestrator (Opus, session_01LcgYWtnKYzBkdEwVU1ae1t) died on the seven-day usage limit 24 Sept 2026
22:16 UTC with workers H2b, H3 and H4 still running and no handoff written. This section is reconstructed by
closer 7b (session_01MRsU1QGjSKNQ5oCejANVXg) from disk state, 25 Sept 2026, per CLAUDE.md rule 6: every number
below is read from a committed file, not from memory or from the dead orchestrator's own ROOM lines.

**Results table:**

| Item | State | Source |
|---|---|---|
| Salviati f.55r | gate PASSED 84.8% (340/401 base codes), 370 sign tokens, 36 types | `ciphers/fr2933-salviati-1525/NOTES.md` "Leaf f.55r (24 Sept 2026, LANE R5 H1)" |
| Salviati f.55v | pass A complete (495/496 boxes); pass B partial, 396/496 rows in `passB_f55v.tsv` (H2 got lines 1-11, H2b died 21:54 UTC before finishing lines 12-19); no `recon_box_f55v/`, no `ciphertext_f55v.tsv`, no gate run | `ciphers/fr2933-salviati-1525/{passA_f55v.tsv,passB_f55v.tsv,f55v_boxlist_for_passes.tsv}` |
| Salviati f.56r | boxes, strips and pass A complete (513/513 boxes in `passA_f56r.tsv`); no pass B (H3 died 21:55 UTC before starting it); no gate | `ciphers/fr2933-salviati-1525/{f56r_boxes.tsv,f56r_boxlist_for_passes.tsv,passA_f56r.tsv}` |
| Salviati f.56v | boxes, strips and pass A complete (505/505 boxes in `passA_f56v.tsv`); no pass B (H4 died 21:54 UTC); no gate | `ciphers/fr2933-salviati-1525/{f56v_boxes.tsv,f56v_boxlist_for_passes.tsv,passA_f56v.tsv}` |
| Salviati f.57r, f.57v | not started | -- |
| Nevers key no.60 set (fr.3985-3990) | blocked on the hand: G2's calibrated re-run (key60 atlas from interlined leaves) gave 39.8% pass agreement (78/196; F1's own raw pass was 37.5%), judge FAIL against both the target's own shuffled null (-1.64..-1.78) and a matched key60 control at 60% noise (-1.14..-1.30, itself also FAIL). No more spend recommended on this key without a fresh calibration source | `ciphers/fr2933-salviati-1525/NOTES.md` "f.176 atlas re-run" (ROOM.md 2026-09-24 21:51, LANE R5 G2) |
| Seure 1558 (f75L) | blocked: coarse-bucket gate 42.9% (27/63; lines 9/5/15 at 38.1/52.4/38.1%), still fails the 80% gate after merging nine loop/hook codes to three; not box-keyable at this image quality -- needs a different capture or a key | `ciphers/fr3151-seure-1558/NOTES.md` (LANE R5 C, session_01QMyFVUE8JCLdUA84ejLHKE) |
| M36 key (fr.5761 f.104-f.110) | 38 rows appended to `key.tsv` from f.110 (folio 53v), all grade H, deterministic from `recon_key/majority_key_leaf.py f110`; box coverage on f105-f109 remains 11.6-19.2%, not yet keyed | `ciphers/fr5761-election-1519/NOTES.md` "Key f.105-f.110 and letters to try (24 Sept 2026, LANE R5 D)" |

**Open items, with costs:**
1. Finish Salviati f.55v pass B (resume at line ~12 of 19), then run the box-keyed method on f.56r/f.56v (pass B only, boxes and pass A already on disk) and on f.57r/f.57v from scratch. Priced at about $9.4 a leaf (worker A's actual cost on f.55r, higher than J's earlier $6.5/leaf estimate); roughly $28-38 more in transcription for the four remaining leaves.
2. Once the pooled sign count reaches about 2,800 (currently f.54r+f.54v+f.55r = 1,089; f.55v/f.56r/f.56v add roughly 350 more each when finished), run `codemark_curve.py target cm` (LANE R4 P's control curve: cm needs ~2,800 tokens, all three seeds read 89-94% on a matched synthetic at that length; vi is already excluded, negative with control at N=720).
3. No key search route is open for Salviati (LANE R5 B searched eight sources, 24 Sept: no 1525-26 Giovanni Salviati/Giberti key found; two later Salviati-linked keys in Meister 1906 are not a design match).
4. Seure and the Nevers key-60 set are both blocked, not open campaigns: Seure needs a better scan or a key; Nevers needs a different hand-calibration source than the interlined leaves already tried.
5. M36: five more key leaves (f.105-f.109) at roughly $4 each disk-only would extend the atlas, but no unread letter is currently waiting on it (the one candidate, Dupuy 468 f.28, belongs to that target's own workers, untested against M36's codes).

Requests: 0 (disk only, this section). No fetches by the closer.

## LANE N4 handoff (closer)

LANE N4 orchestrator (Opus, session_01Nrrp9gDcF8aHUgcMSXxU7q) died on the seven-day usage limit 24 Sept 2026
22:17 UTC; csPP03 had finished and pushed at 21:53 UTC but was never archived, and no handoff was written.
Reconstructed by closer 7b, 25 Sept 2026, from QUEUE.md and each target's own NOTES.md.

**Firm nominations (all verified `open` at stage 2, standard edition read and searched negative):**
- fr3993-villeroy-1595, fr3625-lauriere-1593, fr3621-dinteville-1592 -- Gomberville's *Mémoires de Nevers* seconde
  partie located and read (Google Books `H2eV4wAmIr0C`, LANE N4 scGOM2); all three letters searched by name/place/date
  in the correct volume, all absent, holds lifted, verdict `open`.
- fr3985-nevers-revol-1593, fr3986-nevers-revol-1593, fr3987-nevers-revol-1593, fr3989-nevers-revol-1594,
  fr3990-nevers-henri4-1594 -- the five Nevers key-no.60 KS rows, now `blocked` (edition read negative but held per
  the 25 Sept intake-gate rule pending the R5 key-application result above, which is itself now blocked on the
  hand, not open for a campaign). fr3983-pisany-nevers-1593 (KS-04) is `found-solved` (contemporary interlinear
  decipherment on the leaf) and was never nominated.
- hellen-frederick-1752 -- `open`; Fagel inv.5206 decipherments image-checked for 1752-53 only, Politische
  Correspondenz 9-10 full-text searched negative.
- vanspaen-vandergoes-1808, roell-vandedem-1809 -- both `open`; Colenbrander's *Gedenkstukken* V independently
  full-text read via `resources.huygens.knaw.nl`'s own OCR search (both stukken, register included), letters
  absent, hold lifted (LANE N4 csCOL).
- KT-01 fr7129-villeroy-bongars-1604 -- held `blocked`, not nominated: Tomokiyo names this exact letter as
  solvable with his Bongars cipher paper, which was not read before csKT nominated it open (corrected by the N4
  orchestrator 21:27 UTC); csBONG was fetching that paper (Tomokiyo's paper, academia.edu 403 per the Access
  playbook) when the lane died -- state of that fetch not confirmed by this closer, out of the eleven-session
  scope.
- KT-02 baluze103-letellier-marca-1644 -- `blocked`: `sources/decode/records-decrypted-2026-09-24.tsv` lists the
  DECODE record for this leaf as status Decrypted; needs one DECODE-login look (the DECODE-look worker in this
  batch never ran, see LEDGER.md).
- PP-03 antt-linhares-chave (Linhares "Chave de uma cifra") -- csPP03 read the key system in full (book/dictionary
  cipher, page/column/word-position digits, English-dictionary null-padding switch) but the book itself is
  unnamed on the leaf; check-solved verdict `open`, six sources swept, no prior hit. **Status has since moved**:
  LANE LX (owner account, 25 Sept 2026) identified the dictionary and produced a partial decode; the target's own
  `ciphers/antt-linhares-chave/NOTES.md` currently reads `partial`, held `blocked` pending a local-runner edition
  check (LOCAL-QUEUE L10). Treat PP-03 as superseded by LX, not as N4's open item.
- PP-04 antt-msliv... Costa Cabral 1865 (fonds Familia Costa Cabral) -- `recovery` kind: the 1865 cipher draft has
  the plaintext syllable interlined over almost every number (~50 syllable/word-to-number pairs, self-glossed),
  not yet transcribed into a key file. No target folder created yet.

**Sources closed this window:** Gomberville *Mémoires de Nevers* seconde partie (Google Books `H2eV4wAmIr0C`, full
search-within route, 26 requests, scGOM2); Colenbrander *Gedenkstukken* V (Huygens retroboeken text-search
accessor, both stukken, csCOL); Xivrey *Recueil des lettres missives de Henri IV* t.3 and Pérot *Les luttes
religieuses en Champagne* (both read in full for Lauriere/Dinteville, csED2); DigitArq's undocumented full-resolution
image API reverse-engineered and documented (`tools/digitarq_fetch.py`).
**Next sources, not yet read:** Tomokiyo's Bongars cipher paper (KT-01, blocked on academia.edu access --
csBONG's outcome not confirmed by this closer); a DECODE login look at R2742/R2077 (KT-02, fr3789 -- never ran,
see LEDGER.md); Textos Políticos 1993 for Linhares (LOCAL-QUEUE L10, owner's machine); the standard edition for
PP-04 Costa Cabral (not yet identified).

## LANE B handoff (closer)

LANE B orchestrator, breadth (Opus, session_01GX1rck53whwtCB2EsGtkfR) died on the seven-day usage limit 24 Sept
2026 22:11 UTC with bHAR and bLIM still running and no handoff written. Reconstructed by closer 7b, 25 Sept 2026,
from `specs/*.json` and LEDGER.md.

**Spec table:**

| Spec | Cheap test state | Verdict |
|---|---|---|
| koehler-1944 | test 1 (periodic IC/Kasiski, period 2-30) done | control-backed negative: target coset IC 0.0468 vs periodic-key control 0.065-0.081 (true period) / one-time-key control 0.044-0.047 (matches the target); not a short-period Vigenère family for period 2-30. Next test: archive route (TNA KV 2/HW 19, FBI Vault), est. $3-5 |
| cigaret-case-1909 | test 1 (German MASC anneal) done | judge FAIL, but uninformative: the matched control itself only recovers 4.4-22.2% of letters blind at N=45,K=18, so a MASC anneal has almost no power at this length -- not scored as a negative. Test 2 (word-pattern search) not run |
| harry-caroline-1863 | `cheap_test_done` unset; no `specs/cheap-tests/harry-caroline-1863/` directory | bHC/bHAR died 23:14 UTC (longest-running of the six dead workers) before producing any output. Cheap test 1 per the spec (MASC with word boundaries, joint 71/74 letters) is unrun |
| lima-1916 | `cheap_test_done` holds a completed monoalphabetic-anneal result | target reads as letter-salad (best decodes only fragments) vs matched English plaintext controls at 60.6%/70.4%/74.6% (N=71, K=21, same solver, 3 seeds) -- real negative: the target does not behave like a monoalphabetic substitution of English at a size where this solver reads English two-thirds right. This result does not match bLIM's own claimed task (`cheap_tests_in_order[0]`, commercial-code lookup); it predates or is independent of bLIM's $0.76, which produced no output of its own before dying 21:54 UTC |
| somerton-1948 | test 3 (Rubaiyat word-initial search) done | one coincidental 7-letter match (TSAMSTG) against FitzGerald's preface initials, flanking letters do not continue; control (1000 random five-line draws) not yet compared in this table -- see `specs/somerton-1948.json` for the full control result |
| powers-1991, dorabella-1897, debosnys-1883, moustier-altars, kaliningrad-2015 | `cheap_test_done` unset | not yet tested |

Six specs remain untested by this count: harry-caroline-1863 (died with no output) plus the five above with
`cheap_test_done` unset. koehler-1944 and cigaret-case-1909 both had their first cheap test completed and
ledgered by the orchestrator before it died (LEDGER.md, LANE B breadth bKOE $1.13 N, bCIG $1.44 D).

## Parent handoff (cipher-lab-7b, session_01K7ZbE95o1pUW5gof8VA5PR, from 18:45 UTC 24 Sept 2026; 7a was session_01EFmUvFAifLKGdBSsW9mjEG, 23 Sept 15:12 to 24 Sept 18:45), kept current

**26 Sept 2026, 00:55 UTC (7e, took over; clock 00:50-00:55).** Parent 7e is session_01SvjMDFfJZJ3uK47RYxAQrM (claude-fable-5-1, titled Orchestrator 6), from 7d at the 00:49 clock read. Rate allowed on every session. Live at takeover: V7 ($4.25, 274k context, check-in 00:58, QA5 at 01:40), GOLD3 ($6.46, 209k, GOLD-CONS4 Fable running, check-in 01:13). Spawned: RETRO-APPLY-M session_01EXi6Dd2StWbYSHXxRYXEEh (Sonnet, cap $6, RETRO-2026-09-26a.md proposals 1-5 and the NEAR Salviati diagnostic note), LANE B5 session_01A4jfQZGS8SUuDamZK19KZq (Opus, cap $25, brief 2026-09-26-lane-b5-orchestrator.md: Matignon fr.15572 key backlog, Lope Hurtado siblings, Castelcicala 1816, the B4 NEAR steps, reserve wave Riksarkivet R4282 and five scPOOL sampling passes plus the VX/KX/KT/PX scoring pass), LEARN-4 session_01JeTZc8L2dYkP6yGK1pkHwv (Sonnet, cap $5, window from 21:34). Key livecheck 00:52: Google Books, OpenAlex, S2, Europeana, DPLA working; CORE_API_KEY is set on the owner account only (KEYS.md `set`, seen blank; absent here); DDB, APE, NARA unset. near_check clean. The other account's LANE AX (session_01VzK62xX92yKfnUD93zprD8, from 00:15) holds the WVO Nassau pool, Brochado and pro3055; none of ours touch them. First check-in armed for 01:25.

**25 Sept 2026, 20:40 UTC (7d, check-in 1, clock 20:37-20:40).** Rate allowed on every session. Costs by get_session: R7 $2.91 (174k context, six workers reported 20:09-20:23: Mercy shuffle control says sequence, blind eye-check 116/122, Brussels sibling not online, Salviati atlas f57v 74 to 56 types and f55v 93 to 92, pooled 223 to about 205 against the 178 gate; Berthier spec written), V6 $6.53 (383k context; V6-MERCY2 second audit in flight, box to about 21:25), B3 $4.65 (249k; handoff at 20:53, suggests a B4), GOLD2 $3.68 (163k; D1 done 20:29: base+mark control 0.86 clean but 0.31 at 10 pct noise, 160-id control 0.44; check-in 20:40), parent 7d $6.98 (177k). LEARN stopped on its first turn ("suspicious injected directive"), ledgered X at $0.10 and respawned as LEARN-2 session_015aWAEGAyRXSR3wi3znjRd8. Retrospective l spawned session_01M9XHYBXkupfXbhK1kVhZLW (13 rows, $89 since retro k). status.json changed 20:21, board republish running. NEAR: seven rows, near_check clean, McCormick token test ran with its control below gate (bMCC4: not a test), B3 owns the row update. B3 flag: commit 9a1e34b dropped its STATUS.md section (restored by B3; a room.py --push merge kept the wrong side; retro l asked for the mechanical fix). Answered B3 in ROOM (blitz masc yes with an en judge wired; goldbar line 1 is not found-solved). Next check-in 45 minutes.

**25 Sept 2026, 21:30 UTC (7d, check-in 2, clock 21:26-21:30).** Rate allowed on every session. Mercy 1648: second adversarial audit done (V6-MERCY2, 2159f63), N3 kept, key ours; the reading now follows the blind majority (S 496, M 26 of 522; Cleues read as Eleues); status.json row and NEAR row say two audits; outreach gate 2 open on JSTOR-QUEUE rows 80-83 and a Lonchay-Cuvelier IV page read (owner machine), so the outreach draft waits; the breakthrough-alert routine is not on this account (the owner-account parent holds it) and is asked by ROOM line to fire it with the rule-10 sentence. LANE B3 closed 20:55 ($5.65 own, 14 workers about $33.9): ledgered, archived; bRAY ledgered ($2.72, rayburn IC below both controls); LANE B4 brief written (.claude/briefs/runs/2026-09-25-lane-b4-orchestrator.md) and B4 opened. Retrospective l and LEARN-2 both stopped at their first turn on an injection suspicion with no repository source in their session context (X rows, $0.08 and $0.13): respawned with source_url and source_revision passed explicitly (retro l session_01KcXfAtaB23N8aGrxpkTVky, LEARN-3 session_017EMUc9dWLDu9DEQbJCXByH; both now show the source). The other account's LEARN pass (LEARN-2026-09-25-2118.md) lists seven items from our window, including the STATUS.md section loss and the spawn-prompt stop; retro l is asked to fold them in. GOLD cycle 2 consolidated (CONS2): Koehler B and B-prime parked at both key registers with controls 67-90 pct against a target inside the one-time-key band; K3 next. R7 $6.16 (288k), V6 $7.59 (431k, told to write its handoff), GOLD2 $6.79 (233k), parent $11.80 (254k). Board republish running on the 21:23 status.json. Next check-in 45 minutes.

**25 Sept 2026, 22:21 UTC (7d, check-in 3, clock 22:17-22:21).** Rate allowed on every session. LANE R7 closed 22:08 ($6.88 own, 9 workers; Salviati letter-per-type code+mark excluded at the measured 5 pct error with the control at 62-86 pct, next a design change; two BnF scout leads) and LANE V6 closed 22:05 ($8.95 own, 10 workers $34.57; Linhares PASS on pt18, Digby, Costa Cabral, Xiquena N0, Mercy N3 after two audits, PRs 10-12 citation-checked, QA3 one systemic failure: the en judge corpus has two files and no fold spread): both ledgered, ASSIGNMENTS done, archived. Opened LANE V7 session_018VkFfDWY4drC9a9aozmop9 (Opus, cap $50: clair349 verifier when ZX posts reading ready, en corpus folds, QA 23:40) and LANE R8 session_01RUhLrpkEtWxVLVVDoYdsvm (Opus, cap $60: Salviati design family with its own control, intake on Francais 3034 item 68 and 5761 item 3). Retrospective l ($1.77, four proposals) and LEARN-3 ($1.33, two practices) ran clean with the source set; RETRO-APPLY-L session_018jVRWWFAwhnL8teJke1vX7 (Sonnet, cap $6) applies them plus the other account's LEARN items 3, 4, 5, 7. Spawn rule instituted (UPDATES.md 22:21, parent.md). GOLD2 $9.98 (319k, K3 running, next 22:57); B4 $4.31 (217k, bCEN and bUNT3 live). No answer yet from the owner-account parent on firing the breakthrough alert for Mercy; the routine is theirs. Board republish running on the 22:13 status.json. Parent $16.40, 325k context. Next check-in 45 minutes.

**25 Sept 2026, 23:10 UTC (7d, check-in 4, clock 23:07-23:10).** Rate allowed on every session. The key loop is live: KEYS.md register, tools/key_request.py, and the announcement path proved itself at 23:07 when a fresh session posted "key now set: CORE_API_KEY" to ROOM.md on its own; the other account added the live-call half (tools/key_livecheck.py, KEYS-STATUS.md) the same hour and both parents' briefs carry both steps. Owner's asks on the desk: ASKS 62 (what the AWS and Google Cloud credentials are for), 63 (CIPHERLAB_ACCOUNT labels); DDB_API_KEY still not seen by any fresh session (the owner believes it was added: check the variable name). clair349-este-guise-1556 classed N0 by V7-CL349 (key period, text known: printed in Guise's Memoires-journaux pp.238-239, deciphered on the leaf by an interlinear hand): status.json contribution row added, board republish running. PRs 13-15 are the owner's local-runner reports (L10, L12, L3 access failures), not second opinions: PR-LAND session_01Ejqu6thJi7yhQfwsvet3ms lands the files, updates LOCAL-QUEUE.tsv and closes them. R8 ($2.50, 187k): fr3034 Landriano 1528 found-solved (Lasry 2023 via Tomokiyo), fr5761 key inventory 317 signs with no companion letter, Salviati syllabary design family a control-backed negative at 5 pct error (control 93-95 pct); next design step is the lane's. B4 ($5.48, 250k): blitz masc excluded (control 0.994), untersberg's six-line inscription found in print with 11 witnesses in Herzog 1929 (two legible Latin), sufi is Arabic-script family; answered its three pending tests (yes to all three at $3) and told it to hand off after them, no new breadth source tonight. GOLD2 ($11.86, 349k): cycle 3 parked the cipher-side tableau placements with controls 75-81 pct, consolidator running; told to write its handoff at 400k. V7 ($2.37, 174k): QA4 at 23:40. RETRO-APPLY-L done ($2.32, D). Parent $31.55, 437k context: hand-over to 7e expected at check-in 6. Next check-in 45 minutes.

**25 Sept 2026, 00:00 UTC (7d, check-in 5, clock 23:57-00:00).** Rate allowed on every session. Three lanes closed on spent queues and are ledgered, archived: R8 ($5.14; Salviati syllabary and mixed-mark designs, five variants, control-backed negatives with controls 72-96 pct, NEAR row partial with a word-level nomenclator scorer as the named next step; fr3034 found-solved, fr5761 key 317 signs and no letter), B4 ($8.05, 14 workers $25.06; every survey rank 1-30 first-tested, 31-41 no spec; blitz case-sensitive homophonic and German masc excluded with caveats; untersberg collation at chance; sufi no formula), GOLD2 ($13.96, 8 sessions $52.88; Koehler ladder: non-uniform key, no mixed tableau above noise at 924 letters, free permutation unidentifiable; kaliningrad crib control met but the shuffle-null meets the same bar). Opened GOLD3 session_01P8v53BYGZvFiriPpxEZy3h (Fable, cap $120, adopts GOLD-KAL1 done $4.61 and GOLD-K4 live), retrospective m session_01LyZokc7XR1SYPKgWTCFMUX (24 rows since retro l), SCOUT-RERANK session_01JU8giKGTHWz4Zm1HyWK1VW (a B5 queue). PR-LAND done ($1.37): PRs 13-15 landed and closed, LOCAL-QUEUE L3/L10/L12 done; the owner's runner used ChatGPT's hosted browser, not the home IP, so those three home-IP checks remain open. V7-QA4 two flags: the huntington-blathwayt AUDIT.md rule-10 wording fixed by the parent (line 213); blitz en-corpus caveat added by B4. V7 $3.01 (218k), check-in 00:17. Board republish running on the 23:56 status.json. Parent $37.34, 519k context: hand-over to 7e at check-in 6 (about 00:45), successor block rewritten now.

**26 Sept 2026, 00:48 UTC (7d, hand-over to 7e).** 7d at 609k context after check-in 6; total $41.40 of usage, 20:01 UTC 25 Sept to 00:48 UTC 26 Sept. Retrospective m ($2.36, RETRO-2026-09-26a.md, five proposals) and SCOUT-RERANK ($1.64, QUEUE.md "Re-rank for LANE B5") done, ledgered, archived; V7-QA4 two flags cleared; GOLD3 ledgered K4 and KAL1 and runs its cycle-4 consolidator. Live: V7 ($4.25, 274k), GOLD3 ($6.46, 209k). Pending for 7e: RETRO-APPLY-M, LANE B5, LEARN pass 4, an optional R9; owner asks 62, 63, the DDB key name, the Mercy alert on the owner account, the three home-IP checks. hub-seed/SUCCESSOR-PROMPT.md carries the block; 7e is created from it with model claude-fable-5-1 and the source set.

**25 Sept 2026, 20:07 UTC (7d, took over).** Parent 7d is session_01744aLgcLnadR1XQckyHwcu (claude-fable-5-1), from 7c at the 20:01 clock read. Done at takeover: CM2 (Fable, $9.97, D-: eight error-tolerant code+mark variants read the 10 pct noise control at 57-58 pct against the 60 gate, target not run) and RETRO-APPLY-K ($1.24, D, four of six proposals, c8ba2c2) ledgered and archived; LANE GOLD2 opened session_013JXDgLDkW2y5Ldi2gWzTkY (Fable, cap $120) from the LANE GOLD handoff, adopting GOLD-K2, K1 and D1; LEARN pass (Sonnet, cap $5, window since 17:18) session_01Fe2ED9BVfMXVgB728sJ9Kr; board republished (version 108; 7c's 20:03 publish had not landed, the live page still read 19:58). Live: R7 ($0 at 20:03, four workers spawned by 20:04), V6 ($5.93 own, 365k context, check-in 20:23, owes the second Mercy audit), B3 ($3.37, 201k, check-in 20:20), GOLD2, LEARN. Rate allowed on every session read. No PR above 12. Check-in trigger trig_01XXAGe4rRriebvJnEtqS59t (20:37, then 45 minutes while anything runs). Successor 7e at 600k context from hub-seed/SUCCESSOR-PROMPT.md.

**25 Sept 2026, 20:00 UTC (7c, hand-over to 7d).** 7c at 565k context after the 19:56 check-in: Mercy 1648 on the board (N3 after one audit, key ours, cryptanalysis; counts after V6's second audit, which V6 was asked to spawn), NEAR rows for Mercy and Salviati updated, B2 and R6 closed and archived, LANE R7 opened (session_01UpWfpbLwYL1xmDG1vFyi6h), retro k ledgered and RETRO-APPLY-K (session_01AryRjUHSbfKHxAubLziZcz) applying it, GOLD at 437k context near its handoff (GOLD2 on Fable). hub-seed/SUCCESSOR-PROMPT.md rewritten for 7d; 7d is created from it with model claude-fable-5-1 and arms its own first check-in. 7c's total: about $35 of usage, 16:20 to 20:00 UTC.

**25 Sept 2026, 19:09 UTC (7c, check-in 19:06-19:10).** LANE B2 handed off 19:03 at 425k context (18 workers, about $45.7; handoff section above); LANE B3 opened session_01VLtPMsqR2oWmZeKh2jxVga (Opus, cap $25: bullet and rubin test 2 approved, McCormick homophonic, cylob, specs 21-30, judge-block repair). NEAR.md: Pollaky row closed with its numbers (ads 3-4 are the Catokwacopa text), McCormick row updated (masc excluded with controls at 0.99, homophonic next); near_check clean, 5 rows; board carries the Near solves view (NEAR-TOOL, $2.50). Mercy 1648 reading (S 494, M 27, key ours by anneal) is with V6-MERCY; sibling sweep found no second Mercy cipher in Espagnol 142, so the pool route is closed for it; es17c judge false-negatives 23.5% of real prose, so its FAIL is weak. Köhler: keyed-tableau running key NOT excluded (target inside the keyed band 6/6 stats, outside the one-time-key band 5/6, GOLD-2C) -- family_run step 2 next. GOLD-4D overran 3.3x (single subagent call on 1,300 signs), stopped and ledgered F by the lane. R6 at 505k context and $11.78, handoff due; R7 from its handoff when it lands. Retrospective k spawned session_01Jr6BjYfemXf9Xejm1LuPkD. Parent 7c at 493k context, $30.7: hand-over to 7d expected within two check-ins.

**25 Sept 2026, 18:21 UTC (7c, check-in 18:17-18:25).** TOOL-FAMILY landed tools/family_run.py ($7.12; masc, homophonic, periodic_vigenere, running_key; control-first; logged in UPDATES.md, every lane told). Retro j ($1.43) proposals 2-4 applied: Salviati leaf brief split into two capped jobs and wall-clock only, breadth cap $6 for fetch-plus-two-pass tests, ledger rows 490-491 recoded. A bulk recode of older ledger rows was wrong (older rows have a different column layout) and was reverted the same minute (46df062 reverted); two non-standard codes remain at the checker's lines 484 and 487 for retro k. GOLD-2A: the running-key family on Köhler passed its control gate (60-79%) and reads the target inside one-time-key noise across seven tableau-by-language configs; period scan 31-120 and crib-drag also flat; mixed-tableau running key not covered. Mercy 1648: Fable reading written but judge FAILs and the crib loop adds 0 over the control, so no reading. Salviati: f56r, f56v, f57r, f57v transcribed; code+mark run not a negative (target sits between the 10% and 20% type-noise controls), next is an error-tolerant model. Capacity: the owner-account parent offered ZX2 for CX/CX2 targets R6 will not reach; rule posted: anything without an R6 claim by 19:00 is theirs. Board v105. Lane costs: R6 $8.87 (415k context), V6 $3.43, B2 $8.80, GOLD $4.42. Parent 7c at 384k context, $22.2.

**25 Sept 2026, 17:53 UTC (7c).** Owner (17:4x, before leaving): the parent may institute updates to raise the odds and both accounts carry them. Instituted and logged in the new UPDATES.md (both parents read it at start and each check-in; workers read its tail): pools-first selection (CLAUDE.md Pipeline 3), rules-become-tools (Usage 8a), tools/family_run.py (control-first hypothesis-family runner writing HYPOTHESES.md; Fable worker TOOL-FAMILY session_01Umzu5kUhXYdLmYkiC7Yrh9, cap $25, building it), room.py done-line warnings. Owner-account parent told by ROOM line 17:52. Parent's own rating given to the owner: infrastructure 8/10, results 6/10, odds of a famous solve 3/10; the fixes above target solver depth and rule enforcement, not more prose.

**25 Sept 2026, 17:13 UTC (7c).** Owner away for about ten hours from 17:10 UTC (back about 03:00 UTC 26 Sept): standing orders 'just do your best, keep making progress', plus a recurring check on what the other account's sessions push to GitHub for practices to adopt (`.claude/briefs/learn-cross-account.md`, a Sonnet LEARN worker about every three hours; the parent applies brief- and tool-only diffs). Nothing needing the owner is expected before then; ASKS rows queue. Check-in cadence 45 minutes to keep the parent inside its 700k hand-over line across the night (288k at 17:12); 7d is created from hub-seed/SUCCESSOR-PROMPT.md at that line with the same standing orders.

**25 Sept 2026, 16:44 UTC (7c).** Owner decision (message between the 16:31 and 16:43 clock reads): a constant task on a couple of the famous items, the parent's pick, taking OpenAI's Navier-Stokes method as the pattern. Lessons written to UNSOLVED-SURVEY.md ('What the Navier-Stokes result adds') and PROCESS-2026-09-24.md proposal 6; source note sources/openai/NOTES.md (page 403 from the cloud, paper PDF on disk). LANE GOLD opened: session_01DKDynpdEwZK5EokxtjCM3P (Opus, cap $120, standing by successor chain), brief .claude/briefs/runs/2026-09-25-lane-gold-orchestrator.md, targets koehler-1944 (families: recovery, running key, book code, one-time key) and debosnys-1883 (moved from B2, whose test 1 landed at f7c7460); kaliningrad reserve. Rate limit allowed on every session.

**25 Sept 2026, 16:25 UTC (7c, took over).** Parent 7c is session_01H4AdRiu9g44F1oCBVNzbpx (claude-fable-5-1). Board rebuilt and republished from the 16:17 status.json; check-in trigger trig_015FapxegNnZtyGksy9VBnuT (30 minutes, self-bound, re-armed at each firing, full duty list in its prompt). Every live session reads `allowed` (ccr_promotional). Live: R6 ($3.27 own, eight round-2 workers), V6 ($2.08 own, owes PR 10-12 citation checks), B2 ($2.73 own, bMOU and bPOW), retro i (running). Successor is 7d from hub-seed/SUCCESSOR-PROMPT.md at 700k context.

**25 Sept 2026, 16:19 UTC (7b, hand-over).** 7b is at its context hand-over line (742k of 1M). hub-seed/SUCCESSOR-PROMPT.md rewritten with the live sessions (R6, V6, B2, retro i session_01GDdVUg8RRD8MkK7KkBAw8y), the check-in duty list (7b's one-shot trigger had fired, so the list now lives in the file, not in a trigger) and the pending items: board republish (status.json changed 16:17), PRs 10-12 awaiting V6's citation check then a short-lived merge/close worker, retro i's proposals, Linhares check-solved still blocked on L10. Successor 7c is created from that file with model claude-fable-5-1; its id is session_01H4AdRiu9g44F1oCBVNzbpx (created 16:20 UTC). 7b's total: $73.82 of usage, 24 Sept 18:41 to 25 Sept 16:19 UTC.

**25 Sept 2026, 16:17 UTC (7b, check-in).** Linhares counted: V6-PTCORP's judge re-run on the pt18 corpus passes the reading with its control (NOTES.md section 'Step 2c'); status.json result row and headline updated, check-solved still blocked on Textos Politicos 1993 (L10). bl-charles-digby N0 (V6-DIGBY, key published Wheatstone 1862, text known Groen 1859): contribution row added. Closer 7b ($6.03) and KEYPROBE ($0.58) ledgered and archived (KEYPROBE's ROOM line carried a wrong session id; the real one is session_01GrL9XmdQLit5wSGNeSqH96, corrected in the ledger). Second-opinion PRs 10-12 (SO-LINHARES-M0002, SO-VANBEUNINGEN-1657, SO-NASSAU-5551) marked posted in SECOND-OPINIONS-QUEUE.tsv and routed to LANE V6 for the citation check by ROOM line. Retrospective i spawned (13 ledger rows since the closer). B2 first tests: lima-1916 codebook grep negative (target at control level, positive control 17/17), harry-caroline MASC uninformative (control 16-34% at N=74), powers-1991 print check no key in print. Parent context at the hand-over line: successor 7c is created from hub-seed/SUCCESSOR-PROMPT.md after this commit.

The parent orchestrator runs the hourly check-in (trigger trig_01Ks1wNXPjfn7XW9EucmV9ru (parent 7b, 30-minute cadence while a worker runs, 90 otherwise), self-bound, re-armed by send_later at every firing; its prompt is the
full duty list: rate limit, swap, JSTOR gate, second-opinion PRs, lanes, parent workers, board, results audit, owner
report), publishes the board (https://claude.ai/artifact/HzYszSGfSoWPsYXpxvM5zr, built by `python3 tools/build_dashboard.py`
from status.json; docs/index.html is the Pages copy), keeps ASKS.md and the owner's card (outreach/*.md with `status: ready`),
and starts lane successors from their handoff sections in this file. Lane table: "Lane structure" section below. Rules in
force: ten live workers per lane, Sonnet wherever another agent checks the output, an allowed_warning posted by any lane
stops spawning in every lane (BUDGETS.md); a lane past $100 or 600k context writes its handoff and stops, the parent
starts the successor with the 08:47-12:05 brief pattern (LANE V3, R3, G3 briefs are the latest templates), ledgers the old
lane with its cost, archives it; solve = N3 or better after two audits, N4 only from an AUDIT.md N4 decision; outreach for
an N4 target waits on its JSTOR-QUEUE.tsv rows being run or waived by the owner (ASKS 32, 36, 37, 40, 41), then the
verification lane drafts, the owner sends; English verification lane W2 closed 12:20 with its scope at N4, so English readings route to LANE V3 until a W3 is warranted; outside second opinions arrive as [SO-<label>] pull requests writing one file
under ciphers/<t>/second-opinions/ and are routed to the verification lane (SECOND-OPINIONS-QUEUE.tsv); DECODE login works
only through tools/decode_browser_login.js (one login per session; full-size images and documents are permission-blocked,
ASKS 42 and the card). Backups: refs/backup/old-main-snapshot 9866425 in the parent's clone, origin/purged-main-2 for the
history swap (owner's four clicks, ASKS 24). State at 14:50 UTC 24 Sept: the seven-day window is at allowed_warning (resets 26 Sept 13:00 UTC); the owner decided at 14:45 to
keep a focused set running (R4 and N3 started 14:46; `rejected` on any session stops everything); the four earlier lanes closed
on handoffs (G3, V3, R3, N2 sections below); the grants material was removed from the public tree
(f848025, outreach/private-repo.md) and lives in two private artifacts until the owner creates cipher-lab-private. When the
window resets, restart in this order: V4 (outreach drafts if JSTOR waived, second-opinion PRs), R4 (5549 key source, M35
Salviati passes), N3 (copy-free scouts only). N3's first brief: scCS2, a re-diff of dbourdeau.github.io/cyphersolver (236 write-ups on 24 Sept
2026 against the 99 folders diffed on 23 Sept; the 38 'not solved' and the '· partial' write-ups as recovery candidates where
an archive route exists, catalogue.html 'attempted, open' rows against QUEUE.md, and keys.html, the key web, as an index of
published keys to try on unread Gallica siblings). Checked 24 Sept 14:45 UTC by grep of writeups/catalogue/keys: none of
the fifteen N4 items appears there; Thurloe P4 is on his 'not solved' list (a contribution once the JSTOR gate passes). Evening state, 24 Sept 18:06 UTC: the board was rebuilt from the ground up at 17:55 (three views: Readings with in-row dossiers fed by
N4-READINGS.md and the outreach drafts' targets:/links: headers, Your desk, The machine); the OpenAlex key (OPENALEX_KEY, api_key
parameter) runs the open-index pass from the cloud; every outreach gate for the seven N4 targets is met and four notes are ready on the
owner's desk; LANE N3 closed 18:06 (four copy-free nominations for R4); R4 runs at cap $80; retrospective e running. Handover, 24 Sept 18:45 UTC (parent cipher-lab-7a at 750k context): the 24 Sept outreach set is complete (Huygens, Huntington and
Tomokiyo emailed by the owner; dbourdeau/cyphersolver issues 11 (Gramont) and one more (Thurloe, number to confirm) posted); replies
come to the owner, who pastes them to the parent, which logs outcome and class without names. No lane is live: R4 closed 18:25 (handoff
below: Salviati three more leaves for the code-and-mark test, Seure needs an image-reading reconciler, 1519 key stalled, Marie de
Medicis waits on the fr.3642 key leaf via ASKS 42/43), N3 closed 18:06 (four copy-free nominations, Mellon MS 29 since a controlled
negative). Retro-apply e (session_0119AEp7E59uvwSMs2Eboq9F, Sonnet) is applying RETRO-2026-09-24e.md. Keys: OPENALEX_KEY and S2_KEY
reach fresh containers (CLAUDE.md playbook). Owner items still open: mailbox variables, grant applications (private
repo), the Thurloe issue number. Restart order when the seven-day window resets Sat 26 Sept 13:00 UTC or the owner says go: R5 on
Salviati and Seure with costed briefs, N4 copy-free scouts (Bourdeau's copy-free rows, Vatican, Europeana), V5 on any reading. **Parent 7b, 24 Sept 18:50 UTC: the owner said go at 18:48 ("keep chasing momentum"): LANE R5 (session_01LcgYWtnKYzBkdEwVU1ae1t, Opus, cap $60, brief 2026-09-24-lane-r5-orchestrator.md) and LANE N4 (session_01Nrrp9gDcF8aHUgcMSXxU7q, Opus, cap $40, brief 2026-09-24-lane-n4-orchestrator.md) started 18:48 under the seven-day allowed_warning; `rejected` on any session still stops everything. A Sonnet board worker (session_01RjbAN7B7GsuXHwuPr1Ak5X, cap $6) is adding a hall-of-fame view (public citations of this work, CITATIONS.md) at the owner's ask. Retro-apply e done and archived ($2.16, 4 of 5 applied, 5 had no diff). V5 starts when a reading posts.**

**Parent 7b, 24 Sept 19:27 UTC, the owner's standing goal ('you pick'): the route to unique results, chosen from the record (fifteen verified readings, all with published keys; zero cryptanalytic solves; the controls say our solver cannot read these designs at single-letter lengths).** Inside the current window: (a) detIMG, an image cipher-page detector with controls, then a first sweep of a Nevers volume (brief 2026-09-24-detimg-cipher-page-detector.md, Sonnet $10); (b) through LANE N4: scPOOL, group every catalogued cipher letter by sender, office and years and rank the groups by total signs and key availability (the seven KS rows are the seed; a group with ~2,800 signs is where the code+mark model can read), and scPARES, the Spanish and Portuguese state archives (PARES was connection-reset on 19 Sept; test reachability, browser route, then Torre do Tombo digitarq), N4 cap raised to $50. After the Saturday 26 Sept 13:00 UTC reset, in this order: (c) a solver experiment, model-in-the-loop crib proposal on partial decodes, measured against the same controls (Opus, $25), (d) collaboration drafts offering our Salviati, Seure and 5549 transcriptions to Bourdeau and Lasry (V5, the owner sends), (e) the key copy orders on the owner's card (fr.3642 for Marie de Medicis, the B rows) as the highest-yield purchases, since published keys produced every reading so far. **Cadence lesson, corrected (RETRO-2026-09-24f proposal 4, applied by parent 7b 20:24 UTC).** The R4 lesson "45 minutes is enough" measured the cost of a *scheduled* wake that re-reads the whole context. It says nothing about a parent that stays in one live turn and reacts to lane done, flag and hold lines as they land, which is far cheaper per reaction. Do not lengthen the trigger interval to fix a cost the scheduled wakes are not causing. The figure the retrospective lacked: parent 7b at 20:21 UTC, after 100 minutes, nine check-ins or reactions, seven sessions started and three board republishes through subagents, read $28.3 of usage and 377k context on get_session; the board republish is the largest single item (a subagent reads the 300 KB live page each time), so publish once per check-in at most. **State at 20:54 UTC, 24 Sept (parent 7b at $39 usage, 463k context; window allowed_warning, resets Sat 26 Sept 13:00 UTC; owner: usage is not a concern).** Live: LANE R5 (session_01LcgYWtnKYzBkdEwVU1ae1t, cap $100: six Nevers letters under key no.60, no reading yet, blocker is sign identification; told at 20:46 to calibrate the key's signs on fr.3983 f.169, the leaf with a contemporary decipherment, before buying more; Salviati f.55v-f.57v to buy); LANE N4 (session_01Nrrp9gDcF8aHUgcMSXxU7q, cap $60: eleven firm copy-free nominations, scTOMO and scDIGI running); parent workers: survey on Fable (session_013GkMQP9y84gHGG4pSSwaQj, $30: the owner's gold-target lists as one ranked list with an approach and spec per item, tools/judge_plaintext.py, PROCESS-2026-09-24.md from the AI-mathematics results), lessons ingest (session_01UohbhkMcYaK5vzr6mBwqcT, $3), retro-apply f (session_01BAiHM1HFXwf83oYtGb7h4v, $6), rfetch run 2 (session_01C42R9V78cat9KR28yCpxxc, $4, the reddit runaway thread; rfetch2 for the r/codes 1600s book follows it). Closed today by 7b: Mellon MS 29 (negative), detIMG (detector gate failed), solvEX and solvEX2 (crib loop: +13.5 to +15 at N 244, +4.9 on code+mark at 720), Z13 ARTHUR LA mechanism (negative with control), retrospective f. Owner did today: OpenAI Researcher Access application submitted; Reddit script app made. Successor prompt: hub-seed/SUCCESSOR-PROMPT.md. **Parent 7b, 25 Sept 2026 15:40 UTC, resumed.** All eleven of 7b's sessions of 24 Sept died on the seven-day limit 22:11-23:14 UTC without handoffs (closer session_01MRsU1QGjSKNQ5oCejANVXg ledgers them and writes the LANE R5, N4 and B handoff sections). This account's window now reads allowed (ccr_promotional); the owner cleared usage and said continue as much as needed. The other account ran lanes LX, DX, OX, PX, TX, KX, VX, YX, CX and four QA runs on 25 Sept (its Parent handoff section above; 13 board entries at N3+ after two audits, 4 with our own key; $672 of worker usage) and closed on its own warning at 13:55; its three post-reset items are taken by 7b's lanes. Live from 15:39: LANE R6 (session_018MWpKL71WnBxA8k4ejVkBS, Opus $80: Salviati f.55v-f.57v then code+mark; YX's 13 gate-passing targets by lead class; PP-04), LANE V6 (session_01V2BHwhVh1k72qSYuBFCyGd, Opus $50: Portuguese 1780-1830 judge corpus and the Linhares re-run, verifier for bl-charles-digby, verifiers for readings, rolling QA every two hours), LANE B2 (session_01NS12APP1R55K6TGZrBbP97, Opus $25: breadth). Their common rules: `.claude/briefs/runs/2026-09-25-lanes-7b-COMMON.md` (cost read by the orchestrator, mechanical intake gate, judge only with a real corpus, lead classes, breadth before campaign). Parent 7b at $50 and about 615k context; hand-over to 7c at 700k with hub-seed/SUCCESSOR-PROMPT.md. If this parent
stops, a successor parent reads this section, the lane table,
the last check-in prompt (list_triggers), takes over the trigger with update_trigger persistent_session_id, and continues.

## LANE CX2 handoff (session_018cUWVBDyZzw2sgLAmZKL75), 25 September 2026, 17:05 UTC

Check-solved sweep, round 2. Pool: the YX triage's section D print-check campaigns (sp35, sp54, sp87 x4, sp90 x2,
ra-karlxi) plus every copy-free triage target still failing tools/intake_gate_check.py. 21 targets, 10 Sonnet workers
(briefs .claude/briefs/runs/2026-09-25-lane-cx2-{sp87a,sp87b,sp90,jac,nord,frawi,brit2,misc2,fix,bert}.md), USD 32.96,
7-19 min each, none past its box; orchestrator about USD 3.60. Rate allowed throughout. Every target below now exits 0.

| verdict | targets |
|---|---|
| open, handed to LANE R6 (ROOM 16:26 and 17:05) | sp87-chesterfield-1747, sp87-newcastle-1743, sp87-further-1712, sp87-brunswick-1759, sp90-raby-1704, sp90-raby-whitworth-1705, sp35-townshend-key-1719, sp54-maclean-1745, ra-karlxi-fullmakt-1677 (REQUEST stays Gated), destaing-gerard-1779, hellen-frederick-1752, berthier-napoleon-1812, maurice-rupert-1645, rah-xiquena-1868, decode-2754-bnf-baluze156-1636 |
| partial, line-2 citation, handed to R6 | harley-287-1587, clairambault1225-paget-1714 (L11), wellington-maitland-1812 |
| partial with intake blocked (LOCAL row) | pro3055-clinton-1779 (Saberton, Cornwallis Papers pt.11, L16), catokwacopa-1875 (newspaper issue, L13) |
| found-solved | none. berthier tested: Chuquet's clear 22 Dec letters are not marked as sent in cipher, so the pairing is unconfirmed |

Leads worth a worker: berthier (Vilcoq 1969 p.24 on Persee reproduces the whole cryptogram as a plate: transcription is
copy-free, and Chuquet p.440's two clear letters of the same date are candidate cribs); maurice-rupert (BL Add MS 18982
ff.95-96, same volume, 'partially ciphered (with deciphering)', BL offline); sp90-raby-1704 (BL Add MS 61137 f.41,
Blenheim duplicate, catalogue only); sp87-brunswick (HMC 3rd Report, non-TNA Ferdinand-Holdernesse holding). The
TNA SP items are digitised=false: their next step is a copy order, which is now allowed (stage 2 reached).
Left in the triage and failing the gate: three DECODE-gated items (decode-1162, -1168, -2678) and thurloe-barriere
(ZX). Open for the parent: (1) the 38 REQUEST.md targets in triage section D have never had a check-solved verdict,
yet their copy orders are on the owner's card (Pipeline step 2); a CX3 sweep of them at about USD 3 per target
would clear or kill those asks (asked 15:48, no answer); (2) tools/intake_gate_check.py passes an edition line saying
"was not opened" (pro3055); (3) check-solved.md should say a worker who finds the clear text of a same-date letter
runs the found-solved test itself (FRAWI did not). Running count passing the gate as open or partial: 15 (YX+CX) + 18 (CX2) = 33; 2 more are compliant as blocked.
No live workers, no pending check-in.

## LANE YX handoff (session_01PHaEdHeQY2FtMHLo9yGeoe), 25 September 2026, 13:34 UTC

Left-open copy-free targets. Opened 10:30 by the parent; closed at 13:34 because every session now reads `allowed_warning` on the seven-day window (BUDGETS.md scaling rule: no new workers anywhere). 16 Sonnet workers, USD 75.80 of worker usage, all ledgered and archived; orchestrator about USD 7.7. No live workers, no pending check-in. **No reading passed its judge; no AUDIT.md, no N-class, no second opinion this lane.**

| target | outcome (25 Sept 2026) | next |
|---|---|---|
| antt-msliv0638-brochado-1712 | partial. YX-BRO79: Carta 79's gloss misread (pra->para) fixed from the image; leave-one-out gate now passes (82.6% vs noise-matched 91.4%). Letter 134 candidate C49 M16 U5, but with the new pt judge it FAILs language (-1.443 vs null_p99 -1.428): not a reading. | the other dragging entries (Carta 15, 80, Passage 2a m0284/m0294, Carta 101) by image; only then another decode |
| oldenbarnevelt-brederode-1605 | open. NA 1.01.02 inv.6016 1605-06 folder read leaf by leaf (91 leaves): no cipher, key or decipherment. "Holland 2613" not resolvable in 3.01.04.01 or 1.01.02. | ask NA to resolve the RGP citation; de Leeuw 2022 (LOCAL-QUEUE L12) |
| clair349-este-guise-1556 | partial, gate passes (citation restated at line 2). Key transcribed from fr.20974 (key_alpha 47 rows, 20 H; key_nomen 59 rows, 5 H). Two blind passes of f9 (33 lines) held as ciphertext_draft.tsv: 51.9-65.6% agreement depending on the measure, under the gate; no decode. | one worker: give both passes the key's own atlas codes as a shared vocabulary, re-pass, then decode_key.py (load_keys added) + fr judge |
| clair571-estrades-1645 | open. Letter pinned to Clairambault 575 p.1209; none of Clair 571-582 digitised. REQUEST.md (BnF, batched: 575 p.1209, 574 f.3-4 Brasset key, 579 p.341), **ASKS row 49**. | owner's copy order |
| willem-van-hessen-1567 | open, gate passes (Groen I/III, Gachard II-III read). 1069 sibling: one line per worker (p2 line 1, 14 signs); target 1127 not imaged (REQUEST.md). Parked. | copy order first |
| thurloe-barriere-1654 | open. Pass B reconciled (90.5% after normalization; pass A had dropped a 25-token line); negative stands: 30.0% vs control 31.1%. | permutation z-test on the gloss positions |
| decode-2754-bnf-baluze156-1636 | open. Lasry's second Sabran key negative with matched control (5.412 bits/char = shuffle median vs positive control 3.754); both published Sabran keys fail. | none cheap |
| ormond-arran-1678 | open. Printed Ormond-Longford Cipher 2 (5/20, 34.9th pct) and Cipher 3 (3/20, p=7.8%) negative with control; Cipher 1 has no table on disk. | a Cipher 1 table (HMC vol.5), or a sibling |
| wellington-maitland-1812 | partial. 4 more dictionary copies fail; the remaining editions (Scott, Fulton and Knight 1802, Dublin/London Entick 1801-11, Jones 1800) have no digital copy: library only. | owner/library |
| tools | judge_plaintext.py: pt (pt17, Vieira letters) and it wired, with a test. intake_gate_check.py: partial treated as open (11 tests). decode_key.py: load_keys merges two key files. gbooks_search_within.py sleep 1.5 s. | CX's open ask: found-solved reads as FAIL; an open over an unread edition passes |

- **Triage** (ciphers/_triage/2026-09-25-lane-yx-triage.md): 99 open/partial targets triaged; intake gate PASS 2 of 99 before LANE CX's sweep (15 after). 63 blocked on a person, an archive or a gated account.
- **For LX / the parent:** antt-linhares-chave's committed reading FAILs the new pt judge (-1.559 vs real_p05 -1.014; word cover passes 0.758); the parent's LX-JUDGE is testing whether the judge discriminates on a 26-word dictionary-code fragment.
- **Orphan fixes done** (parent 11:40): colbert26 Kind rewritten, canvas 21 held back; thurloe-barriere negative re-checked on two passes.
- **Lessons** (LEDGER rows): a judge with no corpus for the language is not a gate; a new NOTES section inserted above the verdict breaks the gate tool; workers stopped at 23-38% of their time boxes twice, so a box is also a minimum working time; arbitrary-sign passes need a shared atlas vocabulary before agreement means anything; raw reconcile_passes numbers on printed codes measured notation (5.4%) not error (90.5%). Retrospective trigger met (16 rows, USD 75.80).

## LANE CX handoff (session_01SRJHk4mkeudAH4L39Kc9K6), 25 September 2026, 12:55 UTC

Check-solved sweep on the copy-free targets of the YX triage (ciphers/_triage/2026-09-25-lane-yx-triage.md) that
failed the intake gate. Pool 21, not ~36: of the triage's A/B targets, 7 were YX-claimed and 7 already exited 0 on
tools/intake_gate_check.py; sections C and D were out of scope. Seven Sonnet workers (briefs
.claude/briefs/runs/2026-09-25-lane-cx-{stuart,mary,fr16,clair,ital,brit,apw}.md), USD 24.30 in total, 9-22 min each,
none past its box. Orchestrator USD 3.20. Rate allowed throughout.

| verdict | targets |
|---|---|
| open, gate exit 0, handed to LANE YX (ROOM 12:17 and 12:55) | la-garde-1577, birago-nevers-1571, sp53-22-f52, ormond-arran-1678, clair1161-avis-flandre-1688, clairambault296-paget-1713, bl-james-1669, bl-sacchetti-nunzio-1623, bl-gualterio-1700, courten-diary, clair571-estrades-1645, espagnol142-mercy-1648, decode-4450-bnf-fr20506-1525 |
| blocked (LOCAL-QUEUE row) | sp53-16-78, sp53-16-79 (CSP Scotland viii pp.211-212, probable calendar entry by HTRC EF, L13); fr16092-maisse-1582 (Boucher, Lettres de Henri III V-VI, L9); fr4687-paleologue-nevers (Ferrari 1999, L8; corrected from open by the orchestrator, 1059e26) |
| partial, line-2 citation added | mornington-1798 (Ingram 1970, be-api fts, no hit), catokwacopa-1875, moray-wood-1568 (corrected from open: Aymeloglu's repo carries a cryptanalytic reading of the postscript, credited) |
| found-solved | bl-charles-digby: Wheatstone's 1862 Philobiblon decipherment of Charles I's cipher (F1); shelfmark match to Add MS 6912 circumstantial, wants a verifier |

Of the 13 open, only clair1161 (image on disk, transcription) and la-garde / ormond-arran / clairambault296 have a
copy-free next step; the BL items and courten need copy orders or a reading room, and birago, sp53-22-f52 and
decode-4450 carry control-backed negatives already. Running count passing the gate: YX triage 2 + CX 13 = 15.
Open for the parent: (1) tools/intake_gate_check.py reads only open/blocked, so every `partial` and `found-solved`
exits 1, and it passes an `open` whose citation window says the edition was unread (fr4687): two small fixes;
(2) a verifier for bl-charles-digby; (3) sections D print-check campaigns (sp35, sp54, sp87, sp90, ra-karlxi) were
not in this lane's pool and still carry no gate-passing verdict. No live workers, no pending check-in.

## LANE VX handoff (session_01EYwyYDeAaQReWy7ZuQcoxe), 25 September 2026, 11:08 UTC

Key beside the letter, copy-free. Opened 06:32 UTC by the parent. Closed at 11:08 with every target it opened at a
stated status; no reading passed judge + re-derivation, so no verifier ran and no AUDIT.md exists. QA 08:19 and 10:36
passed every VX item (intake gates, 60% gates, honest judge FAILs).

**Scout counts (job 1, five scouts over two rounds).** 8 rows in QUEUE.md "Key beside the letter (LANE VX, 25 Sept
2026)", all copy-free (image tested at full size): VX-E01-03, VX-N01-03 (all Nationaal Archief), VX-S01-02. Gallica/BnF
(five earlier passes) and BL/BSB/e-codices are exhausted for this pattern; Europeana api2demo gave pure noise (32
queries). About 12 copy-order leads recorded in the section (BnF Français 4717 item 19 cipher + déchiffrement, 4720/
4694/4724 Nevers keys; BL Add MS 18777-80, 28728, Egerton 1696; NA De Witt 1672 cipher + Oplossing 3.20.66.01 inv.
175/182/183, Staten-Generaal Sont/Schaep enclosures with translations, Fagel key items 1.10.29 inv. 499/824; Rigsarkivet
Lagau 1712 intercepts, undigitised). Host findings: ONB Primo search works via tools/browser_fetch.js; BSB manuscript
JSON API (handmade facet); Riksarkivet Search API; Alvin attachment/document route; KB DK, Rigsarkivet's new platform,
Digitalarkivet (names Anthropic) and NLF are robots-blocked; NA catalogue spells some items "cyferschrift".

**Check-solved (job 2).** open 5 (E01, E03, N01, N02, N03), closed-negative 1 (S02: plaintext nickname list), parked
for LANE N4 1 (E02, the Legatie Turkije key beside roell-vandedem-1809), key-only 1 (S01).

**Per target, state and best next step.**
- ciphers/na-schonenberg-1678-1716 (E01), partial: 87-code key from the leaf's own interlinear gloss; the two unglossed
  closing lines decode to fragments (12 C, 7 M, 9 unkeyed of 28), re-derivation identical. Next: a third pass over the
  glossed lines L04-L14 to lift M codes, then the closing lines again. Low value.
- ciphers/na-oldenbarnevelt-2442-1605 (E03), open, kind cryptanalysis, key ours: Spanish with vowels as digits
  (a=4 e=8 i=3 o=7 u=2), reproduced by two independent derivations; 269 tokens S170 M7 I92; judge language FAIL
  -1.32 vs -0.828, word cover PASS. Next: image pass on blocks B (51%) and C1 (43%) to clear the 60% gate, settle
  digit 6 (b/v candidate), then judge again.
- ciphers/na-janssens-java-1811 (N02), partial, key period: 209-code nomenclator from the decipherments of dispatches
  No.2, No.3, No.5 (No.5 also survives as a plain fair copy, the control that caught a key-merge bug) and a Vanteau
  table on leaf 208 (same code). Target leaf 188 (No.1 Triplicata) 163 tokens C52 M24 U87, 46.6% keyed, judge FAIL.
  No No.1 decipherment in leaves 180-219 or invnrs 7/11/13/26. Next: page through the ~185 unsampled leaves of invnr 12
  for more deciphered dispatches.
- ciphers/na-suriname-map-1781 (N01), partial, key period: 17-sign homophonic key from 2007A/2007B twin and 2061's
  gloss; reads 'van' (2039) and 'PLAN' (2077) out of sample; з still contradictory; targets 2039/2046/2077 not decoded.
  Next: settle van-vs-PAN on 2039 line 2, then use 2077's mixed plain/cipher legend as the crib.
- ciphers/na-raad-azie-1800 (N03), open: Colenbrander III-IV read, not printed; inv. 209's ciphered body is decimal
  digits, the inv. 317 (Elout/Van Grasveld) letter system cannot read it (control 100%). Next: treat 209 as a numeral
  cryptanalysis target with its own spec.
- ciphers/alvin-gustav3-chiffre (S02), closed-negative.

**Handed to other lanes.** Bescheiden Oldenbarnevelt II no. 92 (Brederode 1605, printed cipher, editor found no key)
to LANE TX, taken. VX-E02 to LANE N4 (parent's ruling).

**Lessons.** (1) Workers cannot read their own cost: seven wrote "well under cap" at 1.3-4.6x; COMMON now uses a
wall-clock box and bans self-reported cost, and it held for every worker after it. (2) New-term sweeps (ontcijfering,
in cijfer, cyferschrift) found rows cijferschrift alone missed. (3) Period decipherments are rarely complete keys for a
different letter: all three recovery reads stalled at 40-65% coverage because the target's vocabulary exceeds the key
source; a plain fair copy beside a cipher (Janssens No.5) is the strongest control found.

**Cost.** 21 worker sessions, USD 204.85 (LEDGER.md, session metadata); orchestrator about USD 7. Rate allowed
throughout.

## LANE KX handoff (session_01JPoYAFvVfraJibxQdQfrqp), 25 September 2026, 11:00 UTC

Question: what else can the keys we hold read? Answer this window: nothing on disk that was not already known; one new open
target found on the way. Kind of result: a controlled negative plus a new target (contribution), no reading, no AUDIT.md.

- **Cross-match (job 1).** `tools/key_crossmatch.py`, `KEY-CROSSMATCH.tsv/.md` (KX-XMATCH, repaired by KX-XMATCH2). 60 key
  files, 57 usable; 35 find their own ciphertext; 8 of 35 pass the positive control (rank 1 on own text, z vs shuffled key
  >= 4, above shuffled-letter windows). 0 hits, 8 weak (all own-folder rows the pairing could not assign), 0 of 8 false
  positives on century/language-gap pairs. Known reuse pairs (Nassau key_5549/Lodewijk) cover ~0.8 but reach only z 2.45;
  Brienne tables stay under 0.5 coverage across their two folders. The real-text floor of judge_plaintext fails every own
  decode (fr16/de16 are edited text), so it is recorded, not used as a gate. 22 keys still have no own text (no decode.json;
  fr5160 needs one; dupuy452 unsegmented; P9 bespoke). Read "0 hits" as: no cross-read among the 8 validated keys, untested
  for the rest. New corpora tools/data/{la,nl,pt,es,en16}_repo built from repo readings.
- **Office map (job 2).** KEY-OFFICES.tsv (49 keys, 29 offices); QUEUE "Key reuse candidates (LANE KX)": KX-01 Mélanges de
  Colbert 26 part III (Brienne 1661) closed, no cipher in 104/375 canvases, ark corrected to btv1b10035069t; KX-02 (Thurloe
  glossed letters) belongs to TX-THUR; KX-03 new.
- **KX-03, ciphers/colbert26-lathuillerie-1644 (open).** La Thuillerie -> Servien, 1645-48, Mél. Colbert 26 part I, 11
  enciphered letters on 21 canvases. Check-solved open (Négociations secrètes 1725-26 vols 1-4 and APW online full text read).
  The second hand's interlinear notes are topical paraphrases, not a decipherment (KX-LATHKEY2): cribs, no key. Transcribed:
  canvases 20, 21, 27, 30 (519 tokens, 129 signs; blind second pass 58-97% agreement, 109 disagreements open); canvas 26 is a
  different long-number system; 16 canvases queued in NOTES.md. Spec specs/colbert26-lathuillerie-1644.json; cheap test 1 done
  (KX-LATHCT1): canvases 20+21+27 and canvas 30 are two alphabets (Jaccard 0.255 vs same-key control 0.764), and neither is
  the key family of key_1646, key_brienne_1647 or key_1659 (Jaccard 0.14-0.25 vs same-key 0.53-0.86, inside the
  different-key controls). Next, if anyone takes it: settle the 109 disagreements, then cheap test 2 (crib placement of the
  named entities in the notes); full transcription only if test 2 moves it. Expected value is low (very large nomenclator,
  few hundred tokens per alphabet).
- **Workers** (LEDGER): OFFICE 2.57 D, XMATCH 9.50 D-, COLB26 3.95 N, XMATCH2 9.40 N, COLB26P1 9.19 D, LATHKEY 44.06 F
  (interrupted after 61 min without a push), LATHKEY2 2.10 D, LATHTR 6.41 D, LATHCT1 2.47 D; total $89.65; orchestrator
  ~$7. No live workers, no pending check-in.
- **Lessons.** (1) A positive control needs known pairs, not only a null; the first build reported "0 hits" with 1 of 56 keys
  validated. (2) Interrupt a worker at 2x its alarm, not only on the 45-min stall rule ($44 lost). (3) A leaf-map note of
  "decipherment on the page" must be confirmed token by token at native resolution before anyone calls a letter solved (two
  workers and this orchestrator repeated it for 90 min). (4) tools/room.py --push after a manual commit pushes nothing
  ("nothing staged"): a tool fix for the retrospective.

## LANE PX handoff (session_01KapVpHVzNpnnQce5C8c3LY), 25 September 2026, 09:55 UTC

Portuguese holdings and dictionary codes. Opened 04:25 by the parent; closed at its own stop rule (last gate failed).
- **Scouts (job 1):** PX-SCDIGI3 1 row, copy-free 1 (PX-01 ANTT PT/TT/MSLIV/0638, Brochado's London letterbook 1712-13 with its own "Deciffrada" appendix); PX-SCDICT 0 new rows (Gallica/BNP/Europeana/web negative; in-repo only Linhares and Wellington-Maitland); PX-SCDIGI4 0 copy-free, 3 undigitized copy-order leads (PX-02 MNE-ASC/R/4 cifrante-decifrante key, PX-03 MRM/M027.001 tables, PX-04 Palmela dispatch). DigitArq keyword harvesting is exhausted (search stems and fuzzes); next yield is fonds walked leaf by leaf.
- **Check-solved (job 2):** PX-01 `blocked` (CS01: Dória 1944 *Cartas*, 100 copies, unreachable) -> `open` (CS01B: Google Books search-within on rE7SAAAAMAAJ, 19 queries, none of the appendix's London words in the 248 body pages). Open after check-solved: 1 of 1.
- **Read (job 3), ciphers/antt-msliv0638-brochado-1712, status `partial`:** appendix m0279-m0296 = 39 entries (letters 13-123), two blind passes (85.8% raw; the z/7/2 shape settled from a crop atlas as one sign, a barred 7), H 1588/1702 (93.3%). System: homophonic letter substitution applied to selected words inside clear Portuguese (the letters call it a "Diccionario"). Period key key.tsv 40 codes / 29 C; decode.json + `tools/decode_key.py --check` exit 0 for the appendix and the body. Appendix self-consistency 338/390 = 86.7% (corrected from 88.5% after a scoring bug in scripts/06 was fixed). Body: letter map (page = letter number); cipher runs on m0179/m0180 (= letters 80/81, controls) and m0275-m0276 (letter 134, ~70 tokens, past the appendix's last deciphered letter).
- **Gate (not passed, so no reading):** leave-one-out over aligned spans, real 80.2% vs a noise-matched synthetic control 91.0% (5 seeds, 89.8-92.8): gap 10.8 against a 10-point band. Letter 134 is NOT decoded; no spec, judge or re-derivation exists; no verifier, no AUDIT.md, no second opinion.
- **Open, one next test:** hand-check appendix Carta 79 against its image (real 26.7% vs control ~93% on that entry: an entry problem, not generic noise); if fixing it closes the gap, run PX-BRODEC's steps 3-5 (brief .claude/briefs/runs/2026-09-25-lane-px-brodec.md) and then a verifier (Dória 1944, Memórias da Paz de Utrecht purl.pt/23773 unread, Santarém, ANTT catalogue, phrase search, JSTOR row for Hawes 1946 not yet queued).
- **Lessons:** Sonnet workers cannot see their own cost (BROKEY $30.92 and BROKEY2 $14.42 both reported "well under cap"); the orchestrator must watch cost_usd and size jobs small. A key gate must be leave-one-out on aligned spans against a design-matched, noise-matched control, never raw agreement with an abbreviated period gloss (my PX-BRODEC brief got this wrong).
- **Cost:** 14 Sonnet workers $96.30 (ledgered, all archived); orchestrator about $9.50. Retrospective trigger reached for this lane.

## LANE TX handoff (session_01UDxtM9Xv2dnPfoo5z9T6wA), 25 September 2026, 09:35 UTC

Printed ciphertext and orphan recoveries. 13 Sonnet workers, about $61.87 of worker usage; orchestrator about $5.5. No live workers, no pending check-in. Rate allowed throughout.

- **Triage** (.claude/briefs/runs/2026-09-25-lane-tx-triage.md): the printed-ciphertext detector sections hold 26 rows, not ~38: P1 and W1 closed, P2-P24 are thurloe-printed, rounds 2 and 4 had no survivors, HT1 open. The vein is exhausted outside Thurloe. Rows with a confirmed key route: 0 in the detector sections; 1 in the lane's named orphan (WVO 5551).
- **WVO 5551** (ciphers/jan-van-nassau-1572-75; Jan van Nassau to Orange, Keulen, 17 Apr 1574): check-solved open (Groen IV/V indexes and Supplement read in full, Gachard III page by page). Partial reading 26/32 codes under Lodewijk's 1574 table, C23 I2 M1 U6, re-derived 0 diff. AUDIT.md V-TX and V-TX2: **N3**, key **ours**, not N4 (Glawischnig 1973 cites the letter; Jacobi and Blok/Muller not reached). SO-NASSAU-5551 queued. Lead: a second copy at Staatsarchiv Marburg (old citation 4f Nld. 165), not located in Arcinsys; REQUEST.md and **ASKS row 48** for the owner to ask the archive. Six codes (126,127,137,140,145,146) outside the key.
- **thurloe-printed residue**: Lockhart and three vol.3 letters found-solved in print; P10 p.620 L10 10/14 groups read by Blake's key but **N0, key published** (Powell 1937, NRS 76); P3 postscript cross-key check 0/21 raised.
- **HT1** (Recueil des instructions, Suede vol.2): closed-negative, prose about cipher custody only (ciphers/_leads/recueil-suede-chiffre.md).
- **thurloe-barriere-1654** (Barriere to Conde, 20 Nov 1654, Birch II 721-722): open; word-per-code nomenclature, 368 tokens, sparse printed gloss; spec specs/thurloe-barriere-1654.json; first test **negative with matched control** (gloss key coverage 29.3% vs control 33.4%, 10 seeds). Only pass A transcribed (pass B abandoned). Next named test: permutation z-test on the gloss positions; 4 short unglossed fragments 1655-57 are the only siblings.
- **oldenbarnevelt-brederode-1605** (Bescheiden Oldenbarnevelt II no.92, from LANE VX): open, no key route; ~121 codes, ~100 distinct values 30-741 (blind infeasible, inferred). Leads: NA 1.01.02 inv. 6016 (digitised, 624 pp unindexed, 1605-06 folder read 2 leaves); de Leeuw 2022 open-access paper (LOCAL-QUEUE L12).
- **Lessons** (LEDGER): brief exclusions per item, not per folder (my sweep brief excluded all of Thurloe); an image found a printed gloss the OCR-only pass missed; two workers ran ~2x their alarms (BARRT $12.05, KEYS $11.53) -- an interrupt did not stop BARRT, archive did. With 13 rows and ~$62 this lane alone meets the retrospective trigger.

## LANE OX handoff (session_01BE3g8tWbS4T24KXMpShHt4), 25 September 2026, 04:35 UTC

Pool of 12 orphaned open, copy-free targets; triage `.claude/briefs/runs/2026-09-25-lane-ox-triage.md`; job briefs
`2026-09-25-lane-ox-*.md`. 19 worker sessions (all Sonnet), about $89 of worker usage (one F, OX-HEL, stalled on an
AskUserQuestion prompt; COMMON now forbids it), orchestrator about $6. No live workers, no pending check-in.

| target | outcome (25 Sept 2026) | next |
|---|---|---|
| vanbeuningen-dewitt-1657 | partial. Cipher copy found (NA 3.01.17 inv.1538 ff.210-211, plain copy ff.208-209); ciphertext 862 tokens; key by known-plaintext alignment (align.py): 53 codes/21 letters, 446/517 coded tokens C, 70 M, codes 11 and 40 genuinely ambiguous; decode_key --check 0; fresh re-derivation agreed. AUDIT.md: letter text N1 (Fruin/Japikse 1919 pp.405-406), key/decipherment of the cipher copy N3. | SO-VANBEUNINGEN-1657 queued (parent assigns the check when the PR lands); N4 needs Postma 2006 read (JSTOR/owner). |
| vaudemont-willemiii-1699 | found-solved: Japikse KS24 n.220 p.242 prints the 25 Mar 1699 letter from Robethon's deciphered exemplaar. | none |
| breda-statengeneraal-1624-25 | found-solved (plaintext in print): Van der Hoeven, Geschiedenis der vesting Breda (1868) Bijlage XIX, clear text, not marked as a decipherment (N2 shape); Van der Kemp IV p.391 negative. | none unless a verifier wants the ciphertext mapped (copy order NA 1.01.02 inv.4945) |
| clairambault1225-paget-1714 | partial. Two nomenclator letters, Pierre Paget, vice-consul at Genoa, 8 Apr and 28 Aug 1714, f.60-66; ciphertext 2340 tokens (500 cipher, 122 codes, same key); four interlinear glosses. Attempt 1 negative with matched control (target 0% extension/2 contradictions vs control 8.2%/0). | LOCAL-QUEUE row for AN Marine B7 (1714-16, Paget originals, possibly fuller decipherment); no second cryptanalysis attempt. |
| willem-van-hessen-1567 | open, target cipher only in the KHA original (REQUEST.md). Siblings: 174 printed (Groen, Lettre CCLXIX) with a nomenclator key leaf in its bundle; 1069 (1563) carries an interlinear decipherment, no printed edition; its sign read stopped at the 60% gate (glyph atlas started, 10 signs). | Optional: read 1069's interlinear German decipherment as paleography (not glyph-by-glyph), then a verifier; needs the check-solved intake gate first. |
| hellen-frederick-1752 | open in NOTES.md but effectively blocked: Fagel 5206 runs Oct 1752-Jul 1753 (no 4 Jan 1752 despatch); ciphertext DECODE-only, account lacks document permission (ASKS 42). | waits on ASKS 42 |
| la-garde-1577 | open; two control-backed negatives on file; GSME/LMSAC/Groen print check negative; GSME digits confirm the transcription (25/27, 18/18). | only lead: WVO 6467's manuscript margin "solution", unconfirmed |
| Heinsius five (borssele-heinsius-1714, heinsius-hermitage-1704, heinsius-dopff-1702, heinsius-vanhaersolte-1703, rumpf-vandebie-heinsius-1716-19) | archive-only (NA 3.01.19 incl. key items 2315-2317 not digitised); one consolidated request in borssele-heinsius-1714/REQUEST.md, ASKS 46 (H.A. 1836 first). | owner's copy order |

Lessons applied to the lane briefs: known-plaintext keys by scripted word alignment, not hand matching; date-bracket a
volume from a few header crops before paging it; an unfamiliar symbol alphabet needs a glyph atlas before blind passes;
no AskUserQuestion in unwatched sessions. Retrospective trigger: OX-HEL scored F (flagged to the parent 03:18).

## LANE LX handoff (session_01UXTpujdthrPiBDUG57oNwf), 25 September 2026, 03:12 UTC

- **Target:** `ciphers/antt-linhares-chave` (ANTT PT/TT/CLNH/0086/11, DigitArq docId a03cef08d3c04758aa148f5be56d3401). Status `partial`: letter pages 2-3 read, pages 1 and 4 not in this item.
- **Book verdict (pass, round 1):** Vieyra, *A New Pocket Dictionary of the Portuguese and English Languages*, Part I, London 1809 (archive.org `newpocketdiction00viey`). 12/12 key-sheet worked-example groups resolve at exact page/column/rank from the page images, trims from the end (BOOK.md). Worked-example group 5 is `23812`, not `23312`.
- **Reading:** m0002, 26 groups: H 25, M 1 (group p3l1pos4 re-read `285219` -> `283219`, recorded in ciphertext.tsv and graded M; its token 'cagar' is doubtful). `tools/decode_key.py ciphers/antt-linhares-chave --check` exits 0; fresh re-derivation 23/26 on the pre-fix key, 3 settled from the image. Judge PASS is vacuous: `judge_plaintext.py` has no Portuguese corpus.
- **Audit:** AUDIT.md, m0002 fragment N3, Vieyra identification N3. Safe sentence: "This two-page mid-letter fragment was read from the cipher key and a period dictionary at grade H/M; no prior print of its text or prior decipherment was found in the sources searched 24-25 Sept 2026 (AUDIT.md)."
- **Siblings:** maco 86 has 21 items; 17 of 21 and 138 of 604 images eye-checked (LX-SIB, SIB2, SIB3), all ordinary correspondence, no cipher and no leaf of m0002's letter. The fonds's two other "Chave de uma cifra" units (PP-06 CLNH/0020/14, PP-07 CLNH/0078/80) are not digitised.
- **Open jobs:** (1) SO-LINHARES-M0002 queued in SECOND-OPINIONS-QUEUE.tsv; when the runner's PR is posted, a fresh Sonnet verifier checks it (lane brief job 6); this lane is closed, so the parent assigns it. (2) maco 86 /04 (46), /01 (82), /02 (126), /09 (212) unchecked, a fresh DigitArq budget per session. (3) PP-06/PP-07: copy order or digitisation request (person). (4) A Portuguese corpus for judge_plaintext.py before any pt spec gates anything. (5) Outreach gate 2 (second adversarial audit) not run.
- **Cost:** workers $51.20 (BOOK 6.83, TR 8.09, DEC 10.43, SIB 1.62, VER 2.90, FIX 9.00, SIB2 1.47, SO 1.09, SIB3 1.33), orchestrator about $3.40. Rate limit `allowed` throughout.

## LANE DX handoff (session_01LgrmyB7HMcMaeLTRNbEqb4), 25 September 2026, 02:12 UTC

- **Login:** DECODE login works on the owner account (browser route, `tools/decode_browser_login.js`, plain user name); one login at 01:36 UTC fetched 8725, R413, R4930, R1172, R1180. Record pages and thumbnails are real; every attached document and full-size image is the "Insufficient permissions" placeholder (sha1 035489a0...). DECODE reading jobs (lane job 3) wait on the role upgrade, ASKS row 42 (`outreach/decode-image-access.md`), not on credentials.
- **R413 (boswell-1628) and R4930 (randolph-sussex-1569):** both found-solved (ASKS row 1: Woodard 2021; f.278 contemporary decipherment); metadata filed under each decode/; no reading job run.
- **Neighbour clusters (QUEUE D1-D8):** D2, D3, D8 (Bourdeau sessa1524), D4 (damiata1624), D7 (gramont1529) found-solved; D6 folded into D2; D1 found-solved earlier. D5 `ciphers/bne20211-ferdinand-1478` blocked: Galende Díaz read (items /56, /73 only), Tomokiyo 2018 body unread (academia.edu account), ASKS row 45. BNE's digital library 403s from the cloud.
- **Open jobs:** D5 solver once ASKS 45 or 42 is answered; job 3 on 8725 once DECODE documents open. No verifier needed (no reading produced).
- **Cost:** workers $10.29 (probe 0.28, NB-FI 1.80, NB-ES 2.71, LOGIN 2.45, D5ED 3.07), orchestrator about $2.80. Rate limit `allowed` throughout.

## LANE R4 handoff (session_01LrTggxL1PyxmJd6eygqaGY), 24 September 2026, 18:22 UTC

Lane: recovery, two phases: 14:46-16:30 UTC (brief lane-r4-orchestrator, workers A-I) and 16:58-18:22 UTC after the owner's 16:53
decision relayed by the parent (cap $80, 8 workers; workers J-R). Run under the seven-day `allowed_warning` throughout, never `rejected`.
Seventeen workers closed, $81.16 of worker usage; orchestrator about $66. All closed workers ledgered (LEDGER.md with session ids), in
hub-seed/ASSIGNMENTS.md, archived. **One worker live at close: R, the Mellon MS 29 solver (Opus, $4, session_01Avww7WjGT5QhGoQ7JhrKj9,
brief lane-r4-r-mellon-solver) -- for the parent to ledger, archive and route ('for LANE V4' only if it posts a reading).**

**Results (novelty from the verifiers, not this lane):**
| Target | Result | Class |
|---|---|---|
| trew-posthius-1614-18 | both cipher passages read with the leaves' own 12-pair reciprocal keys; 109 tokens H 96 M 13, --check 0 (F); German 1614 text; status partial | for LANE V4 |
| bowes-walsingham-1583 | numerical name-codes collated, codes.tsv: C 1 (189 Montrose), M 9, unread 2 (E) | -- |
| fr5761-election-1519 | f.104 key as a dataset: key.tsv 37 rows H 30 M 7 (three atlas passes, D H L) | -- |
| fr2933-salviati-1525 | f.54r and f.54v transcribed (83.5%, 83.6%; 719 signs). Excluded with matched controls: simple homophonic over base signs (control 75-92%), consonant-sign + vowel-mark (control 93-96%). Code+mark homophonic needs ~2,800 signs (P's curve) | -- |
| fr3993-villeroy-1595, fr3022-garbino-1528 | no design with a working control at their lengths (Villeroy letters+syllables+codes control 2-6%; Garbino none at 1,315 groups), conditional on Bourdeau's transcriptions (N) | -- |
| jan-van-nassau 5549 | 5205 and 5209 fitted, negative (C) | -- |
| fr3789-mariedemedicis-savary-1610 | both passages transcribed; key (BnF fr.3642) not on Gallica, DECODE photo blocked: status blocked, ASKS 43 (M) | -- |
| fr3151-seure-1558 | six items surveyed (cipher in 40=41, 43=44), f75L captured and re-segmented (noise 56% -> 9%), passes still 38.5%: the hand's signs do not separate by shape (K, O) | -- |
| beinecke-mellon29-elia | ff.1v-2v captured from Yale IIIF, two passes reconciled: 248 signs, 32 types, 58 words (Q); solver R: no reading, controlled negative (Italian, German mono and homophonic controls 88-97%, target below every control), closed-negative 18:43 by the parent | -- |

**Open items (priority):**
1. Posthius (LANE V4): read the faint interlinear letters over 1614 cipher lines 2-4 at native resolution before classing.
2. Mellon MS 29: R's result (parent processes).
3. Salviati: f.55r-f.57v with the box-keyed method (~$6.5 a leaf, ~$40), then `codemark_curve.py target cm` on ~2,800 signs; keys
   to seek: a Salviati nunciature key (ASV Segreteria di Stato; Strozziane).
4. Marie de Medicis 1610: waits on ASKS 43 (DECODE role upgrade of ASKS 42, or a BnF reproduction of the fr.3642 key leaf).
5. Seure 1558: not box-keyable; needs an Opus reconciler reading the image for the codes, or a key. Costed at roughly $30 for item 40.
6. M36: f.105-f.110 of the key (same atlas) and the 1519 letters it might open (none in fr.5761 carries 'chiffre').
7. Bowes: a C beyond 189 needs CSP Scotland vi as text. 5549: key source outside Willem's 1574 letters.

**Lessons:**
- Workers that supervised pass subagents overran 1.7-2.7x (A, B, D); after the 16:58 common-rule addendum ("do it yourself, at most one
  pass-B subagent, check cost every page") every phase-2 worker finished under its cap.
- Price a target at its first leaf before buying the rest (J: $6.5 a leaf) and price cryptanalysis with a control curve before buying
  transcription (P, $1.60, showed the code+mark model needs the whole letter).
- Box-keyed confirm/correct passes work where signs separate by shape (Salviati 62.8% -> 83.5%) and fail where they do not (Seure 38.5%
  after the segmentation was fixed); check that on three lines before committing a capture budget.
- Control-first settled five cryptanalysis questions for $1.60-$2.15 each (I, N, P).

## LANE N3 handoff (session_01QimvzgvoH4ALachGScXUC9), 24 September 2026, 16:36 UTC, updated 18:05 UTC

Lane: copy-free nominations, successor to LANE N2 (14:16). Ran 14:46-16:36 UTC under the seven-day `allowed_warning` (owner's decision
14:50; never `rejected`). Own usage about $11.5 of $35; 8 Sonnet workers $25.59, every one ledgered and archived. Briefs:
`.claude/briefs/runs/2026-09-24-lane-n3-*.md`, shared rules `2026-09-24-lane-n3-COMMON.md` (N2 COMMON plus an edition rule, below). Nothing is running.

**Firm stage-2 nominations: 4, all copy-free (Gallica IIIF), per hour:** 14:46-15:46: 1 **fr3993-villeroy-1595** (CS2-26, Nevers to Villeroy
16 Aug 1595, 753-sign mixed nomenclator, cryptanalysis; the edition check rests on Bourdeau's named full-text search of Gomberville t.2, not re-run by us).
15:46-16:36: 3 **fr3022-garbino-1528** (CS2-01, cryptanalysis; CSP Spain III.2 and Lanz v.1 read; Sanudo Diarii v.47 OCR unusable, a gap),
**fr3151-seure-1558** (CS2-02, cryptanalysis; Ribier both tomes and Francisque-Michel read), **fr3789-mariedemedicis-savary-1610** (CS2-05, recovery:
key BnF fr.3642 per Lasry 2021/DECODE R2077, only a partial photo tried; Lasry's break covers sibling fr.3541, not this letter).
**Blocked (edition unreadable, volume named):** fr3625-lauriere-1593 and fr3621-dinteville-1592 (Gomberville 1665 on Gallica only as images; Xivrey t.3
and Perot 1911 read, negative; CS2-16 signer probably the baron, not the bishop, and sibling fr.3623 5/13 July 1592 is a lead), fr3198-labbe-1577
(Nuntiaturberichte III/IX, Koller 2003, not online), fr3984-sega-1593 (Acta Nuntiaturae Gallicae; **fr.3985 no.7 is a probable found-solved**, Goujet 1758
Mémoires de la Ligue v.5 pp.411-414, leaf check pending). **Copy-order:** CS2-17 fr3975-vieuville-1587 (B/W microfilm) and the 22 DECODE-thumbnail CS2 rows.
**Closed-negative:** TR-1 trew-schellhammer-1653 (key-only leaf; a key source for the Volckamer circle).

**Sources closed this lane (do not repeat):** cyphersolver site (writeups/catalogue/keys re-diffed 24 Sept; 32 CS2 rows, keys index at
sources/solver-diffs/2026-09-24-cyphersolver-keys.tsv, 81 published keys); Trew Briefsammlung (all cipher terms, wildcards; BV1 + TR-1 only); Bavarikon
(round 2, Handschrift/Urkunde/Archivgut x institutions: 0 rows; the whole host is now a tested negative for archive-held cipher).
**Next, if the lane reopens after 26 Sept 13:00:** (1) a Gallica page-reader for Gomberville 1665 t.1-2 (images only: read the pages for July 1592 and
July 1593 by eye or OCR) unblocks CS2-06 and CS2-16; (2) a verifier/image check of fr.3985 no.7 against Goujet v.5 pp.411-414; (3) CS2-05 is the best
recovery pick: fetch fr.3642 at full size from Gallica and apply it; (4) the 22 copy-order CS2 rows could turn copy-free only through DECODE full images
(ASKS 42) or the holding archives' own viewers (Saxony R5005-08, BayHStA ÄA 4591 R9319/R9424 are the likeliest); (5) the keys TSV against unread
Gallica siblings for the recovery lane.
**Widening, 16:58-18:05 UTC (parent relaying the owner, cap $60, 6 workers):** five more workers, $30.3. Tested negatives, closed as copy-free
nomination sources: e-manuscripta.ch (OAI has no full-text verb) and e-codices (no letters facet); Europeana TEXT+IMAGE ('cipher' = monogram in
images); Grotius Briefwisseling (keys only, no ciphertext), KB manuscripts (portal retired, collecties.kb.nl Cloudflare); Kalliope digital-copy
filter (no SRU index; 26 digitised hits all excluded) and handschriftenportal.de (medieval book secret-writing). Vatican digi.vatlib not re-run
(LANE N clean negative). From the last CS2 rows: **beinecke-mellon29-elia** (CS2-14, Elias of Cortona alchemical cipher ff.1v-2r, Yale IIIF, open
after csED3; Witten/Pachella catalogue not digitised) is a firm copy-free nomination; **fr2988-ranzo-1520s** (CS2-15) is open but folded into
fr3022-garbino-1528 (same Ranzo corpus); fr15564-mercoeur-1586 blocked (no edition for June 1586); sanguszkow-mniszech-dunin-1714 copy-order;
fr.3985 no.7 found-solved (plaintext = Goujet v.5). **Retracted: fr3993-villeroy-1595** (its Gomberville t.2 search likely ran on the Première
partie: csGOM found only Première-partie arks on Gallica, content ending before 1591); CS2-06/-16 stay blocked for the same reason.
**Firm copy-free nominations at 18:05: 4** -- fr3022-garbino-1528 (+ fr2988 Ranzo), fr3151-seure-1558, fr3789-mariedemedicis-savary-1610 (recovery),
beinecke-mellon29-elia. Next for Gomberville: the seconde partie in another library (BSB, ONB, Google Books via LANE V) unblocks three targets
(villeroy, lauriere, dinteville). Retrospective trigger passed (19 LANE N3 ledger rows, ~$62 workers): flagged to the parent 17:39.

**Lessons (written into lane-n3-COMMON.md where they are rules):** (1) check-solved workers call 'open' with the edition "not located this pass"
(csCS2a, third time today); the rule now says the nomination line needs the volume and pages read in NOTES section 2, and an edition-check worker
($3-4) after check-solved is the cheap fix. (2) Workers misuse status words (csED2 wrote `partial` for "partly printed"): the orchestrator corrects
line 1. (3) Workers under-report their own cost (scBAV2 ~$1.5 vs $3.94): read get_session. (4) Scouts on already-digitised collections are cheap
($2.6-4.3) but yield is thin once a collection is swept; the solver's own catalogue ("attempted, open") was this lane's best source.

## LANE N2 handoff (session_01DfQyAaXAgcoFZMAbBTGj4f), 24 September 2026, 14:16 UTC

Lane: nominations, successor to LANE N (09:53-14:16 UTC). Stopped on the **seven-day** rate-limit `allowed_warning` (first seen 13:50,
resets Sat 26 Sept 13:00 UTC; BUDGETS.md). Own usage $68.2; 20 Sonnet worker sessions about $73.5, every one ledgered (LEDGER.md), ASSIGNMENTS
rows, archived. Briefs: `.claude/briefs/runs/2026-09-24-lane-n2-*.md`; shared rules `2026-09-24-lane-n2-COMMON.md`. Nothing is running.

**Firm stage-2 nominations (15, of which 2 copy-free), per hour:**
09:53-10:53: 2/0 heinsius-dopff-1702, heinsius-hermitage-1704 (+HU10 addendum later; candidate key NA 3.01.19 invnr 2317).
10:53-11:53: 6/1 **jan-van-nassau-1572-75 letter 5549** (copy-free; LANE R3: postscript read, body negative with control, needs a key source),
sp36-stquentin-pretender-1743, pro3053-horesse-1717, sp81-roe-1638 (decipher sibling f.88?), heinsius-vanhaersolte-1703, breda-statengeneraal-1624-25.
11:53-12:53: 0 (the hour went to closing the WVO family).
12:53-13:53: 4/0 sp99-wotton-1622 (f.159 sibling), sp81-stanning-1631 (decipher siblings ff.93/169/216), sp8-ehrenstein-1689, sp36-ball-1745.
13:53-14:16: 3/1 nla-heinrich-braunschweig-1519, stas-waldburg-1653 (edition leads closed by csDA2), **trew-posthius-1614-18** (copy-free, IIIF,
Erlangen; 1614 block has a complete SALUTEM keyword alphabet on the leaf in the sender's hand; 1618 two key blocks in two hands -- a recovery for
whoever runs the next recovery lane; no reading yet, no verifier yet).
Collected from LANE N's last worker: rumpf-vandebie-heinsius-1716-19 (letter 142 negative with control, LANE R2 H1) and vaudemont-willemiii-1699, both copy-order.
**Held, not firm:** gla-claudiamedici-1633 (BAGK NF II/8 unreadable: not on IA, HathiTrust Cloudflare), hza-hohenlohe-1679 (Archiv für hohenlohische
Geschichte 2, WLB journals Anubis-gated), hstas-osiander-1627 (Württembergische Vierteljahrshefte, no full-text route); sp78-waldegrave-delafaye-1734
(N55: catalogue may describe a copy, page check first); borssele-heinsius-1714 and vanbeuningen-dewitt-1657 (leaf/holding unresolved);
DA4 Krauske 1893 Manteuffel decipherment (in-archive, not printed in NASG 14: a contribution once copied).
**Retracted:** jan-van-nassau 5207, 5213, 5221 (printed in clear in Groen V). **Corrected:** rumpf and borssele are copy-order (NA 3.01.19 has no scans).

**Copy-order is the norm now.** Every Heinsius (NA 3.01.19), De Witt (3.01.17), Staten-Generaal (1.01.02) item checked is physical, unscanned; TNA and
German state archives likewise. Copy-free came only from printed ciphertext (Groen 5549) and Bavarikon.

**Sources closed this lane (do not repeat):** WVO as a target source (sources/wvo/print-status-2026-09-24.tsv: 43 of 73 printed, 20 carry
contemporary decipherments on the leaf = key sources for recovery, listed there); DECODE DC11-DC20 (Partially decrypted / no images); DECODE
full-size images (blocked for our account by permission, ASKS 42, outreach/decode-image-access.md; Bourdeau's login reads them); Florence Dieci di
Balìa 32 records (blocked: no edition; Gabbrielli 1863 keys 3-4 name filza 7; images only via DECODE); Polish repcyfr/FBC (negative); EMLO beyond
EM5 (EM4 Wallis-undeciphered blocked on Bodleian imaging, EM5 found-solved); Huygens retroboeken rounds 1-2 (HU1-HU11 done); Arcinsys Hessen (WAF 403).
**Next, if the lane reopens after 26 Sept 13:00:** check-solved csN4 (TNA/BL, brief lane-n-csN4.md) and N48/N49/N56, AN1-AN7, IE1-IE4 (copy-order);
LABW `chiffre` pages 2-8 (scDEA stopped at page 1); Bavarikon other object categories (Urkunden, Akten) with the facet pattern in QUEUE.md; the three
held German edition leads by a browser-capable worker; one enquiry to the holding archive for any undigitised 'in cipher' line (NLS MS 20769 lesson).
**For a recovery lane:** trew-posthius-1614-18 (copy-free, key on leaf); the WVO key sources above for the Nassau circle; key collections DA1-DA3/DA6.

**Lessons (written into lane-n2-COMMON.md where they are rules):** (1) create_session for a worker needs `source_url`; without it five workers idled
23 minutes refusing an 'unverified instruction' (LEDGER row X). Check get_session two minutes after spawning. (2) Read cost_usd, not an estimate: this
session reported ~$12 when get_session said $34. (3) A check-solved worker will post 'open' with an edition lead named but unopened; the
orchestrator must hold such nominations (csDA). (4) Workers sometimes forget their own nomination lines (csHU2); the brief should say 'post them
yourself'. (5) Watch rateLimitType, not just status: the warning that stopped this lane was the seven-day window, which a five-hour reset does not clear.

## LANE V3 handoff (session_01VmWU2CzMFSQKBCWe8XqfTi), 24 September 2026, 13:27 UTC

Verification of French/Dutch/German/Spanish/Italian readings (and English since LANE W2 closed 12:20) plus Google Books
and DBNL, 12:02-13:27 UTC, successor to LANE V2. Closed on the 40-minute quiet rule. Two workers (about $3.1), orchestrator
about $7; rate limit `allowed` throughout. No LANE V3 worker is live; both are ledgered, in hub-seed/ASSIGNMENTS.md (237,
238) and archived. Briefs: `.claude/briefs/runs/2026-09-24-lane-v3-{common,g1,v1}.md`.

| Target | Item | Result | Worker |
|---|---|---|---|
| lodewijk-van-nassau-1573-74, august-van-saksen-1561-64 | 4610/4611/4616; 53/57/126 | stay **N4**: Daussy 2007 read by Google Books search-within, negative; Kluckhohn I already closed by D2; OpenAlex/S2 still 429 | G1 (Sonnet) |
| jan-van-nassau-1572-75 | 5549 postscript (J5S reading, C 163) | **N1**: plaintext printed in clear, Groen Suppl. 1847 no.45 pp.146*-148*, 23/23 words agree; body unread, not classed | V1 (Opus) |

**Open items for whoever holds verification next:**
1. LANE R3 J7 (session_012QC4L49VqeaQqqrs21uD9w, spawned 13:23) is attempting the 5549 body (runs 1-61, the "new" key) by crib
   cryptanalysis with a German control. If it reads, it needs a verifier: Groen prints the body only as raw numbers, so
   the question is whether any archive decipherment or later edition exists (WVO 5549 record, KHA, Groen's notes).
2. The Granvelle correspondence t. IV-V (Poullet/Piot) is the one family on the Lodewijk N4 table still logged as a gap:
   the tome identity among five full-view Google Books copies is unresolved (G1, AUDIT.md 'Residual families').
3. Outreach for every N4 (Gramont, Danzay, Lodewijk, Saxony, and the English set) is held only at gate 2: all 63
   JSTOR-QUEUE.tsv rows are still `queued` (ASKS 32-34, 36, 37, 39-41). OpenAlex's shared-IP budget resets at midnight UTC.
4. DBNL requests from LANE R3 for Groen clear texts of WVO 5204-5213 lapsed when J6 finished; answer if asked again.
   Groen IV Lettre CDXLIV (5797) is on disk at ciphers/lodewijk-van-nassau-1573-74/groen/.

Lesson (LEDGER): before briefing a gap from an AUDIT.md table, grep the whole file for later sections that closed it
(G1's Kluckhohn job was stale).

## LANE V2 handoff (session_017QzVuGiZ8wFQY6HZfUxH1q), 24 September 2026, 11:58 UTC

Verification lane for French/Dutch/German/Spanish/Italian readings and Google Books, 08:47-11:58 UTC, successor to
LANE V. 17 workers (plus LANE V's last two collected), about $49 of worker usage, orchestrator about $30; stopped at
about $79 of the $100 cap with nothing waiting. No LANE V2 worker is live. Every worker is ledgered (LEDGER.md, session
ids), in hub-seed/ASSIGNMENTS.md (184 onward) and archived. Common brief: `.claude/briefs/runs/2026-09-24-lane-v2-common.md`.

**Classes (all in the targets' AUDIT.md; status.json rows match):**
| Target | Item | Class | Audits |
|---|---|---|---|
| clair1108-duvergier | Vergier to Pontchartrain, Mar 1696, A and B | N0 (interlinear decipherment on the leaf) | V1 |
| clair1067-brienne-poland-1646 | Brienne to the Queen of Poland, 19 May 1646 | N0 | LANE V verifier |
| fr5160-letellier-1653 | f.67, Brienne to Servien, 10 Oct 1659 | N0 (clear text on f.68r) | V5, V5b |
| gunther-van-schwarzburg-1561 | WVO 8246 | N0 (Japikse no.316, spaced type) | V4 |
| lodewijk-van-nassau-1573-74 | 5811, 4503 (WV2) | N0 (Groen IV CDLXXXIII/CDLXXXIV) | V7 |
| jan-van-nassau-1572-75 | 5200 p1 | N1, found-solved (Groen IV CCCLXXXIX; 454/460 letters agree) | V6 |
| lodewijk-van-nassau-1573-74 | 4610, 4611, 4616 | **N4** (no prior decipherment located) | V2, A1, D1 |
| lodewijk-van-nassau-1573-74 | 4612 | N3 (keyed runs do not read yet) | V2, A1 |
| august-van-saksen-1561-64 | 126 | **N4** | V3, A2, D1 |
| august-van-saksen-1561-64 | 53 (cryptanalytic, S238 M126 of 364), 57 | **N4** | A2, A3, D2; 57 re-checked vs DNOK by V8 |
| fr20140-danzay-1557 | f.35r-36r | N4 (LANE V's last worker) | collected |

**Outreach:** every N4 above is held at gate 2 on JSTOR rows only: ASKS 32 (Gramont), 33 (Danzay), 36-37 (Lodewijk,
Saxony 126), 39 (Saxony 53/57). CONTRIBUTIONS.md carries each safe sentence marked 'held at gate 2'; no drafts written.
Second-opinion prompts queued: SO-LODEWIJK-1573-74, SO-SAXONY-126, SO-SAXONY-53-57.

**Open items for whoever holds verification next:**
1. LANE G2 never posted readings for decode-2754 (Baluze 156, 1636) or decode-2678 (Colbert 127, 1665); watch ROOM.
2. WVO print check (sources/wvo/groen-check-2026-09-24.tsv): 5549 printed as raw numbers and 5797 partly undeciphered
   in Groen are with LANE N2 csWV2 (11:43); 5194/5207/5213/5221/5799/5810 are in print in clear; 10260 needs its four
   other editions (Lacroix, Muller, Gerlo-de Smet, GSME) checked.
3. Lodewijk 4612 is N3 only because it does not read; if a changed table is found, it needs a fresh verifier.
4. Host notes: OpenAlex and Semantic Scholar answered 429 all day from these containers (log unreachable, retry from
   another session later); books.google.com page text served an 'automated queries' block at 10:25 (use the googleapis
   API only).

**Lessons written into briefs:** check-solved and verifier briefs now require reading a WVO record's Brongegevens codes
first (GPA/GPAS = Groen, JC = Japikse, DNOK = Demandt regests) and treat Japikse's spaced type as deciphered cipher. Five
WVO letters were captured and read that were already printed; one N4 (57) had an unread edition code until V8.

## LANE V handoff (session_01B5x2Dshzz71xBzbJqFnXYQ), 24 September 2026, 05:30 UTC

Verification lane, 03:04-05:30 UTC. Stopped spawning at rate_limit `allowed_warning` (05:30). No LANE V worker is live.
Since 05:16 LANE V owns only the French BnF targets and Google Books queries posted for it; LANE W owns English
targets, Eckert and Thurloe. 29 workers collected (LEDGER rows carry session ids), about $80 of worker usage.

**Classes (all in the targets' AUDIT.md; status.json results rows match):**
- Gramont f.29r (Villandry) and f.30 (Francis I), Rome, 20 May 1530: N3, two audits each; blind second readers done and
  applied (f.30 H 1500 / M 241 / U 232). N4 decision (05:14): stays N3 until two families come back negative: Camusat
  tract ff.91-217 plus versos (read by LANE G 05:37: negative) and a DECODE search (LANE N, queued; the only gap left). Then a fresh N4-decision
  verifier; nothing else to search. SO-GRAMONT-F29R and SO-GRAMONT-F30 prompts queued.
- Danzay to the Cardinal of Lorraine, Copenhagen, 27 Jan 1557 (fr.20140 f.35r-36r): N3, two audits plus the f.36r
  verifier; f.35 second-reader changes applied (H 509 / M 59 / U 70). Delavaud 1911 and Daussy 2015 read, negative;
  Daussy 2001 is on Duplessis-Mornay, not Danzay (ASKS 26 no longer blocks N4). N4 waits only on LANE N's DECODE search.
  f.36r pass C proposed one change (36R1 pos 9 le -> r2), not yet adjudicated.
- Eckert 1862 T1-T10: N1. Thurloe P11-13: N0. fr5160 Brienne f.86/f.88: N0 (f.87 is the contemporary decipherment).
  Eckert E4/E5: N3, two audits, N4 blocked only by Zooniverse Talk (ASKS 27); now LANE W's.

**Final, 07:50 UTC: LANE V closed (own usage about $95 of the $120 cap).** Two LANE V workers are still running and are
handed to cipher-lab-7a to collect (LEDGER row with Session column, status.json, archive): Danzay N4 decision after the
Cryptiana thread closed negative (session_01MoWhkX7KpTtDeEZ8YAWg6z, Opus, $8) and the verifier for Brienne to the Queen of
Poland 1646, ciphers/clair1067-brienne-poland-1646 (session_01Udgi32LVQHdPhEgPKEf6fe, Opus, $10); both end with a ROOM.md
line 'for cipher-lab-7a'. Gramont f.29r and f.30: N4 (no prior decipherment located); the outreach drafts (Tomokiyo/Lasry
email, Bourdeau issue text) wait only on ASKS row 32 (11 JSTOR rows run or waived). Whoever takes verification next
should watch ROOM.md for 'for LANE V' lines at every check-in: the French BnF targets, and Google Books queries posted by
LANE W.

**07:21 UTC update:** Gramont f.29r and f.30 are **N4 (no prior decipherment located)**; outreach gate 2 is open only on 11
JSTOR rows (ASKS row for the owner); draft the outreach once they are answered or waived. Danzay stays N3 until the Cryptiana
forum thread is read (worker session_01L1CNm9KdabuHxwMAGjocEr), then a fresh N4-decision verifier. Google Books runner for
LANE W: session_01KvYknGitoZUTD1KDPB6XW7. Collect both.

**Next, in order (for whoever runs verification):** (1)-(2) DECODE search (LANE N, none) and Camusat ff.91-217 (LANE G, negative) are in; fresh N4-decision verifiers started
06:53: Danzay session_01PKbcXogQ4jYw1rsHvm2Svx, Gramont session_01FwWKsqwM57oancfisEiVEE ($10 each) -- collect them; (3) f.36r adjudicated and applied 06:24 (H 37 / M 26 / U 4); (4) second-opinion
PRs [SO-*]: check every citation as a lead, log unconfirmed ones in AUDIT.md; (5) at N4, outreach gate 2 still needs the
JSTOR-QUEUE.tsv rows for the target answered or waived by the owner before any draft goes out.

**Lessons written into briefs or the ledger:** verifiers search the holding archive's full text across the collection
(verifier brief); IA loans give a person, not a worker, a readable page (CLAUDE.md playbook); a contemporary
decipherment in the same volume is N0 without print; an N4 decision needs a principal-families table, not the audits'
own gap lists; value-changing second-reader proposals go to an Opus adjudicator, not a Sonnet applier.
Not kept: ASSIGNMENTS rows (ASSIGNMENTS.md lives in the hub repository, which this session did not have).

## LANE R3 handoff (session_01GPDjihFcZasP5KTSYRS5uN), 24 September 2026, 13:52 UTC

Lane: recovery on copy-free nominations, 12:03-13:52 UTC, successor to LANE R2. Four workers (J5I J5S J6 J7), $41.15 of worker
usage, orchestrator about $14. All ledgered (LEDGER.md with session ids), in hub-seed/ASSIGNMENTS.md, archived. Briefs
`.claude/briefs/runs/2026-09-24-lane-r3-*.md`. Stopped because no copy-free nomination remains (the last, 5549, arrived 11:51)
and because **this session read `allowed_warning` on the seven-day window at 13:50 UTC (resets Sat 26 Sept 13:00 UTC)**, posted
in ROOM and BUDGETS.md. No live workers.

**Results (novelty from the verifiers, not this lane):**
| Target | Result | Class |
|---|---|---|
| jan-van-nassau-1572-75 5549 closing stretch | leaf pp.4-5, 226 tokens, read under Lodewijk's 1574 five-per-letter table: C 163 I 13 M 6 U 44; `decode_5549.json --check` 0; agrees with Groen Suppl. no.45 pp.146*-148* | N1 (V3 V1) |
| jan-van-nassau-1572-75 5549 body | runs 1-61, 539 numerals, image-checked (590/593 agree with Groen); key not on file. Negative with matched German control: control 10.9% tokens / 14.4% letters, true key scores below found key, so beyond the anneal at this length (J7) | -- |
| sibling keys | 5550, 5552, 5557, 5204 are in Lodewijk's 1574 table (5550/5552/5557 glossed on the leaf); 5207/5208/5213 are a separate <100 system that Groen V prints in clear (known-plaintext pairs, untouched) | -- |

**Open items:**
1. 5549 body needs a key source, not more cryptanalysis: untested 5205 and 5209 (one-page fit with j6/fit.py, $2); letters to or
   from Jan Nov 1573-Mar 1574 in other archives. Crib context is in groen/groen_5549.tsv.
2. The <100 system of 5207/5208/5213 (Willem to Jan, 1574): three known-plaintext pairs with Groen V in clear; an aligner job
   would give its key (N1 at best, since Groen prints the text) -- a dataset, low priority.
3. Ranzo f.136 (decode-4450): not spawned; 320 codes in 749 tokens with no crib cannot be read by an anneal (a control would
   fail as J7's did); needs a clear copy. DECODE 1162 Modena stays blocked on ASKS 42.
4. csWV3's key sources (sources/wvo/print-status-2026-09-24.tsv: 5801/11250 decipherment for Lodewijk NB1 gaps; 58, 1069;
   7630) are leads for the next recovery lane, none started.

**Lessons:**
- The pre-capture look paid: Groen printed 5549's numbers, so J5I became a one-pass image check against print, and the leaf
  showed a cipher stretch Groen had silently printed in clear.
- Look at neighbouring briefnrs on the WVO leaf before cryptanalysis: J5S found glossed siblings in five minutes.
- Image-reading workers still overran (J5I 47%, J5S 72%); the two TSV-first workers (J6, J7) finished at 75% and 28% of cap.
- Run the matched control first: J7 settled "beyond the method" in 20 minutes for $4.


## LANE R2 handoff (session_0169D5ZhVf9y378dTq1bHp41), 24 September 2026, 11:25 UTC

Lane: recovery and cryptanalysis on copy-free targets, 08:47-11:25 UTC, successor to LANE R. 19 workers (inherited R19 plus
C1 L1 S1 G1 L2 D1 J1 W1 F1 L3 J2 W2 H1 J3 L4 D2 and the two over-cap stops), about $115 of worker usage, orchestrator about $22.
All ledgered (LEDGER.md, session ids), results rows in status.json, briefs `.claude/briefs/runs/2026-09-24-lane-r2-*.md`.
ASSIGNMENTS rows not kept (hub repository not reachable from this session). No live workers at handoff.

**Results (all `decode_key.py --check` 0; novelty from the verifiers, not this lane):**
| Target | Result | Class |
|---|---|---|
| huntington-luzerne-destouches-1781 | R19: 108(B) is a duplicate (96.0%); key agrees 92.8-94.2% with Destouches' glosses; 108(A) C 410 M 163 U 146 of 719. Closed here. | N0 |
| august-van-saksen-1561-64 | 57 = System A (C 247 M 53 of 300); 53 = third key, broken by tools/homophonic_anneal.py (control 99.3%), S 238 M 126 of 364 incl. f.266v | N4 (53, 57) |
| gunther-van-schwarzburg-1561 | key 79 signs aligned from 5109 vs Japikse no.236; 8246 C 817 M 53 U 83 of 953 | N0 (Japikse spaced type) |
| lodewijk-van-nassau-1573-74 WV2 | 5811 C 616 of 1542; 4503 built (237, M); 5810 one pass; 5799 fails the table (control 81.5%) | 5811, 4503 N0 (Groen IV) |
| jan-van-nassau-1572-75 | printed 1572 key (5198 reprint) reads 5200 p1 H 680 of 807, p2 left H 325 of 399; 5218/5222 printed in Groen | 5200 N1; 5218/5222 retracted |
| la-garde-1577 | negative on a 3-witness reconciled transcription: homophonic control 73.5%, periodic 100%, target none | -- |
| rumpf-vandebie-heinsius-1716-19 | letter 142 negative: 208 tokens, 64 signs, control 28.8-70.7%; now copy-order (LANE N2) | -- |
| decode-4450-bnf-fr20506-1525 | dataset: 749 tokens, 320 codes, 94.1% agreement with Bourdeau's fr.2988 f.9 witness | -- |

**Open items:**
1. WVO GPA letters (Jan 5207 5213 5221 5549; Lodewijk 5194 5797 5799 5810): LANE V2's G3 runs the Groen-by-page check. Only
   letters whose cipher Groen omits are worth a reader; the tools and passes are in place (key_1572, R18 table, wv2/build.py).
2. decode-1162-modena-ambung-1492 (DC4): blocked on 200 px DECODE thumbnails. LANE N2's dcB tests the logged-in ImagesList route
   (Bourdeau got full-size scans that way); if it lands images, one Sonnet transcription pass, then assess.
3. decode-4450 Ranzo: two witnesses on disk; a solver needs a clear copy or crib (Bourdeau's annealer got function words only).
4. La Garde: a code/nomenclator in number form is the untested hypothesis; Groen VI 249-251 context (DBNL, LANE V2's host) is the
   crib source.
5. DC2 decode-1411 and DC5 decode-9970 stay HELD by LANE N's 08:37 line.

**Lessons:**
- WVO's Bron code GPA means the letter is printed in Groen van Prinsterer; two workers ($17) read letters already in print.
  Check the print by date, and open every page of the WVO PDF (C1 found Groen and Japikse pages bundled inside), before briefing.
- Image-reading workers overrun: J1 42%, W1 89%, L3 175%, R19 70% over. About $3 a dense page for Sonnet at several zooms;
  scope by pages (three at most) and give Opus the TSVs only.
- Aligner and finisher jobs with a key in hand stay cheap (G1 $3.48, F1 $2.20, D2 $2.52 by reusing Bourdeau's witness).
- create_session needs source_url (LANE N2 lost 23 minutes without it).

## LANE R handoff (session_01SEnQgi5wPVmMADaVHnWkNN), 24 September 2026, 08:44 UTC

Lane: recovery and cryptanalysis on copy-free stage-2 targets, 05:05-08:44 UTC. 21 workers (R1-R21), $188 of worker usage,
orchestrator about $64. Every finished worker ledgered (LEDGER.md), ASSIGNMENTS rows 104 onward, results rows in status.json.
Briefs: `.claude/briefs/runs/2026-09-24-lane-r-*.md` (common rules in `-common.md`). Stopped at the orchestrator's $65 mark.

**Readings (all `tools/decode_key.py --check` 0; novelty not classified by this lane):**
| Target | Kind | Result | Handed to |
|---|---|---|---|
| rah-canada-1869 | recovery | note read from its own interlinear Spanish, C 665 M 2 of 667; LANE W: N0 | done (AUDIT.md) |
| huntington-blathwayt-madrid-1728 (U2) | recovery | key 395 groups C from seven deciphered items, one code 1725-29; BLA 184/186/191(a) C 129 M 22 U 21 of 172 | LANE W (R17's ROOM line 08:16) |
| huntington-luzerne-destouches-1781 (U1) | recovery | key 229 figures C from mssDE 68/37/55; 108(A) C 347 M 157 U 215 of 719 (R16 context fills all M, control 50%) | LANE W; see open item 1 |
| lodewijk-van-nassau-1573-74 (NB1) | recovery, partial | letter cipher, five numbers per letter from n; key from 4613/4615; targets C 2512 I 267 M 658 U 575 of 4012 | LANE V (R20 08:36) |
| august-van-saksen-1561-64 (NB2) | recovery | two systems; key B from 98 f.67; 126 p4 C 214 M 26 of 240 | LANE V (R21 08:41) |
| oxenstierna-gustav-adolf-1632 (W1) | catch | found-solved: Torpadie, Historisk tidskrift 8 (1888); our reading an independent re-decipherment (control 98.0%) | done (AUDIT.md N0) |

**Open items for whoever takes the lane:**
1. **R19 still running** (Sonnet $5, session_01RcrjBffN5sbbMVbWJPaZ6v): fetches Huntington mssDE 108(B), the deciphered duplicate of 108(A)
   that LANE W found (08:17), aligns its glosses and scores our key against them. Collect it: ledger, archive, and rewrite the U1
   results row (108(A) is then read from the duplicate's contemporary decipherment, C, and the key gets an external check).
2. **NB1 Lodewijk:** still gappy (U 575, M 658). Next: an Opus pass on the M/U stretches with the key and the image (TSV-first, crops
   only for M runs), or a third pass on 4611/4612 where agreement was lowest. Names/nulls above 120 need the sibling pairs.
3. **NB2 Saxony:** 53 (1561) and 57 (August's own) not read; 53 shares system A's shapes but not its key; key A (from 74) is in
   key_74. One Opus aligner-style worker, $5.
4. **NB4 la-garde-1577:** captured and inventoried only (6179 pp.2-3, ~140 numeral groups in French prose; Marnix 6467 same design,
   short marginal notes). Both pass workers lost their output. Next: one Sonnet reader with page-by-page writes ($4), then an Opus
   cryptanalysis with a matched control; Groen's printed text (DBNL, LANE V's host) gives the context around each gap.
5. **Hosts held:** hdl.huntington.org (R19 until it stops), resources.huygens.knaw.nl (free).

**Lessons (written into `.claude/briefs/runs/2026-09-24-lane-r-common.md`; worth a template edit in `.claude/briefs/transcription.md`):**
- Opus workers that read page images blow caps 2-3x (R6 $44, R7 $35). The same targets finished for $2-5 when Sonnet produced TSVs and
  Opus worked TSV-first (R10, R17).
- Where the decipherment sits in the file, skip blind passes: one aligner on the image with the plaintext beside it (R8 $3.42, R18
  $4.29, R21 $4.79) beat two blind passes (7.6%, 32%, 56% agreement on cursive digits and symbols).
- Pass subagents must write their TSV page by page; R14 and R15 lost every pass at the interrupt ($20).
- A cloud worker cannot be messaged directly; interrupt it, then a one-shot `create_trigger` with `persistent_session_id` delivers
  "push within two tool calls and stop". It worked for R6, R7, R13, R14 and R15.
- Search the whole holding collection for duplicates first (LANE W found mssDE 108(B) after $60 of key work on 108(A)); and run the
  print check for a printed cipher before the solver (W1 fell to an 1888 journal).

## LANE N handoff (session_01W4z8JhXJYHRjorPC1Qkpiy), 24 September 2026, 09:55 UTC

Lane: nominations (05:04-09:55 UTC). About 40 Sonnet workers, every finished one ledgered (LEDGER.md), ASSIGNMENTS rows, archived.
Briefs: `.claude/briefs/runs/2026-09-24-lane-n-*.md`; shared rules in `2026-09-24-lane-n-COMMON.md` (edition-not-read = blocked, 80-percent cap stop,
open every bundled page of a free PDF). LANE N itself ran to $128 of usage, over its cap: see Lessons.

**Still running, for LANE N2 to collect:** check-solved HU (session_01M9UDxvoQKRt5ZG1Z7TWy3B, Sonnet $6, brief lane-n-csHU.md): HU4 Rumpf/van de Bie
to Heinsius 1716-19, HU8 Van Beuningen to De Witt 1657 (clear and cipher copies), HU6 Vaudemont to Willem III 1699, HU5 Borssele; holds
nationaalarchief.nl, resources.huygens.knaw.nl and LANE N's archive.org slot until its done line. Nothing else is running.

**Nominations per hour (firm stage 2 / of which copy-free):** 05:08-06:08 9/0 (R1 R2 R3 R5 R7 Riksarkivet; N50 N51 N52 N53 TNA); 06:08-07:08 4/3
(lodewijk-van-nassau-1573-74, august-van-saksen-1561-64, la-garde-1577; willem-van-hessen-1567 copy-order); 07:08-08:08 2/2 (decode-2754 Baluze 156,
decode-2678 Colbert 127 -- both taken by LANE G2 for Gallica capture); 08:08-09:08 4/4 (jan-van-nassau-1572-75, gunther-van-schwarzburg-1561,
decode-4450-bnf-fr20506-1525, decode-1162-modena-ambung-1492); 09:08-09:55 0. Total 19 firm, 9 copy-free.
**Released to LANE R/R2 (copy-free):** the Orange-circle targets (lodewijk incl. 6 WV2 letters, august-van-saksen, la-garde, jan-van-nassau minus
5218/5222, gunther-van-schwarzburg), decode-4450 (DECODE gives 200-px thumbnails only: needs Gallica fr.20506 f.136 and fr.2988 f.9 via LANE G2),
decode-1162 (thumbnails only and its transcription is served as forbidden.png: blocked on access unless the owner asks DECODE).
**Held or retracted, with reason:** R6 ra-crusenstolpe-1809 and R8 ra-karlxi-fullmakt-1677 (edition not located); the six IR folders
(della-torre-olanda-1690, viganego-torino-1717, belmesseri-napoli-1627, salvago-caraffa-1691, clerville-francia-1648, taurello-roma-1527: open
without the Savoy/Este/Genoa edition read); decode-1411-hhsta-vienna-1600 (DECODE says Partially decrypted); decode-9970-simancas-1527 (CSP Spanish
vol. 3 pt 2, HathiTrust msu.31293027025760 seq 508/980, unread); jan-van-nassau 5218 and 5222 retracted (Groen prints their cipher passages).
**Found-solved catches (never nominated):** R9 Gripenstierna (Beckman 1999/2002); DC3 Villeroi 1577 (Lasry 2022); DC6 Mazarin-Bordeaux (Lasry 2025);
DC7 Catherine of Aragon (Bosbach 2018, Tomokiyo); WV4 Marnix (Muller 1888, Gerlo/De Smet); Greenhow at LoC (Tomokiyo, Fishel 2014).

**DECODE state.** RecordsList filtered by status is login-free (tools/decode_list.py). Census sources/decode/records-non-decrypted-2026-09-24.tsv:
1186 Non-decrypted + Partially decrypted Cipher records; the diff (-diff.tsv, tools/solver_repo_diff.py --census): 596 ours, 510 Bourdeau, 9
Aymeloglu, 60-71 held by none. DC1-DC10 checked (above); DC11-DC20 unchecked and mostly a Modena/Milano cluster (ids 1121-1167) that DECODE marks
Partially decrypted -- check DocumentsList before any nomination. DECODE images are 200-px thumbnails for these records: DECODE is a finding aid,
not an image source; get the image from the holding archive. Open asks for DECODE: LANE W's Blathwayt query (09:51 ROOM: Huntington / Blathwayt /
Marchmont / Ripperda in Decrypted records, 1728-29) is NOT yet run.

**Sources found this lane (routes that work):** WVO database (resources.huygens.knaw.nl/wvo; curator notes 'onopgelost cijferschrift', free PDF per
letter; sources/wvo/: 92 cipher records harvested, all circles checked); Huygens retroboeken full-text accessors (Heinsius/De Witt =
search_in_text, Oldenbarnevelt/Willem III/Staten-Generaal = searchText; sources/huygens/, HU1-HU8); EMLO Solr backend
(emlo.bodleian.ox.ac.uk/solr/all/select, bibo_Note:"not decoded", 'Cipher letter' facet; EM1-EM3 copy-order); RAH OAI-PMH (74 percent swept, resume
from offset 18400); FBC graphql API for Polish libraries (no hits yet; repcyfr.pl worth a proper harvest); HTRC EF numeral detector
(tools/htrc_numeral_pages.py; controls pass, needs an index/paylist filter before another round).
**Dead ends (do not repeat):** PARES (TLS root, ASKS 28) and BDH (Cloudflare); NARA (API key, ASKS row); Founders Online 'not deciphered' notes (all
solved by the editors); LoC digitised (0 of 40); IA manuscripts metadata (0); CUDL/Digital Bodleian (0); DigiVatLib (all deciphered in situ);
Florence ASFi viewer (search fails its own control); German digitised libraries (best HAB leads not digitised); BL (no manuscript copy-free now:
access.bl.uk DNS-dead); US research libraries B (6 of 7 hosts blocked).

**Next round should sweep (copy-free first):** check-solved HU rows (after csHU reports) and the unswept asterisked Vaudemont entries in the Willem
III/Bentinck index; other correspondence editions with curator cipher notes and free scans (Grotius Briefwisseling, Oldenbarnevelt, Staten-Generaal
Lias despatches on Nationaal Archief scans); EMLO 'Cipher letter' facet beyond the 3 rows, filtered to letters with linked images; DECODE: run LANE
W's Blathwayt query, then DC11-DC20 by DocumentsList; the DC5 page read (CSP Spanish, needs Google Books -- LANE V2's host); RAH OAI remainder;
repcyfr.pl. Copy-order rows still unchecked: N54-N66 (briefs csN2-csN4 ready), N48/N49/N56 (BL), AN1-AN7, IE1-IE4, EM1-EM3, IR6/IR7/IR9.

**Lessons.** (1) My own cost: I reported "about $39" to ROOM while get_session said far more; the orchestrator's context re-read at every check-in
is the spend. Read cost_usd at every check-in and hand off at 550k context. (2) Parallel scouts at 2x load burnt the shared window in 40 minutes
(05:10-05:50); seven workers were cut off. (3) tools/room.py matched conflict markers anywhere in a line and spliced ROOM.md when a line quoted
marker text; fixed by a worker (844b58b, anchored at line start). Two workers committed conflict markers into QUEUE.md/QUEUE-scores.json via
stash pops; both fixed. (4) The census diff pooled 'Partially decrypted' with 'Non-decrypted' and missed Bourdeau holdings; check-solved caught it
before LANE R spent anything -- keep status as a hard filter. (5) Scouts do not nominate; several wrote 'nominations: N' for queue rows.
(6) Free PDFs can bundle the printed edition: open every page before 'open'.

## LANE S handoff (session_01PE7TAF6Hsp3MHtFEkDPP4a), 24 September 2026, 04:58 UTC

Lane: finding and gating targets outside Gallica (03:05-04:58 UTC). 25 Sonnet workers, about $140 of worker usage, every one
ledgered (LEDGER.md), ASSIGNMENTS rows 61-83, results rows in status.json. Briefs: `.claude/briefs/runs/2026-09-24-lane-s-*.md`.

**For the parent to promote (stage 2, copy-free):** rah-canada-1869 (RAH digital library); huntington-luzerne-destouches-1781 (U1;
Tomokiyo decoded a sibling 8 Jan 1781 Luzerne letter, Yale, same code, key unidentified); huntington-blathwayt-madrid-1728 (U2;
recovery by alignment: six sibling items carry French decipherments); oxenstierna-gustav-adolf-1632 (W1; printed cipher
extracted, 733 tokens / 91 values; key not public: two undigitised Riksarkivet candidates in its REQUEST.md, SE/RA/202/1 and the
Horn-Bielke E 2348/E 2350 duplicates). A solver for W1 or U2 is the parent's to assign.
**Stage 2, copy order (REQUEST.md drafted, nothing on the owner's card):** N20, N22, N27, N28, N29, N34, N36, N37, N41, N43, N44,
N45, N46, N47, E1, U3, U5, K1, K2, K4. Held by the parent's instruction, not checked: N23-N26, N31-N33, N35, N38, N39; N48-N66
not yet checked.
**Found-solved catches:** N21 Palavicino 1590 (Stone 1956); K3 Ulrich-Zwingli 1531 (Zwingli SW 11 no. 1193); N40 Cotton cluster 6 of
14 volumes (Tomokiyo keys, a 1759 print, Brewer L&P ii for Galba B IV), 4 unresolved; N42 Wallis letter-book (a key resource,
not a target); RAH Morillo item 1 (Rodríguez Villa 1908).
**Sweeps and negatives with controls:** detector rounds 2-4 (276 + 212 + 152 editions; 1 survivor, W1); scouts K (Kalliope: K1-K4),
U (Huntington, Lambeth: U1-U5; two access routes in CLAUDE.md), E (Europeana negative; RAH E1), R (Riksarkivet R1-R10), Z (Polish,
Czech, Hungarian, Slovenian libraries: zero). Blocked or keyless: NRS (egress), BSB/MDZ, ONB, DDB, Archivportal-D, Polona API.
**Still running / open:** check-solved I (R1, R2, R3 with keys in folder; R7) session_01Wxt9yrhshAu6m7cRw5qya9 -- parent to collect
and archive; then check-solved J (R5, R6, R8, R9), brief ready, one worker at a time on the Riksarkivet.
**Next if the lane reopens:** check-solved N48-N66 (copy-order, lower value); Polona with the browser tool; a CRO sweep via TNA
Discovery 'held by other archives'; QUEUE-scores.json non_decode rows 41-66 still to re-apply from 9aafdef (my policy refused it).
**Lessons written into templates:** .claude/briefs/detector-test.md (index pre-filter, whole-volume decipherment grep, no rebase
during a background fetch). ROOM.md: a claim commit stages ROOM.md only (5573927 deleted N41-N66; restored).

## LANE W (English-language verification), 24 Sep 2026, 05:35 UTC

Orchestrator session_011UFnhZnyCntZ8Bn9FpKyTq, cap $80. Spawning paused at rate_limit `allowed_warning` (resets 06:10 UTC).
- Eckert E4/E5: Talk gap not closable from this environment (no Wayback captures of talk.zooniverse.io; live host
  egress-blocked). Stay N3; ASKS 27 now carries the three direct subject links (AUDIT.md 'Talk gap, second attempt').
- Results rows, English targets: 16 checked, 7 corrected (hub-seed/results-audit-W-2026-09-24.tsv).
- Thurloe P4 (Stamford, 13 Mar 1655): **N4 (no prior decipherment located)**, 09:04, after two audits, an N4-decision verifier and
  LANE N's DECODE negative. Outreach gate 2 open on JSTOR rows and OpenAlex/S2 (ASKS 34); Bodleian image ASKS 30.
- Luzerne 1781 mssDE 108(A) and 68: N0, found-solved (deciphered duplicate 108(B) in the same collection).
- rah-canada-1869 (Cañada note): N0 (clear text on the item). Blathwayt BLA 184/186/191(a): N3 single audit, second audit running.
- Gustav II Adolf to Oxenstierna 1632 (W1): N0, found-solved (Torpadie, Historisk tidskrift 8, 1888). Lesson added to
  .claude/briefs/check-solved.md.

## LANE W2 status, 24 Sep 2026, 11:47 UTC

LANE W2 orchestrator session_01CLm9uFwyau9hRmDcm2vALE (successor to LANE W's 10:09 handoff), about $4 of $100 at 11:46.
Three workers, about $4.5 together, all ledgered and archived; none live.
- **Blathwayt BLA 186 (cipher lines), 191(a), 184: N4** (no prior decipherment located), B1 11:03, AUDIT.md 'N4 set (LANE W2
  worker B1)'. BLA 186's clear text stays N1 (Rose 1831 ii 414-15); any outreach states that print. Gate 2: ASKS 40.
- **Eckert E4/E5: N4** (no prior decipherment located), E2 11:27, AUDIT.md 'N4 set (LANE W2 worker E2)'. The Talk gap (ASKS 27)
  closed without the owner: `talk.zooniverse.org` serves the Talk API as JSON where `talk.zooniverse.io` is refused (E1). Gate 2: ASKS 41.
- **Thurloe P4: N4** unchanged; gate 2 on ASKS 34; ASKS 30 (Bodleian leaf) has a card.
- **Owner cards (status: ready):** outreach/gramont-jstor-waive.md (JSTOR rows for all N4 items incl. Blathwayt, Eckert),
  outreach/openalex-s2-owner-queries.md (six open-index queries; OpenAlex/S2 still 429 from cloud at 11:01),
  outreach/bodleian-rawl-a24-p4.md (ASKS 30). No outreach drafts until gate 2 is answered or waived.
- **Closed 12:20 UTC 24 Sep 2026** (about $5 of $100): nothing new in scope since 11:47; ASKS 34/40/41 still open; no live worker.
- **Next LANE W:** once ASKS 34/40/41 are answered or waived, draft outreach for P4, Blathwayt and Eckert (gate 6 links).
  Blathwayt lead from B1: DECODE BL Add MS 32270/32305 and SP 106 box 7 key collections may hold the Pareti code.

## LANE W handoff, 24 Sep 2026, 10:09 UTC

LANE W orchestrator session_011UFnhZnyCntZ8Bn9FpKyTq stopping at about $62 of $80 (handoff rule: stop before $70). Workers A-K
(11 LEDGER rows, about $27 of worker usage), all archived; no LANE W worker is live. Classes are in each AUDIT.md.
- **Thurloe P4** (Stamford, Calais, 13 Mar 1655): **N4 (no prior decipherment located)**, two audits + N4 decision + DECODE.
  Outreach gate 2 open only on ASKS 34 (JSTOR rows 35-37/39/40; OpenAlex/S2 from the owner's machine). ASKS 30: Bodleian leaf.
  SO-THURLOE-P4 queued. No outreach draft yet; next LANE W: draft only after ASKS 34 is answered or waived.
- **Blathwayt BLA 186/191(a)/184** (Huntington, 1728-29): N3 x3, two audits, partial. BLA 186's clear part printed by Rose
  (Marchmont Papers 1831 ii 414-15). N4 decision (worker K): only DECODE's Decrypted list is open, posted for LANE N at 09:51;
  negative => N4 for all three with the sentences in AUDIT.md 'N4 decision' s.4, set by a small verifier (worker J pattern, $3).
- **Eckert E4/E5**: N3, two audits; N4 waits only on ASKS 27 (Zooniverse Talk, browser; no Wayback copies exist).
- **N0 / found-solved** this shift: Gustav II Adolf to Oxenstierna 1632 (Torpadie 1888), rah-canada-1869 (clear text on the
  item), Luzerne 108(A) and 68 (duplicate 108(B) deciphered by Destouches).
- **Results rows** for all of the above match AUDIT.md (worker A audited 16 English rows at 05:17; rows edited since by LANE W).
- **Briefs changed:** check-solved (national journal after an 'unsolved' edition; whole-collection duplicate search);
  verifier (recipient's printed family papers in translation).
- **Retrospective:** LANE W has 11 ledger rows; the next lane's 12th row triggers one (.claude/briefs/retrospective.md).
- **Watch for:** LANE N's two DECODE results (Blathwayt); 'for LANE W' lines from LANE R2 (English/Huntington readings);
  ASKS 27, 30 and 34 answers.

## Lane structure, 24 Sep 2026, 03:05 UTC (owner: scale to about fifty live sessions)

The parent orchestrator (session_01EFmUvFAifLKGdBSsW9mjEG, "cipher-lab-7a") runs four lane orchestrators, each Opus with a
cap of $80 (raised to $120 and 16 workers at 05:12 UTC 24 Sept 2026 when the owner authorised doubling the effort; back to 10 workers at 06:34 after the window was exhausted in forty minutes, see BUDGETS.md) and up to about ten workers, each owning its hosts so no two lanes hit the same host in parallel:

| Lane | Session | Owns | Hosts |
|---|---|---|---|
| T, Thurloe printed cipher (closed 05:19 UTC, scope exhausted; P4 audit with LANE W) | session_01EwdS3bprjRaK49MrSERfA2 | ciphers/thurloe-printed, solvers with controls, print checks | archive.org text only |
| G, Gallica digitised manuscripts (handed over 06:39 UTC; LANE G2 live from 07:43) | session_015NqJ9uu5Ef3Bo6QaRiGcGp (G2; was session_014zWyan51u9qMn9gnHpm1Aq) | every M row, crops, passes, reconcilers, same-office key trials | the only lane on gallica.bnf.fr and archivesetmanuscrits (at most two fetchers at a time) |
| V, verification (closed 07:50 UTC on handoff; succeeded by V2) | session_01B5x2Dshzz71xBzbJqFnXYQ | verifiers, adversarial second audits, blind second readers, toward-N4, the results-list audit, outreach drafts at N4 | Google Books, HTRC, IA full text, loc.gov, Delpher, DBNL |
| S, scouts and detectors (closed 04:58 UTC, succeeded by LANE N) | session_01PE7TAF6Hsp3MHtFEkDPP4a | check-solved on N20+ and Q rows, extraction of printed cipher, further detector rounds, non-Gallica catalogues | IA advancedsearch, TNA Discovery API, BL, NRS, Wellcome, LOC, BSB, Europeana |
| G2, Gallica manuscripts (07:42-11:56 UTC, closed on handoff; succeeded by G3) | session_015NqJ9uu5Ef3Bo6QaRiGcGp | Brienne-Poland 1646 key to LANE V, fr.5160 1653-band key trials and canvas walk, Du Vergier 1696 reconciliation, Gramont f.30r top lines, Gallica scout round 4 | the only lane on gallica.bnf.fr and archivesetmanuscrits, two fetchers at most |
| V2, verification FR/NL/DE/ES/IT (08:47-11:57 UTC, closed on handoff; succeeded by V3) | session_017QzVuGiZ8wFQY6HZfUxH1q | Du Vergier 1696, Lodewijk van Nassau, August of Saxony, the DECODE-BnF items; Google Books for every lane; Gramont and Danzay outreach held at gate 2 | Google Books, HTRC, IA full text by claim, DBNL, Huygens, WVO |
| W2, verification of English-language readings (10:57-12:20 UTC, closed: every English item at N4; English readings go to LANE V3 until a W3 is needed) | session_01CLm9uFwyau9hRmDcm2vALE | Eckert E4/E5 Zooniverse gap, Blathwayt N4 families, Huntington and Riksarkivet readings, the LANE W owner asks to the card | HathiTrust APIs, HTRC, loc.gov, Founders Online, NARA, Wayback, Huntington catalogue, Scandinavian editions, BHO |
| G3, Gallica manuscripts (12:02-14:01 UTC, closed on handoff at the seven-day allowed_warning; no successor until 26 Sept 13:00 UTC) | session_01WVnAc4cU7RQjEoBfbkuGrG | G2's successor priorities only; DC8/DC9, natives for the recovery lane, one more scout family; pauses if only owner orders remain | the only lane on gallica.bnf.fr and archivesetmanuscrits, two fetchers at most |
| V3, verification FR/NL/DE/ES/IT (12:02-13:27 UTC, closed on handoff, nothing unowned; no successor until 26 Sept 13:00 UTC) | session_01VmWU2CzMFSQKBCWe8XqfTi | readings 'for LANE V3', second-opinion prompts for the Saxony and Lodewijk N4 items, outreach drafts once JSTOR rows are waived | Google Books, HTRC, IA full text by claim, DBNL, Huygens, WVO |
| R5, recovery (successor to R4, 18:48 UTC 24 Sept, owner: keep chasing momentum under the seven-day warning) | session_01LcgYWtnKYzBkdEwVU1ae1t | Salviati f.55r-f.57v priced at the first leaf then the code+mark model, Seure coarse atlas, M36 key leaves f.105-110, N4 nominations; cap $60, 6 workers | gallica images on disk; Cryptiana and solver-diff snapshots on disk for the key search |
| N4, copy-free nominations (successor to N3, 18:48 UTC 24 Sept) | session_01Nrrp9gDcF8aHUgcMSXxU7q | Gomberville 1665 seconde partie as text, fr.3985 no.7 leaf check, published keys vs unread Gallica siblings, holding-archive viewers for the CS2 copy-order rows, check-solved with the edition in the verdict; cap $40, 4 Sonnet workers | Google Books, HathiTrust APIs, BSB, ONB, IA full text, gallica (two fetchers), sachsen.de and BayHStA viewers |
| R4, recovery (successor to R3 and to G3's Salviati/M36 work, 14:46 UTC, owner's decision to run under the seven-day warning) | session_01LrTggxL1PyxmJd6eygqaGY | Posthius 1614/18 key-on-leaf, Salviati 1525 atlas passes and key trial, 1519 election key transcription, 5549 key source, Bowes numerical codes; cap $50, 5 workers |
| N3, copy-free nominations (successor to N2, 14:46 UTC) | session_01QimvzgvoH4ALachGScXUC9 | cyphersolver site re-diff, Trew collection sweep, check-solved on copy-free rows; cap $35, 4 Sonnet workers |
| N2, nominations (09:52-14:16 UTC, closed on handoff at the seven-day allowed_warning; no successor until 26 Sept 13:00 UTC) | session_01DfQyAaXAgcoFZMAbBTGj4f | copy-free first: DECODE census beyond DC20, Nassau circle and Huygens editions, RAH OAI, Vatican, Simancas, Florence; four firm nominations an hour | IA advancedsearch, TNA Discovery API, BL, Wellcome, loc.gov, PARES, Italian and Vatican sites, Huntington CONTENTdm catalogue, Lambeth CalmView, Riksarkivet, HTRC, de-crypt.org (one worker at a time), Huygens and WVO |
| R3, recovery on copy-free nominations (12:03-13:52 UTC, closed on handoff at seven-day allowed_warning) | session_01GPDjihFcZasP5KTSYRS5uN | Jan van Nassau 5549 (closing stretch C 163, N1; body negative with control) | resources.huygens.knaw.nl |
| R2, recovery on copy-free targets (08:47-11:25 UTC, closed on handoff; succeeded by R3) | session_0169D5ZhVf9y378dTq1bHp41 | Jan van Nassau 1572-75, Günther of Schwarzburg 1561, the four DECODE records with images, Lodewijk additions, La Luzerne 108(B) key | hdl.huntington.org, RAH, Riksarkivet IIIF, Nationaal Archief and Huygens images, NARA, loc.gov |
| N, nominations (successor to S, 05:04 UTC; asked to hand off 09:53 at $128) | session_01W4z8JhXJYHRjorPC1Qkpiy | check-solved N48-N66 and R rows, new catalogue families (Italian and Vatican archives, PARES, LoC, NARA, Dutch), HTRC detector, the DECODE Non-decrypted census; target four stage-2 nominations an hour, posted as ROOM `nomination:` lines | IA advancedsearch, TNA Discovery API, BL, Wellcome, loc.gov, NARA, PARES, Italian and Vatican sites, Huntington CONTENTdm, Lambeth CalmView, Riksarkivet, HTRC, de-crypt.org (one worker at a time) |
| R, recovery and cryptanalysis on copy-free targets (05:04-08:44 UTC, closed on handoff; succeeded by R2) | session_01SEnQgi5wPVmMADaVHnWkNN | U2 Blathwayt alignment, U1 Luzerne, W1 Oxenstierna solver with control, rah-canada-1869, then LANE N's copy-free nominations; readings to LANE V | hdl.huntington.org, RAH, Riksarkivet IIIF, NARA and loc.gov images, US library image servers |
| W, verification of English-language readings (05:06-10:09 UTC, closed on handoff; succeeded by W2) | session_011UFnhZnyCntZ8Bn9FpKyTq | Eckert E4/E5 toward N4 (Zooniverse Talk gap), Thurloe P4 audit, every reading from LANE T and LANE R, English results-list audit; LANE V keeps the French BnF targets and Google Books | HathiTrust APIs, HTRC, loc.gov, Founders Online, NARA, Wayback, Huntington catalogue, Riksarkivet and Scandinavian editions, BHO |

Every lane writes its own LEDGER, ASSIGNMENTS and results rows, hands readings to LANE V by a ROOM line, stops spawning at
rate-limit status `allowed_warning` and interrupts its workers at `rejected`. The parent keeps the board, ASKS, the
owner's card and the hourly check-in, and promotes to the board. Twelve workers started before the lanes keep their
original parent until they report.

Every LEDGER.md row a lane writes carries the worker's session id, and a lane greps the full LEDGER.md for that id
before appending a row for it — a lane can see another lane's or the parent's rows in the same shared file, so this
catches a worker archived twice (RETRO-2026-09-24b: two exact-duplicate rows, $9.22, from two of five concurrent
lane orchestrators archiving the same session; the aggregate retrospective trigger also ran to 55 rows/~$334 before
anyone checked because each lane counted only its own dispatches — the parent's hourly check-in now runs that count
against the whole ledger, across every lane, at every check-in).

**LANE S, 03:23 UTC: two new working hosts.** Huntington Library's CONTENTdm API (`hdl.huntington.org`) and
Lambeth Palace Library's CalmView catalogue (`archives.lambethpalacelibrary.org.uk/CalmView`, a plain repeatable
GET results URL found, no session needed -- see QUEUE.md's new section for the exact pattern) both answer curl
directly and produced real candidates (U1-U3, U5 in QUEUE.md "UK and US catalogue candidates"). The Royal
Archives/Georgian Papers Programme (`gpp.rct.uk`, same CalmView software) is reachable but low-yield (heraldic
"cipher" noise, one already-famous 1880 telegram). e-codices.unifr.ch's real search endpoint was found and gives
zero "cipher" hits; not worth another sweep. NRS stays egress-blocked (one reachability test only, per the
brief). County-record-office access via TNA Discovery stays gated on ASSIGNMENTS row 13's scoring worker
(`session_01JE9661cSHNoQDHEvtc2qQb`) posting `done` in ROOM.md -- not posted yet, skipped entirely this sweep.

## Handoff from orchestrator wake 2 (noautopilotytbiz, session_01SepNMpYrr6L2EwqL43aTnm), 24 September 2026, 01:20 UTC

**What this wake produced.** One reading at N3 and one reading found in print; still zero unique solves until the Gramont second audit reports.
- Gramont to Villandry, Rome, 20 May [1530], BnF fr. 2980 f.29r (ciphers/fr2980-gramont): read with Tomokiyo/Lasry's published Gramont 1530 key, 569 signs, H 538 / M 26 / U 5; partial and single-reader. Verifier class N3 (AUDIT.md). An adversarial second audit (session_012r7Td2JUq7nX5UmkAJXLCd, Opus, cap $12) was still running at this wake's close (01:47 UTC, reading Le Grand vol. 3); the next orchestrator collects it, writes its LEDGER row, and archives it; nothing goes outside the repo until it reports (Outreach gate 2). f.30 (the second letter, about 55 lines): shared sign atlas committed, two passes not reconciled (worker stopped at cap). Next: a Sonnet crop/pass worker plus an Opus reconciler, then decode.py.
- Raince to Madame, 25 Oct 1525, Dupuy 452 ff.28-29 (ciphers/dupuy452-carpi-1520): read with Tomokiyo's 1526 key, H 5,281 / C 77 / M 355 / U 12 of 5,725, but printed in Jacqueton 1892 P.J. XXXIII from the decipherment at f.31 of the same volume; f.20 and f.24 are printed there too (P.J. XXXI, XXXII). Verifier class **N0** (AUDIT.md, 01:47 UTC): found-solved; our key-to-glyph mapping and re-decipherment are a contribution only.
- Dropped: M9 Morvillier 1546 (Lasry 2023), M10, M11 (no ciphertext). Tomokiyo's 'readable with a published key' list gave no further free letter. Bourdeau offline-only scout: B1-B5, all copy-order.
- Briefs changed from RETRO-2026-09-24 (proposals 1-3, 4 in part); ASKS 22 and 23 decided by cipher-lab-7a under the owner's standing instruction.

**Ownership split (ROOM.md 00:54):** this wake owned fr2980-gramont and dupuy452 ff.28-29; cipher-lab-7a owns everything else (DECODE, scouts, dupuy452 f.24, orange-nassau-1572). The next orchestrator collects the two running audits above, writes their LEDGER rows, and republishes the board.

**Lessons for the templates:** the class gate must search the standard modern edition of the recipient's diplomacy (Jacqueton for Louise de Savoie), and any same-volume 'déchiffrement' item, before transcription money; on image-heavy transcription, a Sonnet worker cuts crops and the atlas and Opus only reconciles (the Opus f.30 worker ran to cap on image work).

## Handoff from the ytbiz orchestrator, 23 September 2026, 22:24 UTC

**01:19 UTC, 24 Sept: Gramont f.29r at N3; Raince found in print.** The verifier classed Gramont's letter to Villandry (fr. 2980 f.29r, 20 May [1530]) N3: no printed plaintext or decipherment located. The reading is partial (several lines continuous French, the rest letters not yet divided) and rests on one transcription. An adversarial second audit is now trying to find it in print; no outward note before it reports (Outreach gate 2). The Raince letter to Madame (Dupuy 452 ff.28-29) reads with Tomokiyo's 1526 key, H 5,281 of 5,725, but Jacqueton's La politique extérieure de Louise de Savoie (1892) prints it from the decipherment at f.31 of the same volume, and the other two letters (Carpi f.20, Raince to Robertet f.24) too: a contribution (a key-to-sign mapping and an independent re-decipherment), not a unique solve; a Sonnet verifier is setting the class. The f.30 Gramont worker stopped at its cap with the atlas committed.

**00:51 UTC, 24 Sept: Gramont f.29r reads with the published key; verifier running.** Gramont to Villandry, Rome, 20 May 1530 (BnF fr. 2980 f.29r): the cipher passage reads with Tomokiyo and Lasry's Gramont 1530 key into continuous French, 569 signs, graded H 538, M 26, unread 5 (decode.py --check passes). The two blind passes failed (29 % agreement, coded against drawings from another hand); the reading rests on the reconciler's transcription with a legend cut from the leaf, checked by the key producing French. No class yet: a verifier session (Opus) is searching Le Grand 1688, Letters and Papers, Pocock, Ehses and the rest, and an adversarial second audit follows if it comes back above N1. The second letter (f.30, about 55 lines) is being transcribed with the same legend. ASKS 22 and 23 were decided by the parent orchestrator under the owner's standing instruction; the Raince solver has started on the 50-type text, 1526 key first. The Raince third pass stopped at its cap with nothing committed.

**00:32 UTC, 24 Sept: Tomokiyo list and retrospective.** Tomokiyo's pages name 14 letters that his published keys should read; none is free for us (Bourdeau's repository holds the Bayonne 1529 and Birago clusters, one is already solved, and fr. 2980 Gramont is ours and in hand). His academia.edu list was built from his own site after that host answered 403. The retrospective (RETRO-2026-09-24) found this window's failure and over-run shares double the day before, from stale container clones and clock drift, not reasoning; four brief fixes are applied and two policy items are on ASKS row 23. The Raince third pass was stopped at its $6 cap; the Gramont transcription and key worker is still running.

**00:03 UTC, 24 Sept: Raince reconciled, not clean; Gramont gated at N3.** The Raince letter (Dupuy 452 ff.28-29) was rebuilt from the images by glyph segmentation and clustering: 5,725 signs in 50 types, 365 marked uncertain. By the gate the owner set (passes within 5 %, fewer than 40 types) it is not clean: pass A skipped half of 28 lines, and 22 of the 50 types are rare signs that only a solver can merge or keep. The solver is held; a third pass covers the skipped half-lines and the gutter, and ASKS row 22 asks the owner whether the solver may start with 50 types. Gramont's two letters of 20 May 1530 (fr. 2980) pass the print gate at best case N3 (not in Letters and Papers iv.3, which calendars two other Gramont cipher letters of February 1530 from Le Grand; Le Grand's own May 1530 pages were unreachable and go to the verifier). Transcription and Tomokiyo's published key are next. Dupuy 468's check.py now carries the ten gloss exceptions.

**23:43 UTC, 23 Sept: M8-M11 swept.** Two of the four survive only as plain copies (M10 Sabran 1637, M11 Du Faure 1622; dropped). M9 Morvillier 1546 was broken by George Lasry in 2023 (Tomokiyo's page names this very letter): found-solved, the worker's 'open' corrected. M8, Gramont's two letters from Rome of 20 May 1530 (fr. 2980 ff.29-30, about 650-800 signs), is open: Tomokiyo writes that they 'can be read with Gramont's cipher (1530)', the key he published, and no solver repository has applied it. A print check (Le Grand 1688, Letters and Papers Henry VIII, Pocock) runs before any transcription, since du Bellay's 1529 letters turned out to be in Le Grand. The owner asked this wake to keep going and take on more targets; a Tomokiyo bibliography worker (row 26) also lists every letter his pages say is readable with a published key.

**23:40 UTC, 23 Sept: wake 2, first reports.** Bourdeau offline-only scout (row 21) done: of 12 items his repository marks offline-only or stuck, 7 were already ours and 5 are added as QUEUE B1-B5 (WW2 censorship manual, 1520s superscript ciphers, Ungnad 1576, Florence 1414, Toulon 1803); none is copy-free, so none is promoted while the copy-order asks wait. The first row 25 worker stalled on a stale clone and was replaced. The Raince reconciliation (Opus) and M8-M11 check-solved (Sonnet) are running. The previous orchestrator session prepared a history purge on `purged-main`; swapping it in is the owner's step (ROOM.md, 23:39).

**23:16 UTC, 23 Sept: wake 2 started.** The three outreach emails were sent by the owner on 23 Sept (Tomokiyo, BnF, NLS; CONTRIBUTIONS.md). A fresh orchestrator session on this account (session_01SepNMpYrr6L2EwqL43aTnm, Opus, cap $60) now carries the list below, starting with the Raince reconciliation (ASSIGNMENTS row 24), then M8-M11 check-solved, then rows 21 and 25. This session closed at $235.5.

Read this, then CLAUDE.md (the Outreach rule and the good-citizen rule are new today), the lane table above, ASKS.md
and the last 40 lines of ROOM.md. The credential session started at 21:40 UTC may still be running its own list
(presence test, DECODE login, Sforza images, catalogue pull, IA loan, Google Books page for Bowes, JSTOR pass,
Ingram 1970 check); read its ROOM.md lines and ASKS.md rows before repeating anything.

**First job (ASSIGNMENTS row 24):** reconcile the two blind transcription passes of Raince to Madame, 25 Oct 1525
(ciphers/dupuy452-carpi-1520/passA.tsv, 4,797 tokens in 124 codes; passB.tsv, 6,012 rows in 25 codes) against the
160 crops by image-based glyph clustering (segment signs, cluster by shape, label clusters, then map both passes onto
the clusters), producing ciphertext.txt with a sign inventory. Then try Raince's 1526 key (Tomokiyo's francis.htm,
BnF fr. 2984, Desenclos 2018) and run tools/nomenclator_anneal.py with a matched control. Best case N3 (class gate
passed 23 Sept). Strongest model for the reconciliation, cap about $40; the solver only if the inventory is clean.

**Then:** M8-M11 check-solved (digitised BnF lane, still open); the Bourdeau offline-only scout (row 21); the P2-P24
Thurloe passages only after a leaf check against the tracked Thurloe pieces. No new keyword sweeps of copy-order
lanes while ASKS rows 14-16 wait on the person. Run the retrospective after 12 ledger rows or $60.

**Standing facts:** zero unique solves so far. Both readings of 23 Sept (Bowes, Dupuy 468) were in print; the gates
caught them; they are logged as F2 and F1 contributions in CONTRIBUTIONS.md with drafts in outreach/. Two BL orders
are out (Courten, Mornington). TNA page checks reopen in the UK morning. This orchestrator ran to $218; close at $60.

**Next session on this account, first actions (written 18:02 UTC, 23 Sept 2026).** (1) Presence test of the seven
variables with `test -n`, no values printed. (2) One DECODE login attempt via `tools/decode_fetch.sh 8725 ...`; on
success, ASKS row 1 to done and ASSIGNMENTS row 7 starts (record 8725, then a polite full catalogue pull to
`sources/decode/`, then the neighbour tool on the whole catalogue). (3) One archive.org login attempt via
`tools/ia_borrow.py` on a named page check (ASKS row 2). (4) Read the three worker reports of the night (non-DECODE
scout, Burgess 1912, Bowes 1583) in ROOM.md and the target NOTES, and pick from the new QUEUE sections. The
good-citizen rule in the Access playbook applies to every request.

**21:56 UTC, 23 Sept: credential session (ytbiz), done.** All seven credential variables reach a fresh container on this account (ASKS row 10 done). DECODE: the single login was rejected (`IS_LOGGEDIN:false`; row 1 back to open, with the observation that the form asks for a user name while the variable holds an address); record 8725, the Sforza-Maino images and the catalogue pull did not start, so ASSIGNMENTS row 7 stays blocked. archive.org: login and a one-hour loan work, but lending items are served obfuscated for the site's own reader and `tools/ia_borrow.py` now stops on such a payload instead of decoding it; the Hamilton 1932 report pages go to the person (row 18). Google Books: no full-view copy of CSP Scotland vi exists, but its no-preview copies answer phrase searches with running-text snippets, which reached nos. 389 and 584: Boyd prints the Bowes names in clear and the numeric codes in quotation marks, with no cipher note on the names, and p.566 cites fol. 299 with "In cipher" footnotes (AUDIT.md section 10; the verifier decides whether that moves N1). JSTOR: challenge-blocked for curl and Chromium, credentials untested, eight queries handed to the person (row 17). Next session on this account: nothing credential-side until rows 1 and 17 move; the Dupuy 468 verifier, the Dupuy 452 crops and the detector test were live at 21:34 UTC in the other orchestrator's session and are theirs.

**Correction, 17:29 UTC.** Re-running the exclusion by volume as well as by id shows Bourdeau's repository already
names 193 of the 202 neighbour pairs in the cached catalogue, and D1 (Pallotto) is found-solved (key broken 2018,
printed edition). Five pairs survive (D8, RAH 9/29), in a volume between two he is reading. So the cached-catalogue
neighbour lane is not ours. What is: (a) the full DECODE catalogue behind the login, which the scrape does not cover;
(b) archives not on DECODE at all, where the two projects do not look (Gallica beyond his BnF picks, BL and TNA
series, NRS, county record offices, dealers), reached by the access playbook and copy orders; (c) the four archive
requests already drafted. The count-maximising plan is therefore a scout on non-DECODE catalogues (TNA Discovery
"cipher" hits, NRS, BL Explore, Gallica full-text for "chiffre" with no DECODE record), which needs the network fix.

## Handoff to the next orchestrator (21 September 2026, 03:00 UTC)

Read this, then CLAUDE.md, then the target table below. Everything you need is in the repository; nothing
important lives only in the previous session's conversation.

**What this project is.** Read old ciphered letters nobody has read. The bottleneck is access, not
cryptanalysis: the online material has been swept by two well-funded AI projects, so our lane is the paper in
archives. README "What counts as a result" defines the three kinds (recovery, cryptanalysis, contribution)
and every board card carries one.

**Where to look.** `STATUS.md` (this file) is the human board. `status.json` feeds `dashboard.html`, published
at https://claude.ai/artifact/Mbveo2jWKwmA7RTqBuCkis (owner's account) and, from the noautopilotytbiz account, at
https://claude.ai/artifact/HzYszSGfSoWPsYXpxvM5zr (published 23 Sept 2026; each account can only republish its own);
rebuild with `python3 tools/build_dashboard.py` and republish to your account's URL after every worker result.
docs/index.html is the same page for GitHub Pages (ASKS row 8). `CLAUDE.md` holds the ten rules, the Pipeline, the Usage
section (model tiering; Sonnet for search and transcription, the top model for reconciliation, verifier and
orchestration), the Access playbook and the Improvement loop. `ROOM.md` is the workers' shared channel.
`LEDGER.md` is one row per worker with cost and outcome. `QUEUE.md` is the ranked queue; `.claude/briefs/`
holds the role templates.

**The two rules that were learned the hard way.** Rule 10: a solver may never call anything new or
unpublished; only a separate verifier, after a logged search, assigns an N-class. And no copy order, payment
or quote request reaches the owner until a check-solved sweep has set that target to stage 2.

**Orchestrator change, 23 September 2026, 15:20 UTC.** The previous orchestrator's account is logged out; a fresh orchestrator on the noautopilotytbiz account took over from this handoff, with nothing unpushed on the old account. That account's environment has no credentials set (ASKS.md row 10), so this orchestrator runs only credential-free jobs: Randolph 1570 native-resolution re-transcription (ASSIGNMENTS row 1) and a check-solved sweep on queue ranks 11, 13, 15, 17, 18 (row 3). The Google Books print checks (row 2) wait for an account with the key.

**23 September 2026, 16:40 UTC, what happened next.** Two workers reported. (1) Check-solved on queue ranks 11, 13, 15, 17, 18: Charles I to Rupert 1645 was read by Bourdeau on 21 Sept with Lasry's King-Queen key (dropped, found-solved); Harley 287 is mostly read by Bourdeau since 21-22 Sept (partial); Catokwacopa 1875 partial with no unique plaintext recoverable; Burgess 1912 and Bowes 1583 open at stage 2. (2) A sibling sweep for Randolph 1570 found that the next leaf, f.278 (DECODE R4932), is a clerk's contemporary decipherment, read by Bourdeau on 21 Sept, and that Boyd's 1903 calendar already says "partly in cipher, deciphered". Randolph is dropped as found-solved; the transcription worker was stopped and its crops are kept for the record. Lesson written to LESSONS.md: open every neighbouring DECODE record with the same shelfmark, and re-clone the solver repositories before every campaign, because Bourdeau's project read three of our queue items in two days.

**Blocked on the owner, new:** this account's environment has no credentials (ASKS row 10) and its network policy denies every archive host: archive.org, bl.digirati.io, hathitrust.org, wikisource.org, gutenberg.org, de-crypt.org, scienceblogs.de (ASKS row 11). From this account only github.com, pypi.org and googleapis.com are reachable, so no access, print-check or image work can run here until the environment's Network access setting is changed. The owner's steer for the week is one cipher solved that a verifier can class N3 or better; with the archive lane closed from this account, the only candidate with material obtainable is Burgess 1912, and its text is on Wikisource and Internet Archive, both blocked.

**15:49 UTC.** The queue was diffed against fresh clones of both solver repositories with the new `tools/solver_repo_diff.py`: four more rows had been solved years ago and are dropped (Boswell 1628 solved 2021, Goring 1645 solved 2020, Sadler 1559 printed 1809, Anne 1711 printed), five are partly read by Bourdeau (ranks 7, 8, 19, 20, 35). The Randolph worker stopped and committed 49 native crops. DECODE record R413 is no longer needed (ASKS row 1 updated).

**15:59 UTC.** The harvest (QUEUE.md "Candidates held on GitHub", 12 rows) gave one genuine cryptanalysis candidate reachable from here: the Sforza-Maino 1446 pair, BnF italien 1583 ff.68 and 70, which Bourdeau closed unread after annealing each letter alone; the joint anneal as one shared key was never tried. Check-solved: open at stage 2, conditional on DECODE, Gallica and Cerioni being unreachable from this account. Lope Hurtado 1522 was left alone as Bourdeau's live target.

**16:46 UTC, end of this orchestrator's wake.** The Sforza-Maino solver finished: four matched synthetic pairs of the same design read at 99% or better, the real pair cleared its shuffled baseline by 0.2-0.4 nats against 1.8-2.0 for the controls, no token claimed. Closed-negative, conditional on Bourdeau's draft transcription, since no image is reachable from this account. Reusable tooling landed in tools/ (joint nomenclator annealer, 15th-century Italian model). Nothing was solved today.

**What the owner's steer needs next.** One cipher solved that a verifier can class N3 or better is not reachable from this account as configured: every archive host is blocked (ASKS row 11) and no credentials are set (row 10). Once either is fixed, the order of attack is: (1) Burgess 1912, text on Wikisource, stage 2, untested acrostic families named in its NOTES; (2) Bowes 1583, search-print in CSP Scotland vi, then BL images; (3) the Sforza pair re-transcribed sign-exact from the Gallica image and rerun through run_target.sh; (4) the harvest rows G1 and G2 only if Bourdeau has stopped on them (re-run tools/solver_repo_diff.py first). Spink lot 1184's question lapsed with today's sale; the images were saved on 19 Sept.

**Running right now (16:46 UTC):** nothing. Erving 1807 was found already printed and dropped; Randolph 1570 has images and a first-pass transcription but no key, and is queued behind the owner's credential fix.

**Waiting on the owner:** rotate the DECODE and archive.org passwords (both were printed into worker
transcripts on 20 Sept) and set IA_USER to the account email; email Spink before the 23 Sept sale; the Kansas
order for Stair; an NLS quote and five-leaf sample for MS 20769; a British Library quote for Monck.

**Waiting on archives:** National Records of Scotland (Hamilton key sheets), The National Archives (Stepney
page check, order 3660178), the Huntington (corpus enquiry sent 19 Sept).

**Standing routines:** weekly retrospective, Mondays 06:00 UTC, emails five proposed changes and a
cost-per-result verdict. Breakthrough alert, fired on demand. Morning summary, as scheduled.

**Cost note.** The previous orchestrator ran from 17 to 21 September and reached $2,042 of plan usage, more
than every worker combined, because one long session re-reads its whole history. Prefer a fresh orchestrator
session every few days over one that runs for ever.

## Overnight summary, 19-20 September 2026 (written 05:15 UTC, completed 06:12 UTC)

**Nothing was cracked.** One over-claim was caught and turned into a rule; two archive orders are out; three new
targets are filed with requests drafted; the browser fix works in every new container.

**Done tonight**

- Eckert 1864: twenty entries read at grade H from the surviving Cipher No. 1 book; the "four not printed" claim
  was audited by a separate verifier and withdrawn (E6 and E12 were in print, N1; E4 and E5 no prior print
  located, N3; AUDIT.md). A key test then showed the headquarters entries are Cipher No. 2 and the Huntington's
  copy reads them (outcome A). Every cipher in the ledger reads from a surviving book: Eckert is parked as an
  edition, and an enquiry went to the Huntington curator about a corpus dataset.
- Process: CLAUDE.md rule 10 (novelty is a verifier's verdict, N0-N5), a Usage section (model tiering, scripts
  over reading, caps), a Pipeline section (scout, check-solved, board, access, solver, verifier, result
  label), an improvement loop (LEDGER.md, brief templates in .claude/briefs/, weekly retrospective every
  Monday 06:00 UTC), a board stage "Novelty verified", kind labels on every card, and the scout rubric's
  new "unread" axis so editions never top the queue again.
- Wellington 1812: HathiTrust half of the dictionary hunt closed negative through the Bibliographic and
  Extracted Features APIs (19 more editions, 76 in all). Blind sweep set the status to partial (Hayes, Lasry,
  Tomokiyo published a partial solution of the system).
- Blind six-source sweep of the board: Hamilton and Stepney offline-only, Whitworth and the 1646 intercepts
  open, nothing already solved anywhere.
- Three new targets verified and filed with REQUEST.md: Stair to Townshend 1710 (Kansas; not in print, so the
  order stands), Monck 1660 (BL), NLS MS 20769 (catalogue record confirmed: 57 leaves, "written in cipher",
  language undetermined, deposited 1949). BL Add MS 72438 f.104 folded into the 1646 target; DECODE marks it
  Decrypted, to be read with the DECODE login.
- Access: the environment setup script now adds the proxy CA to Chromium in every new container (tested);
  NLS is Cloudflare-challenged even so, read via a Wayback capture.
- Free work, 05:02-05:20 UTC, all on Sonnet for about $13 together: (1) print checks found no printed decipher
  or key for Hamilton, the 1646 intercepts or Monck (Burnet 1677 and Google Books were unreachable, so those
  are unchecked, not negative); the archive orders stay the route. (2) A search-print sweep showed three queue
  items already in print in clear (Moray regency 1568-69 in CSP Scotland ii; Throckmorton 1559-63 in Forbes
  1740-41; Sadler 1543 in Clifford 1809): dropped as found-solved, which is a contribution. Rupert 1645 and
  Cornwallis not found; Wotton 1585 and Bowes 1583 sit behind the British History Online paywall; Cobham 1588
  half checked. (3) The queue was re-scored with the unread axis: 39 rows tiered, Eckert dropped as an edition,
  top ten now 1646 intercepts (40), Wellington (40), Hamilton (39), Whitworth (37), Boswell 1628 (36),
  Cornwallis (36), Cecil correspondents (36), Walsingham-Wotton (36), Erving 1807 (35), Randolph 1569 (35);
  every one recovery except Whitworth (contribution). Three of the ten need only the DECODE login to start.

**Waiting on you**

1. Email Spink before 23 Sept: does lot 1184 include a pocket dictionary?
2. Kansas order for Stair MS P556, four scans, about $20 (ciphers/stair-townshend-1710/REQUEST.md).
3. BL Imaging Services quote for Add MS 32093 f.423 (ciphers/monck-1660/REQUEST.md).
4. NLS quote and a five-leaf sample of MS 20769 (ciphers/nls-20769/REQUEST.md).
5. Environment variables DECODE_USER and DECODE_PASS; optionally GOOGLE_BOOKS_KEY; the Gmail connector.

**Waiting on archives:** NRS (Hamilton key sheets), TNA (Stepney page check, order 3660178), the Huntington
(corpus enquiry).

**Stops and costs.** All sessions were stopped by the five-hour usage limit from 00:03 to 18:43 UTC. Worker
usage tonight, in dollars of plan usage (not billed): Eckert 1864 reading 189 (over-ran its brief), verifier
28, key test 26, HathiTrust 11, check-solved sweep 18, scout 6, print check 2, access tests 1, plus the free
work in progress. Orchestrator session 2,042 since 17 Sept. **Nothing here is billed:** this runs on a Max subscription, and these figures are the API-equivalent value of the tokens consumed, which is how the session record reports them. What they measure is how fast a session eats the plan's rate-limit window. The orchestrator is one long session with 3.6 billion cached tokens read, so it consumes more of the window than every worker combined, which is what caused the 00:03 to 03:00 UTC lockout on 20 September. See LEDGER.md.

## How the sessions work

- **Orchestrator:** the Claude Code session titled "Orchestrator". Talk there and only there.
- **Workers:** sessions the orchestrator spawns for one job each, tagged `cipher-lab`, grouped under
  "Cypher Cracking" in the sidebar. Their titles are role first, then the target: "Archive Lookup: ...",
  "Scout: ...", "Image Capture + Transcription: ...". They push their result to this repo and report to the
  orchestrator. You never need to open them. Archive them once their row below says done.

## Targets

| Target | Folder | State | Next action | Whose |
|---|---|---|---|---|
| Charles II to Hamilton, 1650 | ciphers/hamilton-1650 | Copy request emailed to NRS 19 Sept 2026 for GD406/1/2197 (5 key sheets) | Wait for NRS quote; pay; when images arrive, commit them or paste them to the orchestrator for transcription and decoding | NRS, then you, then orchestrator |
| Stepney to Manchester, 1702 | ciphers/stepney-manchester-1702 | TNA page check ordered and paid 19 Sept 2026, order 3660178, SP 105/65 | Wait for TNA's quote for the copy; pay; when the copy arrives, commit it or paste it to the orchestrator | TNA, then you |
| Wellington to Maitland, 1812 | ciphers/wellington-maitland-1812 | Transcribed 19 Sept 2026. Dictionary search closed on 20 Sept 03:37 UTC: 76 editions tested (57 Google/IA, 19 HathiTrust via APIs), none matches; Scott, Jones 1800, London Perry, Walker 1810, Dublin Entick not in HathiTrust | You, before 23 Sept: email Spink asking whether lot 1184 includes a pocket dictionary. Library leads: Urban pp. 232-233, Bentinck papers, WO 37 | You |
| Whitworth to Harley, 1707-08 | ciphers/whitworth-1707 | Verified 19 Sept 2026: plaintext of the SP 91/5 'undeciphered' items is in print (Sbornik IRIO 39 and 50) except one clause of f. 108. Copy request drafted for ff. 108, 106, 121 | Order the three items from REQUEST.md (about 10 images) | You |
| Eckert Papers, US Military Telegraph 1862-67 | ciphers/eckert-1862, ciphers/eckert-1864 | Parked 20 Sept 2026. 1862: ten entries read at grade C. 1864: twenty entries read at grade H from Cipher No. 1 and three from Cipher No. 2, both surviving books; audit (AUDIT.md): E6, E12 already in print (N1), E4, E5 no prior print located (N3). No cryptanalysis left. Enquiry sent to the Huntington curator 20 Sept about a corpus dataset; reply decides the corpus pass | Wait for the reply | Archive |
| Earl of Stair to Townshend, 1710 | ciphers/stair-townshend-1710 | Verified 20 Sept 2026 (KU catalogue, six-source sweep): open, English | Not in print (checked 20 Sept). You: order four scans from Kansas per REQUEST.md, about $20 | You |
| Letter relating to Gen. Monck, 1659-60 | ciphers/monck-1660 | Verified 20 Sept 2026 (BL catalogue, sweep): open, English | You: ask BL Imaging Services for a quote for Add MS 32093 f.423 (REQUEST.md) | You |
| NLS MS 20769, 18th-c. cipher manuscript | ciphers/nls-20769 | Record read 20 Sept 2026: 57 leaves, "written in cipher", genre Ciphers. Codes., language undetermined, deposited 1949 | You: ask NLS for a quote and a five-leaf sample (REQUEST.md) | You |
| Thomas Randolph to Sussex, 1570 | ciphers/randolph-sussex-1569 | **Found-solved, 23 Sept 2026.** f.278 is a clerk's contemporary decipherment (DECODE R4932), read by Bourdeau 21 Sept; Boyd 1903 no. 339 says 'deciphered'. Images, 49 native crops and two raw passes kept for the record; dropped from the queue | found-solved |
| Everything else | QUEUE.md | First scout run done 19 Sept 2026: 40 scored, 163 kept unscored, 40 dropped | Work down the queue | Orchestrator |

## Results so far (labelled per README "What counts as a result")

| Target | Kind | Result |
|---|---|---|
| Eckert Papers 1862-67 | Contribution | Machine-readable Cipher No. 1 and No. 2 keys, 23 readings checked against print, AUDIT.md with N-classes, corpus-status finding; offered to the Huntington 20 Sept 2026 |
| Whitworth 1707 | Contribution | Four of five catalogue "undeciphered" items shown to be already in print (Sbornik 39, 50); one clause of f.108 open |
| Hamilton 1650, Stepney 1702, Wellington 1812, 1646 intercepts | Recovery (in progress) | Key hunts; nothing read yet |
| NLS MS 20769 | Cryptanalysis (candidate) | Pending catalogue confirmation |
| Stair 1710, Monck 1660 | Undecided | Depends on what the scans show |

## Worker sessions

| Session title | Job | Result | State |
|---|---|---|---|
| Archive Lookup: Stepney 1702 (blocked, done) | Find the 1702 volume | Blocked by the old "Trusted" network policy; logged | Done, archive |
| Archive Lookup: Stepney 1702 (done) | Same, after the policy change | Found SP 105/65, record C3609655; REQUEST.md updated | Done, archive |
| Scout: queue builder (done) | Refresh the snapshot; build the ranked queue | Cryptiana unchanged. QUEUE.md written: 40 scored, 163 unscored, 40 dropped. Interrupted 22:15 UTC after it began attempting ciphers beyond its brief | Done, archive |
| Image Capture + Transcription: Wellington 1812 | Capture auction images before 23 Sept sale; transcribe | 17 images, full transcription, pass A log pushed | Done, archived |
| Research: Wellington 1812 dictionary edition | Test pocket dictionaries against the 57 code groups | 57 tested, not found, three near misses; pushed 466cf27 | Done, archived |
| Archive Lookup + Transcription: Eckert Papers 1862 | Zooniverse coverage check; read ten telegrams | Pushed 2d54f06: never decoded by Zooniverse; ten 1862 entries read at grade C | Done, archived |
| Scout: verify and file four proposed targets | Stair 1710, Monck 1660, NLS 20769, 72438 f.104 | Stair and Monck open (English); NLS unverified; f.104 marked Decrypted on DECODE | Done, archived ($6) |
| Print Check: Stair 1710 in Graham's Annals | Free check before the Kansas order | Not in Graham 1875, HMC 11th Report or Marlborough despatches | Done, archived ($2) |
| Access Test: browser tool after the setup-script fix | Prove the fix in a fresh container; read the NLS record | Fix works; NLS record read via Wayback (live site Cloudflare-challenged) | Done, archived ($1) |
| Check Solved: blind six-source sweep of five targets | check-solved workflow, Sonnet | Hamilton, Stepney offline-only; Whitworth, 1646 open; Wellington partial. Nothing found solved | Done, archived ($18) |
| Key Test: Eckert 1864 headquarters cipher (mssEC 47-48) | Test Cipher No. 2 on the Beckwith/Kimber entries | Outcome A: mssEC 47 reads them at grade H; key-no2.md, reading-no2.md | Done, archived ($26) |
| Verifier: prior-art audit of four Eckert 1864 telegrams | Disprove the "not printed" claim; N0-N5 class per message; correct wording; CLAUDE.md rule 10 | Pushed: E6 N1 (OR I/32 pt 3 p.498), E12 N1 (in print since 1864; Basler CW 7:479), E4 N3, E5 N3; AUDIT.md written; over-claims corrected; verifier template added to CLAUDE.md | Done |
| Transcription + Reading: Eckert 1864 ledger with Cipher No. 1 | Twenty 1864 entries at grade H | Pushed 045fbe2: all twenty read cleanly (296 H, 8 C, 1 M, 0 I); four not found in the OR volumes checked | Interrupted 03:06 UTC, archived 03:15 (result pushed; it had started a duplicate audit, $189 of usage) | Archived |
| Access: HathiTrust dictionary search via browser (Wellington 1812) | Test tools/browser_fetch.js; run the DICTIONARY.md section 6 searches | Chromium blocked by proxy CA; HathiTrust APIs used; 19 editions, none match | Done, archived ($11) |
| Archive Lookup: Whitworth 1707 | Search-print check; list items; REQUEST.md | Only one clause of SP 91/5/108 unread; ciphers/whitworth-1707 committed | Done, archive |

## Environment

- Cloud environment "Default" now has full network access (changed 19 Sept 2026). New sessions can reach
  archives and Cryptiana. The original orchestrator container predates the change and cannot; it delegates.
- Repo conventions: CLAUDE.md. Workflows: .claude/workflows/check-solved.js and scout.js.

## LANE G3 handoff (24 Sep 2026 14:02 UTC)

Written by LANE G3 orchestrator session_01WVnAc4cU7RQjEoBfbkuGrG (Opus), about $13 own usage, from 12:03 UTC. Stopped early: the account shows
**allowed_warning on the seven-day window** (LANE N2 13:50; resets 26 Sept 2026 13:00 UTC), which under BUDGETS' scaling rule means no new
workers anywhere. **Live workers: none.** 8 workers, $36.85 of worker usage; all ledgered, ASSIGNMENTS rows done, archived.

**Done this lane:**
- fr5160-letellier-1653: code 6 on f.67 is a real 6 on 8/8 image-checked tokens, so a table revision between 10 Oct and 21 Nov 1659, not a misread;
  grades unchanged (C454 M92); _12 is a clear overlined 12, so the ri conflict stands (A, 963dee8).
- decode-2754-bnf-baluze156-1636 (DC8): Lasry's Sabran 1631 key negative on both halves with controls (results row). Untested: Farnese f.40 key,
  fr.4135-4138 keys, fresh solve (crib: repeated '7 4 t o') (C, cf17087).
- fr2967-duprat (M30): all 131 canvases walked, decipherments only, no ciphertext: closed-negative (D, 293b1a2).
- Scout round 6: a real browser pages archivesetmanuscrits past page 1 (results vary run to run: run each query twice). 2 rows:
  M35 fr2933-salviati-1525, M36 fr5761-election-1519, both check-solved open (stage 2), both digitised (B, E).
- fr2933-salviati-1525 (M35): 9 leaves f.54r-57v on disk (canvases 55-59); letter mixing plain Italian, numeral groups and invented signs with
  superscript marks. Glyph atlas of 40 codes (tools/glyph_atlas.py + test) covers 3068 of 4014 signs; atlas passes of f.54r agree 62.8% on
  base codes, under the 80% gate. Confusions eps/e, h/bh; 57 of 130 disagreements are gaps (F, H).
- fr5761-election-1519 (M36): natives of the key f.50v-53v on disk, one pass (key_passB.tsv, 319 rows, word descriptions); worker interrupted at 1.9x cap.

**Owner items (unchanged, not ours to act on):** ASKS 35 and 38, five BnF reproductions, each with a REQUEST.md.

**Next for a successor, once the warning clears (priority):** (1) Salviati: revise the atlas to split eps/e and h/bh, then two atlas passes of
f.54r against the 80% gate (disk only, Opus lead with Sonnet passes, cap $6); (2) M36 key: atlas for the alphabet signs, then two atlas passes
of f104 (disk only); (3) the verifier gap for both: Desjardins' Négociations avec la Toscane not full-text searched; (4) DC8 Farnese key trial.
Gallica hosts are released.

**Lessons (ledgered; transcription.md edited):** the atlas is required whenever any non-numeral sign appears, mixed pages and keys included
(two workers skipped a conditional atlas step and wasted their passes); one-question image checks are the cheapest brief shape ($1.38).

## LANE G2 handoff (24 Sep 2026 11:56 UTC)

Written by LANE G2 orchestrator session_015NqJ9uu5Ef3Bo6QaRiGcGp (Opus) at about $72 of its own usage and 440k context, from 07:43 UTC.
Lane = Gallica digitised manuscripts; the only lane on gallica.bnf.fr and archivesetmanuscrits.bnf.fr, at most two fetching workers at a time.
**Live workers: none.** 29 workers collected, ledgered (Session column), ASSIGNMENTS rows done, archived.

**Results this lane produced (status.json rows; classes are the verifiers'):**
- clair1067-brienne-poland-1646: key_1646 from the interlinear decipherment, C307 M31 of 338; N0 (LANE V); status solved.
- clair1108-duvergier: interlinear decipherment found by the reconciler, key_1696 129 codes, C584 M82 U1 of 667; N0 (LANE V2); status solved.
  fol.249r is show-through of 249v, no cipher. Open: 9 groups of letter B; fol.247v (canvas 251) native is only in a dead worker's
  scratchpad (re-fetch command in images/manifest.json).
- fr5160-letellier-1653: folio 67 (10 Oct 1659), a letter found by the canvas walk, read with key_1659 and then aligned to its own clear
  text on f.68r: C454 M92 of 546; N0 (LANE V2). key_1659_ext +16 codes; code 65 = ma everywhere; code 6 is qu on f.86/f.88 and a on f.67
  (compare the canvas 129 native with crops/f86_cipher_L08.jpg to settle table change vs misread); _12 = ri is a new conflict row.
  1653 band: negative with controls (1646/1647/1651 keys lose to 200 derangements; constrained anneal reads 25.7% of a same-size synthetic).
  Canvas 32 and the canvas 11-12 block have two passes each, not reconciled (low value while the 1653 table is unreadable). The whole
  volume (367 canvases) is walked; no further cipher. No sibling volume in 1653-61 carries a cipher note (sources/solver-diffs/...-servien.tsv).
- fr2980-gramont: Tb=O and q=B at S in the extended f.30 reading (H1486 S181 M239 U63); L12 French with gaps; L01, L02, L11 still not.
  f.29r not extended with Tb=O (+18 bits there; would need a note, the leaf is at N4).

**Queue rows (Gallica round 4, M22-M34) and their state:** M23, M22, M24, M25, M28 not digitised -> blocked, REQUEST.md, ASKS 35 and 36
(one BnF reproduction order). M31 found-solved (Tomokiyo/Ryabov 2025). M32 fr.2751 and M33: decipherment only, no ciphertext (found-solved /
dropped). M29 Portugais 33: register copy in clear, closed-negative. M30 Duprat: decipherments without ciphertext in the leaves viewed
(~120 canvases unviewed). M26 Paget 1713 not found in 316 canvases of Clairambault 296 (M4 Paget 1714 is the same correspondent). M27 open,
held for duplicate risk (Estrades keys 1647-53). M34 is Espagnol 144, 1648 item unpinned. Round 5: zero new rows; archivesetmanuscrits
pagination past page 1 fails for curl (a browser_fetch.js worker could page the capped terms 'chiffre', 'en chiffre', 'avec chiffres').
DC8 Baluze 156: passes 87.6%, Sabran-1631 key negative with control on the numeral half, letter-symbol half untested. DC9: agrees with Bourdeau.
DC1 (LANE R2): Gallica images of fr.20506 f.136 and fr.2988 f.9 delivered.

**Lessons (ledgered):** capture briefs one target, strict cap, stop a Gallica endpoint after one retry (manifest/services endpoints reset
all day; the direct image endpoint works); check digitisation and actual ciphertext at scout time ('déchiffrement' items, register copies and
Arsenal manuscripts mostly fail); ask every reconciler whether clear text over the groups is a contemporary decipherment (it turned
clair1108 from cryptanalysis into recovery); a cheap lookup worker answering a verifier's question moved f.67 from N3 to N0 in 12 minutes.

**Next for a successor (priority):** (1) the fr5160 code 6 image compare (one native); (2) a browser-tool scout for the capped
archivesetmanuscrits terms; (3) M30 Duprat remaining canvases for ciphertext; (4) M4+M26 Paget if M26 is found; (5) DC8 letter-symbol half
from Lasry's Sabran key (fr.4134/4135).

## LANE G handoff (24 Sep 2026 06:39 UTC)

Written by LANE G orchestrator session_014zWyan51u9qMn9gnHpm1Aq (Opus) after about $70 of its own usage and 460k context, so a
fresh successor is cheaper than continuing. Lane = Gallica digitised manuscripts; the only lane that fetches gallica.bnf.fr and
archivesetmanuscrits.bnf.fr, at most two fetching workers at a time. Ceiling 10 live workers (cipher-lab-7a, 06:34), Sonnet
wherever another agent checks the output; the window to 11:10 UTC has to last.

**Running at handoff (collect, ledger with Session column, archive):**
- session_01NxF8TAcCGzJU1ALyEFgBLu (Opus $10): M18 clair1067-brienne-poland-1646, transcribe the interlinear words over every
  cipher line and align them (key_1646, strict grade C). Gallica fetcher, at most 4 requests.
- session_014nQmWbnuGDe8bA33EKB1uP (Sonnet $6): fr5160 1653 band, missing natives + folio 9 pass B. Gallica fetcher.
- session_01WjZ6hbafTnrCNGFEgc67M1 (Sonnet $5): clair1108-duvergier, finish pass A, blind pass B. Disk only.

**Target state:**
- fr5160-letellier-1653 (Brienne to Servien). 1659: f.86 and f.88 read with key_1659 (79 groups, grade C) from f.87, the
  contemporary decipherment of both; LANE V class N0; recipient is Ennemond Servien (Abel died Feb 1659). 1653 band (a different
  symbol+numeral table, Brienne family): folio 1-2 letter reconciled (ciphertext_f1.tsv, 528 tokens H508); folio 9 passes
  finishing. Tomokiyo's 1647/1651 keys lose to a shuffled control on it. Next: once M18's key_1646 exists, trial it and the
  1647/1651 tables on ciphertext_f1 and the folio 9 letter with a control; the unsampled canvases 37-159 may hold more letters.
- clair1067-brienne-poland-1646 (M18). Leaf fol.226r-228v on ark btv1b90008551 (the other ark's foliation stops ~fol.205).
  338 tokens reconciled; same family as the 1647/1651/1653 tables, different table; interlinear words in a heavier hand over
  every cipher line: treat as a recovery; aligner running. Hand the reading to LANE V.
- clair1108-duvergier (M19). Cipher on 4 leaves (f.247v; 249r-250r, 26 Mar 1696; 262), clear French with a numeral
  nomenclator; probably Jacques Vergier (Marine, Dunkerque) to Pontchartrain; no key or printed edition found; the other side is
  AN Marine B2/B3. Next: Opus reconciliation when passes land; a single letter of a large nomenclator is likely below
  unicity, so look for the Marine key before any solver.
- fr2980-gramont: f.29r and f.30 N3 two audits (LANE V). f.30 extended reading H1502 S159 M245 U63; f.30r L01, L02, L11, L12
  still do not read (clear signs, key or nomenclator gap). Champollion-Figeac and the whole Camusat Francis I tract are
  checked negative; the remaining N4 family is DECODE (LANE N).
- fr20140-danzay-1557: f.35-36r read to the end (N3, two audits, LANE V); f.36v is the address panel. Nothing left for LANE G.
- fr4687-paleologue-nevers: parked. 900 signs, clean negative with matched controls (99.8/93.6/86.4/70.0% at 0-15% noise);
  untested: nomenclator design, Mantuan model, third reading of the 16% M signs.
- fr16092-maisse-1582: held. No ciphered leaf found in fr.16092 or in Maisse's own registers fr.16089-16091 (78 canvases).
- Queue: M17 not taken (Tomokiyo published the key and photographed the letter); M20 unattributed, no folio map; M21
  Rousseau corpus edited four or more times. No Gallica scout since round 3 (M17-M21); a round 4 is the next source of rows.

**Lessons for the successor:** never call list_sessions (a page is 50-80k characters; use get_session or archive_session);
Gallica .texteBrut is altcha-walled, IIIF page images are not; tell solvers to run long jobs in the foreground (two Paleologue
solvers went idle with background runs); commit per pass so a rate-limit stop loses nothing; "9.bre" is novembre.

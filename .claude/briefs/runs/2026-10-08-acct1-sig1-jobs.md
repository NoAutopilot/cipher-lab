# LANE SIG-1 worker jobs (account 1, lane orchestrator session_01Sj9f3TAuMmxN1jSoXezro8; written 8 Oct 2026 22:4x UTC by date -u)

Lane brief .claude/briefs/lane-significance.md (+ lane-common-blast.md). First incarnation: no earlier "LANE SIG handoff" in STATUS.md.
Every ROOM line ends "for LANE SIG-1 (account 1)". Judge every result by what it adds to the letter's content, not by count
(research/SIGNIFICANCE-2026-10-08.md).

Intake gates (pasted 22:44 UTC, all exit 0):
`baluze167-davaux-1637: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`fr2980-gramont: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`;
`lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`august-van-saksen-1561-64: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.

**Common to every worker**
- Read CLAUDE.md, .claude/briefs/prior-work-step.md and your target's NOTES.md sections named below. Run
  `python3 tools/prior_work.py <slug> --item-spec '...' --step-type <type> --fetch` before the first priced step and obey its exit code
  (paste its output into your NOTES section); where it does not reach, run checks 1-4 by hand, one pasted line per check.
- `date -u` before any time; ROOM claim with box end time, a halfway line, a done line (`python3 tools/room.py "<role>" '<text>' --push`,
  single quotes); commit and push every two units; stop before a unit that would cross 80% of cap or box (Usage 6: units x per-unit rate
  is stated in each job; a transcription subagent call gets line crops only, never a full page). Rule 10 and rule 4a wording only; never
  "new", "first", "solved". Never call AskUserQuestion; never print credentials; never name the owner.
- Images: read from disk. Gallica answered 403 to every cloud session on 8 Oct -- no Gallica request in this wave.
- Rule 3: every gate is pre-registered in a committed file BEFORE the target is scored, with a control that can fail differently from the
  target on the statistic computed. Rule 7: decode script with --check, exit 0, pasted.
- file_shrink_guard on every touched file before the final push; `python3 tools/gaps_check.py <target>` after NOTES (paste result).
- Solvers: report what was found and where it was not found; do not classify novelty.

---

## SIG-B228 (Opus 5.5, solver; cap $6, box 90 min, no network): Baluze 170 f.228r-v -- value the 7 unvalued shapes and the unmarked numerals, re-judge
Target baluze167-davaux-1637. Read NOTES "## B167-228 solver" and its Remaining gaps (gap 2), "## D4-B167", "## D4V-B167", "## D1-BAL170", "## D1-BAL170B".
Item spec: `shelfmark=BnF Baluze 170;folio=228r;date=1640-08-25;sender=Chavigny;recipient=Avaux` (adjust the date to what NOTES gives for f.228; step type `transcribe`).
1. Pre-register (commit `b167228/prereg_sig.md` before any value is looked at in f.228 context): a shape gets a letter value only from an
   external exemplar -- Tomokiyo's letter block (`images/louisxiii_davaux.png`, sources/cryptiana/web/louisxiii.htm) or a glossed f.229/other
   glossed-leaf occurrence of the same shape -- never from f.228's own context (the ARM-C1 shape; B167-228 already refused q = c on that
   ground). Rule: two independent blind Sonnet reads of the exemplar sheet vs the f.228 tiles must name the same exemplar; else the shape stays U.
2. Units: shape tiles for q 6, ll 4, g+ 3, ff_crossed 2, ll|u4 1, v 1, wave 1 cut from `images/crops/b170f228*` (local PIL crop or
   `tools/iiif_lines.py --image`), one tile sheet per shape group; and the 27 unmarked numerals (b167228/key_unmarked.tsv) re-checked for an
   accent on the native crops. About 6 Sonnet calls (3 shape-sheet pairs x 2 blind reads) + 2 numeral-mark calls + 1 reconciliation by you,
   ~$0.6 per call.
3. Decoy control inside the sort: include 3 already-valued f.229 shapes (e.g. hook s, gam u, y+ r) as unlabelled tiles; the gate needs
   >= 2 of 3 decoys matched to their right exemplar by both reads, or no shape value is adopted.
4. Apply adopted values through key files / exceptions (never hand-edit a reading), `python3 tools/decode_key.py ciphers/baluze167-davaux-1637 --check`
   (exit 0), then re-run `b167228/judge_null.py` unchanged (fr17, same 40 nulls, same 3-segment positive control) and paste the table beside
   B167-228's (-0.993 vs real_p05 -0.887). Re-check Tomokiyo's f.228 fragment "sont mal satisfaits de" against the new reading.
5. NOTES "## SIG-B228 (8 Oct 2026, account 1, for LANE SIG-1)": counts H/C/S/M/I/U before and after, the judge table, what f.228 now says
   (one paragraph, M-graded words marked), Remaining gaps / Escalation. Do not classify; the lane sends any reading that clears the judge to a
   separate verifier.

## SIG-GRA30 (Opus 5.5 with Sonnet reader subagents; cap $10, box 150 min, no network): fr.2980 f.30r-v -- native re-read of the worst lines, decode, control
Target fr2980-gramont. Read NOTES sections on f.30 (reconciliation_f30.md, "f30r_top", the eh/CROSS split, R12D-GRAZB2, Remaining gaps) and
TRANSCRIPTION.md. Item spec `shelfmark=BnF fr.2980;folio=30r;date=1530-05-20;sender=Gramont;recipient=Francis I`, step type `transcribe`.
Scope: NOT L01, L02, L11, L12 or the open-code positions of Remaining gaps (instrument retired; a re-read cannot key HASH/TRI/INF/B8/ev).
1. Choose lines by script, before looking at images: from reading_f30_extended_tokens.tsv rank f.30r/f.30v lines by (M + U tokens) and by
   fr16 line score (linescore_f30r_top.tsv's scorer or tools/judge_plaintext.py per line); take the worst 8 lines outside the excluded set.
   Commit the list and the gate (`n12gra/` style folder `sig30/prereg.md`) before any pass.
2. Control (known answer, same hand, same protocol): 2 lines of fr.3040 f.18r from `images/fr3040_f18/` whose text is fixed by Le Grand III
   pp.454-457 (N9-GRA4 alignment). The same two blind passes + reconciliation; decode with key.tsv; per-sign agreement with Le Grand.
   Gate (pre-registered): the control's keyed-sign agreement must be >= the N9-GRA4 figure for those lines minus 0.05, else stop: the protocol
   is not better than what is on file and no f.30 change is applied.
3. Target: two blind Sonnet passes per line (one call per line = its two half-crops from `images/crops_f30/`, with the legend sheet
   `legend_sheet.png`), reconciliation by you from the crops; a sign changes only where both passes agree against ciphertext_f30.tsv or
   your crop check settles a split. Units: 8 lines x 2 + 2 control lines x 2 = 20 calls at ~$0.35, + reconciliation ~$1.5.
4. Apply through ciphertext_f30.tsv (log every changed sign with before/after and evidence in `sig30/changes.tsv`), then
   `python3 ciphers/fr2980-gramont/decode.py --check` and `python3 tools/decode_key.py ciphers/fr2980-gramont --check` (both exit 0).
   Score the 8 lines before/after with the same fr16 line scorer AND a shuffled-change null (apply the same number of sign changes at random
   positions of the same lines, 200 draws): report the real gain against the null's p95 -- a gain inside the null band is "no change", not a
   gain.
5. NOTES "## SIG-GRA30 (8 Oct 2026, account 1, for LANE SIG-1)": changes, counts H/C/S/M/U before/after, the control and null numbers, the
   8 lines as read before and after, what they now say (rule 4 grades marked). Remaining gaps / Escalation.

## SIG-4612 (Opus 5.5, solver; cap $5, box 100 min, no network): Lodewijk van Nassau WVO 4612 -- word-unigram-LM global anneal behind its null-start pre-check
Target lodewijk-van-nassau-1573-74. Read NOTES Remaining gaps item "4612 cipher body", "## GAPS43" (gaps43/word_anneal.py, PREREG.md,
control.json), HYPOTHESES.md rows for 4612. Item spec `shelfmark=KHA A 11;wvo=4612;sender=Lodewijk van Nassau;recipient=Willem van Oranje`
(date from NOTES), step type `key`.
This is the step NOTES names: a different objective from GAPS43's word segmentation (rule 3 third-attempt clause: different instrument, allowed once).
1. Objective: fr16 word-unigram log-probability of the best segmentation (Viterbi over tools/data fr16 word counts) with a per-character
   out-of-vocabulary cost; nulls 121-138 dropped as in GAPS43. Implement as an `--objective unigram` option in gaps43/word_anneal.py (keep the
   old objective as default), with an offline test.
2. Pre-check (pre-registered in `gaps43/PREREG-unigram.md`, committed first): on the 5811 cut (N=833), key_full must score better than the
   optimum the anneal reaches from a null start (unperturbed key_full start included); if not, stop -- "untested-by-this-tool", target not run.
3. Gate: the same 20%-perturbed key_full control, 3 seeds, recovery >= 0.90 each. Only on PASS run 4612 v3 (ciphertext_4612_v3.tsv) from
   key_full and from 3 perturbed starts; report the French-word share against the shuffle max (60.6%) and the 79.2% bar, and fr16 judge.
4. Units: pre-check ~$1, control 3 seeds ~$1.5, target ~$1; CPU in this container only, serial (no concurrent background band).
5. HYPOTHESES.md row(s) with both numbers; NOTES "## SIG-4612 (8 Oct 2026, account 1, for LANE SIG-1)"; Remaining gaps item updated.
   Any reading produced: decode script with --check; do not classify.

## SIG-AVS (Opus 5.5; cap $3.5, box 75 min): August of Saxony -- the Qf shape sort in WVO 126 and the 74 p3 l.10 idx 6 re-look
Target august-van-saksen-1561-64. Read NOTES Remaining gaps (126 Qf item), "## R12A-AVS175", "## RUN6-AVS62", "## Keyhunt 7 Oct 2026".
Item spec `shelfmark=SHStA Dresden Loc. 8510/5;wvo=126;date=1564-09-16;sender=Willem van Oranje;recipient=August van Saksen`, step `transcribe`.
Context for you: every WVO August<->Willem letter with cipher in 1561-64 is already in this folder (KH1-D); this job is the two small
image steps the folder names, not a search for more letters.
1. **Huygens host token:** before any request to resources.huygens.knaw.nl, `git fetch -q origin main && git show origin/main:ROOM.md | grep -i "huygens take\|huygens release" | tail -4`;
   if the newest is a `take` by another worker < 40 min old with no later release, wait (Monitor/background loop, no foreground sleep, up to
   30 min). Then `python3 tools/room.py "SIG-AVS" 'huygens take (<=3 requests)' --push`, fetch 00126.pdf, 00098.pdf, 00074.pdf (>= 2 s apart,
   scratch only, manifest entries only), `... 'huygens release (N requests)' --push`.
2. Qf: blind shape-identity sort of 126 L1 pos 20 against 126's own Pf exemplars, with f.66's Qf/Pf pair as control (pre-registered first:
   the control pair must sort correctly in both of two blind Sonnet reads, else Qf stays M). 2-3 calls.
3. 74 p3 l.10 idx 6 (T? vs n) and f.19 l.13 ("machen sich keinem" vs Rachfahl's "möchten wohl leiden"): native crops, two blind reads each. 2 calls.
4. Apply through ciphertext/exceptions files, `python3 tools/decode_key.py ciphers/august-van-saksen-1561-64 --check` exit 0; NOTES
   "## SIG-AVS (8 Oct 2026, account 1, for LANE SIG-1)"; Remaining gaps updated.

---

## AUD-SIG-CHAV (account-3 VERIFY lane; Opus 5.5, verifier; cap $5, box 75 min) -- step type `new-family-audit`
baluze167-davaux-1637, Chavigny to d'Avaux, Amiens, 25 Aug 1640 (Baluze 170 f.229r-v), N3 D2 after AUD1-B167 + AUD2-B167. The two source
families both audits left open (research/SIGNIFICANCE-2026-10-08.md "Checks still owed"; AUD2-B167 "not N4: Hessian-side editions, AAE"):
(a) the Archives des Affaires étrangères, Correspondance politique (Allemagne / Hesse / Suède 1640): the published inventories and any printed
selection (e.g. the Acta Pacis Westphalicae preliminaries, Avenel's notes citing AAE CP volumes for Aug 1640), searched for a clear copy or
minute of the Chavigny despatch of 25 Aug 1640 or its Eberstein/Salvius clause; (b) the Hessian side: Rommel's Geschichte von Hessen VIII,
the Melander/Eberstein literature (Hessian army command 1640), Amalie Elisabeth editions, for France's promised reward to Eberstein in Aug 1640.
CLAUDE.md verifier template steps 2-5; JSTOR rows to JSTOR-QUEUE.tsv in both families (i) and (ii). Write AUDIT.md "## AUDIT 3 (AUD-SIG-CHAV)";
the class may stay, rise or fall; carry any change into status.json and the SO row (rule 10 propagation). Add one line, written by you, to
research/SIGNIFICANCE-2026-10-08.md "## Lane SIG additions": what the passage says, what it adds beyond print, the caveat (rule 10 wording).

## AUD-SIG-E146 (account-3 VERIFY lane; Opus 5.5, verifier; cap $3, box 60 min) -- step type `new-family-audit`
eckert-1864 E146 (Quartermaster General's office to Allen, Louisville, 12 Dec 1864: Donaldson's recommendation that the military railroads
take over the Louisville and Nashville), N3 weak after FV-LS5-B + AUD2-LEDGER-2. Owed family: the railroad's published histories --
Lee (2011) on the L&N, Klein's History of the Louisville & Nashville Railroad (1972), Herr's Louisville & Nashville (1943), and US Military
Railroads reports (McCallum's 1866 report; Donaldson's own QM reports for 1864-65 in the QMG annual report / OR ser. III vol. 5) -- searched
for the Dec 1864 seizure proposal. Same template steps; AUDIT.md section "## AUDIT 3 (AUD-SIG-E146)"; propagation; one line in the
"## Lane SIG additions" section as above.

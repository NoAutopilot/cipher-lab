# Scout-plan jobs (account-3 orchestrator, 8 Oct 2026 01:3x UTC). From workflow wf_e0950d6a-d50: six read-only scouts, a planner, an adversarial critic; briefs below are the critic-revised text.
Every depth ruling uses .claude/briefs/runs/2026-10-08-acct3-depth-bar.md (overrides any inline DEPTH BAR text below if they differ).
Expected counted gains are low (0.1-1 each): these keep accounts 1/2/4 busy on the best available odds; report honestly either way.


## DEPTH-MH
# DEPTH-MH (account-3 orchestrator, 8 Oct 2026 01:1x UTC). default-lane common tail; Opus 5.5 (depth-regrade verifier).
Rule-4a depth re-check of two counted-class rows that the 4 Oct bulk pass held at D1. Neither row has AD or code-recurrence evidence on file.
- ciphers/sachsstaatsarchiv-manteuffel-1712: SHStA Dresden Loc. 694/08 f.410 P.S., Manteuffel to Flemming, Nov 1712. N4, two audits, D1 at 66.7%. Key published (Krauske 1893); agrees 17/17 with the f.468 period glosses.
- ciphers/hellen-frederick-1752: DECODE R1953, Hellen to Frederick II, 4 Jan 1752. N3, two audits, D1 at 53.9%. Key period (R4369).
Add-on: ciphers/fr3416-nevers-fils-1589 f.35r (N4; D07-NEVFV held D1 on 7 Oct).
You are separate from every solver of these items, and from DEPTH-REGRADE (session_015eezFKYThEoRKoeamyhxSD), R9-MANTV, VHEL, A3V-VHEL2 and D07-NEVFV (session_01US4m8bWufn8tBfr1swic9c).
- Do not decode. Do not change a key, ciphertext or reading.
- Do not adopt the R7A-HEL53/R8-HEL image corrections. That is a solver step, named for later.
- Leave the N-class untouched.
Read first:
- each folder's AUDIT.md depth sections, its status.json row and its NOTES Remaining gaps;
- CLAUDE.md 4a;
- research/DECIPHERMENT-STANDARDS-2026-10-04.md section 3 and step 3a.
Paste `python3 tools/intake_gate_check.py <t>` for all three.
Common (.claude/briefs/README.md common tail):
- `room.py --start`, then a claim naming the cap and box end;
- `date -u` for every time;
- rebase before writing status.json, AUDIT.md, SO rows or ROOM, and keep both facts on a conflict;
- run tools/file_shrink_guard.py on every touched file and paste the output in the done line; push with `room.py --push`;
- no AskUserQuestion; cost is the orchestrator's get_session figure.
Stop before starting a unit that would cross 80% of cap or box.

DEPTH BAR. The orchestrator fixes this bar for every depth ruling tonight; DEPTH-BIR117, AUD2-WVO11008 and AUD2D-OLD2442 use the same text. Copy it into the PREREG before computing anything.
- CLAUDE.md 4a governs where it differs from the research note.
- Cipher clause: a contiguous H/C/S stretch longer than the authentication distance (AD) for the design, about 1.5 x unicity.
  - H(K) = the design's key space plus every liberty the reading took: U wildcards, M tokens, r|re|ro and o|ou|ous choices, repairs.
  - An unfitted external or period key does NOT shrink H(K) to the liberties alone.
  - The zero-liberty (H_lib+20)/R reading (about 6-8 letters here) is not used.
- External check: an external check (key agreement with period glosses, a period key sheet) is a D3/D4 element under CLAUDE.md 4a. It does NOT replace the clause at D2, although research section 3 offers it as an alternative.
- Code clause: a code value that reads sensibly in >= 2 independent contexts.
  - An H or C grade on the value does not satisfy this on its own, although research section 3 says 'or carry H/C grade'.
  - A verbatim repeated phrase counts once (lodewijk precedent).
- D2 = one clause plus your own true, specific sentence about the content, written from the reading. Droysen or Fagel 5177 may confirm the sentence, never supply it. Otherwise hold D1.
- If you think the convention is wrong, post one ROOM flag for the parent and still rule under this bar.

UNITS. Usage 6 estimates: about $2.5 per main item, about $1.5 for the add-on, about $1 for the write-up, plus the Opus floor.
0. Write PREREG-DEPTH-MH.md in each folder: the bar, the statistics, the control and the decision rule. Push it before any statistic. About 0.5.
1. Manteuffel f.410. About 2.5.
   - Rule 7: `python3 tools/decode_key.py ciphers/sachsstaatsarchiv-manteuffel-1712 --check` must exit 0.
   - One script over reading_tokens.tsv computes three things:
     - per line, the longest H/C/S runs, with liberties counted;
     - the AD under the bar, with R from tools/data/fr18;
     - the code values recurring in >= 2 non-duplicate contexts (217 'la reine d'Angleterre' C x3; 390 Stettin).
   - Matched control (rule 3). It must be able to differ from the target. Grade runs and recurrence counts do not depend on the key, so a shuffled key cannot move them. Use two key-dependent statistics instead:
     - (i) the longest stretch that segments into fr18 words;
     - (ii) for each recurring code value, the fr18 n-gram score of a +/-8-letter window in each context.
   - Compute (i) and (ii) on the target and on 200 value-shuffled-key decodes (VERIFY-MANT's shuffle design, key classes kept). Report the target, the shuffle p95 and the max.
   - The fr18 judge FAIL near its gate is the ZX-DEC349 shape (the f.467 gloss scores -1.417). Treat it as 'cannot decide', not as a depth argument either way.
2. Hellen R1953. About 2.5.
   - Rule 7 first: key_r4369/rederive_helrd.py, or tools/decode_key.py on key_r4369/decode.json with --check.
   - Run the same script on key_r4369/reading_R1953_tokens.tsv. Candidates: 884 'prince de' H in 5 contexts, 863 'province' H x2, 825 'quoique', 1257 'nouvelle' S x2. Drop verbatim repeats such as 're et quoique sur les ex' (x2).
   - Control: recompute statistics (i) and (ii) under 200 value-shuffled R4369 keys (the LR100 shuffle design). The 'p 0/200' on file was computed on a different statistic; do not reuse it as this control.
   - key_rebuild/fagel_corpus_H.txt may be used to check context consistency only.
3. Write-up, per item. About 1.
   - AUDIT.md section '## AUDIT (depth re-check, DEPTH-MH)': the bar, target vs control numbers, D1 or D2 and why, and the sentence if earned.
   - status.json row (rebase first): depth, depth_pct, depth_unread, depth_sentence (D2 only), depth_check, depth_by (your session id), depth_date, decode_status ('Partially decrypted' at D2).
   - `python3 tools/depth_check.py` must exit 0; paste the output.
   - Correct SO-MANT-F410 or the Hellen SO row only if a quoted count or depth changed (rule 10).
4. Add-on, only if units 0-3 end under 80% of cap and box: fr3416 f.35r run 1 ('.aisi.nlesauroit[Seigneur].e', 14 H) under the same bar. About 1.5.
   - State the AD and whether any content sentence is possible. Expect D1 to hold.
   - The clear letter has bare figures: '{11}', '7', '97' (in the no.25 nomenclator: Roy de nauarre, Pape, recherche). If overbars would make them meet the code clause, cut 4 crops and paste the command:
     `python3 tools/iiif_lines.py --ark <fr.3416 ark from NOTES> --canvas <N> --region <x,y,w,h> --out <scratch> --debug`
     Then file one ASKS row for the owner's overbar look.
   - Do not read those crops yourself: machine readers of this hand are retired.
Done line: the depth per item, with the target and control numbers. Do not decode, do not touch other targets, do not classify novelty.

## VIV-ANCHOR
# VIV-ANCHOR (account-3 orchestrator, 8 Oct 2026 01:1x UTC). default-lane common tail; Opus 5.5 (solver).
Disk-only, known-plaintext anchoring of the unkeyed labels in ciphers/fr16104-vivonne-spain-1572, inks 63, 53 and 54.
- All three are N3 with two audits, held at D1 by D1-F16104I and DA1-VIV.
- The decodes have no f, m or p, and 'que' reads 'qae': the labels are not mapped one-to-one to the cells of Tomokiyo's Vivonne1 key (key_tomokiyo.tsv).
The instrument is new for this target. It is not:
- the stream_align key rebuild from a flat start ([retired]);
- a machine shape judge (two NON-TESTs per label question, so a third tuning is barred);
- the whole-label n-gram cell rank (negative for that instrument only).
Material: the ink-40 cipher (tx/f102r_rec.tsv, tx/f102v_rec.tsv, tx/f103r_rec.tsv) against the clerk's ink-41 decipherment (tx/dec_f10*_merged.txt with {del:..} stripped). Cross-check against the N5-VIVK alignment (tx/vivk_test.py, anchor j0=1265, tx/dec_norm.txt).
Paste `python3 tools/intake_gate_check.py fr16104-vivonne-spain-1572` first. No network, no vision.
Common: .claude/briefs/README.md common tail:
- `room.py --start`, claim, `date -u`;
- rebase before writing shared files;
- run file_shrink_guard.py on every touched file;
- `tools/gaps_check.py fr16104-vivonne-spain-1572` must pass before the done line;
- no AskUserQuestion.
Stop before starting a unit that would cross 80% of cap or box.

UNITS (Opus floor included).
1. PREREG_vivanchor.md, pushed before any score: the statistics, gates, thresholds and seeds below. ~0.5
2. Anchor script (~1.5).
   - For each decipherment word of >= 7 letters, find the ink-40 cipher positions where every non-target letter decodes exactly under key_tomokiyo.tsv.
   - Collect the label at each target-letter slot, unique positions only.
3. Known-answer control before any target value (~1).
   - Hold out the keyed letters d, t, o, r, c, n and s one at a time.
   - Gate: >= 5 of 7 recover their own key label at a share >= 2/3.
   - Below the gate: log NON-TEST in HYPOTHESES.md with both numbers, and stop.
4. Assignments (~0.5).
   - A U label (V, 2, c, o, e, r), or an f, m, p or u-after-q cell, gets a value only with >= 3 distinct positions at a share >= 2/3.
   - Grade it C (clerk decipherment) and add a key.tsv row citing the positions.
   - Known caveat: label e is rare in ink 40 (10 tokens). Expect e/o to stay undecided.
5. Re-decode (~1.5).
   - Run tx/viv63_decode.py, tx/viv53G_decode.py and tx/viv54L_decode.py, each with --check.
   - Re-run the b2 order gate and the 200-wrong-key gate under newly registered seeds and the registered stretch statistic.
   - Report per ink the longest H/C stretch with every liberty counted, beside the ~42-letter AD the verifiers used. Re-read the f.191v L26-27 pardon clause and note its gaps and repairs.
Rule 10: if the reading changes after AUDIT.md, say so in NOTES and flag ROOM for a verifier. Update Remaining gaps and Escalation. If f, m and p stay under 3 positions, name the next instrument but do not start it: ink 50/51 known plaintext (fr.16104 ff.157-159v against ff.162r-163r), about $15.
Do not set depth or the N-class.

Follow-up (separate session, account 1). The parent queues it only if step 3 passes AND some ink's longest H/C stretch reaches about 42 letters or the pardon clause reads without repairs. DA2-VIV, verifier, Opus, cap $4, box 50, one session for all three inks in the DA1-VIV shape:
- rule 7 --check and the gates re-run;
- the clause and the content sentence;
- the status.json depth fields;
- AUDIT.md and the SO-VIV53/54/63 propagation;
- `tools/depth_check.py` exit 0.
Report what was found and where it was not found; do not classify novelty.

## KH-CS3
# KH-CS3 (account-3 orchestrator, 8 Oct 2026 01:1x UTC). default-lane common tail; Sonnet (check-solved), per .claude/briefs/check-solved.md including its '## Premise check'.
Three key-in-hand BnF leads from LANE ST-ACCESS (7 Oct), settled before any deep work. Multi-target check-solved precedent: BNF-Q2-CS.
At claim, write one ROOM line to LANE BNF-FOCUS. BNF-VALUE dropped fr.3988 as 'live in the KHF lane'; it is this orchestrator's.
Common: .claude/briefs/README.md common tail:
- `room.py --start`, claim, `date -u`;
- one request per host at a time, >= 1.5 s apart; stop a host on 429/403/challenge, one retry after a pause at most;
- report request counts per host;
- rebase before writing shared files;
- run file_shrink_guard.py on every touched file;
- no AskUserQuestion.
Stop before starting a unit that would cross 80% of cap or box.

UNITS (~1.5 per vision call).
(a) BnF fr.3988 f.143r-144v and address f.145v (Gallica btv1b9060634t, canvases 304-309). Henri IV to Nevers, Mantes, catalogued 22 Dec 1593; the leaf heads '24 de Dec 1593'. Key no.60 (tools/keys/key60.tsv). ~3.5
   - Open ciphers/fr3988-henri4-nevers-1593/NOTES.md with the status word on line 1.
   - Lettres missives iii-iv were already read (fr3985 NOTES).
   - Read: supplement vols viii-ix (Guadet) by IA full text (advancedsearch + be-api fts); Gomberville, Mémoires de Nevers.
   - Make a fresh shallow clone of dbourdeau/cyphersolver and grep it for 3988, f.143 and nevers1593. Grep the aaymeloglu catalogue too (cite it, copy nothing).
   - Check the DECODE listing on disk (sources/decode). Run sources/desenclos/2026-10-04/search.py with fr.3988 terms. Do a web search and read the Cryptiana and Cipherbrain comment threads.
   - Premise: answer Tomokiyo's 'Interlined deciphering' note for fol.143 (henryiv2.htm, league.htm). The crop step is mandatory and pasted:
     `python3 tools/iiif_lines.py --ark btv1b9060634t --canvas 304 --region <cipher block> --out <scratch> --debug --lines-per-crop 2`
     Look for a pale gloss on the strip crops: 2 calls, never the full page.
   - Rule out duplicate content against the glossed f.119 (Henri IV, 23 Dec) and f.99 (Revol, 22 Dec). Their canvases are estimated at about c256 and c216, and the manifest labels everything NP, so confirm by eye. Compare clear opening lines only: 1 call on crops.
   - Paste `python3 tools/intake_gate_check.py fr3988-henri4-nevers-1593`.
(b) Baluze 155 c273-274 (btv1b9001401d): SA-G's 'unread' Servien 1632 block. ~0.8
   - One IIIF request for canvas 273 at ',1500'. Read the folio stamp.
   - Compare the block's opening with Tomokiyo's second-copy strip on disk: ciphers/decode-2754-bnf-baluze156-1636/images/servien/servien1.png (clear 'De ceste sorte', then 'ctscrdx...').
   - Match: log in decode-2754 NOTES and on KEYHUNT-2026-10-07.tsv line 180: 'inside DECODE R2750 (f.123-130) / Tomokiyo servien.htm: N0, not a sibling'.
   - No match: write one line naming it unread, with key_servien_1632_letters.tsv as the candidate key (not key_sabran_1631). No transcription.
(c) Only if (a) and (b) end under 60% of cap: BnF fr.3053 canvases 16 and 34 (btv1b90601432). ~1.5
   - This is Denonville, Cardinal of Mâcon, Rome, to Montmorency, 1536: DECODE R4233/R4234, 'Partially decrypted'. It is not Gramont.
   - In the same clone, grep Bourdeau's rome1536, gramont1529 and CATALOGUE.md for 3053, f.6 and f.16.
   - Read the BnF finding aid cc49513k. Get foliation from the manifest canvas labels only (no image views).
   - IA full text: Correspondance du cardinal Jean du Bellay II and Ribier I, for 'cardinal de Mascon' 1536.
   - Open ciphers/fr3053-macon-1536/NOTES.md with the verdict, the premise check and the intake gate output.
   - Correct the SA-G3 line in fr2980-gramont NOTES (~l.1547, 'Gramont family').
Last (~0.2, no requests): one-line corrections.
- dupuy452-carpi-1520 NOTES and KEYHUNT line 113: fr.3091 c50 = no.23, Gramont to Montmorency, 11 Oct 1529, read by Lasry (GL.htm) and by Bourdeau (gramont1529).
- KEYHUNT line 115: Dupuy 265 f.336r = Raince to Du Bellay, solved by Lasry (GL.htm).
- fr7129 NOTES and the KEYHUNT SA-G row: fr.7126 f.274 = Bongars cipher no.15, glossed; not a no.2/no.3 known-plaintext source.
No transcription and no decode in this session.

Follow-up (separate session, account 2; the parent queues it only if fr3988's intake gate exits 0): F3988-DT, solver, Opus, cap $4, box 50, disk only.
- PREREG first.
- Decode keyhunt_f143/passQ.tsv (N=177) and passP.tsv (N=466) with tools/keys/key60.tsv. Score with the fr16 4-gram against 200 value-shuffled key60 copies (letter, syllable and word classes kept).
- Positive control: leaf 298 passD, subsampled to N=177 (ARM3-ADJ). It must rank 1/201 with z >= 3.
- Negative control: KHF-4's Mayenne control tags decoded with key60. They must NOT reach the gate.
- If either control misses: NON-TEST. Stop and log it.
- Target gate: passQ ranks 1/201 with z >= 3; passP is the replication. Run judge_plaintext fr16 on the target decode and on a shuffled-target decode (rule 3, ARM-C1).
- Pass: name the transcription job. Native crops of c304-308, two blind passes plus one reconciliation per page, about 15 calls at ~1.5. Split it in two under the $15 job cap.
- Fail: log it in HYPOTHESES.md. The next instrument is a hand-matched atlas from the glossed f.99/f.119 (~$8-10).
- Report what was found and where it was not found; do not classify novelty.
This session: report what was found and where it was not found; do not classify novelty.

## ES132-SLIC
# ES132-SLIC (account-3 orchestrator, 8 Oct 2026 01:1x UTC). default-lane common tail; Opus 5.5 (solver).
Pre-registered S licence for the unprinted paragraphs of ciphers/es132-vargas-mexia-1578.
- Documents: BnF Espagnol 132 f.89r-91r (Philip II to Vargas Mexia, 19 Sept 1578) and f.119r-120r (15 Oct 1578).
- AUDIT 1 (A3V2-ES132A1, 4 Oct): the printed paragraphs are N0 at D2 (C grade). The unprinted paragraphs are N3 at D1 and graded M only ('M-only text is not S').
- Disk only. Both blind passes already exist for every page (passes/; ciphertext_f89r..f120r.tsv).
Tell LANE BNF-FOCUS in your claim line that this is a BnF item.
Common (.claude/briefs/README.md common tail):
- `room.py --start`, claim, `date -u`;
- rebase before writing shared files;
- run file_shrink_guard.py on every touched file;
- `tools/gaps_check.py es132-vargas-mexia-1578` must pass before the done line;
- no AskUserQuestion.
Stop before starting a unit that would cross 80% of cap or box.
Paste `python3 tools/intake_gate_check.py es132-vargas-mexia-1578` first.

UNITS (Opus floor included).
0. Freshness check. About 0.3.
   - Run `git ls-remote` and make one shallow clone of el-descifrador/cabinet-noir. Compare its es132 folder with the 30 letters on file (last checked at 47b6db9).
   - If f.89 or f.119 now appear there, stop and flag it in ROOM as a found-solved risk. Run no further units.
   - Read NOTES Remaining gaps. The fresh rule-7 re-derivation owed after A3V3-ES132S (43 settled tokens) is NOT yours to discharge: a solver session cannot be its own fresh re-derivation. Run the existing --check (test2.py / settle_dup.py) as a staleness check only. Record in NOTES that the fresh re-derivation is still owed and is the first step of the verifier follow-up.
1. PREREG_slic.md, pushed before any score. About 1.5. The grade rule:
   - A token in the unprinted paragraphs becomes S only if both blind passes agree on its sign AND its key cell decoded to the printed letter at least k times in the known-answer paragraphs. Fix k before scoring. Every other token stays M.
   - Cp.30 nomenclature codes (numbers >= 38) have no key on disk. They stay M/U and are reported separately, never counted in gate (a).
   - Gate (a), held-out accuracy: derive the confirmed cells from one letter's printed paragraph (Teulet 15 Oct = f.119v/120r; 19 Sept = f.90v L10-L26). Apply the rule to the other letter's printed paragraph. Require S-token accuracy against the print >= 0.90, in both directions.
   - Gate (b), a control that can differ: the same rule under 200 value-shuffled Cp.30 keys. It must license far fewer tokens, at accuracy below the gate. Report its p95.
   - Gate (c), power at the measured error: inject the measured pass-disagreement rate into the known-answer paragraphs. The rule must still meet (a) on >= 16 of 20 seeds.
   - Precedent shape: BIR-APPLY and D2-B117KAPC (ciphers/birago-fr3252-1571-72/NOTES.md).
2. Run the gates. About 1.5. If any gate fails, stop. Log the result in HYPOTHESES.md with both numbers; M stays M.
3. If all gates pass, regrade the unprinted pages. About 1.5.
   - Regenerate with the folder's RD7 procedure (test2.py / RD7-2026-10-04*.md), adding a --check if the script lacks one.
   - Recount H/C/S/M/U per letter.
   - List the longest S stretch per letter and the liberties it took, beside the design AD (1.5 x unicity for Cp.30, liberties counted). The verifier, not you, rules depth.
4. Judge. About 0.5.
   - Run `python3 tools/judge_plaintext.py` with the folder's es16 corpus (the nearest era to 1578; report its per-fold spread, rule 3) on the regraded text and on a shuffled-target decode. Paste the output into NOTES.
   - Update Remaining gaps and Escalation.
Do not set depth or the N-class.

Follow-up (separate session, account 2; the parent queues it only if step 2 passes): AUD2D-ES132, verifier, Opus, cap $6, box 70.
- First, the owed fresh rule-7 re-derivation of the f.89 pages (spec + key + test2.py/settle_dup.py --check). If it differs by more than the M tokens, send the reading back and stop.
- Then a depth re-grade of both letters under tonight's DEPTH BAR.
- Then the adversarial AUDIT 2 for the N3 part: cabinet-noir, Teulet, Mignet, CODOIN, the Simancas guides, a phrase search.
- SO rows.
- The parent then writes the status.json rows (recovered-passages, N3 part only).
Report what was found and where it was not found; do not classify novelty.

## AUD2-WVO11008
# AUD2-WVO11008 (account-3 orchestrator, 8 Oct 2026 01:1x UTC). default-lane common tail; Opus 5.5 (verifier).
Second adversarial audit of ciphers/wvo-11008-certain-1572: WVO 11008 (KHA A 11/XI 15), Orange as 'George Certain' to Lodewijk as 'Lambert Certain', Keulen, 12 Aug 1572.
AUDIT 1 (KHF2-VERIFIER, 7 Oct): N3, key period, D2 at 80% (32 of 40 non-null tokens H). Brief shape: .claude/briefs/runs/2026-10-08-acct3-aud2-ls.md.
You are separate from KH2-D, KHF-2 and KHF2-VERIFIER. Do not protect their conclusions.
Common (.claude/briefs/README.md common tail):
- `room.py --start`, then a claim with the cap and box end; `date -u` for every time;
- rebase before writing shared files;
- run file_shrink_guard.py on every touched file and paste the output in the done line;
- no AskUserQuestion.
Stop before starting a unit that would cross 80% of cap or box.

UNITS (about $1.5 each, plus the Opus floor).
1. Rule 7 and control.
   - `python3 ciphers/wvo-11008-certain-1572/decode.py --check` must exit 0.
   - Eye-check the run tokens on the crops already on disk (images/p1_L02_s*.jpg and p1_L07_s*.jpg).
   - If a run is not covered by those crops, fetch the PDF once (manifest.json source URL, Huygens, >= 2 s apart), extract the page with pdfimages, and run this command, pasting it:
     `python3 tools/iiif_lines.py --image <page1 jpg> --out <scratch> --prefix p1 --lines-per-crop 3 --max-width 2000 --debug`
   - Re-run the matched key-permutation control under the printed 1572 Orange-Nassau table (ciphers/jan-van-nassau-1572-75/key_1572.tsv). The figures on file are 4-gram -1.435 vs shuffle p95 -1.576 (6/1000). Report both numbers.
2. Novelty. Read AUDIT 1's family log, then search at least the families it left:
   - Waanders 2022 ToC; De Leeuw 2000 index;
   - Gachard, Correspondance de Guillaume le Taciturne (IA full text / be-api fts);
   - the Groen van Prinsterer Archives supplement;
   - Huygens retroboeken phrase search (CLAUDE.md host table, >= 2 s apart);
   - OpenAlex, Semantic Scholar and CORE with their keys; Persée; HAL;
   - Google Books with country=US and the key;
   - tools/print_check.py on phrases.txt;
   - JSTOR-QUEUE.tsv rows in families (i) and (ii) (they never block).
3. Depth (rule 4a). Keep it or lower it; never raise it. Use the orchestrator's DEPTH BAR for tonight (same text as DEPTH-MH):
   - Cipher clause: an H/C/S stretch above 1.5 x unicity for the 1572 table's design, with every liberty counted. A period table that was not fitted does not shrink H(K) to the liberties.
   - An external check (here, the printed period table) is a D3/D4 element under CLAUDE.md 4a. It does not replace the clause at D2. AUDIT 1's 'non-statistical external check' argument therefore does not carry D2.
   - Code clause: a code value reading sensibly in >= 2 independent contexts. Letter-table values (15=e, 39=n, 12=d, 54=s) are cipher letters, not code values, and do not meet it. An H/C grade alone does not meet it either.
   - Names alone meet neither clause.
   - If neither clause holds, lower to D1 and say why. If you think the bar is wrong, post one ROOM flag for the parent and still rule under it.
4. Write '## AUDIT 2 (second adversarial, AUD2-WVO11008)' in AUDIT.md:
   - families searched and families unreachable;
   - class: keep N3, raise to N4 only per rule 10, or lower;
   - key `period`; a depth line with the check used; one safe and one unsafe sentence;
   - correct SO-WVO11008-CERTAIN in SECOND-OPINIONS-QUEUE.tsv if a count, class or depth changed (rule 10).
Parent follow-up, not this session:
- NOTES line 1: open -> partial (rule 5);
- rewrite the gap bullets in ' - blocker:' form until `tools/gaps_check.py wvo-11008-certain-1572` passes;
- the status.json row (recovered-passages; N-class and depth from your AUDIT 2).
Do not decode other letters. Do not touch other targets.

## AUD2D-OLD2442
# AUD2D-OLD2442 (account-3 orchestrator, 8 Oct 2026 01:1x UTC). default-lane common tail; Opus 5.5 (verifier).
Second adversarial audit and first depth for ciphers/na-oldenbarnevelt-2442-1605.
- Document: Nationaal Archief 3.01.14 inv. 2442, Senisteros to Juan de la Peña, 23 Dec 1605 (copy).
- Blocks: B (f.55, 95 tokens: S90 M4 I1) and C1 (f.56, 61 tokens: S53 M6 I2).
- AUDIT 1 (VERIFY-OLD, 3 Oct): N3, key ours. The key is a vowel-digit cipher (a=4 e=8 i=3 o=7 u=2) with consonants in clear (VX-CT03).
- No depth has ever been set: rule 4a arrived after AUDIT 1.
You are separate from VERIFY-OLD, R15-OLDV2 and every solver (VX-CT03, A2-OLD/2, OLD-PASS2, R12-R15). Do not decode. Blocks A and C2 are not yours: they wait on the owner's sorter.
Common (.claude/briefs/README.md common tail):
- `room.py --start`, claim, `date -u`;
- rebase before writing shared files;
- run file_shrink_guard.py on every touched file and paste the output in the done line;
- no AskUserQuestion.
Stop before starting a unit that would cross 80% of cap or box.

UNITS (about $1.5-2 each, plus the Opus floor).
1. Rule 7.
   - `python3 ciphers/na-oldenbarnevelt-2442-1605/scripts/apply_key.py --check` must exit 0.
   - Eye-check a sample of B and C1 tokens on the existing images/ crops. No new fetch.
   - Recount S/M/I per block, both per word token and per digit (cipher) token.
2. Novelty, on the Spanish side that AUDIT 1 left at 'not N4'.
   - Search Senisteros and Peña by name and date.
   - Editions: CODOIN; Lonchay-Cuvelier, Correspondance de la cour d'Espagne (IA be-api fts; no borrow); Rodríguez Villa; the Simancas Estado guides.
   - Google Books with country=US and the key; OpenAlex, Semantic Scholar and CORE with their keys.
   - tools/print_check.py on phrases.txt. Add 'i se lamenta de uer los tiempos que corren' and two more distinctive phrases first.
   - JSTOR-QUEUE rows in families (i) and (ii).
3. Depth (rule 4a step 3a), under the orchestrator's DEPTH BAR for tonight (same text as DEPTH-MH). An external check is a D3/D4 element and not a D2 alternative. H(K) is design-level, with every liberty counted.
   - Unit of measure: only the digits are cipher; consonants are transcribed cleartext.
     - depth_pct = the share of digit tokens graded H/C/S (research section 3 item 2). Also report the word-token share, labelled as such.
     - The stretch is counted in consecutive digit tokens.
   - Write the AD for this design into AUDIT.md before measuring any run.
     - H(K) = the vowel-to-digit map over the digits used, plus every liberty: M tokens, I repairs, u/v choices, word-break choices.
     - R = redundancy per digit token, estimated empirically from tools/data/es1600 as the entropy drop of vowel identity given its consonant frame. Not the per-letter R of Spanish prose. Show the computation.
   - Measure the longest S/H stretch per block in digit tokens.
   - Matched control on file: VX-CT03 recovers 100% at N=325, K=7, both clean and at 37.3% crib noise. That is not the target's N (rule 3, ARM3-ADJ). Before using it for anything above D2, subsample the same control to N=95 and N=61 with the same script and report both numbers.
   - D2: one stretch clears the AD and you write a true, specific sentence about the content.
   - D3: >= 80% H/C/S on digit tokens, gaps mostly names, and AD plus a matched control at this length.
   - Report the es judge FAIL as a FAIL. It is not a depth gate (rule 7).
   - If you think the bar or the unit is wrong, post one ROOM flag and still rule under it.
4. Write '## AUDIT 2 (second adversarial + depth, AUD2D-OLD2442)' in AUDIT.md:
   - families searched and families unreachable;
   - class: keep N3, raise to N4 only per rule 10, or lower;
   - key `ours`; depth, depth_pct (digit-token basis) and the check used; one safe and one unsafe sentence;
   - re-check the wording of SO-OLDEN-2442-BC1 and correct it if a count or class changed.
Parent follow-up, not this session: write the status.json row (recovered-passages) from your section, then run `python3 tools/depth_check.py`. NOTES line 1 open -> partial (rule 5).
Do not decode. Do not touch other targets.

# NEWT-B check-solved jobs (LANE NEWT-B-account-2, written 6 Oct 2026 23:1x UTC by date -u)

Parent: LANE NEWT-B-account-2 (session_01G6QuLXC8cNrSyEF4PeczQC), brief .claude/briefs/runs/2026-10-06-acct3-newtargets.md PART B.
One worker per job below. Model Sonnet. Cap USD 7 per job (check-solved 5 + premise check 2), box 70 min; stop at 80% of either.
No transcription, no key application, no cryptanalysis, no paid orders, no DECODE login unless the job says so.

## Selection (why these five, and what was dropped)

Source: QUEUE.md "Tier A"/"Tier B" (rows 1-37) and the scPOOL "real pools" table, minus every row that is already a
ciphers/ folder. Fresh shallow clones of dbourdeau/cyphersolver (HEAD 5 Oct 2026 21:27 -0500) and aaymeloglu/unsolved-ciphers
were grepped by shelfmark, DECODE id and sender on 6 Oct 2026 23:1x UTC. Dropped as already read or worked by others:
Walsingham-Wotton 1585 (Bourdeau wotton1585), Add MS 4136 Cecil batch (Smith complete, Lomer/Middelmore/Coligny read,
Norreys partial, Percy 63 signs attempted), Harley 1582 (read), Harley 7001 R7766 (Bourdeau 93%), Harley 260 R8356/R8358/R8363
(Bourdeau: clear in Digges 1655, residue a nine-sign run, too short), Wood-Cecil 1568 R2989 (Bourdeau wod1568), Gun Wa 1889
(Aymeloglu: 77 letters, feedback family exhausted with 20/20 controls), Folger V.b.264 (host blocked to the cloud), Charles I
Isle of Wight 1648 (no key located, blocked). Pools: RAH 9/23-25, Barb.lat 6956/6960, ARA Carpio-Fuenmayor, ASV France 17-18,
ASV Spain 364C all overlap Bourdeau targets already keyed or read (bPOOL0, 26 Sept); Barb.lat 6956 is ciphers/pallotto-1628
(found-solved). Five survive; fewer than eight because the selection rule finds nothing else worth a $3 test.

## Jobs

| job | slug (new folder) | item | why it might move | first cheap test to name if open |
|---|---|---|---|---|
| NB-HYDE | hyde-add4166-1659 | Intercepted letter of Edward Hyde, 1 Nov 1659, BL Add MS 4166 ff.92-93, DECODE R4886, "undeciphered portions" (Tomokiyo unsolved.htm, thurloe.htm) | Hyde's 1659 correspondence keys are in print: the Hyde-Barwick key (THE=370, 1-692, Vita Johannis Barwick 1721 plate facing p.316, IA bim_eighteenth-century_vita-johannis-barwick-s_barwick-peter_1721, transcribed in Bourdeau's targets/hyde/barwick_key.py) and the Thurloe-printed Hyde keys (ciphers/thurloe-printed, ciphers/monck-1660 name the Hyde-Barwick key test). QUEUE says numbers run to ~966, above 692: check which Hyde key covers that range | apply the matching printed Hyde key to the R4886 groups (thumbnail/transcription first) vs a shuffled-group control |
| NB-CRAV | craven-rupert-1648 | William, Baron Craven to Prince Rupert, The Hague, 6 Nov 1648, BL Add MS 18982 ff.134-135, DECODE R8447 (Tomokiyo unsolved.htm: "seems to use some different cipher" from the volume's deciphered letters) | the same volume carries deciphered Rupert-circle letters (Add MS 18980-82, DECODE R8429-R8454; ciphers/maurice-rupert-1645/NOTES.md has the volume survey) | group/sign count from the DECODE record and thumbnails, then a key-family test against the volume's deciphered keys with a matched control |
| NB-BAGNO | bagno-francia104-1652 | Niccolo Guidi di Bagno (nuncio, Paris) to the Secretariat of State, 5 Jan 1652, AAV Segr. Stato Francia 104 ff.5r-7v, DECODE R5622 | Bourdeau attempted 22 Sept 2026 (targets/bagno1652, status "-"): four pages unseparated decimal cipher with Italian clear words; Lasry's Francia 346 key structurally excluded (66/666). Check whether this is Bourdeau's own stated next step (check-solved.md "Stated next step") and whether the 1652 Paris nunciature register or a decifrato exists (AAV Francia 104 itself, Francia 97-105, Barberini) | if open and not a duplicate-effort risk: segmentation test of the decimal stream (2-digit vs mixed) against a synthetic matched control at the same N |
| NB-CORN | cornwallis-pro3011-1780 | Cornwallis Papers, American campaign, TNA PRO 30/11 items Discovery marks undeciphered (6/23-26, 3/207-209, 69/18-24, 68/32-35), 1780-81 | Bourdeau research/oldest/scan_2026-09-23/hard_targets.md: "Saberton decoded the southern British ciphers (JAR 2019)"; Saberton, The Cornwallis Papers (2010) prints keys. Expect found-solved; confirm per item and say which (if any) item is not covered. ciphers/pro3055-clinton-1779 and LOCAL-QUEUE/JSTOR-QUEUE rows already mention Cornwallis -- read them first | only if an item survives: apply Saberton's printed key to that item |
| NB-CHHM | charles-hm-cabinet-1645 | Charles I to Henrietta Maria, 8 April 1645, one sentence left in their private cipher in The King's Cabinet Opened (1645) (QUEUE Tier B rank 26) | the King's Cabinet letters were printed deciphered, so the private cipher's table is largely recoverable from the other letters (Tomokiyo charlesi.htm; Lasry's reconstructed Henrietta Maria household keys, Bourdeau README "Henrietta Maria's household -> Charles I ... complete"); Green, Letters of Queen Henrietta Maria (1857) p.299; Aymeloglu CATALOGUE.md row R660/R931/R595 points to the same Naseby haul | apply the table built from the deciphered King's Cabinet letters to the one sentence vs a shuffled-key control (too-short is a legitimate verdict: give N and unicity) |

## Steps (each worker, its own job only)

0. First action `python3 tools/room.py --start` (if it fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`).
   `date -u`. ROOM claim via tools/room.py with your job id, slug, cap 7, box end time, "for LANE NEWT-B-account-2".
1. Read .claude/briefs/check-solved.md in full and run it for your item: six sources (web incl. the model-solve family; print:
   the standard edition/calendar opened by you, with pages; community lists and the "## Web and blog check" section with the
   four plain searches and the three blog site searches, comment threads opened; DECODE login-free listing via
   `tools/decode_list.py` and the record page; Bourdeau and Aymeloglu -- fresh shallow clones in your scratchpad, grep by
   shelfmark, DECODE id, sender, date, read the hit files, quote any sentence about this very letter verbatim; and the
   solver's own planning text for it). Editor's-note phrase sweep and HTRC fallback as that brief says.
2. Premise check (a)-(d) as in the same brief, written as "## Premise check (<job>, <date>)".
3. Create ciphers/<slug>/NOTES.md: line 1 the bare status word (open, partial, found-solved, blocked, ...), line 2 the one
   sentence naming the edition/calendar you read and the pages, then sources, the verdict reasoning, the two sections above,
   and "## While waiting" if blocked or waiting. No ciphertext.txt unless a transcription already exists in print or on
   DECODE as an attached document (then copy it as transcribed, with source and date).
4. Run `python3 tools/intake_gate_check.py <slug>` and paste its output into NOTES.md. Fix the citation until it exits 0 when the
   verdict is open/partial; a blocked/found-solved verdict may stay nonzero -- say so.
5. Only if the verdict is open or partial and the gate exits 0: write specs/<slug>.json (follow specs/README.md and an
   existing spec such as specs/rayburn-2004.json: slug, name, date, language_candidates, ciphertext_pending or ciphertext with
   source, alphabet, constraints, cheap_tests_in_order with test 1 = the table's named test made concrete, matched_control,
   cheap_test_done [] , judge block, value, model, written). Do NOT run the test.
6. If found-solved: say who read it and where (README F0/F1/F2), and what correction or key it leaves to hand on.
7. Leave shared registers (CATALOG.md, QUEUE.md, status.json, WORK-QUEUE.tsv) to the lane. Commit only your folder and spec by explicit path,
   `git fetch origin main && git rebase FETCH_HEAD && git push origin HEAD:main`.
8. ROOM done line via tools/room.py: verdict, gate exit code, spec written or not, request counts per host, "for LANE NEWT-B-account-2".
   Report in five lines; stop.

Good-citizen rule and the CLAUDE.md host table for every request (DECODE 1.5-2 s apart; BL IIIF is dead; TNA Discovery API ok;
Google Books with country=US and the key; OpenAlex/S2 with keys). At most two Sonnet subagents. Report what was found and where it
was not found; do not classify novelty; never the words new, first, novel, solved, cracked for anything this project did. Never
print or commit credentials. Never call AskUserQuestion. Never name the owner.

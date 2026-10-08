# ST-LEDGER-2 worker brief (account 1, LANE ST-LEDGER-2, session_01F54CxP1w63RgwvrKV1pN4S; written 8 Oct 2026 03:5x UTC)

Parent round: .claude/briefs/runs/2026-10-08-acct3-ledger2.md, section ST-LEDGER-2. Method, steps 0-4 and the reader/verifier
sections are those of .claude/briefs/runs/2026-10-07-acct1-st-ledger-workers.md (read its header steps 0-4, "Wave 2" LS-R1/LS-R2 and
LS-V1/LS-V2 sections in full) -- this file only changes entries, IDs, caps and the points below. Read CLAUDE.md and
ciphers/eckert-1864/NOTES.md sections "## LS-PRE", "## LS-R3", "## LS-R4" (worked examples) first. Every ROOM line ends
"for LANE ST-LEDGER-2".

Changes from the wave 1-4 brief (all workers):
A. Commit early, never end without a commit. Two earlier sessions on E30-E36 (LS-R2, LS-R2b, 7 Oct) ended after about 8 minutes
   with nothing on origin: one because its permission mode refused a Bash call, the other ended its turn saying "decode handed off".
   So: (1) after transcribing each two entries, append them to ciphertext.txt (or -no2/-no9), run the decoder `--write` and
   `--check`, and push (`python3 tools/room.py --push <paths>`) BEFORE reading the next pair; (2) you never hand a step to "the next
   worker" -- decode, print check and the NOTES section are all yours; (3) if any tool call is refused, write one ROOM line quoting
   the refused command verbatim (no credential), push what you have, then try the same step once by a plainer route (e.g. a
   one-line python3 instead of a pipeline); if that is refused too, stop. Your final message must name the last commit hash.
B. Shared files: ciphertext.txt, reading.md, entries-mssEC19.tsv, NOTES.md are touched by up to three readers at once. Fetch and
   rebase immediately before every push; on a conflict keep both sides' blocks in ID order and regenerate reading.md with
   `decode.py --write` (never hand-merge the derived block). Append your NOTES section at the end of the file.
C. Readers: no subagents; read the strip crops yourself. If none of the three keys reads at least 80% of an entry's code-word tokens,
   record "key not in hand" with the counts and go on -- do not guess.

---

## LS-R5 (Sonnet 5.5, solver; cap $6, box 100 min): ten 1864 Cipher No. 1 entries
 Entries (pointer/page/entry_on_page; IDs fixed): 9057/165/1 E55, 9129/237/2 E56, 8927/35/0 E57, 8932/40/1 E58, 8951/59/2 E59,
 9003/111/1 E60, 8959/67/1 E61, 8921/29/2 E62, 9036/144/1 E63, 9038/146/0 E64 (181 words, last).
 If one is in Cipher No. 2 it goes to ciphertext-no2.txt as N2-BG, N2-BH...; old vocabulary to ciphertext-no9.txt as O9-AH, O9-AI...
 NOTES section "## LS-R5 (8 Oct 2026, account 1, for LANE ST-LEDGER-2)". ~0.5 per entry; stop before an entry that would cross 80%
 of cap or box.

## LS-R2c (Sonnet 5.5, solver; cap $5, box 90 min): the parked E30-E36, once
 Entries and IDs as LS-R2 in the wave 1-4 brief: 9051/159/1 E30, 9051/159/2 E31, 9054/162/1 E32, 9055/163/0 E33, 9056/164/0 E34,
 9057/165/3 E35, 9060/168/1 E36 (McCaine in the Shenandoah Valley, Aug 1864). Point A above is the whole reason for this run: push
 after E30-E31. No. 2 entries go to N2-BP..; old vocabulary O9-AP... NOTES section "## LS-R2c (8 Oct 2026, account 1, for LANE
 ST-LEDGER-2)", and replace the sentence "They are still unread" in "## ST-LEDGER parked entries" by one line pointing to it.

## LS-R6 (Sonnet 5.5, solver; cap $6, box 100 min): the 1864 rows guessed Cipher No. 2 / old vocabulary, then the 1865 check
 Step 1 (entries): 8966/74/2, 9104/212/2, 9011/119/2, 8979/87/0, 9139/247/2, 8925/33/1, 8958/66/0, 9019/127/0 (cipher_guess 2) as
 N2-BG.. in ciphertext-no2.txt read with key-no2.md (decode_no2.py), and 8937/45/0, 8907/15/0 (guess 9) as O9-AH.. with key-no9.md;
 cipher_guess is right on 75 of 98, so an entry that turns out Cipher No. 1 goes to ciphertext.txt as E65, E66... If LS-R5 has already
 used N2-BG/O9-AH for a stray entry, take the next free ID after fetching.
 Step 2 (script only, ~10 min, before any 1865 read): does Cipher No. 1 still read the 1865 rows? For every priority-1 1865 row with
 words >= 40, compute the share of its non-function tokens found in key.md's code-word column, and the same share for the read 1864
 E entries (E21-E54) as the control; write both distributions (median, p10) in your NOTES section and a column-free one-line verdict:
 "No. 1 reads 1865 rows" if the 1865 median is within 0.1 of the control's, else "No. 1 does not read 1865 rows (Nos. 3/4 not in hand)".
 Do not read 1865 entries in this job.
 NOTES section "## LS-R6 (8 Oct 2026, account 1, for LANE ST-LEDGER-2)".

## LS-V5 / LS-V6 / LS-V2c (Opus 5.5, first verifier; cap $6.5 for 10 entries, $5 for 7) -- spawned by the lane after the reader finishes
 The LS-V1/LS-V2 section of the wave 1-4 brief, scoped to that reader's entries; AUDIT.md "## AUDIT (LS-V1)" and "## AUDIT (LS-V4)" are
 the worked examples; depth under .claude/briefs/runs/2026-10-08-acct3-depth-bar.md. Section heading "## AUDIT (LS-V5)" etc. Separate
 session from every reader. Mandatory in the search, per not-located entry: the press of the day (Chronicling America / LOC newspapers
 by date window and quoted phrase -- two second-audit drops, E26 and E28, came from NY Herald, Phila. Press and the Welles diary), the
 sender's and recipient's printed papers, OR/ORN by date +/- 3 days, IA/Google Books (country=US + key) quoted phrases, OpenAlex/S2/CORE
 with keys, JSTOR-QUEUE rows in both families (never block). status.json rows for N3+ only with audit_status "one audit"; SO row per
 N3+ entry; `tools/depth_check.py` passes; file_shrink_guard before the final push. Do not decode other entries.

---

# Wave 2 (written 8 Oct 2026 04:1x UTC): first verifiers
Readers done: LS-R5 E55-E64 (5.48), LS-R2c E30-E36 (3.10; E30 E31 E32 E34 E35 located by the reader in OR I/43 pt 1), LS-R6
N2-BG..N2-BM, E65, O9-AH..O9-AJ (3.85; step 2: "No. 1 reads 1865 rows", median 0.276 vs control 0.353). The readers were Sonnet and
fast (13-20 min per batch), so each verifier also: image-checks THREE entries' strip crops word for word (not two), the longest entry
among them, and re-reads from the image every token graded I or M and every word where the reader's NOTES say image and volunteer text
disagree. For the 1865-row verdict: LS-V6 re-runs LS-R6's step-2 script and says whether the 0.077 gap is within the spread of the
control (one line, no reading).
 - LS-V5 (Opus 5.5, cap $6.5, box 90 min): LS-R5's E55-E64. LS-R5 says the Aug 1864 OR volume was not in its cached set (E55 E63 E64
   unsearched there, E60 Basler unsearched): search those first.
 - LS-V6 (Opus 5.5, cap $7, box 95 min): LS-R6's N2-BG..BM, E65, O9-AH..AJ (decode_no2.py / decode_no9.py --check too). N2-BH is
   located by the reader in OR I/43 pt 2 p.468: confirm by script, N1.
 - LS-V2c (Opus 5.5, cap $4, box 60 min): LS-R2c's E30-E36: confirm the five OR I/43 pt 1 locations by script (N1 if word for word),
   full search on E33 and E36.

## LS-R7 (Sonnet 5.5, solver; cap $5.5, box 100 min; written 04:2x UTC): ten more 1864 rows, non-army addressees
 Points A-C and the LS-R5 section apply. McCaine (Valley) rows are skipped: LS-R2c found 5 of 7 already in OR I/43 pt 1.
 Entries and IDs: 9151/259/3 E66 (header says Jan 3rd 1864; page sits in Jan 1865 -- read the date from the image and say which),
 9134/242/0 E67, 9039/147/0 E68, 9093/201/2 E69, 8985/93/2 E70, 8914/22/0 E71, 9075/183/1 E72, 9118/226/0 E73, 9071/179/2 E74,
 8899/7/1 E75. No. 2 entries go to N2-BN, N2-BO...; old vocabulary O9-AK... (fetch first; take the next free ID if one is used).
 Do not commit OR djvu text or other bulk caches (LS-R5 committed 5.5 MB to sources/ia-fulltext/print-check/; reuse it, add nothing).
 NOTES section "## LS-R7 (8 Oct 2026, account 1, for LANE ST-LEDGER-2)".

## LS-V7 (Opus 5.5, first verifier; cap $5.5, box 80 min; written 04:4x UTC) -- LS-R7's batch, same section as LS-V5/LS-V6
 LS-R7 read E66 E67 E68 E70 E72 E73 E74 (No. 1) and one No. 2 entry (its done line says "N2-BN as E71": settle which ID the file
 actually carries and make the NOTES table agree), with M 13, I 5; E69 and E75 recorded "key not in hand". E67 is located by the
 reader in ORN I/11 (Wise to Porter 3 Dec 1864): confirm by script, N1. Two findings from the other verifiers apply here: LS-V6 found
 a Sonnet-read entry (E65) decoded with the wrong key (Cipher No. 1 instead of No. 2), so for EVERY entry first check which key's
 vocabulary its code words belong to (share of tokens in key.md vs key-no2.md vs key-no9.md) before judging the reading; and re-read
 from the image every M token. For E69/E75 say in one line whether one of the three keys does read them after all (counts only).
 Points from Wave 2 (three crops word for word, I/M re-reads, press of the day) hold.

## LS-FIX (Sonnet 5.5; cap $2, box 35 min; written 05:2x UTC): two corrections the first verifiers asked for, nothing else
 Points A-C apply. (1) E65 (8958/66/0) was decoded with Cipher No. 1 but is Cipher No. 2 (AUDIT.md "## AUDIT (LS-V6)"): move its
 block out of ciphertext.txt into ciphertext-no2.txt as the next free N2 ID (fetch first; N2-BN is used), decode with decode_no2.py
 against key-no2.md, both decoders `--write` then `--check` exit 0; leave a one-line "E65: withdrawn, re-filed as N2-B? (LS-FIX)" in
 the ciphertext.txt header comment or reading.md note the way earlier withdrawn IDs are recorded (grep for "withdrawn" first); update
 the entries-mssEC19.tsv already_read cell and the LS-R6 NOTES table row. (2) E60 (AUDIT "## AUDIT (LS-V5)"): fix the header to
 Lincoln to John Hay at the Astor House and add "John" as a plain word in clear, re-run decode.py --write/--check. Then add one line to
 AUDIT.md under "## AUDIT (LS-V6)" and "## AUDIT (LS-V5)" naming the commit that carried each correction (rule 10 propagation); no
 class changes. NOTES section "## LS-FIX (8 Oct 2026, account 1, for LANE ST-LEDGER-2)", three lines. file_shrink_guard before push.

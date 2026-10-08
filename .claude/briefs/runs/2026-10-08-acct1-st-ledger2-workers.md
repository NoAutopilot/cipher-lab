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

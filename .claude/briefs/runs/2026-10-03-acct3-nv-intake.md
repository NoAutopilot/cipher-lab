# NV-INTAKE (account-3 orchestrator, 3 Oct 2026): intake for the Nevers-vein picks NV-01, NV-02, NV-03, NV-09

Source: NEVERS-VEIN.tsv + QUEUE.md "Nevers vein (3 Oct 2026)" (NEVERS-VEIN, 0b9e9356). Model Opus 5.5. Cap USD 5, box 45 min.
Disk and text only: no model reads any image in this job. vision calls: 0 x USD 1.5 = 0

For each of NV-01 (fr.3993 ff.71-72, Ch. de Gonzague to Nevers, 2 Aug 1595, key no.70), NV-02 (fr.3416 f.35, Nevers to
his son, key no.25), NV-03 (fr.4715 f.38, 17 Nov 1589, key no.25), NV-09 (fr.4712 f.10, Nevers to the duchess, 37 numbers
printed on Tomokiyo nevers.htm), in that order:
1. Create ciphers/<slug>/ (slug like fr3993-gonzague-nevers-1595) with NOTES.md, status line `open` or `found-solved`.
2. Check-solved per .claude/briefs/check-solved.md (six sources, dated), PLUS: grep github.com/el-descifrador/cabinet-noir
   (Cabinet Noir v1.0, 29 Sept 2026, CC BY 4.0 -- it already reads fr.4715 n27/n35/n37/n47/n48 and uses fr.3995 keys;
   GF4-BATCH9 / CABNOIR found it, see ROOM 02:46-03:01) and Bourdeau's nevers* folders for the shelfmark and folio.
   A Cabinet Noir or Bourdeau reading of the letter means found-solved: write it and stop on that row.
3. "## Web and blog" and "## Premise check" sections (a)-(d) (check-solved.md), then `python3 tools/intake_gate_check.py
   <slug>` pasted into NOTES.md; exit 0 needed.
4. NV-09 only, if its gate exits 0: Tomokiyo's 37 numbers to ciphertext.txt (source + date, as printed), then apply the
   duchess keys Tomokiyo publishes (no.1, no.2, no.4) by script with tools/decode_key.py conventions; report per key the
   share of tokens the key covers and the reading; matched control = the same 37-token count drawn from a shuffled
   ciphertext under each key (coverage-on-shuffle CANNOT differ by construction -- CLAUDE.md rule 3 -- so score the
   reading with tools/judge_plaintext.py fr16 on 200 shuffles vs the real order instead, rank and z). Grade per token.
5. "## While waiting" in each NOTES.md naming the next step and its cost (NV-01/02: line crops + 2 blind passes +
   reconciliation per leaf, then apply key no.70 / no.25 with the glossed siblings as known-answer control).
Shared files: ROOM claim/done via tools/room.py; do not edit status.json, NEAR.md, PROGRESS.tsv (the orchestrator does).
Report what was found and where it was not found; do not classify novelty. Request count per host in the done line,
which starts "for the account-3 orchestrator". Run tools/file_shrink_guard.py on touched files before the final push.

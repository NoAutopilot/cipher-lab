# PREREG C1161-G1 (15 Oct 2026, account-2 worker for LANE DEFAULT-A2-1616-15), pushed before any montage is built or any score computed

Brief `.claude/briefs/runs/2026-10-15-ytbiz-default-1616-jobs.md` (C1161-G1). Disk only, 0 host requests. Key of record: George Lasry's sheet
(`sources/cyphersolver/2026-10-14-lasry/clair1161/lasry_p073_1.png`, published by D. Bourdeau, CC BY 4.0; credit rule 8). AUDIT class N0: the
text is known; this job only corrects the record of the concordance between our key and his.

## Part 1: blind exemplar re-pass (C1161-EXC protocol unchanged: exc/exc_windows.py, exc/match_prompt.md, exc/tokens.tsv windows)
- **D (group 1 fresh pass B)**: labels s, th, psi, tri, d, rot + control qb (agreed a), one montage, `exc/exc_windows.py OUT D 16161
  s,th,psi,tri,d,rot,qb` -> exc/ids_D.tsv; one blind Sonnet call, prompt exc/match_prompt.md verbatim -> exc/pass_D_g1.tsv.
- **E (fourth reader on f, dia)**: labels f, dia + controls sd (agreed g) and y (agreed r), `exc/exc_windows.py OUT E 16162 f,dia,sd,y`
  -> exc/ids_E.tsv; one blind Sonnet call -> exc/pass_E_g1.tsv.
- Readers see only the sheet and the montage (no label names, values, key, prior passes). Montages in the session scratchpad only.
- POWER: D passes if qb is answered with column a; E passes if sd -> g AND y -> r. A pass failing POWER is a non-test (logged, not used).
- Group 1 MAPPED: D passes POWER and pass A (C1161-EXC, POWER PASS) and D name the same column (rows may differ, u/v one column) or the same
  nom/null entry, neither `none`. Both answered but different -> UNDECIDED (no reconciliation call in this job; named next step). Either `none`
  and no agreement -> NO MATCH. Pass B of group 1 (POWER FAIL) is not used.
- f, dia FINAL: if E passes POWER, final = the column named by >= 2 of A, B, C (C1161-EXC, all POWER PASS in groups 3/4) and E; else UNDECIDED.
- Outcome: his_value_blind and agree/disagree vs key.tsv written to g1/concordance_g1.tsv. No key.tsv or ciphertext.tsv edit.

## Part 2: registered --try at every occurrence (tools/decode_key.py, fr16, --window 8, --nulls 100, defaults otherwise)
Each hypothesis is its own call (no other hypothesis in place), against the current main transcription (ciphertext.tsv with the S275 So/Sl
split, key.tsv), logged to crossword_log.tsv.
- Power controls first (as C1161-S275): P1 `p=e` (p = c, grade C, n 112) must REJECT; P2 `a=u` on a harness key g1/key_P2.tsv (key.tsv with
  a set to o) must ACCEPT. If P1 does not reject or P2 does not accept, every hypothesis below is a NON-TEST (logged only).
- H1 `vdash=d` (ours t, n 8); H2 `2=s` (ours r, n 10); H3 `eloop=a` (ours c, n 36); H4 `ls=e` (ours m, n 40); H5 `K=h` (ours s, n 28);
  H7 `iii=et` (his '###' = et; ours e, n 68); H8 `blot=NULL` (n 1: undecided by the tool's own rule, logged); H9 `x=NULL` (ours f, n 11).
- H6 (6 in his pair 76 = le): harness g1/ciphertext_76.tsv where every adjacent `7 6` in one line (n 19) is one token `76`, key g1/key_76.tsv =
  key.tsv + `76 = ie` (the current reading of 7+6); P1 re-run on this harness must reject; H6 `76=le`. The 7 tokens of 6 outside a pair untouched.
- Any group-1 or f/dia label MAPPED in Part 1 to a value different from key.tsv gets the same --try (H10.., named in the result) if the box
  allows; otherwise named as the next step.
- Reading: tool verdict accept = his value supported at M by --try (recorded in g1/concordance_g1.tsv, not in key.tsv: MQS-CROSSWORD rule, an
  accepted value stays M and key.tsv is not edited in this job); reject = our value kept, conflict stays logged (rule 4); undecided = logged.
Cap USD 3.5, box 70 min (16:32-17:42 UTC); stop before a unit that would cross 80% of either.

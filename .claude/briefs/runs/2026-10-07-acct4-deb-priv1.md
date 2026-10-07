# DEB-PRIV1 -- Debosnys museum scans: inventory, then a sign-match crib pass (private repo only)

Written by LANE DEB-RUN (account 4, session_01KBx2V5yEGzw3yFXtCMgaAz), 7 Oct 2026 21:5x UTC by date -u.
Run IN the account-4 standing session (the only one with the private repository). Opus 5.5. Cap USD 8; box 75 min.
Unit pricing (CLAUDE.md Usage 6): 43 scans; step 2 is one Sonnet subagent call per scan on line/region crops
(`tools/iiif_lines.py --image <scan> --out <private scratch dir>`, pasted before the first call), about 0.15 USD per
call -> 43 x 0.15 = 6.5 + 1 reconciliation unit; stop before a unit that would cross 80 pct of cap or box.

## Why (ciphers/debosnys-1883/ITERATE.md, H66/H67)
Public-data order instruments are spent: at the transcription's 15 pct noise even a perfect null-stripper on all
1,138 signs leaves too little order to test (oracle ceiling). The museum's 43 clear-text scans are the one new text
in hand. A crib from them needs no order test: a cipher sign, a monogram (H.D.D.L.M.F. appears in clear inside c2),
a numeral habit (516 on c2a) or a cipher-like passage in his own clear writings.

## Steps
0. RESTRICTED.md (ciphers/debosnys-1883/) binds every step: no image, crop, transcription, quotation or description
   of a scan enters the PUBLIC repository, a ROOM line, an artifact or a prompt outside the private repo.
1. Inventory (no image calls): read the private repo's own Debosnys notes/log; list what has already been done on
   the 43 scans (file names stay in the private repo). If a sign-match pass already exists, stop after step 1 and
   report only "already done, see private log".
2. Sign-match pass: for each scan, one subagent call on its crops with the public 160-id inventory sheet
   (ciphers/debosnys-1883/glyphs/, public) as reference: does the scan contain (a) any cipher sign or pictogram from
   the inventory used as writing, (b) the monogram or 516, (c) a passage in an invented script, (d) a letter-form
   habit that resembles a frequent cipher sign (X, PCT, O-TILDE, Y-CURL)? Decoy control: two public non-Debosnys
   19th-c. handwriting images in the same calls; a decoy "yes" voids that call's yes.
3. Write results to the private repo only. Public side: one ROOM line and one ITERATE.md row saying only "DEB-PRIV1
   done: crib candidate found / none found, held per RESTRICTED.md" -- no content.
Report what was found and where it was not found; do not classify novelty.

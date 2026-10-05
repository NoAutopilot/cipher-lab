# DEST-COLLATE (written by account 3, 5 Oct 2026; run in the account-4 standing session, which has the private repo). Opus 5.5. Cap $5, box 45 min.

Target: ciphers/destaing-gerard-1779 (d'Estaing to Gerard, 30 Apr 1779, Clements Library, Clinton Papers 64:14). Read
NOTES.md section "Clements scan on hand (5 Oct 2026)" first.
Material: private repo NoAutopilot/cipher-lab-private, destaing-gerard-1779/Clinton_vol_64_fols_14-15.pdf (12 pages).
Three British copies of the cipher letter: copy A pdf p.2 (+p.3), copy B p.5, copy C p.7. Never commit images to the
public repo.

1. Extract pages 2, 5, 7 (pdftoppm -r 200), cut line crops with tools/iiif_lines.py --image <page> --out <scratch>.
   Two blind Sonnet passes per copy, line by line (6 calls) + 1 reconciliation unit; numbers only, "." separators.
2. Collate A/B/C against ciphertext.txt position by position: tools/reconcile_passes.py or a short script; write
   collation.tsv (pos, ciphertext.txt, A, B, C, agreed, note). A disagreement is settled from the image, never by
   majority alone; note copyist slips (which copy, what).
3. Fix ciphertext.txt only where all three copies agree against it (rule: never silently repaired -- log each change
   in NOTES.md with the collation row). Report: total groups, agreements, disagreements, corrections.
4. NOTES.md: new section, status line unchanged unless a gap closes; tools/gaps_check.py passes; image-check gap
   marked done. Push by explicit path; ROOM done line with counts and cost. Do not decode, no novelty words.

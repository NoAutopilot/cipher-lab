# Mazarin to Antoine de Bordeaux, 22 June 1654 (copy), BnF Mélanges de Colbert 11, ff.479-481

**Status: found-solved.**

## Item

DECODE R9482 ("Non-decrypted" in DECODE's own status field as of the 24 Sept 2026 catalogue crawl —
`sources/decode/records-non-decrypted-2026-09-24.tsv`). Metadata (Aymeloglu `decode-records.jsonl`): Sender
Cardinal Mazarin, Receiver Antoine de Bordeaux de Neufville (French resident in London under Cromwell), 1654,
6 pages, cleartext language French, symbol set graphic signs/alphabet/numerical. Picked up by this project as
row **DC6** in QUEUE.md's "DECODE non-decrypted records with images (LANE N diff of 24 September 2026)"
section, scored as `held_by: none` (not matched to our repo, Bourdeau's or Aymeloglu's) — that match is
**wrong**, corrected below.

Brief: `.claude/briefs/runs/2026-09-24-lane-n-csDC2.md`. This worker did not touch de-crypt.org or
archive.org (both held by other LANE N workers this session); everything below comes from the committed
census/diff TSVs, QUEUE.md, a fresh shallow clone of both solver repositories, and Tomokiyo's Cryptiana
snapshot already in `sources/cryptiana/`.

## Check-solved sweep, 24 September 2026

Run directly (not the Workflow tool), per `.claude/briefs/check-solved.md`.

- **Editions first.** BnF Mélanges de Colbert is an archival collection, not itself an edition; the sender's
  printed edition is Chéruel & d'Avenel, *Lettres du cardinal Mazarin* — Tomokiyo's own page (below) already
  checked it and reports it prints other letters of this date from Mélanges de Colbert **51** but not this
  piece (p.572); not re-verified independently this pass.
- **Web / lists (Cryptiana).** `sources/cryptiana/web/louisxiv0.htm`, section "Bordeaux-Mazarin Cipher (1654)"
  (quoted verbatim): *"BnF, Melanges de Colbert 11 ..., ff.479-481, is a copy of a letter from Mazarin to
  Antoine de Bordeaux from 22 June 1654 (DECODE R9482). The cipher looks similar to the above. ... This was
  solved by George Lasry in 2025."* No key image reachable in this pass (Gallica/DECODE not fetched), but the
  solved status and solver/year are stated directly by the specialist who catalogues this exact record.
- **Bourdeau (github.com/dbourdeau/cyphersolver).** `bordeaux/NOTES.md` table, item B (quoted verbatim):
  *"Mazarin → Bordeaux, 22 June 1654, copy; BnF Mélanges de Colbert 11 ff. 479-481 | R9482 | **solved by
  George Lasry, 19 Feb 2025**; key published on cryptiana (`louisxiv_0mazarin.png`); the ciphertext itself is
  not accessible here."* Bourdeau's own item A in the same file (a related 1653 Bordeaux cipher, R8390) is a
  distinct, still-unread record and is not this target.
- **Aymeloglu (github.com/aaymeloglu/unsolved-ciphers).** R9482 appears only in the raw catalogue harvest
  files (`catalogue/decode-catalog.csv`, `decode-records.jsonl`) and `catalogue/exclude.txt` line 31 (`9482`,
  no reason text attached in that file) — consistent with, not contradicting, the found-solved verdict above;
  no separate write-up.
- **DECODE.** Per brief, not queried live. The census diff (`sources/decode/records-non-decrypted-2026-09-24-diff.tsv`)
  still lists R9482's status as "Non-decrypted" and `held_by: none` — DECODE's own catalogue record has not
  been updated to reflect Lasry's 2025 solution, and neither the census-diff script nor the QUEUE.md ranking
  pass caught the match to Bourdeau's `bordeaux/` folder (shelfmark normalisation likely failed on "Mélanges
  de Colbert 11, f 479" vs Bourdeau's "BnF Mélanges de Colbert 11 ff. 479-481" — a leaf-range vs single-leaf
  mismatch). Flagged in ROOM.md for LANE N orchestrator; QUEUE.md's DC6 row corrected below.

**Verdict: found-solved.** Solved by George Lasry, dated 19 Feb 2025 by Bourdeau, published by S. Tomokiyo on
Cryptiana (`louisxiv0.htm`) with the key as `louisxiv_0mazarin.png` (not fetched this pass — Gallica/Cryptiana
image hosting out of this brief's host list). Per README's F-grades: **F1** — the plaintext/key is published
(Cryptiana, Bourdeau) but DECODE's own database record (the specialist catalogue for this collection) still
shows "Non-decrypted", so a DECODE catalogue correction is the contribution left to hand on, not a fresh
reading. No novelty claim made or implied (rule 10); this is a verifier-scope call to confirm, not made here.

## Correction to QUEUE.md

DC6's `held_by` should be `bourdeau:bordeaux`, not `none`, and its status is found-solved, not an open
transcription lead. See ROOM.md flag, 24 Sept 2026.

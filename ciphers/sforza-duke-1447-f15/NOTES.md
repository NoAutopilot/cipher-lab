open
Check-solved for this one letter (SFZ-D, 7 Oct 2026): Osio, Documenti diplomatici tratti dagli archivj milanesi vol. III (Milan 1872, IA bub_gb_88IStucIdgAC), the standard printed edition of the Visconti state letters, was searched whole by full-text grep (SFZ-0, same day: Cusago 32 hits, all 1431; no regest of a 23 Jan 1447 letter of the Duke); Mazzatinti, "Inventario delle carte dell'Archivio sforzesco contenute nei codici italiani 1583-1593 della Biblioteca nazionale di Parigi", Archivio storico lombardo X (1883), IA archiviostoricol10cava, read at its entry for cod. 1584 (printed p. 233-234, djvu text lines 10736-10780): "15. [Lettera] del Duca al medesimo (Cusago 23 gennaio). In cifre : membran." -- listed as cipher, with no "Traduzione" entry after it (contrast f.5/f.6 and f.8/f.9, "Traduzione della lettera precedente"); no decipherment of f.15 located.

# BnF italien 1584 f.15: the Duke's cipher slip, Cusago 23 Jan 1447 -- target folder (SFZ-D)

Worker SFZ-D for LANE ST-REBUILD (account 2), brief `.claude/briefs/runs/2026-10-07-acct2-st-rebuild-workers.md` (Wave 2).
Pool folder: `../sforza-italien1584-1447/NOTES.md` (SFZ-0). Key units: `../sforza-italien1584-1447/duke/`.

## Item

- BnF italien 1584 f.15 (Gallica ark:/12148/btv1b100373864, canvas 17, right page). Filippo Maria Visconti, Duke of Milan,
  to Francesco Sforza, Cusago 23 Jan 1447 (Mazzatinti's attribution and date; the slip is unsigned; later hand on the slip
  "1447, 23 janvier"). One slip, cipher only, 14 lines, about 600-650 signs (SFZ-0's estimate at 1200 px).
- f.17 (canvas 18) is the Duke's clear letter of the same day and place, signed, with two blanks; it is context, not a copy
  (SFZ-0). Used here for names only.

## Check-solved (SFZ-D, 7 Oct 2026; one letter, reusing SFZ-0's pool pass by citation)

- **Osio III** (standard edition of the Visconti/Sforza diplomatic letters): SFZ-0's whole-volume grep, cited above; no f.15.
- **Mazzatinti 1883** (ASL X, IA `archiviostoricol10cava`, `_djvu.txt` downloaded once, 7 Oct 2026, read at cod. 1584):
  f.15 listed "In cifre : membran.", no translation listed after it. The same list gives the Duke's glossed pairs used for
  the key: f.5 (Abiate 10 Jan, in cifre) / f.6 traduzione; f.8 (Abiate 11 Jan, in cifre) / f.9 traduzione; f.23, f.24 (Milano 5
  Feb, in cifre); f.30-31 (two letters, Milano 9 Feb, in cifre); f.36-37 (two letters, Milano 12 Feb, in cifre). SFZ-0 had read
  the f.8 inventory line as "f.8 / f.10": f.9 is the contemporary translation and f.10 a later clear copy (both seen on the
  images, canvases 11 and 12).
- **Google Books API** (key, country=US), two full-text queries on 7 Oct 2026: `"23 gennaio 1447" Cusago` (30 hits: Mazzatinti's
  ASL 1883 inventory itself, Verri's Storia di Milano on a 23 Aug 1447 edict, the Archivio civico inventory 1932 on a 3 Jan 1447
  letter to the podestà; none is this letter), `"Cusaghi" 1447 cifra Sforza` (0 hits).
- **Internet Archive full text** (be-api fts, `"Cusago 23 gennaio"`): 4 Italian items, the Mazzatinti inventory and ASL volumes;
  no edition of the letter.
- **DECODE** (login-free listings in `sources/decode/`, SFZ-0): no italien 1584 record.
- **Solver repositories**: Bourdeau's local snapshots `sources/cyphersolver/2026-10-01..03`, no hit for italien 1584 /
  Sforza / Visconti 1447 (SFZ-0 grep; re-run by SFZ-D: see "Premise check" (b)). Aymeloglu's repository: not re-checked.
- **Cerioni 1970** (La diplomazia sforzesca nella seconda meta del Quattrocento e i suoi cifrari segreti) is a study of the
  Sforza chancery's cipher keys from 1450 on, not an edition of the 1447 Visconti letters; it was not opened in this pass. It
  is relevant as a possible known key (Escalation, known-keys), not as the edition of this letter.

Verdict: `open` -- no decipherment or print of f.15 located in the edition, inventory and full-text searches above.

## Web and blog check

SFZ-0's open-web pass for the pool (seven queries, the Cipher Mysteries "Milanese enciphered letters" post and first 100,000
characters of its comment thread, voynich.ninja thread 5828; Cryptiana blog and Cipherbrain / klausis-krypto-kolumne logged as
not covered by a site search) is reused by citation (`../sforza-italien1584-1447/NOTES.md`, "Web and blog check"). For this
letter, SFZ-D added the two Google Books and one IA full-text query above. No decipherment of f.15 was found on the web, on
Cipher Mysteries, Cryptiana or Cipherbrain as far as those passes reached.

## Premise check

(a) Decipherments the folder already mentions: none for f.15. SFZ-0 records f.17 as a same-day clear companion with blanks
(not a decipherment); Mazzatinti lists no translation for f.15.
(b) Other solvers' working files: `grep -ril "italien 1584\|visconti\|cusago" sources/cyphersolver/` (SFZ-D, 7 Oct 2026): no file.
Aymeloglu's repository not re-checked.
(c) Physical neighbours: f.14 (Pusterla, clear, 21 Jan), f.16 (not listed by Mazzatinti), f.17 (Duke clear, 23 Jan, blanks),
f.18 (instruction to the ambassadors to Aragon, s.d.). None is a copy of f.15's cipher text (SFZ-0, canvases 16-19 at 1200 px).
(d) Recipient's side: Francesco Sforza at Pesaro; the Sforza-side editions are Osio III (read) and the Carteggio degli
oratori (Battioni 2013, from 27 Feb 1447, after this letter's date). No recipient-side decipherment located.

## Intake gate output

`python3 tools/intake_gate_check.py sforza-duke-1447-f15` (7 Oct 2026, 22:02 UTC):

    sforza-duke-1447-f15: open (line 1) -- edition/page or full-text-search citation found within 6 lines
    exit 0

## Key work and result (SFZ-D, 7 Oct 2026): no decode of f.15

Details, numbers and files are in `../sforza-italien1584-1447/duke/NOTES.md`. In short:
- S1: the Amidani key (`../sforza-italien1584-1447/amidani/key.tsv`) on the Duke's glossed slip f.8 scores 0.267 against
  shuffle mean 0.295 / p95 0.334: FAIL, so the Duke's key is not Amidani's at this transcription.
- S2: the Duke's own key from two glossed pairs (f.5/f.7, f.8/f.10), leave-one-letter-out G1 FAILs: mean held-out
  0.441 (run 2, dateline corrected; run 1 0.435) against the 0.60 gate, and f.8 falls below its own shuffle p95 (0.384 vs 0.408).
- S3 (f.15 crop, two passes, decode, controls) was therefore not run, per the brief's stop rule. f.15 has no transcription,
  no decode and no reading; `tools/judge_plaintext.py` was not run (nothing to judge).

## Remaining gaps (SFZ-D, 7 Oct 2026)
Read so far: 0 signs of f.15 transcribed or read; the Duke key gate G1 failed (0.441 mean held-out, 2 units)
- f.15 decode - blocker: not-attempted; needs a Duke key that passes G1 first (SFZ-NEXT, 8 Oct 2026: unit 4 of its brief not started, it would have crossed 80% of the cap; tools/data/it15 now exists for a judge); next: settle the Duke's sign inventory on f.5+f.8 (TRANSCRIPTION.md, sign sorter or glyph_atlas) with a second blind reader, rerun ../sforza-italien1584-1447/duke/g1_duke.py, ~$4
- f.17 blanks vs f.15 - blocker: not-attempted; whether f.15's cipher fills f.17's two blanks is unexamined; next: only after a readable key, ~$1

## Escalation (SFZ-D, 7 Oct 2026)
- [x] siblings: the Duke's glossed pairs f.5/f.7 and f.8/f.10 used; f.23-24/f.26, f.30-31/f.29, f.36-37/f.35 not yet
- [x] clear-pages: f.17 (same-day clear letter) noted as context; no copy of f.15 exists in the volume per Mazzatinti
- [ ] known-keys: Cerioni 1970 / ASMi Visconti cipher registers not checked
- [ ] print: no print of f.15 located (check-solved above); verifier pass belongs to a later reading
- [x] key-rebuild: attempted, G1 FAIL
- [ ] image-check: alphabet settling + second reader on the Duke's glossed slips
- [ ] retry: G1, then S3 on f.15
Verdict: keep going: 2 internal gaps; cheapest next: settle the Duke's sign inventory and a second reader on f.5+f.8, ~$4

## Requests (SFZ-D, 7 Oct 2026)

gallica.bnf.fr: 5 overview canvases at 1400 px (c9-c13), 2 info.json, 4 native regions (c9, c10, c11, c12) = 11, one at a
time, >= 2 s apart, no errors. archive.org: 4 (advancedsearch 2, download 1 `_djvu.txt`); be-api.us.archive.org: 1;
googleapis.com/books: 2. No other host.

# lope-hurtado-1522 -- hypothesis families and data conflicts

Append-only. Family rows are written by `tools/family_run.py` (CLAUDE.md rule 3); none yet -- every reading on this target
so far came from a key source (Bourdeau's clear-copy crib, then Kolosova's published tables), not from a family.

## Data conflicts between two H-grade key sources (CLAUDE.md rule 4; logged 17 Oct 2026, account-4 parent)

Witness A: Bourdeau, dbourdeau/cyphersolver `targets/lopehurtado/key_codes.tsv` and `key_1522_from1524.tsv` (MIT / CC BY 4.0, credited),
values recovered from the contemporary clear copies of R9644 (ff.241-242) and R9649 (f.268) and from the 1523-24 letters.
Witness B: Kolosova 2024, *El lenguaje cifrado en tiempos de Carlos V (1521-1527)*, Cifrario 7 (pp.200-202), reconstructed from her
78-letter edition; our transcription `kolosova2024_cifra7.tsv` (notation: 3 = z, y = ɣ, s = ʃ).
Where the two disagree a code is graded M in any letter whose context does not settle it; neither value is taken by majority.

| code | A (Bourdeau) | A's witness | B (Kolosova) | B's witness | status |
|---|---|---|---|---|---|
| top | por (confirmed) | R9644 f.238 'top ton' = porque, three contexts | razón; por = tog | Cifrario 7 p.202 | open: p/g in the printed group; test at every occurrence |
| zar / 3az | de (confirmed) | R9644 three contexts; 'zar rab' = de V. Mt. | de = 3az as printed | Cifrario 7 p.201 | open: the printed final letter (z or r) is our reading at 272 ppi; likely the same group |
| tod / tud | otro (+s = otros) (confirmed) | R9644 f.238 exact slot | otra = tud | Cifrario 7 p.202 | open: o/u |
| ʃop / sop | bi (confirmed) | 1524 letters, R9634 'obieran', 'avia' | tiempo = sop | Cifrario 7 p.202 | open: Bourdeau's value is a syllable from the 1524 key carried back; Kolosova's a word |
| ʃal / sal | esta (confirmed, 1524 retry) | R9634 14r10 'estan', 15v10 | todo = sal | Cifrario 7 p.202 | open |
| xu | gente (confirmed) | R9645 f.243v gloss 'la gente de v. mgd' | guerra (cifra 10); gente = xe (cifra 10) | Cifrario 10 p.212 | open only if R9645 is in cifra 10; in cifra 7 Kolosova lists no xu |

Agreements (A confirmed, B H): ton que, xud hombre, xul lo, xon mas, tu no, sub si, yaf es, 3un da, teg para, sid Su Santidad, xil le,
xur na, yub el, taf papa, yof esta, yuc en, yon Francia, 3ed arçobispo, tef paz, su se, 3il con, rab Vuestra Majestad, yib duque,
tel pues, 3uf cardenal, xug la, sed su -- 27 codes. Not in B: tab nunca, ɣm fue, ta no, teʒ nueva, ʃʃ su, yan fortaleza.

### Tested at every occurrence (LOPE-KEYAPP, 17 Oct 2026; rows in reading_kolosova_gain.tsv; none resolved, all stay M)
top: context admits por at 6/6 R9634 + 1/1 R9646 occurrences, razón at none; R9649's clear f.268 also has top = por; Bourdeau's tog = por x5
in R9634. ʃop: a syllable (bi) inside spelled words at 7/7; tiempo admitted at none. tod: otro at 1/1 (*lo otro*). ʃal: both admitted at 4/4.
zar: de at all 30 (both witnesses). xu: gente at 7/7 (not in cifra 7). The printed letters (3az, tud, top/tog) still need a re-read of the scan.

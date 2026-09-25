found-solved

# Bernardino Naro / Nuncio Damiata, Paris nunciature to the Secretariat of State — ASV Segr. Stato, Francia, doss. 62 (QUEUE.md row D4)

DECODE record cluster: R59, R60, R61 ("Non-decrypted", doss. 62) beside R71 ("Partially decrypted", doss. 64,
same fond). Source: QUEUE.md "Neighbour-record recovery candidates" row D4. Checked 25 Sept 2026 by LANE DX
worker NB-FI, per the neighbour check-solved brief (`.claude/briefs/runs/2026-09-25-lane-dx-nbcs.md`), before
any DECODE login this session (worker never logged in, per brief).

## 1. Bourdeau (dbourdeau/cyphersolver, shallow clone, 25 Sept 2026)

`grep -ril "naro\|damiata"` over the whole clone finds `cyphersolver/damiata1624/` — a finished folder, dated
21 September 2026 (four days before this check), that covers exactly this cluster. Quoting his NOTES.md:

> "Verdict: read at the time. Both cipher passages carry the Roman office's decipherment on the leaf, and the
> reconstructed key already on the DECODE records fits them." Catalogue entry 256 ("Nuncio Damiata (France) to
> The Secretariat, 22 Dec 1624") is resolved and removed.

His folder identifies the records precisely:
- **R60** (ff. 137-138): the nuncio (Bernardino Spada, archbishop of Damiata)'s letter, Paris, 15 August 1625.
  Three short cipher runs on f. 138r, **each with the period decipherment written above it on the leaf** (an
  interlinear gloss, the Thurloe/Birch pattern check-solved.md flags).
- **R61** (ff. 186-187): Bernardino Naro, Paris, last day of February 1625, with a *Copia* of a Brussels letter
  (21 Feb 1625). One letter-sign cipher line and two figure lines at the foot of f. 186r, again glossed above
  the figures on the leaf.
- **R59** (ff. 126-127; catalogue's "Naro, 3 Jan 1625" is the volume's run-start date, not the letter's):
  Bernardino Naro, Paris, 14 April 1625. Three cipher passages, each glossed above (*il Generale delle galere*;
  *di procurare l'Ambasceria ordinaria di Roma*; *Il card. di Lione lo contrarià*), and independently decoded
  with the reconstructed key against the same three phrases.

The key is George Lasry's 24 Oct 2020 transcription (filed as DOC_D3246/D3247 on the DECODE records
themselves) of the alphabet reconstructed by **Norbert Biermann and Thomas Bosbach** for ASV Francia 64,
1625 — the same key family Biermann broke in 2018 on doss. 64 ("64/10" = **R71**, our own row's cited
Partially-decrypted neighbour). Bourdeau's note: "Francia 64, R62-R71 (catalogue 257): already read. Biermann
broke the key in 2018 on 64/10 (R71), and each record carries its transcription, the key and a
codebreaker.py decryption. It is the same key family as R59-R61." So R71 (this row's own "neighbour") is
itself already read and its key already applied by Bourdeau to R59-R61 (this row's "letter" ids) as a
cross-check, on top of the leaf's own contemporary gloss.

DECODE's own "Non-decrypted" status on R59/R60/R61 is therefore stale bookkeeping, not evidence the material
resists reading — exactly the pattern check-solved.md's own precedent notes (a specialist project's catalogue
already links the item; DECODE's cached metadata has not caught up).

## 2. Aymeloglu (aaymeloglu/unsolved-ciphers, no licence, cited not copied)

`grep -ril "naro\|damiata"` over the whole clone hits only the cached DECODE catalogue files
(`catalogue/decode-catalog.csv`, `catalogue/decode-records.jsonl`) confirming the same Holder/Sender/Status
fields quoted above (Holder "Vatican Secret Archive, i. 1025, Segretario di Stato, doss. 62/64"; R59/60/61
Status "Non-decrypted"; R71 Status "Partially decrypted", Available Documents "Cleartext Deciphered text Key
Transcription"). `TARGETS.md`/`SHORTLIST.md` do not name Naro, Damiata or this fond — untracked there.

## 3. Editions

WebSearch, 25 Sept 2026: "Bernardino Naro nunciature Paris 1625 Acta Nuntiaturae Gallicae edition" —
Cambridge Core / academic.oup.com hits list the published Acta Nuntiaturae Gallicae volumes by nuncio
(Santa Croce 1552-54, Castelli 1581-83, Frangipani 1568-87, Ranuccio Scotti 1639-41, Ranuzzi 1683-89,
etc.); none for the Paris nunciature of 1623-27 (Bernardino Spada, archbishop of Damiata) or for Naro
specifically was found. Not read further this pass (edition status for this exact nunciature: unconfirmed
either way; not needed for the verdict below, since Bourdeau already read the leaf itself, not merely a
print). Meister's 1906 "Die Geheimschrift im Dienste der päpstlichen Kurie" (named in the brief as prior
literature on nuncio ciphers of this period) not opened this session — not needed given §1.

## 4. Community

`grep -ril` over `sources/cryptiana/` for "naro", "damiata": no hits. Cipherbrain and model-solve
announcements not separately queried (Bourdeau's own dated write-up already settles the cluster; see
check-solved.md's own steer to stop once a named source states the specific record).

## Verdict

**found-solved, Bourdeau's lane** (same shape as QUEUE row D1/pallotto-1628, ciphers/pallotto-1628/NOTES.md).
Bourdeau's `damiata1624/` folder, dated 21 Sept 2026, reads all three "Non-decrypted" letters (R59, R60, R61)
directly off the leaf's own contemporary interlinear decipherment, cross-checked against the Biermann/Bosbach
key already filed on the fond (and already applied by him to the "Partially decrypted" neighbour R71 too).
DECODE's Non-decrypted/Partially-decrypted statuses on all four ids are stale. No fresh recovery or
cryptanalysis work is owed here. Per rule 10, this is a search-result statement (Bourdeau's dated repository
entry), not a novelty claim — a verifier would need to check whether Bourdeau's reading, or the underlying
Biermann/Bosbach key, has itself been printed anywhere, but that question is now his lane's, not this queue
row's.

Nothing here needs the DECODE login. No record ids owed to the LANE DX login worker for this cluster.

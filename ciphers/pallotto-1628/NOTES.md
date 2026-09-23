found-solved

# Giovanni Battista Pallotto, nuncio extraordinary to Emperor Ferdinand II (Mantuan succession mission), dispatches of 1628 — BAV Barb.lat 6956

DECODE record cluster (QUEUE.md row D1): R233, R239, R241, R242, R253 (all "Non-decrypted") beside R221
("Partially decrypted"), all Sender "Germania: Giovanni Battista Pallotto", Receiver "Nunzio all'Omperatore"
[sic, DECODE's own transcription of "all'Imperatore"], Region Germany, catalogue date 1628-01-01 (a placeholder
day, per QUEUE.md), same shelfmark. Part of a wider run the catalogue gives as DECODE R215-R285 plus R318 (about
70 ciphered sheets), catalogue entry 236 in `cs-recheck/CATALOGUE.md` (dbourdeau/cyphersolver).

- Source: QUEUE.md row D1 ("Neighbour-record recovery candidates"); sources/solver-diffs/2026-09-23-decode-neighbours.tsv,
  lines for `bav_barb.lat_6956` (ids 253, 242, 241, 239, 233, all matched to neighbour 221).

## Check-solved sweep (23 September 2026)

### 1. Editions (Nuntiaturberichte aus Deutschland / Kiewning / Quazza / Barberini editions)

Web search (WebSearch tool; archive.org and HathiTrust themselves are egress-blocked in this environment,
so volume text itself could not be opened, only catalogue/publisher metadata):

- Query "Kiewning Nuntiaturberichte aus Deutschland Nuntiatur des Pallotto 1628 Band 1": confirms
  **Hans Kiewning (ed.), *Nuntiaturberichte aus Deutschland*, IV. Abteilung (17. Jahrhundert), Band 1:
  *Nuntiatur des Pallotto 1628* (Berlin, 1895; CVI + 380 pp.; reprinted Torino 1973)** exists and covers
  exactly the year DECODE gives (as a placeholder) for this cluster, via kulturkaufhaus.de, DHI Rom's own
  Nuntiaturberichte page (dhi-roma.it/nuntiaturberichte.html), Google Books and WorldCat. Band 2, covering
  1629 (BAV Barb.lat 6960, the sibling volume, not this cluster), is the volume already confirmed word-for-word
  against the register by Bourdeau (see §5 below) — Band 1 was not itself opened this session (HathiTrust/
  archive.org blocked; Google Books full-text not queried with a phrase this pass, see Edition risk below).
- Quazza's *La guerra per la successione di Mantova e del Monferrato* and the "Nunziature di Vienna" series
  named in the brief were not separately searched this pass (time/budget); flagged as unchecked below.
- No Barberini-correspondence edition specific to this exact cluster was found or ruled out.

### 2. Scholarship on this file (the "Sacré 2020" paper named in QUEUE.md, and DECODE-derived papers)

QUEUE.md row D1 cites "Sacré's 2020 Cryptologia paper on papal ciphers (Barb.lat 6956/6960)". WebSearch found
no such paper or author; the actual 2020 Cryptologia paper covering exactly these two shelfmarks is:

**George Lasry, Beáta Megyesi, Nils Kopal, "Deciphering papal ciphers from the 16th to the 18th Century",
*Cryptologia* (2020), pp. 1-62** (DOI 10.1080/01611194.2020.1755915; open-access copies at
uu.diva-portal.org/smash/get/diva2:1511292/FULLTEXT01.pdf and researchgate.net/publication/342406480).
Written up as part of the DECRYPT project. Search result text: "hundreds of enciphered papal letters from the
16th, 17th, and 18th centuries were deciphered, and dozens of keys were recovered"; the paper's own source
material explicitly names both digi.vatlib.it/view/MSS_Barb.lat.6956 (70 letters, 1628) and MSS_Barb.lat.6960
(28 letters, 1629). The QUEUE.md citation is very likely a mis-attribution of this same paper (the shelfmarks,
year and letter counts match exactly); this was **not** independently confirmed by opening the PDF this
session (not fetched — flagged as an unchecked step, since HathiTrust/tandfonline were not tried and the
diva-portal/researchgate mirrors could plausibly be reachable but were not fetched this pass).

### 3. Cryptiana snapshot / Cipherbrain

`grep -ril` over `sources/cryptiana/` for "pallotto", "barb", "6956", "ferdinand ii", "nuncio": one bare
hit for "Pallotto" in `sources/cryptiana/web/vatican.htm` (no surrounding context recovered by the grep;
the page is Cryptiana's general Vatican-ciphers page, consistent with awareness of the correspondence, not a
solve claim). No hit in german.htm or habsburg.htm. Cipherbrain: WebSearch for the 2020 paper surfaced no
Cipherbrain thread specific to Barb.lat 6956; not separately queried by name this pass (unchecked).

### 4. DECODE (blocked; catalogue fields only, via ay/'s cached copy)

de-crypt.org is fully egress-blocked from this environment (per CLAUDE.md's confirmed environment note and
this session's own history); URLs that would need to be opened directly:
`https://de-crypt.org/decrypt-web/RecordsView/221`, `/233`, `/239`, `/241`, `/242`, `/253`.
Cached fields from `ay/catalogue/decode-catalog.csv` and `decode-records.jsonl` (aaymeloglu/unsolved-ciphers,
harvested 19-23 Sept 2026 per that file's own header):

| id | pages | status | sender | receiver | date (catalogue) |
|---|---|---|---|---|---|
| 221 | 1 | Partially decrypted | Germania: Giovanni Battista Pallotto | Nunzio all'Omperatore | 1628-1-1 |
| 233 | 4 | Non-decrypted | " | " | 1628-1-1 |
| 239 | 4 | Non-decrypted | " | " | 1628-1-1 |
| 241 | 7 | Non-decrypted | " | " | 1628-1-1 |
| 242 | 4 | Non-decrypted | " | " | 1628-1-1 |
| 253 | 4 | Non-decrypted | " | " | 1628-1-1 |

All six share holder string "Vatican City, Bibliotheca Apostolica Vaticana, Barb.lat 6956 BAV_Barb.lat_6956-N"
(N = 7, 19, 25, 27, 28, 38 respectively), Cleartext/Plaintext language Italian.

### 5. Bourdeau (dbourdeau/cyphersolver, commit 2e9ec016, 23 Sept 2026, MIT code / CC BY 4.0 text)

`grep -ril` over the whole clone for "barb", "6956", "pallotto" hits `pallotto1629/` (NOTES.md, profile.json,
decode_records.txt, docs/pallotto1629.html, key6956/) and the two catalogue files. Reading
`pallotto1629/NOTES.md`, `CATALOGUE.md` and `SOLVED_CATALOGUE.md` directly (Bourdeau's own text, CC BY 4.0,
quoted, not copied as code):

**This exact cluster is covered, and the sibling shelfmark carries the key.** Bourdeau's write-up (titled
"Pallotto to Barberini, 1629", primarily an analysis of the *sibling* volume BAV Barb.lat 6960, DECODE
R286-R313) states, in an update dated 21 September 2026:

> "Barberiniani Latini 6960 uses the same key as Barberiniani Latini 6956 (which was found by Norbert Biermann
> and Thomas Bosbach) — I found this years ago, but the DECODE DB was never updated." [George Lasry, relayed
> by Daniel/Bourdeau; checked and confirmed by Bourdeau]

and gives the key's actual location: **filed as attached documents on DECODE record R215** (Barb.lat 6956,
the first sheet of the same run our cluster sits in) — `DOC_R215_D1506` (Biermann's key, March 2018),
`DOC_R215_D1507` (Bosbach's), `DOC_R215_D1508` (a merged version), `DOC_R215_D1505` (a decryption run against
R215). This session read all three key documents directly (copies in `cs-recheck/pallotto1629/key6956/`): a
two-digit homophonic-with-nulls alphabet (nulls 1 and 8; a=00/02/20, e=09/30/90, i=05/40/50, o=03/07/70, etc.)
plus two-digit syllable/short-word codes (47 che, 52 con, 57 per, 69 di, 73 la, …) and three-digit nomenclator
groups for names and titles (200 commissario imperiale, 360 duca di Mantova, 460 imperatore, 504 Mantova,
522 Monsignore, 670 Sua Maestà, …). Applying this key (`key6956/apply.py`, a DP segmentation) to the sibling
volume's 28 transcriptions reads all of them into running Italian, confirmed word-for-word against Kiewning's
printed Band 2 (R286 opens "ho riceuto la risposta datami in scritto…" = Kiewning Nr. 153 verbatim).

Bourdeau's own catalogue entry states the status of Barb.lat 6956 itself in plain terms — `CATALOGUE.md` line
357 (entry 236, our exact shelfmark and DECODE range R215-R285+R318, i.e. covering all six of our ids):

> "236 — Giovanni Battista Pallotto (Vienna), 70 ciphered despatches of 1628, BAV Barb.lat. 6956, DECODE
> R215–R285, R318: **solved by others**. Norbert Biermann and Thomas Bosbach broke the key in March 2018;
> their keys and a decryption are filed as documents on DECODE R215 (only R215–R225 are marked 'Partially
> decrypted'). **Removed 21 Sept 2026.**"

and `SOLVED_CATALOGUE.md` line 203 records the parallel confirmed reading of the 6960 sibling under the same
key, again crediting Biermann, Bosbach and Lasry by name and date, and noting the reading is not complete (about
1,750 three-digit nomenclator groups used in 6960 are missing from the 6956 key as filed and stay unresolved).

**What this means for R233, R239, R241, R242, R253 specifically**: Bourdeau did not personally run the
6956 key against these five records (his own applied decryption is of the 6960 sibling, not 6956) — so there
is no line-by-line confirmation in this repository, this session, or (as far as this sweep found) anywhere
public, that the key reads these five particular sheets end to end. But the key itself is not new or
withheld: it was recovered by Biermann and Bosbach in March 2018, is filed publicly on DECODE against R215
(the same file, same run, same cipher system per the catalogue's own description of Barb.lat 6956 as one
homophonic-with-nomenclator system across its ~70 sheets), and Bourdeau — an independent, credited solver —
has removed the whole 236-entry cluster (which contains all six of our ids) from his active catalogue as
solved by others. DECODE's own "Non-decrypted" status on R233/239/241/242/253 is therefore very likely stale
bookkeeping (DECODE itself marks only R215-R225 as even "Partially decrypted", i.e. it has not been updated
to reflect the 2018 key at all), not evidence that the cipher resists the known key.

### 6. Aymeloglu (aaymeloglu/unsolved-ciphers, no licence, cited not copied)

`grep -ril` over the whole clone for "barb", "6956", "pallotto": no hits outside the cached DECODE catalogue
files used in §4 above (`catalogue/decode-catalog.csv`, `catalogue/decode-records.jsonl`). `TARGETS.md`,
`SHORTLIST.md` and `CATALOGUE.md` in that repository do not mention Pallotto, Barb.lat 6956 or 6960 at all —
this cluster is untracked there.

## Edition risk

**High, and separately from the key question.** Two independent facts point the same way: (a) Kiewning's
*Nuntiaturberichte aus Deutschland* IV/1, *Nuntiatur des Pallotto 1628* (Berlin, 1895) is a real, findable
volume covering exactly the year this cluster is catalogued to, in the same series whose Band 2 (1629) Bourdeau
has already confirmed prints the *contemporary Roman decipherments* of the sibling volume's ciphered dispatches
verbatim; (b) the governing 2020 Cryptologia paper (Lasry, Megyesi & Kopal) treats Barb.lat 6956 and 6960 as one
project with keys recovered for both. A worker with archive access must check, before claiming any reading of
R233/239/241/242/253 as a result: (1) whether Kiewning's Band 1 (1895) heads any of the corresponding despatches
"dechiffr." the way Band 2 does for 6960 — if so the plaintext is already in print and reading the cipher
independently is confirmation, not discovery, exactly as the Randolph/Caligula C II precedent in ROOM.md warns;
(2) the full text of the Lasry/Megyesi/Kopal 2020 paper itself (not opened this session — HathiTrust/tandfonline
blocked, the diva-portal/researchgate open-access mirrors were found but not fetched), which may already publish
the reading or a fuller version of the key than the DECODE-filed documents; (3) Quazza's *La guerra per la
successione di Mantova e del Monferrato* and the Nunziature di Vienna series named in the brief, neither checked
this pass.

## Verdict

**found-solved.** Per rule 10, this is reported as a search result, not a novelty claim: the key for this exact
shelfmark (Biermann & Bosbach, March 2018) is filed publicly on DECODE R215 and independently confirmed by
Bourdeau against the sibling volume; Bourdeau's own catalogue lists the whole Barb.lat 6956 cluster (which
contains all six ids in this brief) as solved by others and removed from his active list on 21 September 2026.
No line-by-line application of the key to R233/239/241/242/253 specifically was found in this sweep, and the
edition question (Kiewning Band 1, the 2020 paper's own text) is not closed — a worker who wants a citable
reading of these five records still has to run the known key against DECODE's transcriptions and check both
editions named above before any claim of a result. Not staged as Stage 2 "verified unsolved": this cluster is
not unsolved. Recommended next step is a short access/reconciliation worker (apply `key6956/apply.py` to
R233/239/241/242/253's DECODE transcriptions and check Kiewning Band 1), not a fresh cryptanalytic campaign.

open
Gomberville, *Les Mémoires de Monsieur le duc de Nevers* (Paris 1665), Partie 1 (Gallica bpt6k6435941k) and Partie 2 (bpt6k9738856z), full-text search (Gallica ContentSearch "1571", "Birago", "Lodouico", "Avril 1571", "Ianvier 1572", "Mars 1572") read by this worker on 2 Oct 2026: no Birago letter of 1571-72 in either part (the 1571 hits in Partie 1 are the English marriage negotiation, PAG_562-618); no other edition of the Birago-Nevers correspondence exists (searched, see below).

# Lodovico Birago to the Duke of Nevers, BnF fr.3252, three cipher letters (26 Apr 1571, 8 Jan 1572, 13 Mar 1572)

NEVBIR-3252 (2 Oct 2026, account 2 worker for the account-3 orchestrator), brief
`.claude/briefs/runs/2026-10-02-acct3-nevbir-3252.md`. Source of the candidates: `../nevers-birago-fr3251-1572/BIRAGO-POOL.tsv`
(BIRAGO-SCOUT). Sibling folders: `../ceppo-nevers-fr3251-1570s` (Ceppo-Nevers key, fr.3251 1570-71 letters, and the fr.3252
f.36-37 witness of 5 Apr 1571), `../birago-nevers-1571` (fr.3251 f.119, the Nov 1571 numerical cipher),
`../nevers-birago-fr3251-1572` (Nevers-Birago 1572 key). Tools and keys are used from those folders by path.

## Sources

- BnF français 3252, Gallica `https://gallica.bnf.fr/ark:/12148/btv1b9060232m` (184 canvases, labels all NP; canvas = folio + 1,
  confirmed by eye on the ink foliation of canvases 48 (47), 101 (100), 118 (117) this session). Finding aid
  (as harvested in Bourdeau's `research/gallica_sweep/bnf_candidates.txt`, BnF notice text): no.30 "Lettre, avec chiffre, de
  « LODOVICO BIRAGO » au « duca di Nevers,... Da Saluzzo, li 26 aprile 1571 ». En italien"; no.67 "... Da Saluzzo, li 8 di
  genaio 1572 ». En italien"; no.77 "... à monseigneur le duc de Nyvernois,... De Saluces, le XIIIme mars 1572".
- Images on disk: `images/` (overviews, 1600 px, canvases 47-49, 100-102, 117-119; two native crops of canvas 101). Manifest
  `images/manifest.json`.

## Layout

| no. | folio (canvas) | date | language | cipher | est. signs | decipherment on the leaf | first-test key |
|---|---|---|---|---|---|---|---|
| 30 | f.47r (48 right) | Saluzzo 26 Apr 1571 | Italian | symbol cipher, ~21 lines from "Visto che non ui è che ri pensi." to "Il Grande mi scriue", foot of f.47r; letter continues in clear on f.47v, ends f.48r with signature | ~850 | none seen (overview + premise (c)) | Ceppo-Nevers printed key (Tomokiyo), as applied in `../ceppo-nevers-fr3251-1570s` |
| 67 | f.100r (101 right) | Saluzzo 8 Jan 1572 | Italian | digits with `+` separators, two runs: L1-L8 (after "harebbe a caro 76") and L9-L12 (after "Io dico la pura et mera uerità") | ~800 digits | none seen | Nov 1571 numerical (f.119) or Nevers-Birago 1572 |
| 77 | f.117r (118 right) | Saluces 13 Mar 1572 | French (secretary hand) | symbol cipher, ~13 lines between "Seullement Monseigneur je vous diray" and "Monseigneur je supplie Dieu" | ~330 | none seen | inventory and design check only |

## Check-solved (NEVBIR-3252, 2 Oct 2026)

1. **Web search** (four plain queries, 2 Oct 2026): `Lodovico Birago Nevers "26 aprile 1571" OR "8 gennaio 1572" OR "13 mars 1572"
   Saluzzo lettera` (Wikipedia Saluzzo marquises, unrelated catalogue rows; nothing on these letters); `"français 3252" OR
   "fr. 3252" Birague Nevers chiffre` (no relevant hit); `Birago Nevers 1571 1572 cipher letters BnF 3252 deciphered` (Tomokiyo's
   HistoCrypt paper on the 1592 Henri IV-Nevers digit cipher, another letter and key; nothing on fr.3252); model-solve family
   covered by the same queries (no hit). HARVEST-D (28 Sept 2026, `../ceppo-nevers-fr3251-1570s/NOTES.md`) had already found the
   Treccani DBI life of Lodovico Birago cites fr.3252 among its manuscript sources, with no text of any letter.
2. **Standard edition.** None for the sender; the recipient's edition (Gomberville 1665, both parts) searched inside, line 2 above.
   OCR positive control from VERIFY-NEVBIR-90REST (same day, `../nevers-birago-fr3251-1572/AUDIT.md`): "Birague" and "Lodovico"
   signatures are found by the same search, so a printed Birago letter would be expected to show.
3. **Community lists.** Tomokiyo, `sources/cryptiana/web/nevers.htm` (local mirror): its BnF list covers fr.3251 and other
   volumes; fr.3252 is not listed (HARVEST-D, 28 Sept 2026, and BIRAGO-SCOUT, 2 Oct 2026; re-grepped this session: "3252" absent).
4. **DECODE** (login-free RecordsList, 2 Oct 2026): `x_c_holder LIKE 3252` 0 records; positive control `x_c_holder LIKE 3621`
   8 records.
5. **Bourdeau** (`dbourdeau/cyphersolver`, shallow clone 2 Oct 2026, grep "3252", "birago", "btv1b9060232m"): the three letters
   appear only as rows of his BnF candidate sweep (`research/gallica_sweep/bnf_candidates.txt` lines 274-277, "## 1501-1600
   btv1b9060232m ... 3 items", nos.30/67/77, notice text only); no target folder, no reading, no status. His README's Birago rows
   are fr.3315 (Renato Birago 1574) and fr.3251 f.119.
6. **Aymeloglu** (`aaymeloglu/unsolved-ciphers`, shallow clone 2 Oct 2026, grep "3252", "birago", "birague"): no hit.

Verdict: **open** for all three letters. Not found-solved.

## Web and blog check (NEVBIR-3252, 2 Oct 2026)

(a) Plain web searches: the four queries in Check-solved item 1. (b) Blog site search:
`Birago Nevers chiffre site:cryptiana.blogspot.com OR site:ciphermysteries.com OR site:scienceblogs.de` -- hits were unrelated
Cipher Mysteries pages (Voynich, Cryptologia tags) and a 2016 Klausis Krypto Kolumne month index; none names Birago, Nevers or
fr.3252. The Cryptiana blog's own Birago posts (July and August 2024) are on fr.3251 f.119, not these letters (HARVEST-A,
28 Sept 2026, `../nevers-birago-fr3251-1572/NOTES.md`). (c) No plausible hit had a comment thread to read. Result: no reading
or decipherment of fr.3252 nos.30, 67 or 77 located on the open web or the three blogs.

## Premise check (NEVBIR-3252, 2 Oct 2026)

**(a) the folders' own files.** This folder is new. The sibling folders mention fr.3252 only for the f.36-37 witness (5 Apr
1571, interlinear clerk's decipherment, HARVEST-D) and in BIRAGO-POOL.tsv, whose rows for f.47r/f.100r/f.117r read
"decipherment_attached: no (none seen)". Not found.

**(b) other solvers' working files.** Bourdeau: candidate-list rows only (Check-solved item 5), no apply-key output, no
rendering. Aymeloglu: nothing. Not found.

**(c) physical neighbours, at native resolution where anything was written.** Canvases 47-49, 100-102, 117-119 viewed (1600 px
overviews); every opening was inspected for an interlinear gloss over the cipher, a slip, or a decipherment on the facing page.
- f.47r (canvas 48): no interlinear letters over the cipher lines at overview size; facing page (f.46v, canvas 48 left) is the
  dorse of the preceding item with show-through and a docket "26 April 1571"; canvas 47 is a French letter (unrelated);
  canvas 49 is the clear continuation (f.47v) and the end of the letter with signature (f.48r). No slip.
- f.100r (canvas 101): facing page (f.99v) carries only show-through (a mirrored French letter, checked on a native crop,
  `images/c101_leftblock.jpg`) and a docket, read on a native crop (`images/c101_endorse.jpg`, rotated): "Copie des lettres
  escriptes ... par le S.r Ludovic de Birague ... Janvier 1572" -- a docket for the copies the letter encloses ("la coppia
  della lettera di Sua Maestà"), not a decipherment. Canvas 100 is a French letter of 1572 (f.98v-99r, unrelated text);
  canvas 102 is the clear continuation and signature (f.100v-101r). No slip.
- f.117r (canvas 118): facing page (f.116v) is the address/docket leaf of the preceding item; canvas 117 shows f.116r blank but
  for show-through; canvas 119 shows f.117v (show-through only) and f.118r (faint show-through and a small docket). No slip,
  no clear copy.
Not found, for all three. Caveat: interlinear glosses on the fr.3252 f.36 witness were invisible at 1x and legible only at 2x
(HARVEST-D); the f.47r line crops (native) below were checked for them before transcription.

**(d) recipient's side.** Gomberville's *Mémoires* of the recipient, both parts, searched inside (line 2). Court
correspondence: *Lettres de Catherine de Médicis* vol. 4 (1570-74) was grepped for Birague by VERIFY-NEVBIR-90REST
(2 Oct 2026): five hits are René de Birague, one names Ludovic in command at Saluces after 24 Aug 1572 -- no letter or summary
of these three. Not found.

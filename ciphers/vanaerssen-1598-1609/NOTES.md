blocked
RGP GS 80 (Haak 1934) and GS 108/121 full-text searched by this worker on Huygens retroboeken/oldenbarnevelt (searchText "cijferschrift": 6 hits, GS 80 pp.397, 400, 474, 497, 538, GS 108 p.XIII; "Aerssen cijfer": 6 hits, GS 80 pp.397, 398, 497, GS 121 pp.182, 192, 450), 8 Oct 2026; the two residue letters (inv. 2019 scans 77 and 87, 3 Jul and 5 Aug 1601) were not opened by this worker, and their absence from Haak rests on Bourdeau's complete RGP 80 list, not on this worker's own date check -- hence blocked.

# François van Aerssen to Johan van Oldenbarnevelt, Paris 1598-1609 (NA 3.01.14 inv. 2016-2025) -- pool inventory

Opened by AERS-POOL (LANE FAMILY, account 2), 8 Oct 2026, 19:20-19:4x UTC by `date -u`, from oldenbarnevelt-brederode-1605
NOTES.md "The 10 Aug 1598 sleutel ... (R10-OBRED98)". Job: inventory the pool and check-solved it; no transcription, no decoding.

## Prior work (prior-work step, 8 Oct 2026)

`python3 tools/prior_work.py vanaerssen-1598-1609 --item-spec 'shelfmark=NA 3.01.14 inv. 2016;date=1598-08-10;sender=Francois van
Aerssen;recipient=Johan van Oldenbarnevelt' --step-type lookup --fetch` -> exit 4: LEAD 1-own = this worker's own ROOM claim (19:20,
covers this item; not someone else's work); UNCHECKED 3-tomokiyo, 3-solver x2, 4-editions. Answered by hand:
- 1 own work: grep "Aerssen" over ciphers/*/NOTES.md -> oldenbarnevelt-brederode-1605 (R9-NAKEY, R10-OBRED98: inv. 2016 METS, scans 7,
  16, 30-32 on disk, design read) and na-oldenbarnevelt-2442-1605 l.1313 (catalogue mention only). No reading of any Aerssen letter by us.
- 3 solvers: **dbourdeau/cyphersolver `targets/aerssen1601/`** (clone of 7 Oct 2026, HEAD 1fb3c46f): "François van Aerssen ->
  Johan van Oldenbarnevelt, Paris, Nationaal Archief 3.01.14 inv. 2019 scans 57 and 66 | 25 May; 2 Jun 1601 | 4 Oct 2026 | partial |
  Key rebuilt from the 11 and 28 May interlinear glosses and 30 April list A (scan 46); decipherment by Feyseel Nur (with Claude and
  Codex). No contemporary decipherment of the target passages; unprinted in the editions searched." (README row, verbatim, abridged
  after "searched"). Its `evidence/inventory_2016_2019.tsv` inventories the cipher-bearing scans of inv. 2016 and 2019 (rows copied
  with credit into pool.tsv) and its `evidence/prior_art.txt` lists all 41 Aerssen->Oldenbarnevelt letters printed in RGP 80 with their
  cipher notes. This is the main finding: **the pool's cipher-bearing part (inv. 2016 + 2019) is Bourdeau's working area, with his
  own stated open gaps (codes 47', 45', 20^, 88'; holdout validation; Legatie-archief 611/612 key sheet).** Duplicate-effort risk.
  aaymeloglu/unsolved-ciphers (clone 8 Oct 2026): grep aerssen/aersen/Oldenbarnevelt -> 0 hits.
- 3 Tomokiyo/blogs: grep sources/cryptiana, sources/ciphermysteries, sources/schmeh -> 0 hits; web (below) 0.
- 3 DECODE: cached listings sources/decode/records-decrypted/non-decrypted-2026-09-24.tsv, keys-all-2026-09-28-merged.tsv: no
  Aerssen/Oldenbarnevelt/3.01.14 row, no Nationaal Archief record dated 159x-160x. Cache is two weeks old (not re-crawled).
- 4 editions: RGP GS 80/108/121 searched by this worker (line 2). Positive control: GS 80 p.397 (no. 222, 29 May 1598, "origineel
  gedeeltelijk in cijferschrift. In de copie is het cijfer opgelost. De sleutel is in hetzelfde dossier aanwezig") found, matching
  Bourdeau's citation. GS 108 p.XIII: cipher in that volume "maar in één stuk" (no. 92 = oldenbarnevelt-brederode-1605); Veenendaal
  omitted the Aerssen letters of 1602-1613 (Bourdeau, vol.2 Inleiding pp.VII-VIII; not re-read here). Van Deventer, Vreede,
  Nouaillac: not opened by this worker (Bourdeau's prior_art.txt reports them; Nouaillac's 11 May 1601 cipher letter is to Valcke).

## Pool inventory (this worker, 8 Oct 2026) -- `pool.tsv`

Item pages of inv. 2017-2025 read once each (scan lists in `na_301_14_2017_2025_scans.tsv`; inv. 2016's list is in
`../oldenbarnevelt-brederode-1605/na_301_14_2016_scans.tsv`). Scan counts: 2017 14, 2018 3, 2019 177, 2020 230, 2021 3, 2022 83,
2023 3, 2024 268, 2025 35. Catalogue dates with "*" are the letters printed in RGP 80 (they match Haak's numbers: 29 May, 15 Aug,
19 Dec, 31 Dec 1599; 31 Dec 1600; 1601 list).
Contact sheets at 400 px by this worker's own eye: 107 scans (2017/2018/2021/2023/2025 every 3rd, 2020/2022 every 6th, 2024 every 8th);
then 21 scans at 1000-1400 px (all of 2017; 2018/1; 2020/1, 85; 2021/1; 2022/1; 2024/17). inv. 2019 not re-sampled (Bourdeau's
inventory covers it); inv. 2016 from R10-OBRED98.

Result (H for what was seen, design only, nothing transcribed):
- **Syllabary cipher with runs is confined to 1598 (inv. 2016) and Jan-Jul 1601 (inv. 2019)**, matching Bourdeau's note that
  "syllabic runs stop after Jun/Jul 1601" (new chiffre sent 23 Jun 1601, Haak no. 318).
- **1599 (inv. 2017): isolated name codes only**: 29 May 1599 "21" with a cross, twice (printed, Haak no. 265, p.538 "Deze namen in
  cijferschrift"); 19 Aug 1599 "25" with a cross, about three times, unglossed (not in Haak's list; 25 = Villeroy per Haak p.604).
  15 Aug, 19 Dec and 31 Dec 1599 pages show names in clear.
- **1600, 1602, 1605-1609 (inv. 2018, 2020-2025): no cipher seen** on any sampled page; on the 1400 px scans names are written out
  (Buzanval, Villeroy, Sully on 4 Jan 1602). Isolated name codes would not show at 400 px, so "none seen" for the thumbnail-only
  scans is a sampling result, not a negative.
- Nearly every cipher-bearing 1598/1601 letter carries a period decipherment (interlinear, a per-letter gloss sheet, or list A/B):
  as targets they are KNOWN (N0); as material they are key sources.

## Best two unglossed or partly glossed letters (step 4)

1. inv. 2019 scan 77, 3 Jul 1601, ~20 signs, "interlinear (partial?)" in Bourdeau's inventory; after the new chiffre of 23 Jun 1601,
   so the 11/28 May 1601 glosses (key in hand: Bourdeau's key.tsv, CC BY text / MIT code) may not apply. Not printed in RGP 80.
2. inv. 2019 scan 87, 5 Aug 1601, ~20 signs, gloss status "?". Not printed in RGP 80.
(Third, name codes only: inv. 2017 scan 8, 19 Aug 1599, about 3 x "25+", read by Haak's own value as Villeroy -- not a read worth a unit.)
Both are below any useful authentication distance alone (~20 signs), sit beside Bourdeau's active target, and depend on the
post-23-Jun-1601 key, of which no period table is known (Legatie-archief 611 IV, location unresolved). Next read if anyone takes it:
one 1400 px fetch of scans 77 and 87 (2 NA requests) and an eye check of the gloss state, ~0.3; a transcription unit would be one
Sonnet pass on line crops per scan (~1.5 each) + reconciliation (~1.5), ~4.5 for both. **Recommendation: do not promote**; the pool
is Bourdeau's working area and its residue is ~40 signs. A better use is to send Bourdeau the inv. 2017 finding (1599 = name codes
only) and the 2018/2020-2025 "no cipher seen" sample, which his inventory does not cover -- an outreach item, owner's call.

## Web and blog check (AERS-POOL, 8 Oct 2026)
- web: "François van Aerssen Oldenbarnevelt cipher letters 1601 decipherment" -> Wikipedia (Aarssens), unrelated HistoCrypt papers; nothing.
- web: "\"Aerssen\" chiffre lettres Oldenbarnevelt \"3.01.14\" cijfer" -> DBNL biographies, NA 3.22.28 finding aid; nothing on a cipher.
- web: "\"van Aerssen\" Buzanval chiffre 1598 Henri IV ambassade Paris déchiffrement" -> Nouaillac 1908 (Honoré Champion page), ARCSI
  Henri IV/Hesse 1609 table; nothing on this correspondence.
- web: "aerssen1601 cyphersolver Aerssen Oldenbarnevelt 25 May 1601 Claude" (model-solve check) -> nothing indexed (Bourdeau's page
  dbourdeau.github.io/cyphersolver/aerssen1601.html exists per his README but is not in the search index).
- blogs: "Aerssen cipher site:scienceblogs.de OR site:cryptiana.blogspot.com OR site:ciphermysteries.com" -> 0 relevant hits.
No comment thread to open.

## Premise check (AERS-POOL, 8 Oct 2026)
(a) folder's own mentions: the source folder's NOTES records interlinear decipherments and gloss sheets in inv. 2016 -- found (they make
those letters KNOWN). (b) other solvers' working files: found -- Bourdeau aerssen1601 (above). (c) neighbours: the per-letter gloss
sheets and list A/B sit inside the same packs -- found. (d) recipient side: Haak RGP 80 prints the 1598-1601 letters with cipher
decoded in spaced type (Bourdeau's list, positive control re-found here) -- found.

## While waiting
The one action that depends on nobody: fetch inv. 2019 scans 77 and 87 at 1400 px (2 NA requests, "NA take") and record their gloss
state in pool.tsv, ~0.3 -- that alone settles whether any unglossed residue exists outside Bourdeau's two letters.

Requests: www.nationaalarchief.nl 9 (item pages), service.archief.nl 128 (107 thumbnails at 400 px, 21 scans at 1000-1400 px), all
>= 1.9 s apart, descriptive UA, no 403/429/challenge; resources.huygens.knaw.nl 3 (>= 2.2 s); github.com 2 shallow clones; web search 5.
No subagents.

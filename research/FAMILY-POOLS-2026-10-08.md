# Family pools and design priors, 8 Oct 2026 (FAM-POOL, LANE FAMILY account 2)

Job FAM-POOL, 16:22-16:4x UTC 8 Oct 2026 by `date -u`. Disk only: 0 network requests. Supplies (c) and (d) of
`.claude/briefs/lane-family.md` for the lane's next waves. No reading, no key or transcription file changed.
Scope: Dutch, German, Iberian, British/Irish, DECODE/Scandinavian, BnF with images on disk; Huntington ledgers and
Gallica excluded.

## What was already done (prior-work check 1 on the job itself)

`KEYHUNT-2026-10-07.tsv` (LANES KH-1/KH-2, 7 Oct 2026) already ran "unread siblings per key" for every KEY-OFFICES.tsv
row. For the in-scope offices it found **0 unread, unglossed, unprinted siblings** for: august-van-saksen (WVO 53-175 all
in folder or glossed), willem-van-hessen key_1069/key_174 (1068/1130/5922 glossed), gunther-van-schwarzburg (Japikse),
jan-van-nassau key_5549, lodewijk key.tsv (WVO 1810 Lumbres: 13 codes, other key), orange key_nepveu (11008 decoded
7 Oct), vanbeuningen-dewitt (printed clear or other key), oxenstierna (AOSB prints every decipherment), thurloe (every
further passage glossed: Montagu 6, Fauconberg 2, Downing 43+), huntington-blathwayt (all in folder), rah-canada (0 at
catalogue level), fr20140-danzay (key sources), antt-linhares (key units undigitised; copy orders CO-11/CO-12), the
Puebla keys (printed in CSP Spain I), Alonso Sanchez (glossed or an outside solver's live pool), espagnol142-mercy (0
reachable). This job does not repeat those rows; it adds the pools KEYHUNT did not cover (frame volumes, DECODE
letter records, NA scan runs) and the design priors.

## Table (in-scope pools with unread material)

Prior-work check 1 = grep of the id in ciphers/*/NOTES.md, ROOM.md last 1,500 lines, WORK-QUEUE.tsv, NEXT-STEPS.tsv,
KEYHUNT-2026-10-07.tsv, 8 Oct 2026 16:3x UTC. Checks 2-4 (leaf neighbours, holder note, edition) were not run by this
job (no reading): **unchecked**, owed by the job that takes the row.

| # | pool / office | key in hand | unread letters (id) | signs (est.) | images / route | check 1 (our own work) | intake gate |
|---|---|---|---|---|---|---|---|
| 1 | Manteuffel, Saxon envoy reports 1712-13 (SHStA Dresden 10026 Loc. 694/08-09) | yes: Krauske table Loc. 694/10 (key.tsv codes 1-401), period | 694/08 frames 0485, 0391, 0390, 0395, 0375, 0214, 0436, 0241, 0435; 694/09 0070 (ranks 3-13 of `mant0609/rank_unglossed.tsv`, Krauske coverage 0.92-1.00); 546 of 894 frames never seen | ~150 code tokens eye-sampled in those 10; volume total unknown (about 5-9% of frames carry code) | www.archiv.sachsen.de frame URLs in `images/loc694-08-09/frames.tsv`, HTTP 200 (MANT-0609, 8 Oct) | CLEAR for these frames (0 hits; only 0390 in a MANT-0609 inventory line). 694/09 0015/0016/0052 = **live FAM-MANT15 claim**, excluded | `partial (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0) |
| 2 | Orange circle 1572, Willem van den Bergh -> Willem van Oranje | no (KEYHUNT: design mismatch with the Nassau keys) | WVO 11106, 19 Sep 1572, KHAG A 11/XIV A/10-12, "Geheel in geheimschrift, zonder sleutel" | one page, ~23 lines, roughly 600-900 signs | WVO 11106.pdf (3 images), resources.huygens.knaw.nl | CLEAR (no folder; KEYHUNT row "not decoded; next: transcription + monoalphabetic test after check-solved") | no folder: check-solved owed |
| 3 | Palatine envoy Rusdorff -> Axel Oxenstierna 1628 (Riksarkivet) | no; candidate key source on the same host: DECODE Chifferklaver keys R4104 (II:2, 1620s), R4120 (II:18, 1626), images not on disk | DECODE R4333, R4334, R4335, R4336, R4337 ("Riksarkivet_Rusdorff_Oxenstierna_1628-1..5", Non-decrypted, 4+3+3+2+3 = 15 pages, numeric code, signature groups 760 761 3230 853 953) | 15 pages, plausibly 2,000+ | DECODE listing login-free; full-size images need the one-login browser route (`tools/decode_browser_login.js`, `--guess-fullsize`; worked on R4692, 2 Oct) | CLEAR (0 hits outside riksarkivet-r4282-1628 NOTES.md:1385, which names them as a side lead only) | no folder: check-solved owed |
| 4 | Sociëteit van Suriname secret correspondence 1781 (NA 1.05.03 inv. 373) | yes: period "Oud/Nieuw Secreet Alphabet" (inv. 86), key_period*.tsv | inv. 373 scans not yet looked at next to the glossed hits: 0697-0701, 0703-0729, 0731-0745, 0747-0757 (offsets not sampled); 1,030 scans in all | glossed letters found so far ~6 scans; unglossed unknown | service.archief.nl IIIF, 114 requests clean on 6 Oct | CLEAR for the neighbour ranges (0 hits); 0702/0730/0746/0758 done (R13/R14/R15, D4-SUR) | `partial (line 1) ...` (exit 0) |
| 5 | Swedish chancery 1628, R4282 (folder riksarkivet-r4282-1628) | no; same R4104/R4120 lead as row 3 | R4282 whole letter, 0 of 1,094 signs read | 1,094 | on disk | in folder; the R4104/R4120 view is its own named suggestion (NOTES.md:1383), not run (0 ROOM hits) | `open (line 1) ...` (exit 0) |
| 6 | Hellen (Prussian resident, The Hague) 1763 | no: R4386/R4388 retired by pre-registered tests (D2-HELR, N7-HELBC) | DECODE R1045-R1048, R1060, R1061 | 1,234 (pooled_1763.txt) | on disk | in folder, blocker no-key-material | `partial (line 1) ...` (exit 0) |
| 7 | Linhares household, ANTT CLNH maço 86 | yes (dictionary cipher, key.tsv) | items /02 (126 images), /09 (212) unopened; /01, /04 thumbs done by KH1-E 7 Oct (0 cipher) | 0 known; 19 of 21 items eye-checked, no cipher | DigitArq, `tools/digitarq_fetch.py` | KH1-E (7 Oct) covered /01+/04; /02, /09 CLEAR | `blocked (line 3) -- already terminal` |
| 8 | Blathwayt Madrid run 1725-29 (Huntington mssBLA) | yes (key.tsv) | BLA 187 / 191(a) residue (18 groups context-filled R9-HUNT; no TNA copy R10-HUNTTNA) | ~12 lines | on disk | in folder; regrade only | `partial (line 3) ...` (exit 0) |

## Design priors (`tools/design_prior.py --no-write`, run 8 Oct 2026 16:3x UTC)

| letter | N | K | above-null families | advisory ranking | nearest keys |
|---|---|---|---|---|---|
| hellen 1763 pooled (R1045-48, R1060-61) | 1234 | 634 | **none** (multi-sign d 4.30 vs null p05 3.61; every family "not above null"); shuffled FP 0.045 | nomenclator 4.49, homophonic 4.98 | es132 key d 3.36, nepveu 3.51 -- all far: unlike every key on file |
| riksarkivet R4282 (sign-per-character stream from r4282_transcription_bourdeau.txt, bracketed plain dropped; `research/family-pools-2026-10-08/r4282_signs.txt`) | 1094 | 34 | multi-sign, letter-for-letter, mixed, code all "plausible" (multi-sign d 0.09 vs p05 0.18); shuffled FP 0.050 | homophonic 0.09, nomenclator 0.20, alphabet substitution 0.23 | Mayenne 1592 homophonic family (synthetic) d 0.08 |
| na-oldenbarnevelt-2442-1605 (already read; run for reference only) | 1177 | 293 | all plausible | nomenclator 1.86 | nepveu d 0.99 |
| Rusdorff R4333-37, WVO 11106 | -- | -- | **not runnable: no ciphertext on disk** (run after the first transcription) | | |

Reading: the 1763 Hellen stream sits outside every reference (K/N 0.51 on a 1-3900 range: a large code book, not a
letter table), so no attack family on file is indicated and the pool stays no-key-material. R4282 (34 signs, letter
shapes) is consistent with a small homophonic or simple letter table, which is what a 1620s Chifferklaver key image
would have to show (the folder's own "3-row 8-block letter table" expectation).

## Ranking (expected value = P(first cheap test moves it) x value / cost)

1. **Manteuffel 694/08 ranked frames (row 1).** Key in hand at 0.92-1.00 coverage, route proven, cheapest per token.
   P high (0.5) that the period key reads letter-range codes; value moderate (unglossed 1712 envoy reports, D2 possible).
2. **WVO 11106, van den Bergh 1572 (row 2).** A whole-letter cipher with the image on a reliable host and no folder;
   P(moves) about 0.3 (single letter, design unknown; a monoalphabetic letter of ~700 signs is in solver range), value
   high (Revolt year, Orange's brother-in-law), cost low.
3. **Rusdorff -> Oxenstierna 1628, DECODE R4333-R4337 (row 3).** The only 2,000+-sign pool in scope without a folder;
   one DECODE login also serves row 5's key-image view. P about 0.2, value high (pool, period key plausibly in the same
   archive's key boxes), cost moderate.
4. Suriname inv. 373 neighbour sweep (row 4): cheap, mostly key-extension (held-out tokens the folder's class tests ask
   for); P 0.4 of finding more cipher, low chance it is unglossed.
5. R4282 key-image view R4104/R4120 (row 5): ~$1.5, pair with row 3's login.
6. Hellen 1763 (row 6): parked; design prior gives no family; reopens only with new key material.
Not ranked: rows 7-8 (low P or internal regrade); BnF-on-disk tie-break did not arise (no in-scope BnF pool row).

## Top 6, next step each

1. **sachsstaatsarchiv-manteuffel-1712, 694/08 0485/0391/0390/0395 (+0375, 09/0070).** After FAM-MANT15 reports: only
   if its 0015+0016 decode beat its shuffled-key control, crop each frame's code lines with `tools/iiif_lines.py --image`,
   two blind passes per frame + one reconciliation (4 frames x 3 calls x ~1.5 = ~$18 at the vision rate; a 2-frame
   first batch ~$9), `tools/decode_key.py --check`, judge fr18 with shuffled-key control. If FAM-MANT15's control failed,
   this row waits. Cost band M. Check-solved: not owed (gate exit 0); prior-work checks 2-4 owed per frame.
2. **WVO 11106 (new folder wvo-11106-bergh-1572).** Check-solved first (owed: Groen van Prinsterer Archives I/III-IV
   for 1572, Japikse, WVO print codes and Inhoud, van den Bergh's printed letters, DECODE, the two solver repos), ~$2;
   then the premise check (the 3 WVO images for a gloss; the facing and following letters), crop + two passes +
   reconciliation (~$4.5), `design_prior.py` on the result, then `family_run.py --family masc` with its matched control.
   Cost band S-M.
3. **DECODE R4333-R4337 Rusdorff (new folder decode-4333-rusdorff-oxenstierna-1628).** Check-solved first (owed:
   Rusdorff's printed *Consilia et negotia politica* (1725) and *Mémoires et négociations secrètes* (ed. Cuhn, 1789),
   AOSB ser. II for Rusdorff, Riksarkivet catalogue note, DECODE record pages, solver repos), ~$2. Then one browser login:
   fetch the five records' full-size images (`--guess-fullsize`) and the R4104/R4120 key images in the same session,
   ~$2; transcribe one page as a sample and run `design_prior.py` before any attack. Cost band M.
4. **na-suriname-map-1781 inv. 373 neighbours.** 600 px contact-sheet sweep of 0697-0701, 0703-0729, 0731-0745,
   0747-0757 (about 55 scans, `passes/inv373_sweep_r13/` scripts unchanged), stop rule: list every cipher scan, glossed
   or not; ~$1.5. A glossed find feeds the folder's held-out [ij]/[sh-lig] class tests; an unglossed find is a target
   under the period key with the map key as control. Cost band S. Check-solved not owed (gate exit 0).
5. **riksarkivet-r4282-1628, view R4104 and R4120.** The folder's own named suggestion (NOTES.md:1383): look for a
   3-row 8-block letter table with 2-digit values 12-91; best done in row 3's login session; ~$1.5 alone. If one fits,
   a key test against R4282 with the folder's permutation control. Cost band S. Gate exit 0.
6. **hellen-frederick-1752 1763 cluster.** No step: design prior indicates no family on file, both positional key
   candidates retired. Keep parked (no-key-material) until a post-1756 key record or a clear copy turns up; nothing
   to brief this wave.

Requests: none (disk only). Vision calls: 0. Subagents: 0.

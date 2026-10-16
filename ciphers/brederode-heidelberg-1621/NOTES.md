open
- **Status:** open (HEID-1623A, 16 Oct 2026: the 12 Aug 1623 block (inv. 6022 scans 166 + duplicate 171) transcribed, witness control 61/64 = 0.953 PASS, 49 of 64 tokens S-as-transcribed; the marginal note on 171 read as running Dutch that carries the block's clear words in order (all M) -- a clear rendering of the passage, identification with Joachimi's solution of res. 1721a M; its code-level alignment is untestable by tools/interlinear_align.py at this N (target 1 vs shuffle p95 1; a known-true positive control also reads 1), so no draft key; next: scan 181 block + its note, then the alignment on the pooled pairs) -- the recipient-side standard edition, *Resolutiën der Staten-Generaal, nieuwe reeks 1610-1670*, deel 5
  (1621-1622, ed. J. Roelevink, RGP, 1983), read through the Huygens retroboeken full-text search (term "Brederode", source 5,
  109 hits, 15 Oct 2026, HEID-1621D) and the printed pages p. 251, 252, 260, 261 (OCR html): p. 260, resolution 1644b, 23 Aug 1621,
  calendars "Brederode, dd. Heidelberg 13 aug." with no summary of its content, and note 1644c reads "S.G 6021 (orig.). Gedeeltelijk
  in code." -- the editor saw the cipher passage and printed no decipherment. The letter of 6 Aug (p. 251, res. 1585a) is "Niet
  aangetroffen". Full-text search of the volume for "ontcijfer": 0 hits; "in code": 6 hits, none a decipherment of this letter.
- **Sender:** P. van Brederode, agent of the States General at Heidelberg (signature "P van Brederode" read on scan 375, HEID-1621B)
- **Recipient:** the States General, The Hague. **Date:** Heidelberg, 13 Aug 1621 (endorsement on scan 380 read "L. 20 Aug. 1621" by HEID-1621B; the edition records the
  letter among those received on 23 Aug 1621, res. 1644b -- the two dates disagree, not settled here)
- **Holder:** Nationaal Archief, 1.01.02 Staten-Generaal, inv. 6021 (liasse Agent Brederode, 1621-1622). Two witnesses of one
  numeral block: scan 375 (signed letter) and scan 379 (the duplicate; 380 "Duplicaet vanden 13 Augusti 1621").
- **Split from:** ciphers/oldenbarnevelt-brederode-1605 (sections "## HEID-1621" and "## HEID-1621B"; working files stay in its
  heid1621/ folder). Files here: `ciphertext.tsv` (scan 379 block as transcribed, every token grade M, copied unchanged from
  `../oldenbarnevelt-brederode-1605/heid1621/ciphertext_6021_379.tsv`); `images/manifest.json` (pointers and sha1s, no image).

## What is established (from HEID-1621, HEID-1621B; grades as there)
- Scan 379 block: 96 numerals, 44 trailing letters, 3 non-numeral signs, inside clear Dutch prose ("Desen dus wijt geschreven
  hebbende, bekomme ick advijs [groups] in date des 29 July ouden stijl dat ..."), all M.
- Preregistered structure (PREREG-HEID1621.md): numeral pairs are (n, n+1) in 40 of 41 (0.976; order-shuffle control p99 0.053);
  21 distinct pairs, values 10-84; one letter per unit; about one unit per Dutch word (S4). Design-class lead (M): a word-level code
  of about 45 units, pair + letter tag. Nothing decoded; no key; no reading.

## Check-solved by sender (HEID-1621C, 15 Oct 2026, 17:13-17:2x UTC by date -u)
The anonymous-pile path ended when HEID-1621B read the signature; this is the normal gate (CLAUDE.md pipeline step 2).
1. **Recipient-side edition (the standard edition for a letter to the States General):** Resolutiën der Staten-Generaal, nieuwe reeks,
   deel 5 (1621-1622), Roelevink 1983. Route 1, Huygens retroboeken `statengeneraal` (new series source ids 1-7, sources/huygens/NOTES.md):
   **HTTP 503 Service Unavailable**, 2 requests, one retry after a 20 s pause, then stopped (good-citizen rule). Route 2, Google Books
   API (country=US): the volume is M-hDAQAAMAAJ, viewability NO_PAGES; one keyed query ("Brederode" "Heidelberg" 1621 agent)
   returned it with the snippet "... Brederode, dd. Heidelberg 20 dec. 1620 ...", so the volume does calendar this sender's letters.
   Further Google Books queries aimed at 8/13 Aug 1621 got "Service temporarily unavailable" (7 of 11 calls this session), not a
   negative. **The edition was not read for Aug 1621: this is why the status is blocked.**
2. **Sender's printed correspondence:** no edition of P. van Brederode's agent letters located. Internet Archive full-text search
   (be-api): "bekomme ick advijs" 0 hits; "agent Brederode" 1621 26 hits, none an edition of his letters (secondary histories:
   Arend/Vlothe *Algemeene geschiedenis des vaderlands*, citing "Resol. Stat. Gen." for his Heidelberg reports of 1618;
   geschiedkundige00leidgoog, "De berichten uit Duitschland van den agent Brederode bleven ontmoedigend"); "Pieter van Brederode"
   Heidelberg 54 hits, none relevant (a 1669 collector of the same name). advancedsearch for a Resolutien volume on IA: 0. Google
   Books hits are histories (Polisensky, *Tragic Triangle* 1991, NO_PAGES; *Early Modern European Diplomacy* 2023, PARTIAL; *Die
   Schlacht am Weissen Berg* 2026, PARTIAL; *Niderlandyzm na Slasku* 2003, NO_PAGES), not editions. Veenendaal, *Bescheiden ...
   Oldenbarnevelt* (RGP GS 80/108/121) ends before 1621 and cannot hold this letter.
3. **DECODE:** cached listings in sources/decode/ (records decrypted / non-decrypted 24 Sept 2026, keys-all 28 Sept 2026) grepped for
   Brederode, Heidelberg/Heydelberg, 6021 and Dutch 1621 rows: none. No live listing request made (the listing cannot be filtered
   by name; a full crawl exceeds the 5-request cap). Cache-based.
4. **Cryptiana:** sources/cryptiana/web grepped for Brederode: none; the two Heidelberg mentions (elizabeth.htm, haldimand.htm) are not
   this item.
5. **Solver repositories:** live shallow clones, 15 Oct 2026: aaymeloglu/unsolved-ciphers (head 8 Oct 2026) -- one "Brederodes" in
   royalist-1646/README.md (a 1646 name list), nothing for 1621, Heidelberg or NA 1.01.02 inv. 6021; dbourdeau/cyphersolver (head 14 Oct
   2026) -- no Brederode/Heydelberg row in research/ or targets/ (matches are word lists and an unrelated 1686 name dictionary).
6. **Holder notice:** NA 1.01.02 inv. 6021 as recorded by OBRED-6021 (`../oldenbarnevelt-brederode-1605/nl_brederode_lias.tsv`): the
   liasse of Agent Brederode, no mention of a cipher or decipherment. Not re-fetched (no www.nationaalarchief.nl budget in the brief).
7. **tools/prior_work.py** (`--item-spec 'shelfmark=NL-HaNA 1.01.02 inv. 6021;folio=scan 375;date=1621-08-13;sender=P. van
   Brederode;recipient=Staten-Generaal;...' --step-type read --offline --ref WORKTREE`): exit 4; LEAD = this job's own claim line;
   LOOK 2-leaf (no gloss check recorded for scan 375 at native size); UNCHECKED tomokiyo/solver-by-unit (no folio key); UNCHECKED-NET
   editions (no prior_editions.tsv row) and live aymeloglu (run by hand in item 5).

## Web and blog check (HEID-1621C, 15 Oct 2026)
Web search "Brederode agent Heidelberg 1621 cipher letter States General": nothing on this letter (Histocrypt papers, an unrelated Yale
cipher sheet, Aitzema). Blog search across Cipherbrain / klausis-krypto-kolumne (scienceblogs.de), the Cryptiana blog
(cryptiana.blogspot.com) and Cipher Mysteries (ciphermysteries.com) for Brederode / Heidelberg 1621 / cijferschrift: no post on this item
(nearest: Klausis "unsolved cryptograms from the thirty years war" 1-2, Vienna material, not this). Comment threads not read one by one.

## Premise check (HEID-1621C, 15 Oct 2026)
- (a) Folder's own mentions of a decipherment, gloss or clear copy: none in HEID-1621/HEID-1621B; the 375 and 379 blocks carry no
  interlinear decode (379 checked at native size; 375 at 1200 px only). Not found.
- (b) Other solvers' working files: neither solver repository has this item (item 5). Not found.
- (c) Physical neighbours: 361-397 screened at 700 px (HEID-1621B, controls 15/15); 374-380 read at 1200 px; no key leaf, clear copy or
  decipherment beside either block. Not found (limit: scan 375's facing page not seen at native size).
- (d) Recipient's side: the Resolutiën SG 1621 volume is exactly this check; unreachable on HEID-1621C's pass, read by HEID-1621D
  (15 Oct 2026, section below): p. 260 res. 1644b calendars the 13 Aug letter, note c "Gedeeltelijk in code", no content, no
  decipherment. Not found.
- **Premise check verdict (HEID-1621D): open.** No decipherment, clear copy or content summary of the cipher passage located in the
  folder, the solver repositories, the neighbouring scans or the recipient-side edition.

## Remaining gaps (HEID-1621D, 15 Oct 2026)
Read so far: 0 of 45 units (nothing decoded; spec test 1 run, undecided; transcription all M)
  (edition step closed: Resolutiën SG NR 5 read by HEID-1621D, p. 251-252, 260-261; res. 1644b "Gedeeltelijk in code", no decipherment printed)
- transcription control (scan 375 second witness vs ciphertext.tsv) - blocker: not-attempted; brief JOB HEID-1621D step 3 priced above its cap; next: iiif_lines crops + two blind Sonnet readers + one reconciliation, ~$5
- the 45 units themselves - blocker: too-short; test 1 C2 rank-match control 0.010 vs gate 0.50 at N=45 (HYPOTHESES.md), no solver family reads this length; next: pool more units from siblings (Escalation, siblings), ~$1.5 per inventory screen

## Escalation (HEID-1621D, 15 Oct 2026)
- [ ] siblings: the 6 Aug 1621 letter (res. 1585a "Niet aangetroffen"), the 8 Aug letter named on scan 376, and Brederode's other 1621-1622 letters in inv. 6021 and 6025 (Lias Duitsland, edition p. XVII) screened stride-1 for numeral blocks in the same code, ~$1.5 per inventory
- [ ] clear-pages: the clear prose around the block (same letter) and the edition's summaries of the neighbouring letters (6, 20, 27 Aug) as context for a crib, only once a pool exists
- [ ] known-keys: KEY-OFFICES.tsv / KEY-DESIGN.tsv not yet searched by tool for a States General agent code of 1618-1622 (pair+letter); next: tools/design_prior.py, ~$0.3
- [x] print: Resolutiën SG NR 5 read (HEID-1621D), no decipherment; no edition of Brederode's agent letters located (HEID-1621C)
- [n/a] key-rebuild: no decipherment, gloss or key sheet located to rebuild from
- [ ] image-check: scan 375 at native size (the second witness and its facing page) not yet seen
- [x] retry: the Huygens host retried and answered (HEID-1621D, 11 requests, all 200)
Verdict: keep going: 1 internal gaps; cheapest next: known-keys design_prior check, ~$0.3, then the scan 375 witness, ~$5

## While waiting
The one action that depends on nobody: transcribe the second witness (scan 375's numeral block at native size, one reader, reconcile
against ciphertext.tsv) -- it tests the M transcription and needs no edition.

## HEID-1621C (15 Oct 2026, 17:13-17:2x UTC by date -u, account 2, Opus; for the orchestrator, owner account)
Brief: `.claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md`, JOB HEID-1621C. Requests: resources.huygens.knaw.nl 2 (both 503);
archive.org 6 (2 advancedsearch, 4 be-api fts); Google Books API 11 (4 answered, 7 "Service temporarily unavailable"); de-crypt.org 0;
github.com 2 clones; web search 2. No image fetched, no decode, no key, no reading.
Intake gate, `python3 tools/intake_gate_check.py brederode-heidelberg-1621` (17:19 UTC):

    brederode-heidelberg-1621: blocked (line 1) -- already terminal, nothing to gate
    exit=0

 Because the verdict is `blocked` (an edition named and not opened), the gate's exit 0 is the terminal-word
pass ("nothing to gate"), not a cleared edition step, so the spec (brief step 3) was **not written**. Spec notes for whoever writes it:
the nl corpus closest in era is `tools/data/nl16` (Marnix, Coornhert, Spieghel, 16th century); nl18 is later; neither is 1621
diplomatic Dutch, so a judge result on it needs the era caveat (rule 3, V6-PTCORP).
**Verdict: blocked** (edition unread: host outage). Next breadth row for the parent (cap 3, after the Huygens retry clears the gate):
spec + first cheap test -- unit inventory (21 pair+letter units, 45 tokens) against a Dutch word-frequency list under a frozen pool,
matched control a synthetic 21-unit word code of the same length from nl16.

## HEID-1621D (15 Oct 2026, 18:13-18:2x UTC by date -u, account 2, Opus; for the orchestrator, owner account)
Brief: `.claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md`, JOB HEID-1621D. Requests: resources.huygens.knaw.nl 11 (all 200: 4
searches "Brederode" source 5 at batch 0/20/40/60, 1 pages.json, 4 OCR pages, 2 searches "in code" and "ontcijfer"); service.archief.nl 0.
No image fetched, no reader, no decode, no key, no reading.

**(1) Edition read.** Resolutiën der Staten-Generaal, nieuwe reeks, deel 5 (1621-1622, Roelevink 1983), Huygens retroboeken full-text
search: "Brederode" 109 hits in the volume; the August 1621 entries opened at the printed pages (OCR html):
- p. 251, 16 Aug 1621, res. 1585a: "Brederode, dd. Heidelberg 6 aug., met berichten uit Duitsland"; note 1585a "Niet aangetroffen".
- p. 260, 23 Aug 1621, res. 1644b: "Brederode, dd. Heidelberg 13 aug."; note c: "S.G 6021 (orig.). Gedeeltelijk in code." No summary
  of content, no decipherment. (Same resolution, item a: Haga's letter from Constantinople "met een cijfercode", a different item.)
- "ontcijfer" in the volume: 0 hits; "in code": 6 hits (pp. 11, 27, 82, 260, 295, 469), none a decipherment of this letter.
- Not settled: the scan 380 endorsement as read by HEID-1621B ("L. 20 Aug. 1621") vs the edition's receipt among the letters of
  23 Aug; the brief's "8 Aug" letter vs the edition's 6 Aug (the duplicate on scan 376 names a letter of 8 Aug, HEID-1621B, M).

**(2) Premise check verdict open**; `python3 tools/intake_gate_check.py brederode-heidelberg-1621` (18:1x UTC):

    brederode-heidelberg-1621: open (line 1) -- edition/page or full-text-search citation found within 6 lines
    exit=0

Spec written: `specs/brederode-heidelberg-1621.json`. First cheap test (PREREG `t1/PREREG-HEID1621D.md` committed 2d18d5ca5 before any
measurement; `t1/inventory.py --check` regenerates `t1/result.json`), control first:
- C1 (held-out coor001boev01 windows, word vs letter at N=45, nearest pool median): 1.000 against gate 0.90 -- passes. Word and
  syllable-proxy pools coincide at this N (median 38, p05 32, p95 42 both), so inventory cannot separate those two.
- Target: N=45 units, K=25 distinct numeral tuples (30 with the trailing letter); top unit 22.23 at 0.111; 13 hapax. Percentile 0.003
  in the word pool (0.021 with letters), 0.002 in the syllable-proxy pool, 1.000 in the letter pool (median 17, p95 20).
- Outcome by the PREREG rule: **undecided** -- below the word band, above the letter band, inside neither. Descriptively the units
  repeat more than 45 words of Dutch prose and less than 45 letters.
- C2 (synthetic word code at the same N; no held-out window reached K 25+-2 in 20000 draws, the 20 nearest have K=32): rank-match to
  the frozen nl16 top-300 list recovers 0.010 of tokens (max 0.067) against gate 0.50 -- CONTROL BELOW GATE; the rank-match was **not
  run on the target**. A frequency attack on 45 units is a non-test; only more ciphertext in the same code can change that.
- Caveats: all target tokens are M; nl16 is 1569-1589 printed prose, not 1621 diplomatic letters; overlapping pairs carrying one
  letter (22.23/23.24 x etc.) may be one code entry, which would lower K further.
Rows in HYPOTHESES.md. Spec `cheap_test_done` carries the same numbers.

**(3) Not run.** The brief prices the scan 375 witness at USD 4.2 and runs it only if steps 1-2 leave at least that under a USD 4 cap,
which cannot hold; named as the next row.

**Status: open.** Next row for the parent: scan 375 second witness (tools/iiif_lines.py crops, two blind Sonnet readers on the numeral
lines, one reconciliation, per-unit agreement with ciphertext.tsv; no reading), cap ~USD 5 (4.2 priced + margin); then the sibling
screen for pool size (Remaining gaps).

## HEID-1621E (15 Oct 2026, 19:11-19:2x UTC by date -u, account 2, Opus; for the orchestrator, owner account)
Brief: `.claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md`, JOB HEID-1621E. PREREG `heid1621e/PREREG-HEID1621E.md` pushed
(11f2aebcf) before design_prior and before any fetch; sheet calls `heid1621e/sheetcalls.txt` pushed (91baf6e8f) before the sheet key was
opened. Requests: **service.archief.nl 130** (1 METS + 128 scans at 700 px + scan 58 at 1200 px), all HTTP 200, take/release lines in
ROOM.md; **www.nationaalarchief.nl 1** (the 1.01.02 EAD, `download/xml`, 22,724,926 bytes, sha256 049dfb73...dccf, scratch only);
**resources.huygens.knaw.nl 13** (8 searches in source 5, 1 pages.json, 4 OCR pages), all 200. No image committed; sha1s in
`images/manifest.json` (`heid_6021e`); `heid1621e/regen_heid1621e.sh` re-derives scans, sheets and the sheet key (cmp check: reproduces).
No decode, no key edit, no reading.

### (1) Design prior and key files on disk
`python3 tools/design_prior.py --no-write heid1621e/units_pairletter.txt heid1621e/units_numeral.txt` (45 units from ciphertext.tsv, M):

    units_pairletter.txt: 45 tokens, 30 distinct, inventory mixed; references at this N: 249
      multi-sign (homophonic/nomenclator/syllabary) d=0.07 envelope=0.2 null_p05=0.08 -> plausible
      mixed (partial table)  d=0.42 envelope=2.56 null_p05=0.33 -> not above null
      letter-for-letter      d=0.48 envelope=0.69 null_p05=0.24 -> not above null
      code                   d=0.56 envelope=2.07 null_p05=0.73 -> plausible
      shuffled-input false-positive rate: 0.110
    units_numeral.txt: 45 tokens, 25 distinct
      multi-sign d=0.08 -> not above null; letter-for-letter d=0.21 -> plausible; mixed d=0.34 -> plausible; code d=0.76 -> plausible
      shuffled-input false-positive rate: 0.120

Reading: at N=45 the prior does not discriminate (three or four classes "plausible" under each tokenisation, false-positive rate 0.11-0.12,
and the verdicts flip with the tokenisation). It licenses nothing beyond the HEID-1621 structural lead (word-level pair+letter units).
KEY-OFFICES.tsv / KEY-DESIGN.tsv: **no States General, Palatinate-mission, Heidelberg or Brederode key of 1618-1625 on file.** In-window
rows are trew-posthius-1614-18 (a Palatine physician's alphabet substitution, not an office key) and riksarkivet-r4282-1628 (Swedish,
1628); the nearest States-General row is vanbeuningen-dewitt-1657 (36 years later). The oldenbarnevelt folder's DECODE key lists
(Munich KAA 4591, Marburg 4 d) are blanket-dated Bavarian/Hessian holdings, none an SG key.

### (2) Pool screen: the rest of inv. 6021 at stride 3
Scans 4, 10, ..., 358 and 400, ..., 802 (128 scans, 4 mod 6) on 15 sheets (SHEET_SCANS=9, seed 16215, the OBRED-6019/6020/6021 disk
controls); one reader, this worker's eye. **Controls 45 of 45 placed correctly** (checked mechanically against `heid1621e/sheetkey.json`);
no sheet is a non-test. With OBRED-6021 (1 mod 6) and HEID-1621B (361-397 at stride 1), inv. 6021 is now screened at stride 3 throughout.
Per-scan calls in `heid1621e/screen.tsv`.
- **One hit: scan 58** (sheet 02 tile K; re-looked at 1200 px, M). A French text, both pages, in one hand, no address or signature on
  this opening, carrying numeral code groups inside the prose: two-digit groups in dotted runs ("14.29.42.191 50.56.22", "13.42.60",
  "22.31.34 13.42.60", "8.43.44.29.22", "49.43.34.13") and three- to four-digit standalone numbers where names would stand ("dans les 426",
  "1684", "2436 represente aux 1870", "2722", "1458", "1897", "1877", "2763", "2795", "1698"). Clear words around them name "le Conte de
  Mansfeld", "le Prince Palatin", "l'Empereur", "le Duc de Baviere", "la dispensation du mariage", "Glatz" (all M, eye at 1200 px). **The
  layout is not the Brederode pair+letter system** (no consecutive pairs, no trailing letters; two-digit groups up to about 60 plus
  three/four-digit name codes), so it does not pool with the 13 Aug 1621 block; it is a separate 1621 French cipher text in the same liasse
  (likely an enclosure or copy sent by Brederode; sender, recipient and date not read). Nothing transcribed or decoded.
- Every other scan (127): Dutch letters to the States General with P. Brederode closes and paraphs, address leaves with red seals, French,
  German, Latin and Italian copies and extracts ("Copie translaat" Feb 1622 on scan 592, "Extract ..." headings), a numbered list down a margin (scan
  52), a money column (scan 106), a few figures in a prose line (scan 208); no numeral-code block, key table, interlinear decipherment or figure postscript at sheet size.
- **The 17 Sept 1621 letter that the edition calls "Gedeeltelijk in code" (below) was not seen** on any stride-3 scan; it may sit on one
  of the two unscreened scans in each run of three, or carry a block small enough to escape a 525 px tile.
- Limits: stride 3 overall (two scans in three of 1-805 not looked at outside 361-397); 700 px tiles on sheets read at about 2,000 px, so a
  block of a dozen groups or fewer inside prose can escape; one reader.

### (3) Key and sibling candidates (no scans)
Full table in `heid1621e/key_candidates.tsv`. Searches: the NA 1.01.02 EAD (28,573 component records, parsed by script for sleutel /
cijfer / cyfer / chiff / ontcijf / decifr / dechiff / cipher / gecodeerd / in code / ziffer, 72 hits, one in 1618-1625); Resolutien SG NR 5
full text for cijfer (3), cijfers (1, index), cijfercode (5), sleutel (2, warehouse keys), gedechiffreerd (0), dechiffreren (0), code (6),
ciffer (0); pp. 82, 275, 295, 447 read (OCR html).
- **Sibling in code, same liasse:** Resolutien SG NR 5 p. 295, 28 Sept 1621, res. 1879b: "Brederode, dd. Heidelberg 17 sept.", note b
  "S.G. 6021 (orig.). Gedeeltelijk in code." A second Brederode letter partly in code in inv. 6021 (digitised) -- the pool the brief asked
  for, located by the edition but not yet by scan. (p. 275, res. 1730c: Brederode 27 Aug 1621, 6021, no code noted.)
- **SG office code, 1621:** p. 82, res. 467: the SG letter to Joachimi and Randwijck (envoys in Germany) -- "Het gedeelte betreffende de
  landgraaf van Hessen en de graaf van Mansfelt zal men in cijfercode stellen"; note b "S.G. 6055 (minuut, met code)". Inv. 6055 (Lias
  Duitsland, 1621 tweede deel): **not digitised** (no EAD dao).
- **Cipher letter with its decipherment, 1622:** p. 447, res. 2931: Mansfelt, Hagenau 13 March 1622, note a "S.G. 6056 (orig. ;
  gedeeltelijk in cijfer, met de oplossing)". Inv. 6056 (Lias Duitsland 1622): **not digitised**. Whether it shares either 6021 system is
  unknown.
- **Key leaf:** inv. 12578.1, "Sleutel geheimschrift 'Rangh van de grootte tot Constantinopelen ...'" (1618-1622), not digitised -- the only
  key leaf of 1618-1625 in the 1.01.02 EAD; Haga's Constantinople code (res. 1644a, the same day as this letter's receipt, "met een
  cijfercode"), a different post.
- **Correction:** inv. 6025 is "Liassen Agent Aitzema" (Hanse towns, 1617-1625), not Lias Duitsland as the HEID-1621D Escalation line said;
  Lias Duitsland for 1621-1622 is inv. 6054 / 6055 / 6056 (not digitised). Later Brederode liassen: 6022 (1623-1626, 595 scans), 6023
  (1627-1631, 536), 6024 (1632-1637, 470), all digitised (titles only here).
- No Resolutien entry names a decipherment ("ontcijferd", "gedechiffreerd", "oplossing") of a Brederode letter in 1621-1622.

**Status: open.** Next row for the parent: find the 17 Sept 1621 letter in inv. 6021 (it should follow the 27 Aug letter; a stride-1
700 px screen of the stretch after scan 397 up to the first Oct 1621 dateline, about 60-80 scans, ~USD 2, then its block at 1200 px and
native), which is the only route to a second block in the same code; then the scan 375 witness (~USD 5). The scan 58 French text is a
separate target candidate (its own intake: sender, date, check-solved), not pool material for this code. Inv. 6055/6056 are copy-order
candidates only if a later step needs the office code or the 1622 decipherment.

## Remaining gaps (HEID-1621E, 15 Oct 2026)
Read so far: 0 of 45 units (nothing decoded; spec test 1 undecided; transcription all M)
- the 45 units themselves - blocker: too-short; test 1 C2 rank-match control 0.010 vs gate 0.50 at N=45 (HYPOTHESES.md); design_prior non-discriminating at N=45 (fp 0.11); next: locate the 17 Sept 1621 letter "Gedeeltelijk in code" in inv. 6021 (Resolutien NR 5 p. 295) by a stride-1 screen after scan 397, ~$2
- transcription control (scan 375 second witness vs ciphertext.tsv) - blocker: not-attempted; priced above HEID-1621D's cap; next: iiif_lines crops + two blind Sonnet readers + one reconciliation, ~$5

## Escalation (HEID-1621E, 15 Oct 2026)
- [ ] siblings: the 17 Sept 1621 Brederode letter "Gedeeltelijk in code" (res. 1879b, S.G. 6021) not yet located by scan; inv. 6021 screened at stride 3 (HEID-1621E + OBRED-6021) and 361-397 at stride 1, one hit of another system (scan 58); next: stride-1 screen after scan 397, ~$2
- [ ] clear-pages: the clear prose around the block and the edition's summaries of neighbouring letters, once a pool exists
- [x] known-keys: design_prior run (non-discriminating at N=45); KEY-OFFICES/KEY-DESIGN have no SG/Palatinate key of 1618-1625; NA EAD key leaf 12578.1 is Haga's Constantinople code (not digitised); SG office code minute inv. 6055 and Mansfelt 1622 decipherment inv. 6056 located, not digitised (HEID-1621E)
- [x] print: Resolutien SG NR 5 read (HEID-1621D, HEID-1621E), no decipherment of a Brederode letter; no edition of his letters (HEID-1621C)
- [n/a] key-rebuild: no decipherment, gloss or key sheet of this system located to rebuild from
- [ ] image-check: scan 375 at native size (the second witness) not yet seen
- [x] retry: the Huygens host answered (HEID-1621D, HEID-1621E, all 200)
Verdict: keep going: 1 internal gaps; cheapest next: stride-1 screen for the 17 Sept 1621 letter, ~$2

## HEID-1621F (15 Oct 2026, 20:12-20:2x UTC by date -u, account 2, Opus; for the orchestrator, owner account)
Brief: `.claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md`, JOB HEID-1621F. PREREG `heid1621f/PREREG-HEID1621F.md` pushed (3bd5e885b)
before any fetch; sheet calls `heid1621f/sheetcalls.txt` pushed per batch (c8bda2199, 4359d18a1) before each sheet key was opened.
Requests: **service.archief.nl 57** (1 METS + scans 398-451 at 700 px + scans 423 and 424 at 1200 px), all HTTP 200, take/release lines
in ROOM.md. No other host. No image committed; sha1s in `images/manifest.json` (`heid_6021f`); `heid1621f/regen_heid1621f.sh` re-derives
scans, sheets and both sheet keys (key 1 checked to reproduce by cmp). No decode, no key, no reading.

### Screen
Stride 1 from scan 398, in order, 6 contact sheets (SHEET_SCANS=9, seeds 16216 and 16217, the OBRED-6020 disk controls). **Controls 18 of
18 placed correctly** (checked against `heid1621f/sheetkey.json`); no sheet is a non-test. Per-scan calls in `heid1621f/screen.tsv`.
- **Hit: scan 423** (batch 1 sheet 03 tile B; re-looked at 1200 px, M). A Dutch letter in the agent's clerk's hand; on the left page a
  paragraph opens "Mij wordt met ondersch[eij]delijcke brieven bericht dat men sich inden [..] hooft te [..]" and carries **two lines
  of dotted numeral groups inside the prose**, about 20 groups, then the clear text resumes ("[..] seer schadelijcke adviysen hier bouen
  int landt, om Uwe Hoog Mogenden regieringe hatich te maecken"). By eye at 1200 px the groups run "22.x. 43. 9. 10.b. 46.f. 67.1[?].
  24.x. 40.d. 24. a. 61. 3. 23.x. 42.d. 22.x. 19.m. 24.x. 119." (every token M; a sighting, not a transcription of record).
- **Date and signature** (scan 424, left page, 1200 px, M): the close reads "uyt Heydelberg desen xvij[den] Septembris xvj[c] xxj", then
  "Uwer Hoog Mogenden onderdanichste ende getrouwste dienaer", signed "Van Brederode" with a paraph. So scans 416?-424 are the letter of
  **17 Sept 1621** that Resolutien SG NR 5 p. 295 res. 1879b calendars as "S.G. 6021 (orig.). Gedeeltelijk in code" (identification M:
  date, place and signature match the calendar entry; one letter of that date seen). The letter's opening is most likely scan 416
  (head "Hooge ende Mogende Heeren", date at the head "[..] Sept 1621", address leaf on the left; 700 px, M).
- **Design, by eye (M):** **not the full pair+letter form of scans 375/379.** On 379 the units are two consecutive two-digit numbers plus a
  letter ("22 23 x", "40 41 d", "46 47 j/f"); on 423 most units are **one number plus a letter** ("22.x", "40.d", "46.f", "24.x"), with
  some bare numbers (43, 9, 61, 3, 119 -- one above the 10-84 range of 379) and at least one bare letter ("a"). Three units on 423 repeat
  the first number and the letter of a 379 unit (22.x ~ 22.23.x, 40.d ~ 40.41.d, 46.f ~ 46.47.j/f): a lead that the same code is
  written in an abbreviated form, or a related table, M; not tested, nothing read.
- **Duplicate:** none seen. The 13 Aug letter's duplicate sat four scans after its original (375/379); scans 425-451 (the PREREG's one
  further batch) show no numeral block at sheet size. A duplicate of the 17 Sept letter may sit further on, or not survive.
- Every other scan (52): Dutch letters to the States General with Brederode closes, French and Dutch copies and extracts ("Extract ..."
  headings on 440, 444?, 447?), address leaves; no other numeral block, key table, interlinear decipherment or figure postscript at
  sheet size. **Last scan screened: 451** (stride 1, 398-451). Scan 424's right page starts a new document endorsed about "24 sept / 4 oct
  1621" (M), so the liasse here is in late September 1621.
- Limits: 700 px tiles on sheets at about 2,000 px can miss a block of a dozen groups or fewer; dates M; one reader.

### Separate intake candidate (recorded only): inv. 6021 scan 58
HEID-1621E's hit, recorded here as a candidate for its own intake and nothing more: a French text over both pages of scan 58, one hand,
with two-digit groups in dotted runs (to about 60) and three- to four-digit standalone name codes (426, 1684, 2436, 1870, 2722, 1458,
1897, 1877, 2763, 2795, 1698), clear words naming Mansfeld, the Prince Palatine, the Emperor, the Duke of Bavaria, "la dispensation du
mariage", Glatz (all M). **Date line: not on scan 58** (HEID-1621E: no address, signature or date on that opening); scans 57 and 59
not looked at in this job, so the date, sender and recipient are unread. Not the Brederode pair+letter layout; it does not pool with
this target. Its own intake (sender, date, check-solved, premise check) is a separate row.

**Status: open.** Next row for the parent: **the two-block transcription, priced per pass** -- `tools/iiif_lines.py` crops at native
size of scan 423 (the 17 Sept block, two lines) and of scan 375 (the 13 Aug signed witness, to control ciphertext.tsv from 379), pasted
before the first call; two blind Sonnet readers per block + one reconciliation per block = 6 passes x ~USD 1.4 = ~USD 8.4 (cap 9; box 75
minutes; service.archief.nl <= 6). Then the pooled unit inventory (13 Aug + 17 Sept) through spec test 1 again with its matched control.
If the duplicate of 17 Sept matters as a second witness: a continuation screen from scan 452 at stride 1, ~USD 1 per 54 scans.

## Remaining gaps (HEID-1621F, 15 Oct 2026)
Read so far: 0 of about 65 units (13 Aug block 45 units + 17 Sept block about 20 groups; nothing decoded; transcription all M)
- the 13 Aug and 17 Sept blocks together - blocker: not-attempted; the 17 Sept block (scan 423) located by HEID-1621F but not transcribed; next: two-block transcription (scan 423 + scan 375 witness) with two blind readers and one reconciliation per block, ~$8.4
- the pooled units - blocker: too-short; test 1 C2 rank-match control 0.010 vs gate 0.50 at N=45 (HYPOTHESES.md); a pool of about 65 units is still short; next: rerun spec test 1 on the pooled inventory with its matched control after the transcription, ~$3

## Escalation (HEID-1621F, 15 Oct 2026)
- [ ] siblings: the 17 Sept 1621 letter located (scans 416-424, block on 423); its duplicate not seen in 425-451; inv. 6021 screened stride 1 at 361-451, stride 3 elsewhere; next: two-block transcription, ~$8.4
- [ ] clear-pages: the clear prose around both blocks once both are transcribed
- [x] known-keys: design_prior run (non-discriminating at N=45); no SG/Palatinate key of 1618-1625 on file; key leaf 12578.1 is another post; inv. 6055/6056 not digitised (HEID-1621E)
- [x] print: Resolutien SG NR 5 read (HEID-1621D, HEID-1621E), no decipherment of a Brederode letter; no edition of his letters (HEID-1621C)
- [n/a] key-rebuild: no decipherment, gloss or key sheet of this system located to rebuild from
- [ ] image-check: scan 375 and scan 423 at native size not yet seen
- [x] retry: the NA and Huygens hosts answered (HEID-1621D, HEID-1621E, HEID-1621F, all 200)
Verdict: keep going: 1 internal gaps; cheapest next: two-block transcription (scans 423 + 375), ~$8.4

## HEID-1621G (15 Oct 2026, 21:11-21:2x UTC by date -u, account 2, Opus; for the orchestrator, owner account)
Crop step (run and pasted before the first reader call, 21:14 UTC):
```
$ python3 tools/iiif_lines.py --image $S/s375_block_native.jpg --out $S/c375 --prefix h375 --debug
s375_block_native.jpg (local): region 1779x1419, 15 lines, 15 bands x 1 segments; pitch 91 distance 63 prominence 69.6
  centres (region y): 45 124 220 307 406 492 584 672 754 862 948 1039 1141 1239 1336
  wrote 15 crops
$ python3 tools/iiif_lines.py --image $S/s423_block_native.jpg --out $S/c423 --prefix h423 --debug
s423_block_native.jpg (local): region 1900x720, 8 lines, 8 bands x 1 segments; pitch 94 distance 65 prominence 86.0
  centres (region y): 20 146 241 337 426 513 614 693
  wrote 8 crops
```
($S = session scratch; native regions 375 "900,780,1780,1420" and 423 "760,2000,1900,720" of NA 1.01.02 inv. 6021; readers get h375_L02-L13 and
h423_L04-L05 only, the lines carrying numerals.)

Brief: `.claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md`, JOB HEID-1621G. PREREG `heid1621g/PREREG-HEID1621G.md` pushed (3ea405b88)
before any fetch. Requests: **service.archief.nl 5** (METS + scans 375/423 at 1200 px + one native region per block), all HTTP 200, take/
release lines in ROOM.md; no other host. No image committed; sha1s of scans, regions and all 23 crops in `images/manifest.json`
(`heid_6021g`); `heid1621g/regen_heid1621g.sh` re-derives them. Readers: 4 blind Sonnet calls (2 per block, line crops only, no key, no
379 text), returns verbatim in `heid1621g/reads_raw.txt`; reconciliation by this worker against the crops (`recon_375.txt`,
`recon_423.txt`, every settlement commented). `heid1621g/units.py [--check]` rebuilds every table below. No decode, no key, no reading.

### Known-answer control: scan 375 vs ciphertext.tsv (scan 379), per PREREG
- **Per-unit agreement 37/45 = 0.822 against the 0.90 gate: FAIL.** As preregistered, the pass is a non-test for letter identity and
  every unit in both new TSVs is graded M (no S anywhere). Both witnesses parse into 45 units in the same order (no insertion/deletion).
- **Numbers: 96/96 agree** in aligned units (every numeral of 375 equals the numeral of 379 at the same place). **Letters: 37/45.**
- The 8 disagreements are all the trailing letter, and all are glyph-naming splits between the two passes, not order or number
  differences: 375 c / 379 r (76.77), e / w (13.14), s / j (46.47), x / c (64.65, twice), S / B (16.17), s / f (47.48), and one blotted
  letter after 46.47 that both 375 readers called a sign (379: f). Per the PX-BRODEC lesson, the gate here mostly measures which pass
  names a secretary-hand letter shape how, but that normalisation was not preregistered: **post-hoc only, not the gate**, merging the
  observed classes (r,c->x; w->e; j,f,b->s) gives 44/45 = 0.978 -- and that merge collapses c vs x, which 379 itself keeps apart, so it
  is no evidence either. Rule 3 status: the control could fail and did; nothing below is licensed as an inventory claim.
- Reader split rates (A vs B before reconciliation): 375 5 of 45 units (S/g twice, s/f, x/z on the same glyph classes); 423 3 of 14 units.

### Scan 423 (17 Sept 1621), transcription of record (all M)
`heid1621g/ciphertext_6021_423.tsv`: two lines, 14 units, after "... voor eenen" and before "spreij-dende":
`22.x 43.q 10.b 46.f 67.i 24.x 40.d 24.a | 61.3.23.x 42.d 22.x 19.m 24.x 119` (unit grammar of the PREREG: a maximal numeral run closed by a
letter). Splits: 43.q (both readers q; by eye the sign has this hand's 4-shape, not the 9 of 19 -- alt 9/4), 67 (one reader 6y), the minim
after 67 (read i as HEID-1621's rule for 379). 119 stands bare before the clear word; 61 and 3 are bare numbers, so the grammar folds
"61.3.23.x" into one run. HEID-1621F's sighting is reproduced except "9.10.b" (readers: q then 10.b).

### Unit inventory (`heid1621g/units.tsv`; M, for planning only -- control below gate)
- Distinct unit ids across 375 + 423: 41; shared ids: **0** -- by construction, since 375's units are number pairs and 423's are single
  numbers; the id comparison cannot see the relation the brief asks about, so the fixed question below is the one that matters.
- **Is the 17 Sept single-number form the 13 Aug pair's first number every time? No: 6 of 12** S1 units (22.x twice, 46.f, 67.i, 40.d,
  19.m) match the first number + letter of a 13 Aug pair; **9 of 12** match either number. Not first: 24.x (13 Aug 23.24.x, second
  number), 42.d (41.42.d, second), 10.b (13 Aug "38.10.11.b": first of the pair 10.11, but the preregistered maximal-run grammar folds 38
  in, so it does not count), 24.a (13 Aug 34.35.a), 43.q (no 13 Aug unit with q). With the letters M and the control failed, this is a
  lead, not a finding: the 17 Sept form is not a simple abbreviation to the first number in every case.

### Next row for the parent
1. **Settle the trailing-letter glyphs** before any pooled test: the 8 letter splits above plus 423's q-vs-4/9 sign go to
   `tools/lookalike_pass.py` across the three witnesses (crops on disk via regen), then, if machines still split, to the owner's sign
   sorter focus list (CLAUDE.md Usage 6); ~USD 1.5, cap 2, no network beyond regen's 5 requests.
2. **The pooled spec + first cheap test, cap 3** (only after 1, or on numbers only now): `specs/brederode-heidelberg-1621.json` with
   both letters' units (13 Aug 45 + 17 Sept 14 = 59 units), test 1 (unit inventory vs a Dutch word-frequency list under a frozen pool)
   with its matched control a synthetic word code of the same N and the same mixed pair/single form; at N=59 expect the C2 control to
   stay far under its 0.50 gate (0.010 at N=45, HYPOTHESES.md), so the test is likely too-short and should say so first.

## Remaining gaps (HEID-1621G, 15 Oct 2026)
Read so far: 0 of 59 units (13 Aug 45 + 17 Sept 14 transcribed, all M; nothing decoded)
- the trailing letters of both blocks - blocker: not-attempted; the 375-vs-379 control failed on letter naming only (numbers 96/96); next: lookalike pass on the letter glyphs across 375/379/423, ~$1.5
- the pooled units - blocker: too-short; test 1 C2 control 0.010 vs gate 0.50 at N=45; pooled N=59; next: pooled spec + test 1 with its matched control after the letter settle, ~$3

## Escalation (HEID-1621G, 15 Oct 2026)
- [x] siblings: the 17 Sept 1621 letter transcribed (scan 423, 14 units); its duplicate not seen in 425-451 (HEID-1621F)
- [ ] clear-pages: the clear prose around both blocks once the letters are settled
- [x] known-keys: design_prior run (non-discriminating at N=45); no SG/Palatinate key of 1618-1625 on file (HEID-1621E)
- [x] print: Resolutien SG NR 5 read, no decipherment of a Brederode letter; no edition of his letters (HEID-1621C/D/E)
- [n/a] key-rebuild: no decipherment, gloss or key sheet of this system located to rebuild from
- [ ] image-check: trailing-letter glyphs across 375/379/423 unsettled (control FAIL on letters)
- [x] retry: the NA host answered (HEID-1621G, 5 requests, all 200)
Verdict: keep going: 1 internal gaps; cheapest next: lookalike pass on the trailing letters, ~$1.5

## HEID-1621H (15 Oct 2026, 22:11-22:2x UTC by date -u, account 2, Opus; for the orchestrator, owner account)
Brief: `.claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md`, JOB HEID-1621H. PREREG `heid1621h/PREREG-HEID1621H.md` pushed (7f4320f16)
before any count. Disk only: 0 network requests, 0 vision calls, no reader subagent. No decode, no key, no reading.
**Departure from the brief, stated:** the brief says the HEID-1621G crops are on disk; they are not in this container (they lived in
that session's scratch, and `heid1621g/regen_heid1621g.sh` needs 5 service.archief.nl requests, which this job may not make). So the
look-alike pass ran its `confusion` and `reconcile` stages on the reads on disk, with an explicit "no re-read" row per flagged tile.

### Step 1: look-alike pass on the trailing letter signs (`heid1621h/letters.py --check`)
- 147 letter-position rows: 375 reader A vs B, 423 reader A vs B, 379 reader A vs B (from ciphertext.tsv notes; the eye's noted
  alternative where both readers agreed), and the 45 aligned 375-vs-379 units. **22 split positions**; named pairs
  (`heid1621h/confusion.tsv`): B/S 3, r/x 3, S/g 2, c/r 2, c/x 2, f/s 2, and once each 9/g, 9/q, B/b, sign/f, e/w, f/j, j/s, x/z.
- `tools/lookalike_pass.py reconcile`: 0 relabelled, 22 UNSETTLED (residual 0.150 -- a 2-of-3 figure on the reads, not accuracy,
  CLAUDE.md Usage 6). All 22 go to `heid1621h/focus.tsv` for the owner's sign sorter (never blocking).
- Per letter sign after the pass (`heid1621h/per_sign.tsv`, agreed positions / positions carrying the sign): a, d, i, k, m, o, p, v
  1.0; b 0.90; x 0.80 (30); c 0.75 (16); f 0.67; g 0.63; e, w 0.5; s 0.4; S 0.17; B, j, r, q, 9, z 0.0. The splits sit in three
  shape families: the hooked x/r/c sign, the long-s family f/s/j, and the capital S/B/g.
- **Control re-run, 375 vs 379 post-pass units: 37/45 = 0.822 against 0.90 -- FAIL** (unchanged, as it had to be with no tile
  settled). The letters stay M; the pooled spec declares the letter an unreliable field and keys units on the numerals.

### Step 2: pooled spec
`specs/brederode-heidelberg-1621.json` rewritten: ciphertext = 13 Aug (379; 375 witness: numerals 96/96, units 37/45) + 17 Sept
(423, 14 units), pooled N=59; alphabet with the letter-field warning; constraints including the counted single-vs-pair test below;
tests in order; `judge` nl16 with its era caveat; the HEID-1621D single-letter result kept under `previous_single_letter_test`.

### Step 3: test 1 at the pooled N, control first (`heid1621h/pooled.py --check`)
- Pools: nl16 two-piece windows (45 + 14 tokens from independent places): word median 50 (p05 43, p95 54), syllable-proxy 49 (42-54),
  letter 19 (16-21).
- **Matched control C3** (300 synthetic word codes from the held-out file, same 45/14 division and the 423 form split, same keys,
  same decision rule): word-band share **0.593 under key KT** (as transcribed) and **0.777 under key KF** (single = first number),
  gate 0.90 -- **both below gate: the inventory test is a non-test at N=59.** Target K recorded, band not read: KT 36, KF 29.
- C2 rank-match at N=59: 0.017 (max 0.119) vs gate 0.50, below gate; the target's rank-match not run.
- **Counted test "single = first number"** (12 S1 units of 423 vs the 40 pair units of 379): numbers only, first 6/12 (value null
  mean 3.35, p 0.089) and either 10/12 (mean 5.76, p 0.013) -- neither under p 0.01, so "single = first number" is **not** supported
  as a rule. With the letter sign: first 6/12 and either 9/12 against the shuffled-pairing null (means 1.09 and 2.25, p 0.0002 and
  < 0.0001): where a 17 Sept number recurs in a 13 Aug pair it carries the same letter sign far more often than chance. That is a
  counted lead (M; the letters themselves are M) for "two letters, one key", not a key and not a reading. HEID-1621G's 6/12 and 9/12
  (with letters, on 375) are reproduced on 379.

Spec did not move (CLAUDE.md 3a): test 1 is a non-test at N=59 and the letter control still fails. Requests: none (0 hosts).

## Remaining gaps (HEID-1621H, 15 Oct 2026)
Read so far: 0 of 59 units (13 Aug 45 + 17 Sept 14 transcribed, all M; nothing decoded)
- the trailing letters of both blocks - blocker: not-attempted; disk-only look-alike pass left 22 positions unsettled (no crops in this container), control 0.822 < 0.90; owner's sorter on heid1621h/focus.tsv in parallel, never blocking; next: crop re-read via regen_heid1621g.sh (5 NA requests) + tools/lookalike_pass.py windows, ~$2
- the pooled units - blocker: too-short; test 1 C3 0.593 (KT) / 0.777 (KF) vs gate 0.90 and C2 0.017 vs 0.50 at N=59; next: sibling search for more units in this code, inv. 6021/6025

## Escalation (HEID-1621H, 15 Oct 2026)
- [x] siblings: the 17 Sept 1621 letter transcribed and pooled (HEID-1621G/H); no further Brederode cipher letter located yet
- [ ] clear-pages: the clear prose around both blocks once the letters are settled
- [x] known-keys: design_prior run (non-discriminating at N=45); no SG/Palatinate key of 1618-1625 on file (HEID-1621E)
- [x] print: Resolutien SG NR 5 read, no decipherment of a Brederode letter; no edition of his letters (HEID-1621C/D/E)
- [n/a] key-rebuild: no decipherment, gloss or key sheet of this system located to rebuild from
- [ ] image-check: trailing-letter glyphs across 375/379/423 unsettled (control FAIL 0.822 after the disk-only look-alike pass)
- [x] retry: the NA host answered (HEID-1621G, 5 requests, all 200)
Verdict: keep going: 1 internal gaps; cheapest next: crop re-read of the 22 letter positions via regen + lookalike windows, ~$2

Status: open. Next row for the parent: (1) letter settle -- `bash heid1621g/regen_heid1621g.sh` (5 NA requests, take/release lines)
then `tools/lookalike_pass.py windows --tiles heid1621h/tiles_letters.tsv` and one blind re-read of the 22 windows, reconcile,
`heid1621h/letters.py` control re-run, cap 2; the owner's sorter on `heid1621h/focus.tsv` in parallel. (2) Sibling search in NA
1.01.02 inv. 6021/6025 (Brederode 1621-1622) for more units in this code, cap 3 -- pool size decides whether any test can run.

## HEID-1621I (15 Oct 2026, 23:13-23:3x UTC by date -u, account 2, Opus; for the orchestrator, owner account)
Brief: `.claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md`, JOB HEID-1621I. PREREG `heid1621i/PREREG-HEID1621I.md` pushed (b4dd11658)
before any fetch or re-read. Requests: **service.archief.nl 4** (METS + the three native block regions; take/release lines in ROOM.md),
**www.nationaalarchief.nl 9** (contact page and form, three guessed order-page paths that answered 404, four item pages for
availability); all others 200. 0 vision calls, no reader subagent: the re-read is this worker's own eye on the native crops. No decode,
no key, no reading.

### Step 1: crops regenerated, look-alike pass WITH crops
- **Departure from the brief, stated in the PREREG before the fetch:** the native block regions (the reads' own source, sha1s on file)
  were fetched instead of the 1200 px scans (4.3x below native, too small for a secretary-hand letter). `heid1621i/regen_crops.sh OUTDIR`
  re-derives them (skips files already present) and checks each region sha1 against images/manifest.json:
```
375 900,780,1780,1420 7e4cf1f3ce0a887de5f8d03dc1b15dfa176fb791 MATCH
379 730,1640,1960,1420 ac1477f81fa528d81e1d440e15630f7532347776 MATCH
423 760,2000,1900,720 b14323f48c48a1ac16e183a7e405de851849b96f MATCH
$ python3 tools/iiif_lines.py --image $O/s375_block_native.jpg --out $O/c375 --prefix h375 --debug   -> 15 lines, wrote 15 crops
$ python3 tools/iiif_lines.py --image $O/s379_block_native.jpg --out $O/c379 --prefix h379 --debug   -> 15 lines, wrote 15 crops
$ python3 tools/iiif_lines.py --image $O/s423_block_native.jpg --out $O/c423 --prefix h423 --debug   -> 8 lines, wrote 8 crops
```
  The 23 h375/h423 crops are byte-identical to HEID-1621G's (sha1 23/23 against manifest heid_6021g). No image committed.
- Re-read (`heid1621i/reread_letters.tsv`, one row per tile with the eye's reason): each of the 22 split positions of heid1621h/focus.tsv
  read on its line crop and compared with agreed exemplars of the same hand. `tools/lookalike_pass.py reconcile` (fixed 2-of-3 rule) via
  `heid1621i/settle.py [--check]`: **14 settled, 8 unsettled** (tool residual 8/147 = 0.054 -- agreement after a non-blind third read,
  not accuracy). Settled: the 16.17 sign is one looped S in all four places (g and B readings dropped; distinct from the 11.12 b sign);
  the 22.23/23.24 sign is x at 379 L02/L06/L10; 31.32 at 379 L12 is the same curved-tail g as 375 L11; 423's sign after 43 is q (straight
  stem; this hand's 9 has a curved tail), so 423 L04 stays "43.q"; the long-s at 375 L07.1 and both 47.48 glyphs have no crossbar (s, not
  f; compare the barred f of 379 L11 29.20.f).
- Unsettled (to the owner's sign sorter, `heid1621i/focus.tsv`, never blocking): 76.77 (375 a plain c, 379 the small x/r shape -- two firm
  different readings, a **witness difference**, not a reader error); 13.14 (one double-bowl shape in both witnesses, e/w naming); 46.47
  at 379 L03 (short sign, j or a short long-s); 64.65 twice (one curled sign in all six places, named x on 375 and c on 379 -- **likely its
  own sign**, distinct from the 22.23 x and the 76.77 plain c; a class question for the sorter); unit 44 (375 an ink blot). Two further
  sorter rows: 379 L07's agreed "f" at 46.47 looks like the unbarred long-s settled s elsewhere (an agreed sign, so not re-read here), and
  the 64.65 class question.
- **Control re-run, 375 vs 379 on the post-pass units: 38/45 = 0.844 against the 0.90 gate -- FAIL.** Changes: +unit 23 (both S), +unit 27
  (both s), -unit 22 (375's reconciled f became s; 379's agreed f there was not a tile, see the sorter row). By the PREREG the trailing
  letters stay **M**; nothing is licensed at S-as-transcribed; the spec keeps the letter field declared unreliable. Of the 7 misses left, 3
  are naming questions on one shape (13.14, 64.65 x2), 1 is a witness difference (76.77), 1 an ink blot, 2 the long-s family.

### Step 3: request for the period key material
`REQUEST.md` written: NA 1.01.02 inv. 6056 (Mansfelt 13 Mar 1622, "gedeeltelijk in cijfer, met de oplossing", Resolutien NR 5 p. 447 res.
2931), 6055 (SG minute "met code", 1621, res. 467-468) and 12578.1 (key "Rangh van de grootte tot Constantinopelen", 1618-1622), each
`"availability": "PHYSICAL"`, 0 scans on the archive's own item page on 15 Oct 2026 (control inv. 6021 `"DIGITALIZED"`, 810, same
minute); route = the NA contact form (read on the day; no price stated on the pages read); a Dutch draft under the form's 1500
characters, with the question whether 6056's oplossing or 6055's code covers the 1621 pair+letter system. ASKS row 170 for the owner's
desk. The draft still needs a CONTRIBUTIONS.md row and the gate-7 fact check before it is sent.

## Remaining gaps (HEID-1621I, 15 Oct 2026)
Read so far: 0 of 59 units (13 Aug 45 + 17 Sept 14 transcribed, all M; nothing decoded)
- the trailing letters of both blocks - blocker: not-attempted; crop re-read settled 14 of 22 splits but the 375-vs-379 control is 38/45 = 0.844 < 0.90 (heid1621i/settle_result.json); next: the owner's sign sorter on heid1621i/focus.tsv (10 rows, backlog, never blocking), ~$0
- the pooled units - blocker: too-short; test 1 C3 0.593 (KT) / 0.777 (KF) vs gate 0.90 at N=59 (HEID-1621H); next: screen the later Brederode liasse inv. 6022 (1623-1626, digitised, 595 scans) for more units in this code, ~$4
- the key - blocker: waiting-on ASKS row 170 (Nationaal Archief reproduction of 1.01.02 inv. 6056, 6055, 12578.1: the 1622 decipherment, the 1621 SG code minute, a key of 1618-1622; not digitised, REQUEST.md)

## Escalation (HEID-1621I, 15 Oct 2026)
- [ ] siblings: the later Brederode liasse inv. 6022 (1623-1626, digitised) not screened; planned: contact-sheet screen by the OBRED-6021 method, ~$4
- [ ] clear-pages: the clear prose around both blocks once the letters are settled
- [x] known-keys: design_prior run; no SG/Palatinate key of 1618-1625 on file; NA key material located and requested (inv. 6056/6055/12578.1, REQUEST.md)
- [x] print: Resolutien SG NR 5 read, no decipherment of a Brederode letter; no edition of his letters (HEID-1621C/D/E)
- [n/a] key-rebuild: no decipherment, gloss or key sheet of this system is in hand to rebuild from
- [x] image-check: native crops re-read (HEID-1621I), 14 of 22 letter splits settled; the rest to the owner's sorter
- [x] retry: the NA hosts answered (HEID-1621I, 4 + 9 requests)
Verdict: keep going: 1 internal gaps; cheapest next: the owner's sign sorter on heid1621i/focus.tsv, ~$0

```
$ python3 tools/gaps_check.py brederode-heidelberg-1621
OK keep-going brederode-heidelberg-1621: keep going: 1 internal gap(s), 2 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```
(The target is `open`, not `partial`: the 6022 sibling screen and the sorter are untried steps that depend on nobody outside, so rule 5's
parked state does not apply.)

Status: open. Next row for the parent: (1) screen NA 1.01.02 inv. 6022 (Brederode 1623-1626, 595 scans) at 700 px on contact sheets with
the OBRED-6020 sheet controls for numeral blocks in this code, cap 4 -- the pool decides whether any test can run; (2) the REQUEST.md
draft to a CONTRIBUTIONS.md row and the gate-7 check (OUT-CHECK), then the owner's send (ASKS 170); (3) the sorter rows in parallel.

## HEID-1621J (16 Oct 2026, 00:11-00:3x UTC by date -u, account 2, Opus; for the orchestrator, owner account)
Brief: `.claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md`, JOB HEID-1621J. PREREG `heid1621j/PREREG-HEID1621J.md` pushed (13d72014a)
before any fetch; sheet calls `heid1621j/sheetcalls.txt` pushed per batch (30581b3e4, 29f5ae5a1, then batch 3) before each sheet key was
opened. Requests: **resources.huygens.knaw.nl 22** (14 searches, 2 pages.json, 6 OCR pages; all 200) -- **2 over the brief's 20**, my
count error, stated here; **service.archief.nl 129** (1 METS + 124 scans at 700 px + 4 at 1200 px; all 200; take/release lines in
ROOM.md); www.nationaalarchief.nl 0. 0 vision calls, no subagent: the screen is this worker's own eye. No image committed; sha1s in
`images/manifest.json` (`heid_6022j`); `heid1621j/regen_heid1621j.sh` re-derives scans and sheets (sheet keys `heid1621j/sheetkey{1,2,3}.json`).
No transcription, no decode, no key, no reading.

### (1) The edition list: `heid1621j/code_letters.tsv`
Resolutien SG NR 5 (source 5), searched for "in code" (6), "in cijfer" (3), "gecodeerd" (0), "code" (6), "Gedeeltelijk" (21, two
batches; catches "in co- de" split by the OCR), "cijfercode" (5), "geheimschrift" (1), "cijfers" (1, index), "cijfer" (3); pages 11, 275,
578, 580, 581 read in OCR. **Only the two known Brederode letters carry a code note in 1621-1622** (13 Aug 1621, p. 260 res. 1644b; 17 Sept
1621, p. 295 res. 1879b; both 6021, both already located). New in NR 5: p. 578 res. 3787b (July 1622, Brederode dd. Straatsburg 9 July,
6021 kopie) -- the States General order him "dergelijke berichten voortaan in geheimschrift te sturen"; the letter itself carries no
code note. The other code hits in NR 5 are other senders (Aitzema p. 11, SG minute p. 82, Bremen envoys p. 275, Haga, Bilderbeke, Mansfelt).
Because step 2 names inv. 6022 (1623-1626), NR 6 (source 6) and NR 7 (source 7) were searched for "code" and "cijfer" (4 searches):
- **NR 6 p. 260, res. 1721 (25 Aug 1623):** "Een brief dd. Straatsburg 12 aug. van Brederode bevat enkele regels in cijfer. Met een besluit
  wordt gewacht tot dit is opgelost"; note 1721a "S.G. 6022 I (orig.). Over het aanhalen van banden met de evangelische Zwitserse kantons.
  De oplossing van het cijfer van de hand van Joachimi." (OCR page read.)
- **NR 6 p. 337, note 2142a:** "S.G. 6022 I (orig.). Het cijfer is opgelost door Joachimi." (search snippet only; the page, and so the
  sender and date, not read -- the Huygens budget was spent; Brederode by the inventory, 6022 = Liassen Agent Brederode, M.)
- NR 7 "code"/"cijfer": hits are other posts (Haga, 6898 France), none in 6022. NR 6 p. 549 "Bij het duplicaat een in code gestelde
  mededeling" and p. 22/28/32 (orders to write "afzonderlijk in code") were not opened: their senders are not in the snippets.

### (2) Screen of inv. 6022 (METS 412b1414-afa2-42fe-b56d-2b5f705e5005, 595 scans)
Orientation probes at 700 px (scans 40, 80, 120, 160, 200; datelines M): scan 40 closes "uyt Straesburg dese 30en January 1623"; scan 160
is German news "Den 1x Julij 1623". Screen at stride 1, 700 px, contact sheets (SHEET_SCANS=9, OBRED-6020 controls, seeds 16220-16222):
165-218, 219-272, 152-159 + 161-164. **Controls 48 of 48 placed correctly** (14 sheets); no sheet is a non-test. **The sheets called no hit
-- and that was wrong three times out of three:** each block below sits inside dense prose and is one to six lines long, and none was seen
on a 525 px sheet tile. They were found on 700 px composites (six scans per 2100 px image, 700 px per scan) viewed from disk for dateline
orientation, then re-looked at 1200 px. Composites were viewed for 161-185 only.
- **12 Aug 1623 (res. 1721) -- located, M.** Scans 165-167: 165 opens the letter (endorsed "L. 19 Aug 1623", head "Hooge ende Mogende Heeren");
  166 right page carries **about five and a half lines of dotted number groups inside the prose** ("... soude sijn 43. c. 22. 40. y. 61 ende
  bequaemste occasie 69. b. 40 ...", groups up to 214, a lower-case letter after some numbers, a few clear words between); 167 closes "uyt
  Straesburg desen 12en Augusti 1623" (day M), signed. **Duplicate:** 170-172 (address leaf 170; 171 the same opening and the same block;
  172 signed). On 171, **a marginal note in a smaller, different hand, about eight lines, is bracketed against the block** -- placement and
  the res. 1721a note ("De oplossing van het cijfer van de hand van Joachimi") make it a candidate for that solution; not read, M.
- **About Oct 1623 (res. 2142) -- probably located, M.** Scan 181: a Brederode letter (head endorsement read "d. 10 / .. 31 Oct 1623", M;
  mentions Basel and Bern in clear, M) with **one line of number groups** ("74. 10. x. 49. 43 41. x et 6. 45. 41. 12. 46. m. 22 p. 52. 67.
  43. 17. T.", every token M) and again a short marginal note in a small hand beside that line. The match to res. 2142 rests on month and
  inventory only (the resolution page was not read).
- **System by eye (M):** neither 1623 block is the full pair+letter form of 375/379 (consecutive pairs plus a letter); both are mostly single
  numbers, some followed by a letter, like the 17 Sept 1621 block on 423 ("22.x", "40.d"). Shared-looking units across 1621 and 1623 ("40" +
  letter, "46", "22") are a lead that the same table continued, not tested.
- **Unit count estimates (M, by eye at 1200 px):** 166/171 block about 50 tokens (numbers and letters together); 181 about 20.
- Elsewhere in 152-272 at sheet size: Dutch letters with Brederode closes, German and French news copies and extracts, a "Relatie" title
  leaf, address leaves; scan 227 is a page covered in pen trials (no numeral run). Datelines run July 1623 (160) to Feb 1624 (about 260).
- Limits: the sheet method missed every small block here, so "no hit" on 186-272 (sheets only) and on the earlier stride-3 screens of 6021
  (HEID-1621E, OBRED-6021) is weak for blocks of one to six lines inside prose; 700 px composites, not sheets, are the instrument for this.

### Next row for the parent
(1) **The two marginal notes** (171, 181): native region crops (`tools/iiif_lines.py --image`), two blind reads + one reconciliation per note
at about USD 1.4 per pass (2 notes x 3 passes = about USD 8.4): if they are Joachimi's decipherment, they are period key material for the
1623 system (grade H for the glossed tokens), and the parent decides what that licenses for the 1621 blocks. (2) The 1623 blocks (166, 171
as two witnesses of one block; 181): 3 blocks x 3 passes x 1.4 = about USD 12.6. (3) Read Resolutien NR 6 p. 337 (res. 2142, 1 Huygens
request) for the sender and date, and the NR 6 p. 22/28/32/549 entries; then a 700 px composite pass over 6022 186-595 and over 6021 for
short blocks the sheets missed (disk-first where scans are already fetched).
**Projected pooled N** if every located block is transcribed and the systems pool: 59 (1621: 45 + 14) + about 50 (12 Aug 1623) + about 20
(Oct 1623) = **about 129 units**, estimate M; whether 1623 pools with 1621 is itself the first question the glosses can answer.

## Remaining gaps (HEID-1621J, 16 Oct 2026)
Read so far: 0 of about 129 units (1621: 59 transcribed, all M; 1623: about 70 located, not transcribed; nothing decoded)
- the trailing letters of both 1621 blocks - blocker: not-attempted; 375-vs-379 control 38/45 = 0.844 < 0.90 (HEID-1621I); next: the owner's sign sorter on heid1621i/focus.tsv (backlog, never blocking), ~$0
- the 1623 blocks and their marginal notes (6022 scans 166, 171, 181) - blocker: not-attempted; located by HEID-1621J, possibly glossed by Joachimi; next: native crops, 2 blind reads + 1 reconciliation per note and per block, ~$21
- the pooled units - blocker: too-short; test 1 C3 0.593 / 0.777 vs gate 0.90 at N=59 (HEID-1621H); next: rerun spec test 1 on the pooled inventory after the 1623 transcription, ~$3
- the key - blocker: waiting-on ASKS row 170 (Nationaal Archief reproduction of 1.01.02 inv. 6056, 6055, 12578.1; REQUEST.md)

## Escalation (HEID-1621J, 16 Oct 2026)
- [ ] siblings: 6022 letters of 12 Aug 1623 (165-167, dup. 170-172) and about Oct 1623 (181) located; 6022 186-595 not checked on composites; planned: composite pass, ~$2
- [ ] clear-pages: the clear prose around all blocks once transcribed
- [ ] known-keys: possible period decipherment beside the 1623 blocks (marginal notes on 171 and 181, Resolutien NR 6 res. 1721a/2142a); planned: read the notes, ~$8.4
- [x] print: Resolutien NR 5 and NR 6 searched; no printed decipherment of any Brederode cipher passage (NR 6 records Joachimi's solutions, does not print them)
- [n/a] key-rebuild: nothing in hand to rebuild from until the marginal notes are read
- [x] image-check: 1200 px re-looks of 166, 167, 171, 181 (HEID-1621J)
- [x] retry: the NA and Huygens hosts answered (HEID-1621J)
Verdict: keep going: 2 internal gaps; cheapest next: read the marginal notes on 6022 scans 171 and 181, ~$8.4

## HEID-1623A (16 Oct 2026, 01:12-01:3x UTC by date -u, account 2, Opus; for the orchestrator, owner account)
Brief: `.claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md`, JOB HEID-1623A. PREREG `heid1623a/PREREG-HEID1623A.md` pushed (117f37a4a)
before any native crop or reader call. Requests: **service.archief.nl 8** (METS; scans 166, 171 at 1200 px, sha1 MATCH heid_6022j; 3
native regions; 2 widened re-fetches as the PREREG allows -- the first 171 block region clipped its first cipher line, the first note region
its right edge); take/release lines in ROOM.md. **Vision calls: 6 blind Sonnet reader calls** (2 per unit, line crops only, text only;
raw returns verbatim in `heid1623a/reads_raw.txt`) **+ 3 reconciliations** by this worker against the native regions. No image committed;
sha1s in `images/manifest.json` (`heid_6022_1623a`); `heid1623a/regen_heid1623a.sh` re-derives everything. No reading of the 1621 pair, no
key.tsv edit, no decode.

Crop commands (run before the first reader call; debug overlays checked):
```
$ python3 tools/iiif_lines.py --image $S/u1_166_block.jpg --out $S/c_h166 --prefix h166 --debug
  region 2041x668, 7 lines, 7 bands x 1 segments; pitch 93 distance 65 prominence 97.2; wrote 7 crops
$ python3 tools/iiif_lines.py --image $S/u2w_171_block.jpg --out $S/c_h171 --prefix h171 --debug
  region 2016x710, 8 lines, 8 bands x 1 segments; pitch 86 distance 60 prominence 100.0; wrote 8 crops
$ python3 tools/iiif_lines.py --image $S/u3w_171_note.jpg --out $S/c_n171 --prefix n171 --debug
  region 681x627, 9 lines, 9 bands x 1 segments; pitch 44 distance 30 prominence 34.9; wrote 9 crops
```
(the note crops were given to reader B at 2x, a plain LANCZOS enlargement of the same crops; reader A had them at native size.)

### Outputs (`heid1623a/`, all regenerated by `build.py`, `--check` clean)
`ciphertext_6022_166.tsv`, `ciphertext_6022_171.tsv` (line, pos, kind, token, alt, confidence, why), `witness_166_171.tsv`,
`note_6022_171.tsv` (39 word rows, every word M), `grammar_1623_vs_1621.tsv`, `pairs_1623.tsv`, `align_1623.tsv`, `align_key_1623.tsv`
(the tool's working output, NOT a key: the alignment did not pass), `shuffle_1623.json`, `poscontrol.py`. No `key_1623_draft.tsv`.

### (1) Witness control, 166 vs 171 (gate 0.90): **61/64 = 0.953 PASS**
Token streams (numerals and single letters): 166 has 64 (47 numerals, 17 letters), 171 has 63 (47, 16). The four differences: after
"59 h" 166 has **49**, 171 has **40**; 166 writes **78 78** where 171 has one 78; 171 has **69** between 49 and 16 where 166 has none
(166 instead carries "61" inserted above the line with carets, which 171 has in the line); 166 ends "a **d**", 171 "a" (a mark at the
binding edge after it, not counted). Caveat stated: the reconciler saw both witnesses and named two look-alike glyphs by one convention in
both (the x/r-like letter as x; the i-shaped 1 as 1), which raises agreement; where both readers of 166 wrote r, the token is M.
Grades per the PREREG rule: **49 of 64 (166) and 49 of 63 (171) tokens S-as-transcribed** (the sign as transcribed, no value read); the
rest M. Nothing is H or C.

### (2) Unit grammar, 1623 vs 1621 (descriptive, M)
The 1623 block is not the 1621 pair+letter system: of 33 adjacent numeral pairs only **1** is (n, n+1) (1621 scan 379: 40 of 41); the
letters stand alone between numerals (c, z, y, h, x, e, p, m, s, H, a, d), not as one trailing tag per unit; and the block mixes in clear
word fragments ("leux", "schrijvinge", "dische", "geven", "Wat Godt"). Under the heid1621g unit grammar 166 gives 24 units (4 P, 4 S1,
5 R, 4 L, 7 N) and 171 gives 23 -- the form labels are artefacts of that grammar here. **No 1623 unit coincides with a 1621 unit** (same
numbers and letter): 0. Of the 29 distinct 1623 numerals, 20 also occur somewhere in the 1621 units (both use the range 10-94; not evidence
of one table).

### (3) The marginal note on 171 (`note_6022_171.tsv`, every word M)
Reconciled: "mij selfs, bijde bequaemste / occasie onder coleur van / der inschrijvinge in de / Westindische Compagnie, te / besonderen,
bijde Switsersche / Evangelische cantons, / dewelcke te bewegen, [?] / te [?] wat Godt / sal willen geven." Readers A and B agreed on
little beyond "West-Indische Compagnie" and "inschrijvinge"; L01, L02, L05, L07 and L08 rest on the reconciler's eye (M). The note is
running Dutch, not a docket or a summary, and it carries the block's own clear words in the same order -- "bijde bequaemste occasie", "[in]
schrijvinge", "[Westin]dische", "wat Godt" -- so it is a clear rendering of this passage written beside it. Its subject (approaching the
Swiss evangelical cantons under colour of subscription to the West India Company) agrees with the edition's own note to res. 1721a ("Over
het aanhalen van banden met de evangelische Zwitserse kantons. De oplossing van het cijfer van de hand van Joachimi"); that it is
Joachimi's hand is not checked (M).

### (4) Alignment of the note to the block (PREREG rule 2)
Five (group, span) pairs, the 171 stream cut at the clear words the note also carries (`pairs_1623.tsv`); `tools/interlinear_align.py
align --code-prefix @ --code-chunk 6 --wildcard ? --keep-fs --shuffle 200 --seed 1623`: tokens 63, values 39; **CONSISTENT real 1;
shuffle mean 0.09, p95 1, max 2, p = 0.075 -- the PREREG gate (real > p95 and real >= 3) FAILs.** The PREREG's second, word-for-word
statistic does not apply: the system is not one code per word (the first pair has 7 codes against "mij selfs").
**Positive control (added after the target run, descriptive, not a PREREG gate):** the same five spans with a cipher generated from a
known one-code-per-chunk table at each pair's real token count (`poscontrol.py`, seeds 1-3), scored by the identical command: real 1, 1, 1
vs shuffle p95 0, 0, 1. A known-true gloss also cannot reach the gate's >= 3 at this N, so the target's FAIL is a **non-test: untestable
by this tool at this N (63 tokens, 5 pairs)**, not evidence against the note being the decipherment. No `key_1623_draft.tsv` (the PREREG
licenses one only on PASS).

### For the parent
- The 1623 system differs from the 1621 one by form (no consecutive pairs, free-standing letters, clear fragments); whether one table
  underlies both is not tested; the 1621 pair is not touched here.
- A different instrument, not a re-tune of this one (CLAUDE.md rule 3, third-attempt clause), is needed for the note: either more pairs
  (scan 181's block and note pooled with these five) or a letter-level hand alignment of the five pairs with its own positive control
  priced as a separate job. Rule 10 wording: the note is "a clear rendering written beside the passage", nothing more.

### Next row
**Scan 181 (about Oct 1623) block + its marginal note:** native regions from the 1200 px scan on disk via regen (2 + 2 NA requests),
`tools/iiif_lines.py --image`, 2 blind Sonnet reads + 1 reconciliation per unit (2 units: 4 x USD 1.4 + 2 = 7.6); then the alignment on
the pooled pairs (171 + 181) with the poscontrol.py positive control run FIRST at the pooled N (rule 3: control before target), ~USD 1.
Resolutien NR 6 p. 337 (res. 2142) read for 181's date and sender (1 Huygens request).

## Remaining gaps (HEID-1623A, 16 Oct 2026)
Read so far: 0 of about 129 units (1621: 59 transcribed, all M; 1623 12 Aug block: 64 tokens transcribed, 49 S-as-transcribed, no value read; Oct 1623: about 20 located, not transcribed; nothing decoded)
- the trailing letters of both 1621 blocks - blocker: not-attempted; 375-vs-379 control 38/45 = 0.844 < 0.90 (HEID-1621I); next: the owner's sign sorter on heid1621i/focus.tsv (backlog, never blocking), ~$0
- the 12 Aug 1623 code values (6022 scans 166/171) - blocker: not-attempted; the marginal note is a clear rendering of the passage but its code-level alignment is untestable by this tool at N=63 (HEID-1623A); next: pool with scan 181's note, positive control first, ~$9
- the Oct 1623 block and its note (6022 scan 181) - blocker: not-attempted; located by HEID-1621J; next: 2 units x (2 reads + 1 reconciliation), ~$7.6
- the pooled units - blocker: too-short; test 1 C3 0.593 / 0.777 vs gate 0.90 at N=59 (HEID-1621H); next: rerun spec test 1 after the 1623 transcription, ~$3
- the key - blocker: waiting-on ASKS row 170 (Nationaal Archief reproduction of 1.01.02 inv. 6056, 6055, 12578.1; REQUEST.md)

## Escalation (HEID-1623A, 16 Oct 2026)
- [ ] siblings: 6022 scan 181 (Oct 1623) located, not transcribed; 6022 186-595 not checked on composites; planned: 181 transcription ~$7.6, composite pass ~$2
- [x] clear-pages: the clear prose and the clear note around the 12 Aug 1623 block read (HEID-1623A, M)
- [ ] known-keys: the 171 note is a clear rendering of the passage (M); its code-level mapping untestable at N=63 by tools/interlinear_align.py; planned: pooled pairs with 181, positive control first, ~$9
- [x] print: Resolutien NR 5 and NR 6 searched; no printed decipherment of any Brederode cipher passage (NR 6 records Joachimi's solutions, does not print them)
- [ ] key-rebuild: from the note once an alignment passes its control; planned: as known-keys
- [x] image-check: native regions of 166 and 171 read (HEID-1623A)
- [x] retry: the NA host answered (HEID-1623A)
Verdict: keep going: 3 internal gaps; cheapest next: scan 181 block + note, ~$7.6

`python3 tools/gaps_check.py brederode-heidelberg-1621` (HEID-1623A): `OK keep-going brederode-heidelberg-1621: keep going: 3 internal gap(s), 3 step(s) untried`

## HEID-1623CAL (16 Oct 2026, 02:16-02:4x UTC by date -u, account 2, Opus; for the orchestrator, owner account)
Disk only, no network, no readers, no images; no reading, no key. PREREG `heid1623cal/PREREG-HEID1623CAL.md` pushed (b7e78baf6) before any run.
Question: can `tools/interlinear_align.py`, run exactly as HEID-1623A ran it (`align --code-prefix @ --code-chunk 6 --wildcard ? --keep-fs
--shuffle 200 --seed 1623`), pass its own gate (CONSISTENT real > shuffle p95 AND real >= 3) on a KNOWN-TRUE gloss with the 1623 block's
grammar, and at what N? Synthetic pairs (`heid1623cal/calib.py`): pair sizes resampled from the real 1623 pairs (7, 6, 7, 32, 11 tokens),
Dutch spans with the 171 note's word-length distribution (words by frequency from tools/data/nl16, 1569-1589), 2.0 letters per token as
in the real pairs, codes from the block's alphabet (numbers 1-99, 26% letter codes). Design A (gating) = HEID-1623A's poscontrol.py
random-cut design; design B (descriptive) = fixed 2-letter chunks, so recurring chunks recur. 20 seeds at each N.

| design | N | seeds passing | mean real CONSISTENT | mean shuffle p95 |
|---|---|---|---|---|
| A | 64 | 0/20 | 0.40 | 0.85 |
| A | 85 | 0/20 | 0.70 | 1.10 |
| A | 120 | 2/20 | 1.40 | 1.75 |
| A | 200 | 2/20 | 1.60 | 2.45 |
| B | 64 (realised 79) | 0/20 | 0.85 | 1.60 |
| B | 85 (realised 105) | 2/20 | 1.30 | 2.05 |
| B | 120 (realised 152) | 2/20 | 2.30 | 3.55 |
| B | 200 (realised 248) | 1/20 | 3.10 | 5.45 |

**No N reaches 18/20; the smallest passing N is above 200 for design A** (and above about 250 tokens even for the easier fixed-chunk
design B, where the shuffle p95 rises with N about as fast as the true count). Result: untested-by-this-tool below N = 200 at least.
Correction logged: a pair-size trim bug (`out[-2] += out.pop()` evaluation order) put 4 of 80 design-A runs off their N; fixed in calib.py
and those 10 (seed, N) rows (both designs) rerun before the table above; the full `calib.py --check` rerun takes about 19 minutes on 4 CPUs
and was not run inside this box (the summary is recomputed from calib_runs.tsv).

**Verdict: read scan 181 for a pooled alignment: no (next instrument or more material).** Pooling to about N=85 gives this tool 0/20 on a
true gloss. Scan 181 is still worth transcribing for its own sake (sibling, gaps list), but not to rescue this alignment.
What else the 1623 clear note licenses: the 12 Aug 1623 passage is a **text-known item on the leaf** -- the marginal note (171) is a period
clear rendering written beside the block (M, HEID-1623A), so the passage is a candidate for N0 (the verifier assigns the class) as a period decipherment on the
leaf, not a reading of ours; it is AUDIT-ready in that wording for a verifier (key source: none of ours; text: known). Next instruments, not
a re-tune of this one: (1) a letter-level hand alignment of the five pairs (each code against the note letters it covers, fixed by the clear
words), priced as its own job with a positive control built by this calib.py at N=64 first; (2) the period key itself (ASKS row 170, NA
inv. 6056/6055/12578.1). For the parent: the known-keys step's instrument `tools/interlinear_align.py` is [retired] for this hypothesis at
N <= 200 (rule 3); the Escalation line's "planned: pooled pairs with 181, positive control first, ~$9" should be replaced by (1) or (2).

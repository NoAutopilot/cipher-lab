open
- **Status:** open -- the recipient-side standard edition, *Resolutiën der Staten-Generaal, nieuwe reeks 1610-1670*, deel 5
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

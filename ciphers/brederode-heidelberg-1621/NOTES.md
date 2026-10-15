blocked
- **Status:** blocked -- the recipient-side standard edition, *Resolutiën der Staten-Generaal, nieuwe reeks 1610-1670*, deel 5
  (1621-1622, ed. J. Roelevink, RGP, 1983), could not be opened this session: resources.huygens.knaw.nl/retroboeken/statengeneraal
  answered HTTP 503 twice (17:13 and 17:14 UTC, 15 Oct 2026), and the Google Books copy (id M-hDAQAAMAAJ) is NO_PAGES (snippet only).
  The volume is known to calendar Brederode's Heidelberg letters (Google Books snippet: "Brederode, dd. Heidelberg 20 dec. 1620");
  whether it summarises the letters of 8 and 13 Aug 1621 (received 20 Aug 1621) or their cipher passage is not yet known.
  Blocked on a host outage, not on a person: the next step is a retry of the Huygens search (below).
- **Sender:** P. van Brederode, agent of the States General at Heidelberg (signature "P van Brederode" read on scan 375, HEID-1621B)
- **Recipient:** the States General, The Hague. **Date:** Heidelberg, 13 Aug 1621 (received "L. 20 Aug. 1621", endorsement on scan 380)
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
- (d) Recipient's side: the Resolutiën SG 1621 volume is exactly this check and is **unreachable** this session (item 1). Unreachable.

## Remaining gaps
- [ ] edition: Resolutiën SG nieuwe reeks 5 (1621-1622), entries for Brederode's letters of 8 and 13 Aug 1621 read around 20 Aug 1621;
  waiting-on: resources.huygens.knaw.nl recovery (503 on 15 Oct 2026); next: one retry of the statengeneraal search
  (`search_term=Brederode`, source 5, plus `Heydelberg`), ~$0.5
- [ ] transcription control: scan 375's block (second witness) against ciphertext.tsv; next: native crop + one reader + reconcile, ~$1.5
- [ ] spec and first breadth test: held until the edition step clears the gate (brief JOB HEID-1621C step 3)

## Escalation
- Siblings: the letter of 8 Aug 1621 and its duplicate (named on scan 376) not yet located in inv. 6021 -- [ ] stride-1 screen, ~$1.5
- Known keys: none for Brederode's 1621 agency in KEY-OFFICES.tsv as far as checked (not searched by tool this job)
- Verdict: parked until the Huygens host answers; then keep going.

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

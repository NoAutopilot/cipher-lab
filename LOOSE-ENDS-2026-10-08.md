# Loose ends, 8 Oct 2026 (LOOSE-ENDS, account 2, for the account-3 orchestrator)

Why: na-oldenbarnevelt-2442-1605 NOTES.md section 1 noted on 25 Sept that leaves 4, 5 and 7 carry cipher of a different letter. The note was in a body section, so no step register carried it and the owner had to spot it on 8 Oct. `tools/loose_ends.py` now finds such notes, and this file is its first whole-repository run plus a triage. Nothing was decoded, and nothing was queued: the orchestrator queues.

## Numbers
- `python3 tools/loose_ends.py` (04:16 UTC): 1,234 hits in 267 folders. 590 had no register carrying them (tracked = no), 119 of them image-untranscribed rows (one row per folder).
- 420 of the untracked hits sit on open, partial, blocked or offline-only folders. Found-solved, solved and closed-negative folders were left out of the triage.
- 12 Sonnet triage batches of 29-38 hits each, plus my own reconciliation, gave 422 verdicts: **46 unlock, 112 done-later, 264 noise.** Two input rows had lost their id in batching, and the batches labelled them H311b and H339b. All verdicts are in `research/loose-ends-triage-2026-10-08.tsv`.
- The 2442 sentence itself was already carried before this run: the 03:54 ROOM line queued OLD-SIBS for leaves 4, 5 and 7 and scans 9-11, so the tool marks it tracked.
- No unlock is strong. The best p_counted is 0.20 (colbert26 sibling leaves, key partly in hand). Most are 0.01-0.04 cheap looks at unfetched sources. The orchestrator should read this as a sweep that found little hidden value: most body-text 'not fetched' or 'never read' notes were noise, or were done later in the same file.

## Top 20 (runnable now, ranked by expected counted documents per dollar = p_counted / cost; cost floored at $0.3)
p_counted is a Sonnet triage estimate of P(a new counted document: N3+, D2+, two audits, per the 8 Oct depth bar). It is a ranking aid, not a measurement. Each line is now in that folder's NOTES.md as a gap ('blocker: not-attempted; noted in the body at <file:line>') and as an Escalation item '[ ] <step>; ~$<cost>; source: loose-ends 8 Oct'. tools/gaps_check.py passes on all 18 folders.

| # | folder | rung | step | ~$ | p | per $ |
|---|---|---|---|---|---|---|
| 1 | fr2933-salviati-1525 (NOTES.md:3400) | print | fetch the CSP Spain vol. 2 text (archive.org djvu or a Wayback copy of the BHO page) and grep Salviati/Toledo 16 Oct 1525 for a paraphrase or clear context of the despatch | 0.3 | 0.02 | 0.067 |
| 2 | lambeth-bacon-649 (NOTES.md:97) | print | fetch the QMRO thesis (CORE with CORE_API_KEY, or a Wayback copy) and grep for ff.490-495 and cipher/decipher | 0.5 | 0.03 | 0.060 |
| 3 | fr5160-letellier-1653 (NOTES.md:1187) | siblings | refetch canvas 45 (and any of 55/58/74 still missing) once each and look for cipher groups; add a cipher leaf to trial_1653 | 0.5 | 0.02 | 0.040 |
| 4 | debosnys-1883 (NOTES.md:44) | image-check | fetch the scan set once and compare with our six PNGs; a sharper copy goes into the TRANSCRIPTION.md pipeline, error measured against BENCHMARK-TX | 0.5 | 0.02 | 0.040 |
| 5 | sp105-paget-1693 (NOTES.md:198) | siblings | walk the /records/PP_MS_4/02 sub-series titles on the SOAS catalogue and list any cipher-bearing Paget letters | 0.5 | 0.02 | 0.040 |
| 6 | nevers-birago-fr3251-1572 (NOTES.md:2153) | retry | run the three disk-only re-tests with the atlas/topk files beside a shuffled-text decode of the same length, sign count and mix | 1.0 | 0.04 | 0.040 |
| 7 | colbert26-lathuillerie-1644 (NOTES.md:54) | siblings | apply the f.23/f.24 key and sibling gloss values to one glossed sibling leaf (canvas 51, or 30/32) at word grain, two blind passes, beside a shuffled-key and a synthetic code+mark control at the leaf's N | 6.0 | 0.20 | 0.033 |
| 8 | colbert26-lathuillerie-1644 (NOTES.md:140) | image-check | retry canvases 11 and 29 once each and note whether either carries cipher | 0.3 | 0.01 | 0.033 |
| 9 | fr4715-vieuville-pool (NOTES.md:224) | siblings | fetch the f.67v canvas once and look for a continuation or cipher | 0.3 | 0.01 | 0.033 |
| 10 | scorpion-1991 (NOTES.md:154) | image-check | fetch the eight images once and look for an uncrossed S5 row (S5 is 180 signs, below unicity alone) | 0.3 | 0.01 | 0.033 |
| 11 | decode-4450-bnf-fr20506-1525 (NOTES.md:554) | siblings | open the 15 records and compare their systems with Ranzo's letter+number code; a key transfer later needs a shuffled-key control of the same length | 1.0 | 0.03 | 0.030 |
| 12 | decode-2754-bnf-baluze156-1636 (NOTES.md:207) | known-keys | fetch the f.40 key images and apply them to the 137 tokens of f.157r beside a shuffled-key null of the same length and symbol count | 1.5 | 0.04 | 0.027 |
| 13 | wvo-hessen-1564 (NOTES.md:571) | siblings | fetch the 14 PDFs once and scan them for cipher spans (siblings of f.23 only) | 0.5 | 0.01 | 0.020 |
| 14 | fr3613-sega-caetani-1591 (NOTES.md:45) | print | read the chapter's footnotes through OpenEdition or a Google Books snippet (country=US) for an edition of the Sega 1591 letters | 1.0 | 0.02 | 0.020 |
| 15 | mccormick-1999 (NOTES.md:273) | print | fetch a Wayback copy of the comment pages and grep them for a claimed reading or new material | 0.5 | 0.01 | 0.020 |
| 16 | oldenbarnevelt-brederode-1605 (NOTES.md:819) | known-keys | read the key slip and the decipherment pairs on scans 31/32 with two blind passes and build the syllabary table, beside a synthetic marked-number syllabary control of equal N and K; then test whether it fits no. 92 | 4.0 | 0.08 | 0.020 |
| 17 | siena-concistoro-2308 (NOTES.md:1007) | image-check | one DECODE browser login, fetch the record image for no. 11 and label it blind | 0.5 | 0.01 | 0.020 |
| 18 | armstrong-madison-1808 (NOTES.md:2015) | siblings | search another LOC or NYPL surrogate and the reel index for the 1806 item | 1.5 | 0.02 | 0.013 |
| 19 | fr5160-letellier-1653 (AUDIT.md:301) | clear-pages | commit the f.68 clear transcription with a second blind pass, align it, and test key1659 rows on the f.68 cipher beside a shuffled-order alignment control of the same length and symbol count | 3.0 | 0.04 | 0.013 |
| 20 | antt-linhares-chave (NOTES.md:1496) | siblings | DigitArq thumbnail montage of /02 and /09 (stride 1), eye-checked for numeral groups, with maco 86 /11 (a known cipher leaf) as the positive control at the thumbnail scale | 3.0 | 0.03 | 0.010 |

Sum of p over the 20: 0.67 expected counted documents, for about $26.7 of steps. The colbert26 sibling leaf (#7) is the only line with p >= 0.1.

## Unlocks held back (an outside blocker, a duplicate, or already carried)
- H016 armstrong-madison-1808: Reading-room request or visit for Box 37 (REQUEST.md); then test family E against the table; blocker waiting-on ASKS 77; p 0.03, ~$0.3. Key for a different office code; only helps if Armstrong used the same family
- H256 fr5160-letellier-1653: refetch canvas 45 native, one retry, classify cipher or clear; blocker none; p 0.02, ~$0.3. duplicate of H252; also 55 folio 31 recovered
- H272 guazzo-nevers-fr4688-1571-72: Add folios to next BnF reproduction quote batch (REQUEST.md) for owner to order; then read leaves; blocker needs-person; p 0.02, ~$0.3. Owner order needed; NOTES.md:161 carries next step but not in register; key search found nothing digitised.
- H337 nevers-birago-fr3251-1572: owner sorts the sortnext.tsv tiles then re-decode f.144r; blocker needs-person; p 0.03, ~$0.5. Depends on owner sign-sorter pass; cryptanalytic result only so far.
- H323 monck-1660: browser login once, search Monck/32093 in DECODE; blocker needs-physical-access; p 0.02, ~$0.5. DECODE login works since 24 Sept; BL images offline; no ciphertext yet
- H327 moustier-altars: site visit or local contact photo; blocker needs-physical-access; p 0.01, ~$0.3. no online image better; no decipherment to test
- H280 intercepted-royalist-1646: Re-probe DECODE 8725 attachments (one browser login) and BL viewer for f.104 image; if image, check Digby key 129 fit; blocker waiting-on BL viewer / DECODE gate; p 0.03, ~$1.0. Status conflict unresolved since 20 Sept; BL images offline since 2023; DECODE image gate varies per record.
- H124 fr15575-syllabic-1592-95: fetch canvas 8 and neighbours at native size, identify f.2r, check cipher type; blocker no-key-material; p 0.01, ~$0.5. No syllabic-1592 key on disk; figure cipher; Tomokiyo has only related leaves
- H324 monck-1660: fetch collection page, look for Hyde key sheets; blocker needs-physical-access; p 0.01, ~$0.5. key lead exists (Barwick); letter image unavailable
- H374 sanguszkow-mniszech-dunin-1714: enquiry to Biblioteka Kornicka for microfilm scans, then compare numerals against R7524 key family; blocker needs-physical-access; p 0.02, ~$1.0. Different correspondence; only possibly the same key family
- H228 fr4712-nevers-duchesse: Apply owner's same-writer judgement to 6 carries, re-run decode_key --check; blocker none; p 0.02, ~$1.5. Only 37 tokens; cannot reach D2 alone, key no.1 non-test
- H373 salvago-caraffa-1691: ASGe copy enquiry per REQUEST.md, or SLSP article-level search; blocker needs-person; p 0.02, ~$1.5. Owner-side enquiry; finding aid read, no digitisation exists
- H316 matignon-mayenne-1586: build Cipher-3 table from period decipherments f.189/190, then two blind passes on f179 crops; blocker none; p 0.05, ~$4.0. native overlay-free image on disk; not-attempted per Remaining gaps
- H088 decode-2754-bnf-baluze156-1636: thumbnail scans of both with contact-sheet triage for sibling cipher pages (about 3 USD per NOTES); blocker none; p 0.03, ~$3.0. Sibling search only; needs a key for any reading.
- H212 fr3987-nevers-revol-1593: After ASKS 102 sort, re-read L07-L21 crops against settled Revol-hand list, two blind passes, decode, judge; blocker waiting-on ASKS 102; p 0.08, ~$8.0. Largest unread block; no Escalation section in this folder; only gap is shared sorter
- H217 fr3989-nevers-revol-1594: After Revol-hand atlas exists run pass A, reconcile, decode; Tomokiyo 'de la diuision' crib; blocker waiting-on ASKS 102; p 0.03, ~$3.0. Short stretches inside clear French, hand atlas needed first
- H315 matignon-mayenne-1586: locate canvas with gallica_folio.py, crop lines, two blind passes, tools/key crib via Tomokiyo opening; blocker no-key-material; p 0.03, ~$3.0. Cipher-3 table henryiii_Matignon3.png not on disk; short leaf
- H355 rah-juan-manuel-1521: fetch R9515 full-size images; transcribe and decode with Tomokiyo nomenclator, pool with siblings; blocker waiting-on ASKS 138; p 0.02, ~$2.0. Two pages only; transcription standard unmet pending owner sort; poolable with 27 other letters.
- H202 fr3985-nevers-revol-1593: After owner sort (ASKS 102) cut f.88 line crops, two blind passes vs settled Revol-hand list, decode with key60; blocker waiting-on ASKS 102; p 0.05, ~$6.0. Key in hand; Revol-hand sign identification is the blocker; f.88 not a folder
- H205 fr3985-nevers-revol-1593: Same as H202: cut lines, blind passes after ASKS 102 sort; blocker waiting-on ASKS 102; p 0.05, ~$6.0. Duplicate of H202; f176 image already transcribed
- H093 destaing-gerard-1779: collate A/B/C number by number against Bourdeau transcription, then Holker key lead; blocker needs-person; p 0.03, ~$4.0. Needs private repo scope; key not in hand.
- H092 della-torre-olanda-1690: owner copy enquiry (REQUEST.md) or Nationaal Archief search for same envoy; blocker needs-person; p 0.01, ~$1.5. Unknown whether enciphered; no edition; blocked target.
- H034 bl-farnese-cipher: Read Lasry paper Fig 5 key; order BL copy of 8716 art.4 cipher leaves; blocker needs-physical-access; p 0.02, ~$5.0. Not digitised; published key exists but no image of our letters
- H039 blitz-ciphers: build glyph inventory in sign sorter then transcribe page 1-2 with two blind passes on iiif_lines crops; blocker no-key-material; p 0.02, ~$6.0. Unsolved invented script; no key, no language known; transcription cost high.
- H065 clairambault528-bouillon-1713: order BnF reproduction via REQUEST.md; if imaged, transcribe and test against 1713 Clairambault sibling keys; blocker needs-person; p 0.02, ~$40.0. Undigitised, lowest-confidence item; may be short annotation; no key on disk.
- H223 fr3993-villeroy-1595: Order BnF reproduction of one leaf (ASKS 111), then pool signs with fr3993; blocker needs-person; p 0.02, ~$60.0. Backlog ask 111, owner quote; may pool with fr3993 signs

Corrections in the reconciliation unit:
- H316 (matignon f.179) was dropped: its own Remaining gaps already carries it. The image check missed this because the register names the file as f179_gallica_native.jpg, not by its leaf number.
- H228 (fr4712 f.10r) was moved to held back: it depends on the owner's same-writer judgement (ASKS 113).
- H205 and H256 were dropped as duplicates of H202 and H252.

## Tool limits (for the next run)
- The tracked heuristic matches material keys (numbers and rare words). A register line that names the material differently is missed, which is why 112 hits came back done-later.
- A register line that cites the hit's own file:line always counts as tracked (added 8 Oct).
- Image rows are grouped one per folder. Untranscribed images are mostly crops under other names, clear pages or print pages: no image row became an unlock in this run.
- next-in-body hits (235 in all) were almost always superseded by later sections.

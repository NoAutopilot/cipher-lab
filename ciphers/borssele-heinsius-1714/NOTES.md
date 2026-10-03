open
Veenendaal, *Briefwisseling van Anthonie Heinsius* Deel 15 (GS 227) pp.517, 531, 538 and Deel 16 (GS 240) p.60 read by this worker (GF4-BATCH15, Huygens retroboeken OCR, 3 Oct 2026), plus full-text search "onopgelost cijfer" (all 19 volumes, 3 hits), "oplossing" (Deel 15, 2; Deel 16, 2), "cijfer" (Deel 15, 11; Deel 16, 15), "gezondheid van de koningin" (Deel 15, 4): the cipher on letter 959's leaf is not printed and no decipherment of it is printed; the only solution named, an undated "uit het cijfer opgelost" piece on the queen's health, is listed under letter 936 (27 March 1714, p.517 n.1), so its match to the 3 April cipher remains the editor's "mogelijk".

# Ph.J. van Borssele van der Hooghe to Anthonie Heinsius, unsolved cipher on the same leaf as letter 959, 3 April 1714

QUEUE row: HU5 (`QUEUE.md`, "Huygens and Nationaal Archief correspondence editions: letters noted in cipher
(LANE N harvest of 24 September 2026)"). Brief `.claude/briefs/runs/2026-09-24-lane-n-csHU.md`.

## Source

Anthonie Heinsius correspondence archive, Nationaal Archief 3.01.19 ("H.A." in the edition), inv.nr. 1836.
Printed in J.G. Smit / A.J. Veenendaal (ed.), *Briefwisseling van Anthonie Heinsius 1702-1720*, Deel 15
(GS227), p.531, letter no. 959, via the Huygens `retroboeken/heinsius` viewer (no login,
`resources.huygens.knaw.nl`).

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents), resolving the ambiguity flagged as caveat
2 in `sources/huygens/NOTES.md` ("HU5 and HU6 are explicitly ambiguous between already solved and a real
recovery lead -- the next worker on either must read the actual leaf/index before nominating further").

1. **Editions first -- the primary edition's own footnote, re-fetched and read directly this pass**
   (`images/heinsius_15_GS227_531.jpg`, page text also read as OCR): letter 959 itself, from Ph.J. van
   Borssele van der Hooghe in London, 3 April 1714, is printed in clear Dutch (a report on English opinion
   about the peace in the North). The editor's footnote to letter 959, quoted here verbatim (not paraphrased):
   > "959 Op hetzelfde blad is bijgeschreven een brief in onopgelost cijfer; verder is nog aanwezig een
   > oplossing van een gecijferde brief, voornamelijk over de gezondheid van de koningin, **mogelijk dezelfde
   > als de genoemde gecijferde brief**. Kopie van Van Borssele's brief aan de Staten-Generaal eveneens
   > aanwezig."
   Translation: "On the same leaf is added a letter in unsolved cipher; furthermore there is also present a
   solution of an enciphered letter, mainly about the health of the queen, **possibly the same as the
   mentioned enciphered letter**. A copy of Van Borssele's letter to the States-General is also present."
   **This resolves the ambiguity only partly, in the editor's own words, not this worker's inference**:
   Veenendaal himself states the "oplossing" *may* be of the very cipher letter on this leaf, but does not
   confirm it -- he uses "mogelijk" (possibly), not "namelijk" or "te weten". This is not a found-solved
   verdict: the edition's own editor stops short of stating this letter is solved, only that a solution of
   *something* is physically present nearby and could be the same item. Resolving it further requires seeing
   the actual leaf (H.A. 1836), which neither this pass nor the harvest pass has done.
2. **Post-edition literature search.** `WebSearch "van Borssele van der Hooghe" Heinsius 1714 cipher` found
   only genealogical and archival-inventory pages about the Van Borssele van der Hooghe family (a different,
   earlier member, Adriaan van Borssele van der Hooghe, Council of State 1692-1718, correspondent of Heinsius
   from Brussels/the army, not London) -- no hit naming this specific letter, its cipher, or a decipherment.
3. **Community lists.** `sources/cryptiana/web/dutch.htm` (read via `tools/html2text.py`): no mention of
   Borssele, van der Hooghe, or this letter.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for "borssele"/"hooghe"/
   "heinsius": zero hits.
5. **Solver repositories.** Fresh shallow clones this pass (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-
   ciphers|`), grepped for "borssele", "hooghe", "heinsius", "1836": no hit.

## Verdict

**Status: open**, but with the strongest caveat of this batch: the printed edition's own editor flags that a
decipherment physically present in the same dossier *may* be of this exact cipher letter. This is not scored
found-solved because the editor himself does not confirm it (rule 10 -- report what was found, do not
over-claim); it is scored open, not blocked, because the edition was located and read directly and gives a
definite (if incomplete) answer. **The very next step on this target, before any solver work, must be to view
the actual leaf (H.A. 1836) at the Nationaal Archief and check whether the "oplossing" text matches the
ciphertext of the "brief in onopgelost cijfer" on the same page** -- if it does, this is found-solved and
should be relabelled; if the two ciphers are visibly different (different hand, different system, unrelated
subject beyond "queen's health"), this remains open and becomes a genuine sibling-recovery case like WVO's NB1
pattern.

**Copy status: NOT copy-free, corrected 24 Sept 2026 (LANE N2 worker csHU2).** The "likely copy-free" claim
above rested only on the generic "Scan"/"Viewer" page-shell text, which is identical across every invnr
regardless of digitisation. The real per-item record (`nationaalarchief.nl/onderzoeken/archief/3.01.19/
invnr/1836`'s embedded `drupal-settings-json` -> `viewer.response`, not the page shell) gives
`"availability":"PHYSICAL","scans":[]` -- **not digitised**, confirmed against a positive control (NA 1.04.02
invnr 1, `"availability":"DIGITALIZED"` with real IIIF URLs, proving the accessor correctly reports a scan
when one exists). This means the leaf check called for above (comparing the "oplossing" text to the cipher
letter) cannot be done online; it requires an archive visit or copy order. `REQUEST.md` written this pass.

**Kind: recovery (ambiguous)**, pending the leaf check above -- either a found-solved correction, or a
sibling-decipherment recovery case if the "oplossing" resolves to a different item.

Search log (rule 10): reported above, per source. Not classified for novelty. Requests this pass:
`resources.huygens.knaw.nl` ~4 (1 pages.json, 1 html_url OCR fetch, 1 image fetch, book_data.js reused from the
HU4 step of this same pass), `www.nationaalarchief.nl` 1 (invnr 1836, in the same batch as HU4's three), `
github.com` 0 (reused the HU4 clones already on disk this session). WebSearch 1. No subagents.

## While waiting (27 Sept 2026, WAIT-PASS-A)

Waits on a copy order or archive visit to view NA 3.01.19 invnr. 1836 (H.A. 1836) and compare the "oplossing"
to the "onopgelost cijfer" on the same leaf, since 24-25 Sept 2026 (REQUEST.md, consolidated Heinsius-circle
request).

- Re-read Veenendaal's edition (already on disk) for another footnote cross-referencing this "oplossing" by letter number, no leaf needed. S.
- Compare this target's cipher design against the key.tsv/decode.json already recovered for sibling Heinsius-circle folders (e.g. heinsius-hermitage-1704, heinsius-dopff-1702) for a design match. M.
- Search Google Books/HathiTrust again for "van Borssele van der Hooghe" + "cijfer"/"chiffre" 1714, beyond the one WebSearch already run. S.

## Web and blog check (GF4-BATCH15, account-4, 3 Oct 2026)
Plain web searches: `"Borssele van der Hooghe" Heinsius 1714 cijfer OR cipher OR chiffre` (hits: NA 3.01.19 inventory pages and PDF; Leiden scholarly-publications items; **de Leeuw, "The Black Chamber in the Dutch Republic during the War of the Spanish Succession"**, pure.uva.nl -- opened, and the whole thesis it belongs to, K. de Leeuw, *Cryptology and statecraft in the Dutch Republic* (UvA 2000, pure.uva.nl/ws/files/3074957/12760_Thesis.pdf), fetched and grepped: "Borssele" occurs only as Adriaan's *Gedenkschriften* in citations; no mention of Philips Jacob, H.A. 1836, or any cipher letter of his; KZGW catalogues; Wikipedia); `"3.01.19" 1836 Heinsius cijferschrift` (NA inventory pages only; inv. 2315-2317 cipher subsection, already in Source); `"onopgelost cijferschrift" Heinsius` (NA inventory pages, unrelated genealogy sites); `"Sleutel van een cijferschrift, waarschijnlijk voor correspondentie met Engeland"` (NA inventory, UvA cryptography syllabi with no Heinsius item). Model-solve check: nothing naming this letter.
Blog site searches: Cipherbrain `Heinsius cipher OR Geheimschrift OR "Hermitage" site:scienceblogs.de` -- 0 relevant; Cryptiana (blog and Tomokiyo's fc2 pages) + Cipher Mysteries `Heinsius Dutch cipher 1704 OR 1714 site:cryptiana.blogspot.com OR site:ciphermysteries.com OR site:cryptiana.web.fc2.com` -- 0 relevant. No hit to open, no comment thread to read. Result: no public decipherment of the 3 April 1714 cipher found. Requests: resources.huygens.knaw.nl 13 (shared with heinsius-hermitage-1704), pure.uva.nl 2 + dare.uva.nl 1, github.com 2 clones; all >=1.5 s apart.

## Premise check (GF4-BATCH15, account-4, 3 Oct 2026)
(a) Folder's own mentions -- found, not viewable: the edition's "oplossing van een gecijferde brief, voornamelijk over de gezondheid van de koningin" (p.531 n.959). This pass located where the edition files it: letter 936 (Borssele, 27 March 1714, p.517) n.1, "Kopieën van Van Borssele's brieven aan de griffier en aan de Staten-Generaal, alsmede een uit het cijfer opgelost ongedateerd stuk over de gezondheid van de koningin, aanwezig in H.A. 1836." It is undated and its ciphertext is not identified, so it may decipher 959's cipher or a 27 March one; only the leaf decides. H.A. 1836 is PHYSICAL, no scans (24 Sept check, unchanged).
(b) Other solvers' working files -- not found: fresh depth-1 clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers grepped for borssele/hooghe/hermitage/sauniere/heinsius: only unrelated substrings (Dutch "Hoogheid", English "hermitage").
(c) Physical neighbours -- found in print, three siblings in the same dossier H.A. 1836: letter 970 (6 April 1714, p.538 n.1) "Op hetzelfde blad is bijgeschreven een briefje in cijfer, dat op een apart blaadje is opgelost: de verwijdering tussen Oxford en Bolingbroke neemt toe..." -- a same-correspondent cipher with a period decipherment slip, i.e. a key source for this letter's system if the leaves are imaged; Deel 16 letter 104 (8 June 1714, p.60 n.1) "een in het cijfer gestelde, ongedateerde en onopgeloste brief" -- a second unsolved Borssele cipher; and the 936 solution above. None is printed in cipher or in clear beyond the editor's one-line gist.
(d) Recipient/other side -- not found, not reached: Borssele's parallel letters to the griffier/States-General (copies in H.A. 1836; originals presumably NA 1.01.02 Staten-Generaal liassen Engeland) were not searched; de Leeuw's thesis (the published study of Heinsius's cipher office) does not discuss this correspondent.

## While waiting (GF4-BATCH15, account-4, 3 Oct 2026)

- Add letters 936 (27 Mar 1714), 970 (6 Apr 1714, cipher + decipherment slip) and Deel 16 no.104 (8 Jun 1714, unsolved cipher) to REQUEST.md beside 959, all in H.A. 1836, so one copy order brings the cipher, its candidate solution and a solved sibling together (text edit only, depends on nobody).
- Sweep Deel 15-16 for every other Borssele letter footnoted "cijfer" (Deel 16 p.317 "het officiële cijfer voor de geheime correspondentie" not yet read) via the same retroboeken full-text route. S.

Gate re-run (GF4-BATCH15, 3 Oct 2026): status `open` unchanged (no printed decipherment of this item; the possible one is unconfirmed and on an undigitised leaf).
```
$ python3 tools/intake_gate_check.py borssele-heinsius-1714
borssele-heinsius-1714: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0 (was 1: no standard-edition citation within 6 lines)
$ python3 tools/next_steps.py --wait-only | grep borssele-heinsius-1714
(no line)
```

## FT4-borssele-heinsius-1714 (3 Oct 2026, account-4)

Step (from GF4-BATCH15 premise (c), c912005e): locate the same-dossier sibling letter 970 (6 Apr 1714, cipher plus a
period decipherment slip) and Deel 16 no.104 in H.A. 1836 online, and if imaged, pair and align them.

- Result: **not digitised.** `https://www.nationaalarchief.nl/onderzoeken/archief/3.01.19/invnr/1836`, embedded
  `drupal-settings-json` -> `viewer.response`, read 3 Oct 2026 03:5x UTC: `"unittitle":"Borssele van der Hooghe, Philips
  Jacob van-, heer van Voorhout-, uit Londen."`, `"scans":[]`, `"has_scan_navigation":false`, `"availability":"PHYSICAL"`.
  Positive control the same minute, same accessor: NA 1.04.02 invnr 1 -> `"availability":"DIGITALIZED"`. Letters 936,
  959, 970 and Deel 16 no.104 all sit in this one inventory number (the edition's own footnotes), so none of the four
  leaves can be read online; steps (2) onward (vision, transcription, interlinear_align, pairing-shuffle control, key
  test on 959) were not run. No vision call, no reading, nothing graded.
- REQUEST.md item 1 extended to letters 936, 970 and Deel 16 no.104 (one order, about 6-8 leaves).
- Requests: www.nationaalarchief.nl 2 (>=1.5 s apart). No other host.

## Remaining gaps (FT4-borssele-heinsius-1714, 3 Oct 2026)
Read so far: 0 of the cipher letter's tokens (no image or transcription of the leaf exists online)
- 959 cipher on the leaf, and its candidate "oplossing" (filed under 936) - blocker: needs-physical-access; NA 3.01.19 invnr 1836 is PHYSICAL, scans [] (re-checked 3 Oct 2026 with a DIGITALIZED positive control); REQUEST.md item 1
- 970 cipher + decipherment slip (period key source) - blocker: needs-physical-access; same inventory number, same check
- Deel 16 no.104 unsolved cipher - blocker: needs-physical-access; same inventory number, same check

## Escalation (3 Oct 2026)
- [x] siblings: 970 (with slip), 936 (candidate solution), Deel 16 no.104 located in print (GF4-BATCH15); none imaged online (this step)
- [n/a] clear-pages: letter 959's clear text is printed but carries no crib for the cipher
- [n/a] known-keys: no Borssele key printed or imaged; inv. 2315-2317 cipher keys also physical only
- [x] print: Veenendaal Deel 15-16 read (GF4-BATCH15); cipher and solution not printed
- [n/a] key-rebuild: no ciphertext available to rebuild from
- [x] image-check: NA per-item record re-read 3 Oct 2026, PHYSICAL
- [n/a] retry: nothing online left to retry until the archive digitises the dossier
Verdict: parked: every gap has an outside blocker (needs-physical-access, REQUEST.md item 1: copy order or visit for NA 3.01.19 inv. 1836, letters 936/959/970 and Deel 16 no.104)

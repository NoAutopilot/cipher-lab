open

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

**Copy status: likely copy-free, not confirmed per item this pass.** `www.nationaalarchief.nl/onderzoeken/
archief/3.01.19/invnr/1836` returns HTTP 200 with the same generic "Scan"/"Viewer" page-shell text seen on
every other invnr tested this pass (756, 1975, 2030, 2044) -- not a reliable per-item confirmation (see HU4's
NOTES.md for the same finding in more detail). No REQUEST.md written.

**Kind: recovery (ambiguous)**, pending the leaf check above -- either a found-solved correction, or a
sibling-decipherment recovery case if the "oplossing" resolves to a different item.

Search log (rule 10): reported above, per source. Not classified for novelty. Requests this pass:
`resources.huygens.knaw.nl` ~4 (1 pages.json, 1 html_url OCR fetch, 1 image fetch, book_data.js reused from the
HU4 step of this same pass), `www.nationaalarchief.nl` 1 (invnr 1836, in the same batch as HU4's three), `
github.com` 0 (reused the HU4 clones already on disk this session). WebSearch 1. No subagents.

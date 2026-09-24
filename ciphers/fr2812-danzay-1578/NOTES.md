found-solved

# Danzay to Henri III, 28 February 1578 -- BnF Français 2812

QUEUE row: M31 (sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv, "Fourth pass, 24 September 2026").

## Source

BnF, Département des Manuscrits, **Français 2812** ("Recueil de lettres et de pièces originales", ancien
8394(5)), archivesetmanuscrits ark `cc49264b`. QUEUE catalogue note: "Letter from 'DANZAY' to the king, with
cipher and decipherment both present," last day of Feb. 1578. Sender: **Charles de Danzay**, French resident/
ambassador to Denmark 1548-1589 (the longest sixteenth-century tenure of any French diplomat, per Daussy 2004).

## Check-solved sweep (24 September 2026)

1. **Web search.** `"Arsenal" "6314"...` -- not run for this row; two queries specific to this item
   (`"fr.2812" OR "Français 2812" Danzay chiffre déchiffrement`) returned only the archivesetmanuscrits
   catalogue record itself (ark cc49264b) and unrelated cipher-tool noise (dcode.fr, Great Cipher, Vigenère) --
   no solver claim surfaced independently of Cryptiana (item 4 below).
2. **Printed correspondence.** Danzay's letters are compiled in *Correspondance de Charles Dantzai, ministre de
   France à la Cour de Danemarck* (1824, from Swedish archives) and C.F. Bricka (ed.), *Indberetninger fra
   Charles de Dançay...1567-1573* (1901, from Danish archives) -- both named by Tomokiyo (danzay.htm, see
   below), who states he has **not seen** (images of) the original manuscripts these editions draw on. Neither
   edition fetched or read this pass; flagged unread, not a search result against this specific letter.
3. **Calendars/state-paper series.** None identified for this French Recueil; not applicable beyond item 2.
4. **Cryptiana / Cipherbrain.** Direct hit, already in the local snapshot (`sources/cryptiana/web/danzay.htm`,
   "Danzay's Ciphers: Ciphers of a French Diplomat with a Long Tenure", first posted 22 Feb 2026). Quoted
   verbatim: *"A French diplomatic cipher used by Charles de Danzay was recently reconstructed by Sergey
   Ryabov... Danzay's Cipher (1574-1578)... The letter from 1574 is from Danzay to Henry III, dated 14 October
   1574 (BnF fr.4736..., f.87)... The other is from Danzay to Henry III, dated 28 February 1578 (BnF fr.2812,
   f.45). Ryabov succeeded in reconstructing the cipher from the decipherment in the margins and thereby
   deciphering the yet unsolved cipher paragraph in the former letter."* This is an exact shelfmark and date
   match for M31 (28 Feb 1578 = "last day of Feb. 1578"). It establishes that **fr.2812 f.45 already carries a
   contemporary marginal decipherment** -- matching QUEUE's own "cipher and decipherment both present" note --
   and that the cipher system used in it was independently reconstructed and published: Sergey Ryabov (2025),
   "Secrets of the Foreign Policy of the Last Valois in Northern Europe," *Quaestio Rossica* 13(4),
   DOI 10.15826/qr.2025.4.1034, written up by S. Tomokiyo (danzay.htm, posted/modified 22 Feb 2026). No
   Cipherbrain (klausis-krypto-kolumne / cipherbrain.de) page found for Danzay; not swept independently this
   pass beyond the general web search in item 1.
5. **DECODE.** Cached catalogue (`unsolved-ciphers/catalogue/decode-catalog.csv`, a fresh shallow clone of
   aaymeloglu/unsolved-ciphers, 1360 Decrypted + non-decrypted rows -- broader than this repo's own
   non-decrypted-only cache) grepped for "2812" and "Danzay": no hit. Ryabov/Tomokiyo's reconstruction is not
   itself catalogued on DECODE under this ark.
6. **Solver repositories.** Fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`
   grepped for "2812", "Danzay", "Dantzai": no hit in either repository's curated files (CATALOGUE.md,
   TARGETS.md, SOLVED_CATALOGUE.md, SHORTLIST.md) or any target folder. Neither solver repository has this item.

Requests: WebSearch 2 queries (this row + the general M31 confirmation). cryptiana.web.fc2.com 0 (danzay.htm
was already in the local `sources/cryptiana/web/` snapshot, no live fetch needed). github.com 2 shallow clones
(shared across all six LANE G2 CS1 rows this worker covers; grepped, kept in scratchpad, not committed).
archive.org 0 for this row.

## Verdict

**found-solved.** The manuscript's own contemporary marginal decipherment (per Tomokiyo's description of
fr.2812 f.45) means this item needed no cryptanalysis in the first place, and the cipher system it uses has
since been independently reconstructed and published (Ryabov 2025; Tomokiyo 2026) from this very letter and
its 1574 sibling (fr.4736). Not a candidate for this project's solver pipeline. Per rule 10, this NOTES.md
states only that a decipherment and a published reconstruction exist and where -- it does not assign an
N-class; that is a verifier's job from AUDIT.md, and is not needed here since the item is not going forward as
a target (result: **found-solved catch**, not a project reading).

For the orchestrator: drop this row from the board/queue pipeline as found-solved (a genuine catch, same shape
as the M9/Gustav-Adolf catches logged in LESSONS.md and QUEUE.md's Fourth-pass exclusions). No nomination.

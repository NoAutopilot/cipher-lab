open

# Raby (1705) and Whitworth (1716-19), Northern-Europe diplomatic ciphers — TNA SP 90/3/358, SP 90/7/149,212, SP 90/8/84

QUEUE row: N27 (`QUEUE.md`, "Candidates not on DECODE"). Extends N13's SP 90/2 (1704) run forward one piece;
see `ciphers/sp90-raby-1704/NOTES.md` (open, stage 2 conditional) and `ciphers/whitworth-1707/NOTES.md`
(open, narrowed to one passage) — read first, per brief, to avoid duplicating either.

## Source

TNA, State Papers Foreign, Prussia and German States. Catalogue text as quoted in QUEUE.md's N27 row:

> **SP 90/3/358** (1705): Raby to Harley, on Frederick I's secret Sweden treaty — same correspondent as
> N13's SP 90/2 cluster (Apr-June 1704), one piece later.
> **SP 90/7/149, 212** (1716-17): Whitworth to Townshend/Stanhope.
> **SP 90/8/84** (1719): Whitworth to Stanhope, translation of f.80 ("itself noted 'partly in cipher'").

Two different correspondents and two different edition questions:

## Raby, SP 90/3/358 (1705)

`ciphers/sp90-raby-1704/NOTES.md` already established that James J. Cartwright (ed.), *The Wentworth Papers,
1705-1739* (1883), is the standard printed edition of Raby's Berlin correspondence, and that it covers
**1705 onward** — i.e. this item, unlike the 1704 cluster, falls inside its stated coverage. Fetched the
archive.org djvu text (`wentworthpapers100strauoft`, 1 request, 1.4 MB) and confirmed a dedicated section
"RABY, AT BERLIN (1705-1708)" beginning with letters dated February 1705. Grepped for "Sweden", "secret
treaty" and "Frederick" throughout: no passage in the fetched text matches "Frederick I's secret Sweden
treaty" specifically (the hits found are unrelated — Frederick's Queen Sophie Dorothee, an index entry for
"Frederick I., King of Prussia", a Torcy cipher-letter mention in a different context). **This is not a safe
negative**: Cartwright's book is an editorial *selection* of Raby's letters (explicitly, per its own preface
style — it prints representative correspondence, not the full despatch run), so a specific folio's content
being absent from the grepped OCR text does not establish it is unpublished, only that the specific published
excerpts this sweep read do not obviously match this item's described content. The exact date of SP 90/3/358
within 1705 is not given in the QUEUE row; without it, checking the book page-by-page for this precise letter
was not completed this sweep.

## Whitworth, SP 90/7/149,212 and SP 90/8/84 (1716-1719)

Different correspondent, different period from `ciphers/whitworth-1707/`'s SP 91/5 Moscow despatches to
Harley/Boyle (1707-08, printed in *Sbornik Imperatorskago Russkago Istoricheskago Obshchestva* vols. 39 and
50) — by 1716-1719 Whitworth had moved from the Russia posting to Berlin/Prussia, and his correspondents here
are Townshend and Stanhope, Secretaries of State after the 1714 change of ministry. The Sbornik series is a
Russian-court-correspondence project and would not cover this period.

Web search found that the British Library holds **Add MS 37373-37389**, described as Whitworth's own
Berlin correspondence and papers "1716, 1719-1722" (seventeen volumes), including letters from Frederick
William I of Prussia, Stanhope, Craggs and Townshend — i.e. a second, retained copy of exactly this
correspondence channel, at a different repository from the TNA originals. This is a **manuscript sibling
copy, not a printed edition** — worth flagging for a future access worker (a BL Add MS 37373-37389 copy could
carry a contemporary decipher, as the SP 91/5 pattern did for Whitworth's earlier posting), but it does not
resolve edition risk on its own; no printed edition of Whitworth's 1716-19 Berlin despatches was located by
web search this sweep.

## Check-solved sweep, 24 September 2026

1. **Print.** See above: Wentworth Papers (1705-1739) covers 1705 by date but not confirmed for this specific
   folio; no printed edition found for the 1716-19 Whitworth-Townshend/Stanhope correspondence, only a BL
   manuscript sibling (Add MS 37373-37389).
2. **Web search.** "Whitworth envoy Berlin Hague 1716 1717 1719 Townshend Stanhope despatches printed
   edition" and variants: surfaced the BL Add MS 37373-37389 holding above; no dedicated cipher-history
   discussion of either correspondence channel.
3. **Community lists.** `sources/cryptiana/` grepped for "Raby", "Whitworth", "SP 90": one hit,
   `web/blencowe2.htm` line 65 — "F.61 (R8762) is another copy without a title and instructions, but it has
   additional entries: 892 (Monsieur), 369 (Bernstorf), St. Jean (Bollingbroke), **Raby (Strafford)**." This
   is a *different* cipher key (a DECODE-catalogued English Deciphering Branch key, R8762) in which "Raby" is
   used as a **cipher code-name for Strafford** (Raby was created Earl of Strafford in 1711) — i.e. evidence
   that Tomokiyo's project has separately catalogued material naming Raby, but not a decipherment of SP
   90/3/358, SP 90/7, or SP 90/8; not the same document, flagged as a lead for a future worker rather than a
   solution. No dedicated Cryptiana/Cipherbrain page for this row's specific items.
4. **DECODE.** Cached catalogue grepped for "SP 90", "Raby", "Whitworth", "Townshend": no record (the R8762
   key above is in Cryptiana's own snapshot, not confirmed present in the cached DECODE CSV export used for
   this check).
5. **Bourdeau.** Fresh shallow clone grepped for "Raby", "Whitworth", "sp 90": no hit tied to this row (the
   repository's Visconti-1727 key material uses "Townshend" only as an unrelated cipher code-number entry in
   a different, Italian nomenclator).
6. **Aymeloglu.** Same clone pass: no hit for "Raby", "Whitworth", or "SP 90" anywhere in the repository.

## Verdict

**Open, stage 2 verified unsolved (conditional).** Not "new"; not "unpublished" (rule 10). Closed-negative on
DECODE, Bourdeau and Aymeloglu. Print check is incomplete on both fronts: SP 90/3/358 sits inside Wentworth
Papers' stated 1705-1739 coverage but was not matched to a specific page (the exact date within 1705 is
needed first); SP 90/7 and SP 90/8 (Whitworth, 1716-19) have no printed edition found, only a BL manuscript
sibling copy (Add MS 37373-37389) not yet checked for a contemporary decipher.

Requests: archive.org 2 (Wentworth Papers djvu, already-cached from the sibling folder's prior fetch pattern,
re-fetched this sweep), github.com (shared clone, see sp35-townshend-key-1719/NOTES.md). 2 WebSearch queries
this target.

## Next

1. Get the exact date of SP 90/3/358 (TNA item-details, out of scope for this LANE S batch's no-Discovery
   rule) and check it against Wentworth Papers page by page.
2. Check BL Add MS 37373-37389 (searcharchives.bl.uk catalogue record) for a contemporary decipher alongside
   the 1716-1719 Townshend/Stanhope letters — cheaper than a TNA copy order if the BL copy already carries
   one.
3. None of the four items is digitised on Discovery (per the QUEUE row); a TNA page-copy order is the
   fallback route if (1)-(2) do not resolve it.

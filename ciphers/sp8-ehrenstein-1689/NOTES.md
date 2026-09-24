open

# Major d'Ehrenstein to M. de Bernsdorff re M. de Guldenstolp, partly in cypher — TNA SP 8/6/65

QUEUE row: N61 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 8/6/65** (item 65, described in the record as folio 208), [1689] (TNA
Discovery, fetched 24 Sept 2026, id C18727349; `digitised: false` confirmed by direct record fetch; no separate
`note` field). Scope content: "Folio 208. Letter from Major d'Ehrenstein to Monsiuer de Bernsdorff regarding
Monsieur de Guldenstolp partly in cypher." SP 8 is **"King William's Chest"** — William III's own papers as
Prince of Orange and King, 1670-1698; TNA's own research guide states the series is "nearly all calendared" in
the printed CSP Domestic for Charles II, James II, and William and Mary. 1689 is the first year of William's
reign and the start of his continental resistance to Louis XIV (Nine Years' War), consistent with correspondence
about raising or coordinating German/Scandinavian military contacts. "Bernsdorff" and "Guldenstolp" plausibly
render Bernstorff (a prominent Hanoverian/Danish noble family) and Gyldenstolpe (a Swedish diplomatic family;
Nils Gyldenstolpe was Swedish envoy to the Hague through the 1680s-90s) — web-searched but not confirmed as the
specific individuals in this letter.

## Check-solved sweep (24 September 2026)

1. **Editions.** TNA's own guide (`nationalarchives.gov.uk`, State Papers Domestic 1660-1714 research guide,
   confirmed by WebSearch 24 Sept 2026) states SP 8 is nearly all calendared in *Calendar of State Papers
   Domestic, William and Mary*, ed. Hardy and Bateson, 11 vols (1895-1937). Vol. 1 (13 Feb 1689-Apr 1690, the
   window that contains this item) was fetched in full text from archive.org (`calendarofstatep02grea_1`) and
   grepped for "Ehrenstein," "Bernsdorff"/"Bernstorff," and "Guldenstolp"/"Gyldenstolpe": **zero hits** for all
   variants. TNA's phrasing is "nearly all," not "all," and period German/Scandinavian names are OCR-fragile, so
   this is a real check with a real caveat, not a full clearance — but it is the standard calendar for this
   series and comes back negative for every named party by direct full-text search.
2. **Sibling search (TNA Discovery, same piece).** `tools/discovery_items.py "SP 8" "SP 8/6" decipher` and
   `... Ehrenstein` return **only the target record itself** — no companion key, decipher, or duplicate found in
   SP 8/6 under those terms.
3. **Community lists.** WebSearch (`Bernstorff Gyldenstolpe Ehrenstein 1689 diplomatic correspondence Denmark
   Sweden William III`) returned only unrelated later Bernstorffs (18th-19th century diplomats) and a
   Gyldenstolpe-family biography (EMLO correspondence catalogue) with no tie to this letter or the year 1689.
   No Cryptiana or Cipherbrain hit; local grep of `sources/cryptiana/` for "ehrenstein"/"bernsdorff"/
   "bernstorff"/"guldenstolp": no hits.
4. **DECODE.** No login attempted. `sources/decode/` greped for "Ehrenstein"/"Bernsdorff"/"Bernstorff"/
   "Guldenstolp"/"SP 8/6": no hits.
5. **Solver repositories.** Both freshly shallow-cloned (24 Sept 2026, shared across this pass's four targets).
   `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`: grep for "ehrenstein|bernsdorff|bernstorff|
   guldenstolp|SP.?8.?6" across both trees: zero matches.
6. **General web search.** As (1) and (3). No result ties a decipherment, key, or prior reading to SP 8/6/65
   specifically, nor definitively identifies "d'Ehrenstein," "de Bernsdorff," or "de Guldenstolp" as the exact
   individuals in this letter (only plausible family-name matches for the period and milieu).

**Host requests this pass:** discovery.nationalarchives.gov.uk 3 (search x2, record detail x1, >=3s apart,
shared budget with the other three targets this run), archive.org 2 (metadata + full-text fetch of CSP Domestic
William and Mary vol. 1), WebSearch 2, github.com 1 shallow clone each of both repos (grepped, shared across all
four targets), sources/decode/ and sources/cryptiana/ local greps (no network).

## Verdict

**Status: open.** The standard calendar for this series (CSP Domestic William and Mary vol. 1, which covers this
exact date window) was fetched in full text and searched for every named party in the catalogue description,
with no hit — a real check, though "nearly all calendared" (TNA's own wording) and OCR fragility on foreign
names keep this a caveat rather than a certainty. No sibling key or decipher found in the same TNA piece; no
community list, DECODE record, or solver-repository entry names this item or any of its three named
correspondents.

**Copy status:** no online image located; `digitised: false` confirmed by direct record fetch (id C18727349).
**Copy-order.** See REQUEST.md.

**Recommended next steps (not run this pass):** (1) a full page-by-page read of CSP Domestic William and Mary
vol. 1 (rather than a name-string grep alone) to rule out an OCR-garbled entry; (2) identify the specific
"d'Ehrenstein," "de Bernsdorff," and "de Guldenstolp" via Scandinavian/Hanoverian prosopography (SSNE database,
per LESSONS.md precedent) before any solve attempt, since a firm identification would open a proper printed-
correspondence search for any of the three; (3) check whether SP 8's neighbouring volumes/pieces (SP 8/1-5,
8/7+) hold a general cipher key for William III's continental correspondents — not searched this pass.

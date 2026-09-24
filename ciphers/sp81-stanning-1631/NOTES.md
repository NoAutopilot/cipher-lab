open

# Duplicate of a paper sent by Mr Stanning, in cipher — TNA SP 81/37/284

QUEUE row: N60 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 81/37/284** (State Papers Foreign, German States), folio 284, [?1631] (TNA
Discovery, fetched 24 Sept 2026, id C7774544; `digitised: false` confirmed by direct record fetch; no separate
`note` field). Scope content: "Folio 284: Duplicate of paper sent by Mr. Stanning in cipher." 1631 is the year
Gustavus Adolphus of Sweden entered the Thirty Years' War in earnest (Breitenfeld, Sept. 1631); Sir Henry Vane
the Elder was sent to Germany that September as English envoy to Gustavus Adolphus's camp, reporting to
Secretary of State Dudley Carleton, Viscount Dorchester.

## Check-solved sweep (24 September 2026)

1. **Editions.** No comprehensive printed calendar or edition covers SP 81 (German States) correspondence for
   1631 — this series has no CSP Foreign equivalent for the Caroline period, and WebSearch for a printed
   edition of Vane's 1631 Swedish-camp correspondence with Dorchester (`Henry Vane elder 1631 Swedish camp
   correspondence Dorchester printed edition letters`) returned only general Vane biography (Wikipedia, SSNE
   database, Find a Grave) with no edition named. "Mr Stanning" is too thin a name to search independently;
   WebSearch (`"Stanning" 1631 Vane Dorchester Gustavus Adolphus cipher correspondence English`) returned no
   identification and only tangential Thirty Years' War background.
2. **Sibling search (TNA Discovery, same piece) — a key/decipher lead.** `tools/discovery_items.py "SP 81"
   "SP 81/37" decipher` finds three items in the same piece with contemporary decipher work already noted by
   the cataloguer: **SP 81/37/93** ("Vane to 'my lord' with duplicate and decipher," 1631 Oct. 19), **SP
   81/37/169** ("Vane to Dorchester — 3 letters with decipher of one," 1631 Dec. 3), and **SP 81/37/216** ("Vane
   to [Dorchester], with portion deciphered," 1631 Dec. 11/22 (sic)). This confirms the piece as a whole carries
   active Vane<->Dorchester ciphered traffic from the Swedish-camp mission, with at least three folios TNA
   itself already marks as (partly) deciphered — the same "look for the sibling" shape as sp81-roe-1638's f.88
   lead, though here the target is explicitly a **duplicate** of a paper "sent by Mr. Stanning" rather than a
   Vane-Dorchester letter itself, so it is not certain the three decipher-marked folios share Stanning's key; a
   "duplicate" also implies an original survives, possibly catalogued or annotated elsewhere. Not resolved by
   image (none online).
3. **Community lists.** WebSearch and local grep of `sources/cryptiana/` for "Stanning"/"SP 81/37": no hits.
4. **DECODE.** No login attempted. `sources/decode/` greped for "Stanning"/"SP 81/37": no hits.
5. **Solver repositories.** Both freshly shallow-cloned (24 Sept 2026, shared across this pass's four targets).
   `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`: grep for "stanning|SP.?81.?37" across both trees:
   zero matches naming this item, this piece, or "Stanning."
6. **General web search.** As (1) and (3). No result ties a decipherment, key, or prior reading to SP 81/37/284
   specifically, or identifies "Mr Stanning" as a known historical figure of the period.

**Host requests this pass:** discovery.nationalarchives.gov.uk 3 (search x2, record detail x1, >=3s apart,
shared budget with the other three targets this run), WebSearch 2, github.com 1 shallow clone each of both
repos (grepped, shared across all four targets), sources/decode/ and sources/cryptiana/ local greps (no
network).

## Verdict

**Status: open.** SP 81 German States has no printed calendar for 1631; no edition of Vane's Swedish-camp
correspondence was located; "Mr Stanning" could not be identified. No community list, DECODE record, or
solver-repository entry names this item. The strongest finding this pass is a **lead, not a clearance**: three
neighbouring folios in the same piece (ff. 93, 169, 216) are already catalogued by TNA as carrying contemporary
decipher work on Vane-Dorchester correspondence from the same months — worth ordering alongside the target (see
REQUEST.md), on the chance the same office cipher covers "Mr. Stanning"'s paper too, though this is not
confirmed and the target is a duplicate, which may point to a different original and route.

**Copy status:** no online image located; `digitised: false` confirmed by direct record fetch (id C7774544).
**Copy-order.** See REQUEST.md.

**Recommended next steps (not run this pass):** (1) identify "Mr Stanning" — a Merchant Adventurers or Eastland
Company agent in the Baltic/German trade is plausible given the context, not checked this pass; (2) once
imaged, compare f.284's cipher symbols against the deciphered stretches of ff.93/169/216 to test whether it is
the same office key; (3) HMC reports for correspondents connected to the 1631 Swedish mission (not searched
this pass, outside this run's hosts).

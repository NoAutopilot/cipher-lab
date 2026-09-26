# Weber 1979 be-api full-text snippets on WE027 (ARM3-LIVCODE, 26 Sept 2026)

Source: `be-api.us.archive.org/fts/v1/search?q=<term>&identifier=unitedstatesdipl0000webe`
(Weber, *United States Diplomatic Codes and Ciphers, 1775-1938*, print-disabled, not borrowable --
per the Access playbook and `tools/data/uscodes-1800/README.md`). This item's `page_num` field is not
a real locator (Access playbook's documented caveat), so no page number is cited; footnote markers (`*!`)
are OCR noise for a superscript note number, not a real character.

## The passage (assembled from three overlapping queries: "WE027", "WE027 nomenclator", "WE027 code")

> ... [despatches to the] Secretary of State James Madison continued to be masked in the **WE027**
> nomenclator.[note] In Washington, the atmosphere was heavy with secrecy during these months; in
> [material not recovered by these queries] ... reconstructed over 1000 of the elements in the
> **WE027 code**. **Livingston to King, Paris, January 25, 1802** [citation, likely a footnote to
> Weber's own source for the reconstruction] ...

Two facts read together, not in conflict:
1. Weber's own reconstruction of WE027 (over 1000 of its elements) is sourced to a specific letter,
   **Livingston to King, Paris, January 25, 1802**.
2. Weber's own prose says despatches **to Secretary of State James Madison** were "masked in the WE027
   nomenclator" -- i.e. WE027 was Livingston's working code for his official correspondence generally,
   not a King-only channel.

This resolves ARM3-COR's flagged discrepancy (`tools/data/uscodes-1800/README.md`'s table calls WE027
"Livingston <-> Madison"; ARM3-COR read Weber's own reconstruction-source citation as "Livingston to
King" and flagged the README as wrong): **both are consistent with Weber's own text.** WE027 is
Livingston's own nomenclator, used with more than one correspondent (Madison as Secretary of State,
and King, per the reconstruction citation); the README's "Livingston <-> Madison" label is not wrong,
just incomplete (it should also name King). Not corrected in that README by this worker (out of this
job's file list, per the brief).

## Other results

- `q=Livingston` (no "WE027" qualifier) surfaces an *unrelated* older passage: the "Livingston-Washington
  and Livingston-Adams-Dana codes" and the "Jay-Livingston secret correspondence" of 1781-82 -- Robert
  R. Livingston's father-generation cousin/relative correspondence from the Confederation period, a
  different code family, not WE027. Not chased further (wrong era).
- `q=King` alone surfaces the "Murray to King" / "King to J.Q. Adams" run (King's London legation
  correspondence with Rufus King as Minister, 1798-99 -- a different King-side code, not WE027 specifically).
- `q=reconstructed` surfaces Weber's general method paragraphs (worksheets, partial keys, Bendikson's
  ultraviolet-radiation recovery of erased passages) -- general methodology, not WE027-specific.
- `q=worksheets` confirms Weber's source for these reconstructions is the **Irving Brant Papers,
  Library of Congress** (Brant being Madison's biographer) -- a possible further lead for a WE027
  table, not chased this pass (out of scope; flagged for a successor).
- Zero hits for "Bowdoin" or "Skipwith" (ARM3-COR's own candidates) anywhere tied to WE027 or code 27.

## Requests

be-api.us.archive.org: 12 (8 single-term + 4 targeted-phrase), all >=1.5s apart, descriptive User-Agent,
no 429/403/challenge. No logins, no credentials touched.

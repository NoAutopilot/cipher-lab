# PREREG-SUR-2061 (15 Oct 2026, 02:5x UTC by date -u; worker SUR-2061, LANE DEFAULT-A4-0235-15, account 4)

Written and pushed before den Heijer 2012 p. 362 is fetched or read.

Item: H. den Heijer, Grote Atlas van de WIC II (2012), NA 2.14.97 inv. 24.2, p. 362 -- the facsimile page for 4.VEL 2061
(Redout Leyden; catalogue `altformavail` "Gefacsimileerd ... deel II p. 362", vel_2030-2090_catalogue.tsv row 2061).

Question: does any clear text on that page (caption, plate labels, any transcription) supply a crib for the 2061 battery
block's unkeyed (U, 10) or two-valued (M, 69) tokens in reading_2061_battery_nieuw_tokens.tsv?

Pass rule (fixed now):
1. A crib counts only if it is clear Dutch text on the page (or a proper name -- place, fort, person -- that the cipher
   would spell as written), read in clear by one blind Sonnet pass and confirmed by a second independent checker pass.
   An English paraphrase (as on AMH 2218) is content, not a crib, and cannot move a token.
2. MATCH: the crib aligns to a contiguous span of the 2061 decode at >= 2 U or M tokens, AND every H/C token inside the
   aligned span agrees with the crib letter (zero conflicts with a known key value), AND the span is placed where the
   crib's meaning belongs (same legend letter / battery number per AMH 2218).
3. Anything less (1 token, any H/C conflict, English-only content, no clear text) = NOT FOUND for this item.
4. No key.tsv / key_period* edit unless `tools/decode_key.py . --try CODE=VALUE` passes its own control for the value
   class; otherwise a match is recorded as an M-grade lead in NOTES.md only.
Requests: service.archief.nl IIIF <= 8 (plus the NA item page for the scan list), >= 1.7 s apart; images stay in scratchpad.

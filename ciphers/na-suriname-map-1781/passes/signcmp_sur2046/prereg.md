# SUR-2046 (account 4, LANE DEFAULT-A4-2040), 12 Oct 2026 -- pre-registration, pushed before the vision call and before any look at the 2046 crops

Why: GAPS18's reading of 4.VEL 2046 (redout Purmerent) has 31 U tokens on reader codes that key_period_codes_nieuw.tsv
lacks. Question per token: which sign of the Nieuw Secreet Alphabet sheet (NA 1.05.03 inv. 86 scan 0003) is it, or none.

Targets (31, from reading_2046_legend_nieuw_tokens.tsv grade U; exact counts, which differ from the brief's "[d-hook] x9,
[s-hook]" summary): [d-hook] 10, [amp] 3, [o-flag] 3, [s-hook] 3, [3-breve] 2, [delta-grave] 2, and one each of [1-hook],
[a-grave], [delta-dots], [diamond], [h-tilde], [p-grave], [w-dots], [x-dot-grave].
Known-answer controls (20, mixed in blind, query numbers shuffled so number does not reveal role): 2 H tokens each (seeded
sample, seed 2046) of reader codes 3, 7, [lambda], [psi], 5, [hash], 6, [delta], h, o, each the sheet's own sign under the key.
queries_key.tsv holds role and key value; the reader never sees it.

Instrument (GAPS25/GAPS29 shape): crops = GAPS18's tools/iiif_lines.py half-line crops images/crops_2046_leg/leg46_Lnn_s1/_s2
(no full image), query positions masked as #k in the line's reader-code sequence (query_sequences.txt); references =
blind_refs.jpg, ALL 54 signs of the sheet (45 alphabet signs + 9 code-group signs; plain-letter and word columns cut away),
relabelled R1-R54 with seed 20261012 (blind_key.json). 28 boxes reuse GAPS15's ref_tiles.json, 26 are cut here (build_call.py).
One blind Opus subagent call (brief.md): no values, no decode, no repository context. Then the worker's own reconciliation as
one further priced unit (checks location/consistency of the call's rows; it may only withhold a relabel, never add one).

Settle rule per instance (GAPS25/29): best_conf >= 0.6, located = sure, second choice a tile of a different value or NONE.

Gate (run first, the prior calls' bar): >= 2/3 of the 20 controls (>= 14) settled on a tile whose value equals the key value.
Otherwise: stop, log "non-test (controls below gate)", no relabel, no exception row.

Targets, only if the gate passes:
- A class (reader code) with >= 2 instances in the call is relabelled only if >= 2/3 of its instances are settled AND every
  settled instance names a tile of the same value v; then each SETTLED instance -> v; unsettled instances stay U.
- A singleton class -> v if its one instance is settled.
- Best = NONE at >= 0.6 -> stays U, logged "not on the sheet per the call".
- A settled value on a code-group tile -> the code word.
- Grade of every relabel: M (image-only identity with no key row for this reader code, no crib or control on the word).
Written as 2046-only rows of exceptions_nieuw_image.tsv; key_period_codes_nieuw.tsv unchanged (reader-code identity across
sheets is an image question, GAPS21). Then tools/decode_key.py ciphers/na-suriname-map-1781 --check exit 0; H/C/M/U before
and after. No reading claim is made from this step (GAPS18's vocabulary control FAILed; that stands).

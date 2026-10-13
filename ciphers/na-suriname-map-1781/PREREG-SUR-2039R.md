# PREREG SUR-2039R (account 4, LANE DEFAULT-A4-0935, 13 Oct 2026) -- pushed before the vision call and before any score

Question: which sign of the Nieuw Secreet Alphabet sheet (NA 1.05.03 inv. 86 scan 0003) is each of the 10 unkeyed tokens of the
4.VEL 2039 Remarque (GAPS16 native re-pass; reading_2039_remarque_nieuw_tokens.tsv grade U), or none?
Targets (exact): K x4 (2039_rem_L3:7, L4:5, L4:35, L5:2), O x2 (rem_head:0, L3:48), & x2 (L3:60, L4:42), [J-rev] x2 (L2:11, L4:26).
Not targets: the other five U tokens of the file (F x2, [phi], [z-heavy], [a-tick]) -- outside this job's brief.

Instrument (passes/signcmp_sur2039r/, build_call.py; the SUR-2046 / V-SUR2046 shape):
- References: blind_refs.jpg, ALL 54 sheet signs (SUR-2046's boxes: 45 alphabet + 9 code groups, plain-letter and word columns cut
  away), relabelled R1-R54 with a fresh seed (20391013); mapping in blind_key.json, never shown to the call.
- Known-answer controls: 20 H tokens of the SAME Remarque hand (same crops, same line set), 2 each of o, [hash], r, l, [lambda], 8,
  [psi], [delta], 3, 7 (seed 2039), weighted to round/looped shapes nearest the targets (o and [hash] vs O; l, [lambda], r vs K;
  8 and [psi] vs [J-rev]). Each class is the sheet's own sign under the key, so the control CAN miss (land on another tile) the
  same way a target can: it tests the axis the target answers turn on (base-shape identity against the sheet tiles). Unlike
  V-SUR2046's audit point, the targets here are base shapes, not diacritic variants.
- Queries: 30 (10 targets + 20 controls), numbers shuffled (seed 1039) so the number does not reveal role; positions masked as #k in
  each line's reader-code sequence (query_sequences.txt); crops images/crops_2039_remN/remN_L01..L06_s1..s3 (tools/iiif_lines.py,
  GAPS16; no full image; the debug overlay withheld). The subagent is told nothing of values, decode or repository context, and to
  judge every instance on its own.
- One blind Opus subagent call (brief.md -> result.tsv). Then the worker's reconciliation as one priced unit: location/consistency
  check of the call's rows; it may only withhold a relabel, never add one.

Settle rule per instance (GAPS25/29, unchanged): best_conf >= 0.6, located = sure, second a tile of a different value or NONE.

Gate (run first): >= 14/20 controls settled on a tile whose value equals the key value. Below gate: stop, "non-test (controls
below gate)", no relabel, no exception row.

Targets, only if the gate passes (apply.py -> decisions.tsv):
- Class rule: a class with n instances is relabelled only if >= ceil(2n/3) instances are settled (K: 3 of 4; O, &, [J-rev]: 2 of 2)
  AND every settled instance names a tile of the same value v; then each SETTLED instance -> v; unsettled instances stay U.
- Look-alike withhold (V-SUR2046's rule): if any control whose key value differs from v settles on the same tile as a target's
  settled answer, the class is withheld (stays U, logged "call does not separate it from <control sign>").
- Best = NONE at >= 0.6 -> stays U, logged "not on the sheet per the call".
- A value on a code-group tile -> the code word.
- Grade: M. H only if ALL of: controls >= 18/20 settled correct (margin over the gate), every instance of the class settled at
  best_conf >= 0.7, and no look-alike withhold; otherwise M. No C or S from an image call.
- Rows go into exceptions_nieuw_image.tsv as 2039_rem_* rows only; key_period_codes_nieuw.tsv unchanged (reader-code identity
  across sheets is an image question, GAPS21). Then tools/decode_key.py ciphers/na-suriname-map-1781 --check exit 0; H/C/M/U
  before and after for the 2039 job.
- Any reading of the relabelled words in context is an observation, not a test (not scored, no grade change from it).

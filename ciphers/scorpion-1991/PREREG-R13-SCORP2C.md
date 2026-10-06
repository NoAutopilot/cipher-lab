# Pre-registration: R13-SCORP2C, blind second-coder distinct-code test (scorpion-1991, 6 Oct 2026)

Committed and pushed before coder B's codes are seen or scored. Follows NOTES.md "Cheap test 3" (A2P4-SCORP2), whose
verdict named this step: one coder's codes decided both sides there (coder A = A2P4-SCORP2, `shape/scorpion_codes.tsv`,
`shape/zodiac_codes.tsv`).

**Coder B.** One Sonnet subagent, given only: the 7 S1 row crops (cut with `tools/iiif_lines.py`, same centres as
A2P4-SCORP2), one labelled contact sheet of the 70 Zodiac Z408/Z340 webtoy glyphs (same source, D. Oranchak, refetched),
and the feature-code vocabulary copied verbatim from `shape_prereg.md` ("Feature code" paragraph). No earlier codes, no
NOTES, no sign names. B codes every S1 position (r1c1..r7c10, 70 positions) and every Zodiac glyph (70) into that
vocabulary. B sees the Zodiac sheet as the brief requires; this can only prime B towards Zodiac codes on S1, i.e. it
biases towards SUPPORT, so a NO SUPPORT result is conservative and a SUPPORT result carries that caveat.

**S1 type codes from B.** Positions are mapped to coder A's 53 types by `ciphertext.txt` (layout only, A's names are not
shown to B). A type's B-code is the modal code over its positions (tie: the earliest position).

**Statistic (distinct-code, primary).** CROSS-CODER: the number of distinct non-letter codes (all codes except `L:`) in
B's S1 type codes that occur identically among coder A's Zodiac codes (`shape/zodiac_codes.tsv`), against the number
that occur among the control's codes (`shape/control_unicode_geometric.tsv`, Unicode Geometric Shapes U+25A0..U+25E5,
coded from Unicode names -- no coder at all). S1 side and Zodiac side are now coded by different people; the control
side by no one.
**Control can differ:** the control code set is fixed and independent of both coders; B's S1 codes can land in
either set, both, or neither, so the two counts move independently (coder A's own values: Zodiac 13, control 6
distinct codes, descriptive only).

**Decision rule.** SUPPORT for "draws on published Zodiac material" iff cross-coder Zodiac count minus control count
>= 5 distinct codes AND at least one of the counted Zodiac codes is absent from the control. Otherwise NO SUPPORT.

**Secondary, descriptive (cannot license support):** (a) the same statistic on B's S1 codes against B's own Zodiac
codes; (b) per-type counts as in A2P4-SCORP2 on B's codes; (c) agreement A vs B: Cohen's kappa over the 70 S1
positions (A's type code at each position vs B's position code) and over the 70 Zodiac glyphs, exact-code agreement,
plus base-level agreement (the part before `/`, or the `ST:`/`L:`/`RL:` family name).

Scored by `shape/score_b.py` (writes `shape/result_b.tsv`; `--check` exits non-zero when stale). No reading; every
code is grade M (eye judgement); no tokens graded. Status stays `open` whatever the result.

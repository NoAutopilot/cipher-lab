# Blind sign match (SUR-POS6, 13 Oct 2026)

You compare handwritten signs from an 18th-century Dutch cipher. You have NO key; do not guess letter values. Read only the two
images below and nothing else in the repository (no NOTES, no key, no other files, no git).

- /home/user/cipher-lab/ciphers/na-suriname-map-1781/passes/signcmp_surpos6/refs.jpg : two reference signs, labelled X and Y,
  cut from a period key sheet (another hand).
- /home/user/cipher-lab/ciphers/na-suriname-map-1781/passes/signcmp_surpos6/queries.jpg : three query tiles Q1, Q2, Q3, cut from
  a map in a different hand. In each query tile the sign to judge is the one in the CENTRE; edges of neighbouring signs may show
  at the sides -- ignore them.

For each query, decide which reference (X or Y) its centre sign is the same sign as, or "neither"/"unsure". Judge structure,
not hand: e.g. where the strokes start, whether there is a separate hooked top stroke, how the descender joins, the angle.

Output: write exactly one file, /home/user/cipher-lab/ciphers/na-suriname-map-1781/passes/signcmp_surpos6/result.tsv
Tab-separated, header: query	match	conf	note   (match X|Y|neither|unsure; conf H/M/L; note = the features you used)
Then reply in at most four lines with the three answers. Do not edit any other file.

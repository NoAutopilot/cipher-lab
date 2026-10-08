# PREREG-D4-BROC (8 Oct 2026, written before any blind pass ran)

Job: D4-BROC (LANE DEFAULT-account-4-20261008-0740), letter 134 doubled-loop / 't' image pass.
Crops (cut with tools/iiif_lines.py --image ... --region ... --out images/broc --debug; commands in NOTES.md):
  target: images/broc/m0275_L03.jpg, m0275_L04.jpg (m0275-r1), m0276_L01.jpg (m0276-r1), m0276_L03.jpg, m0276_L04.jpg (m0276-r2)
  control: images/broc/m0179_L01.jpg (m0179-r1, letter 80; appendix Carta 80 copies the run)
  decoys (appendix, atlas PX-BROGLYPH crops, downscaled): images/broc/decoy_m0280_carta13_line2.jpg,
  decoy_m0294_carta110_line2.jpg, decoy_m0291_carta96_line3.jpg

## Slots
S1 m0275-r1 pos 8 (ff?, pass A '55?'); S2 m0276-r1 pos 10 (ff?); S3 m0275-r1 pos 31 (dd?); S4 m0276-r2 pos 16 ('t');
K  m0179-r1 pos 16 (ff?; the Carta 80 appendix copy has a single f -> s at this slot).

## Classes a pass can give a slot
D = one doubled-loop sign (the same shape as K and as the sign after '2' in the m0291 decoy);
P = two digits '5''5' (code 55); X:<code> = another single known code; U = unreadable/other.

## Known-answer gate (per pass; a pass that fails it is void)
G1: token accuracy >= 85% on the two decoy lines against the master transcription, aligned by edit distance,
    z == 7 (one glyph, PX-BROGLYPH): Carta 13 line 2 = 13.c.7.18 | 15.4.5.15.m.c.7.m.5.7.18.y.8.4;
    Carta 110 line 2 = 55.x.7.12.18.7.16.15.e.7.2.7.18.8.18.
G2: the pass gives the m0291 decoy's second sign class D (not P, not two separate digits).
G3: the pass reads m0276-r2 pos 3 (an agreed '55' in a target crop) as 55.
The decoys can fail a pass: a reader that turns every looped sign into 55, or every 55 into a loop, misses G2 or G3.

## What settles a slot
- Both passes valid and both give the same class -> class settled, transcription conf H.
- Valid passes disagree -> reconciliation from the crops (one unit); a reconciled class gets conf M at best.
- < 2 valid passes -> nothing changes; slot stays as it is.
Values: P -> token 55 (key 55 -> p, C). X:<code> -> that code's key value (conf M for S4: a glyph-identity read, not attested).
D -> token 'ff'. key.tsv gains `ff -> s` (grade M, one witness) only if K is class D in both valid passes
(the per-unit merge clause: the m0179 unit's own control is the Carta 80 copy's single f at that slot); otherwise
'ff' stays unkeyed (U). S4 read as 't' (no known code) stays U.
After applying: tools/decode_key.py --check; letter 134 regrade counts reported; no LM rescoring (separate job).

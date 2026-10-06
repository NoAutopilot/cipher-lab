# R12D-GRA blind slot pass (shapes only)

You compare invented cipher signs in images. You do not decode and there is no text to find.
Reference: Read /home/user/cipher-lab/ciphers/fr2980-gramont/atlas/atlas_f29.png first (each row = a code with exemplars).
The four codes that matter: `z` (plain z-shape, NO crossing bar), `zb` (z-shape WITH a horizontal bar across it),
`d` (d-shape: round bowl with an upright/slanting stem going up), `n6` (a 6/delta-like shape: round bowl with a stem curling
back over the top to the left, like the Greek delta).

For each half-line image below, a reader's left-to-right sign sequence is given; the signs to judge are marked [[Snn]].
Locate each marked sign by counting along the sequence (the sequence may be off by one or two signs; use the neighbours),
look at it closely, and answer which of its TWO options it is. If you cannot locate it or cannot tell, answer `cannot`.
Images (Read each): /home/user/cipher-lab/ciphers/fr2980-gramont/images/fr3040_f18/<half>.jpg

- f18rB_L01_a: 2 [[S01: z or zb]] x n6 E p 9 [[S02: z or zb]] 5 H c t D h H
- f18rB_L02_b: v A2 lt u ss2 [[S03: z or zb]] dl lt g bb c 9 2 ST [[S04: z or zb]] h H 5 g2 f g bb lt x
- f18rB_L03_b: dl b h bb 2 9 o x III z H [[S05: z or zb]] 9 o dl [[S06: z or zb]] b 9 NEW:curly s-like g2 2 H c
- f18rB_L04_b: m b xr yt dl c g 2 q ST o lt H [[S07: d or n6]] III D g 9 H x v z xr o
- f18rB_L05_b: 9 [[S08: d or n6]] m 9 r3 q b [[S09: d or n6]] 2 rho [[S10: z or zb]] q bb oi 2 4t x p H 2 bb v oi
- f18rB_L06_a: H c H lam g lt H 9 [[S11: d or n6]] m p x H
- f18rB_L06_b: 5 yt dl z [[S12: z or zb]] 5 H f oi h x [[S13: d or n6]] yt 4t D g H c 2 x o oi 9 z
- f18rB_L07_b: H 9 n6 D g xr c n6 x h bb b H yt H x v z H 2 2 [[S14: z or zb]] x [[S15: d or n6]]
- f18rB_L08_b: oi 5 c q eh H 5 m TRI 4t eh oi dl x [[S16: z or zb]] b 4t 9 oi n6
- f18rB_L09_a: lam h c m [[S17: z or zb]] oi h H [[S18: d or n6]] p x
- f18rB_L09_b: v oi f z bb q D g oi c q [[S19: z or zb]] lt A2 2 lt [[S20: d or n6]] p x z 2 m bb oi
- f18rB_L10_a: HASH q h c xr dl b g [[S21: z or zb]] m z
- f18rB_L10_b: H 2 b g r3 xr m bb q p lt H 2 rho oi [[S22: z or zb]] b H 9 [[S23: d or n6]] m
- f18rB_L11_b: 9 4t x [[S24: z or zb]] eh oi [[S25: d or n6]] yt ST q 2 f x [[S26: d or n6]] III oi h [[S27: z or zb]] 2 ss2

Return ONLY a TSV block: header `slot<TAB>answer<TAB>note`, one row per Snn (S01..S27), answer in {z, zb, d, n6, cannot}, note <= 8 words on the shape seen.

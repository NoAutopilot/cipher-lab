# Shape judge by window, ink 54 (value-blind)

169 positions. First open the reference image /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/ref.png: REF A and REF B are two signs from a 16th-century
cipher table. Then open the montages IN ORDER (6 windows each, captioned in blue with the position id). In each window the red ticks mark
the ESTIMATED position of the sign (can be 1-3 signs off); find it using the keyboard labels of the signs just before and after it.

For each position give ONE class for the sign's SHAPE:
  SIGMA  = two horizontal bars (top and bottom) joined by a near-upright stem, or a stem that bends back; NO diagonal stroke running
           from upper right to lower left (like REF A, a Sigma or a capital I with bars)
  ZED    = top bar and bottom bar joined by a DIAGONAL stroke (like REF B), including a crossed z or a 2-shaped z with a diagonal
  OTHER  = a round-topped 3 (curved top, descender), an x, an r-like loop, a digit 2 without a bottom bar, or anything else
  UNSURE = you cannot find the sign or cannot tell
conf H clear / M probable / L guess.

Montages: /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R01.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R02.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R03.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R04.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R05.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R06.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R07.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R08.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R09.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R10.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R11.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R12.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R13.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R14.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R15.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R16.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R17.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R18.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R19.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R20.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R21.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R22.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R23.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R24.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R25.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R26.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R27.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R28.png, /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_win/viv54R29.png

Answer with one TSV row per position, header: id<TAB>class<TAB>conf<TAB>note   (note = the stroke feature you SAW, e.g. "upright stem").
Write the answer to /home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/tx/lookalike54/viv54R_judge.tsv. Judge shapes only; do not guess any meaning.

Positions (id, neighbours):
f173r.L04.14	before: o g d | after: @ m z
f173r.L04.17	before: z @ m | after: m j m
f173r.L05.19	before: : 7 to | after: m j m
f173r.L05.33	before: P g {curl} | after: m g p
f173r.L05.47	before: : 7 to | after: tz
f173r.L06.21	before: m p # | after: m f m
f173r.L06.33	before: m d P | after: P p #
f173r.L07.7	before: p 4 d | after: tz p m
f173r.L07.17	before: o g d | after: m p #
f173r.L07.26	before: d o tz | after: a j p
f173r.L07.34	before: L i to | after: m d tz
f173r.L08.10	before: o : # | after: a 3 tz
f173r.L08.12	before: # 3 a | after: tz o :
f173r.L08.35	before: d g # | after: P D d
f173r.L08.45	before: y m @ | after: 7 2 m
f173r.L08.47	before: @ 3 7 | after: m
f173r.L09.20	before: P r tz | after: m d 3
f173r.L09.23	before: 3 m d | after: m e 6
f173r.L10.40	before: : 7 to | after: tz d m
f173r.L11.2	before: to | after: m j m
f173r.L11.33	before: d d + | after: P g @
f173r.L11.38	before: g @ m | after: tz d r
f173r.L11.43	before: d r # | after: 7
f173r.L12.25	before: m 4 d | after: o o m
f173r.L12.39	before: d o o | after: m P o
f173r.L12.46	before: o @ m | after: tz
f173r.L13.2	before: m | after: o # P
f173r.L13.7	before: # P r | after: tz j P
f173r.L13.24	before: tz : : | after: P o o
f173r.L13.33	before: : @ m | after: x m d
f173r.L13.34	before: @ m z | after: m d #
f173r.L13.39	before: d # d | after: # m tz
f173r.L13.43	before: # m tz | after: a d y
f173r.L14.5	before: m @ m | after: m 6 to
f173r.L14.9	before: m 6 to | after: m S h
f173r.L14.19	before: @ + # | after: m a g
f173r.L14.39	before: j m S | after: 7 : :
f173r.L14.47	before: : : d | after: # m
f173r.L15.2	before: m | after: o # m
f173r.L15.6	before: o # m | after: g P tz
f173r.L15.14	before: o # m | after: S P tz
f173r.L15.33	before: d o o | after: m P o
f173r.L15.45	before: p d p | after: tz : :
f173r.L15.53	before: o o d | after: j
f173r.L16.4	before: @ tz L | after: m p m
f173r.L16.22	before: X S d | after: m g 6
f173r.L16.37	before: tz 6 m | after: # k m
f173r.L17.7	before: m : to | after: m d y
f173r.L17.37	before: S @ m | after: m 7 d
f173r.L18.10	before: p o o | after: m p y
f173r.L18.17	before: p o o | after: m p A
f173r.L18.22	before: p A P | after: p d tz
f173r.L18.31	before: p d p | after: P P d
f173r.L18.37	before: d o m | after: o z g
f173r.L18.39	before: m z o | after: g m @
f173r.L18.49	before: k P L | after: P j m
f173r.L19.3	before: y d | after: # m d
f173r.L19.7	before: # m d | after: m : tz
f173r.L19.17	before: m # m | after: # z m
f173r.L19.19	before: m x # | after: m d o
f173r.L19.34	before: P p k | after: P tz d
f173r.L19.41	before: # g m | after: m y 7
f173r.L20.15	before: 7 p d | after: # m d
f173r.L20.30	before: p m to | after: m y y
f173r.L21.7	before: o # m | after: tz j tz
f173r.L21.24	before: tz g m | after: r 4 P
f173r.L21.32	before: tz p d | after: 7 # d
f173r.L22.1	before:  | after: m z a
f173r.L22.3	before: z m | after: a p tz
f173r.L22.17	before: y p P | after: m e P
f173r.L22.37	before: d i p | after: d z P
f173r.L22.39	before: p z d | after: P tz a
f173r.L23.42	before: g P p | after: m m p
f173r.L24.4	before: tz d m | after: r tz d
f173r.L24.8	before: r tz d | after: m o o
f173r.L24.14	before: o j m | after: m p #
f173r.L24.36	before: : : m | after: # m P
f173r.L25.17	before: # g m | after: m g #
f173r.L26.6	before: 7 p m | after: # P a
f173r.L26.15	before: P # to | after: m j m
f173r.L27.14	before: # P # | after: m y p
f173r.L27.38	before: a y d | after: m # #
f173v.L01.13	before: m d P | after: m g tz
f173v.L01.33	before: d tz 4 | after: m e s
f173v.L01.39	before: s a d | after: m c a
f173v.L02.10	before: { curl } | after: P d +
f173v.L02.14	before: P d + | after: # g m
f173v.L02.21	before: g d m | after: m + +
f173v.L02.36	before: p l d | after: + tz :
f173v.L02.44	before: 7 p m | after: # to z
f173v.L02.47	before: x # to | after: tz d m
f173v.L03.1	before:  | after: d o o
f173v.L03.5	before: d o o | after: tz d o
f173v.L03.27	before: : : m | after: # m P
f173v.L03.32	before: m P g | after: m m z
f173v.L03.35	before: z m m | after: m z m
f173v.L03.37	before: m z m | after: m t D
f173v.L03.42	before: t D i | after: +
f173v.L04.17	before: l d to | after: P a P
f173v.L04.21	before: P a P | after: m to R
f173v.L04.24	before: z m to | after: tz d tz
f173v.L04.40	before: a d m | after: m to R
f173v.L04.43	before: z m to | after: m 6 to
f173v.L04.47	before: m 6 to | after: m
f173v.L05.12	before: d tz m | after: # : :
f173v.L05.22	before: { asterisk } | after: d p x
f173v.L05.25	before: z d p | after: # g m
f173v.L06.1	before:  | after: m p a
f173v.L06.26	before: p o o | after: k t tz
f173v.L06.34	before: : # @ | after: m d P
f173v.L07.1	before:  | after: d o 6
f173v.L07.11	before: o g P | after: a n p
f173v.L07.28	before: 7 6 a | after: P z z
f173v.L07.30	before: a z P | after: z m p
f173v.L07.31	before: z P z | after: m p k
f173v.L07.37	before: k m m | after: # m p
f173v.L08.11	before: p : : | after: | p d
f173v.L08.23	before: : g d | after: m m p
f173v.L08.38	before: k d d | after: S g m
f173v.L08.51	before: o d p | after: 
f173v.L09.10	before: tz d k | after: 6 z m
f173v.L09.12	before: k z 6 | after: m p P
f173v.L09.28	before: o p m | after: d z P
f173v.L09.30	before: m x d | after: P m |
f173v.L09.37	before: m # m | after: # z m
f173v.L09.39	before: m x # | after: m o P
f173v.L09.46	before: g # tz | after: 
f173v.L10.12	before: d + p | after: o o {
f173v.L10.38	before: b a d | after: m o m
f173v.L11.42	before: o 6 # | after: p z P
f173v.L11.44	before: # z p | after: P z #
f173v.L11.46	before: p z P | after: #
f173v.L12.2	before: to | after: m e d
f173v.L12.9	before: y y to | after: m : :
f173v.L12.20	before: + 4 m | after: m p #
f173v.L12.41	before: m d H | after: 3 z m
f173v.L12.42	before: d H z | after: z m :
f173v.L12.43	before: H z 3 | after: m : P
f173v.L13.9	before: y y P | after: d d d
f173v.L13.19	before: # g # | after: o o 3
f173v.L13.22	before: z o o | after: 8 m x
f173v.L13.25	before: 3 8 m | after: tz m x
f173v.L13.28	before: x tz m | after: # k m
f173v.L13.34	before: m : m | after: H n o
f173v.L13.38	before: H n o | after: k m :
f173v.L14.3	before: o o | after: x r g
f173v.L14.4	before: o o z | after: r g y
f173v.L14.30	before: p p r | after: P p #
f173v.L14.35	before: p # m | after: # m z
f173v.L14.38	before: x # m | after: P y y
f173v.L14.49	before: m a to | after: P
f173v.L15.24	before: tz 6 m | after: # x #
f173v.L15.26	before: m x # | after: # d t
f173v.L15.30	before: # d t | after: # z z
f173v.L15.32	before: t z # | after: z y x
f173v.L15.33	before: z # z | after: y x d
f173v.L15.35	before: z z y | after: d o o
f173v.L15.42	before: j o o | after: m d 4
f173v.L16.38	before: p k m | after: m p #
f173v.L16.48	before: y o o | after: 
f173v.L17.4	before: m # m | after: # d tz
f173v.L17.15	before: n m to | after: tz P o
f173v.L18.30	before: m d P | after: H n o
f173v.L18.45	before: m # m | after: # d
f173v.L19.9	before: p k P | after: z z m
f173v.L19.10	before: k P z | after: z m a
f173v.L19.11	before: P z z | after: m a P
f173v.L19.43	before: p m p | after: L
f173v.L20.3	before: + y | after: + @ [...]

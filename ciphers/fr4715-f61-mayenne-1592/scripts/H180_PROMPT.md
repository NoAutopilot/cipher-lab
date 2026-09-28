# H180 (runner 6, 28 Sept 2026) -- WRITTEN BEFORE THE CALL
Tiles images/h180/tiles.jpg (26: H22's form-A anchors 8 and form-B anchors 6 from read_call_BR.tsv, f.176r brackets 12 that both H177b
passes code as a bracket, rows L13-L19; shuffled seed 180; key scripts/h180_key.tsv never shown), built by scripts/h180_tiles.py.
Design change before the call (logged): a free shape grouping sorted tiles by hand and size in H178b, so this call asks fixed attributes
(H22's own discriminating attribute), not groups.
CONTROL GATE: the diagonal attribute read right on >= 12 of the 14 anchors (A = yes, B = no; 'unclear' counts as wrong). Below it: no
reading of the f.176r tiles is used (non-test).
TARGET: of the f.176r tiles not 'unclear', share with diagonal = no. >= 80% (and at least 7 tiles) -> f.176r's brackets are form B, the
f.61 form, so H177b's EBR = l (43/55 under the period decipherment) is a period reading of f.61's bracket form (B = l/y, H22 under
Tomokiyo's letters). <= 20% -> form A. Else mixed, no reading.
Prompt (one Opus vision call, inline reply, the only tool allowed is reading the one image):
> Read the one image file /home/user/cipher-lab/ciphers/fr4715-f61-mayenne-1592/images/h180/tiles.jpg with your image reader; use no
> other tool and write no file. It holds 26 numbered tiles from 16th-century cipher manuscripts. In each tile, look only at the
> bracket-like sign nearest the horizontal centre (a sign made of a vertical stroke with a top bar and a foot bar, open to the right).
> For that sign answer two questions: (a) diagonal: is there a thin diagonal stroke running from the right end of the top bar down to
> the foot of the vertical (making the sign look nearly like a triangle)? yes / no / unclear. (b) foot: is the foot bar longer than the
> top bar? yes / no / unclear. If the centre holds no bracket-like sign, answer 'unclear' for both. Do not guess any meaning. Reply
> inline ONLY with a TSV block: header 'tile<TAB>diagonal<TAB>foot<TAB>note', one row per tile 1-26. Nothing else.

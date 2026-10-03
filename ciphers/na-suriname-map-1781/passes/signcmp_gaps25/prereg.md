# GAPS25-na-suriname-map-1781 (account-4), 3 Oct 2026 -- pre-registration (pushed before the vision call)

Why: GAPS23's confusion (passes/nota2078_gaps23/confusion.tsv) shows patterned H-letter errors on 2077 against the
2078 Nota: d->c 3, n->m 3, q->a 2 ('dassernes'/'dqssernen' = casserne(n); 'nonteerings' = monteerings; 'nq[g|l]asyn' =
magazyn; 'paqrdestal', 'laborqtorivn'). Working suspicion (not assumed by the rule): readers' [v-tall] is the Nieuw C row
script C, readers' [u-dots] the M row y, readers' x the A row x-with-dots.

Instances (queries_key.tsv, 171): every 2077 token whose reader code the key reads d (v 18, w 3, [v-tall] 9, y 1),
n (l 35, [h-loop] 31, [u-dots] 17) or q (x 13), and the look-alike partners reading a ([delta] 40, p 4) or c ([thorn]
0); no 2077 code reads m (the M row's sign is a reference tile only).

Crops: sign-level boxes were attempted (passes/signcmp_gaps25/locate.py on strips cut by
`python3 tools/iiif_lines.py --image ciphers/na-suriname-map-1781/images/2077_legend_native.jpg --out
ciphers/na-suriname-map-1781/passes/signcmp_gaps25/strips --prefix s77 --columns 50:2400 --centres
93,208,306,478,581,696,796,858,943,1054,1152,1269,1392,1487,1593,1629,1690,1735,1850,2021 --top-margin 25
--bottom-margin 25 --lines-per-crop 1 --max-width 2400 --quality 88`); the width DP did not register signs to tokens
(overlay/2077_L11.jpg: the ruled diagonals join pieces, labels drift 1-3 signs), so a box per instance would put the
wrong sign in front of the reader. Deviation, stated here before the call: the queries are the GAPS19 tools/iiif_lines.py
half-line crops (images/crops_2077_leg, one line per crop) with every target position masked as #k in the line's
reader-code sequence (query_sequences.txt) -- the target's own reader code is hidden, its neighbours are shape names.

Call: one blind Opus call (brief.md). References: blind_refs.jpg, 26 Nieuw Secreet sheet tiles under shuffled labels
(blind_key.json, seed 20261003): D v, D w, C script C, N ij, N l, N h, M y, Q cross, A delta, A p, A x-with-dots and
15 distractor rows. No values, no decode, no repo file but the named ones.

Rule (per instance): settled = best_conf >= 0.6, located = sure, and the second choice is a tile of a different value
(or NONE). Unsettled -> no change.
- Settled on the key's own value: no change (already H).
- Class rule: a reader code class whose settled instances number >= 3 and of which >= 2/3 settle on one value other
  than the key's -> every settled instance of that class on that value gets an exception at grade H ("sheet's own sign
  identified by image", as GAPS21); the class's unsettled instances get that value at grade M; the class's settled
  instances on the old value stay. Codes are not changed in key_period_codes_nieuw.tsv (2077 only; GAPS21 precedent).
- A settled instance on a different value in a class that fails the class rule -> exception value set, grade M.
- Existing C exceptions (GAPS23/24) are not overwritten.
Then: tools/decode_key.py --check exit 0; GAPS23's registered gate re-run unchanged (passes/nota2078_gaps23/score.py,
same pairs, seed, draws) and reported old vs new pooled A and per pair, beside H/C/M/U.

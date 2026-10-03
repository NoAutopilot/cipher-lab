# GAPS45-na-suriname-map-1781 (account-4), 3 Oct 2026 -- pre-registration (pushed before the vision call)

Why: 2077's reader code [u-dots] (17 tokens) decodes n at H, keyed "by shape name" only (key_period_codes_nieuw.tsv:
"Nieuw N row ij with dots"). GAPS23's 2078 parallel shows n->m 3 times on it, and GAPS37 saw the same on "nag·syn"
(magazijn). The Nieuw key's M row is "y (small loop above)" and its N row "ij / y with dots": two similar signs. No 2077
cipher token reads m, so there is no same-hand cipher m exemplar. VERIFY4 (ce81bd69) named this step: use 2077's own
plain-written letters as same-hand references.

Instrument (the GAPS37 form, 34dbb366): ONE blind Opus vision call on the GAPS19 half-line crops
(images/crops_2077_leg/leg77_<Lnn>_s1/s2.jpg, 13 lines). All 17 [u-dots] tokens are masked as #k in their lines' reader-code
sequences (query_sequences.txt). 15 same-hand references are single letters masked inside 2077's plain words: lowercase m
4 (Ambagts, Kamer, the label m, materialien), lowercase n 6 (den, van x2, berging, nog, een), y-with-dots 5 (huÿs,
bootehuÿs, Vaartuÿgen, gevangenhuÿsen, Smeederÿ). The reader is told no value and no hypothesis and is not told which #k are
cipher and which are references. Plain script is legible, so the references are NOT blind (the reader can read "Ka#7er");
the 17 cipher tokens are. The reader sorts all 32 into letterforms and, per query, reports the mark above the body
(dots / loop / none / unclear). Key: queries_key.tsv (not shown to the reader).

Gate (leave-one-out over the 15 known references, run first by apply.py): (a) every reference located = sure and
form_conf >= 0.6; (b) the 4 m references share one form Fm; (c) the 6 n references share one form Fn != Fm; (d) the 5
y-dots references share one form Fy, different from Fm. LOO: for each reference, removing it leaves (b)-(d) satisfied by
the rest and it falls in its own class's form. If the gate fails: "non-test (same-hand plain-letter gate failed)", no
value is changed.

Rule (only if the gate passes), per [u-dots] token, located = sure and form_conf >= 0.6:
- form = Fm -> m at H ("sheet's own sign identified by image against same-hand plain m");
- form = Fy or Fn -> n stays (H, now image-supported);
- any other form (a cipher-only form) or below the bar -> unchanged.
If >= 12 of 17 fall in a cipher-only form, the call is logged "plain references cannot settle n|m: the cipher sign
matches no plain letterform" (a non-result, not a negative), no change.
The mark-above column (dots vs loop; the key's M sign has a loop, its N sign dots) is reported per token, NON-GATING.

Context expectation, written now, NON-GATING (descriptive only, not used to change any value): reading the decoded words,
16 of 17 [u-dots] sit where Dutch wants m (gouvernement, magazijn x7, materiaal, watermolen x2, monteerings, kamer, makers,
mascines, and L09:11 'co?iesean'); L10:7 ('tinn?e?en') and L12:37 ('atoriv?vo') are unclear. Context is a crib-type
argument (grade I at most) and is not applied here.

Then: tools/decode_key.py --check exit 0; GAPS23's registered gate re-run unchanged (score.py and nota2078.tsv
byte-identical copies of passes/nota2078_gaps37/ in passes/nota2078_gaps45/), old vs new pooled A, beside H/C/M/U.
A reading change is carried into AUDIT.md item 4 as a propagation note (re-class stays a separate verifier's).
Vision calls: 1 (Opus). Requests: none (disk only).

# GAPS37-na-suriname-map-1781 (account-4), 3 Oct 2026 -- pre-registration (pushed before the vision call)

Why: GAPS21 and GAPS29 failed to separate 2077's reader code g into the Nieuw key's two values (G-row 9 = g, L-row tailed g
= l) against the inv. 86 sheet tiles (cursive sheet vs calligraphic legend hand); that instrument is [retired]. This step
uses same-hand references: the four C-known 2077 g tokens (exceptions_nieuw_image.tsv, GAPS23/24): L06:4 = g (query #12);
L10:61, L12:26, L12:48 = l (#22, #27, #28).

Leave-one-out adapted (stated before the call): only one g exemplar exists, so a plain LOO on L06:4 would leave no g
reference. The call is therefore *leave-all-out*: one blind Opus call sorts all 46 masked g instances (incl. the four)
into letterforms with no reference labelled and no value given (brief.md, query_sequences.txt, GAPS19 half-line crops
images/crops_2077_leg). The four C-known tokens are scored as held-out items after the call; the reader never sees them
marked. This is stricter than LOO (no anchors shown at all) and a uniform-answer reader fails it.

Gate (run first, on the four C-known only): all four located = sure and form_conf >= 0.6; #22, #27, #28 in one form (Fl);
#12 in a different form (Fg). Otherwise the step is logged "non-test (same-hand gate failed)", no value is changed and
no exception is written.

Rule (only if the gate passes), for the 42 other g tokens: form = Fl, form_conf >= 0.6, located = sure -> l at H ("sheet's
own sign identified by image against same-hand C anchors"); form = Fg under the same bar -> g at H; anything else (a third
form, conf < 0.6, approx) -> unchanged (g|l, M). The four C rows are not overwritten. Codes in key_period_codes_nieuw.tsv
are not changed. Class-collapse note: if the gate passes but >= 41/42 land in one form, apply as above but report it.

[u-dots] / n->m (3 tokens): not included. 2077 has no code that reads m, so no same-hand m exemplar exists; a same-hand
call cannot test n vs m. Logged, unchanged.

Then: tools/decode_key.py --check exit 0; GAPS23's registered gate re-run unchanged (passes/nota2078_gaps25/score.py and
nota2078.tsv byte-identical copies in passes/nota2078_gaps37/, same pairs, seed, draws), old vs new pooled A per pair,
beside H/C/M/U. A reading change is carried into AUDIT.md item 4 (re-class stays a separate verifier's).
Vision calls: 1 (Opus). Requests: none (disk only).

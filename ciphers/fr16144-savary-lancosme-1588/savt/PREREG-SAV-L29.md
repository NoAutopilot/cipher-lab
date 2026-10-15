# PREREG SAV-L29 (LANE DEFAULT-A2-1410-15, account 2), written 15 Oct 2026 14:3x UTC by date -u, before any image is fetched or read

Job: c251 (f.123r) margin gloss line 29 + a firmer read of gloss lines 17-28, on one-line crops.
- Image: one openapi.bnf.fr region, c251 pct:0,59,30,21 at max (gloss lines ~17-30), scratch only; at most 3 requests in all.
- Crops: `tools/iiif_lines.py --image <region> --out <dir> --prefix g251c --lines-per-crop 1 --overlap 30 --debug`, debug overlay checked.
- Passes: two blind Sonnet subagent calls on the same crops (pass A3 top-down, pass B3 bottom-up), no prior reading of these lines shown
  (neither SAV-GLOSS2's nor SAV-L14 reader B's), then one reconcile by this Opus session against the region.
- Line grade rule (same as SAV-GLOSS/SAV-GLOSS2): A+B when both passes support the line's main words; A or B when one pass only; R when
  only the reconciler reads it. Every word grade M (eye read of a period gloss, no key applied).
- "Firmer" is declared before reading as: a line where the new pair agrees on at least one more content (non-function) word than the
  SAV-GLOSS2 row for the same line; counted per line and reported, with the line ids matched by position against SAV-GLOSS2's rows.
- After reconcile only: compare against SAV-L14 reader B's L16-L29 ("pour sa mere ... se saisist de luy") and report agreements; this
  comparison is a report, not a gate.
- No alignment, no key edit, no print search. Output appended to savt/gloss_c251_c252_reconciled.tsv; passes in savt/gloss_c251_passA3.tsv,
  savt/gloss_c251_passB3.tsv.

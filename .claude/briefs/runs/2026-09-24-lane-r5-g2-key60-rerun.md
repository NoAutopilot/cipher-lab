LANE R5 WORKER G2 -- NEVERS fr.3985 f.176: calibrated re-run with the key no.60 atlas, one leaf, judge first (Opus, cap $8; disk only).
Common rules: .claude/briefs/runs/2026-09-24-lane-r5-common.md (note its PROCESS proposal 4: a judge output before any further leaf).
Read tools/keys/key60_atoms.md (G's atlas section: this hand writes +o like 'to', 20 like 'ro', ++ like 'll', a looped f for phi, and
does not separate X+ from X++), tools/keys/key60_atlas/ (atlas.tsv, contact sheet), ciphers/fr3985-nevers-revol-1593/NOTES.md (F1, G).
Leaf: f.176 only (2 Sept 1593, 12 short cipher runs inside clear text; images on disk from F1). No fetches.
1. Pass A (you) against the atlas, not the raw key tags; one blind Sonnet pass-B subagent given the atlas contact sheet and the five
   hand-specific confusions above, writing its TSV to disk; tools/reconcile_passes.py. Report agreement.
2. Whatever the agreement, apply key60 (tools/decode_key.py, decode.json) to the agreed rows and run tools/judge_plaintext.py on the
   decoded runs (French, 1593 spelling) and on a matched control (the same number of runs of French from the clear text of the same leaf,
   enciphered with key60 and decoded back through the same pipeline with the observed disagreement rate as noise). Report both judge
   outputs.
3. Judge PASS and agreement >= 80% -> settle disagreements on the image, --check exit 0, grades, NOTES, ROOM "for LANE V5: ... reading
   ready (H h M m I i)". Otherwise -> NOTES section and ROOM "for LANE R5: f.176 atlas re-run agreement x%, judge FAIL/PASS", stop.
Cost stop rule as the common rules. NOTES.md section "Calibrated re-run f.176 (24 Sept 2026, LANE R5 G2)". Rule 10 wording.

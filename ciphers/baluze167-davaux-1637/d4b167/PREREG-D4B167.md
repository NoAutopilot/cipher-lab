# PREREG D4-B167 (account 4 worker, for LANE DEFAULT-account-4-20261008-0740), written 8 Oct 2026 09:3x UTC before any pass

Same token forms, same norm.py (d1bal170/norm.py), same split statistic and gate as d1bal170/PREREG-D1BAL170.md and
d1bal170b/PREREG-D1BAL170B.md. Prompts: d4b167/prompt_pass{A,B}_b170f229{r,v}.txt (= d1bal170 prompt, one image per line).
Passes: Sonnet subagents, blind, crops + d1bal167/exemplar_sheet.png only, one call per page per pass (4 calls):
 f.229r passes A, B on images/crops/b170f229r_L03-L14, L16-L18, L20-L21 (17 lines);
 f.229v passes A, B on images/crops/b170f229v_L01-L06, L12-L15 (10 lines).
Split statistic: 1 - agree/aligned columns from `tools/reconcile_passes.py` (no --keep-plain) on norm.py output, cipher tokens only,
marks included; A vs B per page. Agreement, not accuracy (TRANSCRIPTION.md).
Gate: split <= 0.10 on a page -> reconcile disagreements.tsv only. Split > 0.10 -> reconcile by eye from the crops (1 unit, as the
brief prices it) and record the split; the reconciled sheet is then a provisional transcription whose disputed marks are graded M.
Decode (brief: "decode with the folder's key"): reconciled tokens through key.tsv via decode_key.py, a new job section in decode.json
so the committed f.157/169 reading is untouched. Grades: H only for an unmarked-uncertainty token whose key row is H; any token with ?
or a reconciled disagreement -> M; letter signs graded by shape->letter (d1bal167 exemplars: gam u, h n, w e, S s, c x, p s, ll l,
hook s, y+ r single-letter shapes -> per key L:x row; u4 (t/n), loop (u/i/d), 4u (a/d) and unlisted shapes -> M at best).
No language gate is claimed on the f.229 decode; a fragment-level reading only (rule 4a depth is the verifier's).

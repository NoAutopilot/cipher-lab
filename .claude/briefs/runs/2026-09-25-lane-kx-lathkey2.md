LANE KX job 3d: KX-LATHKEY2, transcription and period key for ciphers/colbert26-lathuillerie-1644, successor to KX-LATHKEY
(interrupted at $44 after 61 min without a push; its two transcription passes were lost). Sonnet. Stall alarm $8, and this
time it binds: at $6 push what you have and stop at $8 whatever the state. Parent: LANE KX orchestrator
session_01JPoYAFvVfraJibxQdQfrqp. Read .claude/briefs/runs/2026-09-25-lane-kx-COMMON.md first; it binds.
ROOM role: "LANE KX worker KX-LATHKEY2 (Sonnet, <your session id>)".

On disk already (do not refetch the canvases): images/crops/canvas{20,21,26,27,30,32,33,35,36,39,40,47-51,54-56,62,63}_full.jpg
(native-res, 2400 px), leaves.tsv (gloss column filled: every cipher-bearing canvas carries a second hand's interlinear
plaintext over most numeral groups). Folder is 28 MB: keep it under 30 MB (put line crops in images/lines/ at <= 1400 px
wide, JPEG q70, and delete intermediates).

Files you may write: ciphers/colbert26-lathuillerie-1644/ only (NOTES.md new section "KX-LATHKEY2 (25 Sept 2026)"), ROOM.md.

Work leaf by leaf, cheapest first, and push after EACH leaf (python3 tools/room.py --push <paths>):
1. For one canvas: cut only the lines that carry numeral groups into line crops (tools/iiif_lines.py can work on the local
   file, or PIL); transcribe each cipher group with the gloss written over or beside it, yourself, from the line crops.
   Row per group into ciphertext.tsv: canvas, line, idx, token (as seen, never repaired), gloss (as seen; '' if none;
   '?' if illegible), context_before, context_after (two or three clear words).
2. Second pass: one Sonnet subagent per ~5 canvases (at most 2 at once), sees only the line crops and the column spec,
   never your rows; write passB.tsv. Reconcile with tools/reconcile_passes.py or a short script; settle disagreements
   from the crop yourself; disagreements.tsv.
3. key_period.tsv from the reconciled rows: code, value (from the gloss), grade C when the gloss is legible and consistent
   across occurrences, M when it is not, count, canvases, note (conflicting glosses listed). A code with two different
   glosses is a homophone/polyvalence question: list both, do not choose.
4. Report: tokens transcribed, pass agreement %, distinct codes, codes fixed by the gloss (C), unglossed tokens, and the
   design the table suggests (single numbers for letters vs syllables vs words; letter-with-mark codes like zz, w').
No decoding beyond the gloss alignment, no reading, no novelty wording. Hosts: none (all from disk).
Final paragraph first line: "T tokens on L leaves, agreement A%; key_period.tsv K codes (C c, M m); U tokens unglossed".

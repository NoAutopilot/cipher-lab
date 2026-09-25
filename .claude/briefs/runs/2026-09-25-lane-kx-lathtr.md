LANE KX job 3e: KX-LATHTR, finish the transcription of ciphers/colbert26-lathuillerie-1644 and write its spec. Sonnet.
Stall alarm $10 (the orchestrator interrupts at $15). Parent: LANE KX orchestrator session_01JPoYAFvVfraJibxQdQfrqp.
Read .claude/briefs/runs/2026-09-25-lane-kx-COMMON.md first; it binds. ROOM role: "LANE KX worker KX-LATHTR (Sonnet, <your session id>)".

State: canvas 20 is transcribed (ciphertext.tsv, single pass, 1ef58c1). KX-LATHKEY2 established the interlinear notes are
topical paraphrases, not a decipherment (NOTES.md "KX-LATHKEY2"): no period key; the notes are cribs. Read that section.
So this is now a cryptanalysis target, and it needs (a) a complete two-pass transcription and (b) a spec, before any test.

Files you may write: ciphers/colbert26-lathuillerie-1644/ (ciphertext.tsv, passB.tsv, disagreements.tsv, images/lines/,
NOTES.md new section "KX-LATHTR (25 Sept 2026)"), specs/colbert26-lathuillerie-1644.json, ROOM.md. No Gallica: crops are
on disk (images/crops/canvas{N}_full.jpg). Folder must stay under 30 MB.

Git: stage your paths and run `python3 tools/room.py --push <paths>` WITHOUT committing first (room.py commits and pushes;
after a manual commit it says "nothing staged" and pushes nothing -- KX-LATHKEY2's flag). After each push, check
`git fetch -q origin main && git log origin/main -1 --oneline` shows your commit.

1. For each remaining canvas (21, 26, 27, 30, 32, 33, 35, 36, 39, 40, 47, 48, 49, 50, 51, 54, 55, 56, 62, 63), in that
   order: cut the cipher-bearing lines to images/lines/ (<= 1400 px wide, JPEG q70); transcribe into ciphertext.tsv with
   the same columns as canvas 20 (canvas, line, idx, token, gloss, context_before, context_after); token as seen, never
   repaired; gloss = the second hand's note nearest the run, verbatim, only on the run's first token. Push after every
   canvas.
2. Second pass: after every 5 canvases, one Sonnet subagent (never more than 2 at once) transcribes the same line crops
   blind (it sees only the crops and the column spec) into passB.tsv; include canvas 20. Compare per line with a short
   script (or tools/reconcile_passes.py if the columns fit); settle each disagreement from the crop yourself, record it in
   disagreements.tsv, and correct ciphertext.tsv. Report the agreement %.
3. Spec: specs/colbert26-lathuillerie-1644.json on the pattern of the other specs/*.json (read specs/README.md): source
   (BnF Mélanges de Colbert 26, Gallica btv1b10035069t, canvases, date read), alphabet (every distinct token, counts),
   design notes (mixed nomenclator: 1-3 digit numbers, single letters, letters with marks; inline with clear French),
   constraints (the notes as topic cribs with their canvas/line; the clear French context either side of each run),
   cheap tests in order (first: frequency/homophone structure vs the key_1646 / key_brienne_1647 / fr5160 key_1659 designs
   of the same office, with a matched synthetic control of the same length and symbol count; second: crib placement of
   the notes' named entities -- Suede/Suedois, Dannois, Prince d'Orange, Naples -- as nomenclator words), and a judge block
   (language fr). Leave cheap_test_done empty: do NOT run any test.
Report what was found and where it was not found; do not classify novelty. Final paragraph first line:
"T tokens on L canvases, S distinct signs, pass agreement A%; spec written".

# PREREG TXE-R: fr.3252 f.117r re-transcribed with today's pipeline (9 Oct 2026, written 08:3x UTC by date -u, before any crop or read)

Job TXE-R, LANE TX-ENGINEER round 3, Amendment 2 guard 3 (brief `.claude/briefs/runs/2026-10-09-account4-txe-r.md`,
`benchmark-tx/PREREG-txeng-3.md` "Decision"). Worker account 4, Opus 5.5. Cap 15, box 150 min. Disk only.

Gates run before this file (pasted in RESULTS-TXE-R.md):
- `tools/intake_gate_check.py birago-fr3252-1571-72` -> partial, pass.
- `tools/prior_work.py` (warn-first): no items.tsv row `f117r`; run with `--item-spec 'shelfmark=BnF fr.3252;folio=117r;date=1572-03-13;sender=Birago;recipient=Nevers'`
  -> verdict plaintext KNOWN (the only KNOWN hold is the f.36-37 clerk gloss, NOTES.md:64, a different leaf), step LEAD (our own
  earlier work on this leaf, which this job re-does by design). Exit 2, warn-first; not a block.

## 1. Crops (no model)
Source on disk: `ciphers/birago-fr3252-1571-72/images/f117/src_ark_12148_btv1b9060232m_f118_4380_1400_3150_1300.jpg`
(3150x1300, the committed native region of canvas 118). Centres: the eye-set centres of NEVBIR-3252-B (the profile detector
drifted from line 6 then), same segmenting as the committed crops:

    python3 tools/iiif_lines.py --image ciphers/birago-fr3252-1571-72/images/f117/src_ark_12148_btv1b9060232m_f118_4380_1400_3150_1300.jpg \
      --out ciphers/birago-fr3252-1571-72/images/f117_txer --prefix f117r \
      --centres 103,223,347,462,580,702,815,944,1062,1210 --max-width 1100 --overlap 60 \
      --band-extent 0.1 --mask-neighbours --overlap-note --note-scale 2 \
      --check-boxes ciphers/nevers-birago-fr3251-1572/atlas/signs.tsv --check-page f117r --debug

(atlas boxes are geometry only, in the region's own coordinates; no label is read.) The debug overlay is checked by eye;
`--follow-slope 300 --only-lines <n>` is re-run only for a line the overlay shows leaving its band. Readers get 2x LANCZOS
copies (gitignored, regenerable), and the `crops_note.md` line verbatim.

## 2. Two blind passes (Opus 5.5)
Readers A and B, each a separate subagent, the folder's own `harvest/f117/blind_pass_brief_f117.md` and
`sign_sheet_blind_1572.png`, the generated crops note in place of the brief's hand-typed overlap sentence, value-blind (no key,
no decode, no other pass, no atlas file). A reads L01-L10 in order; B reads them in reverse. One call per reader if the 30
crops fit, else two calls of 15. Output `harvest/f117/txer/passA.tsv`, `passB.tsv`, committed and pushed before reconciling.

## 3. Reconcile and adjudicate
    python3 tools/reconcile_passes.py harvest/f117/txer/passA.tsv harvest/f117/txer/passB.tsv --crops images/f117_txer --out-dir harvest/f117/txer/rec
One Sonnet third-reader call on the disagreements (and both-L rows) with agreed neighbours as landmarks, value-blind,
crops + sheet only. New ciphertext `harvest/f117/ciphertext_f117_txer.tsv` (line, pos, sign, conf), never overwriting the
committed `ciphertext_f117_top1.tsv`. **conf rule, fixed now:** H where A and B agree on the sign (neither L); M where they
agree but either says L, or where the third reader settled a split by choosing one of the two passes' signs; L where the
third reader chose neither or was unsure. X_/? signs stay as read (they decode U).

## 4. Decode
`harvest/f117/decode_txer.json` = job 1 of `../nevers-birago-fr3251-1572/harvest/tx_decode/eye/apply/decode_apply.json`
with only the ciphertext and output paths changed (same key `harvest/key_1572_sheet.tsv`, same exceptions
`exceptions_apply_f117.tsv`, same grade switches):

    python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --config ciphers/birago-fr3252-1571-72/harvest/f117/decode_txer.json

Caveat fixed now: the exceptions are keyed by (line, pos) of the committed transcription; where the new transcription shifts
positions in a line, an exception lands on another sign. So a secondary decode without the exceptions file is also reported
(same config minus `exceptions`), and every grade change is listed by **aligned** position (per line, new vs committed
signs, `difflib.SequenceMatcher`), not by raw index. The primary number is the brief's (with exceptions); if the two
disagree on the S count by more than the number of exception rows that land on a shifted line, both are reported and the
smaller S count is the one carried to the gate.

## Gates
(a) err_2reader = share of aligned positions (reconcile_passes alignment, gaps counted) where A and B differ; reported beside
    the folder's earlier figures: f.117r NEVBIR-3252-B two Sonnet readers 0.75 agreement (err 0.25), and the brief's 0.56
    (which NOTES.md:135-138 shows is f.47r L01-04, not f.117r; reported as such).
(b) tokens by grade vs the committed 190 S / 63 M / 26 U (RD7), also beside the current 217 S / 36 M / 26 U (D2-B117KAPC);
    "N more tokens at grade S" = new S - 190; list of aligned positions whose grade changed, with new values.
(c) power: HYPOTHESES D2-B117KAPC curve (seed 1: 18/20 at 0.126, 16/20 at 0.183, 6/20 at 0.25). If the new err_2reader is
    <= 0.183 the curve licenses (>= 16/20). If it lies between measured points above 0.183, run
    `decode_control.py <new ciphertext as recon format> --map map_printed.json --corpus fr --err <new err> --seed 1` (200 shuffles,
    20 windows, as KAPC) and license only at >= 16/20 with rank 1. Otherwise the gain is reported as unlicensed.
(d) `python3 tools/judge_plaintext.py specs/birago-fr3252-f117.json --file <new reading, letters only>`, against the committed
    line FAIL -1.224 (real_p05 -0.899). Not worse = score >= -1.224.
A gain is "the key now licenses N more tokens at grade S" only when (c) licenses and (d) is not worse; else "no licensed change".
No grade above S. The committed reading and RD7 stay as they are.

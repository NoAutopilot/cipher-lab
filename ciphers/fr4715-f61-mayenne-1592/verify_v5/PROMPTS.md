# VERIFY-F61-V5 prompts -- WRITTEN BEFORE THE CALLS (29 Sept 2026, verifier session_01GgtGry5o3rrdf23A11VKhT)

Six Opus vision calls, each a fresh subagent that has seen nothing of the campaign. Crops are re-cut this session from fresh
natives (Gallica btv1b9060633d canvases 327 = f.176r, 329 = fol. 177r; one request each, family/requests.log) by the runner's own
recipes (family/sheets/f176r_full/README.md, f177r_full/README.md), into the verifier's scratch (not committed; regenerate the same way).
Atlas: verify_v5/atlas_blind.tsv (the runner's atlas with the one letter-value remark removed).

Sample (fixed now, before any call): f.176r rows **L06-L11** and **L28-L33** (12 of 47 rows, about 790 signs); the clear lines of
fol. 177r that the runner's DP places opposite them (verify_v5/rowmap.py: L06-L11 -> clear L06-L11; L28-L33 -> clear L24-L28), read
with one line of margin each side: **fol. 177r L05-L12** and **L23-L29**.

Calls:
- S1P, S1Q: two independent sign passes of f.176r L06-L11 (identical prompt, output P / Q) -> verify_v5/passes/f176r_signs{P,Q}_L06-L11.tsv
- S2P, S2Q: the same for L28-L33 -> verify_v5/passes/f176r_signs{P,Q}_L28-L33.tsv
- R1: blind read of fol. 177r L05-L12 -> verify_v5/passes/f177r_clearV_L05-L12.tsv
- R2: blind read of fol. 177r L23-L29 -> verify_v5/passes/f177r_clearV_L23-L29.tsv

Sign prompt (rows and output path substituted):
"You are a blind transcriber of a 16th-century cipher manuscript. Use only your file/image reader on the files named here and the
Write tool for the one output file; run no command or script, open no other file. Read first the shape atlas
ciphers/fr4715-f61-mayenne-1592/verify_v5/atlas_blind.tsv (code and shape). Then list every CIPHER SIGN, left to right, in the
cipher rows ROWS, each given as four overlapping crops s1..s4 left to right (/tmp/claude-0/-home-user-cipher-lab/8f3f849a-1d2b-5d29-8183-8ea014e99b4f/scratchpad/f176/f176_Lnn_s1.jpg ... _s4.jpg); neighbouring
crops share about 120 px, marked by red ticks at the top edge -- list a sign in an overlap ONCE, in the earlier crop. Parts of the
rows above and below may intrude at the top or bottom edge: list only the row centred in the crop. Code every sign with the atlas;
EBR_A vs EBR_B: decide by the hairline diagonal (present = EBR_A); use OTHER with a shape note for a sign matching none; if between
two codes give the best and put 'alt CODE' in the note. A clear word standing in a row: sign = PLAIN, word in the note. A sign
struck through: code it and note 'struck'. Confidence h/m/l. Never guess any letter of the alphabet for a sign: shapes only.
Write a TSV with the Write tool to OUTPUT, header exactly: line<TAB>pos<TAB>sign<TAB>conf<TAB>segment<TAB>note ('pos' counts from 1
along the whole row). Reply only with the number of signs per row."

Clear prompt (lines and output substituted):
"You are a reader of 16th-century French secretary hand. Use only your file/image reader on the files named here and the Write tool
for the one output file; run no command or script, open no other file. Read the manuscript lines LINES, each given as three
overlapping crops s1..s3 left to right (/tmp/claude-0/-home-user-cipher-lab/8f3f849a-1d2b-5d29-8183-8ea014e99b4f/scratchpad/f177/f177_Lnn_s1.jpg ... _s3.jpg; neighbours share about 120 px -- read a word in an
overlap once). Parts of the lines above and below may intrude: read only the line centred in the crop. Transcribe each line exactly
as written, letter by letter: period spelling, no modernising, abbreviations not expanded (superscripts as '^'), '?' for an illegible
letter, [brackets] round an uncertain word. Do not guess what the text says beyond what the letters show. Write a TSV with the Write
tool to OUTPUT, header exactly: line<TAB>text<TAB>conf (one row per line, conf h/m/l). Reply only with the number of lines."

Scoring, fixed now (verify_v5/align_v5.py, the verifier's own global DP, not the runner's f61crib.align):
- consensus of P and Q per row (difflib equal blocks only); clear folded by family/h170_gate.fold.
- **Leave-class-out (LCO):** for each class X proposed by key_period_f176.tsv, the anchor key is key v4's letter sets with X removed,
  so X's letter is set by the alignment of its neighbours, never by v4; letters opposite X are counted. Controls: the same with the
  wrong clear fr.3984 f.184r (same N), and with 50 anchor keys whose letter sets are permuted across classes (seeded).
- Endorse-for-this-leaf gate per class: top letter under LCO equals the runner's proposed letter AND its share of X's aligned
  positions >= 0.5 AND the wrong-text share of that letter at X < half the true share. Run on the runner's passes/clear (all rows) and
  on the verifier's sample (P/Q/R) separately; agreement reported row by row.
- f.61 / f.108r / f.108v transfer: per class, v4 with that class narrowed to the proposed letter vs 200 shuffled-value controls (the
  class narrowed instead to a random letter drawn from the family's letter frequency, seed 29), counting matches to the known letters
  at that class's positions only. Endorse for key v5 only if leaf-level (above) passes AND no known-answer leaf in f.61's or f.108's
  hand contradicts it below the shuffled-value p05.

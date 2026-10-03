# NV05E pre-registration (committed before any pass is read or scored), 3 Oct 2026

Leaf: BnF fr.15575 f.228 (Gallica btv1b90637788 canvas f235, right page; foliation "228", struck "234").
What the layout look showed (one 1600 px overview + one 1600 px rendering of the crop source region, by the worker,
before this file): the recto is almost all digit cipher, ~47 lines, codes written run together ("4873 4689"), and it
carries a faint **period interlined decipherment** above each cipher line (seen over L01-L05). The worker read, while
placing crops, the gloss words above L01 ("tan tarde ... por los despachos a la fin han acavado de llegar todos los
que") and L02 ("partieron antes que el de 7 de otubre ... por la mar con don Juan"), and L01's opening "80.80.23" in
the cipher. Nothing else was read before this commit.

Consequence: the leaf's plaintext exists on the leaf (H, the clerk's gloss). This job's decode is therefore scored
the way NV05C scored its fr.3641 control: decode against the gloss, with a value-shuffled control. It is a second
known-answer test of key no.54 and a reading aid, not a recovery of unknown plaintext.

## Units and stop rule
Per pass ~USD 1.5 (brief). f.228 has ~47 lines (~12 four-line batches); one batch costs 3 Sonnet reads (cipher A,
cipher B, gloss G) + 1 reconciliation = 4 units ~USD 6, which with session overhead is about 80 pct of the USD 8 cap.
Scope fixed now: **batch B1 = f.228 L01-L04 only** (crops f228_L01..L04, segments s1-s3). No second batch, and f.233
(canvas f240) gets no transcription in this job: its overview shows it is also fully cipher with a faint interlined
decipherment, and its address panel is on the facing page; it is described from the overview only.

## Decode rule
Key: ../key_no54.tsv as committed by NV05B, the 95 coded syllable rows (codes 10-99), copied unedited to
key_syllabary.tsv (as NV05C). Codes outside the syllabary and nomenclator groups absent from the key are U, never
guessed. Tokenisation as NV05C: a digit run is split into 2-digit codes from the left; an odd final digit is a
single-digit token (header letter sign); every non-digit sign is its own token. `tools/decode_key.py` with a
decode.json in this folder; `--check` exit 0; `--split-check` listed.

## Statistic, control and gate (known-answer, as NV05C)
S = share of scored 2-digit tokens whose decoded letters all fall in the per-line LCS alignment with the clerk's gloss
of that line, both normalised (lower case, accents off, letters only, j->i, v->u, y->i; gloss abbreviations expanded
by NV05C's fixed table only: q/q~ alone -> que, qs -> ques, VM/V.M./vm -> vuestramagestad, S.M./sm -> sumagestad,
duq/duqz -> duque). Control: the same S with values shuffled among the 95 coded rows, 1000 draws, seed 1. Gate:
PASS iff S > control p99 AND S >= 0.60. Scored with ../control_fr3641/score_control.py's statistic (imported, not
re-derived).

## Language judge (brief step 2; reported, secondary to the known-answer gate)
`tools/judge_plaintext.py judge_spec.json --file <decode letters>`, corpus es17 (Cervantes, Quevedo; nearest on disk,
not 1590s-matched, literary not epistolary). Controls through the same judge: (a) value-shuffled key decode of the same
tokens, 200 draws, seed 2, reporting how many PASS; (b) the decode of the target's tokens in shuffled order (seed 3,
one draw per line, 20 draws). A PASS on (b) voids the judge as a gate here (ARM-C1). Since the U tokens (letter
signs, code words) are dropped from the judged string, the judge sees syllable fragments only; a FAIL on the real
decode is then expected and is not a negative on the key (the known-answer gate above is the test).

## Transcription
TRANSCRIPTION.md: crops via tools/iiif_lines.py (command in NOTES.md), 2 blind Sonnet passes of the cipher tokens
(A, B), 1 Sonnet read of the gloss (G), each one call on the B1 crops; reconciliation by the worker on the crops,
disagreeing cipher tokens only, settled from the image **before** the worker opens G's output. err_2reader = tokens
where A != B / aligned tokens (agreement, not accuracy).

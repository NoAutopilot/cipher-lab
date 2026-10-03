# GAPS39 pre-registration (3 Oct 2026, written and pushed before any reading; clock read 06:37 UTC)

Step (GAPS33 Verdict): hand-locate print for the 6 occurrences GAPS33's locate rule dropped (gaps33/dropped.tsv) and
read them with GAPS33's protocol plus a fresh 6+6 control, to bring 139/149 to n=4.

Location (`gaps39/hand_locate.tsv`, fixed before any reading, by the worker from the cipher decode and the print only,
with no answer in view): 5 of 6 band occurrences located (142 x1, 149 x1, 139 x1, 150 x2). 140 at 05810_p5_L08:1 is
dropped: the cipher leaves the print after "grand bruit" (print "bruict par deça quant à la difficulté", cipher "le
temps et la saison"), so there is no single print spot; its two C-null neighbours (138, 122) are dropped with it.
Note for readers' answers: at 5811 Thiel ("graue et s n [?]") and 5810 "peyne [?] hors" the cipher and the print do
not run word for word; that is visible to the readers in the window itself.

Control (fresh, none of GAPS33's 67 kept items): 6 C null (127, 130 hand-located from GAPS33's dropped list; 134, 124,
126, 137 by GAPS33's own locate rule, seed 39, one per code) and 6 C letter (29, 38, 2, 32 hand-located from the
dropped list; 104, 37 by rule). The hand-located controls match the band items' location method (rule 3, design).
`gaps39/build.py` (deterministic) wrote `windows.txt` (17 items, shuffled seed 39) and `answers.tsv` (never shown).

Readers: as GAPS33 -- two blind Opus 5.5 text-only subagent passes (windows pasted into the prompt, told not to open
any file), per item NULL or one letter with confidence high/low; one Opus 5.5 reconciliation pass that sees both
passes and the windows (never answers.tsv), one final call per item or SPLIT. SPLIT = wrong in the control, no
observation for a band code.

Gate on the reconciled calls of this run (all three, else nothing is applied and nothing pools):
- G1: C-null called NULL >= 5 of 6.
- G2: C-letter called a letter (class) >= 5 of 6.
- G3: C-letter called NULL <= 1 of 6.
Also reported: the pooled GAPS33+GAPS39 control (31 + 31), whose G3 rate must stay <= 0.316 for the pooled licence below.

Licence (only if this run's G1-G3 pass): GAPS33's and GAPS39's reconciled band calls are pooled (same protocol, same
decode, same readers' model, each run's own control passed). A band code becomes NULL at grade C (class b) iff pooled
>= 4 NULL and 0 letter calls AND no occurrence contradicts names.tsv's observation at the same occurrence (rule 4: a
conflict is logged, never settled by majority). >= 4 calls of one same letter and 0 NULL = an M hypothesis in
HYPOTHESES.md, not applied. At this N only 139 and 149 (3 NULL each in GAPS33) can newly reach 4, and only if their one
new occurrence is called NULL; a letter call on either blocks it. 142 (GAPS33: NULL x3 + letter x1) cannot be licensed
whatever its new call. 150 (no GAPS33 observation) is recorded only.
If a code is lifted: key_full.tsv row with source "GAPS33+GAPS39 local-window reading", readings regenerated,
`tools/decode_key.py ... --check` exit 0, grades counted per rule 4.
No item, prompt rule or threshold is changed after the first reading.

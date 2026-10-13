# PREREG-SYL54-TRY (13 Oct 2026, 10:1x UTC by date -u; account-4 worker for LANE DEFAULT-A4-0935)

Written and pushed before any `--try` score on this folder is computed.

## Question
Does the no.54 mark legend (key_no54_legend.tsv, SYL54-LEG) read in f.228? The legend gives two values for what read as one
caret (s, l) and one dotted n (en, l); the blind mark read of this job (images/fr3995/marks, one Sonnet call) did not separate
either pair (same mark, medium). Context is the only remaining instrument.

## Scope found before scoring (counts only, no decode)
- The 16 marked nomenclator rows (9 circumflex-above, 7 plus-after; 13 distinct codes): none of gi, gue, fum, num, nem, non, nir,
  vur, zus, hom occurs in f.228 L01-L08 (ciphertext.tsv + ciphertext_b2.tsv); 17 (x4) and 87 (x2) and 0 occur only as unmarked
  tokens (17 and 87 are syllabary codes ci/ui in key_syllabary.tsv). So code + modifier has n = 0 for all 16 rows: untestable at
  this N, logged as such, no --try run for them.
- The marks themselves are transcribed as separate tokens: `^` n = 13, `n` n = 15, `+` n = 1. In key_no54.tsv the plain `n` is a
  header letter sign = e (H); the transcription does not record a dot on f.228's n, so f.228 `n` may be the letter sign or the
  dotted-n mark.

## Hypotheses (one --try call each, other hypotheses not in place)
T1 ^=s; T2 ^=l; T3 n=en; T4 n=l; T5 n=e (the key's own header value, the comparison for T3/T4); T6 +=e (n = 1: undecided by rule).
Assumption stated, not tested: a mark transcribed as its own token stands where its added letter is read ("s after" = the token
after its host). The legend's "in the middle" and "between" readings are not modelled.

## Instrument
`python3 tools/decode_key.py ciphers/fr15575-syllabic-1592-95/f228 --try X=V --lm tools/data/es1600 --window 8 --nulls 100`
(es1600 = CODOIN volumes, the nearest era/register Spanish corpus on disk). Statistic, null 1 (shuffled positions), null 2
(random values of V's class), verdict (accept / reject / undecided) exactly as the tool's own --help. Log with
`--try-log ciphers/fr15575-syllabic-1592-95/crossword_log.tsv`.

## Matched control (run first; gate)
Same text, same tool, same settings, in a scratch copy of f228/ whose key_syllabary.tsv drops three keyed H codes of similar n
and a multi-letter value: 23 (de, n 9), 24 (da, n 9), 73 (que, n 9). `--try` each with its true value. Control PASSES if at least
2 of 3 are accepted; plus one wrong-value check per code (23=da, 24=de, 73=lo) of which at least 2 of 3 must be rejected or
undecided (not accepted). If the control fails either part, every T1-T6 verdict is "non-test at this N" and no pair is settled.
The control's value class is syllables (2-3 letters); for the single-letter hypotheses (T1, T2, T4, T5, T6) it is a nearer
class than none, not a matched one: say so in the result.

## Gate for a pair
Caret pair settled to X in {s, l} only if the control passes, X is accepted, and the other is not accepted. Same for the
dotted-n pair over {en, l} (T5 reported beside it). Otherwise "not settled".

## What follows from a result
No key.tsv, key_no54*.tsv or decode.json edit in this job. An accepted value is logged in HYPOTHESES.md as M (CLAUDE.md
MQS-CROSSWORD line: no --try control has passed for a mark-modifier value class). The SYL54-LEG post-hoc 8/9 circumflex -s count
is a motivation only, not evidence for T1.

# PREREG R9-SIENA15 -- no. 15 against key R4764 through a shape concordance (6 Oct 2026, written ~05:52 UTC, pushed before scoring)

Question: is DECODE R4764 ("Cifra con m. Bern(ardin)o Buonins(egni) or(atore) a S. M.tà", Bourdeau's candidate) the key of no. 15
(R4803, Mario Bandini, Dec 1546 / Jan 1547)?

Inputs, fixed now: `transcripts/no15.tok` (232 tokens, from Bourdeau's verified no15v.txt) and `concordance_R4764_no15.tsv`
(variant P = 14 signs given letter values + 6 null signs; variant V = P with the V rows applied, V rows replacing P rows for the same
sign). Value `&` is scored as the letters "et"; doppie values as the doubled pair.

Statistic S2 (order-sensitive): drop null signs; split the stream at every "|" and every sign without a value; inside each maximal
stretch of valued signs, concatenate the values and take the mean it16 bigram log10 probability over all adjacent letter pairs
(`tools/judge_plaintext.py` LANG_CORPORA["it"] = tools/data/it16, 16th-century Italian letters: era-matched to 1546-47; add-one smoothing,
as run_test_no19.py).

Controls (both can change S2 for the target):
(a) 2000 value-shuffled keys: the multiset of values of the valued signs permuted across those signs (coverage, stretches, and value
    multiset fixed; the assignment changes, so S2 changes).
(b) 200 order-shuffled streams: the non-"|" tokens permuted over the non-"|" positions (breaker positions fixed; which signs are
    adjacent changes, so S2 changes).

Gate (per variant): PASS iff p_a = (#(a) >= real + 1)/(2001) <= 0.05 AND real S2 > the 95th percentile of (b).

Validity (positive control, decides whether a miss counts as a negative): 100 it16 passages enciphered under H1 "R4764 is the key":
walk the passage; a doubled pair whose doppia sign has a value is emitted as that sign with probability q; a letter whose value has
valued signs is emitted as one of them (uniform) with probability q, else as a placeholder sign for that letter (stands for the key
homophones the concordance did not match); a null sign is inserted after a token with probability r = 27/(232-27). q is set once so the
mean valued-token count matches the target's (P: 71). Breakers "|" are placed at the target's own breaker positions. Power = share of
passages where the true mapping meets the same gate (500 value shuffles, 100 order shuffles). If power < 0.8 for a variant, a miss in
that variant is logged as a NON-TEST at this N, not a negative (rule 3, R8-SIENA19 precedent).

Not done: no decode is offered as a reading; a PASS would only send the decode to `tools/judge_plaintext.py` and a verifier.
Script: specs/cheap-tests/siena-concistoro-2308/run_test_no15.py (seeded, `--check`).

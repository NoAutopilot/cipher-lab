# PREREG DA1-COL3 (account 1, LANE DEFAULT-account-1-20261007-1440, 7 Oct 2026, written ~15:5x UTC before any pairing or score)

Held-out word-level pairing on c54, c55, c56, c62, c63 (the five Jan-Feb 1648 canvases DA1-COL and DA1-COL2 did not pair). One blind
Sonnet subagent call per canvas on line crops re-cut with the recorded A2-COL17 / R8-COL26 `tools/iiif_lines.py` commands, shown only
the crops, the committed c5456/c6263 *_reconciled.tsv groups (gap marks "|" removed) and gloss, no key, judging horizontal position
only. Reconciliation (the +1 unit) is mechanical only: index ranges inside the row, ordered, non-overlapping; no boundary moved by key
knowledge. Output siblings/word_pairs_col3.tsv.

1. Tested codes (fixed now). TEST, gated: DA1-COL's FAIL-LOWPOWER codes 15 e, 21 t, 29 r, 32 u, 39 e, 54 e, 75 la, 76 e, 77 l, 83 mo,
   85 na, 86 e; plus 30 s and 75 la (PASS on DA1-COL2's pass only), 46 ce (now M) and 31 t (held, data conflict) -- 15 codes. REPORT,
   scored but never gated or demoted: the five codes at C on both passes, 16 se, 20 i, 67 leur, 81 me, 96 que.
2. Statistic: word_da1.py's word-grain positional hit (code j of k slots in a word of L letters predicted at round(j*L/k) +-1, not
   circular), H = hits over the code's occurrences in cleared units. Script `siblings/word_col3.py` (word_col2.py with only units, token
   files, pairs file, code lists and alpha changed; listed in its docstring).
3. Control W (pairing shuffle): within each canvas the gloss words are permuted over that canvas's word spans, 10000 draws, seed
   20261007 + 1440. It moves only the pairing, which is the axis H depends on, so it can differ from the target.
4. Instrument check per canvas (Szembek per-unit lesson): the pre-DA1-COL key_f23 C codes (siblings/key_f23_preDA1COL.tsv) pooled must
   have H > p95 and P < 0.05 in that canvas, or the canvas is not scored. No canvas clears -> NON-TEST, no key change.
5. Gate per TEST code: PASS iff H > p95, P < 0.05/15 = 0.00333 and hits in >= 2 cleared canvases. P_min >= alpha -> UNDERPOWERED;
   FAIL with subsampled positive-control power < 0.5 -> FAIL-LOWPOWER (not a negative).
6. Merge rule. A TEST code that PASSes goes to key_f23.tsv at grade C (note: held-out DA1-COL3), EXCEPT 31 = t: a PASS strengthens the
   sibling-side witness only and 31 stays held as a data conflict with f.23's own gloss (rule 4; not settled by count). A TEST code that
   does not PASS is unchanged (held-out silence is logged, not a demotion). REPORT codes are never changed by this run. Reading
   regenerated with tools/decode_key.py --check; judge output pasted in NOTES.md.
7. Caveat registered now: the anchor_r10 values were chosen by R10-COL26B on the 14 cleared units, which include c54-56 and c62-63, at
   span (containment) grain; these canvases are held out from the word-level pairing (DA1-COL/COL2), not from the value choice. The
   pairing is one pass per canvas; DA1-COL2 measured ~11% of groups under a different word between two passes on other canvases.
8. Stop rule: if after c54-56 (3 calls) the cap or 80% box would be crossed by c62-63, stop, score nothing, write what remains.

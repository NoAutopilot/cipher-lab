# H168 design check (runner 6, 28 Sept 2026) -- pre-registered before any call

Question: is fr.3984 fol. 7r (canvas f14) written in f.61's polyphonic sign design?
Two blind Opus vision calls, identical prompt, one per query image; the reader is not told which query is the target.
- Call 1: `query_C_fr3984_f188r.jpg` (POSITIVE CONTROL: fr.3984 f.188r, a family leaf whose readings are in key v4).
- Call 2: `query_T_fr3984_f14.jpg` (TARGET: fr.3984 f.14 = fol. 7r).
Reference for both: `reference_family.jpg` (f.61 line sheets L03, L05 on top; a strip of fr.3982 f.101r below).

Prompt (verbatim, <QUERY> replaced by the path):
> Two images of 16th-century cipher manuscripts. REFERENCE: <reference_family.jpg>. QUERY: <QUERY>. Ignore ordinary
> handwritten French words; look only at the invented cipher signs. (1) List the 12 most frequent distinct cipher signs in
> QUERY, most frequent first, each with a one-line shape description and a rough count. (2) For each, say YES if a sign of
> essentially the same shape appears among the REFERENCE's cipher signs, NO if not, UNSURE if unclear. (3) List any sign that
> is frequent in the REFERENCE but absent from QUERY. (4) One sentence: same sign system, or a different one? Reply as a
> TSV table for (1)-(2) (rank, shape, count, match), then (3) and (4) as plain lines. No other text.

Gate (fixed now): design MATCH if >= 8 of the query's 12 signs are YES (UNSURE counts as NO). The control must pass the gate
for the target's result to count (rule 3); a control FAIL makes the test a non-test and the design question goes back to eye.

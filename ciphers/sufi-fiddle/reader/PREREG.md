# PREREG -- GAPS94-sufi-fiddle (account-4), 3 Oct 2026, committed and pushed before the reader call

Step (GAPS93 Verdict): dump the matched spans (Malay and Arabic lists) and run one blind Opus Jawi/Arabic reading pass.

1. Span dump: `../malay-arabic/dump_spans.py` writes `../malay-arabic/spans.tsv` (every 1-3-group span whose skeleton is in
   the Malay or Arabic list at length >= 2, with the C3/C2 tiling's chosen spans marked). It is kept in scratch and is NOT
   committed or shown to the reader until the reader has returned; the reader also gets no repo access (no tools).
2. Reader: one Opus 5.5 subagent call, text only, no image, no word-list results, no mention of Muhammad or of any
   language other than as a list of candidates (Arabic, Malay/Jawi, Tausug, Maranao, Persian, Turkish, other). Input:
   `fig1_arabic.txt` (rendered by `render_arabic.py` from ciphertext_fig1.txt) plus the transcription's error rate
   (18.5 pct two-reader split, dots the commonest error). Prompt: `prompt_reader.txt`. Output: `reader_out.json`, a list
   of items {line, group_from, group_to, arabic, roman, language, gloss, confidence H/M/L}.
3. Pre-registered comparison (script `compare.py`, written after this file and before the reader returns):
   - S1 position agreement: for each reader item, does it share >= 1 group with a chosen_C3 span of either list (union)?
     Observed count O over the N items; expected E = sum over items of the probability that a span of the same width,
     placed uniformly among the valid (no-OBSCURED) positions of the same line, shares a group with that union; exact
     Poisson-binomial one-sided p = P(X >= O). Reported for all items and for items at confidence H/M.
   - S2 word agreement: for each reader item, is its word (Arabic letters through ar_skel, roman through roman_skel) the
     skeleton of a spans.tsv row at exactly the same group span, AND is the word itself (Arabic as written, or roman
     lowercased) in that list's index for the skeleton? Count W/N, descriptive only (no gate).
   - No gate: agreement is a consistency check between two readers of one transcription, not a confirmation (both rest on
     the same hand copy and the same 18.5 pct-split sign labels).
4. Grading (rule 4): no H, no C. A reader item at confidence H/M is graded M; at L it is graded I. Nothing is S (no
   two-word cryptanalytic control). Counts reported per grade.
5. Box: one call (~USD 1.5). If the reader returns nothing locatable, S1/S2 are reported as N = 0, not as a negative.

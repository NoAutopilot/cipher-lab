# spot1 pre-registration (A2P4-LVN97, LANE-A2PUSH4 account 2, 3 Oct 2026, written before any transcription pass or alignment)

Target: 5797 (KHA A3 895/I, WVO 5797), Groen IV CDXLIV p.222, the paragraph Groen prints from "werden E.G. nhumehr von
der bekannten persohn" (p.222 top) through "...welches ein insel ist, bringen." It contains the garbled stretch
"begert das uff dert mögen. [Phit] so E.G. ... vol ssen gemacht werden ... 11 haupter ... meinung ist, die
schlachtordnung ...". Manuscript: 05797.pdf p.3 lines L06-L08 and p.4 lines L01-L18 of spot1/crops (the
tools/iiif_lines.py cut of 300-dpi renders; p.4 L09-L18 is the garbled stretch, located by eye from the page
overview: L09 opens "173.121.67.81.92.82.22.32 das 40.90.87...", Groen's "begert das uff dert").

## Transcription
Two blind Sonnet passes per page (p3 L06-L08; p4 L01-L18), each given crop paths only, then one reconciliation
call on the disagreements only (tools/reconcile_passes.py). Units: one manuscript word = one space-separated unit;
a unit may mix codes and clear letters, e.g. `36.26.ch.8.lb.123.bich`.

## Decode
key_full.tsv (v3, as committed at 5ce7de2b) applied per code; NULL dropped; code absent from the key -> '?'; clear
letter fragments kept as written. Produced with tools/decode_key.py conventions (spot1/decode_spot1.json, --check).

## Alignment rule (fixed now)
- Normalisation (both sides): lowercase; ä ö ü -> a o u; ß -> ss; v w -> u; j y -> i; ck -> k; remove everything
  that is not a-z or '?'; collapse doubled letters. Groen's editorial apparatus ("Ga naar margenoot+ [#491]",
  "Ga naar voetnoot1 [#492]") is removed; bracketed conjectures keep their letters ("[Phit]" -> phit).
- Cipher word: a decoded unit containing at least one numeric code that decodes to a letter; eligible if its
  normalised string has >= 3 known letters (non-'?').
- Similarity sim(a,b) = 1 - lev(a,b)/max(len a, len b); '?' matches nothing.
- Monotone DP: the eligible cipher-word sequence is aligned in order against the word sequence of the reference
  text; a cipher word may match one reference word or the concatenation of 2 or 3 consecutive reference words, if
  sim >= 0.75; skips on either side cost nothing; maximise the number of matched cipher words (ties: more
  reference words consumed).
- Fragment words F of a reference text: its words not consumed by an exact (normalised) monotone match of the
  manuscript's clear whole words (the same DP, exact equality, one-to-one).

## Statistics
- A = (fragment words of the reference consumed by cipher-word matches) / |F| -- the brief's "share of Groen's
  printed fragment words reproduced in order".
- B = matched eligible cipher words / eligible cipher words (fixed denominator).

## Controls (same decoded run, same rule)
- (s) 200 word-shuffles of the Groen paragraph (seeds 1-200): order destroyed, same words.
- (d) three different Groen IV CDXLIV German paragraphs, first N words where N = the target paragraph's word count:
  d1 "Die schwere last..." + "Was seithero..."; d2 "Von zeittungen weisz..." + "langk hefftig practiciret..."; d3
  "Es lest sich, Gott lob, unsere Graveneinigung..." + following paragraphs.
Both can differ from the target on A and B (order for s, content for d).

## Gate (PASS needs all three)
1. A_target >= 0.50.
2. B_target >= p95(B over s) + 0.15.
3. B_target >= max(B over d1-d3) + 0.15.
PASS: readings at the garbled spots are reported at the key's grades (C/H per token, I where a letter is repaired);
FAIL: nothing is claimed for the interior beyond the transcription, logged as untested at this transcription.
Per-spot report regardless: for each Groen bracket/garble ([Phit], "uff dert", "vol ssen", "11 haupter",
"meinung ist", "Scholbich"), the cipher unit(s) beside it and their decode.

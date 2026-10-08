# PREREG D4-PISA -- f.275v head gloss, the words after "il desiroit" (8 Oct 2026, pushed before any tile read or score)

Question. The period decipherment at the head of fr.16045 f.275v (Gallica btv1b9060906j c563, second hand) runs "... qui descouurist cest
affere lequel il desiroit" and then a short phrase. Colbert 16 pt II p.122 (kp86f/colbert_f275v.txt) has "laquelle il desiroit tenir si
cachée". D1A-PISG noted descriptively that the gloss may read "tenir tres secrete"; D1A-PISG2 left it [?] (M). This job settles which.
Why a new instrument: the earlier line crops (f275vGH_L04_s2) cut the phrase between bands L04 and L05 (the line sags at its right end), and
the one-call blind line reader is [retired] for G2 (D1A-PISG2). Here: word tiles, each read in a forced choice among look-alike options.
Source (amended before any read, 8 Oct 2026 08:5x UTC by date -u): the planned native Gallica region (c563, 550,490,2475,1060) answered HTTP 500 and,
on the one retry after a pause, 503, so Gallica was not hit again. The only image on disk holding the whole phrase is D1A-PISG's
images/f275vGH_lines_debug.jpg (the same region at 0.646 x native, 1600 px wide, with 1-px band lines drawn on it). pisa/deline.py removes
the drawn lines (coloured pixels in rows y-1..y+1 of each line replaced by the mean of rows y-2 and y+2); pisa/pisa.py --build cuts every
tile, target and controls alike, from that one de-lined image and upscales 2x, so controls and target share scale, hand and processing.
Control set as cut (margin B is outside this image, so luxembourg and asseurer are replaced by faisant and dilligence): communiquer,
entendre, par lettres, personne, neantmoings, perpetuel, dilligence, faisant. Boxes, options and seed are frozen in pisa/pisa.py.

Instrument. One blind Opus subagent call. It sees N tiles (each a PNG/JPG crop of one word or short phrase, with some neighbouring ink) in a
random order, labelled T01..TN; for each it first writes a free transcription, then picks exactly one of 8 options listed for that tile, in an
option order shuffled per tile (seed 4). It is told only "16th-century French secretary hand, second-hand marginal decipherment"; it sees no
copy, key, decode, neighbouring text or the question being tested, and does not know which tile is the target.
- Target tile X: the phrase after "desiroit" (cut wide enough to include the whole phrase and the last letter of "desiroit").
  Options (8, balanced 4 "secret" / 4 "cache" forms): tenir si cachee; tenir tres secrete; tenir tres secret; tenir si secrete;
  tenir bien cachee; tenir fort secrete; tenir tres cachee; tenir si couuerte.
- Control tiles (known answer; copy word, settled in the D1A-PISG2 reconciliation): 8 words from the same gloss hand on the same page, each
  with its true word plus 7 look-alike decoys of similar length and letter shapes, chosen before the read. The planned set is
  communiquer, lettres, personne, descouuert, neantmoings, perpetuel, luxembourg, asseurer (a word whose tile cannot be cut cleanly is
  replaced by another reconciled word, logged, before the read). communiquer and lettres are the words both earlier blind readers got wrong.
- Controls can differ from the target on the statistic (a forced choice on a different tile, scored against a known answer), so they measure
  this reader's accuracy with this instrument on this hand, not the target's answer.

Gates.
 GC (control): forced choice correct on >= 7 of 8 control tiles (chance 1/8 each; P(>=7 of 8 by chance) < 1e-5).
 GT (target): if GC passes, the target's forced choice is the reading of the phrase; its letters are graded S (cryptanalytic/paleographic,
    control-backed). If the reader's free transcription of X contradicts its own forced choice in the distinguishing word (si/tres/bien/fort,
    cachee/secret(e)/couuerte), the result is reported as split and the phrase stays M.
 If GC fails: non-test for this instrument at this tile size; the phrase stays M; no fourth attempt at the same tiles by this instrument.
Outcome. Either answer is reported beside the copy: "si cachee" = gloss and Colbert copy agree here; any other option = a period-gloss vs
copy wording difference at this point (a fact about the two witnesses, not about the cipher). key86.tsv, transcriptions, readings and
kp86f grades unchanged in every outcome (running-text gloss, no sign-level value). One vision unit + one reconciliation unit (the worker
checks the reply against the tiles and logs it; the reconciliation is descriptive and cannot change the gated answer).
Script: pisa/pisa.py builds the tiles' order and option lists (seeded), and scores the verbatim reply (pisa/reader.txt) into
pisa/pisa_result.json with `--check`.

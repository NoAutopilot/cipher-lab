target: spinelli-beinecke-c1515
goal: a verified reading of Thomas Spinelli to Leonardo Spinelli, Barcelona, 7 Sept 1519 (Beinecke GEN MSS 109, Spinelli Family Papers) at N3 or better after two audits
started: 2026-09-27 20:47 UTC
daily_budget_usd: 40
spent_today_usd: 3.50
spent_day: 2026-09-27
closed:

## Attempts already made

- INTAKE-SPINELLI (27 Sept 2026, parent worker, Sonnet, session_01A8LNPQ8NzN53Yx9byfcLpL): Job 0 gate -- NOT
  found-solved (Tomokiyo's `henryvii.htm` prints only the one phrase, "la gubernation d'ispagnia", recovered from
  this letter, no transcription; Domnina's own PDF at istina.msu.ru 404s to this job's one allowed request,
  unreachable, not itself checked -- flagged, not treated as a "no"; the Beinecke Blacklight record and its IIIF
  manifest metadata name no transcription either). Built this folder: NOTES.md; `images/manifest.json` (IIIF
  Presentation API 3.0, 3 canvases, p.[1] fetched at 1500px, p.[2]/p.[3: address leaf] not fetched);
  `keys/key_spinelli_c1515.tsv` (45 rows, 23 AB / 21 M / 1 ?, transcribed from Tomokiyo's own separately-published
  `spinelly1515.png` reconstruction -- not Domnina's Fig.1 itself, which was unreachable -- via two independent
  blind Sonnet vision reads settled by this worker's own zoomed crops; 3 blank letter columns q/x/z, 5 homophone
  columns d/i/l/n/t, 12 nulls, 5 word-codes). A direct look at p.[1] (no vision call) found the top ~9 lines
  continuous cipher, several shapes matching the key table on sight, then plain Italian prose from "L'amorte del
  Car[dinale]..." onward -- not transcribed or decoded this job. 2 of 4 allowed vision subagent calls used, both
  spent on the key transcription, none on the letter itself. Stopped: job finished on its own brief (a Layout
  intake -- no cryptanalysis, no reading, no class); named "locate the known phrase and calibrate, then two blind
  passes on the whole letter plus a shuffled-key control" as the next step, which this file's H1-H4 now formalize.

## Hypotheses

| id | rank | hypothesis | needs | est_usd | status | result |
|---|---|---|---|---|---|---|
| H1 | 1 | Fetch canvases p.[2] (10867299) and p.[3: address leaf] (10867300) at 1500px via the same IIIF image API used for p.[1] (collections.library.yale.edu/iiif/2/{id}/full/1500,/0/default.jpg), write both into images/manifest.json with sha1 and a content_note; a direct look then flags where cipher lines sit on each page before any vision call is spent locating a specific phrase | nobody | 0.5 | done | both canvases fetched (sha1 in manifest); cipher = p.[1] top ~9 lines + p.[2] two isolated lines (~55 signs, native x,y,w,h 401,2037,2973,376); p.[3] address leaf, no cipher; 0 vision calls |
| H2 | 2 | One Sonnet vision pass over line crops (tools/iiif_lines.py --image, never the full page) of p.[2]'s two-line cipher block first (H1: native x,y,w,h 401,2037,2973,376, ~55 signs), falling back to p.[1]'s own 9 cipher lines if the phrase is not there, searching for the symbol run key_spinelli_c1515.tsv predicts for Tomokiyo's known-answer span "la gubernation d'ispagnia"; a match calibrates the key against real ciphertext at grade C (the plaintext is Tomokiyo's, not ours) and confirms or corrects the homophone and blank-column reading before any blind pass runs | nobody | 2 | done | not located: best 3/22 crib alignment over 251 signs coded by 3 blind passes (chance; synthetic control 22/22); conditional on pass quality (~2/3 agreement with a direct look); 22% of signs unmapped by the key, letter frequencies under the key not Italian (a 3%, e 2%, i 1%) -> atlas before any key-coded pass |
| H11 | 3 | Glyph atlas from the letter's own ink: segment the ~330 signs of both cipher blocks (crops already on disk) and cluster them by shape with tools/glyph_atlas.py (pip install its deps; the dupuy452-carpi-1520 method), write glyphs/atlas with one reference crop per cluster and a cluster-frequency table; H2 showed 22% of signs match nothing in key_spinelli_c1515.tsv and the key-coded letter profile is not Italian, so both blind passes must code against this atlas, not the key (transcription brief, Raince/Salviati lesson) | nobody | 3 | open |  |
| H10 | 4 | Two independent blind Sonnet vision passes transcribing p.[2]'s two-line cipher block (~55 signs, H1's region, crops cut first with tools/iiif_lines.py --image per the mandatory-crop rule) sign by sign against H11's atlas codes (not the key), reconciled with tools/reconcile_passes.py (2 reads + 1 reconciliation priced); the smallest self-contained cipher unit in the letter, bounded by clear text on both sides, so it doubles as H2's calibration material and as H4's first decode input | nobody | 1.5 | open |  |
| H3 | 5 | Two independent blind Sonnet vision passes transcribing p.[1]'s own ~9 cipher lines sign by sign against H11's atlas codes (not the key); H2's pass A files are usable as one of the two passes (crops cut first with tools/iiif_lines.py per the mandatory-crop rule, never the full page image to a subagent call), reconciled with tools/reconcile_passes.py; this is the transcription H2 calibrates against and H4 decodes, kept as its own priced step per the reconciliation-costing lesson | nobody | 3 | open |  |
| H4 | 6 | Apply the calibrated key (H2) to H3's reconciled transcription via a decode.json layout and tools/decode_key.py, then run a 20-shuffled-key control (rule 3) before any word beyond Tomokiyo's own known phrase is reported as a reading; the gate is the shuffled-key mean, not a fixed percentage, since no matched control has run on this design yet | nobody | 1 | open |  |
| H12 | 7 | Atlas-cluster frequency profile against Italian: rank H11's clusters by count, compare with Italian letter frequencies and with the key's own assignments; test whether the frequent unmapped shapes (numeral-2 x13, x-cross x12, ll, diamond) behave as vowel homophones, with a shuffled-assignment control for any claimed match; H2 found a, e, i nearly absent under the key as read | nobody | 1 | open |  |
| H13 | 8 | Correct keys/key_spinelli_c1515.tsv's word-code rows from the key image (H2): six symbols not five -- 2-with-bar AND 4-with-plus both under 'Emperor King of Arragon', capital-H under 'Prince of Castile' (the H occurs in the letter), boxes 'new amity'; grade M, note the letter's 8-9 unmapped sign types in the header; re-run tools/key_design.py --check | nobody | 0.5 | open |  |
| H5 | 9 | Check whether q, x and z (the three blank letter columns in key_spinelli_c1515.tsv) are attested anywhere in H4's decode, or would even be expected in a short Italian business and family letter, by a plain letter-frequency count, to tell a genuine gap in the source table from an artifact of this letter's own short vocabulary | nobody | 0.5 | open |  |
| H6 | 10 | Query the Wayback Machine CDX API (web.archive.org/cdx/search/cdx) for any archived snapshot of Domnina's PDF URL at istina.msu.ru, which returned a live 404 to INTAKE-SPINELLI's one allowed request; a snapshot would let a future worker cross-check this folder's Tomokiyo-sourced key against Domnina's own Fig.1 without waiting on a person route | nobody | 0.5 | open |  |
| H7 | 11 | Fetch archives.yale.edu/repositories/11/archival_objects/2787659 (the Archives at Yale item-level finding aid), a different host INTAKE-SPINELLI's own allowed network scope excluded, for any sender, recipient or date corroboration, or a transcription note, not already in the Beinecke Blacklight record | nobody | 0.5 | open |  |
| H8 | 12 | Cross-check key_spinelli_c1515.tsv (Tomokiyo's own reconstruction) against Domnina's original Fig.1 (Geheime Post, 2015, p.185) once a working route to her PDF exists, since this folder's key has never been checked against her own table | doc a working route to istina.msu.ru's Domnina_Spinelli_cipher PDF (a mirror, a corrected URL, or a library database); ASKS row not yet filed | 2 | open |  |
| H9 | 13 | Scholarship search for Ekaterina Domnina, "Ciphers in Early Tudor Diplomacy" (Geheime Post, 2015), and for the Spinelli brothers' cipher correspondence generally, sender and recipient and date ANDed with a cipher keyword via the open indexes, plus a JSTOR row in both the sender/date and bare-quoted-phrase families per the verifier brief once H2 or H4 yields any decoded text | doc a JSTOR-QUEUE.tsv row for this target, not yet filed | 0.5 | open |  |

## Log

2026-09-27 20:47 UTC | session_01HFV78hjVwFisJYV3vnGgeT | seed | 0 | CAMPAIGN.md written, 9 hypotheses.
2026-09-27 22:00 UTC | session_016fvFiTTAhQng2VqbiBDmRE | H1 | 0.5 | done: p.[2] and p.[3] fetched (2 requests, sha1 in manifest); cipher = p.[1] ~9 lines + p.[2] two isolated lines (~55 signs), p.[3] address leaf no cipher, '4pp.' narrowed (text ends p.[2]); re-rank: new H10 (blind passes on the p.[2] block) at rank 3 because it is the smallest bounded cipher unit and calibration material for H2, H3-H9 shift down one; H2 amended to start on the p.[2] crops. 0 vision calls.
2026-09-27 23:25 UTC | session_016fvFiTTAhQng2VqbiBDmRE | H2 | 3.0 | done (1.5x est): crib not located, best 3/22 over 251 signs from 3 blind key-coded passes (control 22/22), conditional on pass quality; 22% of signs unmapped by the key, key-coded letter profile not Italian; key image has 6 word codes not 5. Re-rank: new H11 (glyph atlas from the letter's own ink) at 3 ahead of H10/H3, which now code against the atlas; new H12 (cluster frequencies vs Italian) at 7 and H13 (key word-code fix) at 8; H5-H9 shift down. H8 stays needs: doc.

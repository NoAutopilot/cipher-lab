target: spinelli-beinecke-c1515
goal: a verified reading of Thomas Spinelli to Leonardo Spinelli, Barcelona, 7 Sept 1519 (Beinecke GEN MSS 109, Spinelli Family Papers) at N3 or better after two audits
started: 2026-09-27 20:47 UTC
daily_budget_usd: 40
spent_today_usd: 0
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
| H1 | 1 | Fetch canvases p.[2] (10867299) and p.[3: address leaf] (10867300) at 1500px via the same IIIF image API used for p.[1] (collections.library.yale.edu/iiif/2/{id}/full/1500,/0/default.jpg), write both into images/manifest.json with sha1 and a content_note; a direct look then flags where cipher lines sit on each page before any vision call is spent locating a specific phrase | nobody | 0.5 | running session_016fvFiTTAhQng2VqbiBDmRE |  |
| H2 | 2 | Once H1 lands: one Sonnet vision pass over the cipher lines on p.[2]/p.[3] (or a re-look at p.[1]'s own 9 cipher lines if the phrase sits there instead) searching for the symbol run key_spinelli_c1515.tsv predicts for Tomokiyo's known-answer span "la gubernation d'ispagnia"; a match calibrates the key against real ciphertext at grade C (the plaintext is Tomokiyo's, not ours) and confirms or corrects the homophone and blank-column reading before any blind pass runs | nobody | 2 | open |  |
| H3 | 3 | Two independent blind Sonnet vision passes transcribing p.[1]'s own ~9 cipher lines sign by sign against key_spinelli_c1515.tsv's inventory (crops cut first with tools/iiif_lines.py per the mandatory-crop rule, never the full page image to a subagent call), reconciled with tools/reconcile_passes.py; this is the transcription H2 calibrates against and H4 decodes, kept as its own priced step per the reconciliation-costing lesson | nobody | 3 | open |  |
| H4 | 4 | Apply the calibrated key (H2) to H3's reconciled transcription via a decode.json layout and tools/decode_key.py, then run a 20-shuffled-key control (rule 3) before any word beyond Tomokiyo's own known phrase is reported as a reading; the gate is the shuffled-key mean, not a fixed percentage, since no matched control has run on this design yet | nobody | 1 | open |  |
| H5 | 5 | Check whether q, x and z (the three blank letter columns in key_spinelli_c1515.tsv) are attested anywhere in H4's decode, or would even be expected in a short Italian business and family letter, by a plain letter-frequency count, to tell a genuine gap in the source table from an artifact of this letter's own short vocabulary | nobody | 0.5 | open |  |
| H6 | 6 | Query the Wayback Machine CDX API (web.archive.org/cdx/search/cdx) for any archived snapshot of Domnina's PDF URL at istina.msu.ru, which returned a live 404 to INTAKE-SPINELLI's one allowed request; a snapshot would let a future worker cross-check this folder's Tomokiyo-sourced key against Domnina's own Fig.1 without waiting on a person route | nobody | 0.5 | open |  |
| H7 | 7 | Fetch archives.yale.edu/repositories/11/archival_objects/2787659 (the Archives at Yale item-level finding aid), a different host INTAKE-SPINELLI's own allowed network scope excluded, for any sender, recipient or date corroboration, or a transcription note, not already in the Beinecke Blacklight record | nobody | 0.5 | open |  |
| H8 | 8 | Cross-check key_spinelli_c1515.tsv (Tomokiyo's own reconstruction) against Domnina's original Fig.1 (Geheime Post, 2015, p.185) once a working route to her PDF exists, since this folder's key has never been checked against her own table | doc a working route to istina.msu.ru's Domnina_Spinelli_cipher PDF (a mirror, a corrected URL, or a library database); ASKS row not yet filed | 2 | open |  |
| H9 | 9 | Scholarship search for Ekaterina Domnina, "Ciphers in Early Tudor Diplomacy" (Geheime Post, 2015), and for the Spinelli brothers' cipher correspondence generally, sender and recipient and date ANDed with a cipher keyword via the open indexes, plus a JSTOR row in both the sender/date and bare-quoted-phrase families per the verifier brief once H2 or H4 yields any decoded text | doc a JSTOR-QUEUE.tsv row for this target, not yet filed | 0.5 | open |  |

## Log

2026-09-27 20:47 UTC | session_01HFV78hjVwFisJYV3vnGgeT | seed | 0 | CAMPAIGN.md written, 9 hypotheses.

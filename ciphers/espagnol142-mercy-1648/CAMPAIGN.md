target: espagnol142-mercy-1648
goal: a verified reading of the letter at N3 or better after two audits
started: 2026-09-27 20:29 UTC
daily_budget_usd: 40
spent_today_usd: 0
spent_day: 2026-09-27
closed:

## Attempts already made

- Check-solved sweep, six sources, 24-25 Sept 2026: addressee "abbé/Baron de Mercy" identified as Archduke
  Leopold Wilhelm's envoy; no prior print or decipherment found in Le Clerc, APW (structurally ends 19 May
  1648, three weeks short), Cryptiana, DECODE, Bourdeau, Aymeloglu.
- Y5 (25 Sept): folio pinned at BnF Espagnol 144 (not 142) f.22r-22v, ark `btv1b10035717h` canvases 58-59,
  content-confirmed by the dateline "Barneton a seis Junio de 1648".
- Y6 (25 Sept): two blind transcription passes reconciled at 95.3% agreement (`ciphertext.tsv`, N=521 codes,
  K=38); no published period key found for this office within the pass's host limits (github.com only).
- Y8 (25 Sept): built `tools/data/es17` Spanish corpus; ran `tools/homophonic_anneal.py` with its matched
  control first (rule 3) -- target beats the control by 167-181 points across seeds and both mark variants;
  judge FAILs (not yet a reading). Flagged an exact-frequency-profile control as the next worker's first
  move; a scratch attempt at it had a bug (K=307-320 instead of 38) and was abandoned, never fixed.
- M2 (25 Sept): graded reading from the anneal key plus hand corrections: S 494, M 27, H 0, C 0 of 521 codes.
  Crib-loop gain gate run against the matched control: control gains 0.0, target gains from -1154.3 to
  -1199.1 (worse by the numeric objective) -- gate not met numerically, though legibility improved.
- MR (25 Sept): fresh re-derivation from spec+key+ciphertext byte-identical to the committed reading
  (rule 7 satisfied).
- MJ (25 Sept): built `tools/data/es17c` (3 register-matched Cartas tomes, 1643-47); FAIL did not flip to
  PASS (clear words -0.891 vs real_p05 -0.867); held-out false-negative rate 23.5% blended, 3.95x per-fold
  spread.
- M3 (25 Sept): finding-aid and image sweep of Espagnol 142-144 for a sibling ciphered leaf under the same
  key -- none found; the target is the only item in the whole 605-canvas volume marked "chiffrée"; pooled N
  stays 521.
- R7-MSHUF (25 Sept): shuffle-control test -- full-shuffle and line-shuffle anneals of the target's own code
  multiset score far below even the matched-control band (verdict: the anneal gap is carried by real
  sequence structure, not the skewed symbol profile).
- R7-MEYE / R7-MREV (25 Sept): independent blind re-transcription of the 5 disputed 14-vs-19 glyphs and the
  v07 token-count mismatch; blind majority reverted 3 of 5 exceptions and split one token; reading updated
  to S 496, M 26 of 522 (`Cleues` -> `Eleues`); judge FAIL essentially unchanged.
- V6-MERCY / V6-MERCY2 (25 Sept): verifier classed the reading **N3**, key **ours**; safe sentence in
  AUDIT.md; two wording corrections logged (shelfmark, sender inference).
- SO-MERCY-F22 second opinion, checked by V8-SO16 (26 Sept): 9 of 9 checked claims confirmed against source;
  no confirmed lead moves N3.
- V-GATE2 (26 Sept): outward-facing gate 2 closed (JSTOR rows 79-82 answered, no hit; second adversarial
  audit and open-index pass done).
- IA-BORROW / Local runner L20 (25-26 Sept): Correspondance de la Cour d'Espagne VI borrowed but page images
  obfuscated for scripts; the owner read printed p.647 directly -- a different letter (11 June 1648,
  Peñaranda to Philip IV), not the target instruction. ASKS row 59 closed.
- R7-MSIB (25 Sept): traced Lonchay 1896 p.445 n.2's cited sibling, the 15 April 1648 instruction to Mercy,
  to Brussels AGR Secrétairerie d'État et de Guerre t. LXIV f.16 -- digitised per AGATHA but reading-room-only,
  no online image. ASKS row 60 filed; SEND-QUEUE.tsv row S3 (a reproduction/quote form) queued 26 Sept, still
  `queued` as of this write.
- MERCY-KEY (27 Sept): fetched DECODE records 958-965 (Brussels SEE "chiffres 1647-98") login-free; ruled
  out by design (958 mixes alphabet+numeric+nomenclature at ~50 codegroups, 959-965 are >100-entry
  nomenclature-dominated keys; target is a flat 38-value all-numeric substitution with no nomenclature
  class); thumbnails unreadable at served resolution. Gayangos BM catalogue (4 vols) grepped: one 1641 Mercy
  item, a different mission, no cipher language nearby.
- MERCY-JUDGE2 (27 Sept): widened the judge corpus to all seven Cartas/Memorial histórico tomes
  (`tools/data/es17c7`, 1634-1647); blended false-negative rate roughly halved (23.5% -> 11.1%) but per-fold
  spread widened (3.95x -> 11.5x); pre-registered gate (blended <10%, spread <2x, clear words PASS) not met
  on either leg -- verdict stays "judge cannot decide", not a real negative. 20/20 shuffled nulls of the
  reading FAIL cleanly (the judge does separate order from scramble at this N, just not reliably enough to
  gate on).

## Hypotheses

| id | rank | hypothesis | needs | est_usd | status | result |
|---|---|---|---|---|---|---|
| H1 | 1 | Exact-frequency-profile control (Y8's flagged, never-fixed next step): build a control that replicates the target's own 38-code occurrence multiset exactly (not just corpus letter frequency allotted to homophone group sizes), anneal it 5 seeds against `tools/data/es17`/`es17c7`, and compare to the target's -1154.3 to -1154.6 (K=38, N=522 post-MREV). Passes (still informative) if the target beats this stricter control by more than 2x the control's own inter-seed spread. | nobody | 3 | running session_01V7xEY9JxjCxiXnQLtjFnfL | |
| H2 | 2 | Targeted 4x-zoom re-crop and blind vision re-check of the five still-unread rare codes (48, 52, 65, 72, and the two marks) plus the v04 "NOLADIRENTNONYSIIUNA" stretch and r16-r17 after Brandenburg, against `images/f22r_canvas58.jpg`/`f22v_canvas59.jpg` directly (the same method MREV used to settle the v07 split) -- tests whether any are genuine word-codes/nulls or mistranscribed digits. | nobody | 3 | open | |
| H3 | 3 | Re-run `tools/homophonic_anneal.py --fix` with the 29 confirmed `key.tsv` codes held, on the current 522-token `cipher_codes.tsv` (post-MREV v07 split, one token more than M2's original 521-token run) -- confirms M2's -1199.1 anneal-with-fixes figure still reproduces after the token-count change; a rule-7 consistency check nobody has explicitly re-run since MREV. | nobody | 2 | open | |
| H4 | 4 | Within-tomo homogeneity split of the `es17c7` judge corpus (named next step in `tools/data/es17c7/README.md`): split each of the 7 tomes by internal date range or correspondent rather than by tomo count, re-run the leave-one-fold-out false-negative rate, and re-judge the reading if the blended rate drops under 10% with per-fold spread under 2x. | nobody | 4 | open | |
| H5 | 5 | Apply `tools/family_run.py`'s wordcode family (built for fr2933-salviati-1525) to the marked/word-code positions ([MARK:box], [MARK:frac], codes 48/52/65/72 flagged in `key.tsv` as possible word codes or nulls), using the already-transcribed plain-Spanish context as anchors; matched control first (same N/K/design against es17c7). | nobody | 3 | open | |
| H6 | 6 | Blind independent second vision pass (a fresh Sonnet subagent, no context from `reading.txt`/`key.tsv`) re-transcribing only r16-r17 and v04 from the native images, to settle whether the unread stretch is a transcription tangle or contains further token boundaries -- distinct from H2, which targets specific rare-code positions with the reader's own eye; this is a from-scratch second pass on the whole unread span, the project's usual two-pass rule applied to a fresh question. | nobody | 2 | open | |
| H7 | 7 | Brussels AGR Secrétairerie d'État et de Guerre t. LXIV f.16 (the 15 April 1648 sibling instruction to Mercy, in clear per Lonchay 1896): a reproduction or reading-room quote would supply either a crib or independent confirmation of the sender. Form already filed (SEND-QUEUE row S3, ASKS row 60), awaiting the owner's send and the archive's reply. | doc: AGR SEE t.LXIV f.16 reproduction/quote, SEND-QUEUE.tsv row S3 / ASKS row 60 | 0 | open | |
| H8 | 8 | Lonchay-Cuvelier IV (the 1647-1665 Madrid-Brussels calendar; seqs 56-130 cover 1648), a full page read of the entries naming Mercy/Leopold Wilhelm's 1648 dispatches -- seen only at HTRC token level and Google Books snippet so far (AUDIT.md S2.4); the volume is Cloudflare-blocked from the cloud (HathiTrust) and not on Internet Archive. Would settle whether Leopold's covering dispatch summarises the 6 June instruction's content. Not yet queued in LOCAL-QUEUE.tsv -- filing that row is the owner-side prerequisite. | doc: LOCAL-QUEUE.tsv row for a Lonchay-Cuvelier IV (HathiTrust `mdp.39015014126620`) page read of the 1648 entries, not yet filed | 0 | open | |

## Log

2026-09-27 20:29 UTC | session_01L7p2vZQmJPYTMvyAvszxFs | seed | 0 | CAMPAIGN.md written, 8 hypotheses.

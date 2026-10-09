# PREREG-MQS-LANGS (9 Oct 2026, written 06:4x UTC by date -u, pushed before any scoring)

Job MQS-LANGS (LANE MQS-2, account 4; brief .claude/briefs/runs/2026-10-09-ytbiz-mqs-next-langs.md; research row
M15 of research/MARY-STUART-TALK-2026-10-09.tsv, "Choose the language by trial, not from the neighbouring documents",
after Lasry, Biermann and Tomokiyo 2023, Cryptologia 47:2, pp.112-115).

## Option under test

`tools/family_run.py SPEC --family F --langs L1,L2,...`: runs one family once per language, each with that language's
own matched control (family_run's usual control, built from that language's LANG_CORPORA entry, gate as given) and,
when the control meets its gate, the target with that language's corpus as the solver's model. Each target decode is
then scored by `judge_plaintext.py` under the SAME language; the ranking statistic is the margin
`score - real_p05` (log10 4-gram per letter; >= 0 means the decode clears that language's real-text 5th percentile).
Languages are ranked by margin; a language whose control missed its gate is listed, not ranked.

New judge key `fr16` = all three tools/data/fr16 files (Catherine de Medicis t.1 and t.2, Marguerite de Valois).
`fr` is left as it is (one file) so no existing French judge figure moves; repointing `fr` is the orchestrator's call.

## Known answers (period-key plaintexts; the cipher is synthetic, so the true language is known)

- **KA-IT**: Birago no.87, the clerk's decipherment sheet (ciphers/nevers-birago-fr3251-1572/harvest/f179r_sheet/
  decipherment_sheet.tsv, column `text`, all lines), Italian. Folded to a-z, bracketed notes dropped, enciphered by a
  random monoalphabetic key (seed 87), word divisions removed.
- **KA-FR**: Gramont f.29r (ciphers/fr2980-gramont/reading.txt, f29r lines only; H 532 of 568 tokens), French.
  Bracket groups ([ET], [COM], [LL], [SS]) kept as their letters, other marks dropped; same encipherment (seed 29).
- Family masc, restarts 8, control seeds 3, gate 0.6, languages `fr,fr16,it,it16dip,es17c,la18,en`.

## Nulls

- **NULL-IT / NULL-FR**: the same plaintexts letter-shuffled (seed 1) before the same encipherment. The margin is a
  4-gram order statistic, which a letter shuffle destroys while keeping N, K and the unigram profile, so the null CAN
  differ from the known answer on the statistic computed (rule 3, "control that cannot vary").

## Gate (all must hold, else the option ships `weak` with both numbers and is not re-briefed)

1. KA-IT: the top-ranked language is `it` or `it16dip`, and `fr` and `fr16` each have margin < 0.
2. KA-FR: the top-ranked language is `fr` or `fr16`.
3. NULL-IT and NULL-FR: no language has margin >= 0 (max margin < 0).
4. Every reported rank has its language's control mean beside it; a language below its control gate is not ranked.

Ceiling note: masc controls at N ~ 500-1,100 are expected near 1.0 recovery; that is fine here because the claim is a
language RANKING, not a gain over blind (rule 3 ceiling paragraph addresses gain gates).

## fr16 per-fold spread (descriptive, no gate)

`judge_plaintext.py --holdout` over the three fr16 files at N=500 and N=1000, 200 samples: report each fold's
false-negative rate and the blended rate. Pre-stated reading: under 5 files, so if the per-fold spread exceeds 2x the
fr16 judge is "of unknown reliability" (rule 3, es17c paragraph); the Marguerite file is small (145 kB) and is the
expected outlier.

## Scope

No target is decoded; no status, key, reading or AUDIT.md changes; no host requests. The synthetic runs write into
a scratch slug (`_mqs_langs_test`) that is removed after; results go to tools/tests/MQS-LANGS-controls.tsv.

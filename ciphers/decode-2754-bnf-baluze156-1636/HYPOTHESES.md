# decode-2754-bnf-baluze156-1636 -- hypotheses and family runs (append-only)

Opened 3 Oct 2026 (FT4, account-4). Rule 3: every key/family tried here carries its matched control side by side.
Earlier runs (24-25 Sept 2026) are logged in NOTES.md and summarised in the first two rows.

| date | hypothesis (key family) | script / output | target | matched control | verdict |
|---|---|---|---|---|---|
| 24 Sept 2026 | Lasry, Louis XIII-Sabran (1631), Baluze 155 f.79: nomenclator numbers | trial.py / trial.tsv | 0/31 numeral hits | shuffled key mean 19.1%, max 83.9% (1000) | negative |
| 24 Sept 2026 | same key, letter alphabet (fixed shape map) | letters_trial.py / letters_trial.tsv | 5.649 bpc (116 letters) | positive 3.066 bpc; shuffle median ~real | negative |
| 25 Sept 2026 | Lasry, Farnese-Sabran (1637), Baluze 156 f.40, letters | letters_trial.py --key2 / letters_trial2.tsv | 5.412 bpc (79), at shuffle median (p 0.500) | positive 3.754 bpc (p 0.000) | negative |
| 3 Oct 2026 | Tomokiyo, Servien-Sabran (1632), Baluze 155 f.105-139, letters; best over overbar ambiguity (13 of 25 classes), same search for all rows | servien_trial.py / servien_trial.tsv | 4.421 bpc (100 letters); p = 0.040 of 200 shuffled keys (0.048 of 1000, seed 7, not committed); no French word >= 4 letters | shuffle median 5.101; positive 3.938 bpc, p 0.000, 74% of letters recovered; fr16 judge: decode -1.755 below null_p99 -1.711 (real_p05 -0.948) | negative at the 1% gate (does not read); weaker negative than the two Lasry keys -- real sits near the shuffles' 5th percentile, not their median |
| 3 Oct 2026 | Period key rebuilt from BnF fr.4140 f.146r (Sabran, 9 Aug 1636, same letter/doubled-letter/digit design) + its period clear copy f.151r; 29 signs kept (grade C) | fr4140_trial.py / fr4140_trial.tsv | 5.232 bpc (89 of 137 tokens covered); p = 0.815 of 200 shuffled keys (worse than their median 4.898); variant DC8 '4' = crossed-tail a (i): 4.682, p 0.455; fr16 judge FAIL -2.235 vs null_p99 -1.63 | leaf pairing 0.897 agreement vs shuffled pairings median 0.196, p99 0.327 (passes); positive 3.366 bpc, p 0.000 | negative, clean (target sits at or above the shuffle median); same design family, different values |

# it19: Italian prose of about 1800-1830 for the judge's language check and as an anneal LM

Built 2 Oct 2026 (A2-CAS7, LANE-A2PUSH account 2, `.claude/briefs/runs/2026-10-02-acct2-a2-cas7.md`) because
`tools/data` held only 16th-century Italian (`it16`, `it16dip`), about 300 years before castelcicala-1816
(Neapolitan despatches, London and Paris, 1816-23). Method: V6-PTCORP's (tools/data/pt18).

Five archive.org `_djvu.txt` OCR files, five works by four authors, see MANIFEST.tsv: Botta, *Storia d'Italia dal
1789 al 1814* t. I (1824); Colletta, *Storia del reame di Napoli dal 1734 sino al 1825* (written 1820s); Cuoco,
*Saggio storico sulla rivoluzione di Napoli* (1806); Foscolo, *Epistolario* vols 1 and 3 (letters c.1795-1815 and
the London years c.1816-27). Political/diplomatic history and letters; no verse, no translations, no dictionaries,
nothing by Castelcicala or Circello. Colletta narrates Neapolitan politics of the target's years but prints no
Castelcicala despatch; never add any castelcicala-1816 material here (circular).

`build.py --raw DIR` drops Google boilerplate, rejoins hyphenation, keeps 60-word chunks that read as Italian prose
(function-word share >= 22%, French <= 2%, Latin endings <= 3%, junk <= 20%) and caps each file at 650,000 folded
letters. Result: 626,436 + 650,597 + 423,736 + 650,501 + 650,034 = **3,001,304 letters**; largest source 21.7%.
Fetched once, one request at a time, 2 s apart (5 archive.org downloads + 4 advancedsearch calls + 1 metadata
call + 1 held-out file for the test).

## Calibration (rule 3 fold-count paragraph), 2 Oct 2026, 200 windows per fold, seeds 1/2

Leave-one-file-out real-prose false-negative rate (`holdout_check.py`), beside the same it19 windows scored under
the 16th-c. default `it` (`era_check.py`):

| N letters | it19 LOO blended | it19 per-fold spread | it19 prose under `it` | spread under `it` |
|---|---|---|---|---|
| 300 | 23.2% | 12.0-42.5% | 21.1% | 13.5-28.5% |
| 1000 | 29.6% | 9.5-65.5% | 58.3% | 41.5-80.5% |

Per fold at N=1000: Botta 22.0, Colletta 32.5, Cuoco 9.5, Foscolo 1 18.5, Foscolo 3 65.5. At N=1000 it19 halves the
false-negative rate the era-mismatched corpus gives period prose (58.3 -> 29.6); at N=300 there is no gain. The
spread is wide and driven by one fold (Foscolo vol. 3, intimate first-person letters, clean Italian, no English or
French found), the same shape as `en`'s Moby-Dick outlier. By rule 3, five files with a 9.5-65.5% spread make a
FAIL/PASS against it19 **of unknown reliability**; use it as a better-matched LM than it16 for search, and report
the per-fold spread beside any gate result. A sixth source in despatch register (printed 1810-30 Italian
diplomatic correspondence) is the obvious next addition if a gate needs it.

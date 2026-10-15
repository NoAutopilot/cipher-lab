# tools/data/ru20: Soviet-era Russian prose (KAL-RUCORP, 15 Oct 2026)

Built for kaliningrad-2015 (brief `.claude/briefs/runs/2026-10-15-acct1-default-0447-jobs.md` "KAL-RUCORP"). Era chosen from the
folder's only dating evidence: Schmeh post 19 comment thread (`sources/schmeh/posts/19-kaliningrad.txt` lines 892-936), a reader's
argument that the notebook paper is of a 1930-1960 type, the ink a fountain pen's, the hand a 10-13-year-old's, and the deposit
1945-48 -- inference by a commenter, not a dated document. So: Soviet prose written 1914-1942, plain/colloquial/juvenile registers.

Six sources, one file each (`MANIFEST.tsv` has the IA identifier, author and death year, work, printing, register and the licence
basis per file). All by authors whose works are in the public domain in Russia (CC RF arts. 1281, 1281(1) war extension) and whose
Russian term had already expired on 1 Jan 1996 (so not restored in the US). Fetched from archive.org `_djvu.txt` OCR, 15 Oct 2026,
15 requests >= 2 s apart. ru.wikisource.org was the brief's first host: it answered HTTP 429 (envoy rate limit, shared egress IP)
on the first request and the one retry; stopped, 2 requests.

| file | source | Cyrillic letters |
|---|---|---|
| ilf_petrov_12stulev_1928 | Ilf & Petrov, Dvenadtsat stulev (1928 printing) | 478,044 |
| gaidar_rakety_1942 | Gaidar, Rakety i granaty (1942) | 29,155 |
| gaidar_soch2_1957 | Gaidar, Sochineniya t.2 (1957; texts 1930s-1941) | 938,069 |
| furmanov_chapaev_1937 | Furmanov, Chapaev (1937 printing; written 1923) | 431,091 |
| furmanov_dnevnik_1930 | Furmanov, Dnevnik 1914-1916 (1930 printing) | 381,094 |
| ostrovsky_stal_1955 | N. Ostrovsky, Kak zakalyalas stal (1955 printing; written 1932-34) | 542,807 |

`ru20/<name>.txt.gz` is cleaned lower-case Cyrillic; `ru20_lat/s1s/<name>.txt.gz` the same in `tools/translit_ru.py` scheme s1s.
Reproduce: fetch the six `_djvu.txt` files named in MANIFEST.tsv into a directory, then `python3 tools/data/ru20/build_ru20.py DIR`.
Other schemes: `python3 tools/translit_ru.py --scheme s1|s3p|s3 <dir with one ru20 file> <out>`.

Limits: OCR misreads are left as they are; the 1957 Gaidar volume's editorial matter, if any, is not removed; Furmanov's diary
content predates 1917 (printed in post-reform spelling); gaidar_rakety_1942 is short (31k letters), so its fold windows overlap.

## Held-out calibration (KAL-RUCORP, 15 Oct 2026)

`python3 tools/judge_plaintext.py --holdout tools/data/ru20_lat/s1s/*.txt.gz --N 1066` (200 windows per fold; log
`tools/data/ru20_lat/holdout_s1s_N1066.log`):

| fold | FN % | held-out p05 | held-out min |
|---|---|---|---|
| furmanov_chapaev_1937 | 16.5 | -0.961 | -1.005 |
| furmanov_dnevnik_1930 | 52.0 | -0.985 | -1.005 |
| gaidar_rakety_1942 | 2.5 | -0.926 | -0.952 |
| gaidar_soch2_1957 | 50.5 | -0.982 | -1.009 |
| ilf_petrov_12stulev_1928 | 99.5 | -1.062 | -1.156 |
| ostrovsky_stal_1955 | 27.0 | -0.968 | -0.992 |

Blended FN 41.3%, spread 2.5-99.5%; held-out p05 -1.011, p01 -1.060, min -1.156. By the pre-registered rule
(`ciphers/kaliningrad-2015/PREREG-KAL-RUCORP.md`) a FAIL/PASS against the in-model real_p05 of this corpus is **of unknown
reliability**; use the held-out p01/min. Worse than ru19_lat s1s (17.4%, 8.0-32.5%): six authors differ more from each other
than eight book groups of one Bible translation. The Ilf & Petrov fold's 99.5% was not diagnosed (its text reads cleanly on a
spot check); a cause is not established.

# HYPOTHESES (august-van-saksen-1561-64)

## Data conflict: System B word sign K (rule 4; logged 6 Oct 2026, A4-AVS175)
| witness | letter | direction, date | K reads | grade of the witness |
|---|---|---|---|---|
| WVO 124 f.134 vs its decipherment f.135 | 124 | Willem -> August, Brussel 16 Apr 1564 | 'der' ('dieweil K weldt' = 'dieweil der Weldt'), n=1 | C (A2-AVS3/A2-AVS4, 2 Oct 2026) |
| WVO 175 p1 interlinear gloss | 175 | Willem -> August, 9 Apr 1567 | 'die' ('vnd die armen', y~1700, gate 0.753 PASS), n=1 clean; +1 probable ('vnd die mit', y~2245, aligner chunk 'vnddie') | C for the clean one (A4-AVS175) |
| context only | 126 p4 f.139 | Willem -> August, Brussel 16 Sep 1564 | 'die' twice ('die Konnigin', 'die adern') | M (exceptions_126.tsv) |
Not settled by the more frequent value. 126 stays M at both K: its date is closer to the 'der' witness. K may be a general article sign
(der/die) in this system; that is a hypothesis, not tested. Test that would move it: a native re-look at 124 f.134's K (is it K?), or a
further K in 175 pp.3-8 or 124 under 'der'.

## R11A-AVSK (6 Oct 2026): homophonic_anneal on native 53 (prereg_avsk.md)
| family | target | control | control result | target result | verdict |
|---|---|---|---|---|---|
| homophonic (tools/homophonic_anneal.py, anneal_53n.py) | ciphertext_53.tsv native, N 364, K 21 | make_control from align_74 (K 21, N 364; exact-profile control not constructible); seeds 1-3 identical by construction | 0.992 (gate C PASS); count<=3 signs 3/6 (gate L FAIL) | 4/6 restarts converge on key_53 + 9 = f; shuffle null 9 = f 0/6 (gate S PASS); G1 = G7 = s | Q1 untestable at this N by this control (9 stays M); Q2 confirmed; no key change |

## R11A-AVS9C (6 Oct 2026): count-2 control for sign 9 (prereg_avs9c.md)
| family | target | control | control result | target result | verdict |
|---|---|---|---|---|---|
| homophonic (tools/homophonic_anneal.py, anneal_53n.py control2) | ciphertext_53.tsv native, N 364, K 21; sign 9 count 2 | make_control on 10 seed-varied 364-letter windows of de1600/briefedespfalzgr01joha (1575-82), each with >= 1 count-2 sign | share mean 0.976 (gate C PASS); count<=3 signs 6/22 = 0.273 (gate L FAIL); count-2 signs 2/12 = 0.167 (gate L2 FAIL) | R11A-AVSK's: 4/6 converge, all 9 = f; shuffle 0/6 | the annealer does not read count-2 signs at N 364 (2/12); its 9 = f is not evidence; sign 9 stays M by context; no key change |

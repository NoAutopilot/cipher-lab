"""AX-4612: write specs/lodewijk-4612.json from ciphertext_4612.tsv as transcribed (R13 draft + settle.py).
Messages = numeral runs, split only where a clear word (=...) interrupts (a line break inside a run is not a break).
Numerals 1-120 are the signs; numerals >120 are dropped (AX-NAMES: 121-149 nulls in the 1574 table; >=150 names or
word codes) and counted; the year 1574 in the date line is clear text, not a code. Nothing is repaired: the
apparently repeated stretch p1_L18/p1_L19 ('101 81|82 2 12 26 105 67 150 =Et =esperons') is kept as transcribed."""
import csv, json, collections
D = 'ciphers/lodewijk-van-nassau-1573-74/'
rows = list(csv.DictReader(open(D + 'ciphertext_4612.tsv'), delimiter='\t'))
runs, cur, dropped, clear = [], [], collections.Counter(), 0
for r in rows:
    s = r['sign']
    if s.startswith('='):
        clear += 1
        if cur: runs.append(cur); cur = []
    elif s.isdigit():
        v = int(s)
        if v == 1574: continue
        if 1 <= v <= 120: cur.append(s)
        else: dropped['121-149' if v < 150 else '>=150'] += 1
if cur: runs.append(cur)
N = sum(map(len, runs))
spec = {
 "slug": "lodewijk-van-nassau-1573-74",
 "name": "WVO 4612, Lodewijk van Nassau to Willem van Oranje, Meer, 6 March 1574 (KHA A 11/XIV d/13a; cipher numerals with clear words)",
 "language_candidates": ["fr"],
 "ciphertext_source": "ciphers/lodewijk-van-nassau-1573-74/ciphertext_4612.tsv (R13 two-pass draft of the WVO page images, settled in part by settle.py; 678 of 1170 rows confidence M) -- a transcription, not the image; a negative is conditional on it (rule 2)",
 "ciphertext_written": "26 Sept 2026, AX-4612 (ax4612/make_spec.py)",
 "ciphertext_note": f"one line per numeral run between clear words; numerals 1-120 kept as signs (N={N}); dropped as nulls/names: {dict(dropped)}; the 1574 of the date line is clear text; {clear} clear-word tokens form the frame and are not in the cipher stream. p1_L18/p1_L19 repeat an 8-numeral stretch with the same clear words, kept as transcribed (possible double reading of one line; not repaired)",
 "ciphertext": [' '.join(r) for r in runs],
 "alphabet": "numerals 1-120 (tokens separated by spaces), the table range of key.tsv; 125 distinct values in the letter overall, 100 in 1-120",
 "constraints": [
   "sibling letters 4613/4615, 4610/4611/4616 and 1574's 5810/5811/4503 read under key.tsv: 24 contiguous blocks of five values, one letter per block, order n..m (the 24-letter alphabet rotated to start at n)",
   "4612 does not read under key.tsv (4.3 pct French share, no cyclic shift; NOTES.md W1) nor under key_5799 (AX-5799)",
   "block IC (ax4612/ic_scan.py): 4612 w=5 best 0.0617 (o0; null p95 0.0567) against 0.078-0.081 for sib/5811/4610 at w=5 o0; 4612 w=6 o0 0.0737 (null p95 0.0659); values 86-100 and 106-110 nearly unused in 4612",
   "AX-NAMES (26 Sept 2026): codes 121-149 are nulls in the 1574 table"
 ],
 "cheap_tests_in_order": [
   "H1: block_homophonic width=5 offsets 0-4 (a 24-block substitution in another letter order), matched control first, gate 0.6",
   "H2: block_homophonic width=4 and width=6 (only if H1's control passes and its target fails)",
   "H3: homophonic --param profile=target (free homophonic at K=100), control first"
 ],
 "cheap_test_done": [],
 "judge": {
   "language": "fr",
   "corpora": ["tools/data/fr16/lettresdecatheri01cathuoft_djvu.txt.gz", "tools/data/fr16/lettresdecatheri02cathuoft_djvu.txt.gz", "tools/data/fr16/lettresindites00marg_djvu.txt.gz"],
   "corpora_note": "fr16: Catherine de Medicis' letters t.1-2 and Marguerite de Valois' letters -- 16th-century French court correspondence, era- and register-matched to a 1574 letter; per-fold false-negative spread in ciphers/lodewijk-van-nassau-1573-74/ax4612/fr16_folds.txt (3 source files: under rule 3's ~5-file threshold, so a FAIL/PASS is of limited reliability)"
 },
 "written": "26 Sept 2026, AX-4612 (LANE AX), for .claude/briefs/runs/2026-09-26-lane-ax-4612.md"
}
json.dump(spec, open('specs/lodewijk-4612.json', 'w'), indent=1, ensure_ascii=False)
print(N, len(runs), dict(dropped), clear, len({t for r in runs for t in r}))

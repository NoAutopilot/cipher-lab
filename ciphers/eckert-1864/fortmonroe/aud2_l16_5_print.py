"""AUD2-LEDGER16-5 (10 Oct 2026, account 1, for LANE LEDGER-16): KWIC over cached IA print-check texts (no network).
Usage: python3 aud2_l16_5_print.py VOLID REGEX [width] [maxhits]"""
import gzip, re, sys
vol, pat = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 300
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 40
t = gzip.open(f'sources/ia-fulltext/print-check/{vol}_djvu.txt.gz', 'rt', errors='replace').read()
hits = list(re.finditer(pat, t, re.I | re.S))
print(f'== {vol} /{pat}/ {len(hits)} hits')
for m in hits[:mx]:
    s = t[max(0, m.start()-w):m.end()+w].replace('\n', ' ')
    print('--', m.start(), s)

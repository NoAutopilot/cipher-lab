#!/usr/bin/env python3
"""CLEAR-SWEEP (10 Oct 2026, for LANE LEDGER-15): print pass over the cached IA djvu texts (sources/ia-fulltext/print-check, 191 volumes) for the 40 entries.
Per entry: the reading's body (text after the first colon, brackets and parentheses removed, split at them), 4-word windows letters-only, each found in a volume's
letters-only text and extended word by word to its longest shared run. Prints per entry the best (volume, run words, KWIC) and every volume with run >= 6.
A miss is a search result (rule 10). Usage: clear_sweep_print.py > clear_sweep_print.out"""
import gzip, glob, os, re, sys
sys.argv = sys.argv[:1]
from clear_sweep_hdl import R, Q
HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
ENT = [e for e in dict.fromkeys(e for e, _, _ in Q) if e != 'CTRL']
tok = lambda s: re.findall(r"[a-z]+", s.lower())
def segs(line):
    line = line.split(' | ', 3)[3]
    line = line.split(': ', 1)[1] if ': ' in line else line
    line = re.split(r'\(FM', line)[0]
    line = re.sub(r'\[[^\]]*\]', ' | ', line); line = re.sub(r'\([^)]*\)', ' | ', line)
    line = re.sub(r"signed .*$", '', line)
    return [tok(s) for s in re.split(r'\|', line) if len(tok(s)) >= 4]
S = {e: segs(R[e][1]) for e in ENT}
best = {e: [] for e in ENT}
files = sorted(glob.glob(D + '/*_djvu.txt.gz'))
print('volumes', len(files), 'entries', len(ENT), flush=True)
for f in files:
    vol = os.path.basename(f)[:-12]
    raw = gzip.open(f, 'rt', errors='ignore').read()
    t = re.sub(r'[^a-z]', '', raw.lower())
    for e in ENT:
        top = (0, None)
        for sg in S[e]:
            a = 0
            while a + 4 <= len(sg):
                ph = ''.join(sg[a:a + 4]); p = t.find(ph)
                if len(ph) >= 16 and p >= 0:
                    # extend over all occurrences (cap 5)
                    q = p; n = 0
                    while q >= 0 and n < 5:
                        k = 4
                        while a + k < len(sg) and t.startswith(''.join(sg[a:a + k + 1]), q): k += 1
                        if k > top[0]: top = (k, (a, q, ' '.join(sg[a:a + k])))
                        n += 1; q = t.find(ph, q + 1)
                    a += max(1, top[0] - 2) if top[1] and top[1][0] == a else 1
                else: a += 1
        if top[0] >= 5: best[e].append((top[0], vol, top[1][2]))
for e in ENT:
    b = sorted(best[e], reverse=True)[:4]
    print(f'== {e} ({R[e][0]})', '; '.join(f'{v} run {n}w' for n, v, _ in b) or 'no volume with a run >= 5 words')
    for n, v, ph in b[:2]: print('     ', v, n, '::', ph[:200])

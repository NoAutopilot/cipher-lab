#!/usr/bin/env python3
"""D07-NEVF25 (PREREG-D07NEVF25.md): frame-switch detector on key-no.25 figure lines, with its insertion control.

  python3 frame_switch.py lines.tsv [--seed 1] [--trials 20]

lines.tsv: line<TAB>figures (reconciled; '[...]' word codes and '?' split a line into runs; spaces, '|', '.' ignored).
Each run is decoded under ../keys/key_no25.tsv at frame 0 and frame 1 (nulls dropped, non-code pairs -> '#'); windows of
8 pairs, step 4, scored by fr16 4-gram mean (decode_f35.py's model). A switch: the leading frame changes and the new
leader leads by >= 0.3 for >= 2 consecutive windows. Control: insert one random digit at a random position of a random
run (>= 16 digits); detected if a switch is flagged within 4 pairs (8 digits) of the insertion. Gate: >= 14/20 detected
and 0 switches on the lines as read; else NON-TEST.
"""
import sys, os, re, random, argparse
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import decode_f35 as D

def key():
    K = {}
    for l in open(os.path.join(HERE, '..', 'keys', 'key_no25.tsv')):
        if l.startswith('#') or l.startswith('code'): continue
        c, v = l.rstrip('\n').split('\t')[:2]; K[c] = v
    return K

def runs(fig):
    out = []
    for part in re.split(r'\[[^\]]*\]|\?|\([^)]*\)', fig):
        d = re.sub(r'[^0-9]', '', part)
        if len(d) >= 2: out.append(d)
    return out

def dec(d, K, frame):
    pairs = [d[i:i+2] for i in range(frame, len(d) - 1, 2)]
    return [('' if K.get(p) == '-' else K.get(p, '#')) for p in pairs]

def windows(d, K, score, frame, W=8, S=4):
    v = dec(d, K, frame); res = []
    for k in range(0, max(1, len(v) - W + 1), S):
        res.append((frame + 2 * k, score(''.join(v[k:k+W]))))
    return res

def switches(d, K, score, margin=0.3):
    w0 = windows(d, K, score, 0); w1 = windows(d, K, score, 1)
    n = min(len(w0), len(w1)); diff = [w1[i][1] - w0[i][1] for i in range(n)]
    lead = [1 if x > 0 else 0 for x in diff]
    found = []
    cur = lead[0] if n else 0
    for i in range(1, n - 1):
        if lead[i] != cur and lead[i+1] == lead[i] and abs(diff[i]) >= margin and abs(diff[i+1]) >= margin:
            found.append(w0[i][0]); cur = lead[i]
    return found, diff

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('lines'); ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--trials', type=int, default=20); a = ap.parse_args()
    K = key(); score = D.model(D.corpus())
    allruns = []
    for l in open(a.lines):
        if l.startswith('#') or not l.strip(): continue
        ln, fig = l.rstrip('\n').split('\t')[:2]
        for r in runs(fig):
            sw, diff = switches(r, K, score); allruns.append((ln, r))
            print('%s run len %d: frame0 %s | switches at digit %s | diff %s' % (ln, len(r), ''.join(x or '.' for x in dec(r, K, 0)), sw, ' '.join('%.2f' % x for x in diff)))
    ndig = sum(len(r) for _, r in allruns); nsw = sum(len(switches(r, K, score)[0]) for _, r in allruns)
    rng = random.Random(a.seed); hit = 0; cand = [x for x in allruns if len(x[1]) >= 16]
    for t in range(a.trials):
        ln, r = rng.choice(cand); p = rng.randrange(2, len(r) - 2); r2 = r[:p] + str(rng.randrange(10)) + r[p:]
        sw, _ = switches(r2, K, score); ok = any(abs(s - p) <= 8 for s in sw); hit += ok
        print('control %2d %s ins@%d -> switches %s %s' % (t + 1, ln, p, sw, 'HIT' if ok else 'miss'))
    gate = hit >= 14 and nsw == 0
    print('digits %d, switches as read %d, control %d/%d -> %s' % (ndig, nsw, hit, a.trials,
          ('PASS (B: no orphan in sample)' if gate else ('control ok, switches found (A?)' if hit >= 14 else 'NON-TEST'))) + ('' if ndig >= 150 else ' [<150 digits: C]'))

if __name__ == '__main__': main()

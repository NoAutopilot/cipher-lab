#!/usr/bin/env python3
"""HEID-1623CAL (16 Oct 2026): positive-control calibration of tools/interlinear_align.py at N = 64, 85, 120, 200 with the 1623 block's
grammar (PREREG-HEID1623CAL.md). Design A = HEID-1623A poscontrol.py's random-cut design (gating); design B = fixed 2-letter chunks
(descriptive). Writes calib_runs.tsv and calib_summary.tsv here. Run from anywhere: python3 calib.py [--check]"""
import sys, os, csv, re, gzip, glob, json, random, subprocess, collections, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '../../..'))
A23 = os.path.join(HERE, '../heid1623a')
NS, SEEDS = (64, 85, 120, 200), range(1, 21)
real_sizes = [len(r['cipher_raw'].split()) for r in csv.DictReader(open(f'{A23}/pairs_1623.tsv'), delimiter='\t')]
note_lens = [len(re.sub(r'[^a-zäëïöüé]', '', w['word'].lower())) for w in csv.DictReader(
    (l for l in open(f'{A23}/note_6022_171.tsv') if not l.startswith('#')), delimiter='\t')]
note_lens = [n for n in note_lens if n > 0]
words = collections.Counter()
for f in sorted(glob.glob(f'{ROOT}/tools/data/nl16/*.txt.gz')):
    words.update(w for w in re.findall(r'[a-z]+', gzip.open(f, 'rt', encoding='utf-8', errors='ignore').read().lower()))
bylen = collections.defaultdict(list)
for w, c in words.items(): bylen[len(w)].append((w, c))
def draw_word(R, n):
    ws = bylen.get(n) or bylen[max(k for k in bylen if k <= n)]
    return R.choices([w for w, _ in ws], weights=[c for _, c in ws])[0]
def sizes(R, N):
    out = []
    while sum(out) < N: out.append(R.choice(real_sizes))
    out[-1] -= sum(out) - N
    if out[-1] < 2 and len(out) > 1: x = out.pop(); out[-1] += x
    return out
def span(R, t):
    ws = []
    while sum(map(len, ws)) < 2 * t: ws.append(draw_word(R, R.choice(note_lens)))
    return ws
class Table:
    def __init__(s, R):
        s.R = R; s.nums = [str(i) for i in range(1, 100)]; s.lets = list('abcdefghmprsxyzH'); R.shuffle(s.nums); R.shuffle(s.lets)
        s.t = {}; s.extended = 0
    def code(s, ch):
        if ch not in s.t:
            if s.lets and s.R.random() < 0.26: s.t[ch] = s.lets.pop()
            else:
                if not s.nums: s.nums = [str(i) for i in range(100 + 100 * s.extended, 200 + 100 * s.extended)]; s.extended += 1
                s.t[ch] = s.nums.pop()
        return s.t[ch]
def build(seed, N, design):
    R = random.Random(f'{seed}-{N}'); tab = Table(random.Random(f'{seed}-{N}-{design}'))
    rows = []
    for i, t in enumerate(sizes(R, N)):
        ws = span(R, t); letters = ''.join(ws)
        if design == 'A':
            cuts = sorted(R.sample(range(1, len(letters)), t - 1)) if t > 1 else []
            chunks = [letters[a:b] for a, b in zip([0] + cuts, cuts + [len(letters)])]
        else:
            chunks = [w[k:k + 2] for w in ws for k in range(0, len(w), 2)]
        rows.append((f'P{i+1}', ' '.join(ws), f'C{i+1}', ' '.join('@' + tab.code(c) for c in chunks)))
    return rows, tab.extended
def run(rows, tmp):
    p = f'{tmp}/pairs.tsv'
    with open(p, 'w') as f:
        f.write('plain_line\tplain_raw\tcipher_line\tcipher_raw\n'); f.writelines('\t'.join(r) + '\n' for r in rows)
    subprocess.run([sys.executable, 'tools/interlinear_align.py', 'align', p, f'{tmp}/a.tsv', f'{tmp}/k.tsv', '--code-prefix', '@',
                    '--code-chunk', '6', '--wildcard', '?', '--keep-fs', '--shuffle', '200', '--seed', '1623', '--shuffle-out',
                    f'{tmp}/s.json'], cwd=ROOT, check=True, capture_output=True)
    return json.load(open(f'{tmp}/s.json'))
def job(a):
    design, N, seed = a; rows, ext = build(seed, N, design)
    with tempfile.TemporaryDirectory() as tmp: s = run(rows, tmp)
    ok = s['real'] > s['p95'] and s['real'] >= 3
    r = [design, N, seed, len(rows), sum(len(x[3].split()) for x in rows), s['real'], round(s['mean'], 2), s['p95'], s['max'], ext,
         'PASS' if ok else 'FAIL']
    print(*r, sep='\t', flush=True); return r
if __name__ == '__main__':
    from multiprocessing import Pool
    with Pool(4) as pool: out = pool.map(job, [(d, N, sd) for d in ('A', 'B') for N in NS for sd in SEEDS])
    hdr = 'design\tN\tseed\tpairs\ttokens\treal\tshuf_mean\tshuf_p95\tshuf_max\tpool_ext\tgate\n'
    body = hdr + ''.join('\t'.join(map(str, r)) + '\n' for r in out)
    summ = 'design\tN\tpass\tof\tmean_tokens\tmean_real\tmean_p95\n'
    for design in ('A', 'B'):
        for N in NS:
            rs = [r for r in out if r[0] == design and r[1] == N]
            summ += f"{design}\t{N}\t{sum(r[-1]=='PASS' for r in rs)}\t{len(rs)}\t{sum(r[4] for r in rs)/len(rs):.1f}\t{sum(r[5] for r in rs)/len(rs):.2f}\t{sum(r[7] for r in rs)/len(rs):.2f}\n"
    if '--check' in sys.argv:
        ok = open(f'{HERE}/calib_runs.tsv').read() == body and open(f'{HERE}/calib_summary.tsv').read() == summ
        print('CHECK', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(f'{HERE}/calib_runs.tsv', 'w').write(body); open(f'{HERE}/calib_summary.tsv', 'w').write(summ); print(summ)

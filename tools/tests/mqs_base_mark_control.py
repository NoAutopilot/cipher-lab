#!/usr/bin/env python3
"""MQS-BASE-MARK controls (tools/tests/PREREG-MQS-BASE-MARK.md, pushed before this ran). Offline.

  python3 tools/tests/mqs_base_mark_control.py [--out tools/tests/RESULTS-MQS-BASE-MARK.tsv] [--seeds 20]

K1 round trip on the Birago 1572 atlas (cluster ids only: no key value is read or written, ASKS 118) and its permuted-sid null;
K2 one-edit reclassification on synthetic French (fr16) with a permuted-mark null; K3 the collapse guard (must-NOT).
"""
import argparse, collections, csv, glob, gzip, os, random, re, subprocess, sys, tempfile, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ATLAS = os.path.join(ROOT, 'ciphers', 'nevers-birago-fr3251-1572', 'atlas')
PY = sys.executable


def tsv(p):
    return list(csv.DictReader(open(p, newline=''), delimiter='\t'))


def wtsv(p, header, rows):
    with open(p, 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t'); w.writerow(header); w.writerows(rows)


def k1(tmp, permute_seed=None):
    signs, marks, clu = tsv(os.path.join(ATLAS, 'signs.tsv')), tsv(os.path.join(ATLAS, 'marks.tsv')), tsv(os.path.join(ATLAS, 'clusters.tsv'))
    scl = {r['id']: r['cluster'] for r in clu if r['kind'] == 'sign'}
    mcl = {r['id']: r['cluster'] for r in clu if r['kind'] == 'mark'}
    mx = {m['mid']: float(m['x']) for m in marks}
    truth = {}
    for s in signs:
        ms = sorted((m for m in s['marks'].split('|') if m), key=lambda m: mx[m])
        lab = '+'.join('m' + mcl[m] for m in ms)
        truth[s['sid']] = 'S' + scl[s['sid']] + (':' + lab if lab else '')
    mp = os.path.join(tmp, 'marks.tsv')
    rows = [dict(m) for m in marks]
    if permute_seed is not None:
        sids = [m['sid'] for m in rows]; random.Random(permute_seed).shuffle(sids)
        for m, s in zip(rows, sids):
            m['sid'] = s
    wtsv(mp, list(rows[0].keys()), [[m[k] for k in rows[0]] for m in rows])
    lp = os.path.join(tmp, 'labels.tsv'); wtsv(lp, ['sid', 'sign'], [[s, truth[s]] for s in truth])
    db = os.path.join(tmp, 'db'); os.makedirs(db, exist_ok=True)
    out = os.path.join(tmp, 'settled.tsv')
    subprocess.run([PY, os.path.join(ROOT, 'tools', 'sign_sorter_apply.py'), '--labels', lp, '--db', db, '--out', out,
                    '--split-marks', mp, '--clusters', os.path.join(ATLAS, 'clusters.tsv')], check=True, capture_output=True)
    res = tsv(out)
    ok = sum(1 for r in res if r['base'] + (':' + r['mark'] if r['mark'] else '') == truth[r['sid']])
    return ok / len(res), len(res), sum(1 for v in truth.values() if ':' in v)


def fr_text():
    txt = ''
    for f in sorted(glob.glob(os.path.join(ROOT, 'tools', 'data', 'fr16', '*.txt.gz')))[:2]:
        txt += gzip.open(f, 'rt', encoding='utf-8', errors='ignore').read()
    txt = unicodedata.normalize('NFKD', txt.lower())
    return re.sub('[^a-z]', '', ''.join(c for c in txt if not unicodedata.combining(c)))


def make_key(text):
    freq = [c for c, _ in collections.Counter(text).most_common()] + [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in text]
    plain = {c: 'B%d' % (i + 1) for i, c in enumerate(freq[:22])}
    dotted = {}
    rest = freq[22:26]
    for i, c in enumerate(rest):            # 4 rare letters: only a dotted form, on a base of another letter
        dotted[c] = ['B%d:dot' % (i + 1)]
    dotted['e'] = ['B5:dot']; dotted['a'] = ['B6:dot']   # 2 dotted homophones of frequent letters
    key = {v: c for c, v in plain.items()}
    for c, vs in dotted.items():
        for v in vs:
            key[v] = c
    return plain, dotted, key


def encipher(seg, plain, dotted, rnd):
    toks = []
    for c in seg:
        if c not in plain or (c in dotted and rnd.random() < 0.3):
            b, m = dotted[c][0].split(':')
        else:
            b, m = plain[c], ''
        toks.append([b, m])
    return toks


def decode(tmp, toks, key, merge=None):
    ct = os.path.join(tmp, 'ct.tsv'); kp = os.path.join(tmp, 'key.tsv'); tk = os.path.join(tmp, 'tok.tsv')
    wtsv(ct, ['line', 'pos', 'base', 'mark', 'conf'], [['L01', i + 1, b, m, 'H'] for i, (b, m) in enumerate(toks)])
    wtsv(kp, ['code', 'value'], sorted(key.items()))
    cmd = [PY, os.path.join(ROOT, 'tools', 'decode_key.py'), tmp, '--ciphertext', 'ct.tsv', '--key', 'key.tsv',
           '--reading', 'r.txt', '--tokens', 'tok.tsv']
    if merge:
        cmd += ['--merge-mark', merge]
    p = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return [r['value'] for r in tsv(tk)], p.stderr


def acc(vals, seg):
    return sum(1 for v, c in zip(vals, seg) if v == c) / len(seg)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--out', default=os.path.join(ROOT, 'tools', 'tests', 'RESULTS-MQS-BASE-MARK.tsv'))
    ap.add_argument('--seeds', type=int, default=20)
    a = ap.parse_args()
    rows = []
    with tempfile.TemporaryDirectory() as t:
        r, n, nm = k1(t); rows.append(['K1', 'birago-atlas', 'round_trip', '%.4f' % r, '1.000', 'PASS' if r == 1.0 else 'FAIL', f'n={n} marked={nm}'])
    with tempfile.TemporaryDirectory() as t:
        r, n, nm = k1(t, 1); rows.append(['N1', 'birago-atlas-permuted-sid', 'round_trip', '%.4f' % r, '<=0.95', 'PASS' if r <= 0.95 else 'FAIL', f'n={n} seed=1'])
    text = fr_text()
    plain, dotted, key = make_key(text)
    before, after, null, guard_hit, guard_fa = [], [], [], 0, 0
    for s in range(1, a.seeds + 1):
        rnd = random.Random(s)
        i = rnd.randrange(0, len(text) - 1500); seg = text[i:i + 1500]
        toks = encipher(seg, plain, dotted, rnd)
        for tkn in toks:
            if rnd.random() < 0.10:
                tkn[1] = '+'.join(x for x in (tkn[1], 'flourish') if x)
        def err(tt):
            return [[b, '+'.join('tick' if x == 'dot' else x for x in m.split('+') if x)] for b, m in tt]
        perm = [m for _, m in toks]; random.Random(1000 + s).shuffle(perm)
        ptoks = [[b, m] for (b, _), m in zip(toks, perm)]
        with tempfile.TemporaryDirectory() as t:
            v0, _ = decode(t, err(toks), key); before.append(acc(v0, seg))
            v1, _ = decode(t, err(toks), key, 'tick=dot,flourish'); after.append(acc(v1, seg))
            v2, _ = decode(t, err(ptoks), key, 'tick=dot,flourish'); null.append(acc(v2, seg))
            _, e3 = decode(t, toks, key, 'dot')
            named = {l.split()[2] for l in e3.splitlines() if l.startswith('merge-mark collapses')}
            guard_hit += named == {c for c in key if c.endswith(':dot')}
            _, e4 = decode(t, toks, key, 'flourish')
            guard_fa += 'merge-mark collapses' in e4
    m = lambda x: sum(x) / len(x)
    rows.append(['K2', 'fr16-synthetic-before-edit', 'accuracy', '%.4f' % m(before), '(baseline)', '', f'seeds={a.seeds} min={min(before):.4f} max={max(before):.4f}'])
    rows.append(['K2', 'fr16-synthetic-after-edit', 'accuracy', '%.4f' % m(after), '>=0.99', 'PASS' if m(after) >= 0.99 else 'FAIL', f'seeds={a.seeds} min={min(after):.4f}'])
    rows.append(['N2', 'fr16-permuted-marks-after-edit', 'accuracy', '%.4f' % m(null), '<=0.95', 'PASS' if m(null) <= 0.95 else 'FAIL', f'seeds={a.seeds} max={max(null):.4f}'])
    rows.append(['K3', 'collapse-guard', 'seeds_all_6_named', '%d/%d' % (guard_hit, a.seeds), '%d/%d' % (a.seeds, a.seeds), 'PASS' if guard_hit == a.seeds else 'FAIL', 'merge dot'])
    rows.append(['K3', 'collapse-guard-false-alarm', 'seeds_flagged', '%d/%d' % (guard_fa, a.seeds), '0/%d' % a.seeds, 'PASS' if guard_fa == 0 else 'FAIL', 'merge flourish'])
    wtsv(a.out, ['control', 'set', 'statistic', 'value', 'gate', 'verdict', 'note'], rows)
    for r in rows:
        print('\t'.join(map(str, r)))


if __name__ == '__main__':
    main()

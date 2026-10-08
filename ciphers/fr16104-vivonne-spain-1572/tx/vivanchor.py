#!/usr/bin/env python3
"""VIV-ANCHOR (8 Oct 2026): word-anchored known plaintext on ink 40 against the clerk's ink-41 decipherment, PREREG-VIVANCHOR.md.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/vivanchor.py            # control (iii), then (iv) only if it passes
    python3 ciphers/fr16104-vivonne-spain-1572/tx/vivanchor.py --control  # control only

Writes tx/vivanchor_result.json. Exit 3 = control below gate (NON-TEST), nothing assigned.
"""
import importlib.util, json, os, random, re, sys, unicodedata
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location('vk', os.path.join(HERE, 'vivk_test.py'))
vk = importlib.util.module_from_spec(spec); spec.loader.exec_module(vk)

PAGES = ('f102r', 'f102v', 'f103r')
DEC = ('f105v', 'f106r', 'f106v', 'f107r', 'f107v', 'f108r', 'f108v')
CONTROL = 'dtorcns'
ALPHA = [c for c in 'abcdefghilmnopqrstuxyz']


def stream():
    toks, pos = [], []
    for p in PAGES:
        for ln in open(os.path.join(HERE, f'{p}_rec.tsv'), encoding='utf-8'):
            if ln.startswith('row\t') or not ln.strip():
                continue
            row, rest = (ln.rstrip('\n').split('\t', 1) + [''])[:2]
            if rest.strip() == 'DUP':
                continue
            tmp = os.path.join(HERE, '.vivanchor_row.tsv')  # reuse vk.tokens() on one row so the reader is identical
            open(tmp, 'w', encoding='utf-8').write(f'{row}\t{rest}\n')
            for i, t in enumerate(vk.tokens(tmp)):
                if re.fullmatch(r'\{.*\}', t):
                    continue
                toks.append(t); pos.append(f'{p}:{row}:{i}')
            os.remove(tmp)
    return toks, pos


def fold(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn').replace('j', 'i').replace('v', 'u')


def vocab():
    W = set()
    for d in DEC:
        s = open(os.path.join(HERE, f'dec_{d}_merged.txt'), encoding='utf-8').read()
        s = re.sub(r'\{del:[^}]*\}', ' ', s)
        s = re.sub(r'\{add:([^}]*)\}', r'\1', s)
        for w in re.split(r"[\s'/’]+", s):
            if not w or any(c in w for c in '<?['):
                continue
            w = re.sub('[^a-z]', '', fold(w))
            if len(w) >= 7:
                W.add(w)
    return sorted(W)


def key():
    k = {}
    for ln in open(os.path.join(T, 'key_tomokiyo.tsv'), encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] == 'code' or len(f) < 2:
            continue
        k[f[0]] = fold(f[1])
    return k


def anchor(toks, W, k, X):
    """unique positions -> (label, is_qu) at X slots of anchoring windows; also number of anchoring windows."""
    hits, nwin = {}, 0
    D = ''.join(k.get(t) or '_' for t in toks)  # one char per token; keyed values are single letters
    for w in W:
        if X not in w:
            continue
        tslots = [i for i, c in enumerate(w) if c == X]
        pat = re.compile('(?=' + ''.join('.' if c == X else c for c in w) + ')')
        for m in pat.finditer(D):
            s = m.start(); nwin += 1
            for i in tslots:
                hits.setdefault(s + i, (toks[s + i], i > 0 and w[i - 1] == 'q'))
    return hits, nwin


def control(toks, pos, W, k):
    out, rec = {}, 0
    for X in CONTROL:
        kh = {c: v for c, v in k.items() if v != X}
        own = {c for c, v in k.items() if v == X}
        hits, nwin = anchor(toks, W, kh, X)
        labs = Counter(l for l, _ in hits.values())
        n = len(hits); share = sum(labs[c] for c in own) / n if n else 0.0
        ok = n >= 3 and share >= 2 / 3
        rec += ok
        out[X] = {'n': n, 'windows': nwin, 'own_labels': sorted(own), 'share_own': round(share, 3), 'recovers': ok,
                  'labels': dict(labs.most_common())}
    return {'per_letter': out, 'recovered': rec, 'of': len(CONTROL), 'gate': '>= 5 of 7', 'pass': rec >= 5}


def null_windows(toks, W, k, n=20):
    rng = random.Random('20261008VA-null'); res = []
    for _ in range(n):
        sh = list(toks); rng.shuffle(sh)
        res.append(sum(anchor(sh, W, k, X)[1] for X in ALPHA))
    return sorted(res)


def targets(toks, pos, W, k):
    per_pos = defaultdict(set); lab = {}; qu = set(); nwin = 0
    for X in ALPHA:
        hits, nw = anchor(toks, W, k, X); nwin += nw
        for p, (l, isq) in hits.items():
            per_pos[p].add(X); lab[p] = l
            if X == 'u' and isq:
                qu.add(p)
    vals = {p: next(iter(v)) for p, v in per_pos.items() if len(v) == 1}
    res = {'anchoring_windows': nwin, 'positions': len(vals), 'dropped_conflicting': sum(len(v) > 1 for v in per_pos.values())}
    # label-centric
    U = sorted({lab[p] for p in vals if lab[p] not in k})
    lc = {}
    for L in U:
        ps = [p for p in vals if lab[p] == L]
        c = Counter(vals[p] for p in ps)
        v, nv = c.most_common(1)[0]
        ok = nv >= 3 and nv / len(ps) >= 2 / 3
        lc[L] = {'n': len(ps), 'values': dict(c.most_common()), 'assign': v if ok else None,
                 'positions': [pos[p] for p in ps if vals[p] == v] if ok else [pos[p] for p in ps]}
    res['label_centric'] = lc
    # cell-centric
    cc = {}
    for cell in ('f', 'm', 'p', 'qu'):
        ps = [p for p in vals if (p in qu if cell == 'qu' else vals[p] == cell)]
        c = Counter(lab[p] for p in ps)
        top = c.most_common(1)[0] if c else (None, 0)
        ok = top[1] >= 3 and top[1] / max(1, len(ps)) >= 2 / 3
        cc[cell] = {'n': len(ps), 'labels': dict(c.most_common()), 'assign': top[0] if ok else None,
                    'conflict': bool(ok and top[0] in k), 'positions': {l: [pos[p] for p in ps if lab[p] == l] for l in c}}
    res['cell_centric'] = cc
    return res


def main():
    toks, pos = stream(); W = vocab(); k = key()
    res = {'tokens': len(toks), 'vocab_ge7': len(W)}
    res['control'] = control(toks, pos, W, k)
    print(json.dumps({'tokens': len(toks), 'vocab': len(W)}))
    for X, r in res['control']['per_letter'].items():
        print('control', X, 'n', r['n'], 'share_own', r['share_own'], 'recovers', r['recovers'], r['labels'])
    print('control recovered', res['control']['recovered'], 'of 7 ->', 'PASS' if res['control']['pass'] else 'NON-TEST')
    out = os.path.join(HERE, 'vivanchor_result.json')
    if not res['control']['pass']:
        json.dump(res, open(out, 'w'), indent=1); sys.exit(3)
    if '--control' in sys.argv:
        json.dump(res, open(out, 'w'), indent=1); return
    res['target'] = targets(toks, pos, W, k)
    nl = null_windows(toks, W, k)
    res['null_windows_shuffled'] = {'n': len(nl), 'median': nl[len(nl) // 2], 'max': nl[-1]}
    json.dump(res, open(out, 'w'), indent=1)
    t = res['target']
    print('target windows', t['anchoring_windows'], 'positions', t['positions'], 'null windows median/max',
          res['null_windows_shuffled']['median'], res['null_windows_shuffled']['max'])
    for L, r in t['label_centric'].items():
        print('label', L, 'n', r['n'], r['values'], '->', r['assign'])
    for c, r in t['cell_centric'].items():
        print('cell', c, 'n', r['n'], r['labels'], '->', r['assign'], 'CONFLICT' if r['conflict'] else '')


if __name__ == '__main__':
    main()

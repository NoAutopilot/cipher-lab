#!/usr/bin/env python3
"""GAPS90 Tausug word-list match on ciphertext_fig1.txt (see PREREG.md in this folder).

Usage: match.py --cowie COWIE_DJVU_TXT --nt NT_READALOUD_DIR [--perms 1000] [--seed 1] [--out results.json]
The two sources are fetched to a scratch dir (URLs in manifest.json); neither is committed.
"""
import argparse, glob, json, os, random, re, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
CT = os.path.join(HERE, '..', 'ciphertext_fig1.txt')
CLASSES = list('btdkNnmlrshjp')
SIGN = {'ha': 'h', 'ha2': 'h', 'kha': 'h', 'lam': 'l', 'dal': 'd', 'sin': 's', 'shin': 's', 'sad': 's',
        'tha': 's', 'ta': 't', 'kaf': 'k', 'fa': 'p', 'ba': 'b', 'ra': 'r', 'ghayn': 'N', 'nga': 'N',
        'nun': 'n', 'mim': 'm', 'lamalif': 'l', 'jim': 'j', 'qaf': 'k',
        'waw': '', 'alif': '', 'hamza': '', 'ya': '', 'ain': '', 'tooth': '*'}
TOOTH = ['b', 't', 'n', 's', '']


def read_target():
    lines = []
    for raw in open(CT, encoding='utf-8'):
        if not re.match(r'^L\d\d:', raw):
            continue
        groups = []
        for g in raw.split(':', 1)[1].split('|'):
            toks = [t.rstrip('?') for t in g.split()]
            if not toks or 'OBSCURED' in toks:
                groups.append(None)
                continue
            groups.append([SIGN[t] for t in toks if SIGN[t]])
        lines.append(groups)
    return lines


def roman_skel(w):
    w = unicodedata.normalize('NFKD', w.lower())
    w = ''.join(c for c in w if c.isalpha())
    w = w.replace('ng', 'N').replace('sy', 's').replace('sh', 's').replace('ch', 'j')
    tr = {'b': 'b', 'p': 'p', 'f': 'p', 'v': 'b', 't': 't', 'd': 'd', 'k': 'k', 'g': 'k', 'q': 'k', 'c': 'j',
          'j': 'j', 'h': 'h', 'l': 'l', 'm': 'm', 'n': 'n', 'N': 'N', 'r': 'r', 's': 's', 'z': 's', 'x': 'ks'}
    return ''.join(tr.get(c, '') for c in w)


def cowie_list(path):
    txt = open(path, encoding='utf-8', errors='replace').read().split('\n')
    start = next(i for i, l in enumerate(txt) if l.strip() == 'Abandon')
    eng = set()
    words = set()
    for l in txt[start:]:
        for t in l.split():
            if t[:1].isupper():
                eng.add(t.strip('.,;:()').lower())
    for l in txt[start:]:
        for t in re.split(r'[\s,;:()]+', l):
            t = t.strip('.\'"*')
            if re.fullmatch(r"[a-z][a-z'\-]{2,}", t) and t.replace('-', '') not in eng:
                words.add(t.replace('-', ''))
    return words


def nt_words(d, held_out=False):
    out = []
    for f in sorted(glob.glob(os.path.join(d, 'tsg_*_read.txt'))):
        is_rev = '_REV_' in f
        if is_rev != held_out:
            continue
        for l in open(f, encoding='utf-8-sig').read().split('\n')[2:]:
            out += [w for w in re.findall(r"[^\W\d_]+", l)]
    return out


def skelset(words, minlen=2):
    return {s for s in (roman_skel(w) for w in words) if len(s) >= minlen}


def span_skels(signs):
    outs = ['']
    for c in signs:
        opts = TOOTH if c == '*' else [c]
        outs = [o + x for o in outs for x in opts]
    return outs


def score(lines, S, minlen):
    covered = total = 0
    chosen = {2: 0, 3: 0, 4: 0}
    single = {2: 0, 3: 0, 4: 0}
    for groups in lines:
        n = len(groups)
        total += sum(len(g) for g in groups if g)
        best = [(0, [])] * (n + 1)
        for i in range(1, n + 1):
            best[i] = best[i - 1]
            for k in (1, 2, 3):
                j = i - k
                if j < 0 or any(g is None for g in groups[j:i]):
                    continue
                signs = [c for g in groups[j:i] for c in g]
                hit = 0
                for s in span_skels(signs):
                    if len(s) >= minlen and s in S:
                        hit = max(hit, len(s))
                if hit and best[j][0] + hit > best[i][0]:
                    best[i] = (best[j][0] + hit, best[j][1] + [hit])
                if k == 1 and hit:
                    single[min(hit, 4)] += 1
        covered += best[n][0]
        for L in best[n][1]:
            chosen[min(L, 4)] += 1
    return covered / max(total, 1), chosen, single, total


def permute(lines, rng):
    p = CLASSES[:]
    rng.shuffle(p)
    m = dict(zip(CLASSES, p))
    m['*'] = '*'
    return [[None if g is None else [m[c] for c in g] for g in groups] for groups in lines]


def render(words, target_cons, nlines, rng, noise):
    """Tausug words -> Jawi-like groups (break after a non-joiner), cut to target_cons consonants."""
    groups_flat = []
    cons = 0
    for w in words:
        w2 = unicodedata.normalize('NFKD', w.lower())
        w2 = ''.join(c for c in w2 if c.isalpha())
        w2 = w2.replace('ng', 'N')
        signs = []
        for i, ch in enumerate(w2):
            if ch == 'a':
                if i in (0, len(w2) - 1):
                    signs.append(('', 'nj'))
            elif ch in 'iey':
                signs.append(('', ''))
            elif ch in 'uow':
                signs.append(('', 'nj'))
            else:
                c = roman_skel(ch) if ch != 'N' else 'N'
                if c:
                    nj = 'nj' if c in 'dr' else ''
                    if noise and rng.random() < noise:
                        c = rng.choice([x for x in CLASSES if x != c])
                    signs.append((c, nj))
        g = []
        for c, nj in signs:
            if c:
                g.append(c)
                cons += 1
            if nj:
                groups_flat.append(g)
                g = []
        groups_flat.append(g)
        groups_flat.append('WB')
        if cons >= target_cons:
            break
    groups_flat = [g for g in groups_flat if g != 'WB']
    per = max(1, len(groups_flat) // nlines)
    return [groups_flat[i:i + per] for i in range(0, len(groups_flat), per)]


def pval(lines, S, minlen, perms, rng):
    t = score(lines, S, minlen)[0]
    ge = sum(score(permute(lines, rng), S, minlen)[0] >= t for _ in range(perms))
    return t, ge / perms


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cowie', required=True)
    ap.add_argument('--nt', required=True)
    ap.add_argument('--perms', type=int, default=1000)
    ap.add_argument('--ctrl-perms', type=int, default=200)
    ap.add_argument('--chunks', type=int, default=20)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--out')
    a = ap.parse_args()
    rng = random.Random(a.seed)
    target = read_target()
    lists = {'L_PD_cowie1893': skelset(cowie_list(a.cowie)), 'L_NT_minusREV': skelset(nt_words(a.nt))}
    held = nt_words(a.nt, held_out=True)
    tcons = sum(len(g) for gs in target for g in gs if g)
    res = {'target_consonants': tcons, 'lists': {}}
    for name, S in lists.items():
        r = {'n_skeletons': len(S)}
        for minlen, tag in ((3, 'C3'), (2, 'C2')):
            c, chosen, single, _ = score(target, S, minlen)
            nulls = sorted(score(permute(target, rng), S, minlen)[0] for _ in range(a.perms))
            r[tag] = {'target': round(c, 4), 'chosen_spans_by_L': chosen, 'singleton_matches_by_L': single,
                      'null_mean': round(sum(nulls) / len(nulls), 4), 'null_p95': round(nulls[int(.95 * len(nulls))], 4),
                      'p': sum(x >= c for x in nulls) / len(nulls)}
        ctrl = {}
        for noise in (0.0, 0.1, 0.2):
            vals = []
            for k in range(a.chunks):
                off = rng.randrange(0, len(held) - 400)
                lines = render(held[off:], tcons, 7, rng, noise)
                c, p = pval(lines, S, 3, a.ctrl_perms, rng)
                vals.append((c, p))
            ctrl[str(noise)] = {'C3_mean': round(sum(v[0] for v in vals) / len(vals), 4),
                                'power_p<0.05': sum(v[1] < 0.05 for v in vals) / len(vals)}
        r['positive_control_C3'] = ctrl
        r['gate'] = 'PASS' if (r['C3']['p'] < 0.05 and ctrl['0.2']['power_p<0.05'] >= 0.8) else (
            'NON-TEST (power<0.8 at 20pct)' if ctrl['0.2']['power_p<0.05'] < 0.8 else 'FAIL')
        res['lists'][name] = r
    js = json.dumps(res, indent=1)
    print(js)
    if a.out:
        open(a.out, 'w').write(js + '\n')


if __name__ == '__main__':
    main()

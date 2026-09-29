#!/usr/bin/env python3
"""DEB-SWARM-0 (29 Sept 2026): build the five synthetic controls shaped like c1 and c2, plus the blind set for group D.

Shape: the same number of lines and signs per line as the settled c1 and c2 (score.py's loader: `_`, MULTI and clear
spans dropped), and a sign-count curve drawn from the pooled c1+c2 rank-frequency curve (the pooled counts are the
same list inventory_settled.tsv gives for these two cryptograms). Sign ids are synthetic (S001...), never Debosnys's
own ids. Plaintexts come from verse NOT in swarm/corpora/ (so a scorer cannot win by memorising its own corpus).

Writes controls/<ID>.tsv (line, position, sign) and controls/sealed/<ID>.tsv (line, position, value), controls/
SHAPE.json (per control: N, K, and the Spearman correlation of its count curve with the real one, no plaintext),
and the blind set controls/B1..B5.tsv with the design of each only in controls/sealed/BLIND.tsv.
Usage: make_controls.py --gut DIR   (DIR holds the pg<id>.txt plaintext sources listed in PLAIN below)"""
import argparse, collections, json, pathlib, random, re, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import score  # noqa: E402
from build_corpora import body  # noqa: E402

NOISE = 0.15  # each token replaced, with this probability, by a sign drawn from the pooled curve (h13 'coarse' style)


def real_shape():
    c1, c2 = score.load_real('c1'), score.load_real('c2')
    pooled = collections.Counter(score.flat(c1) + score.flat(c2))
    return [len(v) for v in c1.values()], [len(v) for v in c2.values()], sorted(pooled.values(), reverse=True)


def verse_lines(path, skip):
    t = body(open(path, encoding='utf-8', errors='replace').read())
    ls = [l.strip() for l in t.split('\n')]
    ls = [l for l in ls if 12 <= len(l) <= 70 and not l.isupper() and re.search(r'[a-zà-ÿ]', l)]
    return ls[skip:]


def letters_from(lines, n):
    s = ''
    for l in lines:
        s += score.fold(l)
        if len(s) >= n:
            return s[:n]
    sys.exit('plaintext too short')


def homophonic(plain, curve, rng):
    need = collections.Counter(plain)
    alloc = collections.defaultdict(list)  # letter -> [(sign, weight)]
    rem = dict(need)
    for i, c in enumerate(curve):
        L = max(rem, key=lambda k: rem[k])
        alloc[L].append((f'S{i + 1:03d}', c))
        rem[L] -= c
    for L in need:  # every letter needs one homophone
        if not alloc[L]:
            donor = max(alloc, key=lambda k: len(alloc[k]))
            alloc[L].append(alloc[donor].pop())
    bags = {}
    for L, n in need.items():
        hs = alloc[L]
        w = sum(c for _, c in hs)
        share = [(s, n * c / w) for s, c in hs]
        cnt = {s: int(x) for s, x in share}
        left = n - sum(cnt.values())
        for s, x in sorted(share, key=lambda t: -(t[1] - int(t[1])))[:left]:
            cnt[s] += 1
        bag = [s for s, k in cnt.items() for _ in range(k)]
        rng.shuffle(bag)
        bags[L] = bag
    return [bags[ch].pop() for ch in plain], list(plain)


FUNC = ['de', 'la', 'le', 'et', 'les', 'que', 'je', 'un', 'des', 'en', 'il', 'est', 'qui', 'pas', 'ne', 'mon', 'vous']


def syllabify(w):
    parts = re.findall(r'[^aeiouy]*[aeiouy]+(?:[^aeiouy]+$|[^aeiouy](?=[^aeiouy]))?', w)
    return parts if ''.join(parts) == w else [w]


def units_of(lines, nsyl):
    words = [score.fold(x) for l in lines for x in re.split(r"[\s'’\-]+", l)]
    words = [w for w in words if w]
    sylfreq = collections.Counter(s for w in words if w not in FUNC for s in syllabify(w))
    top = {s for s, _ in sylfreq.most_common(nsyl)}
    out = []
    for w in words:
        if w in FUNC:
            out.append(w)
        else:
            for s in syllabify(w):
                out.extend([s] if s in top else list(s))
    return out


def syllabic(lines, n, K, rng):
    best = None
    for nsyl in range(20, 400, 5):
        u = units_of(lines, nsyl)[:n]
        d = len(set(u))
        if best is None or abs(d - K) < abs(best[1] - K):
            best = (u, d)
        if d > K:
            break
    u = best[0]
    ranks = [x for x, _ in collections.Counter(u).most_common()]
    ids = list(range(1, len(ranks) + 1))
    rng.shuffle(ids)
    sign = {x: f'S{i:03d}' for x, i in zip(ranks, ids)}
    return [sign[x] for x in u], u


def null_text(curve, lens, rng):
    bag = [f'S{i + 1:03d}' for i, c in enumerate(curve) for _ in range(c)]
    rng.shuffle(bag)
    bag = bag[:sum(lens)]
    # couplet rhyme: in about half the couplets the second line ends on the first line's final sign (h8: 5/10 within)
    starts = [sum(lens[:i]) for i in range(len(lens))]
    for k in range(0, len(lens) - 1, 2):
        if rng.random() < 0.5:
            a = starts[k] + lens[k] - 1
            b = starts[k + 1] + lens[k + 1] - 1
            want = bag[a]
            if bag[b] != want:
                j = next((j for j in rng.sample(range(len(bag)), len(bag)) if bag[j] == want and j not in (a, b)), None)
                if j is not None:
                    bag[b], bag[j] = bag[j], bag[b]
    return bag, None


def write(cid, signs, vals, l1, l2, dest=HERE / 'controls'):
    rows, srows = ['line\tposition\tsign'], ['line\tposition\tvalue']
    i = 0
    for part, lens in (('c1', l1), ('c2', l2)):
        for li, n in enumerate(lens):
            for p in range(n):
                rows.append(f'{part}_L{li + 1:02d}\t{p + 1}\t{signs[i]}')
                srows.append(f'{part}_L{li + 1:02d}\t{p + 1}\t{vals[i] if vals else ""}')
                i += 1
    (dest / f'{cid}.tsv').write_text('\n'.join(rows) + '\n')
    (dest / 'sealed' / f'{cid}.tsv').write_text('\n'.join(srows) + '\n')


def spearman(a, b):
    n = min(len(a), len(b))
    a, b = a[:n], b[:n]
    return round(1 - 6 * sum((x - y) ** 2 for x, y in zip(range(n), range(n))) / (n * (n * n - 1)), 3) if n > 2 else None


def build(design, src, skip, l1, l2, curve, seed):
    rng = random.Random(seed)
    N = sum(l1) + sum(l2)
    if design == 'NULL':
        return null_text(curve, l1 + l2, rng)
    lines = verse_lines(src, skip)
    if design.endswith('HOMO'):
        return homophonic(letters_from(lines, N), curve, rng)
    return syllabic(lines, N, len(curve), rng)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--gut', required=True); a = ap.parse_args()
    G = pathlib.Path(a.gut)
    l1, l2, curve = real_shape()
    SRC = json.loads((HERE / 'controls' / 'PLAINTEXT_SOURCES.json').read_text())
    shape = {'real': {'lines_c1': l1, 'lines_c2': l2, 'N': sum(l1) + sum(l2), 'K_pooled': len(curve), 'top10': curve[:10]}}
    for design in ('FR-HOMO', 'EN-HOMO', 'PT-HOMO', 'FR-SYLL', 'NULL'):
        s = SRC.get(design)
        signs, vals = build(design, G / f"pg{s['gutenberg']}.txt" if s else None, s['skip_lines'] if s else 0, l1, l2, curve, 1000 + len(design))
        write(design, signs, vals, l1, l2)
        c = sorted(collections.Counter(signs).values(), reverse=True)
        shape[design] = {'N': len(signs), 'K': len(c), 'top10': c[:10]}
        if design != 'NULL':  # rule 3 (SALV-DIAG): bracket the target's measured 14-18 pct transcription noise
            nrng = random.Random(77 + len(design))
            pool = [f'S{i + 1:03d}' for i, c0 in enumerate(curve) for _ in range(c0)] if design.endswith('HOMO') else list(signs)
            noisy = [nrng.choice(pool) if nrng.random() < NOISE else x for x in signs]
            write(f'{design}-N15', noisy, vals, l1, l2)
            c = sorted(collections.Counter(noisy).values(), reverse=True)
            shape[f'{design}-N15'] = {'N': len(noisy), 'K': len(c), 'top10': c[:10], 'noise': NOISE}
    rng = random.Random(4242)
    order = ['FR-HOMO', 'EN-HOMO', 'PT-HOMO', 'FR-SYLL', 'NULL']
    rng.shuffle(order)
    blind = ['id\tdesign']
    for i, design in enumerate(order):
        s = SRC.get(design)
        signs, vals = build(design, G / f"pg{s['gutenberg']}.txt" if s else None, (s['skip_lines'] + 400) if s else 0, l1, l2, curve, 9000 + i)
        if design != 'NULL':  # the blind set carries the target's noise too, so D cannot key on cleanliness
            nrng = random.Random(500 + i)
            pool = [f'S{j + 1:03d}' for j, c0 in enumerate(curve) for _ in range(c0)] if design.endswith('HOMO') else list(signs)
            signs = [nrng.choice(pool) if nrng.random() < NOISE else x for x in signs]
        write(f'B{i + 1}', signs, vals, l1, l2)
        blind.append(f'B{i + 1}\t{design}')
    (HERE / 'controls' / 'sealed' / 'BLIND.tsv').write_text('\n'.join(blind) + '\n')
    (HERE / 'controls' / 'SHAPE.json').write_text(json.dumps(shape, indent=1) + '\n')
    print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != 'top10'} for k, v in shape.items()}))

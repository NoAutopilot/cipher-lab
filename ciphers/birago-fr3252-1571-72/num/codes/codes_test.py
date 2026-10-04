"""N8-BIRNUM (4 Oct 2026): dotted groups (family D) and 1x/5x/8x units (family U) as nomenclator codes.
Flank-repetition statistic T vs random-position null, plus a synthetic power control. Rules: PREREG.md (pushed first).
Usage: python3 codes_test.py [--trials 20]  -> prints results; writes out.txt beside it."""
import sys, random, gzip, re, collections, argparse
from pathlib import Path
HERE = Path(__file__).resolve().parent
NUM = HERE.parent
ROOT = HERE.parents[3]
LETTERS = set('mnhfcal')

def tokens(path):
    out = []
    for line in Path(path).read_text().split('\n'):
        out.extend(line.split())
    return out

def parse_f100(toks):
    """-> list of items: ('d',digit) plain, ('g',pair) dotted group, ('b',) break."""
    items, i = [], 0
    dotted = lambda t: t == 'i' or (len(t) == 2 and t[0].isdigit() and t[1] in '.:')
    while i < len(toks):
        t = toks[i]
        if dotted(t):
            run = []
            while i < len(toks) and dotted(toks[i]):
                run.append('1' if toks[i] == 'i' else toks[i][0]); i += 1
            for k in range(0, len(run) - 1, 2):
                items.append(('g', run[k] + run[k + 1]))
            continue
        if t in ('|', 'CLEAR') or t.isalpha():
            items.append(('b',))
        elif t[0].isdigit():
            items.append(('d', t[0]))  # other marks (':' handled above; '5:' etc) -> plain digit
        else:
            items.append(('b',))
        i += 1
    return items

def parse_f119(toks):
    items, i = [], 0
    dm = lambda t: len(t) == 2 and t[0].isdigit() and t[1] in '.:'
    while i < len(toks):
        t = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else ''
        if t == '2~' and nxt == '5-':
            items.append(('g', '25')); i += 2; continue
        if dm(t) and dm(nxt):
            items.append(('g', t[0] + nxt[0])); i += 2; continue
        if len(t) == 2 and t[1] == '.' and nxt == '1':
            items.append(('g', t[0] + '1')); i += 2; continue
        if t in ('|', 'CLEAR') or t.isalpha():
            items.append(('b',))
        elif t[0].isdigit():
            items.append(('d', t[0]))
        else:
            items.append(('b',))
        i += 1
    return items

def segments(items):
    """Split into segments at breaks; each segment is a list of ('d',x) or ('g',xy)."""
    segs, cur = [], []
    for it in items:
        if it[0] == 'b':
            if cur: segs.append(cur)
            cur = []
        else:
            cur.append(it)
    if cur: segs.append(cur)
    return segs

def parse158(digs):
    units, i = [], 0
    while i < len(digs):
        if digs[i] in '158' and i + 1 < len(digs):
            units.append(digs[i:i + 2]); i += 2
        else:
            units.append(digs[i]); i += 1
    return units

def occurrences(segs, family):
    """-> streams (list of digit strings with candidate units marked as spans), occ dict type->[(seg, start, end)]."""
    streams, occ = [], collections.defaultdict(list)
    for si, seg in enumerate(segs):
        s, spans = '', []
        if family == 'D':
            for it in seg:
                if it[0] == 'g':
                    spans.append((len(s), len(s) + 2, it[1])); s += it[1]
                else:
                    s += it[1]
        else:  # U: groups removed (break the stream), 158 parse of plain sub-runs
            sub = ''
            def flush():
                nonlocal s, sub
                pos = len(s)
                for u in parse158(sub):
                    if len(u) == 2: spans.append((pos, pos + 2, u))
                    pos += len(u)
                s += sub; sub = ''
            for it in seg:
                if it[0] == 'g':
                    flush(); s += '##'  # opaque, breaks flanks
                else:
                    sub += it[1]
            flush()
        streams.append(s)
        for a, b, t in spans:
            occ[t].append((si, a, b))
    return streams, occ

def flanks(stream, a, b, blocked):
    L = stream[a - 2:a] if a >= 2 else None
    R = stream[b:b + 2] if b + 2 <= len(stream) else None
    if L is not None and ('#' in L or any(p in blocked for p in (a - 2, a - 1))): L = None
    if R is not None and ('#' in R or any(p in blocked for p in (b, b + 1))): R = None
    return L, R

def T_stat(streams, occlists):
    """occlists: dict type -> [(seg,a,b)]; blocked positions = all candidate spans."""
    blocked = collections.defaultdict(set)
    for lst in occlists.values():
        for si, a, b in lst: blocked[si].update((a, a + 1))
    T, per = 0, {}
    for t, lst in occlists.items():
        Ls, Rs = collections.Counter(), collections.Counter()
        for si, a, b in lst:
            own = blocked[si] - {a, a + 1}
            L, R = flanks(streams[si], a, b, own)
            if L: Ls[L] += 1
            if R: Rs[R] += 1
        m = max([0] + list(Ls.values()) + list(Rs.values()))
        s = max(0, m - 1); per[t] = (len(lst), s); T += s
    return T, per

def null_T(streams, occ, draws, rng):
    free = [(si, a) for si, s in enumerate(streams) for a in range(len(s) - 1) if s[a:a + 2].isdigit()]
    out = []
    for _ in range(draws):
        used = collections.defaultdict(set); fake = {}
        for t, lst in occ.items():
            fl = []
            while len(fl) < len(lst):
                si, a = rng.choice(free)
                if a in used[si] or a + 1 in used[si]: continue
                used[si].update((a, a + 1)); fl.append((si, a, a + 2))
            fake[t] = fl
        out.append(T_stat(streams, fake)[0])
    out.sort()
    return out

def pct(v, q): return v[min(len(v) - 1, int(q * len(v)))]

def select(occ, family):
    if family == 'D': return {t: l for t, l in occ.items() if len(l) >= 2}
    return {t: l for t, l in occ.items() if 2 <= len(l) <= 8}

# ---------- synthetic power control ----------
def corpus_text():
    d = ROOT / 'tools' / 'data' / 'it16dip'
    txt = ''
    for f in sorted(d.glob('*.txt.gz')):
        txt += gzip.open(f, 'rt', errors='ignore').read().lower() + ' '
    txt = txt.replace('v', 'u').replace('j', 'i')
    return re.sub(r'[^a-z ]+', ' ', txt)

def synth_trial(words, seed, draws):
    rng = random.Random(seed)
    # span of ~520 letters
    start = rng.randrange(0, len(words) - 400)
    span, n = [], 0
    for w in words[start:]:
        span.append(w); n += len(w)
        if n >= 520: break
    c = collections.Counter(w for w in span if len(w) >= 4)
    top = [w for w, k in c.most_common() if k >= 3][:3]
    cells_all = [a + b for a in '01234589' for b in '01234589']
    rng.shuffle(cells_all)
    codes = {w: cells_all.pop() for w in top}
    freq = collections.Counter(''.join(w for w in span if w not in codes))
    letters = sorted(freq, key=lambda x: -freq[x])
    table = {l: [cells_all.pop()] for l in letters}
    extra = 40 - len(letters)
    for k in range(max(0, extra)):
        table[letters[k % len(letters)]].append(cells_all.pop())
    items = []
    for w in span:
        if w in codes:
            items.append(('g', codes[w])); continue
        for ch in w:
            for d in rng.choice(table[ch]): items.append(('d', d))
            if rng.random() < 0.05: items.append(('d', rng.choice('01234589')))
    segs = [items]
    streams, occ = occurrences(segs, 'D')
    occ = select(occ, 'D')
    if not occ: return None
    T, _ = T_stat(streams, occ)
    nl = null_T(streams, occ, draws, rng)
    return T, pct(nl, 0.99), len(top), sum(len(v) for v in occ.values())

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--trials', type=int, default=20); ap.add_argument('--draws', type=int, default=2000)
    a = ap.parse_args()
    lines = []
    p = lambda *x: (print(*x), lines.append(' '.join(str(y) for y in x)))
    segs = segments(parse_f100(tokens(NUM / 'f100_recon.txt'))) + segments(parse_f119(tokens(NUM / 'f119_ct2_bourdeau.txt')))
    for fam in ('D', 'U'):
        streams, occ = occurrences(segs, fam)
        occ = select(occ, fam)
        T, per = T_stat(streams, occ)
        nl = null_T(streams, occ, a.draws, random.Random(20261004))
        p(f'family {fam}: types {len(occ)}, occurrences {sum(len(v) for v in occ.values())}, T={T}, '
          f'null mean {sum(nl)/len(nl):.2f} p95 {pct(nl,0.95)} p99 {pct(nl,0.99)} max {nl[-1]}, '
          f'p(T>=real) {sum(x>=T for x in nl)/len(nl):.4f} -> {"PASS" if T > pct(nl,0.99) else "no pass"}')
        p('  per type (n, s):', ' '.join(f'{t}:{n},{s}' for t, (n, s) in sorted(per.items(), key=lambda x: -x[1][0])))
    words = corpus_text().split()
    hits, rows = 0, []
    for s in range(1, a.trials + 1):
        r = synth_trial(words, s, 500)
        if r is None: rows.append(f'{s}:none'); continue
        T, p99, ncode, nocc = r
        hits += T > p99; rows.append(f'{s}:T{T}/p99 {p99}/occ{nocc}')
    p(f'power control (40 cells, 5% strays, 3 planted word codes): {hits}/{a.trials} trials T > own null p99')
    p('  trials:', ' '.join(rows))
    (HERE / 'out.txt').write_text('\n'.join(lines) + '\n')

if __name__ == '__main__':
    main()

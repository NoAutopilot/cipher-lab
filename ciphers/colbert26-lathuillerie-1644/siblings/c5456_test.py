"""A2-COL17: key_f23.tsv C codes on canvas 54, 55 and 56 (folio 50-52, La Thuillerie to Servien, La Haye; canvas 54 opens a letter
docketed "24 Janvier 1648", canvas 56 closes "A la Haye le 27e Janvier 1648") against each leaf's own interlinear gloss.
Pre-registered 3 Oct 2026 (copy of c5051_test.py, statistic, control, gate and floor unchanged), committed BEFORE the canvas 54-56 crops
were cut or any blind pass was read.
Input: siblings/c5456_reconciled.tsv (columns: line, tokens, gloss, note; line ids '54a01', '55b03' ... carry the canvas).
Statistic (unchanged): per numeral line, the ordered greedy walk -- a code scores if its key_f23 value occurs in that line's gloss
(letters only, lowercase, v->u, j->i) at or after the end of the previous match. Primary set C-grade codes; secondary C+M.
UNITS: canvas 54, 55 and 56 are each scored ALONE, each with its own gate, never pooled with each other or with earlier units.
Also reported, NOT gating: 'letter5456' (54+55+56 together).
GATE per canvas: the LENGTH-MATCHED f23-window control -- each line's gloss replaced by a random window of the same length cut from
the f.23 main-text gloss bank (interlinear/f23w_pairs.tsv), 5000 draws; codes and order fixed, so only the French each
run meets changes and the score can differ from the real one. Pass = that canvas's C hits with P(ctrl>=real) < 0.05.
Also reported, not gating: shuffled-gloss (glosses permuted over that unit's lines, 10000 permutations).
Power floor, written before scoring: a unit with fewer than 15 C-valued occurrences is reported 'TOO-SHORT' whatever P is.
A pass extends attestation only: no code enters key_f23.tsv or key.tsv from this script.

HELD-OUT CHECK (NOT a gate; brief A2-COL17), pre-registered here before any 54-56 pass was read: the 17 candidates of
key_f23_anchor.tsv (A2-COL16, fitted on units that never include 54-56). Spans on 54-56 are built exactly as anchor_split.py builds
them (interior spans between consecutive scoring key_f23 C anchors; eligible if 1-3 non-C codes and 1-12 gloss letters).
A candidate OCCURS if it is a span code of at least one eligible 54-56 span; it AGREES if any of its '|' alternatives is a substring
of the text of at least half of its eligible 54-56 spans. Primary scope: the 54-56 canvases that PASS their own gate above (rule 3
per-unit clause); also printed over all three canvases, labelled diagnostic.
Reference (not a gate): control H -- each 54-56 eligible span's text replaced by a random text of the same letter length drawn from
the pool of eligible span texts of the A2-COL16 cleared units (anchor_split.py's own inputs) plus 54-56; 2000 draws; candidates and
span codes fixed, so the agree count can differ.
SUPPORT, written before looking: agree >= ceil(occur / 2) AND agree > control-H p95. Anything less is reported 'no support'; neither
outcome changes key_f23.tsv, key.tsv or key_f23_anchor.tsv.
Usage: python3 siblings/c5456_test.py"""
import csv, random, re, os, math, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')}
runs, gl = {}, {}
for r in csv.DictReader(open(f'{H}/c5456_reconciled.tsv'), delimiter='\t'):
    k = r['line']; runs[k] = [t for t in r['tokens'].split() if t.isdigit()]; gl[k] = norm(r['gloss'])
lines = sorted(k for k in gl if gl[k])
bank = norm(''.join(r['plain_raw'] for r in csv.DictReader(open(f'{T}/interlinear/f23w_pairs.tsv'), delimiter='\t')))
def walk(codes, gloss, grades):
    p = 0; hit = n = 0; hits = []
    for c in codes:
        if c not in key or key[c][1] not in grades: continue
        n += 1; i = gloss.find(key[c][0], p)
        if i >= 0: hit += 1; p = i + len(key[c][0]); hits.append(c)
    return hit, n, hits
def pct(xs, q): xs = sorted(xs); return xs[min(len(xs) - 1, int(q * len(xs)))]
rng = random.Random(20261003 + 5456)
units = [('canvas54', ['54']), ('canvas55', ['55']), ('canvas56', ['56']), ('letter5456', ['54', '55', '56'])]
print('line\tset\treal\tn\thits')
for name, grades in (('C', {'C'}), ('all', {'C', 'M'})):
    for L in lines:
        h, k, hits = walk(runs[L], gl[L], grades)
        print(f"{L}\t{name}\t{h}\t{k}\t{' '.join(f'{c}={key[c][0]}' for c in hits)}")
passed = set()
print('\nscope\tset\treal\tn\tctrl\tmean\tp95\tmax\tP(ctrl>=real)\tgate')
for uname, cans in units:
    ul = [L for L in lines if L[:2] in cans]
    if not ul: print(f"{uname}\t-\t-\t0\t-\t-\t-\t-\t-\tNO-LINES"); continue
    for name, grades in (('C', {'C'}), ('all', {'C', 'M'})):
        h = sum(walk(runs[L], gl[L], grades)[0] for L in ul); n = sum(walk(runs[L], gl[L], grades)[1] for L in ul)
        win = []
        for _ in range(5000):
            s = 0
            for L in ul:
                st = rng.randrange(0, len(bank) - len(gl[L])); s += walk(runs[L], bank[st:st + len(gl[L])], grades)[0]
            win.append(s)
        perm = []
        for _ in range(10000):
            g = [gl[L] for L in ul]; rng.shuffle(g)
            perm.append(sum(walk(runs[L], g[i], grades)[0] for i, L in enumerate(ul)))
        for cn, c in (('f23-window', win), ('shuffled-gloss', perm)):
            P = sum(x >= h for x in c) / len(c)
            gate = '-'
            if (name, cn) == ('C', 'f23-window') and uname != 'letter5456':
                gate = 'TOO-SHORT' if n < 15 else ('PASS' if P < 0.05 else 'FAIL')
                if gate == 'PASS': passed.add(uname[-2:])
            print(f"{uname}\t{name}\t{h}\t{n}\t{cn}\t{sum(c)/len(c):.2f}\t{pct(c,.95)}\t{max(c)}\t{P:.4f}\t{gate}")
# Also reported (not gating): every occurrence of code 12 (key_f23 12 = c, grade C) with its line's gloss.
print('\ncode12\tline\tgloss')
for L in lines:
    if '12' in runs[L]: print(f"12\t{L}\t{gl[L]}")

# ---- HELD-OUT CHECK (not a gate), as registered in the docstring ----
Cset = {c for c, (v, g) in key.items() if g == 'C'}
def spans_of(lns):
    out = []
    for L, codes, g in lns:
        if not g: continue
        p = 0; prev = None; between = []
        for c in codes:
            if c in Cset:
                i = g.find(key[c][0], p)
                if i < 0: continue
                if prev is not None: out.append((L, tuple(between), g[prev:i]))
                prev = p = i + len(key[c][0]); between = []
            elif prev is not None: between.append(c)
    return [s for s in out if 1 <= len(s[1]) <= 3 and 1 <= len(s[2]) <= 12]
# the A2-COL16 cleared units, read exactly as anchor_split.py reads them
old = []
ids = {r['id']: r['sign'] for r in csv.DictReader(open(f'{T}/interlinear/sign_ids.tsv'), delimiter='\t')}
f23 = collections.OrderedDict()
for r in csv.DictReader(open(f'{T}/interlinear/f23w_pairs.tsv'), delimiter='\t'):
    P = r['cipher_line'][:3]; f23.setdefault(P, ([], []))
    f23[P][0].extend(ids.get(t, t) for t in r['cipher_raw'].split()); f23[P][1].append(r['plain_raw'])
for P, (cs, gs) in f23.items(): old.append((P, [c for c in cs if c.isdigit()], norm(' '.join(gs))))
for fn, pre in (('c32', {'L'}), ('c33', {'T', 'B'}), ('c3536', {'35', '36'}), ('c3940', {'39', '40'}),
                ('c4749', {'47', '48', '49'}), ('c5051', {'50'})):
    for r in csv.DictReader(open(f'{H}/{fn}_reconciled.tsv'), delimiter='\t'):
        L = r['line']; p = L[:2] if L[:2].isdigit() else L[0]
        if p in pre: old.append((L, [t for t in r['tokens'].split() if t.isdigit()], norm(r['gloss'])))
pool_old = [s[2] for s in spans_of(old)]
anc = list(csv.DictReader(open(f'{T}/key_f23_anchor.tsv'), delimiter='\t'))
def held(scope, label):
    el = spans_of([(L, runs[L], gl[L]) for L in lines if L[:2] in scope])
    pool = collections.defaultdict(list)
    for t in pool_old + [s[2] for s in el]: pool[len(t)].append(t)
    def count(texts):
        occ = agr = 0; det = []
        for r in anc:
            alts = r['value'].split('|'); idx = [i for i, s in enumerate(el) if r['code'] in s[1]]
            if not idx: continue
            occ += 1; k = sum(any(a in texts[i] for a in alts) for i in idx)
            ok = k * 2 >= len(idx); agr += ok; det.append((r['code'], r['value'], len(idx), k, ok))
        return occ, agr, det
    real = [s[2] for s in el]; occ, agr, det = count(real)
    rh = random.Random(20261003 + 17); ctl = [count([rh.choice(pool[len(t)]) for t in real])[1] for _ in range(2000)]
    p95 = pct(ctl, .95) if ctl else 0; P = sum(x >= agr for x in ctl) / len(ctl)
    sup = 'support' if occ and agr >= math.ceil(occ / 2) and agr > p95 else 'no support'
    print(f"\nheld-out\t{label}\tcanvases {','.join(sorted(scope)) or '-'}\teligible spans {len(el)}\toccur {occ}/{len(anc)}"
          f"\tagree {agr}\tctrl-H mean {sum(ctl)/len(ctl):.2f} p95 {p95} max {max(ctl)} P {P:.4f}\t{sup}")
    print('code\tvalue\tspans\tagree_spans\tagrees')
    for d in det: print('\t'.join(map(str, d)))
held(passed, 'primary (canvases that passed their own gate)')
held({'54', '55', '56'}, 'diagnostic (all three canvases)')

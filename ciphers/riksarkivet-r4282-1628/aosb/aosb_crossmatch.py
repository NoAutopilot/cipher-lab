#!/usr/bin/env python3
"""AOSB-PAIRS (4 Oct 2026): build key_aosb1629.tsv from the alignment of AOSB I:4 letter 231's printed cipher
footnotes (pairs.tsv -> tools/interlinear_align.py -> align.tsv), then run PREREG-AOSB-PAIRS.md: the LOFO control on
the AOSB passages first, then R4284's numeric body and R4282, against 200 meaning-permuted keys.
    python3 aosb_crossmatch.py           regenerate key_aosb1629.tsv and results.json
    python3 aosb_crossmatch.py --check   exit non-zero if either committed file is stale (rule 7)"""
import csv, json, os, random, re, sys, collections
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(H); REPO = os.path.dirname(os.path.dirname(P))
sys.path.insert(0, os.path.join(REPO, 'tools'))
import judge_plaintext as jp

# Word codes: lemma meanings read from the aligned chunks (align.tsv) and the edition's fn10 note; inflected forms
# in the clear text (Regem/Regis, Turca/Turcae) show the codes are lemma codes.
WORD = {'1195': 'obtulisse', '1209': 'opportunitate', '1294': 'perspexeris', '1369': 'principem',
        '1421': 'rex (regem/regis)', '1440': 'responsum', '1520': 'statu', '1775': 'princeps transylvaniae',
        '1784': 'siculi', '1782': 'hungari', '1837': 'regis poloniae', '1839': 'poloniam', '1856': 'moschus',
        '1887': 'rex poloniae', '1973': 'polonos', '1974': 'turca', '1980': 'tartarus', '1981': 'tartari',
        '211': 'armis', '374': 'consiliis', '401': 'convenire', '484': 'destinata', '591': 'electio',
        '895': 'intellexeris', '900': 'intermittas', '959': 'legatus', '8?7': 'inclinare'}
WORD_SRC = {'1782': 'edition fn10 only (copy reads Hungarorum; not in the cipher)'}

def load_align(exclude=None):
    rows = list(csv.DictReader(open(os.path.join(H, 'align.tsv')), delimiter='\t'))
    return [r for r in rows if r['cipher_line'] != exclude]

def letter_key(rows):
    by = collections.defaultdict(collections.Counter)
    for r in rows:
        if r['raw'].startswith('@') and len(r['plain_chunk']) == 1:
            by[r['raw'][1:]][r['plain_chunk']] += 1
    return {v: c.most_common(1)[0] for v, c in by.items()}

def build_key():
    lk = letter_key(load_align())
    out = [('value', 'meaning', 'class', 'n', 'n_majority', 'others', 'grade', 'source')]
    by = collections.defaultdict(collections.Counter)
    for r in load_align():
        if r['raw'].startswith('@') and len(r['plain_chunk']) == 1:
            by[r['raw'][1:]][r['plain_chunk']] += 1
    def sk(v): return (0, int(v)) if v.isdigit() else (1, v)
    for v in sorted(lk, key=sk):
        c = by[v]; m, n = lk[v]
        oth = ','.join('%s:%d' % (k, x) for k, x in c.items() if k != m)
        out.append((v, m, 'letter', sum(c.values()), n, oth, 'C', 'AOSB I:4 pp.341-342 fn alignment'))
    cnt = collections.Counter(r['raw'][1:] for r in load_align() if r['raw'].startswith('%'))
    for v in sorted(WORD, key=sk):
        out.append((v, WORD[v], 'word', cnt.get(v, 0), cnt.get(v, 0), '', 'C' if v != '8?7' else 'M',
                    WORD_SRC.get(v, 'AOSB I:4 pp.341-342 fn alignment')))
    return out

MODEL = None
def model():
    global MODEL
    if MODEL is None:
        import glob
        MODEL = jp.NgramModel([jp.read_corpus(p) for p in sorted(glob.glob(os.path.join(REPO, 'tools/data/la17/*.txt.gz')))])
    return MODEL

def decode_runs(stream, key):
    """stream: list of tokens or None (a break). -> (runs of letters, covered, total)."""
    runs, cur, cov, tot = [], '', 0, 0
    for t in stream:
        if t is None:
            runs.append(cur); cur = ''; continue
        tot += 1
        m = key.get(t)
        if m is None:
            runs.append(cur); cur = ''; continue
        cov += 1; cur += re.sub('[^a-z]', '', m.split('(')[0])
    runs.append(cur)
    return [r for r in runs if len(r) >= 4], cov, tot

def S(runs):
    L = sum(len(r) for r in runs)
    return sum(model().score(r) * len(r) for r in runs) / L if L else None, L

def permuted(key, rng):
    out = {}
    for cls in ('letter', 'word'):
        ks = [k for k, (m, c) in key.items() if c == cls]; ms = [key[k][0] for k in ks]; rng.shuffle(ms)
        out.update({k: (m, cls) for k, m in zip(ks, ms)})
    return out

def run_arm(streams_keys, n_null=200):
    """streams_keys: list of (stream, key{code:(meaning,cls)}). Pooled S, C and the permutation null."""
    def score(keys):
        runs, cov, tot = [], 0, 0
        for (st, _), k in zip(streams_keys, keys):
            r, c, t = decode_runs(st, {a: b[0] for a, b in k.items()}); runs += r; cov += c; tot += t
        s, L = S(runs)
        return s, cov / tot if tot else 0, L
    s, c, L = score([k for _, k in streams_keys])
    null = []
    for seed in range(1, n_null + 1):
        rng = random.Random(seed)
        ns, _, _ = score([permuted(k, rng) for _, k in streams_keys])
        if ns is not None: null.append(ns)
    null.sort()
    p99 = null[int(0.99 * (len(null) - 1))] if null else None
    real = None
    if L >= 20:
        rs, _, _ = model().controls(L, samples=200)
        rs = sorted(rs); real = rs[int(0.05 * (len(rs) - 1))]
    v = 'inapplicable (C < 0.5)'
    if c >= 0.5 and s is not None:
        v = 'NO FIT'
        if s > p99: v = 'FIT' if (real is not None and s >= real) else 'WEAK'
    r4 = lambda x: None if x is None else round(x, 4)
    return {'S': r4(s), 'C': r4(c), 'letters_scored': L, 'null_mean': r4(sum(null) / len(null)) if null else None,
            'null_p99': r4(p99), 'null_max': r4(null[-1]) if null else None, 'real_p05': r4(real),
            'share_null_ge_S': r4(sum(1 for x in null if s is not None and x >= s) / len(null)) if null else None,
            'verdict': v}

def aosb_stream(line):
    st = []
    for t in line.split():
        st.append(t[1:])
    return st

def keyfrom(rows):
    k = {v: (m, 'letter') for v, (m, n) in letter_key(rows).items()}
    k.update({v: (WORD[v], 'word') for v in WORD})
    return k

def r4284_stream():
    st = []; on = False
    for line in open(os.path.join(P, 'r4284_transcription_bourdeau.txt'), encoding='utf-8'):
        if line.startswith('## '):
            on = 'numeric' in line or 'left page' in line; continue
        if not on or line.startswith('#') or '(sic' in line:
            continue
        for t in re.split(r'(\[[^\]]*\])', line):
            if t.startswith('['):
                st.append(None); continue
            for x in t.split():
                x = x.rstrip('?')
                if x.isdigit(): st.append(x)
                else: st.append(None)
        st.append(None)
    return st

def r4282_stream(optimistic):
    rows = list(csv.DictReader(open(os.path.join(P, 'tx2/ciphertext_reconciled.tsv')), delimiter='\t'))
    st = []; last = None
    for r in rows:
        if r['line'] != last and last is not None: st.append(None)
        last = r['line']; st.append(r['sign'])
    return st

def r4282_key(key, optimistic):
    k = {}
    for v, (m, c) in key.items():
        if v == 'λ': k['L'] = (m, c)
        elif optimistic and c == 'letter' and re.fullmatch('[A-Z]', v): k[v.lower()] = (m, c)
    return k

def results():
    rows = load_align(); lines = sorted({r['cipher_line'] for r in rows})
    pairs = {r['plain_line']: r for r in csv.DictReader(open(os.path.join(H, 'pairs.tsv')), delimiter='\t')}
    folds = [(aosb_stream(pairs[l]['cipher_raw']), keyfrom(load_align(exclude=l))) for l in lines]
    res = {'prereg': 'aosb/PREREG-AOSB-PAIRS.md', 'control_lofo': run_arm(folds)}
    ctl = res['control_lofo']
    if not (ctl['C'] >= 0.5 and ctl['S'] is not None and ctl['S'] > ctl['null_p99']):
        res['stop'] = 'CONTROL FAIL: untested-by-this-tool'; return res
    key = keyfrom(rows)
    res['r4284'] = run_arm([(r4284_stream(), key)])
    # rule 3 (ARM3-ADJ): the control's power at the target's own scored-letter count -- 20 random subsets of the
    # LOFO folds, folds added in random order until the decoded letters reach R4284's letters_scored.
    need, hits, sub = res['r4284']['letters_scored'], 0, []
    for seed in range(1, 21):
        rng = random.Random(1000 + seed); order = folds[:]; rng.shuffle(order); pick, L = [], 0
        for st, k in order:
            if L >= need: break
            pick.append((st, k)); L += sum(len(r) for r in decode_runs(st, {a: b[0] for a, b in k.items()})[0])
        a = run_arm(pick, n_null=100); sub.append(a['S'])
        hits += a['C'] >= 0.5 and a['S'] is not None and a['S'] > a['null_p99']
    res['control_power_at_target_letters'] = {'letters': need, 'subsets': 20, 'pass_share': hits / 20,
                                              'S_min': min(sub), 'S_max': max(sub)}
    for opt in (False, True):
        res['r4282_' + ('optimistic' if opt else 'exact')] = run_arm([(r4282_stream(opt), r4282_key(key, opt))])
    return res

def main():
    key = build_key()
    ktxt = ''.join('\t'.join(map(str, r)) + '\n' for r in key)
    res = json.dumps(results(), indent=1, ensure_ascii=False) + '\n'
    kp, rp = os.path.join(H, 'key_aosb1629.tsv'), os.path.join(H, 'results.json')
    if '--check' in sys.argv:
        bad = [p for p, t in ((kp, ktxt), (rp, res)) if not os.path.exists(p) or open(p).read() != t]
        print('STALE: ' + ', '.join(bad) if bad else 'ok'); sys.exit(1 if bad else 0)
    open(kp, 'w').write(ktxt); open(rp, 'w').write(res); print(res)
main()

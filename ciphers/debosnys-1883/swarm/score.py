#!/usr/bin/env python3
"""DEB-SWARM frozen scorer (DEB-SWARM-0, 29 Sept 2026). The one test every swarm claim must pass.

Usage:
  score.py KEY.tsv --text c1|c2|<CONTROL>.c1|<CONTROL>.c2          plain mode (not a claim)
  score.py KEY.tsv --fit c1 --test c2                               HELD-OUT mode (the only accepted test)
  score.py KEY.tsv --control FR-HOMO                                recovery pct on a control (both parts)
  score.py KEY.tsv --control FR-HOMO --fit FR-HOMO.c1 --test FR-HOMO.c2   held-out on a control, with recovery
  score.py --blind-check VERDICT.tsv                                group D: score a committed blind verdict
  score.py --list                                                   list text ids
  score.py --selftest                                               planted key must pass, random key must not

KEY.tsv: two tab-separated columns, sign and value (a header row 'sign<TAB>value' is optional). A value is any
string: a letter, a syllable, a word, or empty (a null). For the language models a value is folded (lower case,
accents stripped, a-z only); a value with no letters reads nothing. Signs not in the key stay unread.

Texts. c1 and c2 are the settled three-pass drafts (ciphertext_c1_draft.tsv, ciphertext_c2_draft.tsv) with the
non-sign classes `_` (noise) and MULTI dropped, the clear digits and capitals listed in clear_spans.tsv dropped
(H43), and a trailing `?` stripped (the settled value is used). Controls live in swarm/controls/<ID>.tsv with parts
<ID>.c1 and <ID>.c2 shaped like c1 and c2.

HELD-OUT: the key is restricted to the signs that occur in the fit text; every other sign stays unread on the
test text. Only the test text is scored. The key file itself is the group's fit; the scorer cannot see how it was
made, so a claim must also commit the key and the fitting script (README.md, the bar).

Statistics (each against --shuffles shuffled keys, default 1000, seed fixed per key and text so a run is
reproducible): the values of the (restricted) key are permuted across its signs, which keeps the value
distribution; and, reported beside it as pct_strat, a frequency-STRATIFIED shuffle (values permuted only among
key signs within bands of BAND=6 consecutive frequency ranks in the scored text). The stratified null was added by
DEB-SWARM-0 because a key built from sign frequency alone (no language) reached 99.9 on the plain shuffle on the NULL
control (README.md, Self-test); the bar needs both. Per language fr, en, pt, es, la: letter-quadgram log-likelihood per quadgram, counted only inside
runs of read signs (an unread sign breaks the run); dictionary cover, the fraction of read letters inside a
dictionary word of 4+ letters (words of 4-12 letters seen 3+ times in the corpus). DEB-VOCAB: the fraction of read
letters inside a word of 3+ letters from Debosnys's public clear writing (vocab/deb_vocab_base.tsv plus
swarm/G-E/CRIBS.tsv when it exists). pct = 100 * (shuffles strictly below the real score) / shuffles.

Output is JSON. For a real text the decoded runs are included; for a control they never are, and the sealed
plaintext (controls/sealed/, read only by this script) is never printed -- only recovery pct.
"""
import argparse, collections, csv, gzip, hashlib, json, math, os, pathlib, random, re, subprocess, sys, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
LANGS = ('fr', 'en', 'pt', 'es', 'la')
SMOOTH = 0.5


def fold(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('ß', 'ss').replace('æ', 'ae').replace('œ', 'oe')
    return re.sub(r'[^a-z]', '', s)


# ---------------------------------------------------------------- texts
C2A_LINES = 17  # c2 page a has 17 lines (c2a_L01-L17), page b 9; controls mirror this split


def load_real(which):
    src = ROOT / f'ciphertext_{which[:2]}_draft.tsv'
    skip = {(r['line'], r['position']) for r in csv.DictReader(open(ROOT / 'clear_spans.tsv'), delimiter='\t')}
    lines = collections.OrderedDict()
    for r in csv.DictReader(open(src), delimiter='\t'):
        s = r['sign'].rstrip('?')
        if s in ('_', 'MULTI', '') or (r['line'], r['position']) in skip:
            continue
        if len(which) == 3 and not r['line'].startswith(which + '_'):
            continue
        lines.setdefault(r['line'], []).append(s)
    return lines


def _part_ok(line, part):
    if part in ('c1', 'c2'):
        return line.startswith(part + '_')
    if not line.startswith('c2_'):
        return False
    n = int(line.split('_L')[1])
    return n <= C2A_LINES if part == 'c2a' else n > C2A_LINES


def load_control(cid):
    base, part = cid.rsplit('.', 1)
    lines = collections.OrderedDict()
    for r in csv.DictReader(open(HERE / 'controls' / f'{base}.tsv'), delimiter='\t'):
        if _part_ok(r['line'], part):
            lines.setdefault(r['line'], []).append(r['sign'])
    return lines


def load_sealed(cid):
    if '+' in cid:
        return [v for c in cid.split('+') for v in load_sealed(c)]
    base, part = cid.rsplit('.', 1)
    out = []
    for r in csv.DictReader(open(HERE / 'controls' / 'sealed' / f'{base}.tsv'), delimiter='\t'):
        if _part_ok(r['line'], part):
            out.append(r['value'])
    return out


def load_text(tid):
    """One id, or several joined by '+' (c1+c2a; FR-HOMO.c1+FR-HOMO.c2a). Parts: c1, c2, c2a (c2 lines 1-17), c2b."""
    if '+' in tid:
        out = collections.OrderedDict()
        for t in tid.split('+'):
            out.update(load_text(t))
        return out
    if tid in ('c1', 'c2', 'c2a', 'c2b'):
        return load_real(tid)
    if '.' in tid and tid.rsplit('.', 1)[1] in ('c1', 'c2', 'c2a', 'c2b') and (HERE / 'controls' / f'{tid.rsplit(".", 1)[0]}.tsv').exists():
        return load_control(tid)
    sys.exit(f'unknown text id {tid!r}; see --list')


def is_blind(tid):
    return any(re.match(r'B\d', t) for t in tid.split('+'))


def is_real(tid):
    return all(t in ('c1', 'c2', 'c2a', 'c2b') for t in tid.split('+'))


def flat(lines):
    return [s for l in lines.values() for s in l]


def load_key(path):
    key = {}
    for row in csv.reader(open(path), delimiter='\t'):
        if not row or row[0].startswith('#') or (row[0] == 'sign' and len(row) > 1 and row[1] == 'value'):
            continue
        key[row[0].rstrip('?')] = row[1] if len(row) > 1 else ''
    return key


# ---------------------------------------------------------------- models
_MODELS = {}


def corpus_text(lang):
    return gzip.open(HERE / 'corpora' / f'{lang}.txt.gz', 'rt').read()


def model(lang):
    if lang in _MODELS:
        return _MODELS[lang]
    words = corpus_text(lang).split()
    q = collections.Counter()
    stream = ''.join(words)
    for i in range(len(stream) - 3):
        q[stream[i:i + 4]] += 1
    tot = sum(q.values())
    floor = math.log10(SMOOTH / (tot + SMOOTH * 26 ** 4))
    lp = {k: math.log10((v + SMOOTH) / (tot + SMOOTH * 26 ** 4)) for k, v in q.items()}
    wc = collections.Counter(w for w in words if 4 <= len(w) <= 12)
    dic = {w for w, c in wc.items() if c >= 3}
    _MODELS[lang] = (lp, floor, dic)
    return _MODELS[lang]


def vocab():
    ws = set()
    for p in (HERE / 'vocab' / 'deb_vocab_base.tsv', HERE / 'G-E' / 'CRIBS.tsv'):
        if p.exists():
            for r in csv.reader(open(p), delimiter='\t'):
                if r and r[0] not in ('word', '') and not r[0].startswith('#'):
                    w = fold(r[0])
                    if len(w) >= 3:
                        ws.add(w)
    return ws


def runs(tokens, key):
    """Decoded letter runs; an unread sign (or a value with no letters is NOT a break: a null reads nothing)."""
    out, cur = [], []
    for s in tokens:
        if s in key:
            cur.append(fold(key[s]))
        else:
            if cur:
                out.append(''.join(cur))
            cur = []
    if cur:
        out.append(''.join(cur))
    return [r for r in out if r]


def quad(rs, lp, floor):
    tot, n = 0.0, 0
    for r in rs:
        for i in range(len(r) - 3):
            tot += lp.get(r[i:i + 4], floor)
            n += 1
    return tot / n if n else float('-inf')


def cover(rs, dic, lo, hi):
    letters = sum(len(r) for r in rs)
    if not letters:
        return 0.0
    hit = 0
    for r in rs:
        m = bytearray(len(r))
        for i in range(len(r)):
            for L in range(lo, min(hi, len(r) - i) + 1):
                if r[i:i + L] in dic:
                    m[i:i + L] = b'\x01' * L
        hit += sum(m)
    return hit / letters


def stats(tokens, key, langs=LANGS):
    rs = runs(tokens, key)
    out = {}
    for L in langs:
        lp, floor, dic = model(L)
        out[f'{L}_quad'] = quad(rs, lp, floor)
        out[f'{L}_dict'] = cover(rs, dic, 4, 12)
    out['vocab'] = cover(rs, vocab(), 3, 14)
    return out, rs


BAND = 6


def bands(tokens, key):
    """Frequency strata for the stratified null: key signs ranked by count in the scored text, cut into bands of BAND
    consecutive ranks; key signs absent from the text form one more band (they read nothing here)."""
    c = collections.Counter(t for t in tokens if t in key)
    ranked = sorted(c, key=lambda s: (-c[s], s))
    out = [ranked[i:i + BAND] for i in range(0, len(ranked), BAND)]
    rest = [s for s in key if s not in c]
    return out + ([rest] if rest else [])


def shuffled_stats(tokens, key, n, seed, stratified):
    rng = random.Random(seed + (1 if stratified else 0))
    groups = bands(tokens, key) if stratified else [list(key)]
    res = collections.defaultdict(list)
    for _ in range(n):
        k = {}
        for g in groups:
            vals = [key[s] for s in g]
            rng.shuffle(vals)
            k.update(zip(g, vals))
        st, _ = stats(tokens, k)
        for kk, v in st.items():
            res[kk].append(v)
    return res


def _cmp(v, nv, n):
    below = sum(1 for x in nv if x < v)
    med = sorted(nv)[len(nv) // 2] if nv else None
    return {'null_median': round(med, 4) if med not in (None, float('-inf')) else None,
            'pct': round(100.0 * below / n, 2), 'beats_all': below == n}


def evaluate(tokens, key, n, seed):
    real, rs = stats(tokens, key)
    null = shuffled_stats(tokens, key, n, seed, False)
    snull = shuffled_stats(tokens, key, n, seed, True)
    rep = {}
    for k, v in real.items():
        a, b = _cmp(v, null[k], n), _cmp(v, snull[k], n)
        rep[k] = {'real': round(v, 4) if v != float('-inf') else None, 'null_median': a['null_median'], 'pct': a['pct'],
                  'beats_all': a['beats_all'], 'strat_null_median': b['null_median'], 'pct_strat': b['pct'],
                  'beats_all_strat': b['beats_all']}
    return rep, rs


def recovery(tokens, key, truth):
    ok = sum(1 for s, t in zip(tokens, truth) if s in key and fold(t) and fold(key[s]) == fold(t))
    return round(100.0 * ok / len(tokens), 2) if tokens else 0.0


def seed_for(key, tid):
    h = hashlib.sha1((json.dumps(sorted(key.items())) + tid).encode()).hexdigest()
    return int(h[:12], 16)


def sha_of(path):
    return hashlib.sha1(open(path, 'rb').read()).hexdigest()


# ---------------------------------------------------------------- modes
def run_plain(keyfile, tid, n):
    key = load_key(keyfile)
    toks = flat(load_text(tid))
    cov = sum(1 for s in toks if s in key) / len(toks)
    rep, rs = evaluate(toks, key, n, seed_for(key, tid))
    out = {'mode': 'plain', 'text': tid, 'key_sha1': sha_of(keyfile), 'N': len(toks), 'coverage': round(cov, 4),
           'read_letters': sum(len(r) for r in rs), 'shuffles': n, 'stats': rep}
    if is_real(tid):
        out['decoded_runs'] = rs
    return out


def run_heldout(keyfile, fit, test, n):
    key = load_key(keyfile)
    fitsigns = set(flat(load_text(fit)))
    rkey = {s: v for s, v in key.items() if s in fitsigns}
    toks = flat(load_text(test))
    cov = sum(1 for s in toks if s in rkey) / len(toks)
    rep, rs = evaluate(toks, rkey, n, seed_for(rkey, fit + '>' + test))
    out = {'mode': 'held-out', 'fit': fit, 'test': test, 'key_sha1': sha_of(keyfile), 'key_signs': len(key),
           'key_signs_seen_in_fit': len(rkey), 'N_test': len(toks), 'coverage_test': round(cov, 4),
           'read_letters': sum(len(r) for r in rs), 'shuffles': n, 'stats': rep}
    if is_real(test):
        out['decoded_runs'] = rs
    elif not is_blind(test):
        out['recovery_pct_test'] = recovery(toks, rkey, load_sealed(test))
    return out


def run_control(keyfile, cid):
    key = load_key(keyfile)
    out = {'mode': 'control', 'control': cid, 'key_sha1': sha_of(keyfile)}
    if is_blind(cid):
        out['error'] = 'the blind set B1-B5 has no recovery mode (it would reveal the design); use --blind-check'
        return out
    if cid.startswith('NULL'):
        out['note'] = 'NULL has no plaintext; recovery is undefined. Use --text/--fit/--test for its language scores.'
        return out
    tot_ok = tot = 0
    for part in ('c1', 'c2'):
        toks = flat(load_control(f'{cid}.{part}'))
        truth = load_sealed(f'{cid}.{part}')
        r = recovery(toks, key, truth)
        out[f'recovery_pct_{part}'] = r
        tot_ok += r * len(toks) / 100
        tot += len(toks)
    out['recovery_pct'] = round(100 * tot_ok / tot, 2)
    return out


def blind_check(path):
    p = pathlib.Path(path).resolve()
    rel = os.path.relpath(p, ROOT.parents[1])
    committed = subprocess.run(['git', 'ls-files', '--error-unmatch', rel], cwd=ROOT.parents[1], capture_output=True).returncode == 0
    clean = subprocess.run(['git', 'diff', '--quiet', 'HEAD', '--', rel], cwd=ROOT.parents[1]).returncode == 0
    if not (committed and clean):
        return {'mode': 'blind-check', 'error': 'the verdict file must be committed and unmodified before it is checked'}
    truth = {r['id']: r['design'] for r in csv.DictReader(open(HERE / 'controls' / 'sealed' / 'BLIND.tsv'), delimiter='\t')}
    guess = {r['id']: r['verdict'].strip().upper() for r in csv.DictReader(open(p), delimiter='\t')}
    rows, right = [], 0
    for bid, d in sorted(truth.items()):
        isnull = d == 'NULL'
        g = guess.get(bid, '')
        ok = (g == 'NULL') == isnull and g in ('NULL', 'LANGUAGE')
        right += ok
        rows.append({'id': bid, 'verdict': g, 'correct': ok})
    return {'mode': 'blind-check', 'verdict_sha1': sha_of(p), 'correct': right, 'of': len(truth), 'rows': rows,
            'passes': right == len(truth)}


def list_ids():
    ids = ['c1', 'c2']
    for p in sorted((HERE / 'controls').glob('*.tsv')):
        ids += [f'{p.stem}.c1', f'{p.stem}.c2']
    return ids


def selftest(n):
    """Planted key on a planted text passes; a random key does not (on the FR-HOMO control, which carries a known
    answer). Uses the sealed answer, so only the harness runs it; prints numbers, never plaintext."""
    import tempfile
    res = {}
    base = 'FR-HOMO'
    sealed = {}
    for part in ('c1', 'c2'):
        for s, v in zip(flat(load_control(f'{base}.{part}')), load_sealed(f'{base}.{part}')):
            sealed.setdefault(s, collections.Counter())[v] += 1
    true_key = {s: c.most_common(1)[0][0] for s, c in sealed.items()}
    rng = random.Random(7)
    letters = [v for v in true_key.values()]
    rng.shuffle(letters)
    rand_key = dict(zip(true_key, letters))
    for name, k in (('planted', true_key), ('random', rand_key)):
        with tempfile.NamedTemporaryFile('w', suffix='.tsv', delete=False) as f:
            for s, v in k.items():
                f.write(f'{s}\t{v}\n')
        a = run_heldout(f.name, f'{base}.c1', f'{base}.c2', n)
        b = run_heldout(f.name, f'{base}.c2', f'{base}.c1', n)
        res[name] = {'fr_quad_pct': [a['stats']['fr_quad']['pct'], b['stats']['fr_quad']['pct']],
                     'recovery_test': [a['recovery_pct_test'], b['recovery_pct_test']],
                     'passes_bar_fr': bar_pass(a, b, 'fr_quad')}
        os.unlink(f.name)
    res['ok'] = res['planted']['passes_bar_fr'] and not res['random']['passes_bar_fr']
    return res


def bar_pass(a, b, stat):
    """The bar (README.md): beats all shuffles in BOTH held-out directions on one statistic, with the coverage floor."""
    return all(x['stats'][stat]['beats_all'] and x['stats'][stat]['beats_all_strat'] and x['coverage_test'] >= 0.5
               and x['read_letters'] >= 60 for x in (a, b))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('key', nargs='?')
    ap.add_argument('--text'); ap.add_argument('--fit'); ap.add_argument('--test'); ap.add_argument('--control')
    ap.add_argument('--shuffles', type=int, default=1000)
    ap.add_argument('--blind-check'); ap.add_argument('--list', action='store_true'); ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    if a.list:
        out = {'texts': list_ids()}
    elif a.selftest:
        out = selftest(a.shuffles)
    elif a.blind_check:
        out = blind_check(a.blind_check)
    elif not a.key:
        ap.error('a key file is required')
    elif a.fit and a.test:
        out = run_heldout(a.key, a.fit, a.test, a.shuffles)
        if a.control:
            out['control_recovery'] = run_control(a.key, a.control)
    elif a.control:
        out = run_control(a.key, a.control)
    elif a.text:
        out = run_plain(a.key, a.text, a.shuffles)
    else:
        ap.error('give --text, --fit and --test, or --control')
    print(json.dumps(out, indent=1))

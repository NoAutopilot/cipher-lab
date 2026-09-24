#!/usr/bin/env python3
"""1653 band key trial: do any of the Brienne-family keys read the folio 1-2 or folio 9 letter?

    python3 trial_1653.py            write trial_1653.tsv and trial_1653_overlap.tsv, print the table
    python3 trial_1653.py --check    exit 1 if either committed file differs from what this script writes

Keys: key_1646 (clair1067, Brienne to the Queen of Poland 1646, recovered at grade C from its interlinear
decipherment), key_brienne_1647 and key_brienne_1651 (Tomokiyo's published tables, Brienne to d'Estrades, reconstructed
by George Lasry), key_1659 (this volume's f.86-88, recovered from the f.87 decipherment).
Letters: ciphertext_f1.tsv (10 Jan 1653, 528 signs) and ciphertext_f9.tsv (folio 9, 226 signs).

Sign mapping, 1653 spelling -> key spelling (grade I: the tables were transcribed by different hands, so shape
identity is assumed, not shown). Bare numerals map to the bare code. Overlined numerals map to the key's marked
series ('N_' in the two Tomokiyo tables, '_N' in key_1646 and key_1659). Dotted numerals, struck signs (~) and the
signs listed in no key (db, mm, I, X in three keys, 11 in two, ...) are unkeyed. Letter-like signs per key: LETTERS.

Measure: mean log2 probability per character of the decoded text under tools/french16_ngram.py (order-5 period
French), over maximal runs of keyed signs of at least 2 characters; an unkeyed sign or clear phrase ends a run.
Higher (less negative) is more French. Controls (rule 3), per key and letter:
  (a) shuffled key: the key's values permuted over its codes, NDER derangements (no code keeps its value);
  (b) synthetic: French text (a fixed window of the fr16 corpus's held-out slice) enciphered with the true key to
      the letter's length, with the letter's own unkeyed positions blanked, so run lengths and coverage match
      exactly; then the true key and NDER derangements are scored on it. (b) shows the test can see a true key at
      this coverage; (a) is the test itself.
A key "beats its control" when its real-letter score is above every derangement (no derangement reaches it) AND the
synthetic control separates (true synthetic score above every synthetic derangement).
Deterministic: seed 1653.
"""
import csv, io, math, os, random, re, statistics, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import french16_ngram as fr

NDER = 200
SEED = 1653
KEYS = {
    'key_1646': (os.path.join(ROOT, 'ciphers', 'clair1067-brienne-poland-1646', 'key_1646.tsv'), 'pre'),
    'key_brienne_1647': (os.path.join(HERE, 'key_brienne_1647.tsv'), 'suf'),
    'key_brienne_1651': (os.path.join(HERE, 'key_brienne_1651.tsv'), 'suf'),
    'key_1659': (os.path.join(HERE, 'key_1659.tsv'), 'pre'),
}
LETTERS = {
    'key_1646': {'d': 'd', 'đ': 'd', 'X': 'X', 'Z': 'Z', 'm': 'm', 'm‡': 'm+', '£': 'L', 'θ': 'o',
                 'q': 'q', "q'": 'q', 'q‡': 'q'},
    'key_brienne_1647': {'tt': 'tt', 'd': 'd', 'đ': 'd', 'Z': 'Z', 'm': 'm', '11': 'u'},
    'key_brienne_1651': {'tt': 'tt', 'd': 'd', 'đ': 'd', 'Z': 'Z', 'q': 'q', "q'": 'q', 'q‡': 'q', '11': '11',
                         'm‡': 'm+'},
    'key_1659': {'m': 'm'},
}
CIPHERS = {'f1': 'ciphertext_f1.tsv', 'f9': 'ciphertext_f9.tsv'}


def load_key(fn):
    k = {}
    for r in csv.DictReader(open(fn, encoding='utf-8'), delimiter='\t'):
        v = r.get('value', r.get('plaintext', ''))
        v = '' if v.strip() == '0' else re.sub('[^A-Z]', '', fr.fold(v))
        k[r['code'].strip()] = v
    return k


def load_cipher(fn):
    """token stream; clear phrases become None (a run break)"""
    out = []
    for r in csv.DictReader(open(os.path.join(HERE, fn), encoding='utf-8'), delimiter='\t'):
        out.append(None if r['token'].startswith('[PLAIN') else r['token'])
    return out


def to_code(tok, kname):
    if tok is None or tok.startswith(('~', '¨')):
        return None
    style = KEYS[kname][1]
    if tok.startswith('_') and tok[1:].isdigit():
        return '_' + tok[1:] if style == 'pre' else tok[1:] + '_'
    if tok.isdigit():
        return tok
    return LETTERS[kname].get(tok)


def runs(values):
    """values: list of str or None -> list of joined runs"""
    out, cur = [], []
    for v in values:
        if v is None:
            if cur: out.append(''.join(cur))
            cur = []
        else:
            cur.append(v)
    if cur: out.append(''.join(cur))
    return [r for r in out if len(r) >= 2]


def score(values, m):
    rs = runs(values)
    n = sum(len(r) for r in rs)
    return (sum(m.logp(r) for r in rs) / n if n else float('nan')), n


def derangements(key, rng, n):
    codes = sorted(key)
    vals = [key[c] for c in codes]
    out = []
    while len(out) < n:
        p = vals[:]
        rng.shuffle(p)
        if all(a != b for a, b in zip(p, vals)):
            out.append(dict(zip(codes, p)))
    return out


def encipher(text, key, n, rng):
    """greedy longest-match: French letters -> key codes, n tokens"""
    byval = collections.defaultdict(list)
    for c, v in key.items():
        if v: byval[v].append(c)
    maxl = max(len(v) for v in byval)
    out, i = [], 0
    while len(out) < n and i < len(text):
        for L in range(min(maxl, len(text) - i), 0, -1):
            s = text[i:i + L]
            if s in byval:
                out.append(rng.choice(sorted(byval[s]))); i += L; break
        else:
            i += 1                                   # letter the table cannot write
    return out


def segment(s, words):
    """True if s splits wholly into frequent period words (DP)"""
    ok = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        ok[i] = any(ok[j] and s[j:i] in words for j in range(max(0, i - 14), i))
    return ok[-1]


def keyed_runs(toks, kname, key, vals=None):
    """maximal runs of keyed tokens: list of [(index, token, value)]"""
    vals = vals or key
    out, cur = [], []
    for i, t in enumerate(toks):
        c = to_code(t, kname)
        if c in key:
            cur.append((i, t, vals[c]))
        else:
            if cur: out.append(cur)
            cur = []
    if cur: out.append(cur)
    return out


def stretches(m, ciphers):
    """key_1659 runs of >= 3 signs that segment wholly into frequent period words, real vs derangements"""
    words = {w for w, n in m.words.items() if n >= 50 and (len(w) >= 2 or w in ('A', 'Y', 'O'))}
    key = load_key(KEYS['key_1659'][0])
    ders = derangements(key, random.Random(SEED + 1), NDER)
    rows, stat = [], {}
    for cname, toks in ciphers.items():
        lines = [r['line'] for r in csv.DictReader(open(os.path.join(HERE, CIPHERS[cname]), encoding='utf-8'), delimiter='\t')]
        def count(vals):
            return sum(1 for r in keyed_runs(toks, 'key_1659', key, vals)
                       if len(r) >= 3 and segment(''.join(v for _, _, v in r), words))
        real = [r for r in keyed_runs(toks, 'key_1659', key) if len(r) >= 3 and segment(''.join(v for _, _, v in r), words)]
        ctrl = [count(d) for d in ders]
        # same measure on the synthetic letter (true key's own French, the letter's unkeyed positions blanked)
        rng = random.Random(SEED + 2)
        syn = encipher(m._held[rng.randrange(0, len(m._held) // 2):], key, len(toks), rng)
        syn_toks = [None if to_code(t, 'key_1659') not in key else '#' + s for t, s in zip(toks, syn)]
        synk = dict(key, **{'#' + c: v for c, v in key.items()})
        def scount(vals):
            out, cur = 0, []
            for t in syn_toks + [None]:
                if t is None:
                    if len(cur) >= 3 and segment(''.join(cur), words): out += 1
                    cur = []
                else:
                    cur.append(vals[t[1:]])
            return out
        stat[cname] = (len(real), statistics.mean(ctrl), max(ctrl), scount(key), statistics.mean(scount(d) for d in ders))
        for r in real:
            rows.append([cname, lines[r[0][0]], ' '.join(t for _, t, _ in r), ' '.join(v.lower() for _, _, v in r),
                         ''.join(v.lower() for _, _, v in r), len(r)])
    return rows, stat


def code_deltas(m, ciphers):
    """key_1659: change in the joint f1+f9 score when one code is left unkeyed; > 0 means the letters read
    better without that value (a code on which the 1653 table probably differs)"""
    key = load_key(KEYS['key_1659'][0])
    def joint(k):
        tot = n = 0
        for toks in ciphers.values():
            vals = [k[c] if c in k else None for c in (to_code(t, 'key_1659') for t in toks)]
            for r in runs(vals):
                tot += m.logp(r); n += len(r)
        return tot / n
    base = joint(key)
    used = collections.Counter(to_code(t, 'key_1659') for toks in ciphers.values() for t in toks)
    rows = []
    for c in sorted(key, key=lambda c: (-used.get(c, 0), c)):
        if not used.get(c):
            continue
        k2 = dict(key); del k2[c]
        rows.append([c, key[c].lower(), used[c], '%.4f' % (joint(k2) - base)])
    return rows


def run_all():
    m = fr.load()
    held = m._held
    rng = random.Random(SEED)
    rows, over = [], []
    ciphers = {c: load_cipher(f) for c, f in CIPHERS.items()}
    for kname, (kfn, _) in KEYS.items():
        key = load_key(kfn)
        ders = derangements(key, rng, NDER)
        for cname, toks in ciphers.items():
            codes = [to_code(t, kname) for t in toks]
            keyed = [c if c in key else None for c in codes]
            nsig = sum(t is not None for t in toks)
            ncov = sum(c is not None for c in keyed)
            real, nch = score([key[c] if c else None for c in keyed], m)
            ctrl = [score([d[c] if c else None for c in keyed], m)[0] for d in ders]
            # synthetic: same positions keyed/unkeyed, true key's own encipherment of French
            start = rng.randrange(0, len(held) // 2)
            syn = encipher(held[start:], key, len(keyed), rng)
            syn_keyed = [s if k is not None else None for s, k in zip(syn, keyed)]
            syn_true = score([key[c] if c else None for c in syn_keyed], m)[0]
            syn_ctrl = [score([d[c] if c else None for c in syn_keyed], m)[0] for d in ders]
            beats = real > max(ctrl) and syn_true > max(syn_ctrl)
            rows.append([kname, cname, nsig, ncov, nch, '%.3f' % real, '%.3f' % statistics.mean(ctrl),
                         '%.3f' % statistics.pstdev(ctrl), '%.3f' % max(ctrl), sum(c >= real for c in ctrl),
                         '%.2f' % ((real - statistics.mean(ctrl)) / statistics.pstdev(ctrl)),
                         '%.3f' % syn_true, '%.3f' % statistics.mean(syn_ctrl), '%.3f' % max(syn_ctrl),
                         sum(c >= syn_true for c in syn_ctrl), 'yes' if beats else 'no',
                         ' | '.join(sorted(runs([key[c] if c else None for c in keyed]), key=len, reverse=True)[:3])])
        # overlap: which 1653 signs this key can and cannot write
        cnt = collections.Counter(t for toks in ciphers.values() for t in toks if t is not None)
        for t, n in sorted(cnt.items(), key=lambda x: (-x[1], x[0])):
            c = to_code(t, kname)
            over.append([kname, t, n, c if c in key else '', key.get(c, '') if c in key else ''])
    srows, sstat = stretches(m, ciphers)
    return rows, over, srows, sstat, code_deltas(m, ciphers)


HEAD = ['key', 'letter', 'signs', 'keyed', 'chars_scored', 'real_bpc', 'shuffled_mean', 'shuffled_sd', 'shuffled_max',
        'shuffled_ge_real', 'z', 'syn_true', 'syn_shuffled_mean', 'syn_shuffled_max', 'syn_shuffled_ge_true',
        'beats_control', 'longest_real_runs']


def render():
    rows, over, srows, sstat, deltas = run_all()
    b = io.StringIO(); w = csv.writer(b, delimiter='\t', lineterminator='\n')
    w.writerow(HEAD); w.writerows(rows)
    b2 = io.StringIO(); w2 = csv.writer(b2, delimiter='\t', lineterminator='\n')
    w2.writerow(['key', 'token_1653', 'count_f1_f9', 'key_code', 'key_value']); w2.writerows(over)
    b3 = io.StringIO(); w3 = csv.writer(b3, delimiter='\t', lineterminator='\n')
    w3.writerow(['letter', 'line', 'tokens', 'values', 'reading', 'n_signs'])
    w3.writerows(srows)
    for c, (n, mean, mx, sn, smean) in sstat.items():
        w3.writerow(['#control', c, 'segmentable runs >= 3 signs: real %d' % n,
                     'derangements mean %.2f, max %d (n=%d)' % (mean, mx, NDER),
                     'synthetic: true key %d, derangements mean %.2f' % (sn, smean), ''])
    b4 = io.StringIO(); w4 = csv.writer(b4, delimiter='\t', lineterminator='\n')
    w4.writerow(['code_1659', 'value', 'uses_f1_f9', 'delta_bpc_if_unkeyed']); w4.writerows(deltas)
    return {'trial_1653.tsv': b.getvalue(), 'trial_1653_overlap.tsv': b2.getvalue(),
            'trial_1653_stretches.tsv': b3.getvalue(), 'trial_1653_1659codes.tsv': b4.getvalue()}


def main():
    files = render()
    if '--check' in sys.argv:
        stale = [f for f, s in files.items() if not os.path.exists(os.path.join(HERE, f))
                 or open(os.path.join(HERE, f), encoding='utf-8').read() != s]
        if stale:
            print('stale: ' + ', '.join(stale)); sys.exit(1)
        print('ok: ' + ', '.join(sorted(files))); return
    for f, s in files.items():
        open(os.path.join(HERE, f), 'w', encoding='utf-8').write(s)
    print(files['trial_1653.tsv'])


if __name__ == '__main__':
    main()

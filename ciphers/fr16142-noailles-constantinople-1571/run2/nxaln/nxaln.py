#!/usr/bin/env python3
"""RUN2-NXALN (4 Oct 2026): known-plaintext alignment of fr.16142 c510-516 (atlas clusters) against Dupuy 521 221R-226R.
Pre-registration: PREREG.md (committed first). Aligner: tools/stream_align.py (interlinear_align.py `stream`).
    python3 nxaln.py control P SEED [--draws 50]     matched synthetic control at impurity P (0.10/0.25/0.40)
    python3 nxaln.py target [--draws 200]            the atlas target (instrument 1)
    python3 nxaln.py key                             write key_learned.tsv (+ gibbs comparison file if present)
Writes results/*.json; prints one summary line per run.
"""
import gzip, json, os, random, re, sys, time, unicodedata
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import stream_align as sa

T = os.path.join(HERE, '..')
TRAIN_LEAVES, HELD_LEAVES = ['c510', 'c511', 'c512', 'c513'], ['c514', 'c515', 'c516']


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z ]', ' ', s)).strip()


def dupuy_stream():
    pages = [l.rstrip('\n').split('\t') for l in open(os.path.join(T, 'nxdup', 'dupuy221_226_norm.txt')) if not l.startswith('#')]
    txt = ' '.join(norm(p[1]) for p in pages)
    a = txt.index('la reception d icelle que') + len('la reception d icelle que')
    b0 = txt.index('sire quelques jours avant')
    b1 = txt.index('me mander', b0) + len('me mander')
    return (txt[a:b0] + ' ' + txt[b1:]).strip()


def fr16_text():
    t = gzip.open(os.path.join(ROOT, 'tools', 'data', 'fr16', 'lettresdecatheri01cathuoft_djvu.txt.gz'), 'rt', errors='ignore').read()
    return norm(t[400000:])  # skip front matter / introduction


def atlas():
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(T, 'nxatl', 'sequences.tsv')) if not l.startswith(('#', 'leaf'))]
    tr = [r[5] for r in rows if r[0] in TRAIN_LEAVES]
    he = [r[5] for r in rows if r[0] in HELD_LEAVES]
    return tr, he


# ---------------- synthetic matched control
def make_key(words_text, rng, n_true=41, n_nom=8):
    let = sa.letters(words_text)
    f = np.bincount(let, minlength=26).astype(float)
    order = list(np.argsort(-f))
    used = [l for l in order if f[l] > 0]
    n_let_sym = n_true - n_nom - 1  # one null symbol
    homs = {l: 1 for l in used}
    k = len(used)
    i = 0
    while k < n_let_sym:  # extra homophones to most frequent letters
        homs[used[i % 6]] += 1; k += 1; i += 1
    sym_of, sid = {}, 0
    for l in used:
        sym_of[l] = list(range(sid, sid + homs[l])); sid += homs[l]
    words = words_text.split()
    wc = {}
    for w in words:
        if len(w) >= 2:
            wc[w] = wc.get(w, 0) + 1
    noms = [w for w, _ in sorted(wc.items(), key=lambda x: -x[1])[:n_nom]]
    nom_of = {w: sid + n for n, w in enumerate(noms)}; sid += n_nom
    null = sid; sid += 1
    return sym_of, nom_of, null, sid


def encipher(text, key, rng, null_rate=0.03):
    sym_of, nom_of, null, _ = key
    out = []
    for w in text.split():
        if w in nom_of:
            out.append(nom_of[w])
        else:
            for c in w:
                out.append(rng.choice(sym_of[ord(c) - 97]))
        if rng.random() < null_rate:
            out.append(null)
    return out


def atlas_noise(seq, n_true, rng, p, n_clu=120, ins=0.08, dele=0.03):
    # over-split each true symbol into clusters
    split = {s: [s] for s in range(n_true)}
    extra = list(range(n_true, n_clu))
    for c in extra:
        split[rng.randrange(n_true)].append(c)
    out = []
    for s in seq:
        if rng.random() < dele:
            continue
        c = rng.choice(split[s])
        if rng.random() < p:
            c = rng.randrange(n_clu)
        out.append(c)
        if rng.random() < ins:
            out.append(rng.randrange(n_clu))
    return out


def line_noise(seq, n_true, rng, p):
    return [rng.randrange(n_true) if rng.random() < p else s for s in seq]


HOMS = dict(a=3, b=1, c=3, d=2, e=4, f=2, g=3, h=1, i=4, l=2, m=2, n=3, o=5, p=2, q=1, r=2, s=3, t=1, u=5, x=2, y=1, z=1)
FOLDS = dict(j='i', v='u', k='c', w='u')


def make_design_key(words_text, n_nom=33, n_null=14, n_dbl=3):
    sym_of, sid = {}, 0
    for l in sorted(HOMS):
        sym_of[ord(l) - 97] = list(range(sid, sid + HOMS[l])); sid += HOMS[l]
    wc = {}
    for w in words_text.split():
        if len(w) >= 2:
            wc[w] = wc.get(w, 0) + 1
    noms = [w for w, _ in sorted(wc.items(), key=lambda x: -x[1])[:n_nom]]
    nom_of = {w: sid + n for n, w in enumerate(noms)}; sid += n_nom
    nulls = list(range(sid, sid + n_null)); sid += n_null
    dbl = list(range(sid, sid + n_dbl)); sid += n_dbl
    return sym_of, nom_of, nulls, dbl, sid


def encipher_design(text, key, rng, null_rate=0.06):
    sym_of, nom_of, nulls, dbl, _ = key
    out = []
    for w in text.split():
        if w in nom_of:
            out.append(nom_of[w])
        else:
            w = ''.join(FOLDS.get(c, c) for c in w)
            k = 0
            while k < len(w):
                out.append(rng.choice(sym_of[ord(w[k]) - 97]))
                if k + 1 < len(w) and w[k + 1] == w[k]:
                    out.append(rng.choice(dbl)); k += 2
                else:
                    k += 1
                if rng.random() < null_rate:
                    out.append(rng.choice(nulls))
    return out


# ---------------- pipeline
def run_pipeline(tr, he, text, n_sym, draws, rng, wrong_pool, label, shuffled_draws=None):
    """tr/he: symbol id lists; text: clear string (words) for the whole stream. Returns result dict."""
    let = sa.letters(text)
    t0 = time.time()
    counts, path = sa.learn(np.array(tr), let, n_sym)
    t_train = time.time() - t0
    key = sa.decode(counts)
    jend = path[-1][1] + 1 if path else 0
    held_let = let[jend:]
    dec = key[np.array(he)]
    acc = sa.nw_score(dec, held_let)
    # null (a) shuffled key
    na = []
    for _ in range(draws):
        k2 = key.copy(); seen = k2 >= 0
        v = k2[seen]; rng.shuffle(v); k2[seen] = v
        na.append(sa.nw_score(k2[np.array(he)], held_let))
    # null (c) wrong text: same-length spans of a different French letter collection
    nc = []
    for _ in range(draws):
        o = rng.randrange(0, len(wrong_pool) - len(held_let) - 1)
        nc.append(sa.nw_score(dec, wrong_pool[o:o + len(held_let)]))
    # null (b) shuffled text (train side words shuffled; held-out scored against the real text)
    nb_draws = shuffled_draws if shuffled_draws is not None else (draws if t_train <= 6 else 40)
    words = text.split()
    # train-side words: those covering letters [0, jend)
    cum, cut = 0, len(words)
    for n, w in enumerate(words):
        cum += len(w)
        if cum >= jend:
            cut = n + 1; break
    nb = []
    for _ in range(nb_draws):
        w2 = words[:cut]; rng.shuffle(w2)
        sh = sa.letters(' '.join(w2 + words[cut:]))
        c2, p2 = sa.learn(np.array(tr), sh, n_sym)
        k2 = sa.decode(c2)
        nb.append(sa.nw_score(k2[np.array(he)], held_let))
    def q(v):
        return float(np.percentile(v, 99)) if len(v) else None
    gb = q(nb) if nb_draws >= 100 else (float(max(nb)) if nb else None)
    res = dict(label=label, n_train=len(tr), n_held=len(he), n_letters=len(let), train_end_letter=int(jend),
               held_letters=int(len(held_let)), t_train_s=round(t_train, 1), acc=round(acc, 4),
               null_a=dict(n=draws, mean=round(float(np.mean(na)), 4), p99=round(q(na), 4)),
               null_b=dict(n=nb_draws, mean=round(float(np.mean(nb)), 4) if nb else None, gate=round(gb, 4) if gb is not None else None,
                           gate_kind='p99' if nb_draws >= 100 else 'max'),
               null_c=dict(n=draws, mean=round(float(np.mean(nc)), 4), p99=round(q(nc), 4)))
    res['gate_pass'] = bool(acc > res['null_a']['p99'] and acc > res['null_c']['p99'] and gb is not None and acc > gb)
    return res, counts, path, key


def summary(r):
    return (f"{r['label']}: acc {r['acc']:.3f} | a p99 {r['null_a']['p99']:.3f} | b {r['null_b']['gate_kind']} {r['null_b']['gate']:.3f}"
            f" (n={r['null_b']['n']}) | c p99 {r['null_c']['p99']:.3f} | gate {'PASS' if r['gate_pass'] else 'FAIL'} | train {r['t_train_s']}s")


def cmd_pairs():
    """Cut the target's train stream alignment into line-sized (cluster run, aligned span +- 3) pairs for gibbs_align.py."""
    tr_real, he_real = atlas()
    let = sa.letters(dupuy_stream())
    path = [tuple(map(int, l.split())) for l in open(os.path.join(HERE, 'results', 'target_atlas_path.tsv')).read().splitlines()[1:]]
    pos = {i: j for i, j in path}
    out = ['plain_raw\tcipher_raw']
    for a0 in range(0, len(tr_real), 40):
        idx = [i for i in range(a0, min(len(tr_real), a0 + 40)) if i in pos]
        if len(idx) < 10:
            continue
        j0, j1 = max(0, pos[idx[0]] - 3), min(len(let), pos[idx[-1]] + 4)
        span = ''.join(chr(97 + x) for x in let[j0:j1])
        codes = ' '.join(str(int(tr_real[i][1:])) for i in range(a0, min(len(tr_real), a0 + 40)))
        out.append(span + '\t' + codes)
    open(os.path.join(HERE, 'results', 'gibbs_pairs.tsv'), 'w').write('\n'.join(out) + '\n')
    print(f'gibbs pairs: {len(out) - 1}')


def cmd_key(check=False):
    """key_learned.tsv: stream value (train counts) vs gibbs modal value vs provisional c262 name vs key.tsv."""
    res = json.load(open(os.path.join(HERE, 'results', 'target_atlas.json')))
    rows = [l.split('\t') for l in open(os.path.join(HERE, 'results', 'target_atlas_counts.tsv')).read().splitlines()]
    hdr, rows = rows[0], rows[1:]
    gib = {}
    gp = os.path.join(HERE, 'results', 'gibbs_key.tsv')
    if os.path.exists(gp):
        g = [l.split('\t') for l in open(gp).read().splitlines()]
        for r in g[1:]:
            gib['k%03d' % int(r[0])] = r[1]
    prov = {}
    for l in open(os.path.join(T, 'nxatl', 'cluster_provisional_names.tsv')).read().splitlines():
        r = l.split('\t')
        if r and r[0].startswith('k') and len(r) > 1:
            prov[r[0]] = r[1:]
    out = ['# RUN2-NXALN learned key, atlas instrument (train c510-c513 only). Gate: %s. Grade C only if gate PASS and both aligners agree.'
           % ('PASS' if res['gate_pass'] else 'FAIL'),
           'cluster\tvalue\tcount\tshare\tgibbs_value\taligners_agree\tgrade\tc262_provisional']
    for r in rows:
        c = np.array([int(x) for x in r[1:]])
        tot = int(c.sum())
        v = chr(97 + int(c.argmax())) if tot else '?'
        sh = c.max() / tot if tot else 0
        gv = gib.get(r[0], '')
        agree = 'yes' if gv and gv == v else ('no' if gv else 'n/a')
        grade = 'C' if (res['gate_pass'] and agree == 'yes') else 'M'
        out.append(f"{r[0]}\t{v}\t{tot}\t{sh:.2f}\t{gv}\t{agree}\t{grade}\t{'|'.join(prov.get(r[0], []))}")
    # comparison with key.tsv through the provisional c262 names (letter part of each label)
    agree = dis = 0; strong_a = strong_d = 0
    for line in out[2:]:
        r = line.split('\t')
        if not r[7] or r[1] == '?':
            continue
        lab, sup, pur = r[7].split('|')[0], int(r[7].split('|')[1]), float(r[7].split('|')[2])
        lets = {x[0] for x in lab.split('/') if x and x[0].isalpha() and (len(x) == 1 or x[1:].isdigit())}
        if not lets:
            continue
        ok = r[1] in lets
        agree += ok; dis += (not ok)
        if sup >= 3 and pur >= 0.6:
            strong_a += ok; strong_d += (not ok)
    out.append(f'# vs key.tsv via c262 provisional letter labels: agree {agree}, disagree {dis}; '
               f'strong labels (support>=3, purity>=0.6): agree {strong_a}, disagree {strong_d}')
    text = '\n'.join(out) + '\n'
    path = os.path.join(HERE, 'key_learned.tsv')
    if check:
        old = open(path).read() if os.path.exists(path) else ''
        if old != text:
            sys.exit('key_learned.tsv is stale')
        print('key_learned.tsv up to date')
        return
    open(path, 'w').write(text)
    print('key_learned.tsv:', len(rows), 'clusters;', out[-1])


def cmd_check():
    """Rule 7: re-learn the train key from the inputs and compare with the committed counts, then check key_learned.tsv."""
    tr_real, he_real = atlas()
    ids = {s: n for n, s in enumerate(sorted(set(tr_real + he_real)))}
    counts, path = sa.learn(np.array([ids[s] for s in tr_real]), sa.letters(dupuy_stream()), len(ids))
    rows = [l.split('\t') for l in open(os.path.join(HERE, 'results', 'target_atlas_counts.tsv')).read().splitlines()[1:]]
    for r in rows:
        if [int(x) for x in r[1:]] != [int(x) for x in counts[ids[r[0]]]]:
            sys.exit(f'counts stale at {r[0]}')
    print('target_atlas_counts.tsv up to date')
    cmd_key(check=True)


def main(a):
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    draws = 50
    if '--draws' in a:
        k = a.index('--draws'); draws = int(a[k + 1]); del a[k:k + 2]
    nbd = None
    if '--b-draws' in a:
        k = a.index('--b-draws'); nbd = int(a[k + 1]); del a[k:k + 2]
    dtext = dupuy_stream()
    fr = fr16_text()
    tr_real, he_real = atlas()
    if a[0] == 'control':
        p, seed = float(a[1]), int(a[2])
        mode = a[3] if len(a) > 3 else 'atlas'
        rng = random.Random(seed)
        L = len(sa.letters(dtext))
        # control text: an fr16 span with the same letter count, taken from the second half of the pool
        off = len(fr) // 2 + seed * 50000
        words, n = [], 0
        for w in fr[off:].split():
            words.append(w); n += len(w)
            if n >= L:
                break
        ctext = ' '.join(words)
        wrong_pool = sa.letters(fr[: len(fr) // 2])
        if mode == 'design':
            ctext = ' '.join(''.join(FOLDS.get(c, c) for c in w) for w in ctext.split())
            key = make_design_key(ctext)
            n_true = key[4]
            seq = encipher_design(ctext, key, rng)
        else:
            key = make_key(ctext, rng)
            n_true = key[3]
            seq = encipher(ctext, key, rng)
        if mode in ('atlas', 'design'):
            noisy = atlas_noise(seq, n_true, rng, p)
            n_sym = 120
        else:
            noisy = line_noise(seq, n_true, rng, p)
            n_sym = n_true
        frac = len(tr_real) / (len(tr_real) + len(he_real))
        cut = int(len(noisy) * frac)
        res, *_ = run_pipeline(noisy[:cut], noisy[cut:], ctext, n_sym, draws, rng, wrong_pool,
                               f'control {mode} p={p} seed={seed}', nbd)
        json.dump(res, open(os.path.join(HERE, 'results', f'control_{mode}_p{int(p*100)}_s{seed}.json'), 'w'), indent=1)
        print(summary(res))
    elif a[0] == 'target':
        rng = random.Random(1574)
        ids = {s: n for n, s in enumerate(sorted(set(tr_real + he_real)))}
        tr = [ids[s] for s in tr_real]; he = [ids[s] for s in he_real]
        wrong_pool = sa.letters(fr)
        res, counts, path, key = run_pipeline(tr, he, dtext, len(ids), draws, rng, wrong_pool, 'target atlas', nbd)
        json.dump(res, open(os.path.join(HERE, 'results', 'target_atlas.json'), 'w'), indent=1)
        inv = {n: s for s, n in ids.items()}
        with open(os.path.join(HERE, 'results', 'target_atlas_counts.tsv'), 'w') as f:
            f.write('cluster\t' + '\t'.join(chr(97 + i) for i in range(26)) + '\n')
            for n in range(len(ids)):
                f.write(inv[n] + '\t' + '\t'.join(str(int(x)) for x in counts[n]) + '\n')
        with open(os.path.join(HERE, 'results', 'target_atlas_path.tsv'), 'w') as f:
            f.write('train_symbol_index\tletter_index\n')
            for i, j in path:
                f.write(f'{i}\t{j}\n')
        print(summary(res))
    elif a[0] == 'pairs':
        cmd_pairs()
    elif a[0] == 'key':
        cmd_key()
    elif a[0] == 'check':
        cmd_check()
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])

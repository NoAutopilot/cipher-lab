#!/usr/bin/env python3
"""R11-SIENAPOOL: rank every other transcribed piece of ASSi Concistoro 2308 fasc. 2 by sign-set overlap with no. 7.

Disk only. Inputs: this folder's transcripts/ plus Bourdeau's targets/siena1421/transcripts (dbourdeau/cyphersolver,
CC BY 4.0 text) given with --bourdeau DIR (a sparse clone; nothing of his is copied into the repository).
Statistics per sibling s vs no. 7:
  J  = Jaccard of the sign inventories (token types);
  B  = number of shared sign bigram types (adjacent cipher tokens within one run).
Nulls (pre-registered in PREREG-R11-SIENAPOOL.md):
  J: curveball swap randomisation of the piece x sign incidence matrix (keeps every piece's inventory size and every
     sign's piece count, so ubiquitous letters/digits are discounted); p = (#null >= obs + 1)/(n + 1).
  B: within-piece token shuffle of s and no. 7 (keeps inventories, destroys order); same p.
Clears = p <= 0.05/m (Bonferroni over m siblings) on J; B reported beside it.
--check reruns and compares with results_pool.json (rule 7).

R13-SIENAJ (6 Oct 2026, PREREG-R13-SIENAJ.md): --blind DIR replaces the rows of nos. 7, 19 and 9 by a second reader's blind sign
inventories (DIR/inv_noNN.tsv, first column = shape id; letters/digits named as themselves, drawn signs given per-letter ids), all
other rows unchanged; J only (no sequences were read, so B is not computed). --liberal additionally merges the doubtful drawn-sign
pairs of DIR/concordance.tsv (descriptive only, not gated). Output results_pool_blind[_liberal].json; --check works the same way.
"""
import argparse, json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(HERE, '..', '..', '..', 'ciphers', 'siena-concistoro-2308', 'transcripts')

def runs_from_tok(path, split_us=False):
    runs = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        for part in line.split('|'):
            toks = []
            for t in part.split():
                if split_us:
                    toks += [x for x in t.split('_') if x]
                else:
                    toks.append(t)
            toks = [t.rstrip('?') for t in toks if t not in ('.', '/', '//')]
            toks = [t for t in toks if t]
            if toks:
                runs.append(toks)
    return runs

def runs_from_txt(path, digits_only=False):
    """Lines 'Lnn ...' (agents G/J/K): drop [clear], {gloss}, <code word>, '.', '/', '?'; split runs at clear text."""
    runs = []
    in_tx = False
    for line in open(path, encoding='utf-8'):
        if re.match(r'^(TRANSCRIPTION|ENTRIES|L\d)', line):
            in_tx = True
        if not in_tx or not re.match(r'^L[\dP.]+\s', line):
            continue
        body = re.sub(r'^\s*L[\dP.]+\s+(y\d+\s+)?', '', line.rstrip('\n'))
        body = re.sub(r'^[^\[]*\]', ' | ', body)     # clear text continued from the line above
        body = re.sub(r'\{[^}]*\}', ' ', body)
        body = re.sub(r'<[^>]*>', ' | ', body)
        body = re.sub(r'\[[^\]]*\]?', ' | ', body)   # clear text breaks a run; unclosed '[' runs to line end
        for part in body.split('|'):
            toks = [t.rstrip('?') for t in part.replace('/', ' ').split() if t not in ('.',)]
            toks = [t for t in toks if t and t != '?' and t != '\u00b7' and not re.search(r'[()\[\]"]', t)]
            if digits_only:
                toks = [t for t in toks if t.isdigit()]
            if toks:
                runs.append(toks)
    return runs

def load(bdir):
    B = lambda f: os.path.join(bdir, f)
    F = lambda f: os.path.join(FOLDER, f)
    pieces = {
        '07': ('J', runs_from_tok(F('no07.tok'))),
        '04': ('G', runs_from_txt(B('no04.txt'))),
        '06': ('?', runs_from_tok(F('no06.tok'))),
        '09': ('J', runs_from_txt(B('no09.txt'))),
        '11': ('?', runs_from_tok(B('no11.tok'))),
        '14': ('?', runs_from_tok(B('no14.tok'), split_us=True)),
        '15': ('L', runs_from_tok(F('no15.tok'))),
        '17': ('?', runs_from_tok(B('no17.tok'))),
        '18': ('?', runs_from_tok(B('no18.tok'), split_us=True)),
        '19': ('J', runs_from_tok(F('no19.tok'))),
        '20': ('?', runs_from_tok(F('no20.tok'))),
        '21': ('J', runs_from_txt(B('no21.txt'))),
        '22': ('K', runs_from_txt(B('no22.txt'), digits_only=True)),
        '23': ('?', runs_from_tok(F('no23.tok'))),
        '24': ('?', runs_from_tok(F('no24p2.tok'))),
        '25': ('?', runs_from_tok(B('no25.tok'), split_us=True)),
    }
    return pieces

def bigrams(runs):
    return {(r[i], r[i + 1]) for r in runs for i in range(len(r) - 1)}

def jacc(a, b):
    return len(a & b) / len(a | b) if a | b else 0.0

def curveball(rows, rng, steps):
    rows = [set(r) for r in rows]
    n = len(rows)
    for _ in range(steps):
        i, j = rng.sample(range(n), 2)
        a, b = rows[i], rows[j]
        oa, ob = sorted(a - b), sorted(b - a)   # sorted: set order follows PYTHONHASHSEED
        if not oa or not ob:
            continue
        pool = oa + ob
        rng.shuffle(pool)
        k = len(oa)
        common = a & b
        rows[i] = common | set(pool[:k])
        rows[j] = common | set(pool[k:])
    return rows

def shuffle_runs(runs, rng):
    flat = [t for r in runs for t in r]
    rng.shuffle(flat)
    out, k = [], 0
    for r in runs:
        out.append(flat[k:k + len(r)]); k += len(r)
    return out

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--bourdeau', required=True, help='path to targets/siena1421/transcripts of a cyphersolver clone')
    ap.add_argument('--null', type=int, default=2000)
    ap.add_argument('--seed', type=int, default=11)
    ap.add_argument('--inventory-only', action='store_true', help='print parsed sizes and stop (no scoring)')
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--blind', help='dir with inv_no07.tsv, inv_no19.tsv, inv_no09.tsv (R13-SIENAJ)')
    ap.add_argument('--liberal', action='store_true', help='with --blind: merge the doubtful pairs of concordance.tsv')
    a = ap.parse_args()
    P = load(a.bourdeau)
    keys = sorted(P)
    inv = {k: {t for r in P[k][1] for t in r} for k in keys}
    ntok = {k: sum(len(r) for r in P[k][1]) for k in keys}
    if a.blind:
        merge = {}
        if a.liberal:
            for line in open(os.path.join(a.blind, 'concordance.tsv'), encoding='utf-8'):
                if line.startswith('#') or line.startswith('liberal_id'):
                    continue
                f = line.rstrip('\n').split('\t')
                for mbr in f[1].split():
                    merge[mbr] = f[0]
        for k in ('07', '19', '09'):
            fp = os.path.join(a.blind, 'inv_no%s.tsv' % k)
            if not os.path.exists(fp):
                continue
            ids = [l.split('\t')[0] for l in open(fp, encoding='utf-8') if not l.startswith('#') and not l.startswith('id\t') and l.strip()]
            inv[k] = {merge.get(i, i) for i in ids}
            P[k] = ('blind', P[k][1])
            ntok[k] = None
    if a.inventory_only:
        for k in keys:
            print(k, P[k][0], 'tokens', ntok[k], 'types', len(inv[k]))
        return
    sib = [k for k in keys if k != '07']
    m = len(sib)
    rng = random.Random(a.seed)
    rows = [inv[k] for k in keys]
    i7 = keys.index('07')
    obsJ = {k: jacc(inv[k], inv['07']) for k in sib}
    nullJ = {k: [] for k in sib}
    tot_inc = sum(len(r) for r in rows)
    for _ in range(a.null):
        rr = curveball(rows, rng, steps=5 * len(keys) * len(keys))
        for k in sib:
            nullJ[k].append(jacc(rr[keys.index(k)], rr[i7]))
    if a.blind:
        res = []
        for k in sib:
            nj = sorted(nullJ[k])
            pJ = (sum(x >= obsJ[k] - 1e-12 for x in nj) + 1) / (a.null + 1)
            shared = sorted(inv[k] & inv['07'])
            res.append(dict(piece=k, transcriber=P[k][0], types=len(inv[k]), shared_types=len(shared), J=round(obsJ[k], 4),
                            J_null_mean=round(sum(nj) / len(nj), 4), J_null_p99=round(nj[int(0.99 * len(nj)) - 1], 4),
                            pJ=round(pJ, 5), clears=pJ <= 0.05 / m, shared=shared))
        res.sort(key=lambda r: (r['pJ'], -r['J']))
        out = dict(seed=a.seed, null=a.null, m=m, alpha=0.05 / m, liberal=a.liberal, no07_types=len(inv['07']), rows=res)
        path = os.path.join(HERE, 'results_pool_blind%s.json' % ('_liberal' if a.liberal else ''))
        if a.check:
            if json.load(open(path)) != json.loads(json.dumps(out)):
                print('STALE: %s differs' % os.path.basename(path)); sys.exit(1)
            print('check ok'); return
        json.dump(out, open(path, 'w'), indent=1, ensure_ascii=False)
        print('piece tr types shared J Jnull_mean Jnull_p99 pJ clears')
        for r in res:
            print(r['piece'], r['transcriber'], r['types'], r['shared_types'], r['J'], r['J_null_mean'], r['J_null_p99'], r['pJ'], r['clears'])
        return
    b7 = bigrams(P['07'][1])
    obsB = {k: len(bigrams(P[k][1]) & b7) for k in sib}
    nullB = {k: [] for k in sib}
    for _ in range(a.null):
        s7 = bigrams(shuffle_runs(P['07'][1], rng))
        for k in sib:
            nullB[k].append(len(bigrams(shuffle_runs(P[k][1], rng)) & s7))
    res = []
    for k in sib:
        nj = sorted(nullJ[k]); nb = sorted(nullB[k])
        pJ = (sum(x >= obsJ[k] - 1e-12 for x in nj) + 1) / (a.null + 1)
        pB = (sum(x >= obsB[k] for x in nb) + 1) / (a.null + 1)
        shared = sorted(inv[k] & inv['07'])
        res.append(dict(piece=k, transcriber=P[k][0], tokens=ntok[k], types=len(inv[k]), shared_types=len(shared),
                        J=round(obsJ[k], 4), J_null_mean=round(sum(nj) / len(nj), 4), J_null_p99=round(nj[int(0.99 * len(nj)) - 1], 4),
                        pJ=round(pJ, 5), B=obsB[k], B_null_mean=round(sum(nb) / len(nb), 2), B_null_p99=nb[int(0.99 * len(nb)) - 1],
                        pB=round(pB, 5), clears=pJ <= 0.05 / m, shared=shared))
    res.sort(key=lambda r: (r['pJ'], -r['J']))
    out = dict(seed=a.seed, null=a.null, m=m, alpha=0.05 / m, no07_tokens=ntok['07'], no07_types=len(inv['07']), rows=res)
    path = os.path.join(HERE, 'results_pool.json')
    if a.check:
        old = json.load(open(path))
        if old != json.loads(json.dumps(out)):
            print('STALE: results_pool.json differs'); sys.exit(1)
        print('check ok'); return
    json.dump(out, open(path, 'w'), indent=1, ensure_ascii=False)
    print('piece tr tokens types shared J Jnull_mean Jnull_p99 pJ B Bnull_mean Bnull_p99 pB clears')
    for r in res:
        print(r['piece'], r['transcriber'], r['tokens'], r['types'], r['shared_types'], r['J'], r['J_null_mean'], r['J_null_p99'],
              r['pJ'], r['B'], r['B_null_mean'], r['B_null_p99'], r['pB'], r['clears'])

if __name__ == '__main__':
    main()

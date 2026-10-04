"""TX-ALTS Test 2 (pre-registered in tx_alts/PREREG.md). Run from harvest/: python3 tx_alts/test2.py
Builds ALTS (pass N with every a/b? alternative + pass B, from-passes --keep-alts), FIRST (N first choice only + B) and
CURRENT (A + B) lattices on f178r + f179r, decodes each at lam 4 and lam 1 (it16dip, printed key), and prints
truth-in-lattice, err_true, and the paired fixed/broken count with a one-sided sign test. Writes tx_alts/test2.json."""
import json, math, os, subprocess, sys
sys.path.insert(0, '../../../tools')
import key_decode_lattice as K
T = '../../../tools/key_decode_lattice.py'; O = 'tx_alts'
key = K.read_key('key_1572_sheet.tsv')
truth = {(r['line'], int(r['pos'])): (K.fold(r['value']) if r['value'].upper() != 'NULL' else '') for r in K.read_tsv('tx_decode/truth87.tsv')}
PAGES = ['f178r', 'f179r']

def strip(src, dst):
    rows = K.read_tsv(src)
    with open(dst, 'w') as f:
        f.write('passage\tpos\tsign_id\talt\tconf\tnote\n')
        for r in rows:
            first, _, conf = K.split_cands(r)
            f.write(f"{r['passage']}\t{r['pos']}\t{first}\t\t{conf}\t\n")

def lattice(name, pa_of, keep):
    out = f'{O}/t2_{name}_topk.tsv'; parts = []
    for p in PAGES:
        tmp = f'{O}/_t2_{name}_{p}.tsv'
        cmd = ['python3', T, 'from-passes', pa_of(p), f'{p}/passB.tsv', '--ref', f'ciphertext_{p}.tsv', '--confusion', 'confusion_1572.tsv', '--out', tmp]
        subprocess.run(cmd + (['--keep-alts'] if keep else []), check=True, capture_output=True)
        parts.append(open(tmp).read().splitlines()); os.remove(tmp)
    with open(out, 'w') as f:
        f.write('\n'.join(parts[0] + sum((x[1:] for x in parts[1:]), [])) + '\n')
    return out

def ok(c, k):
    t = truth.get(k)
    return t is not None and c in key and key[c] == t

for p in PAGES:
    strip(f'{O}/{p}_passN.tsv', f'{O}/{p}_passN_first.tsv')
L = {'CURRENT': lattice('current', lambda p: f'{p}/passA.tsv', False),
     'FIRST': lattice('first', lambda p: f'{O}/{p}_passN_first.tsv', False),
     'ALTS': lattice('alts', lambda p: f'{O}/{p}_passN.tsv', True)}
res = {}; seqs = {}
for name, path in L.items():
    lat = K.read_topk(path)
    t1 = K.top1(lat)
    errs = [k for (k, c), s in zip(lat, t1) if k in truth and not ok(s, k)]
    cov = sum(1 for (k, c) in lat if k in errs and any(ok(x, k) for x in c))
    res[name] = {'positions': len(lat), 'aligned': sum(1 for k, _ in lat if k in truth), 'top1_errors': len(errs),
                 'truth_in_lattice_at_top1_errors': cov, 'mean_cands': round(sum(len(c) for _, c in lat) / len(lat), 2)}
    seqs[(name, 'top1')] = dict(zip([k for k, _ in lat], t1))
    for lam in (4, 1):
        j = json.loads(subprocess.run(['python3', T, 'decode', path, '--key', 'key_1572_sheet.tsv', '--lang', 'it16dip', '--truth', 'tx_decode/truth87.tsv',
                                       '--lam', str(lam), '--out-prefix', f'{O}/t2_{name.lower()}_lam{lam}'], check=True, capture_output=True, text=True).stdout)
        res[name][f'lam{lam}'] = {'changed': j['changed'], **j['truth_lattice']}
        d = K.read_tsv(f'{O}/t2_{name.lower()}_lam{lam}.decode.tsv')
        seqs[(name, lam)] = {(r['line'], int(r['pos'])): r['chosen'] for r in d}

def paired(a, b):
    fixed = broken = 0
    for k in truth:
        if k[0].split('_')[0] not in PAGES or k not in a or k not in b:
            continue
        ra, rb = ok(a[k], k), ok(b[k], k)
        fixed += (not ra) and rb; broken += ra and not rb
    n = fixed + broken
    p = sum(math.comb(n, i) for i in range(fixed, n + 1)) / 2 ** n if n else 1.0
    return {'fixed': fixed, 'broken': broken, 'p_one_sided': round(p, 4)}

# FIRST and ALTS share N's first choices, so their skeletons match position for position (same --ref).
res['paired_ALTS_vs_FIRST'] = {str(lam): paired(seqs[('FIRST', lam)], seqs[('ALTS', lam)]) for lam in (4, 1)}
res['paired_ALTS_vs_CURRENT'] = {str(lam): paired(seqs[('CURRENT', lam)], seqs[('ALTS', lam)]) for lam in (4, 1)}
res['paired_ALTSlam4_vs_FIRSTtop1'] = paired(seqs[('FIRST', 'top1')], seqs[('ALTS', 4)])
json.dump(res, open(f'{O}/test2.json', 'w'), indent=1)
print(json.dumps(res, indent=1))

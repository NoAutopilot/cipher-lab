#!/usr/bin/env python3
"""Key from the period clear copy of BnF fr.4140 f.146r (Sabran, 9 Aug 1636; clear copy f.151r), and its trial on
Baluze 156 f.157r (DC8). FT4b (account-4), 3 Oct 2026.

Step 1 (key, grade C). images/fr4140/pairs_f146.tsv holds one row per cipher run on f.146r: the reconciled cipher tokens
(prefixed @, interlinear_align.py --code-prefix mode: one sign = 0 or 1 plain letter) and the clear words that the
period copy f.151r gives for that run. tools/interlinear_align.py's run_align aligns every run; a sign's value is its
majority letter.
Step 2 (rule 3, leaf control). The same alignment with the clear spans permuted across runs (200 draws, length
structure kept by the runs themselves): the share of sign occurrences that agree with their sign's majority letter
(n >= 2) must beat the shuffled pairings' 99th percentile, or the key is not used.
Step 3 (target test). Every DC8 token whose class is in the key is decoded; the French 5-gram bits/char of the
decoded runs (tools/french16_ngram.py, the same scorer as letters_trial.py / servien_trial.py; unmapped token breaks
a run) is compared with 200 shuffled keys (the key's letters permuted over its signs, homophone structure kept), and
a positive control (held-out French of the same run lengths enciphered with the key, decoded with it).

  python3 fr4140_trial.py           # print and rewrite fr4140_trial.tsv, images/fr4140/key_f146.tsv, fr4140_decode.txt
  python3 fr4140_trial.py --check   # exit 1 if any of them is stale
"""
import csv, os, sys, random, itertools, io
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from french16_ngram import load
import interlinear_align as IA

N_SHUF = 200
PAIRS = os.path.join(HERE, 'images', 'fr4140', 'pairs_f146.tsv')


def read_tsv(fn):
    with open(fn, encoding='utf-8') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def align(pairs):
    prepared, results, counts, shown = IA.run_align(pairs, clear_consumes=True, code_prefix='@')
    rows = IA.token_rows(prepared, results, counts, shown)
    codes = [r for r in rows if r[3] == 'code']
    agree = sum(r[7] == 'agrees' for r in codes)
    return agree / max(1, len(codes)), counts, rows


pairs = read_tsv(PAIRS)
real_share, counts, rows = align(pairs)
rng = random.Random(1636)
shuf_shares = []
for i in range(N_SHUF):
    plains = [p['plain_raw'] for p in pairs]
    rng.shuffle(plains)
    sp = [dict(p, plain_raw=q) for p, q in zip(pairs, plains)]
    shuf_shares.append(align(sp)[0])
shuf_shares.sort()
ctrl_p99 = shuf_shares[int(0.99 * N_SHUF) - 1]
leaf_pass = real_share > ctrl_p99

# key: majority letter per sign; kept only if seen >= 2 times with majority >= 2/3, or once with no conflict
key = {}
key_rows = []
for v in sorted(counts, key=str):
    cnt = counts[v]
    (top, topn), n = IA.top_of(cnt), sum(cnt.values())
    keep = len(top) == 1 and ((n >= 2 and topn / n >= 2 / 3) or n == 1)
    if keep:
        key[str(v)] = top.upper().replace('U', 'V').replace('J', 'I')
    key_rows.append((v, top, n, topn, ','.join(f'{m}:{c}' for m, c in cnt.items() if m != top), 'kept' if keep else 'dropped'))

M = load()
_cache = {}
def lp(s):
    if s not in _cache: _cache[s] = M.logp(s)
    return _cache[s]

def runs(tl, mp):
    out = []
    for toks in tl:
        cur = ''
        for t in toks:
            if t in mp: cur += mp[t]
            else:
                if cur: out.append(cur)
                cur = ''
        if cur: out.append(cur)
    return out

def bpc(rs):
    n = sum(len(r) for r in rs)
    return -sum(lp(r) for r in rs) / n if n else float('nan')

dc8 = read_tsv(os.path.join(HERE, 'ciphertext_draft.tsv'))
lines = [[r['sign'] for r in g] for _, g in itertools.groupby(dc8, key=lambda r: r['line'])]
n_tok = sum(len(l) for l in lines)
covered = sum(t in key for l in lines for t in l)
real_runs = runs(lines, key)
real = bpc(real_runs)
signs, vals = list(key), [key[s] for s in key]
shuf = []
for i in range(N_SHUF):
    vs = vals[:]; rng.shuffle(vs)
    shuf.append(bpc(runs(lines, dict(zip(signs, vs)))))
shuf.sort()
pct = sum(s <= real for s in shuf) / N_SHUF

# variant: DC8's '4' read as f.146r's crossed-tail a (a+ = i), the one shape pair the reconciler found the passes split on
key_v = dict(key); key_v['4'] = key['a+']
real_v = bpc(runs(lines, key_v))
shuf_v = []
for i in range(N_SHUF):
    vs = [key_v[s] for s in key_v]; rng.shuffle(vs)
    shuf_v.append(bpc(runs(lines, dict(zip(list(key_v), vs)))))
pct_v = sum(x <= real_v for x in shuf_v) / N_SHUF

inv = {}
for s, v in key.items(): inv.setdefault(v, []).append(s)
text = ''.join(M._held)
i = rng.randrange(0, len(text) - 5 * max(1, sum(map(len, real_runs))))
segs = []
for L in [len(r) for r in real_runs]: segs.append(text[i:i + L]); i += L + 7
syn = [[rng.choice(inv[ch]) if ch in inv else '?' for ch in seg] for seg in segs]
pos = bpc(runs(syn, key))
pos_shuf = []
for _ in range(N_SHUF):
    vs = vals[:]; rng.shuffle(vs)
    pos_shuf.append(bpc(runs(syn, dict(zip(signs, vs)))))
pos_shuf.sort()
pos_pct = sum(s <= pos for s in pos_shuf) / N_SHUF
words = sorted({w for r in real_runs for a in range(len(r)) for b in range(a + 4, len(r) + 1)
                if (w := r[a:b]) in M.words and M.words[w] >= 20})

out = [('# fr4140_trial.tsv -- regenerated by fr4140_trial.py (3 Oct 2026); bits/char lower = more French', ''),
       ('key_source', 'period clear copy BnF fr.4140 f.151r of cipher letter f.146r (9 Aug 1636), reconciled runs'),
       ('runs', len(pairs)), ('code_tokens_aligned', sum(r[3] == 'code' for r in rows)),
       ('leaf_agree_share', f'{real_share:.3f}'), ('leaf_shuffle_median', f'{shuf_shares[N_SHUF // 2]:.3f}'),
       ('leaf_shuffle_p99', f'{ctrl_p99:.3f}'), ('leaf_beats_control', 'yes' if leaf_pass else 'no'),
       ('key_signs_kept', len(key)), ('key_signs_dropped', sum(r[5] == 'dropped' for r in key_rows)),
       ('dc8_tokens', n_tok), ('dc8_tokens_covered_by_key', covered),
       ('dc8_letters_decoded', sum(map(len, real_runs))),
       ('real_bpc', f'{real:.3f}'), ('shuffle_median_bpc', f'{shuf[N_SHUF // 2]:.3f}'),
       ('shuffle_best_bpc', f'{shuf[0]:.3f}'), ('real_share_of_shuffles_as_good_or_better', f'{pct:.3f}'),
       ('variant_dc8_4_as_a+_bpc', f'{real_v:.3f}'), ('variant_share_of_shuffles_as_good_or_better', f'{pct_v:.3f}'),
       ('positive_control_bpc', f'{pos:.3f}'), ('positive_shuffle_median_bpc', f'{pos_shuf[N_SHUF // 2]:.3f}'),
       ('positive_share_of_shuffles_as_good_or_better', f'{pos_pct:.3f}'),
       ('real_words_ge4_in_decode', ' '.join(words) or '(none)'),
       ('real_decode_runs', ' '.join(real_runs)),
       ('verdict', ('reads' if pct < 0.01 and real < pos + 0.5 else 'does not read (negative, matched)')
        if leaf_pass else 'key not licensed (leaf control failed); target test reported for the record only')]
body = '\n'.join(f'{k}\t{v}' if v != '' else k for k, v in out) + '\n'
kbuf = io.StringIO()
w = csv.writer(kbuf, delimiter='\t', lineterminator='\n')
w.writerow(['sign', 'letter', 'n', 'agree', 'others', 'status'])
w.writerows(key_rows)
dec = []
for l, g in itertools.groupby(dc8, key=lambda r: r['line']):
    dec.append(l + '\t' + ' '.join(f"{r['sign']}={key.get(r['sign'], '?')}" for r in g))
files = {os.path.join(HERE, 'fr4140_trial.tsv'): body, os.path.join(HERE, 'images', 'fr4140', 'key_f146.tsv'): kbuf.getvalue(),
         os.path.join(HERE, 'fr4140_decode.txt'): '\n'.join(dec) + '\n'}
if '--check' in sys.argv:
    stale = [f for f, b in files.items() if not os.path.exists(f) or open(f, encoding='utf-8').read() != b]
    if stale: print('stale:', ' '.join(map(os.path.basename, stale))); sys.exit(1)
    print('fr4140 trial files up to date'); sys.exit(0)
for f, b in files.items(): open(f, 'w', encoding='utf-8').write(b)
print(body)

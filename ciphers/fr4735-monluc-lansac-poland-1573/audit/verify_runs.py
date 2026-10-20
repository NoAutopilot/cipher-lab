"""VERIFY-MONLUC: how many C (confirm) tokens sit in runs of consecutive confirms, real vs shuffled-clear and vs f.139."""
import sys, random, json, collections
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, sys.argv[1] + '/c269')
import align_c268 as A
import align_c269 as B
def runs(rows):
    # run = maximal sequence of keyed confirm tokens with consecutive clear positions (unkeyed/fill tokens break nothing if empty)
    lens = []; cur = 0; last = None
    for r in rows:
        if r['value'] is None and not r['clear']: continue
        if r['kind'] == 'confirm' and (last is None or r['cpos'] == last + 1):
            cur += 1
        else:
            if cur: lens.append(cur)
            cur = 1 if r['kind'] == 'confirm' else 0
        last = r['cpos'] if r['kind'] == 'confirm' else None
    if cur: lens.append(cur)
    return lens
def dist(lens, keyed):
    tot = sum(lens)
    return {k: round(sum(l for l in lens if l >= k) / keyed, 3) for k in (1, 2, 3, 4, 5)}
def go(name, toks, clear, unsure, other, draws=20):
    _, p, _, _ = A.align(toks, clear); rows = A.classify(toks, clear, p, unsure)
    keyed = sum(t['value'] is not None for t in toks)
    out = {'real': dist(runs(rows), keyed)}
    _, p, _, _ = A.align(toks, other); out['f139'] = dist(runs(A.classify(toks, other, p)), keyed)
    words = [w[2] for w in A.load_clear()]; rng = random.Random(7); acc = collections.defaultdict(list)
    for _ in range(draws):
        rng.shuffle(words); c = ''.join(words)
        _, p, _, _ = A.align(toks, c)
        for k, v in dist(runs(A.classify(toks, c, p)), keyed).items(): acc[k].append(v)
    out['shuffled_mean'] = {k: round(sum(v)/len(v), 3) for k, v in acc.items()}
    out['shuffled_max'] = {k: max(v) for k, v in acc.items()}
    print(name, json.dumps(out), flush=True)
words = A.load_clear(); clear = ''.join(w[2] for w in words); unsure = [w[3] for w in words for _ in w[2]]
other = A.fold(open(A.HERE / 'c270_text.txt', encoding='utf-8').read())
go('c268', A.load_tokens(), clear, unsure, other)
# c269 graded bands, against the clear after c268's end (align_c269's own restriction)
_, _, _, end = A.align(A.load_tokens(), clear)
key = {l.split('\t')[0]: l.split('\t')[2] for l in list(open(A.HERE / 'key.tsv'))[1:]}
toks = [{'line': f[0], 'pos': int(f[1]), 'sign': f[2], 'conf': f[3], 'value': A.fold(key[f[2]]) if key.get(f[2]) else None}
        for fn, g in B.BANDS for f in [l.rstrip('\n').split('\t') for l in open(B.HERE / fn)][1:]]
go('c269', toks, clear[end:], unsure[end:], other)

"""catokjoint.py -- neighbour-conditioned phrase-level LM search (NEAR-POLL, 9 Oct 2026), pre-registered in
ciphers/pollaky-1865-1875/PREREG-NEAR-POLL.md. Our own code; imports catoklm.py (R13-CATOKLM) and catok23.py unmodified.
Only change from catoklm: the first word is scored P(w1 | left context) and P(right context | last word) is added.

  python3 catokjoint.py run --line N     control first, target only if the control meets the gate -> catokjoint_lineN.json
  python3 catokjoint.py known            known-answer lines 7, 27, 28 -> catokjoint_known.json
  python3 catokjoint.py merge            merge into catokjoint.json
  python3 catokjoint.py --check          re-run everything and exit 1 if catokjoint.json is stale (~20 min, 4 processes)
"""
import collections, json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import catoklm as M  # noqa: E402
from catok23 import pairs, trie, edges, MAX_LINE_OMIT  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CTX = {9: ('lectures', None), 26: ('lectures', 'dying'), 29: ('declaration', None)}
KNOWN = {7: (None, 'i', 'repeated'), 27: (None, 'declaration', 'dying'), 28: ('dying', None, 'declaration')}


def kbest(A, B, lm, T, left, right):
    a, b = len(A), len(B)
    best = collections.defaultdict(list); best[(0, 0)] = [(0.0, 0, ())]
    for (i, j) in sorted(((i, j) for i in range(a + 1) for j in range(b + 1)), key=lambda x: x[0] + x[1]):
        cur = best.get((i, j))
        if not cur or (i, j) == (a, b): continue
        cur.sort(reverse=True); del cur[M.BEAM:]
        for w, ni, nj, om in edges(i, j, A, B, T):
            base = M.first_src(w, i, j, A, B) - M.OMIT * om
            end = (ni, nj) == (a, b)
            lst = best[(ni, nj)]
            for sc, tot, ws in cur:
                if tot + om <= MAX_LINE_OMIT:
                    s = sc + base + lm.lp(ws[-1] if ws else left, w)
                    if end and right: s += lm.lp(w, right)
                    lst.append((s, tot + om, ws + (w,)))
            if len(lst) > 4 * M.BEAM:
                lst.sort(reverse=True); del lst[M.BEAM:]
    seen, final = set(), []
    for sc, tot, ws in sorted(best[(a, b)], reverse=True):
        if ws not in seen: seen.add(ws); final.append((round(sc, 3), tot, ' '.join(ws)))
    return final[:M.K]


def control(A, B, lm, T, held, rng, use_l, use_r):
    L = len(A) + len(B)
    c = {'n': 0, 'unique': 0, 'correct_unique': 0, 'wrong_unique': 0, 'planted_in_top20': 0, 'word_acc_top1': 0.0,
         'examples': []}
    while c['n'] < M.NCTL:
        t = rng.choice(held); target = L + rng.randint(3, 12)
        k = rng.randrange(1, len(t) - 60); k0 = k; ws = []
        while sum(map(len, ws)) < target: ws.append(t[k]); k += 1
        left = t[k0 - 1] if use_l else None; right = t[k] if use_r else None
        if sum(map(len, ws)) - L > 12 or any(w not in lm.V for w in ws): continue
        if (use_l and left not in lm.V) or (use_r and right not in lm.V): continue
        s = M.synth_prior(ws, L, len(A), rng)
        if s is None: continue
        a, b = s
        rr = kbest(a, b, lm, T, left, right); uu, _ = M.verdict(rr)
        planted = ' '.join(ws); top = rr[0][2] if rr else ''
        c['n'] += 1; c['unique'] += uu
        c['correct_unique'] += uu and top == planted; c['wrong_unique'] += uu and top != planted
        c['planted_in_top20'] += any(x[2] == planted for x in rr)
        c['word_acc_top1'] += M.wordacc(top, planted) if top else 0.0
        if len(c['examples']) < 3:
            c['examples'].append({'left': left, 'planted': planted, 'right': right, 'A': a, 'B': b, 'top': top})
    for k in ('unique', 'correct_unique', 'wrong_unique', 'planted_in_top20', 'word_acc_top1'):
        c[k] = round(c[k] / M.NCTL, 4)
    c['gate_met'] = c['correct_unique'] >= 0.50 and c['wrong_unique'] <= 0.10
    return c


def setup():
    train, held = M.corpus(); lm = M.LM(train); return lm, trie(lm.V), held


def run_line(ln):
    lm, T, held = setup(); A, B = pairs()[ln]; left, right = CTX[ln]
    ctl = control(A, B, lm, T, held, random.Random(M.SEED + ln), left is not None, right is not None)
    row = {'line': ln, 'A': A, 'B': B, 'letters': len(A) + len(B), 'left': left, 'right': right, 'control': ctl}
    if not ctl['gate_met']:
        row['target'] = None
        row['verdict'] = 'CONTROL BELOW GATE: untestable by this instrument at this N; target not scored'
    else:
        r = kbest(A, B, lm, T, left, right); u, m = M.verdict(r)
        row['target'] = {'unique': u, 'margin': m, 'top5': r[:5]}
        row['verdict'] = 'unique, control-backed (S)' if u else 'control-backed: not forced by this instrument'
    print(json.dumps({k: row[k] for k in ('line', 'verdict')}), {k: ctl[k] for k in ctl if k != 'examples'}, flush=True)
    return row


def known():
    lm, T, _ = setup(); P = pairs(); out = []
    for ln, (left, right, pub) in KNOWN.items():
        A, B = P[ln]; r = kbest(A, B, lm, T, left, right); u, m = M.verdict(r)
        out.append({'line': ln, 'A': A, 'B': B, 'left': left, 'right': right, 'published': pub,
                    'top1': r[0][2] if r else None, 'top1_is_published': bool(r) and r[0][2] == pub,
                    'unique': u, 'margin': m, 'published_rank': next((k + 1 for k, x in enumerate(r) if x[2] == pub), None),
                    'top5': r[:5]})
        print(out[-1]['line'], out[-1]['top1'], out[-1]['unique'], out[-1]['published_rank'], flush=True)
    return out


def merge():
    res = {'prereg': 'ciphers/pollaky-1865-1875/PREREG-NEAR-POLL.md', 'lines': [], 'known_answer': None}
    for ln in CTX:
        f = os.path.join(HERE, 'catokjoint_line%d.json' % ln)
        res['lines'].append(json.load(open(f)) if os.path.exists(f) else
                            {'line': ln, 'control': None, 'target': None,
                             'verdict': 'control run not completed inside the box; target not scored'})
    f = os.path.join(HERE, 'catokjoint_known.json')
    if os.path.exists(f): res['known_answer'] = json.load(open(f))
    return res


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['run']:
        ln = int(a[a.index('--line') + 1])
        json.dump(run_line(ln), open(os.path.join(HERE, 'catokjoint_line%d.json' % ln), 'w'), indent=1)
    elif a[:1] == ['known']:
        json.dump(known(), open(os.path.join(HERE, 'catokjoint_known.json'), 'w'), indent=1)
    elif a[:1] == ['merge']:
        json.dump(merge(), open(os.path.join(HERE, 'catokjoint.json'), 'w'), indent=1)
        for ln in list(CTX) + ['known']:
            f = os.path.join(HERE, 'catokjoint_%s.json' % (ln if ln == 'known' else 'line%d' % ln))
            if os.path.exists(f): os.remove(f)
    elif a[:1] == ['--check']:
        old = json.load(open(os.path.join(HERE, 'catokjoint.json')))
        new = {'lines': [run_line(r['line']) if r['control'] is not None else r for r in old['lines']],
               'known_answer': known() if old['known_answer'] is not None else None}
        new = json.loads(json.dumps(new))
        ok = new['lines'] == old['lines'] and new['known_answer'] == old['known_answer']
        print('OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    else: print(__doc__)

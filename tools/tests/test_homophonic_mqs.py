#!/usr/bin/env python3
"""Offline test for the MQS-SOLVER options on tools/homophonic_anneal.py and tools/families/homophonic.py (9 Oct 2026;
Lasry, Biermann and Tomokiyo 2023 App. A; CTTS). No network. Each block names what it must catch / must not block.

  python3 tools/tests/test_homophonic_mqs.py
"""
import json, os, random, subprocess, sys, tempfile
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(R, 'tools'))
import homophonic_anneal as ha
from collections import Counter

TXT = ('nousauonsreceuostrelettredudixiemedecemoisetlesennemisontpasselarivieredelalysetmarchentersgand'
       'leroyuostremaistreestencoreaparisetattendlesnouuellesdelaroynesamere')
m = ha.Model([TXT * 20, 'lesennemisontpasselarivieredelalysetmarchentersgand' * 10], 3)
p = ha.fold(TXT * 2)
seq, pp, truth = ha.make_control(p, 34, len(p), m, 3)

# 1. must NOT change: every default run reproduces today's scores byte for byte at a fixed seed. The fixture values
#    below were recorded from the pre-MQS code (commit before MQS-SOLVER) on this exact toy.
def default_runs():
    out = []
    for norm in ('none', 'nc2'):
        for uw in (0.0, 1.0):
            r = ha.solve(seq, m, 2, 3000, 7, uw, norm=norm)
            out.append([round(r[0][0], 9), sorted(r[0][1].items())])
    return out
import hashlib
FIX_SHA = '78248e33914cb4121f7178c44ed8413dbce88fa31ddb53406e89941cca02ccf0'  # sha256 of json.dumps(default_runs()) from the pre-MQS-SOLVER code (main at d77ba19fb)
got = hashlib.sha256(json.dumps(json.loads(json.dumps(default_runs()))).encode()).hexdigest()
assert got == FIX_SHA, 'default anneal output changed'
# explicit defaults equal implicit ones (the MQS kwargs at their defaults do not perturb the RNG stream)
r1 = ha.solve(seq, m, 2, 2000, 5, 1.0)
r2 = ha.solve(seq, m, 2, 2000, 5, 1.0, moves='reassign', max_homophones=0, gaps=None, min_count=0, homophone_budget=0)
assert r1 == r2
print('ok default unchanged (fixture + explicit defaults)')

# 2. swap preserves the multiset of assigned letters (every accepted state); must catch: a swap that changes counts
start = {}
def chk_swap(key):
    c = Counter(key.values())
    assert c == start['c'], 'swap changed the letter multiset'
rng = random.Random(11)
k0 = ha._init_key_mqs(sorted(set(seq)), {}, {}, {}, list(ha.ALPHA), [m.freq[a] for a in ha.ALPHA], random.Random(11), 0, 'swap')
start['c'] = Counter(k0.values())
sc, key = ha.anneal(seq, m, 3000, random.Random(11), 1.0, moves='swap', on_accept=chk_swap)
assert Counter(key.values()) == start['c']
# incremental score under swap equals a full re-score, every norm, with and without gaps
for norm in ('none', 'nc2', 'nc2paper'):
    for g in (None, {seq[3]}):
        sc, key = ha.anneal(seq, m, 2000, random.Random(2), 1.0, moves='both', norm=norm, gaps=g)
        full = ha.score(m, ''.join(key.get(x, ha.GAP) for x in seq), 1.0, norm)
        assert abs(sc - full) < 1e-6, (norm, g, sc, full)
print('ok swap multiset; swap/both incremental == full score (none, nc2, nc2paper; with/without gaps)')

# 3. cap never exceeded in any accepted state (must catch: a key piling signs on e); must NOT block a within-cap key
def chk_cap(key):
    assert max(Counter(key.values()).values()) <= 2, 'cap exceeded'
for mv in ('reassign', 'both', 'swap'):
    sc, key = ha.anneal(seq, m, 3000, random.Random(4), 1.0, moves=mv, max_homophones=2, on_accept=chk_cap)
    chk_cap(key)
try:
    ha.anneal(['a%d' % i for i in range(60)], m, 10, random.Random(1), 1.0, max_homophones=2)
    raise AssertionError('infeasible cap not refused')
except ValueError:
    pass
print('ok cap held in every accepted state (reassign, both, swap); infeasible cap refused')

# 4. --min-count / --homophone-budget: processed share reported, low-count signs read '?'
cnt = Counter(seq)
g, share = ha.search_gaps(seq, min_count=3)
low = {s for s, c in cnt.items() if c < 3}
assert g == low and abs(share - sum(1 for x in seq if x not in low) / len(seq)) < 1e-12
res = ha.solve(seq, m, 1, 1500, 3, 1.0, min_count=3)
dec = ''.join(res[0][1].get(x, ha.GAP) for x in seq)
assert all(dec[i] == ha.GAP for i, x in enumerate(seq) if x in low) and all(x not in res[0][1] for x in low)
assert all(dec[i] != ha.GAP for i, x in enumerate(seq) if x not in low)
g2, sh2 = ha.search_gaps(seq, budget=10)
assert len(set(seq) - g2) == 10 and sh2 < 1.0
# CLI reports the share (control mode, no network)
with tempfile.TemporaryDirectory() as d:
    open(os.path.join(d, 'c.txt'), 'w').write(TXT * 20)
    open(os.path.join(d, 'p.txt'), 'w').write(' '.join(TXT[i:i + 5] for i in range(0, len(TXT), 5)) * 4)
    cmd = [sys.executable, os.path.join(R, 'tools', 'homophonic_anneal.py'), '--control', os.path.join(d, 'p.txt'),
           '--signs', '30', '--length', '300', '--corpus', os.path.join(d, 'c.txt'), '--restarts', '1', '--iters', '500',
           '--control-homs', '1-2', '--min-count', '4', '--out', os.path.join(d, 'o.json')]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    assert 'processed' in out, out
    o = json.load(open(os.path.join(d, 'o.json')))
    assert 0 < o['processed_share'] < 1 and o['homs_per_letter'] and max(int(k) for k in o['homs_per_letter']) <= 2
    # marked control: unknown mode keeps marked signs as gaps, skip deletes them; both score the same letter tokens
    for mode in ('skip', 'unknown', 'wild', 'nomen'):
        subprocess.run(cmd[:-6] + ['--marked', '0.3:20', '--marked-mode', mode, '--out', os.path.join(d, mode + '.json')],
                       capture_output=True, text=True, check=True)
    js = {k: json.load(open(os.path.join(d, k + '.json'))) for k in ('skip', 'unknown', 'wild', 'nomen')}
    assert len({j['letter_tokens'] for j in js.values()}) == 1 and js['skip']['marked_share'] > 0.15
print('ok min-count/budget gaps and processed share (library + CLI); marked control, four modes, one denominator')

# 5. --drop-letters h / --collapse-doubles
try:
    ha.set_text_options('h', False)
    assert ha.fold('Le chasteau Hault') == 'lecasteauault'
    mh = ha.Model([TXT + 'chachacha'], 3)
    assert 'h' not in mh.alpha and 'h' not in mh.freq and mh.V == 23
    r = ha.solve(seq, mh, 1, 500, 1, 1.0)
    assert 'h' not in ''.join(r[0][1].values())
    ha.set_text_options('', True)
    assert ha.fold('passee assez') == 'paseasez' and 'ss' not in ha.fold(TXT * 3)
finally:
    ha.set_text_options()
assert ha.fold('passee hault') == 'passeehault' and not hasattr(ha.Model([TXT], 3), 'alpha')
print('ok drop-letters h (model and output), collapse-doubles ss->s, defaults restored')

# 6. --as-unknown: no scored window crosses a gap; must catch: the same probe under --skip (deletion) does cross
probe = ['a', 'b', 'X', 'c', 'd']
seen = []
class Spy:
    order, freq = 3, m.freq
    def logp(self, g):
        seen.append(g); return -1.0
ha.score(Spy(), 'ab?cd', 0.0)
assert seen == [], seen                              # ab?cd: both fragments shorter than 3, nothing scored
seen.clear(); ha.score(Spy(), 'abcd', 0.0)          # the --skip stream: X deleted, 'abc' and 'bcd' join across it
assert seen == ['abc', 'bcd'], seen
# the anneal's own windows: none spans the gap sign's position
seq2 = list('abcdefgh'); seq2[4] = 'X'
spy = []
class Spy2:
    order, freq = 3, {a: 1 / 24 for a in ha.ALPHA}
    def logp(self, g):
        spy.append(g); assert ha.GAP not in g, g; return -1.0
ha.anneal(seq2, Spy2(), 200, random.Random(1), 0.0, gaps={'X'})
assert spy and all(ha.GAP not in g for g in spy)
print('ok as-unknown: no window spans a gap; the --skip stream does join neighbours')

# 7. nc2paper equals raw / sum N_c^2 (times the constant n^2 q0) on a toy; nc2 does not in general
t = ha.fold('lesennemisontpasse')
raw = sum(m.logp(t[i:i + 3]) for i in range(len(t) - 2))
sq = sum(c * c for c in Counter(t).values())
n = len(t)
assert abs(ha.paper_score(raw, sq) - raw / sq) < 1e-12
assert abs(ha.score(m, t, 0.0, 'nc2paper') - raw / sq * n * n * ha.nc2_q0(m)) < 1e-9
# ranking: the paper's ranking between two plaintexts of one length is nc2paper's
u = ha.fold('aaaaaaaaaaaaaaaaaa')
rawu = sum(m.logp(u[i:i + 3]) for i in range(len(u) - 2)); squ = len(u) ** 2
assert (ha.score(m, t, 0.0, 'nc2paper') > ha.score(m, u, 0.0, 'nc2paper')) == (raw / sq > rawu / squ)
print('ok nc2paper == raw / sum N_c^2 x n^2 q0; ranking is the paper\'s')

# 8. families/homophonic.py --param names reach the solver; absent = old behaviour
from families import homophonic as fh
msgs = [seq]
d1 = fh.solve(msgs, {}, 3, 1, [TXT * 20], {'iters': 800})
d0 = ha.solve(seq, ha.Model([TXT * 20], 3), 1, 800, 3, 1.0)
assert d1[1] == d0[0][0]
d2 = fh.solve(msgs, {}, 3, 1, [TXT * 20], {'iters': 800, 'moves': 'both', 'max_homophones': '2', 'min_count': '3',
                                           'norm': 'nc2paper'})
assert ha.GAP in d2[0] and max(Counter(d2[2]['key'].values()).values()) <= 2
with tempfile.TemporaryDirectory() as d:
    f = os.path.join(d, 'cls.txt'); open(f, 'w').write(seq[0] + '\n')
    d3 = fh.solve(msgs, {}, 3, 1, [TXT * 20], {'iters': 800, 'exclude': f})
    assert all(d3[0][i] == ha.GAP for i, x in enumerate(seq) if x == seq[0])
print('ok families/homophonic --param moves/max_homophones/min_count/norm=nc2paper/exclude')
print('all MQS-SOLVER tests passed')

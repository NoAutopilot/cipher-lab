#!/usr/bin/env python3
"""GAPS-spinelli-beinecke-c1515 (2 Oct 2026, account-4): sign-level alignment of passes/ciphertext_v6.txt against the
joined 2017 Cipherbrain reading (Norbert #7 for p.1, Thomas #10 for p.2 -- the N0 plaintext, verify2/cipherbrain_2017-03-24_tommaso.txt),
using the shared known-plaintext aligner tools/interlinear_align.py (run_align / token_rows, --code-prefix mode) rather than a private DP.

What this answers (gap 1 of NOTES.md "Remaining gaps"): for every one of the 259 v6 signs, which plain letter of the 2017 text it sits
over, and whether that letter agrees with the sign's key.tsv value -- so the next transcription pass knows WHICH signs to re-read,
not only which lines. No vision, no requests, no key change. Grades: the 2017 text is a modern reading (C-with-a-note, not H).

Conventions (rule 3, PX-BRODEC: one convention on both sides before diffing): u/v and i/j folded; the 2017 text's [bracketed] editorial
insertions and (?) dropped (as verify2/compare_2017.py); 'que' -> 'k' and 'rr' -> 'w' pre-folded (letters absent from the text) to one character each because the
aligner's --code-prefix mode gives every sign 0 or 1 plain characters (EPSILON = que, EIGHTBAR = rr|cc in the atlas key); Thomas #10's
'??' kept as two wildcard positions. Each passage is one segment (no word boundaries), so the aligner's segment bonuses cannot pull
null signs onto word-initial letters. --null-cost 0: a sign may take no letter at no charge (nulls are unseeded).

Control (rule 3): the same alignment, same prior, against the 2017 letters shuffled within each passage (20 seeds). The statistic
(share of letter-bearing signs whose aligned letter equals their key value) varies with letter order, so the control can fail.

    python3 verify2/align_2017.py            # writes verify2/align_2017_pairs.tsv, _prior.tsv, _align.tsv, _key.tsv, _signs.tsv, _summary.json
CLI equivalent of the real run: python3 tools/interlinear_align.py align verify2/align_2017_pairs.tsv OUT_ALIGN OUT_KEY --code-prefix @ --prior verify2/align_2017_prior.tsv --null-cost 0 --wildcard ?
"""
import os, sys, csv, json, random, importlib.util
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H); R = os.path.dirname(os.path.dirname(T))
spec = importlib.util.spec_from_file_location('ia', os.path.join(R, 'tools', 'interlinear_align.py')); ia = importlib.util.module_from_spec(spec); spec.loader.exec_module(ia)

REF_P1 = ['etliditechemadama', 'margeritanonvolearrettarelagu', 'bernationedispagniaetchepiu', 'dinclinationesimosraalconte',
          'palatinocheadaltri', 'arrivocaroneloettrovola', 'resolutionedicostoromiliore', 'diqueloelpapadomandava']   # Norbert #7
REF_P2 = ['seebisognioelgubernatoredibressa', 'andaraisui??eri']                                                      # Thomas #10
def norm(s): return s.replace('v', 'u').replace('j', 'i').replace('que', 'k').replace('rr', 'w')   # k = que, w = rr (neither letter occurs in the 2017 text; the aligner lowercases, so markers must be a-z)
PLAIN = {'p1': norm(''.join(REF_P1)), 'p2': norm(''.join(REF_P2))}

# signs, with their page/line/pos from ciphertext_v6.tsv (the committed transcription); ciphertext_v6.txt is the same token stream
rows = list(csv.DictReader(open(os.path.join(T, 'ciphertext_v6.tsv')), delimiter='\t'))
txt = [l.split() for l in open(os.path.join(T, 'passes', 'ciphertext_v6.txt')).read().splitlines() if l.strip()]
assert [r['sign'] for r in rows] == [s for l in txt for s in l], 'ciphertext_v6.tsv and passes/ciphertext_v6.txt differ'
SIGNS = {'p1': [r for r in rows if r['page'] == 'p1'], 'p2': [r for r in rows if r['page'] == 'p2']}

# key: key.tsv (grades H/M) first, then the atlas key for codes key.tsv omits (value ? there)
KEY = {}
for path in ('key.tsv', os.path.join('keys', 'key_domnina_2016_atlasmap_v6.tsv')):
    for r in csv.DictReader([l for l in open(os.path.join(T, path)) if not l.startswith('#')], delimiter='\t'):
        KEY.setdefault(r['code'], (r['value'].strip(), r['grade']))
def keyval(code):
    v = KEY.get(code, ('?', '-'))[0]
    return {'que': 'k', 'rr': 'w', 'cc': 'x'}.get(v, v)   # same markers as norm(); cc -> x (also absent from the text)

with open(os.path.join(H, 'align_2017_pairs.tsv'), 'w') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
    for p in ('p1', 'p2'):
        w.writerow([p, PLAIN[p], p, ' '.join('@' + r['sign'] for r in SIGNS[p])])
with open(os.path.join(H, 'align_2017_prior.tsv'), 'w') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['code', 'value'])
    for c, (v, g) in KEY.items():
        v2 = {'que': 'k'}.get(v, v)
        if v2.isalpha() and len(v2) == 1: w.writerow([c, v2])   # nulls, ?, rr|cc unseeded: the plain text decides them

def run(plain_by_page):
    pairs = [{'plain_line': p, 'plain_raw': plain_by_page[p], 'cipher_line': p, 'cipher_raw': ' '.join('@' + r['sign'] for r in SIGNS[p])} for p in ('p1', 'p2')]
    prior = ia.load_prior(os.path.join(H, 'align_2017_prior.tsv'), 100, code_mode=True)
    prepared, results, counts, shown = ia.run_align(pairs, floor=100, prior=prior, code_prefix='@', null_cost=0.0, wildcard='?')
    return prepared, results, counts, shown

def classify(prepared, results):
    """per sign: the aligned chunk vs the key value; plus the plain letters no sign took."""
    out, uncovered = [], []
    for (p, raw, toks, letters, starts, ends, _), chunks in zip(prepared, results):
        page = p['plain_line']; covered = [False] * len(letters)
        for r, (kind, code), c in zip(SIGNS[page], toks, chunks):
            chunk = letters[c[0]:c[1]] if c else ''
            if c:
                for k in range(c[0], c[1]): covered[k] = True
            kv = keyval(code)
            if kv == 'null': cls = 'null-empty' if not chunk else 'null-took-letter'
            elif kv == '?': cls = 'unkeyed-empty' if not chunk else 'unkeyed-took-letter'
            elif chunk == '?': cls = 'over-unread-??'
            elif not chunk: cls = 'letter-sign-empty'
            elif chunk == kv: cls = 'agree'
            else: cls = 'conflict'
            out.append([page, r['line'], r['pos'], code, kv, KEY.get(code, ('?', '-'))[1], chunk, cls, c[0] if c else ''])
        for k, ch in enumerate(letters):
            if not covered[k]: uncovered.append([page, k, ch, letters[max(0, k - 4):k] + '[' + ch + ']' + letters[k + 1:k + 5]])
    return out, uncovered

def agree_rate(signs):
    lb = [s for s in signs if s[4] not in ('null', '?')]
    return sum(s[7] == 'agree' for s in lb) / len(lb), len(lb)

prepared, results, counts, shown = run(PLAIN)
signs, uncovered = classify(prepared, results)
with open(os.path.join(H, 'align_2017_signs.tsv'), 'w') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['page', 'line', 'pos', 'code', 'key_value', 'key_grade', 'aligned_2017', 'class', 'plain_index']); w.writerows(signs)
with open(os.path.join(H, 'align_2017_uncovered.tsv'), 'w') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['page', 'plain_index', 'letter', 'context']); w.writerows(uncovered)
rows_tool = ia.token_rows(prepared, results, counts, shown)
with open(os.path.join(H, 'align_2017_align.tsv'), 'w') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['cipher_line', 'k', 'raw', 'kind', 'value', 'repair', 'chunk', 'status']); w.writerows(rows_tool)
with open(os.path.join(H, 'align_2017_key.tsv'), 'w') as f:   # what each code reads in the 2017 text, by count (the tool's value->meaning key)
    w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['code', 'key_value', 'key_grade', 'reads_2017', 'n_aligned'])
    for code in sorted(counts, key=lambda c: -sum(counts[c].values())):
        w.writerow([code, keyval(code), KEY.get(code, ('?', '-'))[1], ' '.join('%s:%d' % kv for kv in counts[code].most_common()), sum(counts[code].values())])

real_rate, n_lb = agree_rate(signs)
rng = random.Random(5); ctrl = []
for _ in range(20):
    sh = {}
    for p, s in PLAIN.items():
        L = list(s); rng.shuffle(L); sh[p] = ''.join(L)
    pr, rs, _, _ = run(sh); ctrl.append(agree_rate(classify(pr, rs)[0])[0])
cls = Counter(s[7] for s in signs)
by_line = defaultdict(Counter)
for s in signs: by_line[(s[0], s[1])][s[7]] += 1
summary = {'signs': len(signs), 'letter_bearing_signs': n_lb, 'agree_rate_real': round(real_rate, 3),
           'control_shuffled_plain_20': {'mean': round(sum(ctrl) / len(ctrl), 3), 'max': round(max(ctrl), 3), 'ge_real': sum(c >= real_rate for c in ctrl)},
           'classes': dict(cls), 'uncovered_plain_letters': len(uncovered), 'plain_len': {p: len(PLAIN[p]) for p in PLAIN},
           'by_line': {'%s %s' % k: dict(v) for k, v in by_line.items()}}
json.dump(summary, open(os.path.join(H, 'align_2017_summary.json'), 'w'), indent=1)
print(json.dumps(summary, indent=1))

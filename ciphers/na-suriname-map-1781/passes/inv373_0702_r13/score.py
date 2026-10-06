#!/usr/bin/env python3
"""R13-SUR702: score the inv. 373 scan 0702 blind cipher pass against the reconciled gloss (PREREG.md, pushed 2fcd61117 first).
Reads passA_sonnet_blind.tsv (cipher rows, blind), gloss_reconciled.tsv, ../../key_period_codes_nieuw.tsv,
../inv373_0693_r10/sign_table.tsv. Writes score.out, align_words.tsv, sign_table.tsv, candidates_0702.tsv. No key edit."""
import os, re, random, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(H, '..', '..')
def rows(p):
    for l in open(p, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        yield l.rstrip('\n').split('\t')
key = {f[0]: f[1] for f in rows(os.path.join(T, 'key_period_codes_nieuw.tsv')) if f[0] != 'code'}
key['[y-fam]'] = 'm|n'  # PREREG: y-family agrees with m or n (0693 sign table); reported separately
st93 = {f[0]: {x.split(':')[0] for x in f[4].split()} for f in rows(os.path.join(H, '..', 'inv373_0693_r10', 'sign_table.tsv')) if f[0] != 'code'}
st93['[y-fam]'] = {'m', 'n'}
ALIAS = {'[ij]': '[y-fam]', 'y': '[y-fam]', 'ÿ': '[y-fam]', '[lambda]': 'λ', '[d-loop]': '[ezh-dot]', '[x-dots]': '[x-dot]'}
EQ = {'j': 'i', 'y': 'i', 'ij': 'i', 'u': 'v'}
def norm(c): return EQ.get(c, c)
def letters(w):
    out, i = [], 0
    while i < len(w):
        if w[i:i+2] == 'ij': out.append('ij'); i += 2
        else: out.append(w[i]); i += 1
    return out
blind = {f[0]: f[2] for f in rows(os.path.join(H, 'passA_sonnet_blind.tsv')) if len(f) > 2 and f[1] == 'cipher'}
gloss = {f[0]: f[1] for f in rows(os.path.join(H, 'gloss_reconciled.tsv')) if f[0] != 'crop'}
TOK = re.compile(r'\[[^\]]+\]|\S')
DROP = {'-', '.', "'", '–', '"', ',', ';', ':'}
def cwords(s):
    # PREREG word groups: split on '|'; within a piece, if the reader wrote multi-sign chunks (left-page style, e.g.
    # '3[y-fam] w7'), each whitespace chunk is a word; if every chunk is one sign (right-page style), the piece is one word.
    s = re.sub(r'\[[^\]]+\]', lambda m: m.group(0).replace(' ', '_').replace(':', '='), s)  # keep [other: ...] codes whole
    s = re.sub(r'-\s*(?:[0-9]\s*)+-', ' | ', s)          # plain numerals between dashes
    s = s.replace(',', ' | ').replace(';', ' | ').replace(':', ' | ')
    out = []
    for piece in s.split('|'):
        chunks = [[x for x in TOK.findall(c) if x not in DROP] for c in piece.split()]
        chunks = [c for c in chunks if c]
        words = chunks if any(len(c) > 1 for c in chunks) else ([sum(chunks, [])] if chunks else [])
        out += [[ALIAS.get(x, x) for x in w] for w in words]
    return out
def gwords(s):
    s = re.sub(r'[0-9]+', ' ', s); s = re.sub(r"[^A-Za-zÀ-ÿ ]", ' ', s)
    return [w.lower() for w in s.split()]
pairs, aw = [], ['crop\tgloss_word\tsigns\tstatus']
for c in sorted(gloss):
    if c not in blind: continue
    cw, gw = cwords(blind[c]), gwords(gloss[c])
    if len(cw) != len(gw):
        aw.append(f'{c}\t{" ".join(gw)}\t{" | ".join(" ".join(t) for t in cw)}\tskip-line ({len(gw)} gloss words, {len(cw)} cipher groups)'); continue
    for g, t in zip(gw, cw):
        L = letters(g)
        if len(L) != len(t): aw.append(f'{c}\t{g}\t{" ".join(t)}\tskip-len ({len(L)} vs {len(t)})'); continue
        aw.append(f'{c}\t{g}\t{" ".join(t)}\taligned')
        pairs += [(s, x, c, g) for s, x in zip(t, L) if s != '?']
def ag(code, x, table):
    if table is key: return any(norm(v) == norm(x) for v in key[code].split('|'))
    return norm(x) in {norm(v) for v in table[code]}
def stat(pp, table, noy=False):
    k = [(s, x) for s, x, *_ in pp if s in table and not (noy and s == '[y-fam]')]
    return (sum(ag(s, x, table) for s, x in k) / len(k) if k else 0.0), len(k)
out = [f'pairs with gloss: {sum(1 for c in gloss if c in blind)}; aligned words: {sum(1 for a in aw if a.endswith("aligned"))}; positions: {len(pairs)}']
for name, table, noy in (('S1 key_period_codes_nieuw', key, False), ('S1 without [y-fam]', key, True), ('S2 0693 sign table', st93, False)):
    real, n = stat(pairs, table, noy); rnd = random.Random(702); xs = [p[1] for p in pairs]; ctl = []
    for _ in range(1000):
        rnd.shuffle(xs); ctl.append(stat([(p[0], x) for p, x in zip(pairs, xs)], table, noy)[0])
    ctl.sort(); p99 = ctl[989]; mean = sum(ctl) / len(ctl)
    gate = ('SAME SYSTEM' if real >= 0.60 and real > p99 else 'not shown') if name == 'S1 key_period_codes_nieuw' else 'descriptive'
    out.append(f'{name}: keyed {n}, agree {real:.3f}; shuffled-gloss control mean {mean:.3f} p99 {p99:.3f} -> {gate}')
tab = collections.defaultdict(collections.Counter)
for s, x, *_ in pairs: tab[s][norm(x)] += 1
sr = ['code\tnieuw_value\tletters_seen\tagree\tconflict\tverdict']; cand = ['code\tsuggested\tcount\tnieuw_value\tnote']
for s in sorted(tab):
    seen = tab[s]; nv = key.get(s, ''); tot = sum(seen.values())
    a = sum(n for x, n in seen.items() if nv and any(norm(v) == x for v in nv.split('|')))
    conf = tot - a if nv else 0
    v = 'unkeyed' if not nv else 'agree' if conf == 0 else 'conflict' if a == 0 else 'mixed'
    sr.append(f"{s}\t{nv}\t{' '.join(f'{x}:{n}' for x, n in seen.most_common())}\t{a}\t{conf}\t{v}")
    if v != 'agree': cand.append(f"{s}\t{seen.most_common(1)[0][0]}\t{seen.most_common(1)[0][1]}\t{nv}\t{v}; all: " + ' '.join(f'{x}:{n}' for x, n in seen.most_common()))
open(os.path.join(H, 'align_words.tsv'), 'w').write('\n'.join(aw) + '\n')
open(os.path.join(H, 'sign_table.tsv'), 'w').write('\n'.join(sr) + '\n')
open(os.path.join(H, 'candidates_0702.tsv'), 'w').write('# from the 0702 gloss pair (blind tokens), for a verifier; NOT applied to any key\n' + '\n'.join(cand) + '\n')
open(os.path.join(H, 'score.out'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))

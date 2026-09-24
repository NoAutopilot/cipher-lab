#!/usr/bin/env python3
"""Settle recon disagreements for the Blathwayt 1725-29 run without images where the key decides (R17, 24 Sept 2026).

  python3 settle.py            write ciphertext.tsv and settle_log.tsv from passA.tsv + passB.tsv
  python3 settle.py --check    exit 1 if the committed ciphertext.tsv / settle_log.tsv are stale

Alignment: per line, pass B aligned to pass A by Needleman-Wunsch over groups (as tools/reconcile_passes.py), with
one repair: pass A split BLA188_p3 line 9 in two (A L09 = one group, A L10 = the rest), so every later A line on that
page is one number ahead of B. A L09+L10 are joined and A L11-L19 renumbered L10-L18 before aligning (checked by eye
on both passes' group sequences: A L11 '? 665 576 1200 1020 660 899 831 1143' = B L10 '282 665 576 1200 ...').

Rule 'key-consistent': at a column where A and B read different groups, take the gloss written over that column (either
pass, normalised). If that gloss is attested for A's group elsewhere in the run (columns where both passes agree on the
group) and not for B's, take A; the converse takes B. Same test settles 'agree-flagged' columns to H when the gloss
there matches the group's gloss elsewhere. Rows 'image' are settled from a crop (settle_image.tsv, by eye, R17).
Everything else stays M with the alternative kept.
"""
import csv, sys, unicodedata, re, collections, io, os

HERE = os.path.dirname(os.path.abspath(__file__))


def load(path):
    out = collections.OrderedDict()
    for r in csv.DictReader(open(os.path.join(HERE, path)), delimiter='\t'):
        g = (r.get('group') or '').strip().rstrip('?')
        if g == '':
            g = '?'
        out.setdefault(r['line'], []).append((g, (r.get('conf') or '').strip(), (r.get('gloss') or '').strip()))
    return out


def fix_a(a):
    """Pass A BLA188_p3: join L09+L10, renumber L11.. down by one."""
    new = collections.OrderedDict()
    for line, toks in a.items():
        m = re.match(r'BLA188_p3_L(\d\d)$', line)
        if m and int(m.group(1)) >= 10:
            n = int(m.group(1)) - 1
            key = 'BLA188_p3_L%02d' % n
            if n == 9:
                new[key] = new.get(key, []) + toks
                continue
            new[key] = toks
        else:
            new[line] = toks
    return new


def norm(gl):
    if gl is None:
        return ''
    s = unicodedata.normalize('NFD', gl.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.replace('’', "'")
    if s in ('none', 'struck', '?', '') or s.startswith('struck'):
        return ''
    if '...' in s or '..' in s:
        return ''
    s = re.sub(r"[^a-z0-9']", '', s)
    return s


def align(A, B):
    n, m = len(A), len(B)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0] = -i
    for j in range(1, m + 1):
        S[0][j] = -j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = max(S[i - 1][j - 1] + (1 if A[i - 1][0] == B[j - 1][0] else -1), S[i - 1][j] - 1, S[i][j - 1] - 1)
    i, j, cols = n, m, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and S[i][j] == S[i - 1][j - 1] + (1 if A[i - 1][0] == B[j - 1][0] else -1):
            cols.append((A[i - 1], B[j - 1])); i -= 1; j -= 1
        elif i > 0 and S[i][j] == S[i - 1][j] - 1:
            cols.append((A[i - 1], None)); i -= 1
        else:
            cols.append((None, B[j - 1])); j -= 1
    return cols[::-1]


def build():
    a = fix_a(load('passA.tsv'))
    b = load('passB.tsv')
    lines = list(a) + [l for l in b if l not in a]
    table = {l: align(a.get(l, []), b.get(l, [])) for l in lines}
    # gloss evidence: columns where both passes agree on the group
    ev = collections.defaultdict(collections.Counter)
    for l, cols in table.items():
        for k, (x, y) in enumerate(cols):
            if x and y and x[0] == y[0] and x[0] != '?':
                for t in (x, y):
                    g = norm(t[2])
                    if g:
                        ev[x[0]][g] += 1
    img = {}
    p = os.path.join(HERE, 'settle_image.tsv')
    if os.path.exists(p):
        for r in csv.DictReader(open(p), delimiter='\t'):
            img[(r['line'], int(r['pos']))] = (r['group'], r['conf'], r['note'])
    ct, log = [], []
    for l, cols in table.items():
        for k, (x, y) in enumerate(cols, 1):
            ga = x[0] if x else '-'
            gb = y[0] if y else '-'
            flag = (x and x[1] != 'H') or (y and y[1] != 'H')
            glosses = [norm(t[2]) for t in (x, y) if t and norm(t[2])]
            gl = collections.Counter(glosses).most_common(1)[0][0] if glosses else ''
            rule, conf, sign, alt = '', 'H', ga, ''
            if ga == gb and ga != '?':
                if not flag:
                    rule = 'agree'
                else:
                    own = ev[ga].copy(); own[gl] -= 2 if gl else 0
                    if gl and own[gl] > 0:
                        rule = 'agree-flagged,key-consistent'
                    elif not gl and ga in ('1240', '1243', '1250', '1324'):
                        rule = 'agree-flagged,no-gloss'; conf = 'M'
                    else:
                        rule = 'agree-flagged'; conf = 'M'
            else:
                cand = [g for g in (ga, gb) if g not in ('-', '?')]
                ok = [g for g in cand if gl and ev[g][gl] > 0]
                if len(cand) == 2 and len(ok) == 1:
                    sign = ok[0]; alt = (gb if sign == ga else ga); rule = 'key-consistent'
                elif len(cand) == 1 and ga != gb and ('-' in (ga, gb)):
                    sign = cand[0]; conf = 'M'; rule = 'gap'; alt = 'A:-' if ga == '-' else 'B:-'
                else:
                    sign = ga if ga not in ('-', '?') else gb; alt = 'B:' + gb if sign == ga else 'A:' + ga
                    conf = 'M'; rule = 'undecided'
                log.append((l, k, ga, gb, gl, ';'.join('%s:%s' % (g, ev[g].most_common(2)) for g in cand), rule, sign))
            if (l, k) in img:
                s2, c2, note = img[(l, k)]
                sign, conf, rule = s2, c2, 'image:' + note
                log.append((l, k, ga, gb, gl, '', 'image', sign))
            ct.append((l, k, sign, conf, alt, rule, gl))
    return ct, log, ev


def dump(ct, log):
    f1 = io.StringIO(); w = csv.writer(f1, delimiter='\t', lineterminator='\n')
    w.writerow(['line', 'pos', 'group', 'conf', 'alt', 'rule', 'gloss'])
    w.writerows(ct)
    f2 = io.StringIO(); w = csv.writer(f2, delimiter='\t', lineterminator='\n')
    w.writerow(['line', 'pos', 'A', 'B', 'gloss_here', 'gloss_elsewhere', 'rule', 'taken'])
    w.writerows(log)
    return f1.getvalue(), f2.getvalue()


if __name__ == '__main__':
    ct, log, ev = build()
    s1, s2 = dump(ct, log)
    if '--check' in sys.argv:
        bad = [f for f, s in (('ciphertext.tsv', s1), ('settle_log.tsv', s2))
               if not os.path.exists(os.path.join(HERE, f)) or open(os.path.join(HERE, f)).read() != s]
        if bad:
            print('stale:', bad); sys.exit(1)
        print('ok'); sys.exit(0)
    open(os.path.join(HERE, 'ciphertext.tsv'), 'w').write(s1)
    open(os.path.join(HERE, 'settle_log.tsv'), 'w').write(s2)
    c = collections.Counter(r[5].split(',')[-1] if not r[5].startswith('image') else 'image' for r in ct)
    print(len(ct), 'columns;', dict(c), '; conf', dict(collections.Counter(r[3] for r in ct)))

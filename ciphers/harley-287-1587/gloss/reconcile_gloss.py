#!/usr/bin/env python3
"""A2-HAR7 (3 Oct 2026): reconcile passA.tsv and passB.tsv (blind Sonnet passes) into gloss_pairs.tsv.

Cipher: token alignment (difflib) per row. Agreed tokens kept; the systematic l/p split on the looped crossed-stem sign
(the sign under gloss "h", distinct from the phi = l in the cipher line above it on f84r L07; checked by eye on f84r L03_s1
and L07_s1) -> p; every other disagreement -> ? (the aligner's wildcard, never counted as evidence).
Gloss: GLOSS below, settled by the worker from the crops and the cipher word lengths where the passes differ (see notes).
    python3 reconcile_gloss.py [--check]
"""
import csv, difflib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
GLOSS = {  # rows where the passes' gloss differs; worker's settlement (? = letter not settled)
 'L01': 'thes answeres brought vs by norice after three',
 'L02': 'pla?es attendaunce ?be shewe smal hope of any good',
 'L03': 'successe in the great cause therefore seinge we',
 'L05': 'that we pretending ? to vs went eyther to dower or',
 'L06': 'to calays and there to pres? them resolutely',
 'L07': 'whether they wil condescend to the three poyntes',
 'L08': 'propounded which being refused neer ma?',
 'L09': 'may ?oyhe honor break of and we regre home',
 'L11': 'wether they wil yeald a proofe of the sufficiency',
 'L12': 'of the dukes commission as i desiren',
 'L14': 'treaty and twenty ? after and yeald vs',
 'L15': 'honorable security for our persons',
 'R01': 'growen a dislyke',
 'R03': 'betwen the gouernor and captayns',
 'R04': 'no dyuyne seruyce',
 'R05': 'growe insolent',
 'R06': 'twelu moneth nor disciplyne',
 'R09': 'come hether to reforme',
}


def merge(a, b):
    a, b = a.split(), b.split()
    out, n_agree, n_lp, n_q = [], 0, 0, 0
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal':
            out += a[i1:i2]; n_agree += sum(t != '/' for t in a[i1:i2])
        elif op == 'replace' and i2 - i1 == j2 - j1:
            for x, y in zip(a[i1:i2], b[j1:j2]):
                if {x, y} == {'l', 'p'}:
                    out.append('p'); n_lp += 1
                elif '/' in (x, y):
                    out.append('/' if x == '/' else x)
                else:
                    out.append('?'); n_q += 1
        else:  # unequal length or insert/delete: keep A's word breaks, wildcard its signs
            seg = a[i1:i2]
            out += ['/' if t == '/' else '?' for t in seg]; n_q += sum(t != '/' for t in seg)
    s = ' '.join(out)
    while ' / /' in s:
        s = s.replace(' / /', ' /')
    return s.strip(' /'), n_agree, n_lp, n_q


def build():
    A = list(csv.DictReader(open(os.path.join(HERE, 'passA.tsv'), encoding='utf-8'), delimiter='\t'))
    B = {(r['page'], r['band'], r['pair']): r for r in csv.DictReader(open(os.path.join(HERE, 'passB.tsv'), encoding='utf-8'), delimiter='\t')}
    lines = ['page\tband\tpair\tgloss\tcipher\tnotes']
    tot = [0, 0, 0]
    for a in A:
        b = B[(a['page'], a['band'], a['pair'])]
        c, n1, n2, n3 = merge(a['cipher'], b['cipher'])
        tot[0] += n1; tot[1] += n2; tot[2] += n3
        g = GLOSS.get(a['band'], a['gloss'] if a['gloss'] == b['gloss'] else None)
        assert g is not None, a['band']
        note = 'signs: %d agreed, %d l/p->p, %d ?' % (n1, n2, n3)
        if a['band'] == 'R18':
            note += '; cipher row cut at bottom edge'
        lines.append('\t'.join([a['page'], a['band'], a['pair'], g, c, note]))
    return '\n'.join(lines) + '\n', tot


if __name__ == '__main__':
    text, tot = build()
    p = os.path.join(HERE, 'gloss_pairs.tsv')
    if '--check' in sys.argv:
        ok = open(p, encoding='utf-8').read() == text
        print('check ok' if ok else 'stale'); sys.exit(0 if ok else 1)
    open(p, 'w', encoding='utf-8').write(text)
    print('agreed %d, l/p->p %d, wildcarded %d' % tuple(tot))

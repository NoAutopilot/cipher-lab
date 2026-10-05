#!/usr/bin/env python3
"""D2B-THURP3 (5 Oct 2026): every distinct code in P3's postscript (djvu 48000-48004, John
Butler), at every grade, intersected with pool_1654/key_stamford.tsv (the P5+P6/P7 printed
decipherments of W. Stamford, Calais, March 1655), with Stamford's own support (votes/total).
Applies the rule pre-registered in NOTES.md "D2B-THURP3" before this script was run: a
compatibility gate on shared H/C-graded codes, then regrade only if the gate passes.
Extends tx/check_p3_postscript_crosskeys.py (M values only). Never edits key_butler.tsv or
reading_P3.txt. Writes tx/p3_postscript_stamford_all.tsv.

Usage: python3 tx/p3_postscript_stamford_all.py [--check]
"""
import csv, io, os, sys
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)
READING = os.path.join(TARGET, 'reading_P3.txt')
STAMFORD = os.path.join(TARGET, 'pool_1654', 'key_stamford.tsv')
OUT = os.path.join(HERE, 'p3_postscript_stamford_all.tsv')


def postscript_tokens():
    rows = []
    with open(READING) as f:
        for line in f:
            p = line.rstrip('\n').split('\t')
            if len(p) >= 4 and p[0].startswith('L4800'):
                code = p[1].strip('.,;:')
                rows.append((code, p[2], p[3]))
    return rows


def stamford():
    k = {}
    with open(STAMFORD) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            k[r['value']] = (r['meaning'], int(r['votes']), int(r['total']), float(r['share']), r['grade'])
    return k


def build():
    toks = postscript_tokens()
    sk = stamford()
    occ = Counter(c for c, _, _ in toks)
    codes = OrderedDict()
    for c, g, m in toks:
        codes.setdefault(c, (g, m))
    out = io.StringIO()
    w = csv.writer(out, delimiter='\t', lineterminator='\n')
    w.writerow(['code', 'p3_ps_occurrences', 'butler_grade', 'butler_meaning', 'stamford_meaning',
                'stamford_votes', 'stamford_total', 'stamford_share', 'stamford_grade', 'relation'])
    hc_shared = hc_agree = 0
    shared = 0
    for c, (g, m) in codes.items():
        if c in sk:
            sm, v, t, s, sg = sk[c]
            shared += 1
            rel = ('agree' if sm == m else 'conflict') if m else 'butler_unread'
            if g in ('H', 'C'):
                hc_shared += 1
                hc_agree += rel == 'agree'
            w.writerow([c, occ[c], g, m, sm, v, t, f'{s:.2f}', sg, rel])
        else:
            w.writerow([c, occ[c], g, m, '', '', '', '', '', 'absent'])
    gate = hc_shared >= 3 and hc_agree * 3 >= hc_shared * 2
    summary = (f'postscript tokens {len(toks)}, distinct codes {len(codes)}, shared with key_stamford {shared}; '
               f'H/C-graded shared {hc_shared}, agreeing {hc_agree}; gate {"PASS" if gate else "FAIL"}; '
               f'tokens regraded {0 if not gate else "see rule 2"}')
    out.write('# ' + summary + '\n')
    return out.getvalue(), summary


def main():
    text, summary = build()
    if '--check' in sys.argv:
        with open(OUT) as f:
            if f.read() != text:
                print('STALE: tx/p3_postscript_stamford_all.tsv differs from a fresh run'); sys.exit(1)
        print('OK: matches a fresh run; ' + summary); return
    with open(OUT, 'w') as f:
        f.write(text)
    print(summary)


if __name__ == '__main__':
    main()

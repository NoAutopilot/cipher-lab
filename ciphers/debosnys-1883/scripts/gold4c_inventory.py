#!/usr/bin/env python3
"""GOLD-4C (25 Sept 2026): rebuild pass A for all four cryptograms from glyphs/box_labels.tsv (the by-eye
per-box inventory), classify GOLD-4A's cryptogram-4 disagreement columns against it, and recompute N/K/IC
per cryptogram with scripts/compute_ic.py's own controls (fr16, en16_repo, uniform random at the same K).

Run from ciphers/debosnys-1883:  python3 scripts/gold4c_inventory.py [--check]
Writes passA.tsv, ciphertext_draft.tsv, disagreements_classes.tsv, glyphs/ic_inventory.txt.
--check: regenerate to memory and exit 1 if any committed file differs (rule 7)."""
import csv, sys, os, io, collections, argparse
sys.path.insert(0, os.path.dirname(__file__))
from compute_ic import ic, load_text_letters, random_string, find_corpus_file

OLD_IDS = None  # filled from merge.tsv: the 68-id inventory GOLD-4A's two passes used
NOISE = ('_', 'MULTI')


def read(p):
    return list(csv.DictReader(open(p), delimiter='\t'))


def passA(bl):
    out = io.StringIO()
    out.write('line\tposition\tsign\tfamily\tconfidence\tsource\n')
    for b in bl:
        out.write(f"{b['page']}_L{int(b['line']):02d}\t{b['pos']}\t{b['sign']}\t{b['family']}\t{b['confidence']}\t{b['source']}\n")
    return out.getvalue()


def draft(bl):
    out = io.StringIO()
    out.write('line\tposition\tsign\tfamily\tconfidence\tnote\n')
    for b in bl:
        note = 'single pass A (box_labels.tsv); blind pass B on this inventory pending'
        out.write(f"{b['page']}_L{int(b['line']):02d}\t{b['pos']}\t{b['sign']}\t{b['family']}\t{b['confidence']}\t{note}\n")
    return out.getvalue()


def classes(bl, old_ids):
    """One row per GOLD-4A disagreement column on cryptogram 4 (ciphertext_draft rows with why != agree-flagged,
    as committed by GOLD-4A in glyphs/c4_draft_gold4a.tsv), with its class under the new inventory."""
    lab = {(b['page'], int(b['line']), int(b['pos'])): b for b in bl}
    rows = read('glyphs/c4_draft_gold4a.tsv')
    out = io.StringIO()
    out.write('line\tcol\tA\tB\tnew_sign\tnew_conf\tclass\treason\n')
    counts = collections.Counter()
    apos = collections.Counter()
    for r in rows:
        line = r['line']; page, ln = line.split('_L'); ln = int(ln)
        a_gap = r['alt'].startswith('A:-')
        if not a_gap:
            apos[line] += 1
        if r['why'] == 'agree-flagged':
            continue
        if r['why'] == 'gap':
            A = '-' if a_gap else r['sign']; B = r['sign'] if a_gap else '-'
            new = lab.get((page, ln, apos[line])) if not a_gap else None
            ns, nc = (new['sign'], new['confidence']) if new else ('-', '-')
            cls, why = 'segmentation', 'one pass has a box the other lacks'
        else:
            A = r['sign']; B = r['alt'][2:]
            new = lab[(page, ln, apos[line])]; ns, nc = new['sign'], new['confidence']
            if ns in NOISE:
                cls, why = 'segmentation', 'box is several signs merged (MULTI) or noise (_)'
            elif A.startswith('MISC') or B.startswith('MISC') or A == '_' or B == '_':
                cls, why = 'inventory', 'one id for several shapes (a MISC bucket or the kNN noise class)'
            elif ns not in old_ids:
                cls, why = 'inventory', 'the shape had no id of its own in the 68-id inventory (both old ids were impure)'
            elif ns == A or ns == B:
                cls, why = 'reading', 'both ids exist and are distinct in the new inventory; one pass misread'
            else:
                cls, why = 'reading', 'both passes gave an id other than the one read here'
        counts[cls] += 1
        out.write(f'{line}\t{r["position"]}\t{A}\t{B}\t{ns}\t{nc}\t{cls}\t{why}\n')
    return out.getvalue(), counts


def ic_table(bl, trials=20):
    fr = find_corpus_file('../../tools/data/fr16'); en = find_corpus_file('../../tools/data/en16_repo')
    groups = {'c1': ['c1'], 'c2 (2a+2b)': ['c2a', 'c2b'], 'c3': ['c3'], 'c4 (4a+4b)': ['c4a', 'c4b'],
              'combined (all)': ['c1', 'c2a', 'c2b', 'c3', 'c4a', 'c4b']}
    out = io.StringIO()
    out.write('GOLD-4C inventory (box_labels.tsv), 25 Sept 2026. Controls: compute_ic.py, fr16 / en16_repo text at the\n'
              'same N (20 trials), uniform random string at the same N and K (20 trials). "excl" drops _ and MULTI boxes.\n')
    for col, name in (('sign', 'sign ids'), ('family', 'families (PCT-SLASH->PCT, BAR-SOLID->BLOB)')):
        for excl in (False, True):
            out.write(f'\n== {name}, {"excluding" if excl else "including"} _/MULTI ==\n')
            out.write(f"{'group':<18}{'N':>6}{'K':>5}{'IC_target':>11}{'IC_fr':>9}{'IC_en':>9}{'IC_uniform':>12}\n")
            for g, pages in groups.items():
                seq = [b[col] for b in bl if b['page'] in pages and not (excl and b[col] in NOISE)]
                n, k = len(seq), len(set(seq))
                f = [ic(load_text_letters(fr, n, 1000 + t)) for t in range(trials)]
                e = [ic(load_text_letters(en, n, 2000 + t)) for t in range(trials)]
                u = [ic(random_string(n, k, 3000 + t)) for t in range(trials)]
                out.write(f'{g:<18}{n:>6}{k:>5}{ic(seq):>11.4f}{sum(f)/trials:>9.4f}{sum(e)/trials:>9.4f}{sum(u)/trials:>12.4f}\n')
    return out.getvalue()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--check', action='store_true'); a = ap.parse_args()
    bl = read('glyphs/box_labels.tsv')
    bl.sort(key=lambda b: (b['page'], int(b['line']), int(b['pos'])))
    old_ids = {r['sign_id'] for r in read('glyphs/merge.tsv') if r['kind'] == 'sign'} | {r['sign_id'].split(': ')[0] for r in []}
    old_ids |= {'MISC-%02d' % int(r['cluster']) for r in read('glyphs/merge.tsv') if r['sign_id'] == 'PER-BOX'}
    old_ids |= {'SUN'}
    cls_txt, counts = classes(bl, old_ids)
    files = {'passA.tsv': passA(bl), 'ciphertext_draft.tsv': draft(bl), 'disagreements_classes.tsv': cls_txt,
             'glyphs/ic_inventory.txt': ic_table(bl)}
    stale = [p for p, t in files.items() if not os.path.exists(p) or open(p).read() != t]
    if a.check:
        print('stale: ' + ', '.join(stale) if stale else 'ok: committed files match box_labels.tsv')
        sys.exit(1 if stale else 0)
    for p, t in files.items():
        open(p, 'w').write(t)
    print('disagreement classes on c4:', dict(counts), 'of', sum(counts.values()))
    print(files['glyphs/ic_inventory.txt'])


if __name__ == '__main__':
    main()

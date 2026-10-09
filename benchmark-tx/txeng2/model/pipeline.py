#!/usr/bin/env python3
"""TXE2-MODEL (PREREG-txeng2-5 X21): run the folder pipeline (two blind passes -> value-blind reconcile -> third-reader
adjudication sheet -> apply) once per reader arm on the SAME crops, so the only difference between arms is the reader model.

Pipeline = the Ceppo/Birago folder protocol, unchanged: ciphers/ceppo-nevers-fr3251-1570s/harvest/reconcile_blind.py (aligns
A and B, agree / split / gap rules by the readers' own conf) and adjudication_sheet.py's sheet (four merged neighbours each
side, both candidates, both notes); the third reader (Sonnet, same prompt for both arms) answers adjudicate_out.tsv
(passage pos sign_id conf note); reconcile_blind.py --adjudicated applies it. Nothing here opens a truth file.

    python3 pipeline.py prep  ITEM ARM     # writes work/ITEM_ARM/{A,B}.tsv, passC*.tsv, adjudicate_in.tsv; outputs reader passes
    python3 pipeline.py final ITEM ARM     # needs work/ITEM_ARM/adjudicate_out.tsv; writes outputs/ITEM/passX21_ARM_pipeline.tsv

Declared rules (written before any score):
- Passage ids are joined to the physical line before reconciling (L03.1, L03.2 -> L03, in order), as convert87.py does.
- dint-f128-print passes carry no per-sign conf (pass_instructions.md format): every sign gets conf H, so every split and
  every one-reader sign goes to the adjudicator (none is dropped silently); rows CLEAR:... and '-' dropped (convert.py rule).
- Unsettled '?' rows left after adjudication stay '?' in the output (scored as read).
- birago1572-no87 (dev_tune): today's pipeline L carries NO87-LABELS relabels (7 value-blind tile rulings T50 -> X_CE,
  exceptions_f178v.tsv). The same rulings are transferred to each arm read-free: each arm line is aligned to the committed
  passC line (the sequence the rulings were made on) by the same aligner, and an arm sign aligned to a ruled position that
  reads T50 becomes X_CE. Both the transferred (primary) and raw outputs are written.
"""
import csv, os, subprocess, sys
from collections import OrderedDict, defaultdict

R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
CEP = os.path.join(R, 'ciphers/ceppo-nevers-fr3251-1570s/harvest')
BIR = os.path.join(R, 'ciphers/nevers-birago-fr3251-1572/harvest')
DIN = os.path.join(R, 'ciphers/fr3621-dinteville-1592/f128')
sys.path.insert(0, CEP)
from reconcile_blind import align  # noqa: E402

DEV = ['L%02d' % i for i in range(1, 13)]
ITEMS = {
    'birago1572-no87': dict(fmt='pass', prefix='f178v_', lines=DEV, readers={
        'sonnet': ([BIR + '/f178v/passA.tsv', BIR + '/f178v/passA_L11-23.tsv'],
                   [BIR + '/f178v/passB.tsv', BIR + '/f178v/passB_L11-23.tsv']),
        'opus': ([HERE + '/reads/d87_r1_a.tsv', HERE + '/reads/d87_r1_b.tsv'],
                 [HERE + '/reads/d87_r2_a.tsv', HERE + '/reads/d87_r2_b.tsv'])}),
    'dint-f128-print': dict(fmt='dint', prefix='f128_', lines=None, readers={
        'sonnet': ([DIN + '/passA.tsv'], [DIN + '/passB.tsv']),
        'opus': ([R + '/benchmark-tx/txeng2/cost/reads/armB_page.tsv'], [R + '/benchmark-tx/txeng2/cost2/reads/dint_b2.tsv'])}),
    'ceppo-f87-S': dict(fmt='pass', prefix='f87_', lines=None, readers={
        'sonnet': ([CEP + '/f87/passA.tsv'], [CEP + '/f87/passB.tsv']),
        'opus': ([R + '/benchmark-tx/txeng2/cost2/reads/c87_a_L0%d.tsv' % i for i in range(1, 6)],
                 [HERE + '/reads/c87_r2.tsv'])}),
}
NAMES = {'sonnet': ('A', 'B'), 'opus': ('r1', 'r2')}


def rows(fn):
    with open(fn, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#') and l.strip()), delimiter='\t'))


def load_reader(files, fmt, lines):
    """-> OrderedDict line -> [(sign, conf, alt, note)] in reading order."""
    out = OrderedDict()
    if fmt == 'dint':
        for fn in files:
            for r in rows(fn):
                if (r.get('gloss') or '').startswith('CLEAR:'):
                    continue
                toks = []
                for x in (r.get('signs') or '').split():
                    if toks and toks[-1].startswith('NEW:') and (x.startswith('(') or toks[-1].count('(') > toks[-1].count(')')):
                        toks[-1] += ' ' + x
                    else:
                        toks.append(x)
                out.setdefault(r['line'].strip(), []).extend((t, 'H', '', '') for t in toks if t != '-')
        return OrderedDict(sorted(out.items()))
    runs = defaultdict(list)
    for fn in files:
        for r in rows(fn):
            ln, _, run = r['passage'].strip().partition('.')
            if lines and ln not in lines:
                continue
            runs[(ln, int(run or 0))].append((int(r['pos']), ((r.get('sign_id') or '').strip(), (r.get('conf') or 'M').strip() or 'M',
                                                               (r.get('alt') or '').strip(), (r.get('note') or '').strip())))
    for (ln, run) in sorted(runs):
        out.setdefault(ln, []).extend(x for _, x in sorted(runs[(ln, run)]))
    return out


def write_pass(P, fn):
    with open(fn, 'w') as f:
        f.write('passage\tpos\tsign_id\talt\tconf\tnote\n')
        for ln, seq in P.items():
            for i, (s, c, a, n) in enumerate(seq, 1):
                f.write('%s\t%d\t%s\t%s\t%s\t%s\n' % (ln, i, s, a, c, n.replace('\t', ' ')))


def write_bench(seqs, prefix, fn, label):
    with open(fn, 'w') as f:
        f.write('# TXE2-MODEL X21 %s\nline\tpos\tsign\n' % label)
        for ln, seq in seqs.items():
            for i, s in enumerate(seq, 1):
                f.write('%s%s\t%d\t%s\n' % (prefix, ln, i, s))


def merged(fn):
    out = OrderedDict()
    for r in rows(fn):
        out.setdefault(r['passage'], []).append(r['sign_id'])
    return out


def no87_transfer(seqs):
    """NO87-LABELS: positions where L (labels_dev_tune) reads X_CE and passC reads T50 -> transfer by alignment to passC."""
    C = merged(BIR + '/f178v/passC.tsv'); C.update(merged(BIR + '/f178v/passC_L11-23.tsv'))
    L = defaultdict(list)
    for r in rows(R + '/benchmark-tx/txeng/units/labels_dev_tune.tsv'):
        L[r['line'].replace('f178v_', '')].append(r['sign'])
    out, n = OrderedDict(), 0
    for ln, seq in seqs.items():
        ruled = {i for i, (c, l) in enumerate(zip(C.get(ln, []), L.get(ln, []))) if c == 'T50' and l == 'X_CE'}
        new = list(seq)
        if ruled:
            for ia, ib in align([(s,) for s in seq], [(s,) for s in C[ln]]):
                if ia is not None and ib in ruled and new[ia] == 'T50':
                    new[ia] = 'X_CE'; n += 1
        out[ln] = new
    return out, n


def main():
    cmd, item, arm = sys.argv[1:4]
    it = ITEMS[item]; w = os.path.join(HERE, 'work', item + '_' + arm); os.makedirs(w, exist_ok=True)
    od = os.path.join(R, 'benchmark-tx/outputs', item)
    fa, fb = it['readers'][arm]
    A, B = load_reader(fa, it['fmt'], it['lines']), load_reader(fb, it['fmt'], it['lines'])
    rc = [sys.executable, os.path.join(CEP, 'reconcile_blind.py'), w + '/A.tsv', w + '/B.tsv', '--out', w + '/passC']
    if cmd == 'prep':
        write_pass(A, w + '/A.tsv'); write_pass(B, w + '/B.tsv')
        for P, nm in zip((A, B), NAMES[arm]):
            write_bench(OrderedDict((k, [x[0] for x in v]) for k, v in P.items()), it['prefix'],
                        os.path.join(od, 'passX21_%s_%s.tsv' % (arm, nm)), '%s reader %s (blind, crops + brief only)' % (arm, nm))
        print(subprocess.run(rc, capture_output=True, text=True, check=True).stdout.strip())
        write_bench(merged(w + '/passC.tsv'), it['prefix'], os.path.join(od, 'passX21_%s_reconcile.tsv' % arm),
                    '%s reconcile before adjudication (? = unsettled)' % arm)
        sheet = subprocess.run([sys.executable, os.path.join(CEP, 'adjudication_sheet.py'), w + '/passC'],
                               capture_output=True, text=True, check=True).stdout
        open(w + '/adjudicate_in.tsv', 'w').write(sheet)
        print('adjudicate_in rows', sheet.count('\n') - 1, 'lines', sorted({l.split('\t')[0] for l in sheet.splitlines()[1:]}))
    elif cmd == 'final':
        print(subprocess.run(rc + ['--adjudicated', w + '/adjudicate_out.tsv'], capture_output=True, text=True, check=True).stdout.strip())
        seqs = merged(w + '/passC.tsv')
        if item == 'birago1572-no87':
            write_bench(seqs, it['prefix'], os.path.join(od, 'passX21_%s_pipeline_raw.tsv' % arm), '%s pipeline, no relabel transfer' % arm)
            seqs, n = no87_transfer(seqs); print('NO87-LABELS transferred', n)
        write_bench(seqs, it['prefix'], os.path.join(od, 'passX21_%s_pipeline.tsv' % arm), '%s pipeline (reconcile + Sonnet adjudication)' % arm)
        print('pipeline signs', sum(len(v) for v in seqs.values()), 'unsettled ?', sum(v.count('?') for v in seqs.values()))


if __name__ == '__main__':
    main()

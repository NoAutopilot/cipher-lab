#!/usr/bin/env python3
"""Build the Ceppo-Nevers key-family items for BENCHMARK-TX.tsv (TX-BENCH, 3 Oct 2026).

ceppo-f36v-gloss: Birago 1571 no.24, BnF fr.3252 f.36v line 1 (v36top_L01 pos 1-18), truth = the clerk's interlinear gloss
  letter above each sign (HARVEST-D eye read, ciphers/ceppo-nevers-fr3251-1570s/harvest/witness_f36/alignment_pairs.tsv,
  "parlandone il signor"), forced through the printed Ceppo-Nevers key (harvest/key_f11.tsv + key_extra.tsv, X_THETA2 = r).
  Independent of the reader passes. Positions whose gloss letter is read at conf L are excluded.
ceppo-f21v-S, ceppo-f87-S: BnF fr.3251 f.21v and f.87, the S-graded tokens of the committed decode
  (harvest/reading_f21v_tokens.tsv, reading_f87_tokens.tsv), the plain value forced through the same key. NOT independent
  of the committed transcription (an S token is the committed sign decoded): the committed/reconciled output scores 0 by
  construction and is not scored; the item measures the single blind passes A and B against the accepted reading. M, I, U
  tokens are excluded and counted.
A plain value forces the SET of signs of that value (homophones): a homophone swap is invisible (value-level err_true).
Run from the repo root: python3 benchmark-tx/build_ceppo.py
"""
import csv, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(ROOT, 'ciphers/ceppo-nevers-fr3251-1570s/harvest')
B = os.path.join(ROOT, 'ciphers/birago-fr3252-1571-72/harvest/f36')
OUT = os.path.join(ROOT, 'benchmark-tx')


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def keymap():
    by_val = {}
    for p in ('key_f11.tsv', 'key_extra.tsv'):
        for r in rd(os.path.join(C, p)):
            by_val.setdefault(r['value'], set()).add(r['sign'])
    return by_val


def write_truth(name, header, rows):
    with open(os.path.join(OUT, name + '.truth.tsv'), 'w') as f:
        f.write('# ' + header + '; built by benchmark-tx/build_ceppo.py\nline\tpos\tref_sign\ttruth\tplain\tstatus\n')
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    sc = sum(1 for r in rows if r[5] == 'scored')
    print('%s: %d positions, %d scored, %d excluded' % (name, len(rows), sc, len(rows) - sc))


def norm(name, files, prefix=None):
    od = os.path.join(OUT, 'outputs', name)
    os.makedirs(od, exist_ok=True)
    return od


def write_out(od, fname, files, prefix=None, only_lines=None):
    out = []
    for p in files:
        for r in rd(p):
            ln = r.get('line') or r.get('passage')
            if prefix and '_' not in ln:
                ln = prefix + '_' + ln
            if only_lines and ln not in only_lines:
                continue
            out.append((ln, r.get('pos'), r.get('sign') or r.get('sign_id')))
    with open(os.path.join(od, fname + '.tsv'), 'w') as f:
        f.write('line\tpos\tsign\n')
        for o in out:
            f.write('\t'.join(o) + '\n')


def main():
    by_val = keymap()
    # f.36v line 1 vs the period gloss
    pairs = [r for r in rd(os.path.join(C, 'witness_f36/alignment_pairs.tsv')) if r['crop'].startswith('v36top_L01')]
    rows = []
    for r in pairs:
        ref = {'NEW': 'X_THETA2'}.get(r['sign'], r['sign'].split('/')[0])
        g = r['gloss']
        ts = by_val.get(g, set())
        if r['conf'] == 'L':
            st = 'excluded:gloss-conf-L'
        elif not ts:
            st = 'excluded:no-key-sign'
        else:
            st = 'scored'
        rows.append(('v36top_L01', int(r['idx']), ref, '|'.join(sorted(ts)), g, st))
    # the reader passes run past pos 18; the line's remaining positions are outside the gloss span
    recon = [r for r in rd(os.path.join(B, 'recon.tsv')) if r['line'] == 'v36top_L01']
    for r in recon:
        if int(r['pos']) > 18:
            ref = r['sign'] if r['sign'] != '?' else (r['A'] or '?')
            rows.append(('v36top_L01', int(r['pos']), ref, '', '', 'excluded:outside-gloss-span'))
    write_truth('ceppo-f36v-gloss', 'Birago 1571 no.24 fr.3252 f.36v L1 vs the clerk interlinear gloss (HARVEST-D read)', rows)
    od = norm('ceppo-f36v-gloss', None)
    only = {'v36top_L01'}
    write_out(od, 'passA', [os.path.join(B, 'passA_v36.tsv')], only_lines=only)
    write_out(od, 'passB', [os.path.join(B, 'passB_v36.tsv')], only_lines=only)
    write_out(od, 'passD', [os.path.join(B, 'passD.tsv')], only_lines=only)
    with open(os.path.join(od, 'recon.tsv'), 'w') as f:
        f.write('line\tpos\tsign\n')
        for r in recon:
            f.write('v36top_L01\t%s\t%s\n' % (r['pos'], r['sign']))

    # f.21v and f.87 S-graded spans
    for leaf in ('f21v', 'f87'):
        ct = rd(os.path.join(C, 'ciphertext_%s.tsv' % leaf))
        tk = rd(os.path.join(C, 'reading_%s_tokens.tsv' % leaf))
        assert len(ct) == len(tk), leaf
        rows = []
        for c, t in zip(ct, tk):
            assert c['sign'] == t['sign'], (leaf, c, t)
            v = t['value']
            ts = by_val.get(v, set())
            if t['grade'] != 'S':
                st = 'excluded:grade-' + (t['grade'] or 'none')
            elif c['sign'] not in ts:
                st = 'excluded:value-not-from-key'
            else:
                st = 'scored'
            rows.append((c['line'], int(c['pos']), c['sign'], '|'.join(sorted(ts)) if st == 'scored' else '', v, st))
        name = 'ceppo-%s-S' % leaf
        write_truth(name, 'Ceppo-Nevers fr.3251 %s: S-graded tokens of the committed decode under the printed key' % leaf, rows)
        od = norm(name, None)
        if leaf == 'f21v':
            write_out(od, 'passA', [os.path.join(C, 'f21v/passA_L01-06.tsv'), os.path.join(C, 'f21v/passA_L07-11.tsv')], 'f21v')
            write_out(od, 'passB', [os.path.join(C, 'f21v/passB_L01-06.tsv'), os.path.join(C, 'f21v/passB_L07-11.tsv')], 'f21v')
            write_out(od, 'passC', [os.path.join(C, 'f21v/passC.tsv')], 'f21v')
        else:
            write_out(od, 'passA', [os.path.join(C, 'f87/passA.tsv')], 'f87')
            write_out(od, 'passB', [os.path.join(C, 'f87/passB.tsv')], 'f87')
            write_out(od, 'passC', [os.path.join(C, 'f87/passC.tsv')], 'f87')


if __name__ == '__main__':
    main()

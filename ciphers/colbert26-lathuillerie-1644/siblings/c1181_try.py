"""COL26-1181 (account 4, LANE DEFAULT-A4-0437-15, 15 Oct 2026): per-code test of 11 = re and 81 = me (COL26-KEY leads).

Registration: ../PREREG-COL26-1181.md. Instrument: tools/decode_key.py --try (MQS-CROSSWORD), key key_f23.tsv only (never
written). Streams (one decode_key job each, lines run on): f23 (exceptions_f23), c50 (exceptions_c50) and every key_f23-family
sibling unit in siblings/*_reconciled.tsv (c32, c33, c3536, c3940, c4749, c5456, c6263, and c51 = the 51L rows of
c5051; the 50a/50b rows are canvas 50, already in ciphertext_c50.tsv). Unsettled tokens 'A/B' kept as unkeyed signs.
Held out = every stream except c50 (the candidates came from c50's gloss).

Runs (LM fr17 primary, fr16 sensitivity; window 8; nulls 200):
  T  --try 11=re, --try 81=me on held-out, on c50 alone and on all.
  R  runner-up: key copy with the code blanked, --try CODE=VALUE --words re,me,ble,il,de (runner-up among 23 letters +
     NULL + those words) on held-out (fr17) -- reported, not gating.
  K  value-class known-answer control (2-letter values, C in key_f23: 16 se, 28 la, 33 ux, 36 ez, 51 de) on all streams,
     fr17: key copy with the code's value replaced by one letter ('e', or 'a' where the value starts with e); true value
     tried (5 trials) and each other control value tried (20 trials). Gate for S licence: true accepted >= 4/5 AND false
     accepted <= 2/20.
Writes siblings/c1181_try_out.txt (with --write); temp files in a scratch directory only. --check: re-run and fail if the
committed output differs.
"""
import csv, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(T))
DK = os.path.join(ROOT, 'tools', 'decode_key.py')
OUT = os.path.join(HERE, 'c1181_try_out.txt')
UNITS = ['c32', 'c33', 'c3536', 'c3940', 'c4749', 'c5456', 'c6263']
CONTROL = [('16', 'se'), ('28', 'la'), ('33', 'ux'), ('36', 'ez'), ('51', 'de')]


def sibling_streams(tmp):
    jobs = []
    for u in UNITS + ['c51']:
        src = os.path.join(HERE, ('c5051' if u == 'c51' else u) + '_reconciled.tsv')
        rows = list(csv.DictReader(open(src, encoding='utf-8'), delimiter='\t'))
        if u == 'c51':
            rows = [r for r in rows if r['line'].startswith('51')]
        p = os.path.join(tmp, f'ct_{u}.tsv')
        with open(p, 'w', encoding='utf-8') as f:
            f.write('line\tpos\tsign\tconf\n')
            for r in rows:
                for i, t in enumerate(r['tokens'].split(), 1):
                    f.write(f"{u}_{r['line']}\t{i}\t{t}\t\n")
        jobs.append(dict(name=u, ciphertext=p, key='key_f23.tsv', format='tsv', style='spaced'))
    return jobs


def base_jobs(tmp):
    f23 = dict(name='f23', ciphertext='ciphertext_f23.tsv', key='key_f23.tsv', format='tsv', style='spaced',
               exceptions='exceptions_f23.tsv')
    c50 = dict(name='c50', ciphertext='ciphertext_c50.tsv', key='key_f23.tsv', format='tsv', style='spaced',
               exceptions='exceptions_c50.tsv')
    return f23, c50, sibling_streams(tmp)


def config(tmp, name, jobs, key=None):
    js = []
    for j in jobs:
        j = {k: v for k, v in j.items() if k != 'name'}
        if key:
            j['key'] = key
        js.append(j)
    p = os.path.join(tmp, f'cfg_{name}.json')
    json.dump({'target': T, 'jobs': js}, open(p, 'w'))
    return p


def blank_key(tmp, code, value):
    rows = open(os.path.join(T, 'key_f23.tsv'), encoding='utf-8').read().splitlines()
    out = []
    for l in rows:
        f = l.split('\t')
        if f[0] == code:
            f[1] = value
        out.append('\t'.join(f))
    p = os.path.join(tmp, f'key_{code}_{value or "blank"}.tsv')
    open(p, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    return p


def run(cfg, hyp, lm, extra=()):
    cmd = [sys.executable, DK, T, '--config', cfg, '--try', hyp, '--lm', lm, '--window', '8', '--nulls', '200', *extra]
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    txt = p.stdout + p.stderr
    summ = [l for l in txt.splitlines() if re.search(r'verdict|statistic|p95|accept|reject|undecided', l, re.I)]
    return txt, summ


def main():
    write = '--write' in sys.argv
    check = '--check' in sys.argv
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        f23, c50, sibs = base_jobs(tmp)
        held = [f23] + sibs
        sets = {'heldout': held, 'c50': [c50], 'all': held + [c50]}
        cfgs = {k: config(tmp, k, v) for k, v in sets.items()}
        for lm in ['tools/data/fr17', 'fr16']:
            for hyp in ['11=re', '81=me']:
                for s in ['heldout', 'c50', 'all']:
                    txt, summ = run(cfgs[s], hyp, lm)
                    out.append(f'## T {hyp} {s} lm={lm}')
                    out.append(txt.rstrip())
        for code, hyp in [('11', '11=re'), ('81', '81=me')]:
            k = blank_key(tmp, code, '')
            cfg = config(tmp, f'blank{code}', held, key=k)
            txt, _ = run(cfg, hyp, 'tools/data/fr17', ['--words', 're,me,ble,il,de'])
            out.append(f'## R {hyp} heldout blanked lm=tools/data/fr17')
            out.append(txt.rstrip())
        for code, true in CONTROL:
            one = 'a' if true.startswith('e') else 'e'
            k = blank_key(tmp, code, one)
            cfg = config(tmp, f'K{code}', held + [c50], key=k)
            for v in [true] + [w for _, w in CONTROL if w != true]:
                txt, _ = run(cfg, f'{code}={v}', 'tools/data/fr17')
                out.append(f'## K {code}={v} ({"true" if v == true else "false"}; current {one}) all lm=tools/data/fr17')
                out.append(txt.rstrip())
    body = '\n'.join(out) + '\n'
    if check:
        same = os.path.exists(OUT) and open(OUT, encoding='utf-8').read() == body
        print('c1181_try: up to date' if same else 'c1181_try: STALE')
        return 0 if same else 1
    if write:
        open(OUT, 'w', encoding='utf-8').write(body)
    sys.stdout.write(body)
    return 0


if __name__ == '__main__':
    sys.exit(main())

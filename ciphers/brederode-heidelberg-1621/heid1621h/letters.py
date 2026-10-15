#!/usr/bin/env python3
"""HEID-1621H step 1 (PREREG-HEID1621H.md): look-alike pass on the trailing letter signs, from the reads on disk.

usage: python3 letters.py [--check]
Builds two-reader agreement rows for every letter position (375 A/B, 423 A/B, 379 A/B from ciphertext.tsv notes, and 375 vs 379
reconciled per aligned unit), runs tools/lookalike_pass.py confusion and reconcile (re-read rows = NONE/L: the HEID-1621G crops are
not on disk and no vision call is licensed, so by the tool's fixed rule no tile settles), writes per-sign agreement, focus.tsv and
re-runs the 375-vs-379 unit control on the post-pass units. --check rebuilds in a temp dir and exits 1 if a committed output differs.
No values are read; nothing here decodes.
"""
import csv, difflib, io, json, os, re, subprocess, sys, tempfile, collections
H = os.path.dirname(os.path.abspath(__file__)); G = os.path.join(H, '..', 'heid1621g'); ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
sys.path.insert(0, G)
import units as U  # HEID-1621G unit grammar and readers

def toks(rest):
    out, buf = [], rest.replace('] ', ']\x00').replace(' [', '\x00[').split('\x00')
    for t in buf:
        out += [t] if t.startswith('[') else [x for x in t.split() if x != '.']
    return out

def norm(t):
    if t.startswith('['): return 'SYM' if t.startswith('[sym') else 'CLEAR'
    t = re.sub(r'\?\(.*?\)$', '', t).rstrip('?')
    if t == '1/i': return 'i'
    return 'i' if t == '1' else t   # the undotted minim in letter position: both readers wrote 1, read i (HEID-1621 rule)

def reads(block):
    txt = open(os.path.join(G, 'reads_raw.txt'), encoding='utf-8').read()
    r = {}
    for who in 'AB':
        m = re.search(rf'## {block} reader {who}\n(.*?)(?=\n#)', txt, re.S)
        r[who] = {ln.split('\t')[0]: [norm(t) for t in toks(ln.split('\t', 1)[1])] for ln in m.group(1).splitlines() if '\t' in ln}
    return r

def recon_letters(name):
    """(line, pos-in-line, reconciled token) for every letter-closing token of the reconciled block."""
    out = []
    for ln in open(os.path.join(G, name), encoding='utf-8'):
        if not ln.strip() or ln.startswith('#'): continue
        line, rest = ln.rstrip('\n').split('\t', 1)
        for i, t in enumerate(toks(rest), 1):
            a = t.split('|')[0]
            if not a.startswith('[') and len(a) == 1 and a.isalpha(): out.append((line, i, a))
    return out

def build(outdir):
    agree, rows_c = [], []
    # 375 and 423: reader A vs B at each reconciled letter position (+ positions where a reader put a letter/sign the other did not)
    for block, rec in (('375', 'recon_375.txt'), ('423', 'recon_423.txt')):
        r = reads(block)
        rsplit = {}   # reconciler's letter splits "X|Y" (e.g. 423 q|9/4, the eye's alternative where both readers agree)
        for ln in open(os.path.join(G, rec), encoding='utf-8'):
            if not ln.strip() or ln.startswith('#'): continue
            line, rest = ln.rstrip('\n').split('\t', 1)
            for i, t in enumerate(toks(rest), 1):
                if '|' in t and len(t.split('|')[0]) == 1 and t.split('|')[0].isalpha(): rsplit[(line, i)] = norm(t.split('|')[1].split('/')[0])
        for line in sorted(set(r['A']) | set(r['B'])):
            a, b = r['A'].get(line, []), r['B'].get(line, [])
            for i, (x, y) in enumerate(zip(a, b), 1):
                prev_num = i > 1 and (a[i - 2].isdigit() or b[i - 2].isdigit())
                is_let = lambda t: len(t) == 1 and t.isalpha()
                if (is_let(x) or is_let(y) or (prev_num and (x == 'SYM' or y == 'SYM'))) and not (x.isdigit() and y.isdigit()):
                    if x == y and (line, i) in rsplit and rsplit[(line, i)] != x: y = rsplit[(line, i)]
                    agree.append(dict(idA=x, idB=y, status='split' if x != y else 'agree', passage=f'w{block}_{line}', posA=i))
    # 379: reader A vs B from ciphertext.tsv notes ("A x, B r"); where only the eye's alt is noted, eye vs readers
    for r in csv.reader((l for l in open(os.path.join(H, '..', 'ciphertext.tsv'), encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
        if r[0] == 'line' or r[2] != 'let': continue
        r = r + [''] * (6 - len(r)); lab, alt, note = r[3], r[4], r[5]
        m = re.match(r'A (\S+?)\??, B (\S+?)\??(;|$)', note)
        if m:
            a, b = norm(m.group(1)), norm(m.group(2))
            if a == b and a != lab:   # both readers one way, the reconciler the other: record readers vs eye
                b = lab
            elif a == b == lab and alt and norm(alt) != lab:   # readers agree; the eye's noted alternative is the other label
                b = norm(alt)
        else:
            a, b = lab, lab
        agree.append(dict(idA=a, idB=b, status='split' if a != b else 'agree', passage=f'w379_{r[0]}', posA=r[1]))
    # cross-witness: 375 reconciled vs 379 reconciled, aligned units (HEID-1621G grammar), letter field with case kept
    u375 = U.units_from_tokens(U.read_recon('recon_375.txt')); u379 = U.units_from_tokens(U.read_379())
    def let_case(seq):  # recover the case of the closing letter token (units.py lower-cases it)
        out = []
        for u in U.units_from_tokens(seq): out.append(u)
        return out
    raw375 = [t for t in U.read_recon('recon_375.txt')]; raw379 = U.read_379()
    def closing(seq):
        res, run = [], 0
        for t in seq:
            if U.is_num(t[2]): run += 1
            elif U.is_let(t[2]): res.append(t[2]); run = 0
            else:
                if run: res.append('')
                run = 0
        if run: res.append('')
        return res
    c375, c379 = closing(raw375), closing(raw379)
    a, b = [u['unit'] for u in u375], [u['unit'] for u in u379]
    sm = difflib.SequenceMatcher(None, [x.rsplit('.', 1)[0] for x in a], [x.rsplit('.', 1)[0] for x in b], autojunk=False)
    cross = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal': continue
        for k in range(i2 - i1):
            x, y = c375[i1 + k] or 'NONE', c379[j1 + k] or 'NONE'
            if x == 'NONE' and u375[i1 + k]['form'] == 'N': x = 'SYM' if y != 'NONE' else 'NONE'
            cross.append(dict(idA=x, idB=y, status='split' if x != y else 'agree', passage='x375_379', posA=i1 + k + 1,
                              unit=u375[i1 + k]['numbers']))
    agree += [{k: v for k, v in c.items() if k != 'unit'} for c in cross]
    files = {}
    def w(name, rows, fields):
        s = io.StringIO(); d = csv.DictWriter(s, fieldnames=fields, delimiter='\t', lineterminator='\n'); d.writeheader(); d.writerows(rows)
        files[name] = s.getvalue()
    w('agreement_letters.tsv', agree, ['idA', 'idB', 'status', 'passage', 'posA'])
    # passC (the committed labels: idA = the reconciled/committed side) and tiles for every split position
    passc = [dict(passage=r['passage'], pos=r['posA'], sign_id=r['idA'], conf='M') for r in agree]
    tiles = [dict(run='heid1621h', passage=r['passage'], pos=r['posA'], passC=r['idA'], A=r['idA'], B=r['idB'], status='split',
                  why='split', candidates=','.join(sorted({r['idA'], r['idB']})), before='', after='', noteA='', noteB='')
             for r in agree if r['status'] == 'split']
    reread = [dict(passage=t['passage'], pos=t['pos'], label='NONE', conf='L', second='',
                   note='no re-read: HEID-1621G crops not on disk; no vision call licensed (brief)') for t in tiles]
    w('passC_letters.tsv', passc, ['passage', 'pos', 'sign_id', 'conf'])
    w('tiles_letters.tsv', tiles, list(tiles[0]))
    w('reread_letters.tsv', reread, list(reread[0]))
    for n, s in files.items(): open(os.path.join(outdir, n), 'w').write(s)
    tool = os.path.join(ROOT, 'tools', 'lookalike_pass.py')
    subprocess.run([sys.executable, tool, 'confusion', os.path.join(outdir, 'agreement_letters.tsv'), '--out', os.path.join(outdir, 'confusion.tsv')], check=True, capture_output=True)
    rec = subprocess.run([sys.executable, tool, 'reconcile', '--tiles', os.path.join(outdir, 'tiles_letters.tsv'), '--passc', os.path.join(outdir, 'passC_letters.tsv'),
                          '--reread', os.path.join(outdir, 'reread_letters.tsv'), '--out', os.path.join(outdir, 'passD_letters.tsv'),
                          '--focus', os.path.join(outdir, 'focus.tsv')], check=True, capture_output=True, text=True).stdout
    fp = os.path.join(outdir, 'focus.tsv')   # the no-re-read placeholder is not a candidate for the sorter
    ftxt = open(fp).read(); open(fp, 'w').write(ftxt.replace(', look-alike NONE (L)', ', no look-alike re-read (crops not on disk)').replace('which of NONE, ', 'which of '))
    # per letter sign: positions carrying the sign in any reading; agreed = positions where both readings carry it
    pd = list(csv.DictReader(open(os.path.join(outdir, 'passD_letters.tsv')), delimiter='\t'))
    settled = {(r['passage'], r['pos']) for r in pd if r['note'] != 'lookalike UNSETTLED'}
    per = collections.defaultdict(lambda: [0, 0, set()])
    for r in agree:
        for s in {r['idA'], r['idB']}:
            per[s][0] += 1
            if r['status'] == 'agree' or (r['passage'], str(r['posA'])) in settled: per[s][1] += 1
            else: per[s][2].add(({r['idA'], r['idB']} - {s}).pop())
    sign_rows = [dict(sign=s, positions=v[0], agreed_after_pass=v[1], agreement=round(v[1] / v[0], 3), split_with=','.join(sorted(v[2])))
                 for s, v in sorted(per.items(), key=lambda kv: (kv[1][1] / kv[1][0], kv[0]))]
    w2 = io.StringIO(); d = csv.DictWriter(w2, fieldnames=list(sign_rows[0]), delimiter='\t', lineterminator='\n'); d.writeheader(); d.writerows(sign_rows)
    open(os.path.join(outdir, 'per_sign.tsv'), 'w').write(w2.getvalue())
    # control re-run on the post-pass units: no tile settled, so the unit sequences are the HEID-1621G ones
    relab = sum(1 for r in pd if r['note'].startswith('lookalike') and r['note'] != 'lookalike UNSETTLED')
    gate = difflib.SequenceMatcher(None, a, b, autojunk=False)
    m = sum(bl.size for bl in gate.get_matching_blocks())
    res = dict(agreement_rows=len(agree), split_rows=len(tiles), reconcile=rec.strip(), relabelled=relab,
               control_units_375=len(a), control_units_379=len(b), control_matched=m, control_agreement=round(m / max(len(a), len(b)), 3),
               control_gate=0.90, control_pass=m / max(len(a), len(b)) >= 0.90,
               cross_witness_letter_splits=[f"{c['unit']}: 375 {c['idA']} / 379 {c['idB']}" for c in cross if c['status'] == 'split'])
    open(os.path.join(outdir, 'letters_result.json'), 'w').write(json.dumps(res, indent=1) + '\n')

OUTS = ['agreement_letters.tsv', 'passC_letters.tsv', 'tiles_letters.tsv', 'reread_letters.tsv', 'confusion.tsv', 'passD_letters.tsv',
        'focus.tsv', 'per_sign.tsv', 'letters_result.json']

if __name__ == '__main__':
    if '--check' in sys.argv:
        with tempfile.TemporaryDirectory() as t0:
            t = os.path.join(t0, 'heid1621h'); os.mkdir(t)   # confusion names the leaf after the folder
            build(t)
            bad = [n for n in OUTS if open(os.path.join(t, n)).read() != open(os.path.join(H, n)).read()]
        print('check:', 'STALE ' + ' '.join(bad) if bad else 'OK'); sys.exit(1 if bad else 0)
    build(H); print(open(os.path.join(H, 'letters_result.json')).read())

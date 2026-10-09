#!/usr/bin/env python3
"""Offline round trip for the encipherer's corrections (MQS-STRUCK-2, 9 Oct 2026): a sorter save with struck piles, struck
boxes and overwritten boxes -> tools/sign_sorter_apply.py --pass-out -> tools/decode_key.py --corrections final|original ->
tools/decipher_sheet.py reading. Prereg: tools/tests/PREREG-MQS-STRUCK-2.md. No network; temporary directories only.

  python3 tools/tests/test_struck_roundtrip.py              offline tests + control K / nulls N1, N2 (seeds 0-4)
  python3 tools/tests/test_struck_roundtrip.py --controls   print only the per-seed control table
"""
import csv, json, os, random, re, shutil, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sign_sorter_apply as ssa, decode_key as dk, decipher_sheet as ds, cvd_check

fails = []
TEXT = ("monsieur jay receu vostre lettre du douziesme de ce mois par laquelle vous me mandez que le roy est en bonne "
        "disposition et que les affaires de flandres se portent mieux que lon ne pensoit")
PLAIN = [c for c in TEXT if c.isalpha()][:120]
SEEDS = 5


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


def wtsv(path, header, rows):
    with open(path, 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t'); w.writerow(header); w.writerows(rows)


def fixture(d, seed):
    """Sorter inputs with 10 planted states; returns (planted set, key dict code->letter)."""
    rnd = random.Random(seed)
    letters = sorted(set(PLAIN))
    enc = {l: str(c) for l, c in zip(letters, rnd.sample(range(10, 99), len(letters)))}
    toks = [dict(sign=enc[c], kind='plain') for c in PLAIN]
    for i in rnd.sample(range(len(toks)), 5):
        toks[i]['kind'] = 'over'
        toks[i]['old'] = rnd.choice([v for v in enc.values() if v != toks[i]['sign']])
    for n in range(5):
        i = rnd.randrange(1, len(toks))
        toks.insert(i, dict(sign=rnd.choice(list(enc.values())), kind='struck', via='pile' if n < 2 else 'box'))
    signs, labels, states, moves = [], [], [], []
    for i, t in enumerate(toks):
        sid = f's{i:03d}'; t['sid'] = sid
        line, pos = f'L{i // 32 + 1}', i % 32 + 1
        t['line'], t['pos'] = line, pos
        signs.append([sid, 'p1', pos * 20, (i // 32) * 40, 18, 30, line, pos])
        labels.append([sid, t['sign']])
        if t['kind'] == 'over':
            states.append(dict(sid=sid, state='over', old=t['old']))
        elif t['kind'] == 'struck' and t['via'] == 'box':
            states.append(dict(sid=sid, state='struck'))
        elif t['kind'] == 'struck':
            moves.append(dict(sid=sid, to='DEL'))
    plain_i = [t for t in toks if t['kind'] == 'plain']
    t = plain_i[3]  # one ordinary correction by the person: a mislabelled tile moved to its right pile
    labels[int(t['sid'][1:])][1] = '99'; moves.append(dict(sid=t['sid'], to=t['sign']))
    wtsv(os.path.join(d, 'signs.tsv'), ['sid', 'page', 'x', 'y', 'w', 'h', 'line', 'pos'], signs)
    wtsv(os.path.join(d, 'labels.tsv'), ['sid', 'sign'], labels)
    db = os.path.join(d, 'db')
    for coll, docs in (('piles', [dict(pile='DEL', state='struck')]), ('moves', moves), ('states', states), ('newpiles', [dict(id='DEL')])):
        os.makedirs(os.path.join(db, coll))
        for n, doc in enumerate(docs):
            json.dump(dict(data=doc), open(os.path.join(db, coll, f'{n}.json'), 'w'))
    planted = set()
    for t in toks:
        if t['kind'] == 'struck':
            planted.add(('struck', f"{t['line']}:{t['pos']}", 'DEL' if t['via'] == 'pile' else t['sign']))
        elif t['kind'] == 'over':
            planted.add(('over', f"{t['line']}:{t['pos']}", f"{t['old']}>{t['sign']}"))
    return planted, enc


CALL_RE = re.compile(r'<div class="callout" data-corr="(\w+) ([^"]+)"><b>\w+</b>[^<]*?token \d+: ([^<]*)</div>')


def found(html_doc):
    out = set()
    for k, lp, what in CALL_RE.findall(html_doc):
        m = re.match(r'sign \[(.+)\] crossed out$', what) if k == 'struck' else re.match(r'(.+) overwritten as (.+)$', what)
        if m:
            out.add((k, lp, m.group(1) if k == 'struck' else f'{m.group(1)}>{m.group(2)}'))
    return out


def pipeline(d, enc, mode, null=None, seed=0):
    tgt = os.path.join(d, f'tgt-{mode}-{null}')
    os.makedirs(tgt)
    passp = os.path.join(d, 'pass.tsv')
    rows = list(csv.reader(open(passp), delimiter='\t'))
    h, body = rows[0], rows[1:]
    si = h.index('state')
    if null == 'drop':
        h = h[:si] + h[si + 1:]; body = [r[:si] + r[si + 1:] for r in body]
    elif null == 'shuffle':
        col = [r[si] for r in body]; random.Random(1000 + seed).shuffle(col)
        body = [r[:si] + [c] + r[si + 1:] for r, c in zip(body, col)]
    wtsv(os.path.join(tgt, 'ciphertext.tsv'), h, body)
    wtsv(os.path.join(tgt, 'key.tsv'), ['code', 'value'], [[c, l] for l, c in enc.items()])
    json.dump(dict(format='tsv', ciphertext='ciphertext.tsv', style='concat'), open(os.path.join(tgt, 'decode.json'), 'w'))
    out = os.path.join(d, f'sheet-{mode}-{null}.html')
    ds.main(['reading', tgt, '--out', out, '--tiles', 'none', '--corrections', mode])
    recs, _ = dk.graded_recs(tgt, dict(format='tsv', ciphertext='ciphertext.tsv', corrections=mode))
    acc = [r['value'] for r in recs if r['kind'] == 'sign']
    return open(out).read(), sum(a == b for a, b in zip(acc, PLAIN)) / max(len(acc), len(PLAIN))


def run_seed(seed):
    d = tempfile.mkdtemp()
    try:
        planted, enc = fixture(d, seed)
        ssa.main(['--labels', os.path.join(d, 'labels.tsv'), '--db', os.path.join(d, 'db'), '--out', os.path.join(d, 'settled.tsv'),
                  '--signs', os.path.join(d, 'signs.tsv'), '--pass-out', os.path.join(d, 'pass.tsv'), '--summary', os.path.join(d, 's.json')])
        r = dict(planted=len(planted))
        for mode in ('final', 'original'):
            doc, acc = pipeline(d, enc, mode)
            r[mode] = len(found(doc) & planted); r[mode + '_acc'] = acc
            if mode == 'final':
                r['doc'] = doc
        for null in ('drop', 'shuffle'):
            doc, _ = pipeline(d, enc, 'final', null, seed)
            r[null] = len(found(doc) & planted)
        return r
    finally:
        shutil.rmtree(d)


def controls():
    print('seed\tplanted\tK_final\tK_original\tacc_final\tN1_drop\tN2_shuffle')
    rs = [run_seed(s) for s in range(SEEDS)]
    for s, r in enumerate(rs):
        print(f"{s}\t{r['planted']}\t{r['final']}/10\t{r['original']}/10\t{r['final_acc']:.3f}\t{r['drop']}/10\t{r['shuffle']}/10")
    k = sum(r['final'] == 10 and r['original'] == 10 for r in rs)
    n = sum(r['drop'] < 10 and r['shuffle'] < 10 for r in rs)
    print(f'K 10/10 (final and original) on {k}/{SEEDS} (gate {SEEDS}/{SEEDS}); nulls < 10/10 on {n}/{SEEDS} (gate {SEEDS}/{SEEDS})')
    return k == SEEDS and n == SEEDS, rs


def must_not():
    d = tempfile.mkdtemp()
    try:
        planted, enc = fixture(d, 0)
        lab, db = os.path.join(d, 'labels.tsv'), os.path.join(d, 'db')
        # M1: no state saved -> export byte for byte as before (no state column)
        db0 = os.path.join(d, 'db0'); shutil.copytree(db, db0); shutil.rmtree(os.path.join(db0, 'states'))
        json.dump(dict(data=dict(pile='DEL')), open(os.path.join(db0, 'piles', '0.json'), 'w'))
        a, b = os.path.join(d, 'a.tsv'), os.path.join(d, 'b.tsv')
        ssa.main(['--labels', lab, '--db', db0, '--out', a])
        rows = list(csv.reader(open(a), delimiter='\t'))
        check(rows[0] == ['sid', 'old_sign', 'new_sign', 'status', 'mode'], 'M1: no state saved -> no state column')
        ssa.main(['--labels', lab, '--db', db, '--out', b])
        rb = list(csv.reader(open(b), delimiter='\t'))
        check(rb[0][-1] == 'state' and [r[:5] for r in rb] == rows, 'state column appended last, other columns unchanged')
        check(sum(1 for r in rb[1:] if r[-1] == 'struck') == 5 and sum(1 for r in rb[1:] if r[-1].startswith('over=')) == 5,
              '5 struck and 5 over=OLD>NEW in the export')
        # M3: a state doc for an unknown sid is dropped and counted
        json.dump(dict(data=dict(sid='nope', state='struck')), open(os.path.join(db, 'states', '99.json'), 'w'))
        ssa.main(['--labels', lab, '--db', db, '--out', b, '--summary', os.path.join(d, 's.json')])
        check(json.load(open(os.path.join(d, 's.json'))).get('states_dropped') == 1, 'M3: state doc for an unknown sid dropped, counted')
        # M4: an unknown state is refused
        json.dump(dict(data=dict(sid='s001', state='weird')), open(os.path.join(db, 'states', '98.json'), 'w'))
        try:
            ssa.main(['--labels', lab, '--db', db, '--out', b]); check(False, 'M4: unknown state refused')
        except SystemExit as e:
            check(e.code == 2, 'M4: unknown state refused')
        os.remove(os.path.join(db, 'states', '98.json'))
        try:
            ssa.main(['--labels', lab, '--db', db, '--out', b, '--pass-out', os.path.join(d, 'p.tsv')]); check(False, '--pass-out needs --signs')
        except SystemExit as e:
            check(e.code == 2, '--pass-out needs --signs')
        # tokens-tsv path of the sheet reads a state column too
        tt = os.path.join(d, 'tok.tsv')
        wtsv(tt, ['line', 'pos', 'sign', 'value', 'grade', 'state'], [['L1', 1, '12', 'a', 'H', ''], ['L1', 2, '13', '', 'struck', 'struck'],
                                                                     ['L1', 3, '14', 'c', 'H', 'over=15>14']])
        recs, _ = ds.tokens_from_tsv(tt)
        check([r.get('state', '') for r in recs if r['kind'] != 'line'] == ['', 'struck', 'over=15>14'] and recs[2]['kind'] == 'struck',
              '--tokens-tsv reads the state column')
    finally:
        shutil.rmtree(d)


def gramont_unchanged():
    """M2: an already-read control with no state renders no Corrections section and no correction CSS."""
    d = tempfile.mkdtemp()
    try:
        root = os.path.dirname(os.path.dirname(HERE)); out = os.path.join(d, 'g.html')
        ds.main(['reading', os.path.join(root, 'ciphers', 'fr2980-gramont'), '--config',
                 os.path.join(HERE, 'decode_configs', 'fr2980-gramont.json'), '--job', 'ciphertext.txt', '--tiles', 'none', '--out', out])
        doc = open(out).read()
        check('Corrections on the page' not in doc and 'data-corr' not in doc and '.tk.corr' not in doc,
              'M2: Gramont reading sheet (no state) has no correction section, label or CSS')
    finally:
        shutil.rmtree(d)


def sheet_checks(doc):
    check(doc.count('<h2>Corrections on the page</h2>') == 1 and '.tk.corr' in doc, 'reading sheet has one Corrections section')
    check('STRUCK' in doc and 'OVER' in doc and 'not read' in doc, 'struck and over carry text labels (not colour alone)')
    cols = set(c.lower() for c in re.findall(r'#[0-9a-fA-F]{6}\b', doc))
    allowed = set(c.lower() for c in cvd_check.PALETTES['sheets_light']['marks'] + [cvd_check.PALETTES['sheets_light']['bg'],
                                                                                   '#bbbbbb', '#f0e442', '#56b4e9', '#24211c']
                  + cvd_check.PALETTES['dark']['marks'] + [cvd_check.PALETTES['dark']['bg'], '#a9a39a', '#4a4640', '#1b1916'])
    check(cols <= allowed, 'sheet colours all in the checked palettes: ' + ', '.join(sorted(cols - allowed)))
    check(cvd_check.check_palette('sheets_light')['code'] == 0, 'cvd_check passes sheets_light')
    d = tempfile.mkdtemp()
    try:
        p = os.path.join(d, 'sheet.html'); open(p, 'w').write(doc)
        import subprocess
        r = subprocess.run([sys.executable, os.path.join(os.path.dirname(HERE), 'cvd_check.py'), '--audit', p], capture_output=True, text=True)
        print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else '')
        check(r.returncode == 0, 'cvd_check --audit on the rendered sheet: no CVD-COLLAPSE / RED-GREEN flags')
    finally:
        shutil.rmtree(d)


if __name__ == '__main__':
    if '--controls' in sys.argv:
        sys.exit(0 if controls()[0] else 1)
    must_not()
    gramont_unchanged()
    ok, rs = controls()
    check(ok, 'control K / nulls N1, N2 meet the prereg gates')
    check(all(r['final_acc'] == 1.0 for r in rs), 'final decode reads the plaintext exactly (struck skipped, NEW read)')
    sheet_checks(rs[0]['doc'])
    print('struck round trip: ' + (f'{len(fails)} failures' if fails else 'all passed'))
    sys.exit(1 if fails else 0)

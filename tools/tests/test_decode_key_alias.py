#!/usr/bin/env python3
"""Offline tests for tools/decode_key.py --aliases / --alias-scan (MQS-ALIAS, 9 Oct 2026; Lasry, Biermann and
Tomokiyo 2023 pp.189-190; Browne 1840 via ciphers/sp54-maclean-1745/browne_feigned_names.tsv). No network.

  python3 tools/tests/test_decode_key_alias.py              offline tests
  python3 tools/tests/test_decode_key_alias.py --controls [--out FILE]
        controls A (--aliases, en18 + Browne table) and B (--alias-scan fr, fr16) of tools/tests/PREREG-MQS-ALIAS.md.
        Never writes into a target folder.
"""
import gzip, glob, hashlib, json, os, random, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import decode_key as dk

BROWNE = os.path.join(ROOT, 'ciphers', 'sp54-maclean-1745', 'browne_feigned_names.tsv')
DANZAY_CFG = os.path.join(HERE, 'decode_configs', 'fr20140-danzay-1557.json')
# Constructed, not quoted: the shape of the F125 sentence (Lasry, Biermann and Tomokiyo 2023 p.190); the paper's own
# wording is not on disk.
F125_LIKE = "et monsieur de Throgmorton qui s'apellera entre nous la Tour vous dira le surplus"
fails = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


def table(rows):
    fd, p = tempfile.mkstemp(suffix='.tsv')
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write('alias\tmeaning\tgrade\tfirst_use\tlast_use\tevidence\tsource\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    return p


def offline():
    rows = dk.load_aliases(BROWNE)
    check(len(rows) == 24, f'browne_feigned_names.tsv loads unchanged as an alias table: {len(rows)} rows')
    w = [r for r in rows if r['alias'].startswith('Watson')][0]
    check(w['variants'] == ['watson', 'walker'], f"variant cell 'Watson, or Walker' -> {w['variants']}")
    check(dk.alias_grade('H-print, alignment I') == 'I' and dk.alias_grade('') == 'M', 'grade: last standalone letter')
    lt = dk.load_aliases(table([['la Tour', 'Throckmorton', 'I', '', '', 'p.190', 'constructed']]))
    ann, hits = dk.annotate_aliases(F125_LIKE, lt)
    check('la Tour [= Throckmorton, I] vous' in ann and len(hits) == 1, 'renders la Tour [= Throckmorton, I]')
    ann2, h2 = dk.annotate_aliases('la tourelle du chasteau', lt)
    check(not h2, 'must NOT match inside a longer word (la tourelle)')
    ann3, h3 = dk.annotate_aliases('Morrison met Morris', rows)
    check([x[3] for x in h3] == ['morris'], f'bounded: morris yes, morrison no ({[x[3] for x in h3]})')
    f, _ = dk.fold_chars('ilmarquequetaitestarriue')
    check(not dk.find_aliases(f, rows, bounded=False), 'unbounded run: Tait (4 letters) not looked for at min_len 5')
    f, _ = dk.fold_chars('quelemessagierdemorrisestarriue')
    check([h[3] for h in dk.find_aliases(f, rows, bounded=False)] == ['morris'], 'unbounded run: morris found')
    cues = dk.load_alias_cues('fr')
    fo, _ = dk.fold_chars(F125_LIKE)
    sc = dk.scan_announcements(fo, cues)
    check(len(sc) == 1 and sc[0][2] == 's apellera entre nous' and sc[0][4].startswith('la tour')
          and 'throgmorton' in sc[0][3], f'F125-like sentence flagged with referent and name span: {sc}')
    fo, _ = dk.fold_chars("et monsieur de Throgmorton qui nous entre s'apellera la Tour")
    check(not [s for s in dk.scan_announcements(fo, cues) if 'entre' in s[2]], 'reversed cue words not flagged')
    fo, _ = dk.fold_chars('le roy est arriue a bloys et la royne aussi auec toute la court')
    check(not dk.scan_announcements(fo, cues), 'ordinary sentence: no flag')
    for lang in ('fr', 'en', 'it', 'es'):
        check(len(dk.load_alias_cues(lang)) >= 5, f'cue file {lang} loads')
    # rendering only: the committed Danzay reading and token files are byte-identical after --aliases/--alias-scan
    cfg = json.load(open(DANZAY_CFG, encoding='utf-8'))
    tgt = os.path.join(ROOT, cfg['target'])
    outs = [os.path.join(tgt, j[k]) for j in cfg['jobs'] for k in ('reading', 'tokens')]
    before = [hashlib.sha256(open(p, 'rb').read()).hexdigest() for p in outs]
    tmp = tempfile.mkdtemp()
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'decode_key.py'), tgt, '--config', DANZAY_CFG,
                        '--aliases', table([['le Roy de Dannemarch', 'TEST-MEANING', 'M', '', '', 'test', 'test']]),
                        '--alias-scan', 'fr', '--alias-out', os.path.join(tmp, 'ann.txt'),
                        '--alias-tsv', os.path.join(tmp, 'hits.tsv')], capture_output=True, text=True)
    after = [hashlib.sha256(open(p, 'rb').read()).hexdigest() for p in outs]
    check(r.returncode == 0 and before == after, f'Danzay committed outputs unchanged (exit {r.returncode})')
    hits = open(os.path.join(tmp, 'hits.tsv'), encoding='utf-8').read().splitlines()
    check(hits[0].startswith('kind\tsource') and os.path.getsize(os.path.join(tmp, 'ann.txt')) > 0,
          f'annotated view and hit table written ({len(hits) - 1} rows)')
    al = [h.split('\t') for h in hits[1:] if h.startswith('alias')]
    check(al and all(a[7] and set(a[7]) <= set('HCSMIU') for a in al), 'token grades reported from the decode, not the alias grade')


# ---------------------------------------------------------------- controls (PREREG-MQS-ALIAS.md)

def corpus_words(d):
    words = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'tools', 'data', d, '*.txt*'))):
        t = (gzip.open(p, 'rt', encoding='utf-8', errors='ignore') if p.endswith('.gz')
             else open(p, encoding='utf-8', errors='ignore')).read()
        words.extend(dk.fold_chars(t)[0].split())
    return words


def window(words, seed, n=1500):
    rnd = random.Random(seed)
    s = rnd.randrange(0, len(words) - n)
    return words[s:s + n], rnd


def starts(ws):
    st, k = [], 0
    for w in ws:
        st.append(k); k += len(w) + 1
    return st


def control_a(seeds=range(1, 21)):
    words, rows = corpus_words('en18'), dk.load_aliases(BROWNE)
    pairs = [(r, v) for r in rows for v in r['variants']]
    rec = tot = null2 = fp = nw = 0
    for seed in seeds:
        base, rnd = window(words, seed)
        fp += len(dk.find_aliases(' '.join(base), rows)); nw += len(base)
        planted, shuffled, slots = list(base), list(base), []
        for _ in range(10):
            r, v = rnd.choice(pairs)
            k = rnd.randrange(0, len(planted))
            letters = list(v.replace(' ', '')); rnd.shuffle(letters)
            planted.insert(k, v); shuffled.insert(k, ''.join(letters))
            slots = [(s + 1 if s >= k else s, rr) for s, rr in slots] + [(k, r)]
        st = starts(planted)
        got = {(h[0], id(h[2])) for h in dk.find_aliases(' '.join(planted), rows)}
        rec += sum((st[s], id(r)) in got for s, r in slots); tot += len(slots)
        st2 = starts(shuffled)
        got2 = {h[0] for h in dk.find_aliases(' '.join(shuffled), rows)}
        null2 += sum(st2[s] in got2 for s, _ in slots)
    return dict(recall=rec / tot, null2=null2 / tot, null1_per10k=fp / nw * 1e4, n=tot, words=nw)


IN_LIST = ["qui s'apellera entre nous", 'que nous appellerons', 'lequel nous nommerons', 'sous le nom de',
           'qui sera appelle']
OUT_LIST = ["que j'ay baptise", 'a qui nous donnerons le nom de', 'dorenavant dit', 'que vous entendrez par']
NAMES = ['la tour', 'le banquier', 'monsieur de la riviere', 'le jardinier', 'la poste']


def control_b(seeds=range(1, 21)):
    words, cues = corpus_words('fr16'), dk.load_alias_cues('fr')
    res = {'in': [0, 0], 'out': [0, 0], 'rev': [0, 0]}
    fp = nw = 0
    for seed in seeds:
        base, rnd = window(words, seed)
        fp += len(dk.scan_announcements(' '.join(base), cues)); nw += len(base)
        for kind, lst in (('in', IN_LIST), ('out', OUT_LIST), ('rev', IN_LIST)):
            ws, plants = list(base), []
            for _ in range(3):
                ph = dk.fold_chars(rnd.choice(lst))[0].split()
                if kind == 'rev':
                    ph = ph[::-1]
                nm = rnd.choice(NAMES)
                k = rnd.randrange(0, len(ws))
                seg = ph + nm.split()
                ws[k:k] = seg
                plants = [(s + len(seg) if s >= k else s, L, n) for s, L, n in plants] + [(k, len(ph), nm)]
            st, text = starts(ws), ' '.join(ws)
            flags = dk.scan_announcements(text, cues)
            for s, L, nm in plants:
                lo, hi = st[s], st[s + L - 1] + len(ws[s + L - 1])
                res[kind][0] += any(lo <= f[0] < hi and f[4].startswith(nm) for f in flags)
                res[kind][1] += 1
    return dict(in_recall=res['in'][0] / res['in'][1], out_recall=res['out'][0] / res['out'][1],
                null2=res['rev'][0] / res['rev'][1], null1_per10k=fp / nw * 1e4, n=res['in'][1], words=nw)


if __name__ == '__main__':
    if '--controls' in sys.argv:
        a, b = control_a(), control_b()
        ga = a['recall'] >= 0.95 and a['null2'] <= 0.05 and a['null1_per10k'] <= 10
        gb = b['in_recall'] >= 0.95 and b['null2'] <= 0.05 and b['null1_per10k'] <= 15
        out = ['control\tstat\tvalue', *(f'A\t{k}\t{v:.4g}' for k, v in a.items()), f"A\tgate\t{'PASS' if ga else 'FAIL'}",
               *(f'B\t{k}\t{v:.4g}' for k, v in b.items()), f"B\tgate\t{'PASS' if gb else 'FAIL'}"]
        print('\n'.join(out))
        if '--out' in sys.argv:
            open(sys.argv[sys.argv.index('--out') + 1], 'w', encoding='utf-8').write('\n'.join(out) + '\n')
        sys.exit(0)
    offline()
    print(f'decode_key alias: {len(fails)} failures' if fails else 'decode_key alias: all passed')
    sys.exit(1 if fails else 0)

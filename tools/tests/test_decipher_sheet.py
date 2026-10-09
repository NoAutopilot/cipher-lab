#!/usr/bin/env python3
"""Offline test for tools/decipher_sheet.py (MQS-SHEETS unit 3-4, 9 Oct 2026). Includes the REGRESSION tests R-K1 and R-K2
(they can fail only through a code bug: the value row is read back through decode_key's own functions and compared with
decode_key's own output; they are not known-answer controls) and, with --km, the box-to-token map test KM (slow; it classifies
every held-out tile). Never writes into the repository. Run: python3 tools/tests/test_decipher_sheet.py [--km]"""
import collections, html, json, os, re, shutil, sys, tempfile, types
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
os.chdir(ROOT)
import decipher_sheet as ds, decode_key, cvd_check

CFG = os.path.join(ROOT, 'tools', 'tests', 'decode_configs')
GRA = os.path.join(ROOT, 'ciphers', 'fr2980-gramont')
DAN = os.path.join(ROOT, 'ciphers', 'fr20140-danzay-1557')
BIR = os.path.join(ROOT, 'ciphers', 'nevers-birago-fr3251-1572')
TMP = tempfile.mkdtemp()
fails = 0
def t(ok, msg):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', msg)

def render(mode, target, out, *extra):
    argv = [mode, target, '--out', os.path.join(TMP, out)] + list(extra)
    rc = ds.main(argv)
    return rc, open(os.path.join(TMP, out), encoding='utf-8').read() if os.path.exists(os.path.join(TMP, out)) else ''

TOK = re.compile(r'<div class="tk[^"]*">(?:<img[^>]*>)?<div class="c">(.*?)</div><div class="v">(.*?)</div></div>', re.S)
def value_row(doc):
    return [(html.unescape(c), html.unescape(re.sub(r'<[^>]+>', '', v))) for c, v in TOK.findall(doc)]

def expected_plain(value, grade, null, code):
    s, g = ds.token_text(value, grade, null, code)
    return s + ds.GRADE_FORMS[g]['sup']

def sign_rows(target, config, jobname):
    ns = types.SimpleNamespace(config=config, ciphertext=None, key=None, exceptions=None, style=None, reading=None, tokens=None)
    job = ds.select_job(decode_key.load_config(target, ns), jobname)
    recs, key, ct = ds.graded(target, job)
    return [r for r in recs if r['kind'] == 'sign'], job

# 1. value row == decode_key's own rendering, token for token (Gramont f.29r, Danzay main letter)
for tgt, cfgname, job in ((GRA, 'fr2980-gramont.json', 'ciphertext.txt'), (DAN, 'fr20140-danzay-1557.json', 'ciphertext.txt')):
    cfg = os.path.join(CFG, cfgname)
    rc, doc = render('reading', tgt, 'v.html', '--config', cfg, '--job', job, '--tiles', 'none')
    rows, jobd = sign_rows(tgt, cfg, job)
    got = value_row(doc)
    exp = [(r.get('raw', r['sign']), expected_plain(r['value'], r['grade'], bool(r.get('null')), r['sign'])) for r in rows]
    t(got == exp and len(got) == len(rows), f'{os.path.basename(tgt)}: value row equals decode_key grading token for token ({len(got)}/{len(rows)})')
    # and against decode_key's own token table
    outs, cnt, ct = decode_key.run_job(tgt, jobd)
    tf = jobd.get('tokens', 'reading_tokens.tsv')
    hdr = outs[tf].split('\n')[0].split('\t')
    tr = [l.split('\t') for l in outs[tf].split('\n')[1:] if l and l.split('\t')[hdr.index('grade')] != 'clear']
    iv, ig = hdr.index('value'), hdr.index('grade')
    t([(x[iv], x[ig]) for x in tr] == [(r['value'], r['grade']) for r in rows], f'{os.path.basename(tgt)}: sign rows equal decode_key.run_job token table')

# 2. grade-to-form mapping for every grade letter
f = ds.GRADE_FORMS
t(ds.token_text('a', 'H')[0] == 'A' and f['H']['weight'] == 'bold' and f['H']['sup'] == 'H', 'H: bold capital, superscript H')
t(ds.token_text('a', 'C')[0] == 'A' and f['C']['weight'] == 'bold' and f['C']['sup'] == 'C', 'C: bold capital, superscript C')
t(ds.token_text('a', 'S')[0] == 'A' and f['S']['ul'] == 'solid' and f['S']['weight'] == 'normal', 'S: capital, solid underline')
t(ds.token_text('A', 'M')[0] == 'a?' and f['M']['ul'] == 'dashed', 'M: lower case, trailing ?, dashed underline')
t(ds.token_text('A', 'I')[0] == '[a]' and f['I']['style'] == 'italic' and f['I']['ul'] == 'dotted', 'I: lower case italic in brackets, dotted underline')
t(ds.token_text('?', 'U', code='x9')[0] == '<x9>' and f['U']['mono'], 'U: <code> in monospace')
t(ds.token_text('NULL', 'H', True)[0] == '·', 'NULL: middle dot')
sigs = {g: ds.form_signature(g) for g in f}
pairs = [(a, b) for a in sigs for b in sigs if a < b]
t(all(sigs[a] != sigs[b] for a, b in pairs), f'every pair of grade classes differs in a non-colour property ({len(pairs)} pairs)')

# 3. colour: sheets_light passes the gate, and the sheet's light CSS uses only its colours
t(cvd_check.check_palette('sheets_light')['code'] == 0, 'cvd_check passes sheets_light')
light = set(m.lower() for m in re.findall(r'#[0-9a-fA-F]{6}', ds.CSS.split('@media')[0]))
allowed = set(c.lower() for c in cvd_check.PALETTES['sheets_light']['marks'] + [cvd_check.PALETTES['sheets_light']['bg'], '#bbbbbb', '#F0E442', '#56B4E9', '#24211c'])
t(light <= allowed, f'light CSS colours are the declared palette ({sorted(light - allowed) or "none extra"})')
t('red' not in ds.CSS.lower() and 'green' not in ds.CSS.lower(), 'no red, no green in the CSS')

# 4. exemplar tile ids equal glyph_atlas.pick_spread's for the same inputs
import glyph_atlas as ga, numpy as np
atl = os.path.join(BIR, 'atlas')
st = [r for r in ds.load_tsv(os.path.join(atl, 'secure_tokens.tsv')) if r['grade'] in ('H', 'C', 'S')]
by = collections.defaultdict(list)
for r in st:
    by[r['code']].append(r['sid'])
got = ds.exemplar_ids(atl, by, 3)
signs = ga.read(atl, 'signs.tsv'); idx = {r['sid']: i for i, r in enumerate(signs)}
X = ga.feats(np.load(os.path.join(atl, 'bitmaps.npz'))['signs'], signs, pca_scale='shared')
want = {}
for c, sids in by.items():
    ids = [idx[s] for s in sids if s in idx]
    if len(ids) >= 2:
        want[c] = [signs[ids[k]]['sid'] for k in ga.pick_spread(X[ids], 3, True, 0.2)]
t(got == want and len(got) > 10, f'exemplar ids equal glyph_atlas.pick_spread for the same inputs ({len(got)} codes)')

# 5. --check fails after a one-byte change to key.tsv (scratch copy of Danzay)
d2 = os.path.join(TMP, 'dan'); os.makedirs(d2)
for fn in ('ciphertext.txt', 'ciphertext_f36.tsv', 'key.tsv'):
    shutil.copy(os.path.join(DAN, fn), d2)
cfg = os.path.join(CFG, 'fr20140-danzay-1557.json')
base = ['reading', d2, '--config', cfg, '--job', 'ciphertext.txt', '--tiles', 'none', '--out', os.path.join(TMP, 'chk.html')]
ds.main(base)
r0 = ds.main(base + ['--check'])
kt = open(os.path.join(d2, 'key.tsv'), encoding='utf-8').read()
lines = kt.split('\n')
i = next(n for n, l in enumerate(lines) if l and not l.startswith('#') and len(l.split('\t')) >= 3)
parts = lines[i].split('\t'); parts[2] = parts[2][:-1] + ('x' if parts[2][-1] != 'x' else 'y'); lines[i] = '\t'.join(parts)
open(os.path.join(d2, 'key.tsv'), 'w', encoding='utf-8').write('\n'.join(lines))
r1 = ds.main(base + ['--check'])
t(r0 == 0 and r1 == 1, f'--check exits 0 when current, 1 after a one-byte change to key.tsv ({r0}, {r1})')

# 6. footer carries the key source; header carries depth words and the novelty class
rc, doc = render('reading', GRA, 'f.html', '--config', os.path.join(CFG, 'fr2980-gramont.json'), '--job', 'ciphertext.txt',
                 '--result', 'BnF fr.2980 f.29r', '--tiles', 'none')
t('Tomokiyo' in doc and 'gallica.bnf.fr' in doc and 'Lasry, Biermann and Tomokiyo 2023' in doc, 'footer carries the key source, the image source and the layout credit')
t('partially deciphered (about 94%)' in doc and 'N4' in doc, 'header carries rule 4a depth words and the novelty class')
t(ds.depth_words(dict(depth='D1')) == 'fragments read' and ds.depth_words(dict(depth='D3', depth_pct='85.2')) == 'largely deciphered (about 85%)'
  and ds.depth_words(dict(depth='D4', depth_unread={'names_codes': '3'})) == 'deciphered; 3 name codes unidentified'
  and ds.depth_words(dict(depth='D0')) is None and ds.depth_words({}) is None, 'depth words D0-D4 (none at D0)')

# 7. no boxes (Danzay) with a line image, and f.178r on Birago (atlas boxes exist for other leaves only): the notice
from PIL import Image
white = Image.new('L', (200, 60), 255); white.save(os.path.join(TMP, 'blank.png'))
_ns = types.SimpleNamespace(config=cfg, ciphertext=None, key=None, exceptions=None, style=None, reading=None, tokens=None)
_recs = ds.graded(DAN, ds.select_job(decode_key.load_config(DAN, _ns), 'ciphertext.txt'))[0]
L1 = next(r['label'] for r in _recs if r['kind'] == 'line')
open(os.path.join(TMP, 'li.tsv'), 'w').write(f'line\timage\n{L1}\tblank.png\n')
rep = os.path.join(TMP, 'rep.tsv')
rc, doc = render('reading', DAN, 'nb.html', '--config', cfg, '--job', 'ciphertext.txt', '--line-images', os.path.join(TMP, 'li.tsv'), '--lines', L1, '--tile-report', rep)
t('not aligned to the image' in doc, 'no boxes + a line image: "token row not aligned to the image" notice present')
rows = open(rep).read().split('\n')[1:]
t(any('\tFalse\t' in r and r.startswith('line') for r in rows if r), '--tile-report flags the blank line crop (nonempty False)')
bs = ds.tile_stats(white)
t(not bs['nonempty'] and not bs['ink_ok'], 'tile_stats: blank crop is empty and fails the ink floor')
rc, doc = render('reading', BIR, 'f178r.html', '--job', 'f178r', '--lines', 'L01-L02')
t('not aligned to the image' in doc, 'Birago f.178r (no boxes in the map): "not aligned" notice present')

# 8. no brace is drawn from a key_conflicts-style count file
d3 = os.path.join(TMP, 'kc'); os.makedirs(d3)
open(os.path.join(d3, 'tokens.tsv'), 'w').write('line\tpos\tsign\tvalue\tgrade\nL1\t1\tx1\ta\tH\nL1\t2\tx2\tb\tM\n')
open(os.path.join(d3, 'key.tsv'), 'w').write('code\tvalue\tgrade\nx1\ta\tH\nx2\tb\tM\n')
open(os.path.join(d3, 'key_conflicts.tsv'), 'w').write('item\tcolumns_differing\nx1\t7\nx2\t3\n')
for mode in ('key', 'reading'):
    rc, doc = render(mode, d3, f'kc_{mode}.html', '--tokens-tsv', os.path.join(d3, 'tokens.tsv'), '--key-tsv', os.path.join(d3, 'key.tsv'))
    t('vice versa' not in doc and rc == 0, f'{mode} sheet with a key_conflicts-style count file draws no "or vice versa" brace')

# 9. RESTRICTED.md folder refused
d4 = os.path.join(TMP, 'res'); os.makedirs(d4); open(os.path.join(d4, 'RESTRICTED.md'), 'w').write('x')
try:
    ds.main(['key', d4, '--tokens-tsv', os.path.join(d3, 'tokens.tsv'), '--out', os.path.join(TMP, 'r.html')]); ok = False
except SystemExit as e:
    ok = 'restricted' in str(e)
t(ok, 'a folder carrying RESTRICTED.md is refused')

# R-K2 (regression): Gramont f.29r value row equals reading_tokens.tsv; swapping two key values changes exactly those codes' tokens
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(GRA, 'reading_tokens.tsv'), encoding='utf-8')]
h = rows[0]; body = [r for r in rows[1:] if len(r) >= len(h)]
cfg = os.path.join(CFG, 'fr2980-gramont.json')
rc, doc = render('reading', GRA, 'rk2.html', '--config', cfg, '--job', 'ciphertext.txt', '--tiles', 'none')
got = value_row(doc)
exp = [(r[h.index('sign')], expected_plain(r[h.index('value')], r[h.index('grade')], r[h.index('value')] in ('NULL', 'null'), r[h.index('sign')].rstrip('?'))) for r in body]
t(got == exp, f'R-K2 (regression): Gramont f.29r value row equals reading_tokens.tsv ({len(got)}/{len(exp)} tokens)')
g2 = os.path.join(TMP, 'gra'); os.makedirs(g2)
for fn in ('ciphertext.txt', 'key.tsv'):
    shutil.copy(os.path.join(GRA, fn), g2)
kl = open(os.path.join(g2, 'key.tsv'), encoding='utf-8').read().split('\n')
KH = kl[0].split('\t'); rowsk = [l.split('\t') for l in kl[1:] if l]
used = collections.Counter(r[h.index('sign')] for r in body if r[h.index('grade')] == 'H')
cand = [r for r in rowsk if r[0] in used and r[2] == 'H' and len(r[1]) == 1]
a_, b_ = next((x, y) for x in cand for y in cand if x[1].lower() != y[1].lower() and x[0] != y[0])
va, vb = a_[1], b_[1]
sw = []
for r in kl:
    p = r.split('\t')
    if p[0] == a_[0]: p[1] = vb
    elif p[0] == b_[0]: p[1] = va
    sw.append('\t'.join(p))
open(os.path.join(g2, 'key.tsv'), 'w', encoding='utf-8').write('\n'.join(sw))
rc, doc2 = render('reading', g2, 'rk2s.html', '--config', cfg, '--job', 'ciphertext.txt', '--tiles', 'none')
got2 = value_row(doc2)
diff = {n for n, (x, y) in enumerate(zip(got, got2)) if x != y}
want = {n for n, (c, _) in enumerate(got) if c.rstrip('?') in (a_[0], b_[0])}
t(len(got2) == len(got) and diff == want and want, f'R-K2: swapping the values of {a_[0]} and {b_[0]} changes exactly those codes\' {len(want)} tokens')

# R-K1 (regression): every tile on Birago no.87 is cut at the box atlas/no87_box_token.tsv assigns; the value row equals decode_key's
bx = ds.Boxes(os.path.join(BIR, 'atlas'), os.path.join(BIR, 'atlas', 'no87_box_token.tsv'))
ok_cut = n11 = 0
for job in ('f178v', 'f179r'):
    ns = types.SimpleNamespace(config=None, ciphertext=None, key=None, exceptions=None, style=None, reading=None, tokens=None)
    jb = ds.select_job(decode_key.load_config(BIR, ns), job)
    recs, key, ct = ds.graded(BIR, jb)
    for r in recs:
        if r['kind'] != 'sign':
            continue
        b = bx.token_box(r)
        if not b or len(b) != 1 or b[0][1] != '1:1':
            continue
        n11 += 1
        s = bx.signs[b[0][0]]
        g = bx.grey(s['page']); x, y, w, hh = (int(s[k]) for k in 'xywh')
        m, top = int(0.2 * max(w, hh)), int(0.6 * max(w, hh))
        ref = g[max(0, y - top):y + hh + m, max(0, x - m):x + w + m]
        ok_cut += bool((np.array(bx.cut([b[0][0]])) == ref).all()) and b[0][0] == next(
            m_['sid'] for m_ in bx.rows if m_['line'] == f"{r['folio']}_{r['line']}" and int(m_['pos']) == r['pos'] and m_.get('op', '1:1') == '1:1')
t(n11 > 600 and ok_cut == n11, f'R-K1 (regression): every 1:1 tile cut at the box the map assigns ({ok_cut}/{n11})')
rc, doc = render('reading', BIR, 'rk1.html', '--job', 'f178v', '--tile-report', os.path.join(TMP, 'rk1.tsv'))
ns = types.SimpleNamespace(config=None, ciphertext=None, key=None, exceptions=None, style=None, reading=None, tokens=None)
jb = ds.select_job(decode_key.load_config(BIR, ns), 'f178v')
recs, key, ct = ds.graded(BIR, jb)
exp = [(r.get('raw', r['sign']), expected_plain(r['value'], r['grade'], bool(r.get('null')), r['sign'])) for r in recs if r['kind'] == 'sign']
t(value_row(doc) == exp, f'R-K1 (regression): Birago no.87 f.178v value row equals decode_key reading ({len(exp)} tokens)')

shutil.rmtree(TMP)
if '--km' in sys.argv:
    import runpy
    sys.exit(runpy.run_path(os.path.join(ROOT, 'tools', 'tests', 'km_birago_map.py'))['main']() or (1 if fails else 0))
sys.exit(1 if fails else 0)

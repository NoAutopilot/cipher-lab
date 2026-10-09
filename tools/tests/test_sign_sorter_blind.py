#!/usr/bin/env python3
"""Offline test for the blind-first sorter (MQS-SORTER, 9 Oct 2026; TRANSCRIPTION.md: the person sorting is never shown key
values or machine guesses). Run: python3 tools/tests/test_sign_sorter_blind.py

Fixture: 40 signs with unique sentinel key values QZVAA..QZVBN (letters, since the lattice folds digits away), a top-k lattice over their sign ids, a focus file whose question and
note carry machine phrases. Must catch: a sentinel anywhere in the page, "(decode)", "top-1", "reader weight", a key-derived string in
a rank/focus field. Must NOT block: pile ids (shape cluster names), the rank order, the candidate piles in a "Which pile?" caption.
Positive control: the same lattice built NON-blind does carry "(decode)" and "reader weight" (so the checks above can fail)."""
import json, os, re, sys, tempfile, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import sign_sorter as ss
import sign_sorter_apply as sa
from PIL import Image, ImageDraw

fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok

with tempfile.TemporaryDirectory() as d:
    d = Path(d); (d / 'pages').mkdir()
    im = Image.new('L', (900, 100), 255); g = ImageDraw.Draw(im)
    rows, labs, key = [], [], ['sign\tvalue']
    for i in range(40):
        x = 10 + 21 * i
        g.line((x, 40, x + 15, 70), fill=0, width=2 + i % 3)
        rows.append(f's{i:02d}\tp1\t{x}\t40\t17\t31'); labs.append(f's{i:02d}\tT{i % 8:02d}\tT{i % 8:02d}')
        key.append(f'T{i:02d}\tQZV{chr(65 + i // 26)}{chr(65 + i % 26)}')
    im.save(d / 'pages' / 'p1.png')
    (d / 'signs.tsv').write_text('sid\tpage\tx\ty\tw\th\n' + '\n'.join(rows) + '\n')
    (d / 'labels.tsv').write_text('sid\tsign\tfamily\n' + '\n'.join(labs) + '\n')
    (d / 'key.tsv').write_text('\n'.join(key) + '\n')
    # top-k lattice (key_decode_lattice from-passes layout): line, pos, cand, score; sign ids are the cipher signs (piles)
    lat = ['line\tpos\tcand\tscore']
    for i in range(0, 40, 2):
        lat += [f'p1_00\t{i:02d}\tT{i % 8:02d}\t0.6', f'p1_00\t{i:02d}\tT{(i + 1) % 8:02d}\t0.4']
    (d / 'lat.tsv').write_text('\n'.join(lat) + '\n')
    (d / 'corpus.txt').write_text('qzv sera era bella e la terra era nera ' * 300)
    (d / 'focus.tsv').write_text('s00\tAbout as close to two of your piles; T00 or T01 (decode)?\ns02\tT02 (top-1) or T03; reader weight 40% on T03\n')
    note = "Each of these tiles is about as close to two of your piles; the computer's pick is a guess."
    out = d / 'blind.html'
    args = ['--signs', str(d / 'signs.tsv'), '--labels', str(d / 'labels.tsv'), '--pages', str(d / 'pages'), '--focus', str(d / 'focus.tsv'),
            '--focus-note', note, '--rank-lattice', str(d / 'lat.tsv'), '--rank-key', str(d / 'key.tsv'), '--rank-corpus', str(d / 'corpus.txt'),
            '--rank-sid', 's{pos:02d}', '--title', 'T', '--out', str(out), '--no-preflight']
    ss.main(args)
    html = out.read_text()
    data = json.loads(html.split('const DATA = ')[1].split(';\n')[0].replace('<\\/', '</'))
    strip = lambda h: re.sub(r'[A-Za-z0-9+/=]{200,}', '', h)   # tile/page images are base64: a 3-letter match there would be chance
    check('(1) no sentinel key value anywhere in the page or its DATA', not re.search(r'QZV[A-Z]{2}', strip(html)))
    check('(2) no "(decode)", "top-1" or "reader weight" string', not re.search(r'\(decode\)|top-1|reader weight', html, re.I))
    bad = [(k, r[k]) for r in data.get('rank', []) + data.get('focus', []) for k in ('value', 'alt', 'why', 'detail', 'q') if k in r and re.search(r'QZV[A-Z]{2}|decode|top-1|weight|letters change', str(r[k]))]
    check('(3) no per-tile value/alt/why/detail/q field holds a key-derived or machine string', not bad)
    check('blind flag, mode and seed note in DATA; no values map', data.get('blind') is True and data.get('mode') == 'blind' and 'values' not in data and data.get('seedNote'))
    check('must not block: pile ids and the rank order survive', data['rank'] and {p['id'] for p in data['piles']} == {f'T{i:02d}' for i in range(8)}
          and [r['score'] for r in data['rank']] == sorted((r['score'] for r in data['rank']), reverse=True))
    check('rank captions are "Which pile?" with candidate piles only', all(re.fullmatch(r'Which pile\? T\d\d( / T\d\d)?', r['why']) for r in data['rank']))
    check('focus note replaced by the neutral one', data['focusNote'] == ss.NEUTRAL_NOTE and "computer" not in data['focusNote'])
    check('focus questions lose their machine phrases', [f['q'] for f in data['focus']] == ['About as close to two of your piles; T00 or T01?', 'T02 or T03']
          or all('decode' not in f['q'] and 'top-1' not in f['q'] and 'weight' not in f['q'] for f in data['focus']))
    ss.main(args[:-3] + ['--blind-seed', '7', '--out', str(d / 'b7.html'), '--no-preflight'])
    d7 = json.loads((d / 'b7.html').read_text().split('const DATA = ')[1].split(';\n')[0].replace('<\\/', '</'))
    ss.main(args[:-3] + ['--out', str(d / 'b1.html'), '--no-preflight'])
    d1 = json.loads((d / 'b1.html').read_text().split('const DATA = ')[1].split(';\n')[0].replace('<\\/', '</'))
    check('candidate order is seeded: the same seed repeats', [r['why'] for r in data['rank']] == [r['why'] for r in d1['rank']])
    again = ss.blind_why('s00', ['T01', 'T00'], 7)
    check('blind_why deterministic and order-free in its input', again == ss.blind_why('s00', ['T00', 'T01'], 7) and 'decode' not in again)
    orders = {ss.blind_why(f's{i}', ['T00', 'T01'], 1) for i in range(40)}
    check('both candidate orders occur across tiles (no fixed "top-1 first")', orders == {'Which pile? T00 / T01', 'Which pile? T01 / T00'})
    # positive control: non-blind lattice ranking does carry the machine strings, so the checks above can fail
    dd = ss.build(str(d / 'signs.tsv'), str(d / 'labels.tsv'), str(d / 'pages'))
    rk, _ = ss.rank_from_lattice(dd, str(d / 'lat.tsv'), str(d / 'key.tsv'), corpus=[str(d / 'corpus.txt')], sid_fmt='s{pos:02d}')
    check('positive control: the legacy lattice rank shows "reader weight"', rk and any('reader weight' in r['detail'] for r in rk))
    # --- the declared non-blind mode and its guards ---
    fam = d / 'fam.tsv'
    fam.write_text('family\topen_blind_sorts\tnonblind_shown\tnote\nfamA\tSORT-1\t\t\nfamB\t\t\t\n')
    exp = d / 'export'; (exp / 'moves').mkdir(parents=True)
    check('refused: no key family', 'key-family' in (ss.nonblind_refusal(None, str(exp), {'s00'}, str(fam)) or ''))
    check('refused: no saved blind export', 'blind-sort' in (ss.nonblind_refusal('famB', None, {'s00'}, str(fam)) or ''))
    check('refused: empty export folder', 'holds no saved' in (ss.nonblind_refusal('famB', str(exp), {'s00'}, str(fam)) or ''))
    (exp / 'moves' / 'm1.json').write_text(json.dumps({'sid': 's00', 'to': 'T01', 'updated': '2026-10-08T10:00:00Z'}))
    check('refused: export of other tiles', 'same tiles' in (ss.nonblind_refusal('famB', str(exp), {'zz'}, str(fam)) or ''))
    check('refused: open blind sort in the same key family (TRANSCRIPTION.md named)', 'TRANSCRIPTION.md' in (ss.nonblind_refusal('famA', str(exp), {'s00'}, str(fam)) or ''))
    check('allowed: saved export of the same tiles, no open sort in the family', ss.nonblind_refusal('famB', str(exp), {'s00'}, str(fam)) is None)
    r = subprocess.run([sys.executable, str(ROOT / 'tools' / 'sign_sorter.py'), '--signs', str(d / 'signs.tsv'), '--labels', str(d / 'labels.tsv'),
                        '--pages', str(d / 'pages'), '--title', 'T', '--out', str(d / 'x.html'), '--show-values', str(d / 'key.tsv')],
                       capture_output=True, text=True)
    check('CLI --show-values without the guards: non-zero exit naming TRANSCRIPTION.md', r.returncode != 0 and 'TRANSCRIPTION.md' in r.stderr and not (d / 'x.html').exists())
    (d / 'key2.tsv').write_text('sign\tvalue\tstatus\nT00\tqzv\tconfirmed\nT01\tQzu\tguess\nT02\tNULL\t\nT03\tJ\t\nT04\tI\t\n')
    nb = d / 'nb.html'
    r = subprocess.run([sys.executable, str(ROOT / 'tools' / 'sign_sorter.py'), '--signs', str(d / 'signs.tsv'), '--labels', str(d / 'labels.tsv'),
                        '--pages', str(d / 'pages'), '--title', 'T', '--out', str(nb), '--show-values', str(d / 'key2.tsv'), '--key-family', 'famB',
                        '--blind-sort', str(exp), '--no-register', '--no-preflight'], capture_output=True, text=True)
    nd = json.loads(nb.read_text().split('const DATA = ')[1].split(';\n')[0].replace('<\\/', '</')) if nb.exists() else {}
    v = nd.get('values', {})
    check('non-blind page built with the banner and mode keyed', r.returncode == 0 and nd.get('mode') == 'keyed' and nd.get('banner') == ss.NONBLIND_BANNER and nd.get('blind') is False)
    check('values: CAPITALS confirmed, lower case guess, _ null, ? unknown', v.get('T00', {}).get('v') == 'QZV' and v.get('T01', {}).get('v') == 'qzu'
          and v.get('T02', {}).get('v') == '_' and v.get('T05', {}).get('v') == '?')
    check('group by value merges I/J', v['T03']['g'] == v['T04']['g'] == 'I' and ss.value_group('v') == 'U' and ss.value_group('_') == '_')
    # register stamp
    ss.stamp_nonblind('famB', str(fam), today='2026-10-09')
    ss.stamp_nonblind('famB', str(fam), today='2026-10-12')
    ss.stamp_nonblind('famC', str(fam), today='2026-10-10')
    rows_ = {x['family']: x for x in ss.read_families(str(fam))}
    check('register: first shown date kept, new family added', rows_['famB']['nonblind_shown'] == '2026-10-09' and rows_['famC']['nonblind_shown'] == '2026-10-10'
          and rows_['famA']['open_blind_sorts'] == 'SORT-1')
    # --- the mode column on exports ---
    check('export mode: blind page, no family', sa.export_mode(None, None, None, str(fam)) == 'blind')
    check('export mode: keyed page', sa.export_mode('keyed', None, None, str(fam)) == 'keyed')
    check('export mode: family shown before the sort began is keyed', sa.export_mode('blind', 'famB', '2026-10-10', str(fam)) == 'keyed')
    check('export mode: must not block a sort that began before the family was shown', sa.export_mode('blind', 'famB', '2026-10-08', str(fam)) == 'blind')
    check('export mode: family never shown stays blind', sa.export_mode('blind', 'famA', '2026-10-10', str(fam)) == 'blind')
    adb = d / 'adb'; (adb / 'moves').mkdir(parents=True); (adb / 'moves' / 'a.json').write_text(json.dumps({'sid': 's00', 'to': 'T01', 'updated': '2026-10-11T00:00:00Z'}))
    sa.main(['--labels', str(d / 'labels.tsv'), '--db', str(adb), '--out', str(d / 'set.tsv'), '--page', str(nb)])
    lines = (d / 'set.tsv').read_text().splitlines()
    check('apply writes a mode column: keyed from a non-blind page', lines[0].endswith('\tmode') and all(l.endswith('\tkeyed') for l in lines[1:]))
    sa.main(['--labels', str(d / 'labels.tsv'), '--db', str(adb), '--out', str(d / 'set2.tsv'), '--page', str(out)])
    check('apply writes mode blind for a blind page', all(l.endswith('\tblind') for l in (d / 'set2.tsv').read_text().splitlines()[1:]))
    check('docstring says a keyed row is never BENCHMARK-TX or adjudication evidence', 'never used as BENCHMARK-TX evidence' in sa.__doc__)
    # --- Unit 2: sorting piles (size / name / mark category in every mode, value only non-blind) ---
    (d / 'marks.tsv').write_text('x\ty\tw\th\tsid\tkind\n10\t10\t3\t3\ts00\tdotted\n31\t10\t3\t3\ts01\thooked\n52\t10\t3\t3\ts08\tdotted\n')
    dm = ss.build(str(d / 'signs.tsv'), str(d / 'labels.tsv'), str(d / 'pages'), str(d / 'marks.tsv')); ss.mark_categories(dm, str(d / 'marks.tsv'))
    check('mark category per pile: commonest kind, plain when none', dm['markCat']['T00'] == 'dotted' and dm['markCat']['T01'] == 'hooked' and dm['markCat']['T05'] == 'plain')
    tpl = (ROOT / 'tools' / 'sign_sorter' / 'template.html').read_text()
    check('template: sort piles by size and by name always; mark and value options added only when the data has them',
          'id="psort"' in tpl and 'By size' in tpl and "o.value = 'mark'" in tpl and "if (DATA.nonblind){ const o" in tpl and 'CTTS' in tpl and 'Lasry' in tpl)
    check('template: the score is hidden on a blind page, group by value only non-blind', "DATA.blind ? ''" in tpl and "$('gbvL').hidden = false" in tpl)
print('FAILED' if fails else 'ALL PASS'); sys.exit(1 if fails else 0)

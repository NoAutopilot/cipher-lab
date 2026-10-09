#!/usr/bin/env python3
"""MQS-NAMES control (a): Lodewijk van Nassau 1573-74 name codes, leave one out, under tools/name_candidates.py.
Pre-registered in tools/tests/PREREG-MQS-NAMES.md (pushed before step 'score' ran).

  python3 tools/tests/mqs_names_control_a.py freeze     # build + freeze one pool per held-out code (no scoring)
  python3 tools/tests/mqs_names_control_a.py score      # score from the frozen pools; writes control_a.tsv + .json

Contexts: the folders' own decode configs through decode_key.graded_recs (5549 PS via jan-van-nassau-1572-75/
decode_5549ps_full.json, 5797 via decode_5797_full.json, 5810 via decode_wv2.json) and 5550 from
jan-van-nassau-1572-75/j5s/ciphertext_5550.tsv: the leaf's clear frame (left/right columns) around each run, the run's
tokens decoded under key_full.tsv; the 'gloss' and 'conf' columns are never read (the gloss is the answer).
Masking (brief): for each held-out code every letter carrying it is masked -- no Groen text of that letter in --index
or co-mention; the tool never reads decipherment_/plaintext_/reading files or AX-GLOSS rows."""
import csv, json, os, random, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import decode_key  # noqa: E402
import name_candidates as nc  # noqa: E402

LOD = os.path.join(ROOT, 'ciphers', 'lodewijk-van-nassau-1573-74')
JAN = os.path.join(ROOT, 'ciphers', 'jan-van-nassau-1572-75')
OUT = os.path.join(ROOT, 'tools', 'tests', 'fixtures', 'name_candidates', 'lodewijk')
CONFIGS = [os.path.join(JAN, 'decode_5549ps_full.json'), os.path.join(LOD, 'decode_5797_full.json'),
           os.path.join(LOD, 'decode_wv2.json')]
# Groen IV letters on disk -> WVO letter (NOTES.md: CDIX 5799, CDXXIII 5801, CDXXVII 4611, CDXXXIII 4497, CDXLIV 5797,
# CDLXVIII 5810, CDLXXXIII 5811, CDLXXXIV 4503); Groen Suppl. Lettre 45* = 5549.
INDEX = [('ciphers/lodewijk-van-nassau-1573-74/groen/groen_IV_CDIX.txt', '5799', '1573-04-03'),
         ('ciphers/lodewijk-van-nassau-1573-74/groen/groen_IV_CDXXIII.txt', '5801', '1573'),
         ('ciphers/lodewijk-van-nassau-1573-74/groen/groen_IV_CDXXVII.txt', '4611', '1573'),
         ('ciphers/lodewijk-van-nassau-1573-74/groen/groen_IV_CDXXXIII.txt', '4497', '1573'),
         ('ciphers/lodewijk-van-nassau-1573-74/groen/groen_IV_CDXLIV.txt', '5797', '1573-10-22'),
         ('ciphers/lodewijk-van-nassau-1573-74/groen/groen_IV_CDLXVIII.txt', '5810', '1574-01-06'),
         ('ciphers/lodewijk-van-nassau-1573-74/groen/groen_IV_CDLXXXIII.txt', '5811', '1574-04-13'),
         ('ciphers/lodewijk-van-nassau-1573-74/groen/groen_IV_CDLXXXIV.txt', '4503', '1574-04-15'),
         ('ciphers/jan-van-nassau-1572-75/groen/gpas_lettre45.txt', '5549', '1573-11-21')]
# held-out codes: class, language, sender, recipient, date of the letter(s), truth aliases (pre-registered)
CODES = {
    '202': ('place', 'de', 'Jan van Nassau', 'Willem van Oranje', '1573-12-25',
            'franckreich|frankreich|france|frankrijk|francia|franckrych'),
    '223': ('place', 'fr', 'Willem van Oranje', 'Lodewijk van Nassau', '1574-01-06', 'harlem|haarlem'),
    '153': ('person2', 'de', 'Jan van Nassau', 'Willem van Oranje', '1573-12-25',
            'pfaltzgraf|pfalzgraf|palsgrave|elector palatine|electeur palatin|kurfurst von der pfalz|keurvorst van de palts'),
    '154': ('n1', 'de', 'Lodewijk van Nassau', 'Willem van Oranje', '1573-10-22',
            'herzog von sachsen|duc de saxe|elector of saxony|kurfurst von sachsen|augustus, elector of saxony'),
    '161': ('n1', 'de', 'Jan van Nassau', 'Willem van Oranje', '1573-12-25',
            'landgraf|landgrave|lantgrave|landgraaf'),
    '200': ('n1', 'de', 'Lodewijk van Nassau', 'Willem van Oranje', '1573-10-22',
            "herzog von alba|duc d'albe|duke of alba|duque de alba|hertog van alva|fernando alvarez de toledo"),
    '241': ('n1', 'fr', 'Willem van Oranje', 'Lodewijk van Nassau', '1574-01-06', 'zeelande|zeeland|zelande|zealand'),
    '171': ('trivial', 'de', 'Jan van Nassau', 'Willem van Oranje', '1573-12-25',
            "prinz zu oranien|prince d'orange|william the silent|willem van oranje|guillaume d'orange"),
}


def key_full():
    return decode_key.load_keys(LOD, 'key_full.tsv')


def ctx_5550(hide):
    """Contexts of every code in 5550 runs: clear frame + decoded run; codes in `hide` shown as <code>."""
    key = key_full()
    runs = {}
    for r in csv.DictReader(open(os.path.join(JAN, 'j5s', 'ciphertext_5550.tsv'), encoding='utf-8'), delimiter='\t'):
        runs.setdefault(r['run'], []).append(r)
    rows = []
    for run, toks in runs.items():
        lf = next((t['left'] for t in toks if t['left']), '')
        rf = next((t['right'] for t in reversed(toks) if t['right']), '')

        def rd(t, own):
            s = t['token']
            if s == own or s in hide:
                return f' <{s}> '
            row = key.get(s)
            v = row['value'] if row else None
            if v in ('NULL',):
                return ''
            if v in (None, '', '?'):
                return f' <{s}> '
            v = v.lstrip('=')
            return f' {v} ' if len(v) >= 2 else v
        for i, t in enumerate(toks):
            if not re.fullmatch(r'\d+', t['token']):
                continue
            own = t['token']
            left = lf + ' ' + ''.join(rd(x, own) for x in toks[:i])
            right = ''.join(rd(x, own) for x in toks[i + 1:]) + ' ' + rf
            rows.append(dict(code=own, letter='5550', date='1573-12-25', line=run, pos=t['pos'],
                             left=re.sub(r'\s+', ' ', left).strip(), right=re.sub(r'\s+', ' ', right).strip()))
    return rows


def write_inputs(code):
    os.makedirs(OUT, exist_ok=True)
    cp = os.path.join(OUT, f'ctx_5550_hide{code}.tsv')
    with open(cp, 'w', encoding='utf-8') as f:
        cols = ['code', 'letter', 'date', 'line', 'pos', 'left', 'right']
        f.write('\t'.join(cols) + '\n')
        for r in ctx_5550({code}):
            f.write('\t'.join(str(r[c]).replace('\t', ' ') for c in cols) + '\n')
    ip = os.path.join(OUT, 'index_manifest.tsv')
    with open(ip, 'w', encoding='utf-8') as f:
        f.write('path\tletters\tdate\n')
        for p, l, d in INDEX:
            f.write(f'{p}\t{l}\t{d}\n')
    return cp, ip


def letters_carrying(code):
    """Every letter whose decoded tokens carry the code (configs + 5550)."""
    out = set()
    for cfg in CONFIGS:
        for x in nc.contexts_from_config(LOD, cfg, code):
            out.add(x['letter'])  # (letters, so window crossing does not matter here)
    if any(r['code'] == code for r in ctx_5550(set())):
        out.add('5550')
    return out


def args_for(code, extra=()):
    cls, lang, snd, rcp, date, truth = CODES[code]
    cp, ip = write_inputs(code)
    mask = sorted(letters_carrying(code))
    argv = [LOD, '--code', code, '--sender', snd, '--recipient', rcp, '--date', date, '--lang', lang,
            '--contexts', cp, '--index', ip, '--mask-letters', ','.join(mask), '--truth', truth, '--same-line']
    for c in CONFIGS:
        argv += ['--config', c]
    return argv + list(extra), mask


def freeze(wikidata=False, offline=True):
    res = {}
    for code in CODES:
        argv, mask = args_for(code, ['--freeze-pool', os.path.join(OUT, f'pool_{code}.tsv'), '--freeze-only'] +
                              (['--wikidata'] + (['--offline'] if offline else []) if wikidata else []))
        a = nc.parser().parse_args(argv)
        r = nc.run(a)
        res[code] = dict(sha256=r['pool_sha'], pool=r['pool'], mask=mask)
        print(code, r['pool'], r['pool_sha'], 'mask', ','.join(mask))
    json.dump(res, open(os.path.join(OUT, 'pools.json'), 'w'), indent=1)


def score(nulls=200):
    out, rows = {}, []
    for code, (cls, *_rest) in CODES.items():
        argv, mask = args_for(code, ['--pool', os.path.join(OUT, f'pool_{code}.tsv'), '--nulls', str(nulls),
                                     '--out', os.path.join(OUT, f'candidates_{code}.tsv'), '--top', '15'])
        r = nc.run(nc.parser().parse_args(argv))
        s = r['summary']
        s['class'] = cls
        s['contexts'] = [f'{x["letter"]} {x["line"]}: {x["left"][-40:]} [{code}] {x["right"][:40]}' for x in r['contexts']]
        out[code] = s
        cn = s['context_null'] or {}
        rows.append([code, cls, s['n_contexts'], s['pool'], s['coverage'], s['truth_rank'], s['truth_score'],
                     cn.get('p95_score'), s['beats_null_p95'], (s['decoy_null'] or {}).get('decoy_beat_share'),
                     s['truth_label'], ' | '.join(s['top'][:5])])
    # power check: each n>=2 code cut to one random context, 20 draws
    power = {}
    for code in [c for c, v in CODES.items() if v[0] in ('place', 'person2')]:
        hits = []
        for seed in range(20):
            argv, _ = args_for(code, ['--pool', os.path.join(OUT, f'pool_{code}.tsv'), '--nulls', '0',
                                      '--subsample', '1', '--seed', str(seed)])
            s = nc.run(nc.parser().parse_args(argv))['summary']
            hits.append(bool(s['truth_rank'] and s['truth_rank'] <= 5))
        power[code] = sum(hits) / len(hits)
    out['_power_top5_share_n1'] = power
    json.dump(out, open(os.path.join(OUT, 'control_a.json'), 'w'), indent=1, ensure_ascii=False)
    with open(os.path.join(OUT, 'control_a.tsv'), 'w', encoding='utf-8') as f:
        f.write('code\tclass\tn_contexts\tpool\tcoverage\ttruth_rank\ttruth_score\tnull_p95\tbeats_p95\t'
                'decoy_beat_share\ttruth_label\ttop5\n')
        for r in rows:
            f.write('\t'.join(str(x) for x in r) + '\n')
    for r in rows:
        print('\t'.join(str(x) for x in r))
    print('power (top-5 share at one context, 20 draws):', power)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'freeze':
        freeze(wikidata='--wikidata' in sys.argv, offline='--online' not in sys.argv)
    elif cmd == 'score':
        score()
    else:
        print(__doc__)

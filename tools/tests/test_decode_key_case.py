#!/usr/bin/env python3
"""Offline test for decode_key.py --style case (MQS-SHEETS unit 2, 9 Oct 2026). Re-renders every job of the Danzay and
Gramont test configs in the 'case' style and checks token by token against the job's own token table: folded value
equal, case equal to the grade (H/C/S capitals, M lower, I [lower], U <code>, NULL _), clear words {word}, and that
the existing styles' output is unchanged. Run: python3 tools/tests/test_decode_key_case.py"""
import copy, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import decode_key

CFG = os.path.join(ROOT, 'tools', 'tests', 'decode_configs')
fails = 0
def t(ok, msg):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', msg)

def body(reading):
    return [l for l in reading.split('\n') if l and not l.startswith('#')]

for name in ('fr20140-danzay-1557.json', 'fr2980-gramont.json'):
    cfg = json.load(open(os.path.join(CFG, name)))
    target = os.path.join(ROOT, cfg['target'])
    for job in cfg['jobs']:
        job = dict(cfg.get('defaults', {}), **job)
        outs0, cnt0, _ = decode_key.run_job(target, job)
        cj = copy.deepcopy(job); cj['style'] = 'case'
        outs, cnt, ct = decode_key.run_job(target, cj)
        rd, tk = cj.get('reading', 'reading.txt'), cj.get('tokens', 'reading_tokens.tsv')
        t(outs[tk] == outs0[tk] and cnt == cnt0, f'{cfg["target"]} {ct}: token table and grade counts unchanged by style')
        hdr = outs[tk].split('\n')[0].split('\t')
        iv, ig = hdr.index('value'), hdr.index('grade')
        allrows = [l.split('\t') for l in outs[tk].split('\n')[1:] if l]
        rows = [r for r in allrows if r[ig] != 'clear']  # clear-hand rows (include_clear) are not sign tokens
        nclear = len(allrows) - len(rows)
        toks = []
        for l in body(outs[rd]):
            toks += re.findall(r'\{[^}]*\}|\S+', l.split('\t', 1)[1])
        signs = [x for x in toks if not (x.startswith('{') and x.endswith('}'))]
        if nclear:
            t(len(toks) - len(signs) == nclear, f'{ct}: {nclear} clear-hand words shown as {{word}}')
        # a multi-word value (a word code such as 'le roy') is shown as its words; consume that many tokens per row
        pos, bad, used = 0, 0, 0
        for row in rows:
            val, g = row[iv].lstrip('='), row[ig]
            n = 1 if (row[iv] in cj.get('null_values', ['NULL', 'null']) or g == 'U') else max(1, len(val.split()))
            tok = ' '.join(signs[pos:pos + n]); pos += n
            if row[iv] in cj.get('null_values', ['NULL', 'null']):
                ok = tok == '_'
            elif g == 'U':
                ok = tok.startswith('<') and tok.endswith('>')
            elif g == 'I':
                ok = tok == '[' + val.lower() + ']'
            elif g in 'HCS':
                ok = tok == val.upper()
            else:  # M
                ok = tok == val.lower()
            bad += not ok
        t(pos == len(signs), f'{ct}: every case token consumed by a sign row ({pos}/{len(signs)})')
        t(bad == 0, f'{ct}: folded value and grade-to-case agree on every token ({len(rows) - bad}/{len(rows)})')
        grades = {g: sum(1 for r in rows if r[ig] == g) for g in 'HCSMIU'}
        print('     grades', grades)
        ob = decode_key.run_job(target, job)[0]
        t(ob == outs0, f'{ct}: existing style output unchanged')

# synthetic: every grade letter, a clear word, a null, an I-graded exception (decoded through the shared loop)
recs = [dict(kind='line', label='L1', folio='', line='L1'),
        dict(kind='sign', label='L1', sign='1', value='a', grade='H', null=False),
        dict(kind='sign', label='L1', sign='2', value='b', grade='C', null=False),
        dict(kind='sign', label='L1', sign='3', value='c', grade='S', null=False),
        dict(kind='sign', label='L1', sign='4', value='d', grade='M', null=False),
        dict(kind='sign', label='L1', sign='5', value='E', grade='I', null=False),
        dict(kind='sign', label='L1', sign='6', value='?', grade='U', null=False),
        dict(kind='sign', label='L1', sign='7', value='NULL', grade='H', null=True),
        dict(kind='clear', label='L1', raw='w:nous', value='nous', grade='clear')]
out = decode_key.render_case(recs, {})
t(out == ['L1\tA B C d [e] <6> _ {nous}'], 'every grade letter: ' + out[0].replace('\t', ' | '))
t(decode_key.STYLES['case'] is decode_key.render_case, "'case' registered in STYLES")
sys.exit(1 if fails else 0)

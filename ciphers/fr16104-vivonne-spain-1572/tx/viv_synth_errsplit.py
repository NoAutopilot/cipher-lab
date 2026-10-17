#!/usr/bin/env python3
"""VIV-SYNTH (17 Oct 2026): split pass A's err_true on the Vivonne known-answer leaves by truth-flag class.

tools/tx_bench.py --exclude-flagged drops every flagged row. On these items the flags mix two different things:
  clerk-*       the known text itself is doubtful (the clerk's decipherment was read differently by two blind readers)
  align-*/other the committed reference sign decodes to a different letter than the clerk's -- a reader error OR a one-letter
                alignment shift. Excluding these is circular for any output close to the reference (the committed output
                scores 0.000 there by construction).
This script re-runs tx_bench with only one class treated as flagged, so the two shares can be read apart. Report only;
it writes nothing. Usage: python3 ciphers/fr16104-vivonne-spain-1572/tx/viv_synth_errsplit.py   (run from the repo root)
"""
import contextlib, importlib.util, io, re, sys

ITEMS = ['vivonne1573-f102r-dev2', 'vivonne1573-f103r-confirm2', 'vivonne1573-f201r-dev', 'vivonne1573-f201r-dev-3',
         'vivonne1573-f201v-dev-3', 'vivonne1573-f202r-dev', 'vivonne1573-f211r-dev', 'vivonne1573-f211v-dev']
spec = importlib.util.spec_from_file_location('txb', 'tools/tx_bench.py')
txb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(txb)
RX = re.compile(r'err_true\(0.75-indel align\) ([0-9.]+ \(\d+/\d+\))')


def flagger(mode):
    def f(r):
        fl = (r.get('flag') or '').strip()
        if not fl or fl.startswith('corrected'):
            return False
        parts = fl.split(',')
        clerk = any(p.startswith('clerk') for p in parts)
        other = any(not p.startswith('clerk') for p in parts)
        return clerk if mode == 'clerk' else other
    return f


def run(item, out, mode):
    txb.is_flagged = flagger(mode)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        txb.main(['--item', item, '--exclude-flagged', out])
    m = RX.findall(buf.getvalue())
    return m[0], m[1]


print('item\toutput\tas_measured\texcl_clerk_only\texcl_align_only')
for it in ITEMS:
    for p in ('passA', 'passB'):
        out = 'benchmark-tx/outputs/%s/%s.tsv' % (it, p)
        am, c = run(it, out, 'clerk')
        _, a = run(it, out, 'align')
        print('\t'.join((it, p, am, c, a)))

#!/usr/bin/env python3
"""BRO-178 (9 Oct 2026): settle bro178/ciphertext_draft.tsv (reconcile_passes.py --keep-plain of bro178/passA, passB)
into body178_ciphertext.tsv. Settlements made by the worker from images/crops_m0178_b178 and the full leaf, before
any score (PREREG-BRO178.md). `--check` exits 1 if body178_ciphertext.tsv is stale (rule 7).
"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
SETTLE = {
    # (line, pos): (token, conf, reason)
    ('m0178_L01-1', '14'): ('7', 'M', "A '2?' / B 'Z?': the barred-7 glyph (top bar, diagonal, mid crossbar), not a loop 2; "
                                      "folder convention PX-BROGLYPH -> 7"),
    ('m0178_L02-1', '6'): ('55', 'M', "A '11?' / B 'ss?': the 55/11 glyph (one glyph here, both p in key.tsv; BRO-123 note); "
                                      "written as 55"),
    ('m0178_L02-1', '9'): ('57', 'M', "both '57?': first stroke has the same s-like form as the 5s of '55'; kept as read, no key row"),
}
rows = list(csv.DictReader(open(HERE / 'bro178/ciphertext_draft.tsv'), delimiter='\t'))
lk = 'line' if 'line' in rows[0] else list(rows[0])[0]
out = ['line\tpos\ttoken\tconf\tnote\n']
for r in rows:
    k = (r[lk], r['position'])
    tok, conf, note = r['sign'].rstrip('?'), r.get('confidence') or 'H', 'passA=passB' if r.get('why','').startswith('agree') else r.get('why','')
    if k in SETTLE:
        tok, conf, note = SETTLE[k]
    out.append(f'{r[lk]}\t{r["position"]}\t{tok}\t{conf}\t{note}\n')
text = ''.join(out)
p = HERE / 'body178_ciphertext.tsv'
if '--check' in sys.argv:
    ok = p.exists() and p.read_text() == text
    print(p.name, 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
p.write_text(text); print(f'wrote {p.name}: {len(out)-1} tokens')

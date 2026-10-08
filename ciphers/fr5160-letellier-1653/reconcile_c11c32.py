#!/usr/bin/env python3
"""Canvas 11-12 second cipher block (2 Jan 1653 letter) and canvas 32 (full-page 1653 letter): reconciled ciphertext.

    python3 reconcile_c11c32.py           write ciphertext_c11.tsv, ciphertext_c32.tsv
    python3 reconcile_c11c32.py --check   exit 1 if either committed file differs from what this script writes

TEXT-LEVEL reconciliation (D4-F5160B, 8 Oct 2026): the native crops of canvases 11, 12 and 32 were never committed
(30 MB folder cap) and Gallica answered HTTP 503 to the first region re-fetch at 09:2x UTC 8 Oct 2026, so per the brief
the fetch was stopped and nothing here was settled against the image. The passes are aligned with
tools/reconcile_passes.py (Needleman-Wunsch); every position the two blind passes read alike keeps their joint
confidence, and every disagreement is written at confidence M with the other pass's reading in `alt`. The only
settlements made without the image are shape-description matches: pass B declined to name two signs and described
them instead ("cursive open hook, like ⊃" / "looped ascender flourish resembling cursive H/&"); where that description
sits at the position pass A labels Ɔ / db, both passes saw the same shape, and the token takes pass A's label at M
(the shape is agreed; whether 'db' here is the established tt+looped-d sign is not). Clear French is kept as a
[PLAIN:...] row (a run break for trial_1653.py), pass B's wording with pass A's in `alt` where they differ.
Scribal dots are dropped (reconcile_passes default), as in ciphertext_f1/f9.
"""
import csv, io, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '..', '..', 'tools', 'reconcile_passes.py')
JOBS = {'ciphertext_c11.tsv': ('passA_f11.tsv', 'passB_f11.tsv'),
        'ciphertext_c32.tsv': ('passA_c32.tsv', 'passB_c32.tsv')}
DESC = '?'   # a pass-B shape description in place of a sign label


def load(fn):
    """-> (sign rows for reconcile_passes, {line: [(where, text)]} clear phrases, {line: [descriptions]})"""
    rows = list(csv.reader(open(os.path.join(HERE, fn), encoding='utf-8'), delimiter='\t'))
    signs, clear, desc, seen = [], {}, {}, {}
    for r in rows[1:]:
        if len(r) < 3:
            continue
        line, pos, g = r[0], r[1], r[2].strip()
        conf = r[3].split(' - ')[0].strip() if len(r) > 3 else ''
        is_clear = g.startswith('[') and (pos == 'clear' or conf == 'C' or 'c32' in fn)
        if is_clear:
            clear.setdefault(line, []).append(('pre' if not seen.get(line) else 'post', g.strip('[]')))
            continue
        if g.startswith('['):
            desc.setdefault(line, []).append(g.strip('[]'))
            g = DESC
        seen[line] = seen.get(line, 0) + 1
        signs.append([line, str(seen[line]), g, conf])
    return signs, clear, desc


def draft(a_rows, b_rows):
    with tempfile.TemporaryDirectory() as d:
        for n, rows in (('A.tsv', a_rows), ('B.tsv', b_rows)):
            with open(os.path.join(d, n), 'w', encoding='utf-8') as f:
                csv.writer(f, delimiter='\t', lineterminator='\n').writerows([['line', 'pos', 'group', 'conf']] + rows)
        subprocess.run([sys.executable, TOOL, os.path.join(d, 'A.tsv'), os.path.join(d, 'B.tsv'), '--out-dir', d],
                       check=True, capture_output=True)
        return list(csv.DictReader(open(os.path.join(d, 'ciphertext_draft.tsv'), encoding='utf-8'), delimiter='\t'))


def settle(r):
    """one draft row -> (token, conf, alt, note) or None to drop"""
    s, c, alt, why = r['sign'], r['confidence'], r['alt'], r['why']
    if why.startswith('agree'):
        if s == DESC:
            return None
        return s, ('H' if c == 'H' else 'M'), '', 'both passes'
    other = alt.split(':', 1)[1] if ':' in alt else alt
    if why == 'gap':
        if alt.startswith('A:'):           # pass B only
            if s in ('', DESC):            # B described a shape A did not read as a sign
                return ('Ɔ', 'M', '', 'pass B only: "cursive open hook"; pass A no sign here') \
                    if r['line'] == 'f12_L1' else None
            return s, 'M', '', 'pass B only'
        return s, 'M', '', 'pass A only'
    if other == '' and s == 'Ɔ':
        return s, 'M', '', 'shape agreed: B "cursive open hook, like ⊃" (no label); Ɔ is pass A\'s label'
    if other == '' and s == 'db':
        return s, 'M', 'new sign', 'shape agreed: B "looped ascender flourish, cursive H/&"; identity with db unsettled'
    if {s, other} == {'db', 'tt'}:
        return s, 'M', other, 'loop+cross sign: A db, B tt; image not re-read'
    return s, 'M', other, 'passes differ; image not re-read'


def render():
    out = {}
    for fn, (pa, pb) in JOBS.items():
        a, ca, _ = load(pa)
        b, cb, _ = load(pb)
        rows = draft(a, b)
        by_line = {}
        for r in rows:
            by_line.setdefault(r['line'], []).append(r)
        raw = [r[0] for f in (pa, pb) for r in list(csv.reader(open(os.path.join(HERE, f), encoding='utf-8'),
                                                                 delimiter='\t'))[1:] if r]
        lines = list(dict.fromkeys(raw))
        buf = io.StringIO(); w = csv.writer(buf, delimiter='\t', lineterminator='\n')
        w.writerow(['line', 'pos', 'token', 'conf', 'alt', 'note'])
        for ln in lines:
            pa_c, pb_c = ca.get(ln, []), cb.get(ln, [])
            items = []
            for where in ('pre', 'post'):
                ta = [t for wh, t in pa_c if wh == where]
                tb = [t for wh, t in pb_c if wh == where]
                for i in range(max(len(ta), len(tb))):
                    x, y = (ta[i] if i < len(ta) else ''), (tb[i] if i < len(tb) else '')
                    txt = y or x
                    items.append((where, ['[PLAIN:%s]' % txt, 'H' if x == y else 'M',
                                          '' if x == y else x, 'clear French']))
            body = [settle(r) for r in by_line.get(ln, [])]
            body = [list(t) for t in body if t]
            seq = [i[1] for i in items if i[0] == 'pre'] + body + [i[1] for i in items if i[0] == 'post']
            for k, t in enumerate(seq, 1):
                w.writerow([ln, k] + t)
        out[fn] = buf.getvalue()
    return out


def main():
    files = render()
    if '--check' in sys.argv:
        stale = [f for f, s in files.items() if not os.path.exists(os.path.join(HERE, f))
                 or open(os.path.join(HERE, f), encoding='utf-8').read() != s]
        if stale:
            print('stale: ' + ', '.join(stale)); sys.exit(1)
        print('ok: ' + ', '.join(sorted(files))); return
    for f, s in files.items():
        open(os.path.join(HERE, f), 'w', encoding='utf-8').write(s)
        rows = list(csv.DictReader(io.StringIO(s), delimiter='\t'))
        sg = [r for r in rows if not r['token'].startswith('[PLAIN')]
        print('%s: %d signs, H %d, M %d, with alt %d' % (f, len(sg), sum(r['conf'] == 'H' for r in sg),
              sum(r['conf'] == 'M' for r in sg), sum(bool(r['alt']) for r in sg)))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""no.37 f.60r dense cipher blocks (L06-L14, L25-L30): merge the blind passes, segment the digit stream into key codes.

GAPS-fr4715-vieuville-pool-4, 2 Oct 2026. Disk only.

    python3 scripts/f60r_blocks.py merge            # witness/f60r_blocks_pass{A,B}_b*.tsv -> witness/f60r_blocks_pass{A,B}_long.tsv
    python3 tools/reconcile_passes.py witness/f60r_blocks_passA_long.tsv witness/f60r_blocks_passB_long.tsv \
            --out-dir witness/f60r_blocks_rec --keep-dots --keep-plain
    python3 scripts/f60r_blocks.py segment          # reconciled draft (+ witness/f60r_blocks_settled.tsv) -> f60r_blocks_ciphertext.tsv
    python3 scripts/f60r_blocks.py segcontrol       # the same segmenter on no.58's Tomokiyo dump with its grouping removed

Pass notation (scratch prompt, kept in NOTES.md): digits as written, '.' before a dotted digit, [..] barred digits,
S / X the two key glyphs, ? illegible, (a/b) unsure between two readings (first kept, unit flagged), {words} clear text.
Units after parsing: 'd' digit, '.d' dotted digit, '=d' barred digit, 'S', 'X', '?', 'w:word'.

Each crop overlaps its right neighbour by about 180 px at 3x (60 px native, three or four digits); merge drops the
longest suffix/prefix overlap (2..8 units, at most one mismatch) before appending the next segment.

The 8 rule (GAPS-4): both passes read this scribe's 8 as 0 (no 8 in 1,500 digits; no.58's MONT-4715 confusion matrix
already lists 8->0); an out-of-key pair 0x whose 8x is a key code is emitted as 8x with the marker '8<' (segment
strips the marker and lowers the token to M).

Segmentation (inventory only, never values -- so the value-shuffled control sees the identical token stream): a
dynamic programme over the digit units; a two-digit key code costs 0, a one-digit key code (1 r, 5 a) 0.6, a two-digit
group carrying one dot 0.1 (a word-code '.xy'), a single dotted digit 0.8 ('.x'), a barred run is one word-code, an
out-of-key undotted pair 3 (kept, U), an out-of-key single digit 4 (kept, U). The glyphs S and X map to the key's
two glyph rows.
"""
import csv, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TGT = os.path.abspath(os.path.join(HERE, '..'))
W = os.path.join(TGT, 'witness')
KEY = os.path.join(TGT, '..', 'fr4715-montholon-1589', 'keys', 'key_vieuville_nevers.tsv')
LINES = ['L%02d' % n for n in list(range(6, 15)) + list(range(25, 31))]
READ_LINES = LINES[:9]   # GAPS-4 read L06-L14 (two passes); L25-L30 has pass A only (b3, first cut) -- the next step


def key_codes():
    codes = set()
    for ln in open(KEY, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('sign'):
            continue
        codes.add(ln.split('\t')[0])
    return codes


def parse(text):
    """crop string -> list of (unit, unsure)"""
    out, i, bar = [], 0, False
    while i < len(text):
        c = text[i]
        if c == '{':
            j = text.find('}', i)
            j = len(text) if j < 0 else j
            for w in text[i + 1:j].split():
                out.append(('w:' + w, False))
            i = j + 1; continue
        if c == '[':
            bar = True; i += 1; continue
        if c == ']':
            bar = False; i += 1; continue
        if c == '(':
            j = text.find(')', i)
            alt = text[i + 1:j].split('/')[0] if j > 0 else '?'
            dot = False
            if alt.startswith('.'):
                dot, alt = True, alt[1:]
            for d in alt[:1] or '?':
                out.append((('=' if bar else '.' if dot else '') + d, True))
            i = j + 1; continue
        if c == '.' and i + 1 < len(text) and (text[i + 1].isdigit() or text[i + 1] == '('):
            if text[i + 1] == '(':
                j = text.find(')', i)
                alt = text[i + 2:j].split('/')[0]
                out.append(('.' + (alt[:1] or '?'), True)); i = j + 1; continue
            out.append(('.' + text[i + 1], False)); i += 2; continue
        if c.isdigit():
            out.append((('=' if bar else '') + c, False))
        elif c in 'SX?':
            out.append((c, False))
        elif c == '#':
            out.append(('?', True))
        i += 1
    return out


def overlap_merge(acc, nxt):
    best = 0
    for k in range(min(8, len(acc), len(nxt)), 1, -1):
        a = [u for u, _ in acc[-k:]]; b = [u for u, _ in nxt[:k]]
        mism = sum(1 for x, y in zip(a, b) if x.lstrip('.=') != y.lstrip('.='))
        if mism <= (1 if k >= 4 else 0):
            best = k; break
    return acc + nxt[best:], best


def merge():
    for p in 'AB':
        rows = {}
        # b1..b3: the first cut (images/f60r_blocks3, centred on a straight slope); its s4-s6 crops sit on the wrong row
        # where the lines curve up at the right (both passes reported it), so only s1-s3 are kept from it and s4-s6 come
        # from the straightened, ink-tracked re-cut (images/f60r_blocks3t, pass file _t)
        for f in sorted(glob.glob(os.path.join(W, 'f60r_blocks_pass%s_b*.tsv' % p))):
            for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t'):
                if int(r['crop'].strip()[-1]) <= 3:
                    rows[r['crop'].strip()] = r
        tf = os.path.join(W, 'f60r_blocks_pass%s_t.tsv' % p)
        if os.path.exists(tf):
            for r in csv.DictReader(open(tf, encoding='utf-8'), delimiter='\t'):
                rows[r['crop'].strip()] = r
        out = open(os.path.join(W, 'f60r_blocks_pass%s_long.tsv' % p), 'w', encoding='utf-8')
        out.write('line\tpos\ttoken\tconf\n')
        stats = []
        for L in READ_LINES:
            acc, conf = [], []
            for s in range(1, 7):
                r = rows.get('f60r_%s_s%d' % (L, s))
                if not r:
                    continue
                units = parse(r['text'])
                acc, k = overlap_merge(acc, units)
                conf.append((r.get('conf') or 'M').strip()[:1].upper())
                stats.append(k)
            lc = 'L' if 'L' in conf else 'M' if 'M' in conf else 'H'
            for i, (u, unsure) in enumerate(acc, 1):
                out.write('%s\t%d\t%s\t%s\n' % (L, i, u, 'L' if unsure else lc))
        out.close()
        print('pass %s: %d crops, overlaps dropped per join %s' % (p, len(rows), stats))


def segment_units(units, codes):
    """units: list of unit strings -> list of tokens (codes, '.xy' word-codes, 'w:..', '?')."""
    toks, i = [], 0
    while i < len(units):
        u = units[i]
        if u.startswith('w:') or u == '?':
            toks.append(u); i += 1; continue
        if u.startswith('='):
            j = i
            while j < len(units) and units[j].startswith('='):
                j += 1
            toks.append('.' + ''.join(x[1:] for x in units[i:j])); i = j; continue
        j = i
        while j < len(units) and (units[j][-1].isdigit() or units[j] in ('S', 'X')) and not units[j].startswith('='):
            j += 1
        toks.extend(dp(units[i:j], codes)); i = j
    return toks


def dp(run, codes):
    n = len(run); INF = 1e9
    best = [INF] * (n + 1); back = [None] * (n + 1); best[0] = 0
    glyph = {'S': '♀', 'X': '▽'}
    for i in range(n):
        if best[i] >= INF:
            continue
        cand = []
        u = run[i]
        if u in glyph:
            cand.append((1, 0, glyph[u]))
        else:
            d1 = u.lstrip('.')
            dot1 = u.startswith('.')
            if dot1:
                cand.append((1, 0.8, '.' + d1))
            elif d1 in codes:
                cand.append((1, 0.6, d1))
            else:
                cand.append((1, 4, d1))
            if i + 1 < n and run[i + 1] not in glyph:
                v = run[i + 1]; d2 = d1 + v.lstrip('.')
                dots = dot1 + v.startswith('.')
                if dots == 1:
                    cand.append((2, 0.1, '.' + d2))
                elif dots == 0:
                    cand.append((2, 0 if d2 in codes else 3, d2))
                    # neither pass ever wrote an 8 on this leaf (no.58's dump: 8 is 7.8 pct of digits); no key code starts
                    # with 0, so a pair that starts with 0 and is out of key is read as 8x -- inventory only, flagged '8<'
                    if d2 not in codes and d2[0] == '0' and ('8' + d2[1]) in codes:
                        cand.append((2, 0.3, '8<' + d2[1]))
                elif dots == 1 and d2[0] == '0':
                    cand.append((2, 0.4, '.8<' + d2[1]))
        for L, c, t in cand:
            if best[i] + c < best[i + L]:
                best[i + L] = best[i] + c; back[i + L] = (i, t)
    out, k = [], n
    while k > 0:
        i, t = back[k]; out.append(t); k = i
    return out[::-1]


def segment():
    codes = key_codes()
    draft = os.path.join(W, 'f60r_blocks_rec', 'ciphertext_draft.tsv')
    settled = {}
    sp = os.path.join(W, 'f60r_blocks_settled.tsv')
    if os.path.exists(sp):
        for r in csv.DictReader(open(sp, encoding='utf-8'), delimiter='\t'):
            settled[(r['line'], r['position'])] = (r['sign'], r.get('conf', 'M'))
    by = {}
    for r in csv.DictReader([l for l in open(draft, encoding='utf-8') if not l.startswith('#')], delimiter='\t'):
        L, pos = r['line'], r['position']
        sign, conf = r['sign'], r['confidence']
        if (L, pos) in settled:
            sign, conf = settled[(L, pos)]
        if sign in ('', '-', '_'):
            continue
        by.setdefault(L, []).append((sign, conf))
    out = open(os.path.join(TGT, 'f60r_blocks_ciphertext.tsv'), 'w', encoding='utf-8')
    out.write('# fr4715-vieuville-pool no.37 f.60r dense cipher blocks L06-L14, L25-L30: two blind Opus passes (witness/f60r_blocks_pass{A,B}_*.tsv)\n'
              '# merged and aligned by tools/reconcile_passes.py, disagreements settled in witness/f60r_blocks_settled.tsv, digits segmented into\n'
              '# key codes by scripts/f60r_blocks.py segment (inventory only). token: NN code, .NN dotted/barred word-code, w:word clear word.\n'
              '# conf: the lowest confidence of the digits making the token (H both passes H and agreed; M agreed at M or settled; L unsure).\n')
    out.write('line\tpos\ttoken\tconf\tgloss\n')
    n = 0
    for L in READ_LINES:
        seq = by.get(L, [])
        units = [s for s, _ in seq]
        confs = [c for _, c in seq]
        toks = segment_units(units, codes)
        # carry confidence: walk the units consumed per token
        ui, pos = 0, 0
        for t in toks:
            eight = '8<' in t
            t = t.replace('8<', '8')
            if t.startswith('w:') or t == '?':
                width = 1
            else:
                width = len(t.lstrip('.')) if t not in ('♀', '▽') else 1
            cs = confs[ui:ui + width] or ['L']; ui += width
            c = 'L' if 'L' in cs else 'M' if 'M' in cs else 'H'
            if eight and c == 'H':
                c = 'M'
            pos += 1; n += 1
            out.write('%s\t%d\t%s\t%s\t\n' % (L, pos, t, c))
    out.close()
    print('wrote f60r_blocks_ciphertext.tsv: %d tokens' % n)


def segcontrol():
    """Strip the grouping from no.58's Tomokiyo dump (dots kept on the first digit), re-segment, compare."""
    codes = key_codes()
    dump = open(os.path.join(TGT, '..', 'fr4715-montholon-1589', 'witness', 'aligned_dump_codes.txt'), encoding='utf-8').read().split()
    units, truth = [], []
    for t in dump:
        if t.startswith('~'):
            continue
        dot = t.startswith("'")
        d = t.lstrip("'")
        truth.append(('.' + d) if dot else d)
        for k, ch in enumerate(d):
            units.append(('.' if dot and k == 0 else '') + ({'♀': 'S', '▽': 'X'}.get(ch, ch)))
    got = dp(units, codes)
    import difflib
    sm = difflib.SequenceMatcher(None, truth, got, autojunk=False)
    same = sum(b.size for b in sm.get_matching_blocks())
    print('segcontrol: Tomokiyo groups %d, re-segmented %d, identical tokens in alignment %d = %.3f of his'
          % (len(truth), len(got), same, same / len(truth)))


if __name__ == '__main__':
    {'merge': merge, 'segment': segment, 'segcontrol': segcontrol}[sys.argv[1]]()

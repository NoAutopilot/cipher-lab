#!/usr/bin/env python3
"""AUD2-FAMILY-A2r-1 (second audit, 10 Oct 2026): the period key sheet against the rebuilt key and the l.44535 reading.

python3 audit_period_key.py [--check]
- bm/key_period_f117.tsv: BL Add MS 4166 f.117, endorsed on f.117v "Cypher with Blank Marshal" (DECODE R4897), letter table
  1-101 and names 102-139 as read on the DECODE image by the second auditor (letter columns I/J -> i, V -> u).
- Compares every code of bm/key_blankmarshall.tsv and bm/key_blankmarshall_7.tsv with the sheet (agree / differ / not on sheet).
- Decodes bm/l44535_ciphertext.tsv with the sheet alone and compares, group by group, with the committed bm/reading_l44535.tsv
  (letters compared as letters; name codes compared as sheet label vs reading label, listed).
--check: exit 1 unless every one of the 151 groups is on the sheet and every letter group's sheet value equals the committed
reading's value (so the reading's group values are H-supported), and the comparison table printed matches the committed
bm/audit_period_key.out.
"""
import csv, os, sys
H = os.path.dirname(os.path.abspath(__file__))

def tsv(p): return list(csv.DictReader(open(os.path.join(H, p)), delimiter='\t'))

def main():
    sheet = {r['value']: r for r in tsv('key_period_f117.tsv')}
    out = []
    for fn in ('key_blankmarshall.tsv', 'key_blankmarshall_7.tsv'):
        agree, differ, off = [], [], []
        for r in tsv(fn):
            v, m = r['value'], r['meaning']
            s = sheet.get(v)
            if s is None: off.append(f'{v}={m}')
            elif s['kind'] == 'letter':
                (agree if m == s['meaning'] else differ).append(f'{v}: ours {m} / sheet {s["meaning"]}')
            else:
                differ.append(f'{v}: ours {m} / sheet {s["meaning"]} (name)')
        out.append(f'{fn}: letter codes agreeing with the sheet {len(agree)}; differing or name codes {len(differ)}; not on sheet {len(off)}')
        out += ['  ' + d for d in differ]
        out.append('  not on sheet: ' + ', '.join(off))
    ct = [r for r in tsv('l44535_ciphertext.tsv') if r['kind'] == 'N']
    rd = {(r['row'], r['pos']): r for r in tsv('reading_l44535.tsv')}
    n = len(ct); on = letters_same = names = 0; bad = []
    for r in ct:
        s = sheet.get(r['token']); c = rd.get((r['row'], r['pos']))
        if s is None: bad.append(f"{r['row']}.{r['pos']} {r['token']} not on sheet"); continue
        on += 1
        if s['kind'] == 'letter':
            if c and c['meaning'] == s['meaning']: letters_same += 1
            else: bad.append(f"{r['row']}.{r['pos']} {r['token']} sheet {s['meaning']} / reading {c and c['meaning']}")
        else:
            names += 1; out.append(f"  name group {r['row']}.{r['pos']} {r['token']}: sheet '{s['sheet_label']}' / reading '{c and c['meaning']}'")
    out.insert(len(out) - names, f'l.44535: groups {n}; on the sheet {on}; letter groups with the same value as the committed reading {letters_same}; name groups {names}; mismatches {len(bad)}')
    out += ['  MISMATCH ' + b for b in bad]
    text = '\n'.join(out) + '\n'
    print(text, end='')
    if '--check' in sys.argv:
        ok = (on == n and not bad)
        p = os.path.join(H, 'audit_period_key.out')
        if not os.path.exists(p) or open(p).read() != text: ok = False; print('stale or missing audit_period_key.out', file=sys.stderr)
        sys.exit(0 if ok else 1)
    open(os.path.join(H, 'audit_period_key.out'), 'w').write(text)

if __name__ == '__main__':
    main()

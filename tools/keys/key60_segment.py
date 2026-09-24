#!/usr/bin/env python3
"""Join transcription atoms (tools/keys/key60_atoms.md) into key no.60 signs (tools/keys/key60.tsv).

  python3 tools/keys/key60_segment.py ATOMS.tsv OUT.tsv [--key tools/keys/key60.tsv] [--check]

ATOMS.tsv: 'line pos sign conf' (a reconciled atom file). Per line, greedy longest match: up to 4 consecutive atoms
whose concatenation is a key sign become one token; '^' (superscript mark) is appended to the preceding atom first
and tried both ways; '=word' rows (clear words) pass through. A joined token gets conf M (the segmentation is a
choice, not a reading); a single atom keeps its conf. OUT.tsv: 'line pos sign conf atoms' (atoms = the positions
joined), the ciphertext.tsv tools/decode_key.py reads. --check exits 1 if OUT.tsv differs from a regeneration.
"""
import csv, sys, os

def load_key(p):
    s = set()
    for line in open(p, encoding='utf-8'):
        if line.startswith('#') or line.startswith('sign\t'):
            continue
        s.add(line.split('\t')[0])
    return s

ALIAS = {'∞': 'oo'}   # atom tag -> Bourdeau's key tag for the same shape

def segment(rows, key):
    out = []
    by = {}
    for r in rows:
        by.setdefault(r['line'], []).append(r)
    for ln, rs in by.items():
        atoms = []
        for r in rs:
            if r['sign'] == '^' and atoms and not atoms[-1]['sign'].startswith('='):
                atoms[-1] = dict(atoms[-1], sup=True)
                continue
            r = dict(r)
            q = r['sign'].endswith('?')
            r['sign'] = ALIAS.get(r['sign'].rstrip('?'), r['sign'].rstrip('?')) + ('?' if q else '')
            atoms.append(r)
        i, pos = 0, 0
        while i < len(atoms):
            a = atoms[i]
            pos += 1
            if a['sign'].startswith('='):
                out.append([ln, pos, a['sign'], a['conf'], a['pos']]); i += 1; continue
            best = None
            for n in (4, 3, 2):
                grp = atoms[i:i + n]
                if len(grp) < n or any(g['sign'].startswith('=') for g in grp):
                    continue
                cat = ''.join(g['sign'].rstrip('?') for g in grp)
                if cat in key:
                    best = (n, cat); break
            if best:
                n, cat = best
                out.append([ln, pos, cat, 'M', ','.join(g['pos'] for g in atoms[i:i + n])]); i += n
            else:
                s = a['sign']
                if a.get('sup') and s.rstrip('?') + "'" in key:
                    s = s.rstrip('?') + "'"      # superscript mark read as the key's prime variant
                out.append([ln, pos, s, a['conf'] if not a.get('sup') else 'M', a['pos']]); i += 1
    return out

def render(out):
    return 'line\tpos\tsign\tconf\tatoms\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in out)

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    kp = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'key60.tsv')
    if '--key' in sys.argv:
        kp = sys.argv[sys.argv.index('--key') + 1]; args.remove(kp)
    rows = list(csv.DictReader(open(args[0], encoding='utf-8'), delimiter='\t'))
    new = render(segment(rows, load_key(kp)))
    if '--check' in sys.argv:
        sys.exit(0 if open(args[1], encoding='utf-8').read() == new else 1)
    open(args[1], 'w', encoding='utf-8').write(new)
    print(args[1], new.count('\n') - 1, 'tokens')

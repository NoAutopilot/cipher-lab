#!/usr/bin/env python3
"""R10-BAL103F (6 Oct 2026): map the 42 ambiguous f.50 9s (r9/f50_choices.tsv) to sorter tiles and write sorter/focus_9.tsv,
appended after the 28 r8b questions into sorter/focus_all.tsv for tools/sign_sorter.py --focus.

Mapping, in order: (a) the tile clusters.tsv aligned to that (line, position) column (col is 1-based = ciphertext.tsv position,
checked: 476/628 aligned tiles start in the pile of that position's sign vs 28 for 0-based); smallest |dx| wins; (a') if that
tile's starting pile is not 9 and an unaligned neighbouring tile (one either side) starts in pile 9, that tile, reported 'adjacent'. (b') if the column took no tile, a tile aligned to the column either side that starts in pile 9 (the line's alignment
shifted by one), reported 'shifted'. (b) otherwise,
the tiles strictly between the nearest aligned neighbour columns on the same line, preferring one whose starting pile is 9 and
then the one nearest the linear x-interpolation; reported as 'interp'. (c) otherwise unmapped, reported and dropped.
The question gives no decoded context and no lean (shape only; the circled/plain premise is void, R9-BAL103B).
  python3 ciphers/baluze103-letellier-marca-1644/r10f/focus9.py [--check]
"""
import csv, sys
from pathlib import Path
T = Path(__file__).resolve().parents[1]; S = T / 'sorter'
NINE, WIN = {'10', '15'}, 3   # clusters.tsv shape clusters holding the eyed 9s (11 + 3 of 17 eyed true 9s); window in tiles


def build():
    lab = {r['sid']: r['sign'] for r in csv.DictReader(open(S / 'labels.tsv'), delimiter='\t')}
    xs = {r['sid']: int(r['x']) + int(r['w']) / 2 for r in csv.DictReader(open(S / 'signs.tsv'), delimiter='\t')}
    tiles, col = {}, {}
    for r in csv.DictReader(open(S / 'clusters.tsv'), delimiter='\t'):
        ln = r['sid'].rsplit('_', 1)[0]; tiles.setdefault(ln, []).append(r['sid'])
        if r['col']: col.setdefault((ln, int(r['col'])), []).append((abs(int(r['dx'])), r['sid']))
    used = {s for _, s in (q for v in col.values() for q in v)}
    clu = {r['sid']: r['cluster'] for r in csv.DictReader(open(S / 'clusters.tsv'), delimiter='\t')}
    rows, report = [], []
    for r in csv.DictReader(open(T / 'r9' / 'f50_choices.tsv'), delimiter='\t'):
        ln, p = f"{r['folio']}_{r['line']}", int(r['position']); how = 'aligned'
        if (ln, p) in col:
            sid = min(col[(ln, p)])[1]
            if lab.get(sid) != '9':        # (a') a 30-px alignment can land one tile off: take an adjacent unaligned tile in pile 9
                i = tiles[ln].index(sid)
                adj = [t for t in tiles[ln][max(0, i - 1):i + 2] if t != sid and t not in used and lab.get(t) == '9']
                if adj: sid = adj[0]; how = 'adjacent'
        else:
            left = [c for (l, c) in col if l == ln and c < p]; right = [c for (l, c) in col if l == ln and c > p]
            near = [q[1] for c in (p - 1, p + 1) for q in sorted(col.get((ln, c), [])) if lab.get(q[1]) == '9']
            if near:                       # (b') the column took no tile and a neighbour column's tile starts in pile 9 (line shifted)
                sid = near[0]; how = 'shifted'
                rows.append((sid, Q(ln, p, r))); report.append((ln, p, sid, how)); continue
            if not left or not right: report.append((ln, p, '', 'unmapped')); continue
            cl, cr = max(left), min(right)
            xl = xs[min(col[(ln, cl)])[1]]; xr = xs[min(col[(ln, cr)])[1]]; xe = xl + (xr - xl) * (p - cl) / (cr - cl)
            cand = [s for s in tiles[ln] if xl < xs[s] < xr and s not in used]
            if not cand: report.append((ln, p, '', 'unmapped')); continue
            sid = min(cand, key=lambda s: (lab.get(s) != '9', abs(xs[s] - xe))); how = 'interp'
        rows.append((sid, Q(ln, p, r))); report.append((ln, p, sid, how))
    # (c) shape check, added after an eye check of the first mapping (18 of 42 tiles looked like a 9): the 9 shape sits in
    # clusters NINE; a tile outside them is replaced by the nearest tile within WIN tiles on its line that is in NINE and
    # not already taken ('reshaped'), else dropped ('dropped: <cluster>')
    taken = {sid for sid, _ in rows}; out_rows, out_rep, k = [], [], 0
    for ln, p, sid, how in report:
        if not sid: out_rep.append((ln, p, sid, how)); continue
        q = rows[k][1]; k += 1
        if clu[sid] not in NINE:
            i = tiles[ln].index(sid)
            win = sorted((abs(j - i), t) for j, t in enumerate(tiles[ln]) if 0 < abs(j - i) <= WIN and clu[t] in NINE and t not in taken)
            if not win: out_rep.append((ln, p, sid, f'dropped: cluster {clu[sid]}')); continue
            sid = win[0][1]; how = 'reshaped'; taken.add(sid)
        out_rows.append((sid, q)); out_rep.append((ln, p, sid, how))
    return out_rows, out_rep


def Q(ln, p, r):
    return (f"{ln}.{p}: a 9 whose value (i, r or s) is open. Shape only: long looped g-like tail, or short 9? "
            f"Move long-tailed ones to a new pile named 9g; leave short ones in 9; set aside if not a 9 or a bad cut.")


def main():
    rows, report = build()
    seen, out = set(), []
    for sid, q in rows:
        if sid in seen: continue
        seen.add(sid); out.append(f'{sid}\t{q}\n')
    rep = 'line\tposition\tsid\thow\n' + ''.join('\t'.join(map(str, x)) + '\n' for x in report)
    r8b = (S / 'focus_r8b.tsv').read_text(); r8 = {l.split('\t')[0] for l in r8b.splitlines()}
    allf = r8b + ''.join(l for l in out if l.split('\t')[0] not in r8)
    files = {S / 'focus_9.tsv': ''.join(out), T / 'r10f' / 'map9.tsv': rep, S / 'focus_all.tsv': allf}
    if '--check' in sys.argv:
        # focus_all.tsv is excluded: build.sh's small_pile() rewrites it in place, dropping SMALL tiles
        stale = [p.name for p, t in files.items() if p.name != 'focus_all.tsv' and (not p.exists() or p.read_text() != t)]
        print('stale: ' + ' '.join(stale) if stale else 'up to date'); sys.exit(1 if stale else 0)
    for p, t in files.items(): p.write_text(t)
    hw = [x[3] for x in report]
    print(f"9s {len(report)}: aligned {hw.count('aligned')}, interp {hw.count('interp')}, adjacent {hw.count('adjacent')}, shifted {hw.count('shifted')}, reshaped {hw.count('reshaped')}, dropped {sum(h.startswith('dropped') for h in hw)}, unmapped {hw.count('unmapped')}; "
          f"focus_9 {len(out)} tiles (dupes dropped {len(rows) - len(out)}); overlap with r8b {len(seen & r8)}; focus_all {len(allf.splitlines())}")


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Turn a person's sign-sorter decisions into a settled inventory.

  python3 tools/sign_sorter_apply.py --labels labels.tsv --db DIR --out settled_labels.tsv [--summary summary.json]

--db is the folder the ArtifactData tool writes with out_dir (DIR/piles/*.json, DIR/moves/*.json,
DIR/newpiles/*.json; each file is one document as saved by tools/sign_sorter/template.html). The output has one
row per sign: sid, old_sign, new_sign, status, where status is one of
  kept        the tile stays in its pile
  moved       the person moved the tile to another (or a new) pile
  merged      its pile was declared the same sign as another pile (followed transitively, cycles broken)
  not-letter  its final pile was marked "Not a letter"
  aside       set aside without a pile (needs a second look)
  bad-cut     the tile's box was cut in the wrong place (recut it before reading)
A pile's verdict "same" (all one sign) is recorded in the summary as confirmed. Nothing is guessed: a tile the
person did not touch keeps its old label."""
import argparse, csv, glob, json, os, sys


def load(dirp, coll):
    out = []
    for f in sorted(glob.glob(os.path.join(dirp, coll, '*.json'))):
        d = json.load(open(f))
        out.append(d.get('data', d))
    return out


def apply(labels, piles, moves, newpiles):
    merge = {p['pile']: p['merge_into'] for p in piles if p.get('merge_into')}
    verdict = {p['pile']: p.get('verdict') for p in piles}
    outliers = {sid for p in piles if not p.get('merge_into') for sid in (p.get('outliers') or [])}
    mv = {m['sid']: m['to'] for m in moves if m.get('sid') and m.get('to')}

    def final(pile):
        seen = set()
        while pile in merge and pile not in seen:
            seen.add(pile); pile = merge[pile]
        return pile
    rows = []
    for r in labels:
        sid, old = r['sid'], r['sign']
        dest = mv.get(sid)
        if dest is None and sid in outliers:
            dest = 'ASIDE'
        if dest == 'ASIDE':
            rows.append((sid, old, '', 'aside')); continue
        if dest == 'BAD-CUT':
            rows.append((sid, old, '', 'bad-cut')); continue
        pile = dest or old
        fin = final(pile)
        status = 'moved' if dest else ('merged' if fin != old else 'kept')
        if verdict.get(fin) == 'mark':
            status = 'not-letter'
        rows.append((sid, old, fin, status))
    summary = {
        'tiles': len(rows),
        'by_status': {s: sum(1 for r in rows if r[3] == s) for s in ('kept', 'moved', 'merged', 'not-letter', 'aside', 'bad-cut')},
        'signs_before': len({r[1] for r in rows}),
        'signs_after': len({r[2] for r in rows if r[2] and r[3] != 'not-letter'}),
        'confirmed_piles': sorted(p for p, v in verdict.items() if v == 'same'),
        'not_letter_piles': sorted(p for p, v in verdict.items() if v == 'mark'),
        'merges': merge, 'new_piles': sorted(n['id'] for n in newpiles if n.get('id')),
    }
    return rows, summary


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--labels', required=True); ap.add_argument('--db', required=True)
    ap.add_argument('--out', required=True); ap.add_argument('--summary')
    a = ap.parse_args(argv)
    labels = list(csv.DictReader(open(a.labels, newline=''), delimiter='\t'))
    rows, summary = apply(labels, load(a.db, 'piles'), load(a.db, 'moves'), load(a.db, 'newpiles'))
    with open(a.out, 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t'); w.writerow(['sid', 'old_sign', 'new_sign', 'status']); w.writerows(rows)
    if a.summary:
        json.dump(summary, open(a.summary, 'w'), indent=1)
    print(json.dumps({k: summary[k] for k in ('tiles', 'by_status', 'signs_before', 'signs_after')}))


if __name__ == '__main__':
    main()

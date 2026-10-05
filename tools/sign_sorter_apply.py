#!/usr/bin/env python3
"""Turn a person's sign-sorter decisions into a settled inventory.

  python3 tools/sign_sorter_apply.py (--labels labels.tsv | --atlas-topk T.tsv ...) --db DIR --out settled_labels.tsv [--summary summary.json]
      [--clusters clusters.tsv --atlas-labels ATLAS/labels.json [--atlas-out labels.json] [--source TEXT]]

--db is the folder the ArtifactData tool writes with out_dir (DIR/piles/*.json, DIR/moves/*.json,
DIR/newpiles/*.json; each file is one document as saved by tools/sign_sorter/template.html). The output has one
row per sign: sid, old_sign, new_sign, status, where status is one of
  kept        the tile stays in its pile
  moved       the person moved the tile to another (or a new) pile
  merged      its pile was declared the same sign as another pile (followed transitively, cycles broken)
  not-letter  its final pile was marked "Not a letter"
  aside       set aside without a pile (needs a second look)
  bad-cut     the tile's box was cut in the wrong place (recut it before reading)
  taken-out   taken out of its pile in step 1 ("doesn't belong here") and not yet placed in step 2: unsettled, no
              sign (moves doc with to 'OUT', two-step sorter, 3 Oct 2026); never silently kept in its old pile
  cluster-moved  the person made a cluster decision (DIR/clusters/*.json, TX-SORTER 3 Oct 2026) and this tile, of
              that cluster, had no move of its own: it follows the decision (a sibling letter's tile, or a save from a
              page built before the per-tile moves landed)
A pile's verdict "same" (all one sign) is recorded in the summary as confirmed. A tile the person confirmed in
place ("Right pile: keep it", DIR/checked/*.json {sid, pile}, QA pass 3 Oct 2026) stays 'kept' and is listed in the
summary's confirmed_tiles (only while it has no move of its own). New piles are named by the page (the tile's pile
plus -b, -c, ...: T51-b) and come out as new sign labels like any other pile name. Nothing is guessed: a tile the
person did not touch keeps its old label. A save with no clusters collection (every sorter published before 3 Oct
2026, Birago and Florence included) applies exactly as before.

Family atlas (TRANSCRIPTION.md step 7). With --atlas-labels (a tools/glyph_atlas.py labels.json) and --clusters (the
atlas's clusters.tsv, or sid<TAB>cluster), the decisions are written into the atlas so every sibling letter's next
glyph_atlas atlas/classify run picks them up:
  - a cluster decision sets signs[<cluster>] = the destination pile's final code;
  - a merge A -> B rewrites every signs[] and override[] value A to B; a "Not a letter" pile becomes '_';
  - a single tile moved on its own (no cluster decision covers it) becomes override[<sid>] = its new code, but only
    when that differs from what its cluster already reads;
  - aside and bad-cut tiles are listed under "sorter_review" (not relabelled), and each run appends one
    "sorter_log" entry (UTC time, --source, counts). Provisional clusters ("<pile>~<n>", from sign_sorter.py
    --auto-clusters) are page-local and are never written to an atlas.
Fixed cuts ("Fix the cut", 4 Oct 2026, SORTER-NUDGE): DIR/recuts/*.json ({sid, page, x, y, w, h, old, at}, source
line-image pixels) are written to recuts.tsv beside --out (or --recuts-out): tile, page, old_x old_y old_w old_h, new_x
new_y new_w new_h, at, quad, mask. Since 5 Oct 2026 (SORTER-QUAD) a doc may carry quad [[x, y]] x 4 (TL, TR, BR, BL:
corners moved one by one) and mask [{r, pts}] (brush strokes over a neighbour's ink); both go to the quad and mask cells as
JSON, and new_x .. new_h are then the quad's bounding box. An old {x, y, w, h} doc leaves both cells empty. A recut tile
keeps its pile and status here; tools/sorter_apply_recuts.py re-crops it and updates signs.tsv. No recuts saved: no file
is written.
Must NOT be used to write a cluster label the person did not choose: nothing here infers a code from shape."""
import argparse, csv, glob, json, os, sys


def load(dirp, coll):
    out = []
    for f in sorted(glob.glob(os.path.join(dirp, coll, '*.json'))):
        d = json.load(open(f))
        out.append(d.get('data', d))
    return out


def apply(labels, piles, moves, newpiles, cluster_docs=(), cluster_of=None, checked=()):
    merge = {p['pile']: p['merge_into'] for p in piles if p.get('merge_into')}
    verdict = {p['pile']: p.get('verdict') for p in piles}
    outliers = {sid for p in piles if not p.get('merge_into') for sid in (p.get('outliers') or [])}
    mv = {m['sid']: m['to'] for m in moves if m.get('sid') and m.get('to')}
    cdec = {c['cluster']: c['to'] for c in cluster_docs if c.get('cluster') and c.get('to')}
    cluster_of = dict(cluster_of or {})

    def final(pile):
        seen = set()
        while pile in merge and pile not in seen:
            seen.add(pile); pile = merge[pile]
        return pile
    rows = []
    for r in labels:
        sid, old = r['sid'], r['sign']
        dest = mv.get(sid)
        via_cluster = False
        if dest is None and sid in outliers:
            dest = 'ASIDE'
        c = cluster_of.get(sid) or r.get('cluster')
        if dest is None and c in cdec and cdec[c] != old:
            dest, via_cluster = cdec[c], True
        if dest == 'ASIDE':
            rows.append((sid, old, '', 'aside')); continue
        if dest == 'BAD-CUT':
            rows.append((sid, old, '', 'bad-cut')); continue
        if dest == 'OUT':
            rows.append((sid, old, '', 'taken-out')); continue
        pile = dest or old
        fin = final(pile)
        status = ('cluster-moved' if via_cluster else 'moved') if dest else ('merged' if fin != old else 'kept')
        if verdict.get(fin) == 'mark':
            status = 'not-letter'
        rows.append((sid, old, fin, status))
    summary = {
        'tiles': len(rows),
        'by_status': {s: sum(1 for r in rows if r[3] == s) for s in ('kept', 'moved', 'merged', 'not-letter', 'aside', 'bad-cut')
                      + (('cluster-moved',) if cdec else ()) + (('taken-out',) if any(r[3] == 'taken-out' for r in rows) else ())},
        'signs_before': len({r[1] for r in rows}),
        'signs_after': len({r[2] for r in rows if r[2] and r[3] != 'not-letter'}),
        'confirmed_piles': sorted(p for p, v in verdict.items() if v == 'same'),
        'not_letter_piles': sorted(p for p, v in verdict.items() if v == 'mark'),
        'merges': merge, 'new_piles': sorted(n['id'] for n in newpiles if n.get('id')),
    }
    kept_ok = {k['sid'] for k in checked if k.get('sid')} - set(mv)
    if kept_ok:
        summary['confirmed_tiles'] = sorted(kept_ok)
    if cdec:
        summary['cluster_decisions'] = {c: final(t) for c, t in cdec.items()}
    return rows, summary


def write_atlas(L, rows, piles, moves, cluster_docs, cluster_of, source=''):
    """Fold the decisions into a glyph_atlas labels.json dict (in place); returns the counts logged."""
    import datetime
    merge = {p['pile']: p['merge_into'] for p in piles if p.get('merge_into')}
    mark = {p['pile'] for p in piles if p.get('verdict') == 'mark'}

    def final(x):
        seen = set()
        while x in merge and x not in seen:
            seen.add(x); x = merge[x]
        return '_' if x in mark else x
    signs, over = L.setdefault('signs', {}), L.setdefault('override', {})
    n_clu = n_rel = n_over = 0
    for code_map in (signs, over):          # merges and not-letter piles relabel what the atlas already says
        for k, v in list(code_map.items()):
            f = final(v)
            if v != '_' and f != v:
                code_map[k] = f; n_rel += 1
    covered = set()
    for c in cluster_docs:
        cid, to = c.get('cluster'), c.get('to')
        if not cid or not to or '~' in cid or to in ('ASIDE', 'BAD-CUT', 'OUT'):
            continue                        # provisional page-local groups are never atlas clusters
        signs[cid] = final(to); n_clu += 1; covered.add(cid)
    own = {m['sid'] for m in moves if m.get('sid') and m.get('to')}
    review = L.setdefault('sorter_review', {})
    for sid, old, new, status in rows:
        if status in ('aside', 'bad-cut', 'taken-out'):
            review[sid] = status; continue
        if sid not in own or status not in ('moved', 'not-letter') or sid not in cluster_of:
            continue
        c = cluster_of[sid]
        code = '_' if status == 'not-letter' else new
        if c in covered and signs.get(c) == code:
            continue
        if signs.get(c, '_') != code:
            over[sid] = code; n_over += 1
        elif over.get(sid) not in (None, code):
            over[sid] = code; n_over += 1
    if not review:
        L.pop('sorter_review')
    entry = {'utc': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M'), 'source': source,
             'cluster_decisions': n_clu, 'overrides': n_over, 'relabelled_by_merge': n_rel}
    L.setdefault('sorter_log', []).append(entry)
    return entry


RECUT_COLS = ['tile', 'page', 'old_x', 'old_y', 'old_w', 'old_h', 'new_x', 'new_y', 'new_w', 'new_h', 'at', 'quad', 'mask']
num = lambda v: isinstance(v, (int, float)) and not isinstance(v, bool)


def doc_quad(d):
    """A recut doc's quad as [[x, y]] x 4 (TL, TR, BR, BL), or None when it has none or it is malformed."""
    q = d.get('quad')
    if isinstance(q, list) and len(q) == 4 and all(isinstance(p, list) and len(p) == 2 and all(num(v) for v in p) for p in q):
        return [[round(float(v), 2) for v in p] for p in q]
    return None


def doc_mask(d):
    """A recut doc's brush strokes [{r, pts}] (malformed strokes and points dropped)."""
    out = []
    for st in d.get('mask') or []:
        if not isinstance(st, dict) or not num(st.get('r')) or st['r'] <= 0:
            continue
        pts = [[round(float(p[0]), 2), round(float(p[1]), 2)] for p in st.get('pts') or []
               if isinstance(p, list) and len(p) == 2 and all(num(v) for v in p)]
        if pts:
            out.append({'r': round(float(st['r']), 2), 'pts': pts})
    return out


def recut_rows(docs):
    """db 'recuts' documents -> recuts.tsv rows (sorted by tile). A doc needs a full new box {x, y, w, h} or a quad (whose
    bounding box is then the new box); one with neither is dropped."""
    out = []
    for d in docs:
        q, new = doc_quad(d), [d.get(k) for k in ('x', 'y', 'w', 'h')]
        if q:
            xs, ys = [p[0] for p in q], [p[1] for p in q]
            l, t = int(round(min(xs))), int(round(min(ys)))
            new = [l, t, int(round(max(xs))) - l, int(round(max(ys))) - t]
        if not d.get('sid') or not all(num(v) for v in new):
            continue
        old = list(d.get('old') or [''] * 4)[:4]
        m = doc_mask(d)
        out.append([d['sid'], d.get('page', '')] + [int(round(v)) if num(v) else '' for v in old]
                   + [int(round(v)) for v in new] + [d.get('at', ''), json.dumps(q, separators=(',', ':')) if q else '',
                                                      json.dumps(m, separators=(',', ':')) if m else ''])
    return sorted(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--labels'); ap.add_argument('--db', required=True)
    ap.add_argument('--atlas-topk', nargs='+', help='the glyph_atlas topk files the page was built from (sign_sorter.py --atlas-topk)')
    ap.add_argument('--out', required=True); ap.add_argument('--summary')
    ap.add_argument('--clusters', help="the atlas's clusters.tsv (id, kind, cluster) or sid<TAB>cluster")
    ap.add_argument('--atlas-labels', help='family atlas labels.json to write the decisions into (needs --clusters)')
    ap.add_argument('--atlas-out', help='write the updated atlas labels here instead of in place')
    ap.add_argument('--source', default='', help='one line for the atlas sorter_log (which page, which letter)')
    ap.add_argument('--recuts-out', help='where to write the fixed cuts (default: recuts.tsv beside --out; only when any were saved)')
    a = ap.parse_args(argv)
    if a.atlas_labels and not a.clusters:
        ap.error('--atlas-labels needs --clusters (which tile is in which atlas cluster)')
    if a.atlas_topk:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from sign_sorter import atlas_topk_rows
        labels = [{'sid': r['box'], 'sign': r['k1']} for r in atlas_topk_rows(a.atlas_topk)]
    elif a.labels:
        labels = list(csv.DictReader(open(a.labels, newline=''), delimiter='\t'))
    else:
        ap.error('give --labels or --atlas-topk')
    cluster_of = {}
    if a.clusters:
        for r in csv.DictReader(open(a.clusters, newline=''), delimiter='\t'):
            sid = r.get('sid') or r.get('id')
            if r.get('kind', 'sign') == 'sign' and sid and r.get('cluster'):
                cluster_of[sid] = r['cluster']
    piles, moves, cdocs = load(a.db, 'piles'), load(a.db, 'moves'), load(a.db, 'clusters')
    rows, summary = apply(labels, piles, moves, load(a.db, 'newpiles'), cdocs, cluster_of, load(a.db, 'checked'))
    if a.atlas_labels:
        L = json.load(open(a.atlas_labels))
        summary['atlas'] = write_atlas(L, rows, piles, moves, cdocs, cluster_of, a.source)
        json.dump(L, open(a.atlas_out or a.atlas_labels, 'w'), indent=1, ensure_ascii=False)
    with open(a.out, 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t'); w.writerow(['sid', 'old_sign', 'new_sign', 'status']); w.writerows(rows)
    rc = recut_rows(load(a.db, 'recuts'))
    if rc:
        rp = a.recuts_out or os.path.join(os.path.dirname(os.path.abspath(a.out)), 'recuts.tsv')
        with open(rp, 'w', newline='') as f:
            w = csv.writer(f, delimiter='\t'); w.writerow(RECUT_COLS); w.writerows(rc)
        summary['recuts'] = len(rc)
    if a.summary:
        json.dump(summary, open(a.summary, 'w'), indent=1)
    print(json.dumps({k: summary[k] for k in ('tiles', 'by_status', 'signs_before', 'signs_after', 'atlas', 'recuts') if k in summary}))


if __name__ == '__main__':
    main()

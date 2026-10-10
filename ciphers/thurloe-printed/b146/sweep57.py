"""THUR-V57: b146/sweep.py's grouping applied to Birch 1742 vols 5 and 7 (disk only).

B146_CACHE=<dir with gunzipped collectionofstat03/05/07thur_djvu.txt and runs_inline.tsv from
  tools/ia_numeral_runs.py collectionofstat03thur collectionofstat05thur collectionofstat07thur --cache DIR --inline-run 4 --tsv DIR/runs_inline.tsv>
python3 b146/sweep57.py [--check]    -> bm/v57_hits.tsv (letter groups, vols 5 and 7), bm/v57_control.tsv (vol 3 positive control)
Filter declared before vols 5/7 were read: same as sweep.py (cluster numerals >= 10, outside the volume's index).
Index starts: vol 5 line 66081, vol 7 line 85067 (first 'INDEX.' page header after the text).
"""
import csv, io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sweep
sweep.VOLS.update({'5': ('collectionofstat05thur', 66081), '7': ('collectionofstat07thur', 85067)})
if __name__ == '__main__':
    check = '--check' in sys.argv
    rows = sweep.groups('5') + sweep.groups('7')
    idx = {r['row']: r for r in csv.DictReader(open(os.path.join(HERE, '..', 'index.tsv')), delimiter='\t')}
    G3 = sweep.groups('3'); ctl = []
    for n in (4, 5, 6, 7, 8, 9, 10, 26, 27, 28):
        a, b = map(int, idx['P%d' % n]['window_lines'].split('-'))
        hit = [g for g in G3 if g['line_last'] >= a - 5 and g['line_first'] <= b + 5]
        ctl.append(dict(vol='3', item='P%d' % n, window='%d-%d' % (a, b), found='yes' if hit else 'no',
                        decipherment_flag=';'.join(sorted({g['printed_decipherment'] for g in hit})) or '-', groups_hit=len(hit)))
    def dump(rs, cols):
        b = io.StringIO(); w = csv.DictWriter(b, cols, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rs)
        return b.getvalue()
    out = {'../bm/v57_hits.tsv': dump(rows, sweep.COLS), '../bm/v57_control.tsv': dump(ctl, list(ctl[0]))}
    for name, txt in out.items():
        p = os.path.join(HERE, name)
        if check:
            if not os.path.exists(p) or open(p).read() != txt: print('STALE', name); sys.exit(1)
        else: open(p, 'w').write(txt)
    print('ok' if check else 'groups v5 %d v7 %d; control vol3 %d/%d' % (sum(r['vol']=='5' for r in rows), sum(r['vol']=='7' for r in rows), sum(r['found']=='yes' for r in ctl), len(ctl)))

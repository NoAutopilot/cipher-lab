#!/usr/bin/env python3
"""The L-word pass on no.44 f.67r's clear-French frame (GAPS-fr4715-vieuville-pool-9, 2 Oct 2026).

After the GAPS-6 fold, f67r_ciphertext.tsv carries 233 tokens at conf L (pass C alone at M/L, plus L31's old A/B frame).
This script masks every run of consecutive L clear words as a numbered slot [Sn] in its line, keeps every other token
(H/M words and the settled cipher groups) as context, and picks the crop segment(s) the slot falls in from its character
offset in the line (segments are 1400 px with 150 px overlap over a 3500 px band, so s1 ~0-0.40, s2 ~0.36-0.76,
s3 ~0.71-1.0, widened by 0.15 either side). Two blind readers see only the masked sheet and the crops, never the old L
reading, and write what stands in each slot.

Scoring, per old L word w of a slot (normalised as scripts/f67r_frame_fold.py: lower case, u=v, i=j=y, accents dropped):
  both passes write w at the aligned place (difflib on word lists, plus a no-space substring test for 4+ letters) -> H
  (three readers: C, A9, B9); only one pass -> stays L.
A slot whose two new readings agree with each other (normalised, spaces ignored) but not with the old reading is a
replacement candidate; it goes to the reconciliation call, and is replaced (words at M) only if the reconciler,
shown the crop and all three readings, picks the A9=B9 reading. Cipher tokens are never touched.

  python3 scripts/f67r_lword_pass.py --build OUTDIR          # sheet.md + slots.tsv (old readings in slots.tsv only)
  python3 scripts/f67r_lword_pass.py --score A.tsv B.tsv [--recon R.tsv] [--write]
"""
import difflib, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from f67r_frame_fold import rows, bylines, is_cipher, norm

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CT = os.path.join(HERE, 'f67r_ciphertext.tsv')
SEGS = [(0.0, 0.40), (0.357, 0.757), (0.714, 1.0)]
TAG = 'GAPS-9 L-pass'


def slots():
    out = []
    for line, rs in bylines(rows(CT)).items():
        texts = [r['token'][2:] if r['token'].startswith('w:') else r['token'] for r in rs]
        total = sum(len(t) + 1 for t in texts)
        off, cur = 0, None
        for r, t in zip(rs, texts):
            isL = r['token'].startswith('w:') and r['conf'] == 'L'
            if isL:
                if cur is None:
                    cur = dict(line=line, rows=[], start=off)
                    out.append(cur)
                cur['rows'].append(r)
                cur['end'] = off + len(t)
            else:
                cur = None
            off += len(t) + 1
        for s in out:
            if s['line'] == line:
                s['total'] = total
    for i, s in enumerate(out, 1):
        s['id'] = 'S%d' % i
        a, b = s['start'] / s['total'] - 0.15, s['end'] / s['total'] + 0.15
        s['segs'] = [k + 1 for k, (lo, hi) in enumerate(SEGS) if hi >= a and lo <= b]
    return out


def build(outdir):
    os.makedirs(outdir, exist_ok=True)
    ss = slots()
    sid = {(r['line'], r['pos']): s['id'] for s in ss for r in s['rows']}
    with open(os.path.join(outdir, 'slots.tsv'), 'w') as f:
        f.write('slot\tline\tpositions\tsegments\told\n')
        for s in ss:
            f.write('%s\t%s\t%s\t%s\t%s\n' % (s['id'], s['line'], ','.join(r['pos'] for r in s['rows']),
                                            ','.join(map(str, s['segs'])),
                                            ' '.join(r['token'][2:] for r in s['rows'])))
    crops = 0
    with open(os.path.join(outdir, 'sheet.md'), 'w') as f:
        for line, rs in bylines(rows(CT)).items():
            parts, seen = [], set()
            for r in rs:
                k = (r['line'], r['pos'])
                if k in sid:
                    if sid[k] not in seen:
                        seen.add(sid[k])
                        parts.append('[%s]' % sid[k])
                else:
                    parts.append(r['token'][2:] if r['token'].startswith('w:') else '<%s>' % r['token'])
            segs = sorted({k for s in ss if s['line'] == line for k in s['segs']})
            if not seen:
                continue
            crops += len(segs)
            f.write('%s | crops: %s\n  %s\n' % (line, ' '.join('f67r_%s_s%d.jpg' % (line, k) for k in segs),
                                                 ' '.join(parts)))
    print('slots %d, L words %d, lines %d, crops %d' % (len(ss), sum(len(s['rows']) for s in ss),
                                                         len({s['line'] for s in ss}), crops))


def readpass(path):
    d = {}
    for ln in open(path, encoding='utf-8'):
        p = ln.rstrip('\n').split('\t')
        if len(p) >= 2 and re.fullmatch(r'S\d+', p[0]):
            d[p[0]] = p[1].strip()
    return d


def matched(old, new):
    a = [norm(w) for w in old]
    b = [norm(w) for w in new.split()]
    hit = set()
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            if a[blk.a + k]:
                hit.add(blk.a + k)
    joined = ''.join(b)
    for i, w in enumerate(a):
        if i not in hit and len(w) >= 4 and w in joined:
            hit.add(i)
    return hit


def score(pa, pb, recon=None, write=False):
    A, B = readpass(pa), readpass(pb)
    R = readpass(recon) if recon else {}
    ss = slots()
    tot = up = slot_agree = 0
    cand, replaced = [], {}
    moved = {}
    for s in ss:
        old = [r['token'][2:] for r in s['rows']]
        a, b = A.get(s['id'], ''), B.get(s['id'], '')
        na, nb = ''.join(norm(w) for w in a.split()), ''.join(norm(w) for w in b.split())
        no = ''.join(norm(w) for w in old)
        tot += len(old)
        if na and na == nb:
            slot_agree += 1
        both = matched(old, a) & matched(old, b)
        for i in both:
            moved[(s['rows'][i]['line'], s['rows'][i]['pos'])] = 'H'
        up += len(both)
        if na and na == nb and na != no and not both:
            cand.append((s, a, b))
            r = R.get(s['id'], '')
            if r and ''.join(norm(w) for w in r.split()) == na:
                replaced[s['id']] = (s, a)
    print('slots %d, L words %d; slot strings A9=B9: %d (%.1f pct)' % (len(ss), tot, slot_agree, 100.0 * slot_agree / len(ss)))
    print('old L words confirmed by both passes -> H: %d of %d' % (up, tot))
    print('replacement candidates (A9=B9 != old, no old word confirmed): %d' % len(cand))
    for s, a, b in cand:
        print('  %s %s old=%r new=%r recon=%r' % (s['id'], s['line'], ' '.join(r['token'][2:] for r in s['rows']), a,
                                                R.get(s['id'], '')))
    nrep = sum(len(a.split()) for s, a in replaced.values())
    print('replaced after reconciliation: %d slots, %d old words -> %d new words at M' %
          (len(replaced), sum(len(s['rows']) for s, a in replaced.values()), nrep))
    if not write:
        return
    keep, out = [], []
    for ln in open(CT, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('line\t'):
            keep.append(ln)
    keep.insert(len(keep) - 1, '# 2 Oct 2026 (GAPS-fr4715-vieuville-pool-9, account-4): L-word pass (scripts/f67r_lword_pass.py): '
                'two blind Opus 5.5 readers on masked slots; an old L word both write -> H; a slot both readers agree on '
                'against the old reading is replaced at M only when the reconciler picks it; cipher tokens unchanged.\n')
    rep_rows = {(r['line'], r['pos']): sid for sid, (s, a) in replaced.items() for r in s['rows']}
    done = set()
    for line, rs in bylines(rows(CT)).items():
        pos = 0
        for r in rs:
            k = (r['line'], r['pos'])
            if k in rep_rows:
                sid = rep_rows[k]
                if sid in done:
                    continue
                done.add(sid)
                for w in replaced[sid][1].split():
                    pos += 1
                    out.append([line, str(pos), 'w:' + w, 'M', 'frame %s: replaced %s (A9=B9=recon; old %s)' %
                                (TAG, sid, ' '.join(x['token'][2:] for x in replaced[sid][0]['rows']))])
                continue
            pos += 1
            conf, note = r['conf'], r['note']
            if k in moved:
                conf, note = moved[k], (note + '; ' if note else '') + TAG + ': A9+B9 agree'
            out.append([line, str(pos), r['token'], conf, note])
    with open(CT, 'w', encoding='utf-8') as f:
        f.writelines(keep)
        for o in out:
            f.write('\t'.join(o) + '\n')
    print('wrote', CT)


if __name__ == '__main__':
    if '--build' in sys.argv:
        build(sys.argv[sys.argv.index('--build') + 1])
    elif '--score' in sys.argv:
        i = sys.argv.index('--score')
        rec = sys.argv[sys.argv.index('--recon') + 1] if '--recon' in sys.argv else None
        score(sys.argv[i + 1], sys.argv[i + 2], rec, '--write' in sys.argv)
    else:
        print(__doc__)

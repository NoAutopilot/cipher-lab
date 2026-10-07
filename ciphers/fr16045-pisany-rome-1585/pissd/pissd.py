"""D07-PISSD: page-internal same/different compare of the f.302v T40 tokens with the page's own C-graded T17 tokens.
  python3 pissd/pissd.py build   -> pissd/tok/*.jpg, pissd/blind/Q*.jpg (shuffled pairs, seed 20261007), pissd/blind/key.tsv
  python3 pissd/pissd.py score [--check] -> pissd/result.tsv from pissd/blind/reader.txt under PREREG_pissd.md
Run from the repository root or the target folder."""
import csv, os, random, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
def rows(f): return list(csv.DictReader(open(f'{H}/{f}'), delimiter='\t'))
def build():
    os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(H))))
    from strip import strip
    from PIL import Image, ImageDraw
    os.makedirs(f'{H}/tok', exist_ok=True); os.makedirs(f'{H}/blind', exist_ok=True)
    toks = {r['id']: r for r in rows('tokens.tsv')}; cache = {}; crop = {}
    for t, r in toks.items():
        if r['line'] not in cache: cache[r['line']] = strip(r['line'])
        s = cache[r['line']]; x = int(r['x_centre_strip'])
        c = s.crop((x - 60, 0, x + 60, s.size[1])); c.save(f'{H}/tok/f302v_{r["line"]}_i{r["tok_index"]}.jpg', quality=92); crop[t] = c
    pairs = rows('pairs.tsv'); rng = random.Random(20261007); rng.shuffle(pairs)
    out = ['q\tpair\tshown_left\tshown_right\tkind']
    for k, p in enumerate(pairs, 1):
        a, b = p['left'], p['right']
        if rng.random() < 0.5: a, b = b, a
        h = max(crop[a].size[1], crop[b].size[1]); im = Image.new('RGB', (120 * 2 + 40, h + 16), 'white')
        im.paste(crop[a], (0, 16)); im.paste(crop[b], (160, 16)); d = ImageDraw.Draw(im)
        for x0 in (60, 220): d.polygon([(x0 - 6, 0), (x0 + 6, 0), (x0, 12)], fill='red')
        d.line([(140, 0), (140, h + 16)], fill='black', width=2)
        im = im.resize((im.size[0] * 2, im.size[1] * 2), Image.LANCZOS); q = f'Q{k:02d}'
        im.save(f'{H}/blind/{q}.jpg', quality=92); out.append(f'{q}\t{p["pair"]}\t{a}\t{b}\t{p["kind"]}')
    open(f'{H}/blind/key.tsv', 'w').write('\n'.join(out) + '\n'); print(len(pairs), 'pairs')
def score(check):
    key = {r['q']: r for r in rows('blind/key.tsv')}; ans = {}
    for ln in open(f'{H}/blind/reader.txt'):
        p = [x.strip() for x in ln.rstrip('\n').split('\t')]
        if len(p) >= 3 and p[0] in key: ans[p[0]] = (p[1].upper(), p[2].lower())
    lines = ['q\tpair\tkind\tleft\tright\tanswer\tconf\toutcome']; cnt = {}
    for q, r in sorted(key.items()):
        a, c = ans.get(q, ('NONE', 'none')); firm = c in ('medium', 'high') and a in ('SAME', 'DIFFERENT')
        k = r['kind']
        if k in ('same', 'diff'):
            want = 'SAME' if k == 'same' else 'DIFFERENT'; o = 'right' if (firm and a == want) else 'wrong'
        elif k == 'test': o = ('SAME-T17' if a == 'SAME' else 'DIFF-T17') if firm else 'UNSETTLED'
        else: o = ('SAME-T16' if a == 'SAME' else 'DIFF-T16') if firm else 'UNSETTLED'
        cnt[(k, o)] = cnt.get((k, o), 0) + 1
        lines.append('\t'.join([q, r['pair'], k, r['shown_left'], r['shown_right'], a, c, o]))
    same = cnt.get(('same', 'right'), 0); diff = cnt.get(('diff', 'right'), 0)
    hard = sum(1 for l in lines[1:] if l.split('\t')[2] == 'diff' and l.split('\t')[7] == 'right' and {l.split('\t')[3][0], l.split('\t')[4][0]} == {'S', 'M'})
    gate = same >= 6 and diff >= 6 and hard >= 3
    ts = cnt.get(('test', 'SAME-T17'), 0); td = cnt.get(('test', 'DIFF-T17'), 0)
    verdict = ('NON-TEST (control FAIL)' if not gate else
               'MERGE (T40 tokens = T17; kp87b T40->s witness withdrawn)' if ts >= 6 and td == 0 else
               'DISTINCT (T40 tokens differ from T17)' if td >= 6 and ts == 0 else 'OPEN (mixed)')
    lines.append(f'# control same {same}/7, diff {diff}/7 (hard S-M {hard}/4); gate {"PASS" if gate else "FAIL"}; test SAME-T17 {ts}, DIFF-T17 {td}, UNSETTLED {10 - ts - td}; decoy {dict((o, v) for (k, o), v in cnt.items() if k == "decoy")}; verdict {verdict}')
    txt = '\n'.join(lines) + '\n'; f = f'{H}/result.tsv'
    if check:
        ok = os.path.exists(f) and open(f).read() == txt; print('up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(f, 'w').write(txt); print(txt)
if __name__ == '__main__':
    if sys.argv[1] == 'build': build()
    else: score('--check' in sys.argv)

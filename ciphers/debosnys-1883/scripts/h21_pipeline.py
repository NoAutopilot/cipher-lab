#!/usr/bin/env python3
"""H21 (28 Sept 2026): cryptogram 2 through the H2 recipe. Steps (each a subcommand):
  reconcile  passB_c2.tsv (assembled from the five reader files) vs passA.tsv rows of c2a/c2b, by position ->
             scripts/h21_disputed_positions.tsv and the pairwise numbers (full id, family)
  crops      per-sign 6x crops + row-context strips of the disputed positions -> scripts/h21_crops/ (gitignored)
  adjudicate passC_c2.tsv (assembled from the Fable reader files) -> ciphertext_c2_draft.tsv and rule-5 numbers;
             --check exits 1 if the draft is stale; on the 80 pct gate rewrites the cryptogram 2 sections of ciphertext.txt
Rule: scripts/PROMPTS_c1.md (H2 section, applied to c2 per its H21 section)."""
import csv, os, sys, json, collections
from PIL import Image, ImageDraw
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
PAGES = tuple(sys.argv[sys.argv.index('--pages') + 1].split(',')) if '--pages' in sys.argv else ('c2a', 'c2b')
TAG = 'c34' if '--pages' in sys.argv else 'c2'
def load_A():
    return {(r['line'], int(r['position'])): r for r in csv.DictReader(open(os.path.join(root, 'passA.tsv')), delimiter='\t') if r['line'].split('_')[0] in PAGES}
def load(p): return {(r['line'], int(r['position'])): r for r in csv.DictReader(open(os.path.join(root, p)), delimiter='\t')}
fam = {r['sign']: r['family'] for r in csv.DictReader(open(os.path.join(root, 'glyphs/inventory.tsv')), delimiter='\t')}
base = {r['sign']: r['base'] for r in csv.DictReader(open(os.path.join(root, 'glyphs/base_mark.tsv')), delimiter='\t')}
F = lambda s: fam.get(s, s); Bs = lambda s: base.get(F(s), base.get(s, F(s)))
def reconcile():
    A = load_A(); B = load(f'passB_{TAG}.tsv')
    miss = [k for k in A if k not in B]; extra = [k for k in B if k not in A]
    dis = [k for k in sorted(A) if k in B and A[k]['sign'] != B[k]['sign']]
    famdis = [k for k in sorted(A) if k in B and F(A[k]['sign']) != F(B[k]['sign'])]
    n = sum(1 for k in A if k in B)
    print(f"boxes {len(A)}; B rows matched {n} (A positions missing in B {len(miss)}, B extra {len(extra)})")
    print(f"position-based agreement full id {n-len(dis)}/{n} = {100*(n-len(dis))/n:.1f} pct; family {n-len(famdis)}/{n} = {100*(n-len(famdis))/n:.1f} pct; disputed {len(dis)}")
    with open(os.path.join(here, f'h21_disputed_positions{"_c34" if TAG == "c34" else ""}.tsv'), 'w') as f:
        f.write('line\tposition\n' + ''.join(f'{k[0]}\t{k[1]}\n' for k in dis))
    print(collections.Counter(k[0] for k in dis))
def crops():
    pages = json.load(open(os.path.join(root, 'glyphs/pages.json'))); out = os.path.join(here, 'h21_crops' if TAG == 'c2' else 'h23_crops'); os.makedirs(out, exist_ok=True)
    boxes = {(f"{r['page']}_L{int(r['line']):02d}", int(r['pos'])): r for r in csv.DictReader(open(os.path.join(root, 'glyphs/signs.tsv')), delimiter='\t') if r['page'] in PAGES}
    disp = [(r['line'], int(r['position'])) for r in csv.DictReader(open(os.path.join(here, f'h21_disputed_positions{"_c34" if TAG == "c34" else ""}.tsv')), delimiter='\t')]
    imgs = {p: Image.open(os.path.join(root, 'images', os.path.basename(pages[p]['image']))).convert('L') for p in PAGES}
    for line, pos in disp:
        pg = line.split('_')[0]; bx0, by0 = pages[pg]['box'][0], pages[pg]['box'][1]; page = imgs[pg]
        r = boxes[(line, pos)]; x, y, w, h = (int(r[k]) for k in 'xywh'); x += bx0; y += by0; pad = 6; name = f"{line}_p{pos:02d}"
        page.crop((x - pad, y - pad, x + w + pad, y + h + pad)).resize(((w + 2 * pad) * 6, (h + 2 * pad) * 6), Image.LANCZOS).save(os.path.join(out, name + '.png'))
        top = max(0, y - 18); band = page.crop((bx0, top, min(page.width, bx0 + 1100), y + h + 18)).convert('RGB'); d = ImageDraw.Draw(band)
        d.rectangle((x - bx0 - 2, y - top - 2, x - bx0 + w + 2, y - top + h + 2), outline=(255, 0, 0), width=2)
        band.resize((band.width * 2, band.height * 2), Image.LANCZOS).save(os.path.join(out, 'ctx_' + name + '.png'))
    print(len(disp), 'crops in', out)
def adjudicate(check=False):
    A = load_A(); B = load(f'passB_{TAG}.tsv'); C = load(f'passC_{TAG}.tsv'); rows = []; n = collections.Counter()
    if TAG == 'c34':  # verse line 1 (c4a0, H7): eye pass E and kNN K already agree on 10 of 16; carried as its own two-witness row set
        for r in csv.DictReader(open(os.path.join(root, 'passA.tsv')), delimiter='\t'):
            if r['line'].startswith('c4a0'): rows.append(dict(line=r['line'], position=int(r['position']), sign=r['sign'], confidence=r['confidence'], alt='', why='H7-eye+knn' if r['confidence'] == 'H' else 'H7-eye-only')); n['c4a0'] += 1
    for k in sorted(A):
        a = A[k]['sign']; b = B[k]['sign'] if k in B else None
        if b is None: rows.append(dict(line=k[0], position=k[1], sign=a, confidence='M', alt='', why='no-B')); n['unsettled'] += 1; continue
        if a == b: rows.append(dict(line=k[0], position=k[1], sign=a, confidence='H' if A[k]['confidence'] == 'H' and B[k]['confidence'] != 'L' else 'M', alt='', why='agree-AB')); n['agree-AB'] += 1; continue
        if k not in C: rows.append(dict(line=k[0], position=k[1], sign=a, confidence='M', alt='B:' + b, why='differ-noC')); n['unsettled'] += 1; continue
        c, cc = C[k]['sign'], C[k]['confidence']; n['C-read'] += 1; n['AC-full'] += c == a; n['BC-full'] += c == b; n['AC-fam'] += F(c) == F(a); n['BC-fam'] += F(c) == F(b)
        if c in ('MULTI', '_') and a not in ('MULTI', '_') and b not in ('MULTI', '_'):
            rows.append(dict(line=k[0], position=k[1], sign=a, confidence='M', alt=f'B:{b};C:{c}', why='seg-flag-C')); n['unsettled'] += 1; n['seg-flag'] += 1; continue
        v = collections.Counter([a, b, c]); top, cnt = v.most_common(1)[0]
        if cnt >= 2: rows.append(dict(line=k[0], position=k[1], sign=top, confidence='H' if (cnt == 3 or cc == 'H') else 'M', alt=';'.join(f'{t}:{x}' for t, x in (('A', a), ('B', b), ('C', c)) if x != top), why='settled-majority')); n['settled-full'] += 1; continue
        fv = collections.Counter([F(a), F(b), F(c)]); ft, fc = fv.most_common(1)[0]
        if fc >= 2: rows.append(dict(line=k[0], position=k[1], sign=ft, confidence='M', alt=f'A:{a};B:{b};C:{c}', why='family-settled')); n['settled-family'] += 1; continue
        bv = collections.Counter([Bs(a), Bs(b), Bs(c)]); bt, bc = bv.most_common(1)[0]
        if bc >= 2: rows.append(dict(line=k[0], position=k[1], sign=bt, confidence='M', alt=f'A:{a};B:{b};C:{c}', why='base-settled')); n['settled-base'] += 1; continue
        rows.append(dict(line=k[0], position=k[1], sign=a, confidence='M', alt=f'B:{b};C:{c}', why='three-way')); n['unsettled'] += 1; n['three-way'] += 1
    rows.sort(key=lambda r: ((0 if r['line'].startswith('c4a0') else 1 if r['line'].startswith('c4a') else 2 if r['line'].startswith('c4b') else -1), r['line'], r['position']))
    N = len(rows) - n['c4a0']; out = 'line\tposition\tsign\tconfidence\talt\twhy\n' + ''.join('\t'.join(str(r[c]) for c in ('line', 'position', 'sign', 'confidence', 'alt', 'why')) + '\n' for r in rows)
    p = os.path.join(root, f'ciphertext_{TAG}_draft.tsv')
    if check:
        if open(p).read() != out: print(f'STALE: ciphertext_{TAG}_draft.tsv'); sys.exit(1)
    else: open(p, 'w').write(out)
    full = n['agree-AB'] + n['settled-full']; famlvl = full + n['settled-family']; baselvl = famlvl + n['settled-base']; cr = max(1, n['C-read'])
    print(f"boxes {N}; agreed A=B {n['agree-AB']}; C read {n['C-read']}")
    print(f"(a) pairwise on disputed, full id: A-C {n['AC-full']}/{cr} = {n['AC-full']/cr:.3f}, B-C {n['BC-full']}/{cr} = {n['BC-full']/cr:.3f}; family: A-C {n['AC-fam']}/{cr}, B-C {n['BC-fam']}/{cr}")
    print(f"(b) settled full {n['settled-full']}, family {n['settled-family']}, base {n['settled-base']}; agreement over {N}: full {full}/{N} = {100*full/N:.1f} pct, family {100*famlvl/N:.1f} pct, base {100*baselvl/N:.1f} pct")
    print(f"(c) unsettled {n['unsettled']} (three-way {n['three-way']}, seg-flag {n['seg-flag']}); (d) type-noise floor {100*n['unsettled']/N:.1f} pct, ceiling {100*(n['unsettled']+n['settled-family']+n['settled-base'])/N:.1f} pct; gate 80 pct: {'MET' if full/N >= 0.8 else 'NOT MET'}")
    if full / N >= 0.8:
        secs = {'c2a': '=== Cryptogram 2 (page a) ===', 'c2b': '=== Cryptogram 2 (page b) ==='} if TAG == 'c2' else {'c3': '=== Cryptogram 3 ===', 'c4': '=== Cryptogram 4 ==='}; cp = os.path.join(root, 'ciphertext.txt'); ct = open(cp).read(); new = ct
        if TAG == 'c34' and '=== Cryptogram 4 ===' not in ct: new = ct.rstrip('\n') + '\n\n=== Cryptogram 4 ===\n\n'; ct = new
        for pg, hdr in secs.items():
            lines = collections.OrderedDict()
            for r in rows:
                if r['line'].startswith(pg) or (pg == 'c4' and r['line'].startswith('c4')): lines.setdefault(r['line'], []).append(r['sign'] + ('' if r['why'] in ('agree-AB', 'settled-majority', 'H7-eye+knn') else '?'))
            sec = hdr + f"\n# 28 Sept 2026 ({'H21' if TAG == 'c2' else 'H23'}): 160-id inventory ids, three passes adjudicated by scripts/PROMPTS_c1.md; a trailing ? marks a box unsettled at full id (alts in ciphertext_c2_draft.tsv)\n" + ''.join(' '.join(v) + '\n' for v in lines.values()) + '\n'
            i = new.index(hdr); j = new.find('=== Cryptogram', i + 1); j = len(new) if j < 0 else j; new = new[:i] + sec + new[j:]
        if check:
            if new != ct: print('STALE: ciphertext.txt cryptogram 2 sections'); sys.exit(1)
        else: open(cp, 'w').write(new)
if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    {'reconcile': reconcile, 'crops': crops, 'adjudicate': lambda: adjudicate('--check' in sys.argv)}.get(cmd, lambda: print(__doc__))()

#!/usr/bin/env python3
"""Sign-shape inventory sweep (FT4c, account-4, 3 Oct 2026): which of Sabran's 1636 cipher tables, if any,
shares f.157r's (DC8) sign set. Shape inventory only: no alignment, no reading.

Statistic (pre-registered in PREREG_sweep.md before any letter was scored):
  M  = DC8 sign classes with n >= 2 in ciphertext_draft.tsv.
  R_L = |M & I_L| / |M|, I_L = the set of DC8-named shape classes seen in letter L's cipher runs.
  D_L = how many of DC8's numeral codes {9, 7, 12, 10, 94} appear in L.
  Candidate iff R_L >= max(R over the three controls) + 0.10 AND D_L >= 2. (A first draft used R_f146 + 0.15; the
  calibration run, before any letter was read, showed the known non-key Lasry 1631 passes it, so it was raised.)
Controls: f.146r (blind two-pass inventory), Servien 1632 and Lasry fr.4134 1631 (both known non-keys);
their R values come from on-disk inventories and can differ from each other and from any letter.
Letter inventories: sweep_inventories.tsv (letter, folio, canvas, signs space-separated, note).
--check: exits 1 if sweep_result.tsv is stale."""
import csv, sys, collections, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
NUM = {'9', '7', '12', '10', '94'}

def rows(path):
    return [r for r in csv.DictReader((l for l in open(path) if not l.startswith('#')), delimiter='\t')]

def main():
    c = collections.Counter(r['sign'] for r in rows('ciphertext_draft.tsv'))
    M = {s for s, n in c.items() if n >= 2}
    inv = {}
    inv['CONTROL f146r (same family, not key)'] = {r['sign'] for r in rows('images/fr4140/key_f146.tsv')}
    inv['CONTROL servien1632 (not key)'] = {r['dc8_token'] for r in rows('key_servien_1632_letters.tsv')} - {'-'}
    inv['CONTROL lasry1631 (not key)'] = {r['dc8_token'] for r in rows('key_sabran_1631_letters.tsv')} - {'-'}
    for r in rows('sweep_inventories.tsv'):
        inv[f"{r['letter']} f.{r['folio']} c{r['canvas']}"] = set(r['signs'].split())
    base = max(len(M & I) / len(M) for k, I in inv.items() if k.startswith('CONTROL')) - 0.05
    out = ['unit\tR\tD\tshared\tcandidate']
    for k, I in inv.items():
        R = len(M & I) / len(M); D = len(NUM & I)
        cand = 'control' if k.startswith('CONTROL') else ('yes' if (R >= base + 0.15 and D >= 2) else 'no')
        out.append(f"{k}\t{R:.3f}\t{D}\t{' '.join(sorted(M & I))}\t{cand}")
    out.append(f"# M ({len(M)}): {' '.join(sorted(M))}; gate R >= {base + 0.15:.3f} and D >= 2")
    text = '\n'.join(out) + '\n'
    if '--check' in sys.argv:
        ok = open('sweep_result.tsv').read() == text
        print('sweep_result.tsv', 'current' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open('sweep_result.tsv', 'w').write(text); print(text)

main()

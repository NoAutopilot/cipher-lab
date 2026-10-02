#!/usr/bin/env python3
"""crib_align.py -- align the two unglossed closing cipher lines of NA 1.02.04 invnr 63 to the clear text that
stands beside them on the leaf, with two rule-3 controls (GAPS-na-schonenberg-1678-1716, 2 Oct 2026).

Hypothesis: L18 (5 groups, under the clear word "forma.") enciphers "forma", and L19 (23 groups, over the clear
address "A Dona Antonija de Albanylla &a") enciphers "adonaantonyadealbanylla" (23 letters; cipher spelling -y-
because key.tsv has 32=y at grade C). Statistic per placement: agreements between the crib letter and key.tsv's
value at the positions whose key value is resolved (grade C or M), reported as agree/resolved; a second, weaker
statistic counts U-grade positions whose passB tie set (key.tsv note column) contains the crib letter.

Controls (both can move the statistic, CLAUDE.md rule 3):
  slid-window  the same crib laid over every window of the same length in the glossed body L01-L14 (groups in
               reading order, key.tsv values at each window position): the distribution of agree/resolved a crib
               of this letter make-up reaches against real cipher text that does not say it.
  shuffled-crib the crib's letters permuted at L18's/L19's own positions (all 120 distinct permutations for
               "forma"; --shuffles random permutations for the address): the agreement a crib of these letters
               reaches here by chance.

Usage: python3 ciphers/na-schonenberg-1678-1716/crib_align.py [--shuffles 2000] [--seed 1] [--out crib_alignment.tsv]
Reads ciphertext.tsv and key.tsv beside it; writes crib_alignment.tsv (per-token table) and prints the numbers.
"""
import argparse, ast, collections, csv, itertools, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CRIBS = {'L18': 'forma', 'L19': 'adonaantonyadealbanylla'}
# '?9' (L19 pos 9, tens digit under a blot) is tested as 89 (=n, C) when the crib asks for n; recorded separately.
BLOT_CANDIDATES = {'?9': ['89', '59', '69', ')9']}

def load():
    ct = collections.defaultdict(list)
    with open(os.path.join(HERE, 'ciphertext.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            ct[r['line']].append(r)
    key = {}
    with open(os.path.join(HERE, 'key.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            tie = set()
            m = re.search(r"tied (\{.*?\})", r.get('note', ''))
            if m:
                tie = set(ast.literal_eval(m.group(1)).keys())
            key[r['code']] = dict(value=r['value'], grade=r['grade'], tie=tie, n=r['n'])
    return ct, key

def score(groups, crib, key):
    """agree, resolved, tie_hits, tie_tested, per-position rows."""
    agree = resolved = tie_hits = tie_tested = 0
    rows = []
    for g, c in zip(groups, crib):
        k = key.get(g)
        if k and k['value'] != '[?]':
            resolved += 1
            ok = k['value'] == c
            agree += ok
            rows.append((g, c, k['value'], k['grade'], 'agree' if ok else 'DISAGREE'))
        elif k and k['tie']:
            tie_tested += 1
            hit = c in k['tie']
            tie_hits += hit
            rows.append((g, c, '[?]', 'U', 'tie-set contains' if hit else 'tie-set lacks'))
        else:
            rows.append((g, c, '[?]', 'U', 'never glossed'))
    return agree, resolved, tie_hits, tie_tested, rows

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--shuffles', type=int, default=2000)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--out', default='crib_alignment.tsv')
    a = ap.parse_args()
    rng = random.Random(a.seed)
    ct, key = load()
    body = [r['group'] for ln in sorted(ct) if ln <= 'L14' for r in ct[ln]]
    out = [('line', 'pos', 'group', 'crib_letter', 'key_value', 'key_grade', 'result')]
    summary = {}
    for line, crib in CRIBS.items():
        groups = [r['group'] for r in ct[line]]
        assert len(groups) == len(crib), (line, len(groups), len(crib))
        # target
        g2 = [BLOT_CANDIDATES[g][0] if g in BLOT_CANDIDATES else g for g in groups]
        agree, resolved, th, tt, rows = score(g2, crib, key)
        for i, (g, c, v, gr, res) in enumerate(rows):
            out.append((line, i, groups[i], c, v, gr, res))
        # control 1: slid window over the glossed body
        n = len(crib)
        win = []
        for s in range(len(body) - n + 1):
            ag, rs, _, _, _ = score(body[s:s + n], crib, key)
            win.append((ag / rs if rs else 0.0, ag, rs))
        rates = sorted(w[0] for w in win)
        # control 2: shuffled crib at this line's own position
        if n <= 6:
            perms = sorted(set(itertools.permutations(crib)))
        else:
            perms = [tuple(rng.sample(crib, n)) for _ in range(a.shuffles)]
        sh = []
        for p in perms:
            ag, rs, _, _, _ = score(g2, ''.join(p), key)
            sh.append(ag / rs if rs else 0.0)
        sh.sort()
        t = agree / resolved
        summary[line] = dict(target=f'{agree}/{resolved} = {t:.3f}', tie=f'{th}/{tt}',
            slid=f'n={len(win)} mean={sum(rates)/len(rates):.3f} p95={rates[int(0.95*len(rates))-1]:.3f} max={rates[-1]:.3f} '
                 f'windows>=target={sum(r >= t for r in rates)}',
            shuf=f'n={len(sh)} mean={sum(sh)/len(sh):.3f} p95={sh[int(0.95*len(sh))-1]:.3f} max={sh[-1]:.3f} '
                 f'perms>=target={sum(r >= t for r in sh)} (identity permutation included)')
    with open(os.path.join(HERE, a.out), 'w', encoding='utf-8', newline='') as f:
        csv.writer(f, delimiter='\t').writerows(out)
    for line, s in summary.items():
        print(f"{line} crib '{CRIBS[line]}': target agree/resolved {s['target']}; U tie-sets containing crib letter {s['tie']}")
        print(f"   slid-window control (L01-L14, key.tsv values): {s['slid']}")
        print(f"   shuffled-crib control (same position):          {s['shuf']}")
    print(f"wrote {a.out}")

if __name__ == '__main__':
    main()

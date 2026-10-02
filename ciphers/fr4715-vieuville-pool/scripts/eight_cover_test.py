#!/usr/bin/env python3
"""GAPS-fr4715-vieuville-pool-7 (2 Oct 2026): key-side word-cover test of the 66 L06-L14 8-rule sites.

GAPS-4's inventory-only segmenter (f60r_blocks.dp) reads an out-of-key pair 0x as 8x ('8<'); 66 L06-L14 letter tokens
rest on that rule and sit at I. Blind visual re-reading is retired for this question (GAPS-6, rule 3 third-attempt
clause), so this is a different instrument, on disk only: for every site, the first digit is replaced by each
candidate 8, 0, 6, 9, 3 (second digit kept), the token is decoded with key_vieuville_nevers.tsv (an out-of-key pair,
all 0x and 33/34/35, breaks the run), every other token stays at its record value, and the score is the number of
letters covered by tools/data/fr16 words (scripts/keytest.py cover(), 3-14 letters, freq >= 3) in the decoded run(s)
touching the site. A candidate WINS a site when its score is strictly above every other candidate's.

Statistic: the share of the 66 sites that 8x wins. Licence for I -> H (the brief): 8x wins more sites than every
alternative AND the 8x win share beats a control, the same scoring applied to 66 sites drawn at random (20 seeds,
seed 20261002+k) from tokens whose first digit is settled (undotted in-key two-digit codes not resting on the rule,
first digit not 8, second digit matched to the target sites' second-digit counts) -- the share 8x wins where the
true digit is not 8 is the chance rate this design gives 8x. Known answer: the same scoring at settled tokens whose
true first digit is one of the candidates (8x read off the page in either block, 6x, 9x, 30), share where the true
digit wins -- the instrument's power. Both blocks' streams (L06-L14 and L25-L30 + L28b) are scored, each in its own
reading order. Disk only; no network; no vision.

    python3 scripts/eight_cover_test.py [--out witness/f60r_eight_cover.tsv]
"""
import argparse, csv, os, random, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f60r_blocks as fb
import keytest as kt

CANDS = ['8', '0', '6', '9', '3']


def stream(name, lines):
    """the block's token stream with an 8-rule flag per token, checked against the committed ciphertext."""
    codes = fb.key_codes()
    draft = os.path.join(fb.W, name + '_rec', 'ciphertext_draft.tsv')
    settled = {}
    sp = os.path.join(fb.W, name + '_settled.tsv')
    if os.path.exists(sp):
        for r in csv.DictReader(open(sp, encoding='utf-8'), delimiter='\t'):
            settled[(r['line'], r['position'])] = r['sign']
    by = {}
    for r in csv.DictReader([l for l in open(draft, encoding='utf-8') if not l.startswith('#')], delimiter='\t'):
        sign = settled.get((r['line'], r['position']), r['sign'])
        if sign in ('', '-', '_'):
            continue
        by.setdefault(r['line'], []).append(sign)
    toks = []
    for L in lines:
        for t in fb.segment_units(by.get(L, []), codes):
            toks.append((L, t.replace('8<', '8'), '8<' in t and not t.startswith('.')))
    committed = [r['token'] for r in csv.DictReader(
        [l for l in open(os.path.join(fb.TGT, name + '_ciphertext.tsv'), encoding='utf-8') if not l.startswith('#')],
        delimiter='\t')]
    assert [t for _, t, _ in toks] == committed, name + ': recomputed stream differs from the committed ciphertext'
    return toks


def as_key_tokens(toks):
    out = []
    for _, t, _ in toks:
        if t.startswith('w:') or t == '?' or t.startswith('.'):
            out.append(None)
        else:
            out.append(t)
    return out


def site_score(ktoks, i, code, valmap, words):
    """covered letters in the decoded run(s) touching position i with token i set to code."""
    lo = i
    while lo > 0 and ktoks[lo - 1] is not None and ktoks[lo - 1] in valmap:
        lo -= 1
    hi = i
    while hi + 1 < len(ktoks) and ktoks[hi + 1] is not None and ktoks[hi + 1] in valmap:
        hi += 1
    win = list(ktoks[lo:hi + 1]); win[i - lo] = code
    c, _ = kt.cover(kt.segments(win, valmap), words)
    return c


def score_site(ktoks, i, valmap, words):
    second = ktoks[i][1]
    sc = {d: site_score(ktoks, i, d + second, valmap, words) for d in CANDS}
    top = max(sc.values())
    winners = [d for d in CANDS if sc[d] == top]
    return sc, (winners[0] if len(winners) == 1 else None)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out', default=os.path.join(fb.W, 'f60r_eight_cover.tsv'))
    ap.add_argument('--seeds', type=int, default=20)
    a = ap.parse_args()
    key = kt.load_key()
    valmap = {r['sign']: r['value'] for r in key}
    words = kt.wordlist()
    blocks = {'upper': stream('f60r_blocks', fb.READ_LINES), 'lower': stream('f60r_lower', fb.LOWER_LINES)}
    kts = {b: as_key_tokens(s) for b, s in blocks.items()}

    rows, targets, pool, known = [], [], [], []
    for b, s in blocks.items():
        for i, (L, t, eight) in enumerate(s):
            if kts[b][i] is None or len(t) != 2 or not t.isdigit() or t not in valmap:
                continue
            if eight:
                if b == 'upper':
                    targets.append((b, i))
                continue
            if t[1] in '0345':
                if t[0] != '8':
                    pool.append((b, i))
                if t[0] in CANDS:
                    known.append((b, i))
    print('target sites (L06-L14, 8 rule): %d' % len(targets))
    out = open(a.out, 'w', encoding='utf-8')
    out.write('# GAPS-fr4715-vieuville-pool-7 (2 Oct 2026): scripts/eight_cover_test.py; per target site, covered letters '
              'under each candidate first digit; winner = strict maximum, "-" a tie\n')
    out.write('block\tline\tindex\trecord\t' + '\t'.join('cover_%sx' % d for d in CANDS) + '\twinner\n')
    wins = {d: 0 for d in CANDS}; ties = 0; tot = {d: 0 for d in CANDS}
    for b, i in targets:
        sc, w = score_site(kts[b], i, valmap, words)
        for d in CANDS:
            tot[d] += sc[d]
        if w:
            wins[w] += 1
        else:
            ties += 1
        out.write('%s\t%s\t%d\t%s\t%s\t%s\n' % (b, blocks[b][i][0], i, blocks[b][i][1],
                                                 '\t'.join(str(sc[d]) for d in CANDS), w or '-'))
    out.close()
    n = len(targets)
    print('target wins by candidate: ' + ', '.join('%sx %d' % (d, wins[d]) for d in CANDS) + ', ties %d (of %d)' % (ties, n))
    print('target total covered letters: ' + ', '.join('%sx %d' % (d, tot[d]) for d in CANDS))
    t8 = wins['8'] / n

    # control: matched second digits, first digit not 8, sites drawn without replacement from the settled pool
    need = {}
    for b, i in targets:
        need[kts[b][i][1]] = need.get(kts[b][i][1], 0) + 1
    bysec = {}
    for b, i in pool:
        bysec.setdefault(kts[b][i][1], []).append((b, i))
    print('control pool (settled, first digit not 8, second digit 0/3/4/5): %d; by second digit %s; target needs %s'
          % (len(pool), {k: len(v) for k, v in sorted(bysec.items())}, dict(sorted(need.items()))))
    cache = {}
    def won(site):
        if site not in cache:
            cache[site] = score_site(kts[site[0]], site[1], valmap, words)[1]
        return cache[site]
    shares = []
    for k in range(a.seeds):
        rng = random.Random(20261002 + k)
        pick = []
        for sec, m in need.items():
            src = bysec.get(sec, [])
            pick += rng.sample(src, m) if len(src) >= m else [rng.choice(src) for _ in range(m)]
        shares.append(sum(1 for s in pick if won(s) == '8') / len(pick))
    print('control 8x win share, %d seeds x %d sites: mean %.3f sd %.3f min %.3f max %.3f'
          % (a.seeds, n, statistics.mean(shares), statistics.stdev(shares), min(shares), max(shares)))
    print('target 8x win share %.3f; beats every seed: %s; rank %d of %d'
          % (t8, t8 > max(shares), 1 + sum(1 for x in shares if x >= t8), a.seeds + 1))
    allpool = [won(s) for s in pool]
    print('whole pool (%d settled non-8 sites): 8x wins %d (%.3f)' % (len(pool), allpool.count('8'), allpool.count('8') / len(pool)))

    # known answer: does the true first digit win at settled tokens?
    kr = {}
    for b, i in known:
        d = kts[b][i][0]
        kr.setdefault((b, d), [0, 0, 0])
        w = won((b, i))
        kr[(b, d)][0] += 1
        kr[(b, d)][1] += (w == d)
        kr[(b, d)][2] += (w == '8')
    print('known answer (settled tokens, true first digit in 8/6/9/3, second digit 0/3/4/5):')
    for (b, d), (m, ok, e8) in sorted(kr.items()):
        print('  %s %sx: %d sites, true digit wins %d (%.3f), 8x wins %d' % (b, d, m, ok, ok / m if m else 0, e8))
    for d in ['8', '6', '9', '3']:
        m = sum(v[0] for (b, dd), v in kr.items() if dd == d); ok = sum(v[1] for (b, dd), v in kr.items() if dd == d)
        if m:
            print('  both blocks %sx: %d sites, true digit wins %d (%.3f)' % (d, m, ok, ok / m))


if __name__ == '__main__':
    main()

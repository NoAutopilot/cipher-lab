#!/usr/bin/env python3
"""A1B-CEPPO-CRIB (3 Oct 2026): match clear-text crib words against a decoded cipher run, changing only M/U/I tokens.

  python3 crib_match.py TOKENS.tsv CRIBS.txt [--swap CRIBS2.txt] [--shuffles 1000] [--seed 1] [--out OUT.tsv]

TOKENS.tsv: reading_f*_tokens.tsv (line, pos, sign, conf, value, grade). CRIBS.txt: one word per line, '#' comments.
Each token is a slot: grade S -> its value is fixed (NULL S tokens are dropped); grade M/U/I -> an editable slot
holding its value ('' for NULL/unknown). A crib word w matches at a place in a line if the slots can be turned into w by
(a) substituting the letter of an editable slot (cost 1, an editable NULL slot filled with one letter also costs 1),
(b) dropping an editable slot (cost 1, cost 0 if it is already NULL/empty), with every S letter used in order and
unchanged, and total cost <= k(len w): k=0 for len 5, 1 for len 6-8, 2 for len >= 9; words under 5 letters are ignored.
Multi-letter values (et) are fixed letter runs when S, one editable slot holding 'et' when M (substituting it costs 1).
Spelling fold: lower case, v->u, j->i, y->i, accents stripped.
Statistic: number of distinct crib words with at least one match in the run. Controls: the same statistic on
--shuffles permutations of each line's token order (tokens keep their grades), and on the --swap crib list.
Pre-registered in NOTES.md (A1B-CEPPO-CRIB pre-registration) before any crib list was read against a run.
"""
import argparse, random, sys, unicodedata

def fold(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return ''.join({'v': 'u', 'j': 'i', 'y': 'i'}.get(c, c) for c in s if c.isalpha())

def kmax(n):
    return 0 if n == 5 else 1 if n <= 8 else 2

def load_tokens(path):
    lines = {}
    for i, row in enumerate(open(path, encoding='utf-8')):
        f = row.rstrip('\n').split('\t')
        if i == 0 or len(f) < 6:
            continue
        line, pos, sign, conf, value, grade = f[:6]
        v = '' if value in ('NULL', '', '?') else fold(value)
        lines.setdefault(line, []).append((v, grade == 'S', (line, pos)))
    return lines

def slots_of(toks):
    out = []  # (letters, fixed, tokid) ; fixed tokens expanded letter by letter
    for v, fixed, tid in toks:
        if fixed:
            out.extend((c, True, tid) for c in v)
        else:
            out.append((v, False, tid))
    return out

def match_at(slots, start, w, k):
    """DP from slots[start]: returns (cost, end, edited tokids) of the cheapest way to produce w exactly, or None."""
    n = len(w)
    best = None
    # state: (slot index, chars consumed) -> (cost, edits)
    frontier = {(start, 0): (0, ())}
    for _ in range(len(slots) - start + 1):
        nxt = {}
        for (i, j), (c, ed) in frontier.items():
            if j == n:
                if best is None or c < best[0]:
                    best = (c, i, ed)
                continue
            if i >= len(slots):
                continue
            let, fixed, tid = slots[i]
            cands = []
            if fixed:
                if let == w[j]:
                    cands.append(((i + 1, j + 1), c, ed))
            else:
                if let == '':
                    cands.append(((i + 1, j), c, ed))                     # empty slot skipped free
                    cands.append(((i + 1, j + 1), c + 1, ed + (tid,)))   # filled with w[j]
                else:
                    if w[j:j + len(let)] == let:
                        cands.append(((i + 1, j + len(let)), c, ed))       # kept as read
                    cands.append(((i + 1, j + 1), c + 1, ed + (tid,)))     # substituted
                    cands.append(((i + 1, j), c + 1, ed + (tid,)))         # dropped
            for key, cc, ee in cands:
                if cc <= k and (key not in nxt or nxt[key][0] > cc):
                    nxt[key] = (cc, ee)
        if not nxt:
            break
        frontier = nxt
    for (i, j), (c, ed) in frontier.items():
        if j == n and (best is None or c < best[0]):
            best = (c, i, ed)
    return best

def matches(lines, words):
    hits = []
    for line, toks in lines.items():
        slots = slots_of(toks)
        for w in words:
            k = kmax(len(w))
            for s in range(len(slots)):
                # a match must start on its first letter: a fixed slot equal to w[0] or an editable slot
                if slots[s][1] and slots[s][0] != w[0]:
                    continue
                m = match_at(slots, s, w, k)
                if m and m[1] > s:
                    hits.append((w, line, s, m[0], m[2], slots[s:m[1]]))
    return hits

def stat(lines, words):
    return len({h[0] for h in matches(lines, words)})

def load_words(path):
    ws = []
    for r in open(path, encoding='utf-8'):
        r = r.split('#')[0].strip()
        if r:
            w = fold(r)
            if len(w) >= 5 and w not in ws:
                ws.append(w)
    return ws

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('tokens'); ap.add_argument('cribs')
    ap.add_argument('--swap'); ap.add_argument('--shuffles', type=int, default=1000)
    ap.add_argument('--seed', type=int, default=1); ap.add_argument('--out')
    a = ap.parse_args()
    lines = load_tokens(a.tokens); words = load_words(a.cribs)
    hits = matches(lines, words)
    T = len({h[0] for h in hits})
    rng = random.Random(a.seed)
    per_word = {w: 0 for w in words}
    sh = []
    for _ in range(a.shuffles):
        L2 = {}
        for ln, toks in lines.items():
            t = toks[:]; rng.shuffle(t); L2[ln] = t
        hw = {h[0] for h in matches(L2, words)}
        sh.append(len(hw))
        for w in hw:
            per_word[w] += 1
    sh.sort()
    p95 = sh[int(0.95 * len(sh)) - 1] if sh else 0
    p = sum(1 for x in sh if x >= T) / max(1, len(sh))
    print(f'words {len(words)} (>=5 letters); target distinct words matched T={T}; '
          f'shuffle mean {sum(sh)/max(1,len(sh)):.2f} p95 {p95} max {sh[-1] if sh else 0} p(>=T) {p:.3f}')
    if a.swap:
        sw = load_words(a.swap)
        print(f'swap crib list ({len(sw)} words): distinct matched {stat(lines, sw)}')
    out = open(a.out, 'w', encoding='utf-8') if a.out else None
    if out:
        out.write('word\tline\tslot\tcost\tedited_tokens\tread_as\tword_shuffle_rate\n')
    for w, ln, s, c, ed, sl in hits:
        rate = per_word[w] / max(1, a.shuffles)
        read = ''.join(x[0] if x[1] else '[' + (x[0] or '-') + ']' for x in sl)
        row = f'{w}\t{ln}\t{s}\t{c}\t{",".join(t[1] for t in ed)}\t{read}\t{rate:.3f}'
        print('  ' + row)
        if out:
            out.write(row + '\n')

if __name__ == '__main__':
    main()

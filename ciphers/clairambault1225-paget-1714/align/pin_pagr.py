#!/usr/bin/env python3
"""A3V3-PAGR (4 Oct 2026): firm-neighbour pin, the instrument pre-registered in PREREG_pagr.md (committed 161fc920 before any run).

Per pair: gloss letters folded as tools/gibbs_align.prepare does; the pair's code tokens in order. FIRM tokens (H/C/S in the
pre-job reading, BASE_TOKENS below) emit exactly their value; every other code token emits 0-5 letters; uncovered gloss letters
only before the first / after the last code token. A token is pinned when its candidate chunk set over all complete alignments has
one member. Step 1 known-answer (hide each FIRM token), step 2 shuffled-value null (200 seeds, code -> value map of FIRM permuted),
then the per-token rulings for the PAGA proposals. Writes pin_pagr.txt and pin_pagr_rulings.tsv; --check exits 1 if stale or if an
S/H ruling is missing from ../exceptions.tsv.
    python3 pin_pagr.py [--check]
"""
import csv, os, random, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import gibbs_align as ga
import interlinear_align as ia

BASE = '4b518e74'  # reading_tokens.tsv state the FIRM set is taken from (PREREG_pagr.md)
MAXC = 5
SEEDS = 200
PROPOSALS = {'77': 'ce', '20': 'qui', '84': 'cette', '34': 'e', '38': 'i'}
RESTORE = {('f66L', '48'): ('158', 'mo')}  # row 5: back to H if pinned to its unchanged value


def base_tokens():
    txt = subprocess.run(['git', 'show', '%s:ciphers/clairambault1225-paget-1714/reading_tokens.tsv' % BASE], cwd=HERE,
                         capture_output=True, text=True, check=True).stdout
    return {(r['line'], r['pos']): r for r in csv.DictReader(txt.splitlines(), delimiter='\t')}


def candidates(g, emits):
    """emits: list per token of a fixed folded chunk (str) or None (free 0..MAXC; clear tokens pass '' fixed).
    -> list of candidate-chunk sets per token (empty sets if no complete alignment)."""
    n, L = len(emits), len(g)
    # fwd[i] = set of gloss offsets reachable after token i-1; overhang: token 0 may start anywhere
    fwd = [set() for _ in range(n + 1)]
    fwd[0] = set(range(L + 1))
    opts = []
    for e in emits:
        opts.append([e] if e is not None else None)
    def steps(i, a):
        e = emits[i]
        if e is not None:
            if g.startswith(e, a):
                yield a + len(e)
        else:
            for k in range(0, MAXC + 1):
                if a + k <= L:
                    yield a + k
    for i in range(n):
        for a in fwd[i]:
            for b in steps(i, a):
                fwd[i + 1].add(b)
    bwd = [set() for _ in range(n + 1)]
    bwd[n] = set(range(L + 1))  # overhang after the last token
    for i in range(n - 1, -1, -1):
        for a in range(L + 1):
            if any(b in bwd[i + 1] for b in steps(i, a)):
                bwd[i].add(a)
    out = []
    for i in range(n):
        s = set()
        for a in fwd[i] & bwd[i]:
            for b in steps(i, a):
                if b in bwd[i + 1]:
                    s.add(g[a:b])
        out.append(s)
    return out


def load():
    pairs = ia.load_pairs(os.path.join(HERE, 'pairs.tsv'))
    prep = ga.prepare(pairs)
    toks = base_tokens()
    units = []  # (pair, gloss, [(line,pos,code or None)])
    for p, codes, g in prep:
        pos = p['positions'].split(',')
        units.append((p, g, [(p['page'], pos[j], c) for j, c in enumerate(codes)]))
    return units, toks


def firm_map(toks):
    return {k: ga.fold(r['value'].lower()) for k, r in toks.items() if r['grade'] in ('H', 'C', 'S')}


def emits_for(seq, firm, hide=None, override=None):
    out = []
    for (line, pos, code) in seq:
        k = (line, pos)
        if code is None:
            out.append('')
        elif k == hide or k not in firm:
            out.append(None)
        else:
            out.append(override[code] if override is not None else firm[k])
    return out


def known_answer(units, toks, firm, override=None):
    pinned = right = 0
    for p, g, seq in units:
        for i, (line, pos, code) in enumerate(seq):
            k = (line, pos)
            if code is None or k not in firm:
                continue
            c = candidates(g, emits_for(seq, firm, hide=k, override=override))[i]
            if len(c) == 1:
                pinned += 1
                truth = override[code] if override is not None else firm[k]
                right += (next(iter(c)) == truth)
    return pinned, right


def targets(units):
    out = []
    for p, g, seq in units:
        for i, (line, pos, code) in enumerate(seq):
            if code is None:
                continue
            if str(code) in PROPOSALS or (line, pos) in RESTORE:
                out.append((p, g, seq, i))
    return out


def rule(units, firm, override=None):
    rows = []
    for p, g, seq, i in targets(units):
        line, pos, code = seq[i]
        prop = RESTORE[(line, pos)][1] if (line, pos) in RESTORE else PROPOSALS[str(code)]
        c = candidates(g, emits_for(seq, firm, hide=(line, pos), override=override))[i]
        rows.append((str(code), prop, p['plain_line'], line, pos, c))
    return rows


def main():
    units, toks = load()
    firm = firm_map(toks)
    out = []
    pn, rt = known_answer(units, toks, firm)
    out.append('step 1 known-answer: FIRM tokens %d, pinned %d (coverage %.3f), right %d (accuracy %.3f); gate >= 0.90 on >= 20 pinned: %s'
               % (len(firm), pn, pn / len(firm), rt, rt / pn if pn else 0, 'PASS' if pn >= 20 and rt / pn >= 0.9 else 'FAIL'))
    real = rule(units, firm)
    T = sum(1 for r in real if r[5] == {r[1]})
    # shuffled-value null: code -> value map of firm codes permuted across codes
    code_of = {}
    for p, g, seq in units:
        for (line, pos, code) in seq:
            if code is not None:
                code_of[(line, pos)] = code
    fcodes = sorted({code_of[k] for k in firm if k in code_of}, key=str)
    val = {}
    for k in firm:
        if k in code_of:
            val.setdefault(code_of[k], firm[k])  # one value per code (first seen)
    Ts, accs = [], []
    for s in range(SEEDS):
        vs = [val[c] for c in fcodes]
        random.Random(s).shuffle(vs)
        ov = dict(zip(fcodes, vs))
        Ts.append(sum(1 for r in rule(units, firm, override=ov) if r[5] == {r[1]}))
        if s < 20:
            a, b = known_answer(units, toks, firm, override=ov)
            accs.append(b / a if a else 0.0)
    Ts.sort()
    p95 = Ts[int(0.95 * SEEDS) - 1]
    out.append('step 2 shuffled-value null (%d seeds): target T = %d proposal tokens pinned to the proposal; shuffle mean %.2f, p95 %d, max %d; gate T > p95: %s'
               % (SEEDS, T, sum(Ts) / SEEDS, p95, Ts[-1], 'PASS' if T > p95 else 'FAIL'))
    out.append('          known-answer accuracy under the shuffle (first 20 seeds): mean %.3f' % (sum(accs) / len(accs)))
    gates = pn >= 20 and rt / pn >= 0.9 and T > p95
    rows = ['code\tproposal\tpair\tline\tposition\tcandidates\truling\twhy']
    for code, prop, pl, line, pos, c in real:
        cs = '|'.join(sorted(c)) if c else '(no complete alignment)'
        if not gates:
            g, why = 'M', 'gate failed: untested by this instrument'
        elif c == {prop}:
            g = 'H' if (line, pos) in RESTORE else 'S'
            why = 'pinned to the proposal by firm neighbours'
        elif len(c) == 1:
            g, why = 'M', 'pinned to another value'
        elif not c:
            g, why = 'M', 'pair has no complete alignment with the firm values'
        elif prop in c:
            g, why = 'M', 'admits the proposal, not pinned (%d candidates)' % len(c)
        else:
            g, why = 'M', 'proposal not admitted'
        rows.append('\t'.join([code, prop, pl, line, pos, cs, g, why]))
    txt = '\n'.join(out) + '\n'
    rtxt = '\n'.join(rows) + '\n'
    tp, rp = os.path.join(HERE, 'pin_pagr.txt'), os.path.join(HERE, 'pin_pagr_rulings.tsv')
    need = {(r.split('\t')[3], r.split('\t')[4], r.split('\t')[1], r.split('\t')[6]) for r in rows[1:] if r.split('\t')[6] in 'SH'}
    exc = os.path.join(HERE, '..', 'exceptions.tsv')
    have = {tuple(e[:4]) for e in (l.rstrip('\n').split('\t') for l in open(exc)) if len(e) > 3}
    if '--check' in sys.argv:
        ok = os.path.exists(tp) and open(tp).read() == txt and open(rp).read() == rtxt and need <= have
        print('pin_pagr up to date (%d S/H rulings in exceptions.tsv)' % len(need) if ok else 'pin_pagr STALE')
        sys.exit(0 if ok else 1)
    open(tp, 'w').write(txt)
    open(rp, 'w').write(rtxt)
    print(txt + rtxt)
    print('S/H rulings missing from exceptions.tsv: %d' % len(need - have))


if __name__ == '__main__':
    main()

"""COL26-LM (account 4, LANE DEFAULT-A4-0437-15, 15 Oct 2026): length-matched score for 11 = re and 81 = me.

Registration: ../PREREG-COL26-LM.md. COL26-1181 found decode_key --try's window score cannot tell a right two-letter
value from a one-letter stand-in here (value-class control 1/5). This instrument compares only like with like: a
two-letter candidate V for code X is scored (decode_key.Crossword.score: window +-8 under tools/data/fr17, the same
3-bit word penalty for every alternative, so it cancels) against the 60 commonest two-letter letter pairs of the
fr17 corpus (folded, within-word, V excluded) put in its place. Accept = score(V) above the p95 of those 59-60
alternatives (rank in the top 5%). Streams = held-out (f23 + the key_f23-family sibling units; c50 left out, the
candidates came from c50), key key_f23.tsv (never written), built by siblings/c1181_try.py's own stream builder.

Gate (before 11 and 81 are scored): the five two-letter C codes 16 se, 28 la, 33 ux, 36 ez, 51 de. True value tried
(5 trials), each of the other four control values planted as a false candidate (20 trials).
  G1 full n: true accepted >= 4/5 AND false rejected >= 18/20 (>= 90%).
  G2 at each target's n (11: its held-out n; 81: its held-out n): 20 random draws per control code of that many of the
     code's occurrences (seed 0); mean true acceptance >= 0.8 AND mean false acceptance <= 0.10. A target is scored
     only if G1 and its own G2 pass; otherwise its line reads NON-TEST.
Target verdict: accept / reject per the same rule, reported with rank and margin over p95. Writes siblings/c_lm_len_out.txt
with --write; --check re-runs and fails if the committed output differs.
"""
import collections, glob, gzip, os, random, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import c1181_try as c1  # noqa: E402
import decode_key as dk  # noqa: E402

OUT = os.path.join(HERE, 'c_lm_len_out.txt')
CONTROL = [('16', 'se'), ('28', 'la'), ('33', 'ux'), ('36', 'ez'), ('51', 'de')]
TARGETS = [('11', 're'), ('81', 'me')]
LM = 'tools/data/fr17'
NALT, DRAWS = 60, 20


def bigram_class():
    d = os.path.join(ROOT, LM)
    cnt = collections.Counter()
    for p in sorted(glob.glob(os.path.join(d, '*.txt')) + glob.glob(os.path.join(d, '*.txt.gz'))):
        op = gzip.open if p.endswith('.gz') else open
        with op(p, 'rt', encoding='utf-8', errors='ignore') as f:
            for w in f.read().split():
                w = dk.lm_fold(w)
                for i in range(len(w) - 1):
                    cnt[w[i:i + 2]] += 1
    return [b for b, _ in cnt.most_common(NALT + 5)]


def test(cw, code, val, cls, occ=None):
    fv = dk.lm_fold(val)
    alts = [b for b in cls if b != fv][:NALT]
    s = cw.score(code, val, occ=occ)
    null = sorted((cw.score(code, b, occ=occ) for b in alts), reverse=True)
    p95 = null[max(0, int(round(0.05 * len(null))) - 1)]
    rank = 1 + sum(1 for x in null if x >= s)
    return s > p95, rank, s - p95, len(alts)


def main():
    write, check = '--write' in sys.argv, '--check' in sys.argv
    out = []
    cls = bigram_class()
    out.append(f'# COL26-LM length-matched score; lm {LM}; window 8; class = top {NALT} fr17 letter pairs (V excluded)')
    out.append('# class: ' + ' '.join(cls[:NALT]))
    with tempfile.TemporaryDirectory() as tmp:
        f23, c50, sibs = c1.base_jobs(tmp)
        cfgjobs = [{k: v for k, v in j.items() if k != 'name'} for j in [f23] + sibs]
        cw = dk.Crossword(T, cfgjobs, dk.lm_load(LM), window=8)
    n = {c: len(cw.occ(c)) for c, _ in CONTROL + TARGETS}
    out.append('# held-out occurrences: ' + ' '.join(f'{c}:{n[c]}' for c in n))
    out.append('## G1 full n (code value kind accept rank margin_bits nalt)')
    ta = fa = 0
    for code, true in CONTROL:
        for v in [true] + [w for _, w in CONTROL if w != true]:
            ok, rank, m, na = test(cw, code, v, cls)
            kind = 'true' if v == true else 'false'
            ta += ok and kind == 'true'
            fa += ok and kind == 'false'
            out.append(f'{code}\t{v}\t{kind}\t{"accept" if ok else "reject"}\t{rank}\t{m:+.1f}\t{na}')
    g1 = ta >= 4 and (20 - fa) >= 18
    out.append(f'G1: true accepted {ta}/5, false rejected {20 - fa}/20 -> {"PASS" if g1 else "FAIL"}')
    g2 = {}
    for tcode, _ in TARGETS:
        k = n[tcode]
        rng = random.Random(0)
        tr, fr = [], []
        for code, true in CONTROL:
            occ = cw.occ(code)
            for _ in range(DRAWS):
                sub = occ if len(occ) <= k else rng.sample(occ, k)
                for v in [true] + [w for _, w in CONTROL if w != true]:
                    ok = test(cw, code, v, cls, occ=sub)[0]
                    (tr if v == true else fr).append(ok)
        mt, mf = sum(tr) / len(tr), sum(fr) / len(fr)
        g2[tcode] = mt >= 0.8 and mf <= 0.10
        out.append(f'G2 at n={k} (target {tcode}): mean true acceptance {mt:.3f}, mean false acceptance {mf:.3f} -> '
                   f'{"PASS" if g2[tcode] else "FAIL"}')
    out.append('## targets')
    for code, v in TARGETS:
        if not (g1 and g2[code]):
            out.append(f'{code}={v}: NON-TEST (gate {"G1" if not g1 else "G2"} failed); not scored')
            continue
        ok, rank, m, na = test(cw, code, v, cls)
        cur = cw.current(code)
        out.append(f'{code}={v}: {"accept" if ok else "reject"} rank {rank}/{na + 1} margin over p95 {m:+.1f} bits '
                   f'(n {n[code]}; current key value {cur})')
    body = '\n'.join(out) + '\n'
    if check:
        same = os.path.exists(OUT) and open(OUT, encoding='utf-8').read() == body
        print('c_lm_len: up to date' if same else 'c_lm_len: STALE')
        return 0 if same else 1
    if write:
        open(OUT, 'w', encoding='utf-8').write(body)
    sys.stdout.write(body)
    return 0


if __name__ == '__main__':
    sys.exit(main())

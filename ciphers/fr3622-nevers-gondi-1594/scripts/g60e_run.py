#!/usr/bin/env python3
"""BNF-G60E: f.91 ciphertext.tsv under the unchanged g60d_instrument (no.60 key, Viterbi fr16 4-gram, value-string
nulls within class L/S/W). Registered in .claude/briefs/runs/2026-10-08-ytbiz-bnf-g60e.md. Usage: g60e_run.py [SHUF] [SEED]"""
import sys, random, statistics
from pathlib import Path
here = Path(__file__).resolve().parent; sys.path.insert(0, str(here))
import g60d_instrument as G, judge_plaintext as J
D = here.parent
def seq_of(path):
    s = []
    for l in Path(path).read_text().splitlines():
        if l.strip() and '\t' in l:
            s += [t.rstrip('?') for t in l.split('\t')[1].split() if not t.startswith('w:')]
    return s
def main():
    shuf = int(sys.argv[1]) if len(sys.argv) > 1 else 200; seed = int(sys.argv[2]) if len(sys.argv) > 2 else 6001
    key = G.load_key(); inst = G.Inst(); seq = seq_of(D / "ciphertext.tsv")
    unk = [t for t in seq if t not in key]
    print(f"N tags {len(seq)}; in key {len(seq)-len(unk)}; not in key (U) {len(unk)}: {sorted(set(unk))}")
    ra, rb = inst.stats(seq, key); print("viterbi text:", inst.viterbi(seq, key))
    rnd = random.Random(seed); nul = [inst.stats(seq, G.make_null(key, rnd)) for _ in range(shuf)]
    na = sorted(x[0] for x in nul); nb = sorted(x[1] for x in nul)
    for nm, r, n in (("(a) 4-gram", ra, na), ("(b) word cover", rb, nb)):
        print(f"{nm}: real {r:.3f} shuffled mean {statistics.mean(n):.3f} p95 {J.pct(n,.95):.3f} p99 {J.pct(n,.99):.3f} rank {sum(x<r for x in n)}/{len(n)}")
if __name__ == "__main__": main()

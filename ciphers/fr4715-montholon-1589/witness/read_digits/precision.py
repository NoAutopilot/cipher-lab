"""Non-gating precision diagnostic (MONT-READ-DIGITS definition, committed by MONT-RECROP 27 Sept 2026; reproduces
precision_A.txt exactly): LCS(read digits excl ?, dump window = anchored span +-8 groups) / digits read; control:
within-line digit shuffle, 20, seed 1. Run from the target folder: python3 witness/read_digits/precision.py TSV"""
import sys, random
sys.path.insert(0, 'scripts'); import mont4715c as m
dump, spans = m.dump_spans()
rec = m.read_stream_tsv(sys.argv[1]); rng = random.Random(1)
tot = hit = 0; ctl = [0] * 20
for ln in "L03,L08,L13,L15".split(","):
    js = spans[ln]; ref = dump[max(0, js[0] - 8):js[-1] + 9]
    rd = list(m.groups_stream(ref).replace("'", ""))
    dig = [c for c, _ in m.stream_of(rec[ln]) if c != "?"]
    v = m.lcs_len(dig, rd); tot += len(dig); hit += v
    print(f"{ln}: {v}/{len(dig)} = {v/len(dig):.3f}")
    for i in range(20):
        d2 = dig[:]; rng.shuffle(d2); ctl[i] += m.lcs_len(d2, rd)
print(f"pooled precision {hit}/{tot} = {hit/tot:.3f}; control (within-line digit shuffle, 20, seed 1) mean {sum(ctl)/20/tot:.3f}")

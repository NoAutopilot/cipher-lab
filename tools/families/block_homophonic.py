"""block_homophonic: a numeral table cut into contiguous blocks of `width` values, one letter per block (AX-4612,
26 Sept 2026, LANE AX). The Nassau 1573-74 table (ciphers/lodewijk-van-nassau-1573-74/key.tsv) is this design at
width 5, offset 0: values 1-5 = n, 6-10 = o, ... 116-120 = m. A letter that changed its table but kept the design
differs only in which letter each block carries (a 24-block substitution), so the solver anneals the block -> letter
map only, never the value -> letter map: the ciphertext is first rewritten as block labels and handed to the
masc/homophonic annealer (tools/homophonic_anneal.py, imported, not copied), which assigns one letter per block.

params (all --param k=v):
  width=5     values per block
  offset=0    block boundaries shifted by `offset`: block k holds values offset+1+k*width .. offset+(k+1)*width,
              wrapping inside lo..hi (so offset 2 at width 5 makes 3,4,5,6,7 one block and 118,119,120,1,2 another)
  lo=1 hi=120 the value range the table covers; tokens outside it are refused (drop them in the spec, and say so)
  gap=0       control only: letters of plaintext cut out between consecutive target messages, standing in for the
              clear words that interrupt the numeral runs in a mixed clear/cipher letter (4612: 351 clear-word
              tokens over 19 interruptions, about 80 letters each -> --param gap=80)
  iters=40000 order=3 uni_weight=1.0   passed to homophonic_anneal.solve

Matched control (rule 3, the brief's design): a plaintext window of the target's N letters (with `gap` letters cut
at each of the target's own message boundaries) under a table of the SAME width and offset with a random block
order: the nb = (hi-lo+1)//width blocks carry a random permutation of the alphabet's letters (nb < 24: the nb most
frequent corpus letters, the rest of the plaintext's letters encoded by a random value in range, i.e. unreadable by
design; nb > 24: the extra blocks carry letters drawn by corpus frequency). Within a block, each occurrence draws a
value with probability proportional to the TARGET's own count of that value (+0.5), so the control carries the
target's uneven value-use profile. Recovery = share of letter positions read correctly.

Test: python3 tools/tests/test_block_homophonic.py (offline, under a minute)."""
import random
import homophonic_anneal as ha
from collections import Counter
from families import draw_window

DESCRIPTION = ("contiguous-block homophonic table (--param width=5 offset=0 lo=1 hi=120): the solver anneals the "
               "block -> letter map only; control = same width/offset, random block order, target's value profile")


def _p(params, k, d):
    return type(d)(params.get(k, d))


def geometry(params):
    w, o = _p(params, "width", 5), _p(params, "offset", 0)
    lo, hi = _p(params, "lo", 1), _p(params, "hi", 120)
    if w < 1 or not 0 <= o < w:
        raise SystemExit(f"block_homophonic: need width >= 1 and 0 <= offset < width (got {w}, {o})")
    return w, o, lo, hi


def block_of(v, w, o, lo, hi):
    """Block index of value v: ((v - lo - o) mod range) // width."""
    return ((v - lo - o) % (hi - lo + 1)) // w


def blocks(w, o, lo, hi):
    """{block index: [values]} for the table geometry."""
    out = {}
    for v in range(lo, hi + 1):
        out.setdefault(block_of(v, w, o, lo, hi), []).append(v)
    return out


def to_blocks(msgs, params):
    w, o, lo, hi = geometry(params)
    out = []
    for m in msgs:
        row = []
        for t in m:
            v = int(t)
            if not lo <= v <= hi:
                raise SystemExit(f"block_homophonic: token {t} outside lo..hi {lo}..{hi}; drop it in the spec")
            row.append(f"b{block_of(v, w, o, lo, hi)}")
        out.append(row)
    return out


def make_control(spec, seed, corpora, params):
    N = params["N"]
    w, o, lo, hi = geometry(params)
    gap = _p(params, "gap", 0)
    lengths = params.get("lengths") or [N]
    text = ha.fold("\n".join(corpora))
    total = N + gap * (len(lengths) - 1)
    window, rest = draw_window(text, total, seed)
    plain, pos = [], 0
    for L in lengths:
        plain.append(window[pos:pos + L])
        pos += L + gap
    plain = "".join(plain)[:N]
    model = ha.Model([rest], _p(params, "order", 3))
    rng = random.Random(seed + 4612)
    table = blocks(w, o, lo, hi)
    nb = len(table)
    letters = sorted(ha.ALPHA, key=lambda a: -model.freq[a])
    use = letters[:nb]
    rng.shuffle(use)
    extra = rng.choices(letters, [model.freq[a] for a in letters], k=max(0, nb - len(use)))
    block_letter = dict(zip(sorted(table), use + extra))
    by_letter = {}
    for b, a in block_letter.items():
        by_letter.setdefault(a, []).extend(table[b])
    tc = Counter(int(t) for m in params.get("target_msgs") or [] for t in m)
    seq = []
    for a in plain:
        vals = by_letter.get(a)
        if not vals:  # letter without a block in this geometry: unreadable by design
            seq.append(str(rng.randint(lo, hi)))
            continue
        seq.append(str(rng.choices(vals, [tc.get(v, 0) + 0.5 for v in vals])[0]))
    msgs, pos = [], 0
    for L in lengths:
        msgs.append(seq[pos:pos + L])
        pos += L
    return msgs, plain, [rest]


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    model = ha.Model(corpora, _p(params, "order", 3))
    bmsgs = to_blocks(cipher_msgs, params)
    seq = [s for m in bmsgs for s in m]
    res = ha.solve(seq, model, restarts, _p(params, "iters", 40000), seed, _p(params, "uni_weight", 1.0))
    sc, key = res[0]
    w, o, lo, hi = geometry(params)
    table = {k: f"{v[0]}-{v[-1]}" for k, v in blocks(w, o, lo, hi).items()}
    bk = {table[int(b[1:])]: a for b, a in sorted(key.items(), key=lambda x: int(x[0][1:]))}
    return "".join(key[x] for x in seq), sc, {"restart_scores": [round(r[0], 1) for r in res], "block_key": bk}


def score_recovery(plain, truth):
    n = max(1, len(truth))
    return sum(1 for a, b in zip(plain, truth) if a == b) / n

#!/usr/bin/env python3
"""Offline test for tools/families/block_homophonic.py (AX-4612, 26 Sept 2026). No network. Checks:
(1) geometry: width 5 offset 0 over 1..120 gives 24 blocks of five, 1-5 block 0; offset 2 wraps 118,119,120,1,2
    into one block and puts 3-7 in block 0; a token outside lo..hi is refused.
(2) key.tsv round trip: the Nassau 1574 table (blocks of five from 1, letters n o p ... m) rewritten as block
    labels gives one block per letter, so the family's reduction loses nothing for the known design.
(3) make_control: N tokens split into the target's message lengths, every token in range, values drawn only from
    the block of the plaintext letter's own table entry, and `gap` letters cut between messages.
(4) known answer: a French plaintext of about 800 letters under a random-order width-5 table is read back by
    solve() at >= 0.8 recovery (the annealer on 24 block labels is a masc problem; small iters keep this fast).
Run: python3 tools/tests/test_block_homophonic.py"""
import os, sys, csv
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp  # noqa: E402
from families import block_homophonic as bh  # noqa: E402

FR = os.path.join(ROOT, "tools", "data", "fr16", "lettresindites00marg_djvu.txt.gz")


def test_geometry():
    b = bh.blocks(5, 0, 1, 120)
    assert len(b) == 24 and b[0] == [1, 2, 3, 4, 5] and b[23] == [116, 117, 118, 119, 120], b
    b2 = bh.blocks(5, 2, 1, 120)
    assert sorted(b2[23]) == [1, 2, 118, 119, 120] and b2[0] == [3, 4, 5, 6, 7], (b2[0], b2[23])
    assert len(bh.blocks(4, 0, 1, 120)) == 30 and len(bh.blocks(6, 0, 1, 120)) == 20
    try:
        bh.to_blocks([["121"]], {"width": "5"})
    except SystemExit:
        pass
    else:
        raise AssertionError("token 121 outside 1..120 was not refused")
    print("ok: geometry (24/30/20 blocks, offset wrap, out-of-range refused)")


def test_key_roundtrip():
    rows = csv.DictReader(open(os.path.join(ROOT, "ciphers", "lodewijk-van-nassau-1573-74", "key.tsv")), delimiter="\t")
    key = {int(r["code"]): r["value"] for r in rows if r["code"].isdigit() and int(r["code"]) <= 120}
    per_block = {}
    for v, a in key.items():
        per_block.setdefault(bh.block_of(v, 5, 0, 1, 120), set()).add(a)
    assert len(per_block) == 24 and all(len(s) == 1 for s in per_block.values()), per_block
    assert len({next(iter(s)) for s in per_block.values()}) == 24
    print("ok: key.tsv is 24 single-letter blocks of five at offset 0")


def test_control_shape():
    corpora = [jp.read_corpus(FR)]
    target = [[str(v) for v in (2, 4, 12, 26, 81, 81, 2)] * 20, ["12", "26"] * 30]
    N = sum(map(len, target))
    params = {"N": N, "K": 6, "lengths": [len(m) for m in target], "target_msgs": target, "width": "5", "gap": "40"}
    cm, plain, train = bh.make_control({}, 3, corpora, params)
    assert [len(m) for m in cm] == params["lengths"] and len(plain) == N
    toks = [int(t) for m in cm for t in m]
    assert all(1 <= t <= 120 for t in toks)
    # one letter per block: a value's block always stands for the same plaintext letter
    seen = {}
    for t, a in zip(toks, plain):
        b = bh.block_of(t, 5, 0, 1, 120)
        assert seen.setdefault(b, a) == a, (t, b, a, seen[b])
    # the target's profile weights the draw: within the blocks used, the target's heavy values dominate
    # the target's profile weights the draw: in a block holding one of the target's heavy values, that value
    # (weight 20.5+ against 0.5 for an unused neighbour) carries most of the block's draws
    c = Counter(toks)
    checked = 0
    tc = Counter(int(t) for m in target for t in m)
    for blk in bh.blocks(5, 0, 1, 120).values():
        tot = sum(c[u] for u in blk)
        tw = [tc.get(u, 0) + 0.5 for u in blk]
        if tot >= 10 and max(tw) > 0.6 * sum(tw):  # a block the target's own profile makes lopsided
            v = blk[tw.index(max(tw))]
            assert c[v] > 0.4 * tot, (v, c[v], tot)
            checked += 1
    assert checked >= 1, "no heavy block drawn often enough to check"
    print(f"ok: control shape (N={N}, messages {params['lengths']}, one letter per block, {checked} heavy blocks profile-weighted)")


def test_known_answer():
    corpora = [jp.read_corpus(FR)]
    N = 800
    params = {"N": N, "K": 100, "lengths": [N], "target_msgs": [[str(v) for v in range(1, 121)]], "width": "5",
              "offset": "0", "iters": "15000"}
    cm, plain, train = bh.make_control({}, 7, corpora, params)
    dec, sc, info = bh.solve(cm, {}, 7, 3, train, params)
    rec = bh.score_recovery(dec, plain)
    assert rec >= 0.8, (rec, dec[:80], plain[:80])
    # the wrong offset must not read as well (the geometry is what the family tests)
    p2 = dict(params, offset="2")
    dec2, _, _ = bh.solve(cm, {}, 7, 3, train, p2)
    rec2 = bh.score_recovery(dec2, plain)
    assert rec2 < rec, (rec, rec2)
    print(f"ok: known answer N={N} width 5 offset 0 recovery {rec:.3f}; wrong offset 2 reads {rec2:.3f}")


if __name__ == "__main__":
    test_geometry()
    test_key_roundtrip()
    test_control_shape()
    test_known_answer()
    print("all block_homophonic tests passed")

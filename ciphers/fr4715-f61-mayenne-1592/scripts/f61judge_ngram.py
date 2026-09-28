#!/usr/bin/env python3
"""F61-108V-NGRAM (campaign step H93, 28 Sept 2026, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only: a model-free check of
the H85 judge result. Every set's resolution in a verdict file is scored by tools/judge_plaintext.py's NgramModel (4-gram,
add-k) built on LANG_CORPORA["fr"] (fr16: 16th-century French letters); a set's score is the letter-weighted mean log10
probability per letter over its lines. The null is the same judge's resolutions of the 20 permuted maps in the same call,
so the Frenchness the judge's within-pair choices add is present on both sides. Gate (pre-registered in CAMPAIGN.md H93):
the target ranks 1 of 21 by this score in all three f.108v calls. The control call (known lines) and the fr16 real-text
p05 / shuffled p99 at the f.108v length are reported for context. -> scripts/f61judge_ngram_result.txt [--check]"""
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); sys.path.insert(0, f"{ROOT}/tools")
import judge_plaintext as jp
M = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA["fr"]])
def sc(reading):
    lines = [jp.fold(x) for x in reading.split("|")]; lines = [l for l in lines if len(l) >= 4]
    n = sum(len(l) - 3 for l in lines)
    return sum(M.score(l) * (len(l) - 3) for l in lines) / n if n else -9.9, sum(len(l) for l in lines)
out, gate = [], []
HARD = "--hard" in sys.argv   # H103: the one-swap hard-null calls (H102 control, H100 target); gate: target rank 1 in the f.108v call
TAGS = ("known_h51_swaps105", "f108v_swaps105") if HARD else ("known_h51_s101", "f108v_s101", "f108v_s102", "f108v_s103")
for tag in TAGS:
    k = json.load(open(f"{HERE}/f61judge_{tag}_key.json"))["key"]; tgt = [l for l, m in k.items() if m == 0][0]
    rows = {r["label"].strip(): r for r in csv.DictReader((l for l in open(f"{HERE}/f61judge_{tag}_verdict.tsv") if not l.startswith("#")), delimiter="\t")}
    S = {l: sc(r["reading"]) for l, r in rows.items()}
    rank = 1 + sum(1 for l, v in S.items() if l != tgt and v[0] >= S[tgt][0])
    others = sorted((v[0] for l, v in S.items() if l != tgt), reverse=True)
    out.append(f"{tag}: target {tgt} {S[tgt][0]:.3f} ({S[tgt][1]} letters); best permuted {others[0]:.3f}, median permuted {others[len(others) // 2]:.3f}; rank {rank} of 21")
    if tag.startswith("f108v"): gate.append(rank == 1)
N = 274; real, null, _ = M.controls(N)
out.append(f"fr16 context at {N} letters: real-text p05 {jp.pct(real, 0.05):.3f}, median {jp.pct(real, 0.5):.3f}; letter-shuffled p99 {jp.pct(null, 0.99):.3f}")
out.append(f"GATE {'H103' if HARD else 'H93'}: target rank 1 of 21 in {'the f.108v call' if HARD else 'all three f.108v calls'} -> {'PASS' if all(gate) else 'FAIL'}")
txt = "\n".join(out) + "\n"; res = f"{HERE}/f61judge_ngram{'_hard' if HARD else ''}_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")

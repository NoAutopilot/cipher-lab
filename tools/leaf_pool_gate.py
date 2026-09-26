#!/usr/bin/env python3
"""Per-leaf gate before a transcribed leaf's signs enter a shared ciphertext pool (CLAUDE.md rule 3, per-unit
merge-gate paragraph; LANE B9, 26 Sept 2026, malsburg-hessen-1636 pool wave).

A leaf read by two blind passes and reconciled (tools/reconcile_passes.py -> ciphertext_draft.tsv) is admitted
to the pool only if all three hold:
  (1) quality: share of M-graded signs <= --max-m (default 0.15);
  (2) form: share of signs outside the pool's sign grammar (--form regex, default: 1-3 digits, or one capital
      mark / '#', or a clear word of 2+ letters starting with a capital) <= --max-offform (default 0.05);
  (3) same system: the cosine similarity of the leaf's value-frequency vector with the pool's beats the same
      cosine after a random relabelling of the leaf's distinct values onto the pool's value space (--shuffles,
      default 200): real cosine > relabel p95. The relabel changes which value carries which frequency, which
      is what the cosine measures, so the control can fail differently from the target (rule 3's
      orthogonal-control paragraph). Plain vocabulary overlap is reported but does not gate: a K=95 nomenclator
      saturates the two-digit space, so any two-digit leaf overlaps it. A leaf in a different key (or read as
      noise) has its frequent values in different places and sits inside the relabel band.
A leaf failing any gate is held: its signs stay out of the pool (reported, not merged) -- except a leaf that
clears form and system but fails only quality (M-share): its H-graded signs are pooled for frequency/system
purposes (`pooled_h_only`), and only its M-graded signs stay out of value attestation, the per-token version of
rule 3's per-unit merge-gate paragraph applied within a single leaf (26 Sept 2026, RETRO-2026-09-26g; malsburg
f.28/f.24/f.16 all passed cosine decisively and were held whole before this).

Files: TSVs with a header containing 'sign' and optionally 'confidence' (H/M/...). Several --pool files may be
given (ciphertext.txt plus leaves already admitted).

Usage: python3 tools/leaf_pool_gate.py --leaf recon_0028/ciphertext_draft.tsv --pool ciphertext.txt \
         [--pool pool/leaf_0023.tsv] [--seed 20260926] [--json out.json]
Exit 0 admitted, 1 held, 2 usage error.
"""
import argparse, csv, json, random, re, sys

DEFAULT_FORM = r"^(\d{1,3}|[A-Z#]|[A-Z][a-z]+)$"


def read_signs(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if not rows or "sign" not in rows[0]:
        sys.exit(f"leaf_pool_gate: {path}: no 'sign' column")
    return [(r["sign"].strip(), (r.get("confidence") or "H").strip()) for r in rows if r["sign"].strip()]


def overlap(tokens, vocab):
    return sum(1 for t in tokens if t in vocab) / len(tokens) if tokens else 0.0


def cosine(tokens, pool_counts):
    from collections import Counter
    c = Counter(tokens)
    num = sum(v * pool_counts.get(k, 0) for k, v in c.items())
    den = (sum(v * v for v in c.values()) ** 0.5) * (sum(v * v for v in pool_counts.values()) ** 0.5)
    return num / den if den else 0.0


def gate(leaf, pool, form=DEFAULT_FORM, max_m=0.15, max_offform=0.05, shuffles=200, seed=20260926):
    toks = [s for s, _ in leaf]
    n = len(toks)
    m_share = sum(1 for _, c in leaf if c.upper().startswith("M")) / n
    rx = re.compile(form)
    off = [t for t in toks if not rx.match(t)]
    off_share = len(off) / n
    from collections import Counter
    vocab = set(pool)
    pc = Counter(pool)
    real = cosine(toks, pc)
    ov = overlap(toks, vocab)
    # relabel control: map each distinct leaf value to a random value drawn from the pool's value space
    # widened to the same grammar's range (two-digit numbers 10-99 plus the pool's own non-numeric marks),
    # so a leaf in the same key keeps its overlap and a random relabel does not.
    space = sorted(set(f"{i:02d}" for i in range(10, 100)) | vocab)
    rng = random.Random(seed)
    distinct = sorted(set(toks))
    null = []
    for _ in range(shuffles):
        mp = dict(zip(distinct, rng.sample(space, len(distinct)) if len(distinct) <= len(space)
                      else [rng.choice(space) for _ in distinct]))
        null.append(cosine([mp[t] for t in toks], pc))
    null.sort()
    p95 = null[int(0.95 * (len(null) - 1))]
    res = {
        "n": n, "k": len(distinct), "m_share": round(m_share, 4), "offform_share": round(off_share, 4),
        "offform_examples": sorted(set(off))[:12], "vocab_overlap": round(ov, 4), "cosine_real": round(real, 4),
        "cosine_relabel_mean": round(sum(null) / len(null), 4), "cosine_relabel_p95": round(p95, 4),
        "gate_quality": m_share <= max_m, "gate_form": off_share <= max_offform, "gate_system": real > p95,
    }
    res["admitted"] = res["gate_quality"] and res["gate_form"] and res["gate_system"]
    # A leaf that clears form + system but fails quality (M-share) is not the same as a leaf that fails
    # system: the cosine test already established it is the same cipher, so its H-graded signs are safe to
    # pool for frequency/system purposes. Only its M-graded (uncertain) signs stay excluded from any code-value
    # attestation, the per-token version of rule 3's per-unit merge-gate paragraph (26 Sept 2026,
    # RETRO-2026-09-26g; three malsburg leaves f.28/f.24/f.16 all passed cosine decisively and were held whole).
    res["pooled_h_only"] = res["gate_form"] and res["gate_system"] and not res["gate_quality"]
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--leaf", required=True)
    ap.add_argument("--pool", action="append", required=True)
    ap.add_argument("--form", default=DEFAULT_FORM)
    ap.add_argument("--max-m", type=float, default=0.15)
    ap.add_argument("--max-offform", type=float, default=0.05)
    ap.add_argument("--shuffles", type=int, default=200)
    ap.add_argument("--seed", type=int, default=20260926)
    ap.add_argument("--json")
    a = ap.parse_args()
    leaf = read_signs(a.leaf)
    if not leaf:
        print("leaf_pool_gate: empty leaf", file=sys.stderr)
        return 2
    pool = [s for p in a.pool for s, _ in read_signs(p)]
    r = gate(leaf, pool, a.form, a.max_m, a.max_offform, a.shuffles, a.seed)
    line = (f"leaf {a.leaf}: N={r['n']} K={r['k']} M={r['m_share']:.3f} (<= {a.max_m}) "
            f"offform={r['offform_share']:.3f} (<= {a.max_offform}) vocab overlap {r['vocab_overlap']:.3f}; cosine real "
            f"{r['cosine_real']:.3f} vs relabel mean {r['cosine_relabel_mean']:.3f} p95 {r['cosine_relabel_p95']:.3f} -> "
            f"{'ADMITTED' if r['admitted'] else 'POOLED (H-only, M held per-token)' if r['pooled_h_only'] else 'HELD'}")
    print(line)
    if r["pooled_h_only"]:
        print("  H-graded signs join the pool for frequency/system stats; M-graded signs stay out of key.tsv "
              "value attestation until corroborated by an H occurrence or another leaf's admitted reading "
              "(CLAUDE.md rule 3, per-unit merge-gate paragraph).")
    if r["offform_examples"]:
        print("  offform examples:", " ".join(r["offform_examples"]))
    if a.json:
        with open(a.json, "w") as f:
            json.dump(r, f, indent=1)
    return 0 if r["admitted"] else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""GAPS206 pilot (4 Oct 2026): the 1864 sent ledgers' volunteer text read through Cipher No. 1 (PREREG-GAPS206.md).

Usage: pilot.py DATA_DIR [--write | --check]
  DATA_DIR holds vol18.json, vol19.json, vol15.json: one CONTENTdm dmQuery each (URLs and sha256 in manifest.tsv),
  every page of mssEC 18 / 19 / 15 with its Decoding the Civil War volunteer transcription (field "transc"). Not
  committed (the volunteers' work; re-fetch). Key: ciphers/eckert-1864/key.md through that folder's decode.py.
  --write rewrites results.tsv and pages.tsv; --check exits 1 if either is stale.

Statistics exactly as pre-registered (PREREG-GAPS206.md): S1 gate (R median S > N p95), S2 known-answer recall of the
20 image-reconciled eckert-1864 entries against the volunteer text of the same pointer, with a mismatched-page control
(seed 206), S3 target classification, S4 duplicate-copy 5-gram test against an 1862 null. Measurements only.
"""
import json, random, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "ciphers" / "eckert-1864"))
import decode as d1  # noqa: E402

SEED = 206
MIN_TOK = 30


def common_english(n=1000):
    c = Counter()
    for p in sorted((ROOT / "tools" / "data" / "en").glob("*.txt")):
        c.update(re.findall(r"[a-z]+", p.read_text(encoding="utf-8", errors="ignore").lower()))
    return {w for w, _ in c.most_common(n)}


def pages(data, vol):
    out = []
    for r in json.load(open(Path(data) / f"vol{vol}.json"))["records"]:
        t = r.get("transc")
        if not isinstance(t, str) or not t.strip():
            continue
        m = re.match(r"Page (\d+)", r["title"])
        out.append({"vol": vol, "ptr": int(r["pointer"]), "page": int(m.group(1)) if m else None, "text": t})
    return out


def keyed(text, key):
    """Return (n_alpha_tokens, list of (code stem lower, meaning, kind)) for keyed tokens (blind/line excluded)."""
    toks = re.findall(r"[A-Za-z]+", text)
    hits = []
    for t in toks:
        stem, flag, row = d1.lookup(t, key)
        if row is None or row[2] in ("blind", "line"):
            continue
        hits.append((stem.lower(), row[0], row[2]))
    return len(toks), hits


def s_rate(p, key, common):
    n, hits = keyed(p["text"], key)
    k = sum(1 for s, _, _ in hits if s not in common)
    return n, (100.0 * k / n if n else 0.0)


def pct(xs, q):
    xs = sorted(xs)
    if not xs:
        return float("nan")
    i = min(len(xs) - 1, max(0, int(round(q / 100.0 * (len(xs) - 1)))))
    return xs[i]


def grams(text):
    w = re.findall(r"[a-z]+", text.lower())
    return {" ".join(w[i:i + 5]) for i in range(len(w) - 4)}


def main(argv):
    data = argv[0]
    key = d1.load_key()
    common = common_english()
    T, R, N = pages(data, 18), pages(data, 19), pages(data, 15)
    R = [p for p in R if p["page"] is not None and p["page"] >= 21]
    rows, res = [], []
    S = {}
    for name, ps in (("T", T), ("R", R), ("N", N)):
        vals = []
        for p in ps:
            n, s = s_rate(p, key, common)
            if n < MIN_TOK:
                continue
            p["S"] = s
            vals.append(s)
            rows.append(f"{name}\t{p['vol']}\t{p['ptr']}\t{p['page'] if p['page'] is not None else ''}\t{n}\t{s:.2f}")
        S[name] = vals
    np95 = pct(S["N"], 95)
    for name in ("T", "R", "N"):
        res.append(f"S\t{name}\tpages={len(S[name])}\tmedian={pct(S[name], 50):.2f}\tp05={pct(S[name], 5):.2f}\tp95={pct(S[name], 95):.2f}")
    g1 = pct(S["R"], 50) > np95
    res.append(f"S1\tgate\tR_median={pct(S['R'], 50):.2f}\tN_p95={np95:.2f}\t{'PASS' if g1 else 'FAIL'}")
    if not g1:
        res.append("STOP\ttext route non-test at this key (S1 FAIL)")
        return finish(argv, rows, res)

    # S2 known answer
    byptr = {p["ptr"]: p for p in pages(data, 19)}
    blocks = d1.load_ciphertext()
    shared = total = 0
    entries = []
    for header, lines in blocks:
        ptr = int(header.split("|")[2])
        ref = Counter(m for _, m, _ in keyed(d1.entry_text(lines), key)[1])
        vol = Counter(m for _, m, _ in keyed(byptr[ptr]["text"], key)[1])
        sh = sum((ref & vol).values())
        shared += sh
        total += sum(ref.values())
        entries.append((header.split("|")[0].strip(), ptr, ref))
        res.append(f"S2e\t{header.split('|')[0].strip()}\tptr={ptr}\tshared={sh}\tref={sum(ref.values())}")
    recall = shared / total if total else 0.0
    rng = random.Random(SEED)
    others = [p for p in R]
    ctrl = []
    for _ in range(20):
        sh = tot = 0
        for _, ptr, ref in entries:
            q = rng.choice([p for p in others if p["ptr"] != ptr])
            vol = Counter(m for _, m, _ in keyed(q["text"], key)[1])
            sh += sum((ref & vol).values())
            tot += sum(ref.values())
        ctrl.append(sh / tot)
    c95 = pct(ctrl, 95)
    g2 = recall >= 0.85 and recall > c95
    res.append(f"S2\tknown_answer\trecall={recall:.3f} ({shared}/{total})\tctrl_mean={sum(ctrl)/len(ctrl):.3f}\tctrl_p95={c95:.3f}\t{'PASS' if g2 else 'FAIL'}")
    if not g2:
        res.append("STOP\ttext route non-test (S2 FAIL)")
        return finish(argv, rows, res)

    # S3 target
    above = sum(1 for s in S["T"] if s > np95)
    res.append(f"S3\ttarget\tT_median={pct(S['T'], 50):.2f}\tN_p95={np95:.2f}\t{'IN No.1 vocabulary' if pct(S['T'], 50) > np95 else 'NOT shown'}\tT_above={above}/{len(S['T'])}\tR_above={sum(1 for s in S['R'] if s > np95)}/{len(S['R'])}")
    Ts = sorted([p for p in T if "S" in p and p["page"] is not None], key=lambda p: p["page"])
    for i in range(0, len(Ts), 25):
        ch = Ts[i:i + 25]
        res.append(f"S3s\tT pages {ch[0]['page']}-{ch[-1]['page']}\tabove={sum(1 for p in ch if p['S'] > np95)}/{len(ch)}\tmedian={pct([p['S'] for p in ch], 50):.2f}")

    # S4 duplicate copy
    def gs(ps):
        return [(p, grams(p["text"])) for p in ps if "S" in p]
    gT, gR, gN = gs(T), gs(R), gs(N)
    df = Counter()
    for _, g in gT + gR + gN:
        df.update(g)
    boiler = {g for g, c in df.items() if c >= 3}
    def best(g):
        g = g - boiler
        return max((len(g & (h - boiler)) for _, h in gR), default=0)
    null = [best(g) for _, g in gN]
    thr = max(3, pct(null, 99) + 1)
    tb = [(p, best(g)) for p, g in gT]
    tw = sum(1 for _, b in tb if b >= thr)
    res.append(f"S4\tduplicate\tnull_p99={pct(null, 99)}\tthreshold={thr}\tT_pages_with_R_twin={tw}/{len(tb)}\tN_pages_over={sum(1 for b in null if b >= thr)}/{len(null)}")
    for p, b in tb:
        rows.append(f"T4\t18\t{p['ptr']}\t{p['page'] if p['page'] is not None else ''}\t\tbest5={b}")
    return finish(argv, rows, res)


def finish(argv, rows, res):
    out = {HERE / "results.tsv": "\n".join(res) + "\n", HERE / "pages.tsv": "set\tvol\tpointer\tpage\ttokens\tS_or_best5\n" + "\n".join(rows) + "\n"}
    if "--check" in argv:
        bad = [p.name for p, t in out.items() if not p.exists() or p.read_text() != t]
        if bad:
            sys.stderr.write("stale: " + ", ".join(bad) + "\n")
            return 1
        print("current")
        return 0
    if "--write" in argv:
        for p, t in out.items():
            p.write_text(t)
    print("\n".join(res))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""R7B-ECK62 (6 Oct 2026; rules pre-registered in PREREG-ECK62-WRONGTEL.md, pushed before any number): is the dated OR
match of each of D2-ECK62R's 18 neither-book entries the wrong telegram?

Usage: ec18_wrongtel.py DATA_DIR OR_DIR [--write | --check]
  DATA_DIR/vol18.json and OR_DIR/<vol>.txt exactly as for ec18_align.py (not committed; URLs and sha256 in
  ../pilot1864/manifest.tsv and or_volumes.tsv). --write rewrites wrongtel_entries.tsv and wrongtel_summary.tsv;
  --check exits 1 if either is stale.

Statistic: clear-word coverage = LCS(entry clear words, OR window words) / entry clear words. Clear words are the
'plain' (unkeyed) tokens of ec18_align.tokens() under the entry's aligned book (the reading with brackets removed),
lower-cased, >= 3 letters, in ec18.vocab(). Window = OR words [anchor - 2n, anchor + 2n), n = entry word count.
Positive control: the 14 align_free entries with scored >= 5 and agree_rate >= 0.75. Negative control: the 14 and the 18
with the window centred on the control position ec18_align.py uses (nearest other heading of the same week).
"""
import re, sys, json, collections
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ec18  # noqa: E402
import ec18_align as al  # noqa: E402


def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for k, y in enumerate(b):
            cur.append(prev[k] + 1 if x == y else max(prev[k + 1], cur[k]))
        prev = cur
    return prev[-1]


def pct(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, max(0, int(round(q * (len(xs) - 1)))))]


def main(argv):
    data, ordir = argv[0], argv[1]
    vols, _ = ec18.or_index(ordir, set())
    es = {e["id"]: e for e in ec18.entries(data)}
    keys = {"1": al.d1.load_key(ec18.ROOT / "ciphers/eckert-1864/key.md"),
            "2": al.d1.load_key(ec18.ROOT / "ciphers/eckert-1864/key-no2.md")}
    voc = ec18.vocab()
    rd = lambda f: [l.split("\t") for l in ec18.src(f).read_text().splitlines()[1:]]
    rows = {r[0]: (r[1], r[4], r[5], int(r[6])) for r in rd("align_free_rows.tsv")}
    acc = set(ec18.flips())
    tgt = [r[0] for r in rd("align_flip_entries.tsv") if r[0] not in acc]
    pos = [r[0] for r in rd("align_free_entries.tsv") if int(r[5]) >= 5 and float(r[11]) >= 0.75]
    if ec18.SPLIT2:  # PREREG-ECK62-S2 (R10-ECK62T): 17 flip-selected entries minus accepted flips; 16 positives
        assert len(rd("align_flip_entries.tsv")) == 17 and len(pos) == 16, (len(tgt), len(pos))
    else:
        assert len(tgt) == 18 and len(pos) == 14, (len(tgt), len(pos))

    def measure(i):
        bk, v, pg, j = rows[i]
        e = es[i]
        toks = al.tokens(re.sub(r"\s+", " ", " ".join(e["body"])).strip(), keys[bk])
        n = len(al.seq(toks)[0])
        clear = [w for (w, m, g, k) in toks if k == "plain" and len(w) >= 3 and w.isalpha() and w in voc]
        vw = vols[v]
        cov = lcs(clear, vw[max(0, j - 2 * n):j + 2 * n]) / max(1, len(clear))
        cands = [(abs(p - j), v, p) for p in al.heading_positions(vw, e["date"]) if abs(p - j) > 700]
        if not cands:
            for v2 in sorted(vols):
                if v2 != v:
                    cands += [(10 ** 9, v2, p) for p in al.heading_positions(vols[v2], e["date"])]
        cv, cp = sorted(cands)[0][1:] if cands else (None, None)
        ccov = lcs(clear, vols[cv][max(0, cp - 2 * n):cp + 2 * n]) / max(1, len(clear)) if cv else None
        body = e["body"][1:]
        second = sum(1 for l in body if ec18.DATE.search(l))
        return {"id": i, "book": bk, "date": "%d-%02d-%02d" % e["date"], "vol": v, "page": pg, "n": n,
                "clear": len(clear), "cov": cov, "ctl": ccov, "second_date": second}
    P = [measure(i) for i in pos]
    T = [measure(i) for i in tgt]
    pv = [m["cov"] for m in P if m["clear"] >= 6]
    nv = [m["ctl"] for m in P + T if m["ctl"] is not None and m["clear"] >= 6]
    p10, n90 = pct(pv, 0.10), pct(nv, 0.90)
    pmed, nmed = pct(pv, 0.5), pct(nv, 0.5)
    gate = pmed >= 0.50 and nmed <= 0.25 and p10 > n90
    pages = collections.Counter((m["vol"], m["page"]) for m in T)
    out = ["id\trole\tbook\tdate\tor_vol\tor_page_ocr\tentry_words\tclear_words\tcoverage\tctl_coverage\tsecond_date_lines\t"
           "shares_or_page\tclass"]
    cls = collections.Counter()
    for role, ms in (("target", T), ("positive", P)):
        for m in ms:
            c = "-"
            if role == "target":
                c = ("too-short" if m["clear"] < 6 else "untested" if not gate else "right-telegram" if m["cov"] >= p10
                     else "wrong-telegram" if m["cov"] <= n90 else "undecided")
                cls[c] += 1
                cls[(m["date"][:7], c)] += 1
            out.append(f"{m['id']}\t{role}\t{m['book']}\t{m['date']}\t{m['vol']}\t{m['page']}\t{m['n']}\t{m['clear']}\t"
                       f"{m['cov']:.3f}\t{'-' if m['ctl'] is None else format(m['ctl'], '.3f')}\t{m['second_date']}\t"
                       f"{pages[(m['vol'], m['page'])] if role == 'target' else '-'}\t{c}")
    months = sorted({k[0] for k in cls if isinstance(k, tuple)})
    summ = ["statistic\tvalue", f"targets\t{len(T)}", f"positive_control\t{len(P)} (classified on clear >= 6: {len(pv)})",
            f"positive_median_p10\t{pmed:.3f} {p10:.3f}", f"negative_control\t{len(nv)} windows",
            f"negative_median_p90\t{nmed:.3f} {n90:.3f}",
            f"gate\t{'PASS' if gate else 'FAIL'} (pos median >= 0.50, neg median <= 0.25, pos p10 > neg p90)",
            "target_classes\t" + ", ".join(f"{k} {v}" for k, v in sorted((k, v) for k, v in cls.items() if isinstance(k, str))),
            "target_median_coverage\t%.3f" % pct([m["cov"] for m in T], 0.5),
            "targets_with_second_date_line\t%d" % sum(1 for m in T if m["second_date"]),
            "targets_sharing_an_or_page\t%d" % sum(1 for m in T if pages[(m["vol"], m["page"])] > 1),
            "by_month\t" + "; ".join(m + ": " + ", ".join(f"{c} {v}" for (mm, c), v in sorted(
                (k, v) for k, v in cls.items() if isinstance(k, tuple) and k[0] == m)) for m in months)]
    outs = {"wrongtel_entries.tsv": "\n".join(out) + "\n", "wrongtel_summary.tsv": "\n".join(summ) + "\n"}
    if "--write" in argv:
        for k, val in outs.items():
            (ec18.OUT / k).write_text(val)
    elif "--check" in argv:
        stale = [k for k, val in outs.items() if not (ec18.OUT / k).exists() or (ec18.OUT / k).read_text() != val]
        if stale:
            sys.stderr.write("stale: " + ", ".join(stale) + "\n")
            return 1
        print("current")
    print(outs["wrongtel_summary.tsv"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

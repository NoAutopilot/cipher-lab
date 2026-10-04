#!/usr/bin/env python3
"""NEAR3-THUR one-vote M boundary test (pre-registered in PREREG.md beside this file, 4 Oct 2026).

    python3 boundary_test.py            # writes results.tsv and prints the summary
    python3 boundary_test.py --check    # exits 1 if the committed results.tsv is stale
    python3 boundary_test.py --skip     # v2: results_v2.tsv (skip up to 2 unreadable tokens per side)
    python3 boundary_test.py --skip --tx  # v3 (A3V2-THURBT, 4 Oct 2026): results_tx.tsv; the cipher lines of the
                                        # pages listed in tx/pages.tsv are read from the page-image transcription
                                        # tx/<page>.tsv (label TAB text, one printed line each) instead of the djvu
                                        # OCR; every other line, the plain side, the statistic and the gate unchanged
    python3 boundary_test.py --skip --tx --txplain  # v3 addendum (N8-THUR, 4 Oct 2026): results_tx_full.tsv, the gated
                                        # run -- all five cipher pages (tx/pages_full.tsv) and both printed
                                        # decipherments (tx/plain_pages.tsv) read from the page image
    python3 boundary_test.py --skip --tx --txall    # descriptive: five cipher pages, OCR plain -> results_tx_cipher5.tsv

For each occurrence of a code in the P5+P6 / P7 cipher paragraphs: decode the keyed context either side
(with the code under test removed from the key), locate both contexts in Birch's printed decipherment by
semi-global edit distance, and compare the printed text between them (the gap) with the claimed meaning.
Targets: 67, 153, 84, 275. Controls: K (known-answer C/H codes, own meaning) and W (same occurrences, wrong
meaning). Deterministic (random.Random(0) and (1)); disk only.
"""
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import align_stamford as A  # noqa: E402

TARGETS = [67, 153, 84, 275]
FURNITURE = re.compile(r"STATE\s+PAPERS|THURLOE|J\s+O\s+N\s+H")
MIN_CTX, MAX_COST, WINDOW, UNIQ = 10, 0.25, 60, 5
SKIP = 2 if "--skip" in sys.argv else 0  # v2 (PREREG.md): skip up to 2 unreadable/unkeyed tokens per side
TX = "--tx" in sys.argv  # v3: page-image transcription for the pages in tx/pages.tsv (PREREG.md v3 section)
# v3 addendum (N8-THUR, 4 Oct 2026, PREREG.md): --txplain also reads the printed decipherments from the page-image
# transcription (tx/plain_pages.tsv) and all five cipher pages (tx/pages_full.tsv) -> results_tx_full.tsv (the gated run);
# --txall alone = all five cipher pages, OCR plain side -> results_tx_cipher5.tsv (descriptive)
TXPLAIN = "--txplain" in sys.argv
TXALL = TXPLAIN or "--txall" in sys.argv
NEW_PAGES = ("p274_", "p277_", "p279_")  # new-only split (descriptive)


def load_tx():
    """tx/pages.tsv: page, djvu_from, djvu_to, file -> {djvu_from: (djvu_to, [(label, text), ...])}.
    The transcribed lines replace djvu lines djvu_from..djvu_to (inclusive) in the cipher stream."""
    out = {}
    if not TX:
        return out
    for ln in (HERE / ("tx/pages_full.tsv" if TXALL else "tx/pages.tsv")).read_text().splitlines()[1:]:
        if not ln.strip() or ln.startswith("#"):
            continue
        page, a, b, f = ln.split("\t")[:4]
        rows = []
        for t in (HERE / "tx" / f).read_text().splitlines():
            if not t.strip() or t.startswith("#"):
                continue
            label, text = t.split("\t", 1)
            rows.append((label, text))
        out[int(a)] = (int(b), rows)
    return out


def plain_lines(lines, name):
    """Raw lines of a letter's plain span; with --txplain the transcribed decipherment replaces the djvu span."""
    a, b = A.SPANS[name]["plain"]
    if TXPLAIN:
        for ln in (HERE / "tx/plain_pages.tsv").read_text().splitlines()[1:]:
            let, fa, fb, f = ln.split("\t")[:4]
            if let == name:
                assert (int(fa), int(fb)) == (a, b), (name, fa, fb)
                return [t.split("\t", 1)[1] for t in (HERE / "tx" / f).read_text().splitlines()
                        if t.strip() and not t.startswith("#")]
    return lines[a - 1:b]


def norm(s):
    s = s.lower().translate(str.maketrans("fvjy", "suii"))
    return re.sub(r"[^a-z]", "", s)


def load_key():
    key = {}
    for ln in (HERE.parent / "key_stamford.tsv").read_text().splitlines()[1:]:
        v, m, votes, _t, _s, g, allr = ln.split("\t")[:7]
        if "; boundary " in allr:
            # an entry this test itself changed (decode_stamford BOUNDARY_C / BOUNDARY_M, N8-THUR): score against its
            # pre-test state (first alignment reading, grade M) so every committed results file stays reproducible
            m, g = allr.split(";")[0].split()[0].rsplit(":", 1)[0], "M"
        key[v] = (m.replace("u/v", "u"), int(votes), g)
    return key


def units_by_line(lines, a, b, tx=None):
    """(djvu_line, unit, raw_line) in reading order; junk lines are kept so the furniture check can see them.
    tx (v3): {djvu_from: (djvu_to, [(label, text)])} -- those djvu lines are replaced by the transcribed lines,
    whose "line number" is the transcription label (p275_L02 ...); the same junk filters apply to both."""
    out = []
    tx = tx or {}
    no = a
    while no <= b:
        if no in tx:
            to, rows = tx[no]
            src = [(lab, text) for lab, text in rows]
            no = to + 1
        else:
            src = [(no, lines[no - 1])]
            no += 1
        for label, raw in src:
            if A.JUNK_LINE.search(raw):
                continue
            ln = raw
            for rx in A.JUNK_SUB:
                ln = rx.sub(" ", ln)
            for u in A.tokenize([ln]):
                out.append((label, u, raw))
    return out


def unit_text(u, key, skip):
    if u[0] == "W":
        return u[1]
    if u[0] == "T":
        return "thelordprotector"
    if u[0] == "N" and str(u[1]) != str(skip) and str(u[1]) in key:
        return key[str(u[1])][0]
    return None


def context(units, i, step, key, skip):
    parts, j, skipped = [], i + step, 0
    while 0 <= j < len(units) and len(norm("".join(parts))) < MIN_CTX:
        t = unit_text(units[j][1], key, skip)
        if t is None:
            if skipped >= SKIP or units[j][1][0] == "W":
                break
            skipped += 1
            j += step
            continue
        parts.append(t)
        j += step
    if step < 0:
        parts.reverse()
    s = norm("".join(parts))
    return s if len(s) >= MIN_CTX else None


def semiglobal(p, t):
    """Free start and end in t. -> list of (cost, start, end) for every end position."""
    m = len(p)
    prev = [(0, j) for j in range(len(t) + 1)]  # (cost, start)
    for i in range(1, m + 1):
        cur = [(i, 0)] * (len(t) + 1)
        cur[0] = (i, 0)
        for j in range(1, len(t) + 1):
            d = prev[j - 1][0] + (p[i - 1] != t[j - 1])
            best = (d, prev[j - 1][1])
            if prev[j][0] + 1 < best[0]:
                best = (prev[j][0] + 1, prev[j][1])
            if cur[j - 1][0] + 1 < best[0]:
                best = (cur[j - 1][0] + 1, cur[j - 1][1])
            cur[j] = best
        prev = cur
    return [(c, s, e) for e, (c, s) in enumerate(prev)]


def edit(a, b):
    prev = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        cur = [i] + [0] * len(b)
        for j in range(1, len(b) + 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] != b[j - 1]))
        prev = cur
    return prev[-1]


def test(units, i, meaning, key, skip, plain):
    no, u, raw = units[i]
    if FURNITURE.search(raw):
        return "REFUTE-furniture", "", "", "", raw.strip()[:60]
    left, right = context(units, i, -1, key, skip), context(units, i, +1, key, skip)
    if not left or not right:
        return "INCONCLUSIVE", left or "", right or "", "", "context too short"
    hits = semiglobal(left, plain)
    best = min(c for c, _s, _e in hits)
    if best > MAX_COST * len(left):
        return "INCONCLUSIVE", left, right, "", "left not located"
    ends = [e for c, _s, e in hits if c == best]
    if max(ends) - min(ends) > UNIQ:
        return "INCONCLUSIVE", left, right, "", "left not unique"
    e = min(ends)
    win = plain[e:e + WINDOW + len(right) + 4]
    rh = [(c, s, en) for c, s, en in semiglobal(right, win) if s <= WINDOW]
    rbest = min(rh)
    if rbest[0] > MAX_COST * len(right):
        return "INCONCLUSIVE", left, right, "", "right not located"
    gap = win[:rbest[1]]
    m = norm(meaning)
    d = edit(gap, m)
    if d <= int(0.2 * len(m)):
        v = "CONFIRM"
    elif d > 0.5 * max(len(m), len(gap)):
        v = "REFUTE-gap"
    else:
        v = "INCONCLUSIVE"
    return v, left, right, gap, f"edit {d}"


def run():
    lines = A.djvu_lines()
    key = load_key()
    tx = load_tx()
    letters = {}
    for name in ("P5_P6", "P7"):
        sp = A.SPANS[name]
        pl = plain_lines(lines, name)
        plain = norm(" ".join(A.plain_words(A.clean_lines(pl, 1, len(pl)))))
        letters[name] = (units_by_line(lines, *sp["cipher"], tx=tx), plain)
    occ = [(name, i, u[1]) for name, (us, _p) in letters.items() for i, (_n, u, _r) in enumerate(us) if u[0] == "N"]
    rows = []

    def add(group, name, i, code, meaning):
        us, plain = letters[name]
        v, left, right, gap, note = test(us, i, meaning, key, code, plain)
        rows.append([group, name, str(us[i][0]), str(code), norm(meaning), v, left, right, gap, note])

    for name, i, v in occ:
        if v in TARGETS:
            add("target", name, i, v, key[str(v)][0])
    words = [(n, i, v) for n, i, v in occ if v >= A.CODE_MIN and str(v) in key and key[str(v)][2] == "C"]
    lets = [(n, i, v) for n, i, v in occ if v < A.CODE_MIN and str(v) in key and key[str(v)][2] in "CH"
            and key[str(v)][1] >= 10]
    K = words + random.Random(0).sample(lets, 60)
    for n, i, v in K:
        add("K", n, i, v, key[str(v)][0])
    rng = random.Random(1)
    wpool = sorted({norm(key[str(v)][0]) for _n, _i, v in words})
    lpool = sorted({norm(key[str(v)][0]) for _n, _i, v in lets})
    for n, i, v in K:
        own = norm(key[str(v)][0])
        pool = [x for x in (wpool if v >= A.CODE_MIN else lpool) if x != own]
        add("W", n, i, v, rng.choice(pool))
    return rows


def summary(rows):
    out = []
    for g in ("K", "W"):
        rs = [r for r in rows if r[0] == g]
        ver = [r for r in rs if r[5] != "INCONCLUSIVE"]
        conf = sum(r[5] == "CONFIRM" for r in ver)
        out.append(f"{g}: {len(rs)} occurrences, {len(ver)} reach a verdict ({100*len(ver)/len(rs):.1f}%), "
                   f"CONFIRM {conf}/{len(ver)} = {100*conf/max(1,len(ver)):.1f}%")
    k = [r for r in rows if r[0] == "K"]
    kv = [r for r in k if r[5] != "INCONCLUSIVE"]
    wv = [r for r in rows if r[0] == "W" and r[5] != "INCONCLUSIVE"]
    gate = (len(kv) >= 0.6 * len(k) and sum(r[5] == "CONFIRM" for r in kv) >= 0.8 * len(kv)
            and sum(r[5] == "CONFIRM" for r in wv) <= 0.1 * len(wv))
    out.append("gate: " + ("PASS" if gate else "FAIL (non-test, no change)"))
    if TX:  # descriptive split (not the gate): occurrences on transcribed pages vs on OCR lines
        splits = [("transcribed pages", lambda r: not r[2].isdigit()), ("OCR lines", lambda r: r[2].isdigit())]
        if TXALL:
            splits = [("new pages 274/277/279", lambda r: r[2].startswith(NEW_PAGES)),
                      ("old pages 275/278", lambda r: r[2].startswith(("p275_", "p278_"))),
                      ("OCR lines", lambda r: r[2].isdigit())]
        for lab, sel in splits:
            for g in ("K", "W"):
                rs = [r for r in rows if r[0] == g and sel(r)]
                ver = [r for r in rs if r[5] != "INCONCLUSIVE"]
                conf = sum(r[5] == "CONFIRM" for r in ver)
                out.append(f"  {g} on {lab}: {len(rs)} occurrences, {len(ver)} verdicts "
                           f"({100*len(ver)/max(1,len(rs)):.1f}%), CONFIRM {conf}/{len(ver)} = {100*conf/max(1,len(ver)):.1f}%")
    for r in rows:
        if r[0] == "target":
            out.append(f"target {r[3]} ({r[1]} djvu {r[2]}) claimed '{r[4]}': {r[5]}; left '{r[6]}' gap '{r[8]}' "
                       f"right '{r[7]}' ({r[9]})")
    return "\n".join(out)


def main():
    rows = run()
    tsv = "\n".join(["group\tletter\tdjvu_line\tcode\tmeaning\tverdict\tleft\tright\tgap\tnote"]
                    + ["\t".join(r) for r in rows]) + "\n"
    f = HERE / ("results_tx_full.tsv" if TX and TXPLAIN else "results_tx_cipher5.tsv" if TX and TXALL
                else "results_tx.tsv" if TX else "results_v2.tsv" if SKIP else "results.tsv")
    if "--check" in sys.argv:
        if not f.exists() or f.read_text() != tsv:
            print("stale:", f.name)
            sys.exit(1)
        print("ok:", f.name, "matches")
    else:
        f.write_text(tsv)
    print(summary(rows))


if __name__ == "__main__":
    main()

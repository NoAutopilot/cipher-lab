#!/usr/bin/env python3
"""MONT-4715C (27 Sept 2026): what MONT-4715B's calibration number can and cannot say.

    python3 scripts/mont4715c.py u1        # group-LCS of our v2 signs vs Tomokiyo's dump groups, + order-shuffle control
    python3 scripts/mont4715c.py u2prep    # write witness/tomokiyo_signs_ceiling.tsv (+ v2 L02-L17-only signs file)
    python3 scripts/mont4715c.py classes   # per-class breakdown of v2 signs over L02-L17 and of the dump
    python3 scripts/mont4715c.py u3cover DECODE_TXT   # French word-cover of an H+M decode vs 20 letter-shuffled keys

Target-local, script-only, no network. Inputs are the files already on disk (see NOTES.md "MONT-4715C").
Group notation on both sides: a bare digit string is a letter homophone, a leading apostrophe a dotted
word-code, glyphs (the two symbol cells), '~NN', 'NN*', '^NN' kept literally as printed/drawn. Our
undecidable/illegible positions become a token that can never match.
"""
import csv
import gzip
import random
import re
import statistics
import sys
import unicodedata

KEY = "keys/key_vieuville_nevers.tsv"
V2 = "witness/witness_signs_v2.tsv"
DUMP = "witness/aligned_dump_codes.txt"
SPAN = (2, 17)  # calibration span per MONT-4715 (cumulative sign count against the dump's 959 tokens)


def load_key():
    rows, header = [], None
    for ln in open(KEY, encoding="utf-8"):
        ln = ln.rstrip("\n")
        if not ln.strip() or ln.startswith("#"):
            continue
        cols = ln.split("\t")
        if header is None:
            header = cols
            continue
        rows.append(dict(zip(header, cols)))
    return rows


def v2_groups(lo=SPAN[0], hi=SPAN[1]):
    """Our v2 transcription as (line, group, class) over lines lo..hi."""
    key = load_key()
    out = []
    for r in csv.DictReader(open(V2, encoding="utf-8"), delimiter="\t"):
        ln = r["line"]
        if not (ln.startswith("L") and ln[1:].isdigit() and lo <= int(ln[1:]) <= hi):
            continue
        kr, note = r["key_row"].strip(), r["shape_note"].strip()
        if note.startswith("dotted:"):
            out.append((ln, "'" + note.split(":", 1)[1].lstrip("'"), "dotted"))
        elif kr.isdigit():
            out.append((ln, key[int(kr) - 1]["sign"], "key-row letter"))
        elif note.startswith("unmatched:"):
            out.append((ln, note.split(":")[1], "unmatched definite"))
        elif note.startswith("undecidable"):
            out.append((ln, None, "undecidable"))
        elif kr == "#PLAIN":
            out.append((ln, None, "plain"))
        else:
            out.append((ln, None, "illegible"))
    return out


def dump_groups():
    return open(DUMP, encoding="utf-8").read().split()


def dump_class(g):
    if g.startswith("'"):
        return "dotted"
    if g.isdigit():
        return "bare"
    return "symbol/other"


def lcs_pairs(a, b):
    """LCS between token lists a (ours, None never matches) and b (Tomokiyo's); returns matched indices of b."""
    n, m = len(a), len(b)
    prev = [0] * (m + 1)
    rows = []
    for i in range(1, n + 1):
        ai = a[i - 1]
        cur = [0] * (m + 1)
        for j in range(1, m + 1):
            if ai is not None and ai == b[j - 1]:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = cur[j - 1] if cur[j - 1] >= prev[j] else prev[j]
        rows.append(cur)
        prev = cur
    # traceback
    matched = set()
    i, j = n, m
    get = lambda ii, jj: 0 if ii == 0 else rows[ii - 1][jj]
    while i > 0 and j > 0:
        if a[i - 1] is not None and a[i - 1] == b[j - 1] and get(i, j) == get(i - 1, j - 1) + 1:
            matched.add(j - 1)
            i -= 1
            j -= 1
        elif get(i - 1, j) >= get(i, j - 1):
            i -= 1
        else:
            j -= 1
    return matched


def summarize(matched, dump):
    tot = {"all": 0, "dotted": 0, "bare": 0, "symbol/other": 0}
    hit = dict.fromkeys(tot, 0)
    for j, g in enumerate(dump):
        c = dump_class(g)
        tot["all"] += 1
        tot[c] += 1
        if j in matched:
            hit["all"] += 1
            hit[c] += 1
    return hit, tot


def u1():
    dump = dump_groups()
    variants = {
        "as drawn (dot counts)": (lambda g: g, lambda g: g),
        "dot-blind (apostrophe stripped both sides)": (
            lambda g: None if g is None else g.lstrip("'"), lambda g: g.lstrip("'")),
    }
    for span in ((2, 17), (2, 36)):
        ours = v2_groups(*span)
        print(f"== span L{span[0]:02d}-L{span[1]:02d}: our v2 groups {len(ours)}, Tomokiyo dump groups {len(dump)}")
        for vname, (fo, fd) in variants.items():
            a = [fo(g) for _, g, _ in ours]
            b = [fd(g) for g in dump]
            hit, tot = summarize(lcs_pairs(a, b), dump)
            rng = random.Random(1)
            sh = {k: [] for k in tot}
            for _ in range(20):
                by_line = {}
                for (ln, g, _), x in zip(ours, a):
                    by_line.setdefault(ln, []).append(x)
                shuffled = []
                for ln in sorted(by_line):
                    xs = by_line[ln][:]
                    rng.shuffle(xs)
                    shuffled += xs
                h2, _ = summarize(lcs_pairs(shuffled, b), dump)
                for k in tot:
                    sh[k].append(h2[k] / tot[k])
            print(f"  [{vname}]")
            for k in ("all", "bare", "dotted", "symbol/other"):
                m, s = statistics.mean(sh[k]), statistics.stdev(sh[k])
                z = (hit[k] / tot[k] - m) / s if s else float("nan")
                print(f"    {k:13s} real {hit[k]}/{tot[k]} = {hit[k]/tot[k]:.4f}   order-shuffled (20) mean {m:.4f} sd {s:.4f}   z {z:.1f}")


def u2prep():
    key = load_key()
    s2r = {r["sign"]: i for i, r in enumerate(key, start=1)}
    dump = dump_groups()
    n_key = n_q = 0
    with open("witness/tomokiyo_signs_ceiling.tsv", "w", encoding="utf-8") as f:
        f.write("line\tpos\tkey_row\tshape_note\tconfidence\n")
        for i, g in enumerate(dump, start=1):
            if g in s2r:
                f.write(f"T\t{i}\t{s2r[g]}\t\tH\n")
                n_key += 1
            else:
                f.write(f"T\t{i}\t?\t{dump_class(g)}:{g}\tH\n")
                n_q += 1
    print(f"witness/tomokiyo_signs_ceiling.tsv: {len(dump)} groups, {n_key} resolved to a key row, {n_q} '?'")
    # length-matched v2 file: L02-L17 only
    rows = list(csv.DictReader(open(V2, encoding="utf-8"), delimiter="\t"))
    keep = [r for r in rows if r["line"][1:].isdigit() and SPAN[0] <= int(r["line"][1:]) <= SPAN[1]]
    with open("witness/witness_signs_v2_L02-L17.tsv", "w", encoding="utf-8") as f:
        f.write("line\tpos\tkey_row\tshape_note\tconfidence\n")
        for r in keep:
            f.write("\t".join(r[k] for k in ("line", "pos", "key_row", "shape_note", "confidence")) + "\n")
    print(f"witness/witness_signs_v2_L02-L17.tsv: {len(keep)} rows")


def classes():
    ours = v2_groups()
    c = {}
    for _, _, k in ours:
        c[k] = c.get(k, 0) + 1
    print(f"v2 L02-L17 ({len(ours)} signs):", ", ".join(f"{k} {v} ({v/len(ours):.1%})" for k, v in sorted(c.items(), key=lambda x: -x[1])))
    key = {r["sign"] for r in load_key()}
    dump = dump_groups()
    d = {"bare, in key": 0, "bare, not in key": 0, "dotted": 0, "symbol/other": 0}
    for g in dump:
        cl = dump_class(g)
        if cl == "bare":
            d["bare, in key" if g in key else "bare, not in key"] += 1
        elif g in key:
            d["bare, in key"] += 1  # the two glyph cells
        else:
            d[cl] += 1
    print(f"Tomokiyo dump ({len(dump)} groups):", ", ".join(f"{k} {v} ({v/len(dump):.1%})" for k, v in d.items()))


# ---- U3: French word cover ----
def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return s.replace("j", "i").replace("v", "u")


def wordlist(minfreq=3, minlen=3, maxlen=14):
    import glob
    cnt = {}
    for p in glob.glob("../../tools/data/fr16/*.txt.gz"):
        for w in re.findall(r"[a-zà-ÿ]+", gzip.open(p, "rt", encoding="utf-8", errors="ignore").read().lower()):
            w = norm(w)
            if minlen <= len(w) <= maxlen:
                cnt[w] = cnt.get(w, 0) + 1
    return {w for w, n in cnt.items() if n >= minfreq}


def cover(segments, words, maxlen=14):
    covered = total = 0
    for seg in segments:
        n = len(seg)
        total += n
        best = [0] * (n + 1)
        for i in range(1, n + 1):
            best[i] = best[i - 1]
            for L in range(3, min(maxlen, i) + 1):
                if seg[i - L:i] in words:
                    best[i] = max(best[i], best[i - L] + L)
        covered += best[n]
    return covered, total


def segments_from_signs(signs_path, lo, hi, valmap):
    """H letters from valmap(key_row), M words from decode_rest.py's own gloss tables; I breaks a run."""
    sys.path.insert(0, "scripts")
    from decode_rest import OWN_GLOSS, SIBLING_GLOSS
    segs, cur, last = [], "", None
    for r in csv.DictReader(open(signs_path, encoding="utf-8"), delimiter="\t"):
        ln = r["line"]
        if not (ln == "T" or (ln[1:].isdigit() and lo <= int(ln[1:]) <= hi)):
            continue  # "T" = the single pseudo-line of witness/tomokiyo_signs_ceiling.tsv
        kr, note = r["key_row"].strip(), r["shape_note"].strip()
        tok = None
        if note.startswith("dotted:"):
            d = note.split(":", 1)[1].lstrip("'")
            tok = OWN_GLOSS.get(d) or SIBLING_GLOSS.get(d)
            tok = tok.replace(" ", "") if tok else None
        elif kr.isdigit():
            tok = valmap[int(kr)]
        if tok is None:
            if cur:
                segs.append(cur)
            cur = ""
        else:
            cur += norm(tok)
    if cur:
        segs.append(cur)
    return segs


def u3cover(signs_path=V2, lo=18, hi=36):
    key = load_key()
    words = wordlist()
    real = {i: r["value"] for i, r in enumerate(key, start=1)}
    c, t = cover(segments_from_signs(signs_path, lo, hi, real), words)
    letter_rows = [i for i, r in enumerate(key, start=1) if r["kind"] == "letter"]
    rng = random.Random(1)
    sh = []
    for _ in range(20):
        vals = [real[i] for i in letter_rows]
        rng.shuffle(vals)
        vm = dict(real)
        vm.update(zip(letter_rows, vals))
        c2, t2 = cover(segments_from_signs(signs_path, lo, hi, vm), words)
        sh.append(c2 / t2)
    m, s = statistics.mean(sh), statistics.stdev(sh)
    print(f"wordlist: tools/data/fr16 (3 files), words len 3-14 freq>=3: {len(words)}")
    print(f"L{lo:02d}-L{hi:02d} H+M letters {t}; word-cover real {c}/{t} = {c/t:.4f}; "
          f"20 letter-shuffled keys mean {m:.4f} sd {s:.4f} min {min(sh):.4f} max {max(sh):.4f}; z {(c/t-m)/s:.2f}")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "u1":
        u1()
    elif cmd == "u2prep":
        u2prep()
    elif cmd == "classes":
        classes()
    elif cmd == "u3cover":
        u3cover(*(sys.argv[2:3] or [V2]), *[int(x) for x in sys.argv[3:5]])

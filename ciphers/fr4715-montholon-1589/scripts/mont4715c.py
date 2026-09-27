#!/usr/bin/env python3
"""MONT-4715C (27 Sept 2026): what MONT-4715B's calibration number can and cannot say.

    python3 scripts/mont4715c.py u1        # group-LCS of our v2 signs vs Tomokiyo's dump groups, + order-shuffle control
    python3 scripts/mont4715c.py u2prep    # write witness/tomokiyo_signs_ceiling.tsv (+ v2 L02-L17-only signs file)
    python3 scripts/mont4715c.py classes   # per-class breakdown of v2 signs over L02-L17 and of the dump
    python3 scripts/mont4715c.py u3cover DECODE_TXT   # French word-cover of an H+M decode vs 20 letter-shuffled keys
    python3 scripts/mont4715c.py anatomy   # MONT-CAL U1: classify every missed dump group (confusion/segmentation/dot/...)
    python3 scripts/mont4715c.py spans     # MONT-CAL: the dump's groups assigned to our folio lines via the v2 anchors
    python3 scripts/mont4715c.py segparse  # MONT-CAL: can the key's code inventory segment a boundary-free digit stream? [--ours: our v2 digits]
    python3 scripts/mont4715c.py score TSV L03,L08,L12,L16   # MONT-CAL U3: group-LCS of a recipe TSV vs the dump

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



# ---- MONT-CAL (27 Sept 2026): miss anatomy, per-line dump spans, recipe scoring ----

def lcs_align(a, b):
    """Same DP as lcs_pairs, returning the matched (i, j) pairs in order."""
    n, m = len(a), len(b)
    rows = [[0] * (m + 1)]
    for i in range(1, n + 1):
        ai, prev, cur = a[i - 1], rows[-1], [0] * (m + 1)
        for j in range(1, m + 1):
            if ai is not None and ai == b[j - 1]:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = cur[j - 1] if cur[j - 1] >= prev[j] else prev[j]
        rows.append(cur)
    pairs, i, j = [], n, m
    while i > 0 and j > 0:
        if a[i - 1] is not None and a[i - 1] == b[j - 1] and rows[i][j] == rows[i - 1][j - 1] + 1:
            pairs.append((i - 1, j - 1))
            i -= 1
            j -= 1
        elif rows[i - 1][j] >= rows[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return pairs[::-1]


def classify_gap(ours, dump, conf):
    """Walk one unmatched gap (our tokens vs the dump's) and label each dump group:
    seg (split/merge run), dot (digits right, dot missed), conf (same length, other digits),
    und (our token undecidable/illegible), other (length differs, no run explains it), unpaired (no counterpart)."""
    strip = lambda g: None if g is None else g.lstrip("'")
    lab, p, q = [], 0, 0
    while q < len(dump):
        if p >= len(ours):
            lab += ["unpaired"] * (len(dump) - q)
            break
        a, b = strip(ours[p]), strip(dump[q])
        done = False
        if a is not None:
            for k in (2, 3, 4):  # we merged k dump groups into one
                if q + k <= len(dump) and a == "".join(strip(x) for x in dump[q:q + k]):
                    lab += ["seg"] * k
                    p, q, done = p + 1, q + k, True
                    break
            if not done:
                for k in (2, 3, 4):  # we split one dump group into k
                    parts = ours[p:p + k]
                    if len(parts) == k and None not in parts and "".join(strip(x) for x in parts) == b:
                        lab.append("seg")
                        p, q, done = p + k, q + 1, True
                        break
        if done:
            continue
        if a is None:
            lab.append("und")
        elif a == b and dump[q].startswith("'"):
            lab.append("dot")
        elif len(a) == len(b) and a.isdigit() and b.isdigit():
            lab.append("conf")
            for x, y in zip(b, a):
                if x != y:
                    conf[(x, y)] = conf.get((x, y), 0) + 1
        else:
            lab.append("other")
        p, q = p + 1, q + 1
    return lab


def anatomy():
    ours = v2_groups()
    a = [g for _, g, _ in ours]
    dump = dump_groups()
    pairs = lcs_align(a, dump)
    conf, labels = {}, {}
    bounds = [(-1, -1)] + pairs + [(len(a), len(dump))]
    for (i0, j0), (i1, j1) in zip(bounds, bounds[1:]):
        if j1 - j0 > 1:
            for j, l in zip(range(j0 + 1, j1), classify_gap(a[i0 + 1:i1], dump[j0 + 1:j1], conf)):
                labels[j] = l
    tot = {}
    for j, l in labels.items():
        k = (l, dump_class(dump[j]))
        tot[k] = tot.get(k, 0) + 1
    print(f"matched {len(pairs)}/{len(dump)}; misses {len(labels)}")
    for l in ("conf", "seg", "dot", "und", "other", "unpaired"):
        n = sum(v for (ll, _), v in tot.items() if ll == l)
        det = ", ".join(f"{c} {v}" for (ll, c), v in sorted(tot.items()) if ll == l)
        print(f"  {l:9s} {n:4d}  ({det})")
    print("digit confusion (true dump digit -> ours), count >= 3:")
    for (x, y), v in sorted(conf.items(), key=lambda t: -t[1]):
        if v >= 3:
            print(f"  {x}->{y} {v}")
    digits = "0123456789"
    print("   ours: " + " ".join(digits))
    for x in digits:
        print(f"  dump {x} " + " ".join(str(conf.get((x, y), 0) if x != y else "-") for y in digits))


def dump_spans():
    """Assign each dump group to one of our folio lines through the v2 LCS anchors (the dump carries no manuscript
    line breaks): a group between two anchors on the same line takes that line; across a line break the gap is
    split in proportion to our tokens on each side."""
    ours = v2_groups()
    a = [g for _, g, _ in ours]
    lines = [ln for ln, _, _ in ours]
    dump = dump_groups()
    pairs = lcs_align(a, dump)
    line_of = {}
    for i, j in pairs:
        line_of[j] = lines[i]
    bounds = [(-1, -1)] + pairs + [(len(a), len(dump))]
    for (i0, j0), (i1, j1) in zip(bounds, bounds[1:]):
        gap_d = list(range(j0 + 1, j1))
        if not gap_d:
            continue
        gl = lines[max(i0, 0):min(i1, len(lines) - 1) + 1] or [lines[-1]]
        for k, j in enumerate(gap_d):
            line_of[j] = gl[min(len(gl) - 1, int(k * len(gl) / len(gap_d)))]
    spans = {}
    for j in range(len(dump)):
        spans.setdefault(line_of[j], []).append(j)
    return dump, spans


def recipe_groups(path, want):
    """A recipe's TSV (line pos digits dot confidence) as {line: [group]}; dot=yes -> "'NN", unreadable -> None."""
    out = {}
    for r in csv.DictReader(open(path, encoding="utf-8"), delimiter="\t"):
        ln = r["line"].strip()
        if ln not in want:
            continue
        d = re.sub(r"[^0-9]", "", r["digits"])
        g = None if not d else ("'" + d if r["dot"].strip().lower() == "yes" else d)
        out.setdefault(ln, []).append(g)
    return out


def score(path, lines, shuffles=20, seed=1):
    dump, spans = dump_spans()
    want = lines.split(",")
    rec = recipe_groups(path, want)
    b = [dump[j] for ln in want for j in spans.get(ln, [])]
    a_by = [rec.get(ln, []) for ln in want]
    a = [g for xs in a_by for g in xs]
    hit, tot = summarize(lcs_pairs(a, b), b)
    rng = random.Random(seed)
    sh = {k: [] for k in tot}
    for _ in range(shuffles):
        s2 = []
        for xs in a_by:
            xs = xs[:]
            rng.shuffle(xs)
            s2 += xs
        h2, _ = summarize(lcs_pairs(s2, b), b)
        for k in tot:
            sh[k].append(h2[k] / tot[k] if tot[k] else float("nan"))
    print(f"{path} lines {lines}: ours {len(a)} groups ({', '.join(f'{ln} {len(x)}' for ln, x in zip(want, a_by))}); "
          f"dump {len(b)} ({', '.join(f'{ln} {len(spans.get(ln, []))}' for ln in want)})")
    for k in ("all", "bare", "dotted"):
        if tot[k]:
            print(f"  {k:7s} real {hit[k]}/{tot[k]} = {hit[k]/tot[k]:.3f}   order-shuffled ({shuffles}) mean "
                  f"{statistics.mean(sh[k]):.3f} sd {statistics.stdev(sh[k]):.3f}")
    ndot = sum(1 for g in a if g and g.startswith("'"))
    print(f"  dots marked by recipe {ndot}; dump dotted {tot['dotted']}")



def segparse(seed=1, shuffles=20, ours=False):
    """MONT-CAL feasibility check for the named next step (no reading, no new signs): if a reader gave only a
    continuous digit stream per line (no group boundaries), how many of the dump's groups would the key's own code
    inventory restore? The stream is the dump itself with boundaries removed (dots kept as a mark on the first digit
    in one run, dropped in the other); symbol glyphs stay as hard breaks. Parse: Viterbi over pieces = a key code
    (log of its letter's share, split among homophones) or, where a dot marks the digit, any 2-digit dotted code;
    undotted non-key 2-digit pieces allowed at a penalty. Control: a random valid 1-/2-digit parse of the same stream."""
    import math
    key = load_key()
    freq = {"e": 14.7, "a": 8.1, "s": 7.9, "i": 7.2, "t": 7.2, "n": 7.1, "r": 6.5, "u": 6.3, "l": 5.5, "o": 5.3,
            "d": 3.7, "c": 3.3, "p": 3.0, "m": 2.9, "q": 1.4, "f": 1.1, "b": 0.9, "g": 0.9, "h": 0.7, "x": 0.4,
            "y": 0.3, "z": 0.1}
    by_letter = {}
    for r in key:
        by_letter.setdefault(r.get("value", r.get("plain", "")).strip().lower()[:1], []).append(r["sign"])
    lp = {}
    for L, signs in by_letter.items():
        for sg in signs:
            lp[sg] = math.log(freq.get(L, 0.5) / 100 / len(signs))
    dump = dump_groups()
    rng = random.Random(seed)

    def streams(keep_dot):
        out, cur = [], []
        src = dump
        if ours:  # our v2 L02-L17 groups with their boundaries dropped; undecidable/illegible break the stream
            src = [g if g is not None else "?" for _, g, _ in v2_groups()]
        for g in src:
            if g.startswith("'"):
                d = g[1:]
                cur += [(d[0], keep_dot)] + [(c, False) for c in d[1:]]
            elif g.isdigit():
                cur += [(c, False) for c in g]
            else:
                if cur:
                    out.append(cur)
                out.append(g)
                cur = []
        if cur:
            out.append(cur)
        return out

    def viterbi(st):
        n = len(st)
        best = [(-1e18, None)] * (n + 1)
        best[0] = (0.0, None)
        for i in range(n):
            if best[i][0] < -1e17:
                continue
            for L in (1, 2):
                if i + L > n:
                    continue
                piece = "".join(c for c, _ in st[i:i + L])
                dotted = st[i][1]
                if dotted:
                    sc = math.log(0.01) if L == 2 else None
                elif piece in lp:
                    sc = lp[piece]
                elif L == 2:
                    sc = math.log(0.0005)
                else:
                    sc = None
                if sc is None or any(d for _, d in st[i + 1:i + L]):
                    continue
                if best[i][0] + sc > best[i + L][0]:
                    best[i + L] = (best[i][0] + sc, (i, ("'" if dotted else "") + piece))
        toks, j = [], n
        while j > 0 and best[j][1]:
            i, t = best[j][1]
            toks.append(t)
            j = i
        return toks[::-1]

    def randparse(st):
        toks, i = [], 0
        while i < len(st):
            L = 2 if i + 1 < len(st) and rng.random() < 0.8 else 1
            toks.append("".join(c for c, _ in st[i:i + L]))
            i += L
        return toks

    for keep_dot in (True, False):
        parsed, rnd = [], [[] for _ in range(shuffles)]
        for st in streams(keep_dot):
            if isinstance(st, str):
                parsed.append(st)
                for r_ in rnd:
                    r_.append(st)
                continue
            parsed += viterbi(st)
            for r_ in rnd:
                r_ += randparse(st)
        ref = dump if keep_dot else [g.lstrip("'") for g in dump]
        hit, tot = summarize(lcs_pairs(parsed, ref), dump)
        rs = [summarize(lcs_pairs(r_, ref), dump)[0] for r_ in rnd]
        tag = ("our v2 digits, " if ours else "") + ("dots as read" if keep_dot else "dots ignored")
        print(f"[{tag}] key-constrained parse: {len(parsed)} groups vs dump {len(dump)}")
        for k in ("all", "bare", "dotted"):
            vals = [r_[k] / tot[k] for r_ in rs]
            print(f"  {k:7s} {hit[k]}/{tot[k]} = {hit[k]/tot[k]:.3f}   random valid parse ({shuffles}) mean "
                  f"{statistics.mean(vals):.3f} sd {statistics.stdev(vals):.3f}")


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
    elif cmd == "anatomy":
        anatomy()
    elif cmd == "spans":
        dump, spans = dump_spans()
        for ln in sorted(spans):
            print(ln, len(spans[ln]), " ".join(dump[j] for j in spans[ln]))
    elif cmd == "segparse":
        segparse(ours="--ours" in sys.argv)
    elif cmd == "score":
        score(sys.argv[2], sys.argv[3])

#!/usr/bin/env python3
"""Exhaustive scripted families for a third hidden message in The Master of Mysteries (1912).

23 Sept 2026. Reads the reconciled OCR (units.get('R')); scores with tools/english_score.py (a model built from
Holmes + Moby Dick, not from this book). Writes runs.tsv (one row per family x unit x selector x offset x
direction), control.tsv (the known messages against their families; planted-message detection rates for the
long-sequence families) and top_windows.tsv (the best windows of every long family, for reading by eye).

python3 families.py            full run
python3 families.py --control  control only
python3 families.py --check    regenerate into a temporary folder and exit 1 if control.tsv, runs.tsv or
                               top_windows.tsv differ from the committed files (rule 7)
"""
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import units  # noqa: E402
from english_score import az, default_model, shuffle_z  # noqa: E402

M = default_model()
RND = random.Random(1912)
L = units.letters


def pick(seq, k, from_end):
    """k-th item (1-based) from the start or the end; None if absent."""
    if len(seq) < k:
        return None
    return seq[-k] if from_end else seq[k - 1]


def letter_of(text, j, from_end):
    s = L(text).upper()
    if len(s) < j:
        return ""
    return s[-j] if from_end else s[j - 1]


# ------------------------------------------------------------------ unit views
def story_units(c):
    pages = {}
    for ln in c["lines"]:
        pages.setdefault(ln["page"], []).append(ln)
    return {
        "word": [[w] for w in c["words"]],
        "sentence": c["sentences"],
        "paragraph": c["paragraphs"],
        "line": [ln["words"] for ln in c["lines"] if ln["words"]],
        "page": [[w for ln in v for w in ln["words"]] for v in pages.values()],
    }


def book_units(chapters):
    out = {"sentence": [], "paragraph": [], "line": [], "page": []}
    for c in chapters:
        u = story_units(c)
        for k in out:
            out[k] += u[k]
    return out


# ------------------------------------------------------------------ rows
ROWS = []


def row(family, unit, selector, offset, direction, n, stat, obs, mu, sd, z, text, note=""):
    ROWS.append([family, unit, selector, str(offset), direction, str(n), stat, f"{obs:.3f}", f"{mu:.3f}",
                 f"{sd:.3f}", f"{z:.2f}", text[:60], note])


def score24(seq_letters, nshuf=500):
    s = "".join(seq_letters)
    obs, z, mu, sd, _ = shuffle_z(M.quad, list(s), nshuf, seed=len(s))
    return obs, z, mu, sd


# ------------------------------------------------------------------ family A: story-level letter acrostics
def family_A(stories, collect=None):
    res = {}
    U = [story_units(c) for c in stories]
    for unit in ("word", "sentence", "paragraph", "line", "page"):
        for k in range(1, 9):
            for kend in (False, True):
                for j in (1, 2):
                    for jend in (False, True):
                        items = [pick(u[unit], k, kend) for u in U]
                        if any(i is None for i in items):
                            continue
                        seq = [letter_of(" ".join(i), j, jend) for i in items]
                        if any(not x for x in seq):
                            continue
                        for direction in ("fwd", "rev"):
                            s = "".join(seq if direction == "fwd" else seq[::-1])
                            key = s
                            sel = f"letter {j} from {'end' if jend else 'start'} of unit {k} from {'end' if kend else 'start'}"
                            res.setdefault(key, []).append((unit, sel, k, direction))
    scored = []
    for s, where in res.items():
        obs, z, mu, sd = score24(list(s))
        cov = M.cover(s)[0]
        scored.append((obs, z, mu, sd, cov, s, where))
    scored.sort(reverse=True)
    for obs, z, mu, sd, cov, s, where in scored:
        unit, sel, k, d = where[0]
        row("A story-level letters", unit, sel, k, d, 24, "quad", obs, mu, sd, z, s,
            f"cover={cov}; same string from {len(where)} unit/selector choices")
    return scored


# ------------------------------------------------------------------ family B: story-level word sequences
def family_B(stories):
    U = [story_units(c) for c in stories]
    seqs = {}
    for k in range(1, 13):
        for kend in (False, True):
            ws = [pick(c["words"], k, kend) for c in stories]
            seqs[("word", f"word {k} from {'end' if kend else 'start'}", k)] = ws
    for unit in ("sentence", "paragraph", "line", "page"):
        for k in range(1, 6):
            for kend in (False, True):
                for wend in (False, True):
                    ws = [pick(pick(u[unit], k, kend) or [""], 1, wend) for u in U]
                    seqs[(unit, f"{'last' if wend else 'first'} word of {unit} {k} from {'end' if kend else 'start'}", k)] = ws
    out = []
    for (unit, sel, k), ws in seqs.items():
        if any(not w for w in ws):
            continue
        for direction in ("fwd", "rev"):
            w2 = ws if direction == "fwd" else ws[::-1]
            obs, z, mu, sd, _ = shuffle_z(M.words_pmi, w2, 300, seed=7)
            row("B story-level words", unit, sel, k, direction, 24, "words_pmi", obs, mu, sd, z, " ".join(w2))
            out.append((z, obs, " ".join(w2), unit, sel, direction))
    return out


# ------------------------------------------------------------------ long sequences (book-wide, introduction)
def long_letter_stat(s, w):
    return M.best_window(s, w)[0]


def long_family_letters(family, seqs, w=24, nshuf=20, top=None):
    """seqs: {(unit, selector, offset): [letter per unit]}; best window of w letters, cover, shuffle z."""
    out = []
    for (unit, sel, off), seq in seqs.items():
        for direction in ("fwd", "rev"):
            s = "".join(seq if direction == "fwd" else seq[::-1])
            if len(s) < w + 5:
                continue
            b, pos = M.best_window(s, w)
            cov, cpos = M.cover(s)
            rnd = random.Random(len(s) + off)
            xs, cs = [], []
            u = list(s)
            ncov = min(nshuf, 8)
            for t_ in range(nshuf):
                rnd.shuffle(u)
                t = "".join(u)
                xs.append(M.best_window(t, w)[0])
                if t_ < ncov:
                    cs.append(M.cover(t)[0])
            mu = sum(xs) / nshuf
            sd = (sum((x - mu) ** 2 for x in xs) / (nshuf - 1)) ** 0.5 or 1e-9
            cmu = sum(cs) / ncov
            csd = (sum((x - cmu) ** 2 for x in cs) / (ncov - 1)) ** 0.5 or 1e-9
            ph = plant_letters(s, w)
            row(family, unit, sel, off, direction, len(s), f"best{w}", b, mu, sd, (b - mu) / sd, s[pos:pos + w],
                f"at {pos}; control: {ph}/{NPLANT} planted {w}-letter book sentences recovered as the best window; "
                f"longest word-cover run {cov} (shuffled {cmu:.1f}+-{csd:.1f}, z {(cov - cmu) / csd:.2f}): "
                f"{s[cpos:cpos + cov][:40]}")
            out.append(((b - mu) / sd, b, (cov - cmu) / csd, cov, s[pos:pos + w], s[cpos:cpos + cov], unit, sel, off,
                        direction))
            if top is not None:
                top.append([family, unit, sel, str(off), direction, f"{b:.3f}", s[pos:pos + w], str(cov),
                            s[cpos:cpos + cov]])
    return out


def long_family_words(family, seqs, ws_=(6, 8, 12), nshuf=20, top=None, ktop=15):
    """Best windows of w words by lift (english_score.lift_windows); z against the same statistic on shuffles."""
    out = []
    for (unit, sel), ws in seqs.items():
        ws = [x for x in ws if x]
        for direction in ("fwd", "rev"):
            w2 = ws if direction == "fwd" else ws[::-1]
            for w in ws_:
                if len(w2) < w + 5:
                    continue
                wins, clean = M.lift_windows(w2, w, ktop)
                b, pos = wins[0]
                rnd = random.Random(len(w2) + w)
                xs = []
                u = list(w2)
                for _ in range(nshuf):
                    rnd.shuffle(u)
                    xs.append(M.lift_windows(u, w, 1)[0][0][0])
                mu = sum(xs) / nshuf
                sd = (sum((x - mu) ** 2 for x in xs) / (nshuf - 1)) ** 0.5 or 1e-9
                txt = " ".join(clean[pos:pos + w])
                h1, h15 = plant_words(w2, w)
                row(family, unit, sel, w, direction, len(w2), f"best{w}_lift", b, mu, sd, (b - mu) / sd, txt,
                    f"at {pos}; control: planted {w}-word book sentence is the best window {h1}/{NPLANT}, "
                    f"in the top 15 (read by eye in top_windows.tsv) {h15}/{NPLANT}")
                out.append(((b - mu) / sd, b, txt, unit, sel, direction, w))
                if top is not None:
                    for sc, p in wins:
                        top.append([family, unit, sel, str(w), direction, f"{sc:.3f}", " ".join(clean[p:p + w]),
                                    str(p), ""])
    return out


NPLANT = 10
_SENTS = []


def _sents():
    if not _SENTS:
        _SENTS.extend(s for c in units.get("R").stories for s in c["sentences"])
    return _SENTS


def plant_letters(s, w, n=NPLANT):
    rnd = random.Random(len(s) * 31 + w)
    pool = [L("".join(x)).upper() for x in _sents() if len(L("".join(x))) >= w]
    hits = 0
    for _ in range(n):
        msg = rnd.choice(pool)[:w]
        pos = rnd.randrange(0, len(s) - w)
        t = s[:pos] + msg + s[pos + w:]
        hits += abs(M.best_window(t, w)[1] - pos) <= 3
    return hits


def plant_words(ws, w, n=NPLANT):
    rnd = random.Random(len(ws) * 17 + w)
    pool = [x for x in _sents() if len(x) >= w]
    h1 = h15 = 0
    for _ in range(n):
        msg = rnd.choice(pool)[:w]
        pos = rnd.randrange(0, len(ws) - w)
        t = list(ws[:pos]) + list(msg) + list(ws[pos + w:])
        wins = M.lift_windows(t, w, 15)[0]
        h1 += abs(wins[0][1] - pos) <= 2
        h15 += any(abs(p - pos) <= 2 for _, p in wins)
    return h1, h15


def letter_seqs(units_by_name, names, offsets=(1, 2, 3)):
    seqs = {}
    for unit in names:
        items = units_by_name[unit]
        for off in offsets:
            for end in (False, True):
                seq = [letter_of(" ".join(i) if isinstance(i, list) else i, off, end) for i in items]
                seqs[(unit, f"letter {off} from {'end' if end else 'start'}", off)] = [x for x in seq if x]
    return seqs


def word_seqs(units_by_name, names):
    seqs = {}
    for unit in names:
        items = [i for i in units_by_name[unit] if i]
        seqs[(unit, "first word")] = [i[0] for i in items]
        seqs[(unit, "last word")] = [i[-1] for i in items]
    return seqs


def printed_line_letters(chapters):
    """Printed lines: letters k=1..3 from each end of every line, book-wide and page by page."""
    lines = [ln for c in chapters for ln in c["lines"]]
    return lines


# ------------------------------------------------------------------ controls
def control(stories, book):
    ctl = []
    # 1. the two known messages inside their own family A
    scoredA = family_A(stories)
    known = units.KNOWN
    rank = {s: i + 1 for i, (_, _, _, _, _, s, _) in enumerate(scoredA)}
    ranked = [(s, obs, z) for obs, z, _, _, _, s, _ in scoredA]
    others = [(s, obs, z) for s, obs, z in ranked if s not in known.values()]
    for name, s in known.items():
        obs = M.quad(s)
        z = next(z for t, o, z in ranked if t == s)
        ctl.append(["A", f"known {name}-letters message", s, str(rank.get(s)), str(len(ranked)), f"{obs:.3f}",
                    f"{z:.2f}", f"{obs - others[0][1]:.3f}", f"best other: {others[0][0]} {others[0][1]:.3f} z {others[0][2]:.2f}"])
    # 2. OCR robustness: the same family from each single OCR pass
    for src in ("UC", "CU"):
        b = units.get(src)
        f, l = units.known_acrostics(b)
        ctl.append(["A-ocr", f"single pass {src} (drop capitals restored)", f + " / " + l,
                    str(sum(a != b for a, b in zip(f, known['first'])) + sum(a != b for a, b in zip(l, known['last']))),
                    "48", f"{M.quad(f):.3f}", "", "", "letters differing from the known messages"])
    # 3. planted-message detection for the long letter families (book-wide printed-line initials, W=24)
    sents = [" ".join(s) for c in stories for s in c["sentences"] if 24 <= len(L("".join(s))) <= 60]
    lines = [ln for c in book.chapters[1:] for ln in c["lines"]]
    base = [letter_of(ln["text"], 1, False) for ln in lines]
    base = [x for x in base if x]
    nat = M.best_window("".join(base), 24)[0]
    for trial_set, W in (("24-letter plant, W=24", 24),):
        hits, scores = 0, []
        for t in range(40):
            msg = L(RND.choice(sents)).upper()[:24]
            pos = RND.randrange(0, len(base) - 24)
            s = base[:pos] + list(msg) + base[pos + 24:]
            b, bp = M.best_window("".join(s), W)
            scores.append(M.quad(msg))
            hits += abs(bp - pos) <= 3
        ctl.append(["D", f"book-wide printed-line initials, {trial_set}", "40 trials", str(hits), "40",
                    f"{sum(scores) / 40:.3f}", "", f"{nat:.3f}",
                    "hits = best window lands on the plant (+-3); col 6 = mean plant quad; col 8 = natural best window"])
    # 4. planted word-sentence detection for the long word families (lift, windows of 6, 8, 12 words)
    bu = book_units(stories)
    for unit, which in (("paragraph", 0), ("sentence", 0), ("line", 0), ("paragraph", -1)):
        seq = [i[which] for i in bu[unit] if i]
        for W in (6, 8, 12):
            wsents = [s for c in stories for s in c["sentences"] if len(s) >= W]
            nat = M.lift_windows(seq, W, 1)[0][0][0]
            hits, hits15 = 0, 0
            for t in range(40):
                msg = RND.choice(wsents)[:W]
                pos = RND.randrange(0, len(seq) - W)
                s = seq[:pos] + msg + seq[pos + W:]
                wins = M.lift_windows(s, W, 15)[0]
                hits += abs(wins[0][1] - pos) <= 2
                hits15 += any(abs(bp - pos) <= 2 for _, bp in wins)
            ctl.append(["C", f"{'first' if which == 0 else 'last'} words of {unit}s, {W}-word book-sentence plant",
                        "40 trials", str(hits), "40", str(hits15), "", f"{nat:.3f}",
                        "col 4 = best lift window lands on the plant (+-2); col 6 = plant among the top 15 "
                        "windows written to top_windows.tsv; col 8 = natural best window"])
    # 5. planted 24-word sentence as the story-level word family (family B, whole-sequence pmi z)
    wlong = [s for c in stories for s in c["sentences"] if len(s) >= 24]
    zs = []
    for t in range(40):
        msg = RND.choice(wlong)[:24]
        zs.append(shuffle_z(M.words_pmi, msg, 200, seed=t)[1])
    zs.sort()
    ctl.append(["B", "24-word book sentence as a story-level word sequence", "40 trials",
                str(sum(z >= 3 for z in zs)), "40", f"{zs[len(zs) // 2]:.2f}", f"{zs[len(zs) // 10]:.2f}", "",
                "col 4 = trials with z>=3; col 6 = median z; col 7 = 10th percentile z"])
    return ctl, scoredA


OUT = HERE


def main():
    global OUT
    control_only = "--control" in sys.argv
    if "--check" in sys.argv:
        import tempfile
        OUT = Path(tempfile.mkdtemp())
    book = units.get("R")
    stories = book.stories
    ctl, scoredA = control(stories, book)
    with open(OUT / "control.tsv", "w") as f:
        f.write("family\tcontrol\tstring\trank_or_hits\tof\tquad_or_score\tz\tmargin_or_natural\tnote\n")
        for r in ctl:
            f.write("\t".join(r) + "\n")
    for r in ctl:
        print("\t".join(r))
    if control_only:
        return
    family_B(stories)
    top = []
    # C: long word sequences, book-wide (stories only), first/last word of each unit
    bu = book_units(stories)
    long_family_words("C book-wide words", word_seqs(bu, ("sentence", "paragraph", "line", "page")), top=top)
    # D: long letter sequences, book-wide
    long_family_letters("D book-wide letters", letter_seqs(bu, ("sentence", "paragraph", "line", "page")), top=top)
    # D-page: printed-line letters page by page (each page's own sequence)
    pages = {}
    for c in stories:
        for ln in c["lines"]:
            pages.setdefault(ln["page"], []).append(ln)
    for off in (1, 2, 3):
        for end in (False, True):
            best = None
            allq = []
            for pg, lns in pages.items():
                s = "".join(letter_of(ln["text"], off, end) for ln in lns)
                if len(s) < 10:
                    continue
                q = M.quad(s)
                allq.append(q)
                if best is None or q > best[0]:
                    best = (q, pg, s)
            mu = sum(allq) / len(allq)
            sd = (sum((x - mu) ** 2 for x in allq) / (len(allq) - 1)) ** 0.5
            row("D per-page printed lines", "line", f"letter {off} from {'end' if end else 'start'}", off, "fwd",
                len(allq), "best page quad", best[0], mu, sd, (best[0] - mu) / sd, best[2],
                f"page {best[1]}; z is against the other pages")
    # E: titles and contents
    titles = [t for t, _ in units.TITLES]
    tw = [[w for w in re.findall(r"[A-Za-z']+", t)] for t in titles]
    seqsE = {}
    for j in range(1, 6):
        for end in (False, True):
            seqsE[("title", f"letter {j} from {'end' if end else 'start'} of each title", j)] = [
                letter_of(t, j, end) for t in titles]
    for k in range(1, 4):
        for end in (False, True):
            seqsE[("title word", f"first letter of word {k} from {'end' if end else 'start'}", k)] = [
                letter_of(pick(w, k, end) or "", 1, False) for w in tw]
            seqsE[("title word", f"last letter of word {k} from {'end' if end else 'start'}", k)] = [
                letter_of(pick(w, k, end) or "", 1, True) for w in tw]
    nums = [p for _, p in units.TITLES]
    seqsE[("contents", "page number mod 26 (A=1)", 0)] = [chr(64 + ((n - 1) % 26) + 1) for n in nums]
    lens = [b - a for a, b in zip(nums, nums[1:] + [units.LAST_PAGE + 1])]
    seqsE[("contents", "story length in pages mod 26 (A=1)", 0)] = [chr(64 + ((n - 1) % 26) + 1) for n in lens]
    allw = [w for ws in tw for w in ws]
    for (unit, sel, k), seq in seqsE.items():
        seq = [x for x in seq if x]
        for direction in ("fwd", "rev"):
            s = "".join(seq if direction == "fwd" else seq[::-1])
            obs, z, mu, sd = score24(list(s), 300)
            row("E titles/contents", unit, sel, k, direction, len(s), "quad", obs, mu, sd, z, s,
                f"cover={M.cover(s)[0]}")
    for sel, f in (("first letters of all title words", lambda w: w[0]), ("last letters of all title words",
                                                                           lambda w: L(w)[-1])):
        s = "".join(f(w).upper() for w in allw)
        long_family_letters("E titles/contents", {("title words", sel, 1): list(s)}, w=15, nshuf=50, top=top)
    # F: the Introduction alone
    intro = book.chapters[0]
    iu = story_units(intro)
    long_family_letters("F introduction", letter_seqs(iu, ("word", "sentence", "paragraph", "line")), w=15,
                        nshuf=50, top=top)
    long_family_words("F introduction", word_seqs(iu, ("sentence", "paragraph", "line")), ws_=(4, 6), nshuf=50, top=top)
    iletters = L(" ".join(intro["words"])).upper()
    best = []
    for n in range(2, 61):
        for o in range(n):
            s = iletters[o::n]
            if len(s) >= 12:
                best.append((M.quad(s), M.cover(s)[0], n, o, s))
    for n in range(2, 31):
        for o in range(n):
            ws = intro["words"][o::n]
            s = "".join(w[0] for w in ws).upper()
            if len(s) >= 12:
                best.append((M.quad(s), M.cover(s)[0], -n, o, s))
    best.sort(reverse=True)
    # control: overwrite the letters at one random (n, offset) with a book sentence; is it ranked first?
    rnd = random.Random(465)
    pool = [L("".join(x)).upper() for x in _sents()]
    fh = 0
    for _ in range(NPLANT):
        n = rnd.randrange(8, 61)
        o = rnd.randrange(n)
        idx = list(range(o, len(iletters), n))
        msg = "".join(p for p in pool if len(p) >= 20)
        start = rnd.randrange(0, len(msg) - len(idx))
        t = list(iletters)
        for k, i in enumerate(idx):
            t[i] = msg[start + k]
        t = "".join(t)
        cand = max((M.quad(t[oo::nn]), nn, oo) for nn in range(2, 61) for oo in range(nn) if len(t[oo::nn]) >= 12)
        fh += (cand[1], cand[2]) == (n, o)
    qs = [b[0] for b in best]
    mu = sum(qs) / len(qs)
    sd = (sum((x - mu) ** 2 for x in qs) / (len(qs) - 1)) ** 0.5
    for q, cov, n, o, s in best[:5]:
        row("F introduction", "letter" if n > 0 else "word initial", f"every {abs(n)}th from {o}", abs(n), "fwd",
            len(s), "quad", q, mu, sd, (q - mu) / sd, s, f"cover={cov}; z against all {len(qs)} (n, offset) choices; control: {fh}/{NPLANT} planted "
            f"every-nth-letter sentences ranked first")
    # G: plate captions
    caps = [p["text"] for p in units.get("UC").plates]
    capw = [re.findall(r"[A-Za-z']+", c) for c in caps]
    capw = [w for w in capw if w]
    for sel, seq in (("first letter", [w[0][0] for w in capw]), ("last letter", [L(w[-1])[-1] for w in capw])):
        for direction in ("fwd", "rev"):
            s = "".join(seq if direction == "fwd" else seq[::-1]).upper()
            obs, z, mu, sd = score24(list(s), 300)
            row("G plate captions", "caption", sel, 1, direction, len(s), "quad", obs, mu, sd, z, s,
                f"cover={M.cover(s)[0]}; UC scan, {len(capw)} captions")
    ws = [w[0] for w in capw]
    obs, z, mu, sd, _ = shuffle_z(M.words_pmi, ws, 300)
    row("G plate captions", "caption", "first words", 1, "fwd", len(ws), "words_pmi", obs, mu, sd, z, " ".join(ws))
    # write
    with open(OUT / "runs.tsv", "w") as f:
        f.write("family\tunit\tselector\toffset\tdirection\tn\tstat\tobserved\tshuffle_mean\tshuffle_sd\tz\t"
                "best_text\tnote\n")
        for r in ROWS:
            f.write("\t".join(r) + "\n")
    with open(OUT / "top_windows.tsv", "w") as f:
        f.write("family\tunit\tselector\toffset\tdirection\tbest_window_score\tbest_window\tcover_run\tcover_text\n")
        for r in top:
            f.write("\t".join(r) + "\n")
    print(len(ROWS), "rows")
    if "--check" in sys.argv:
        stale = [f for f in ("control.tsv", "runs.tsv", "top_windows.tsv")
                 if (OUT / f).read_bytes() != (HERE / f).read_bytes()]
        print("STALE: " + ", ".join(stale) if stale else "OK: committed tables regenerate exactly")
        sys.exit(1 if stale else 0)


if __name__ == "__main__":
    main()

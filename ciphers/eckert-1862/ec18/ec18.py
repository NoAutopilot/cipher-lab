#!/usr/bin/env python3
"""A3V3-ECK18 (4 Oct 2026): mssEC 18 (Huntington object 10074, 1864-65 "Ciphers Sent") volunteer text read through
Cipher No. 1 with ciphers/eckert-1864/decode.py (imported, not copied), then print-checked against OR ser. I vols. 32-46.

Usage: ec18.py DATA_DIR OR_DIR [--write | --check]
  DATA_DIR/vol18.json: one CONTENTdm dmQuery (URL and sha256 in ../pilot1864/manifest.tsv; the Decoding the Civil War
  volunteers' transcription, not committed). OR_DIR/<vol>.txt: IA _djvu.txt per OR volume (ids in or_volumes.tsv; not
  committed, re-fetch). --write rewrites entries.tsv, matches.tsv, control.tsv and readings.md; --check exits 1 if any
  is stale.

Entries: the volunteer text is split on blank lines; a block whose first three lines carry a clear date (month day
year) opens an entry, a block without one continues the current entry (pages in page-number order). The header lines
up to the date line are dropped; the rest is decoded by eckert-1864 decode.decode_entry (grades are the key.md row
grades: H = mssEC 41). oov = tokens of the reading outside brackets that are in no English corpus word list
(tools/data/en and the two default novels) and longer than one letter: unkeyed code words, names, misspellings.
Book: an entry is Cipher No. 1 when its No. 1 period/signature words (unity, zebra, zodiac, walrus, webster, yoke,
youth) outnumber its No. 2 punctuation words (tulip, pike, yacht, yawl, yard(stick); ciphers/eckert-1864/key-no2.md),
No. 2 for the reverse, '?' otherwise; the same printed words carry other meanings in No. 2, so a No. 2 entry read with
key.md gives wrong meanings at grade H. Known answer: --book-test runs the rule on eckert-1864's image-read entries
(ciphertext.txt = No. 1, ciphertext-no2.txt = No. 2). "Fully keyed" = book 1, >= 3 keyed tokens and oov 0.

Print match: the reading with every keyed token replaced by its meaning is cut into word 5-grams; a 5-gram occurring
more than 8 times across the OR volumes is a formula and ignored (or_match.py's rule). An entry matches an OR volume when
>= MIN distinct 5-grams fall in one 400-word block AND the entry's clear date ("July 10, 1864", day and month) occurs
within 1500 words before the block's first hit (the OR telegram heading). Control (rule 3): the same matcher with the
dates permuted among the entries (seed 18, 20 permutations; plus the pre-registered 20-entry draw) -- the date condition
is the only thing a permutation can change, so the control can fail differently from the target.
"""
import json, re, sys, random, collections
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "ciphers" / "eckert-1864"))
import decode as d1  # noqa: E402

MIN = 4
SEED = 18
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
DATE = re.compile(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s*(\d{1,2})(?:st|nd|rd|th|d)?\.?,?\s*"
                  r"(?:18)?(6[3-6])\b", re.I)


def vocab():
    ws = set()
    for p in list((ROOT / "tools/data/en").glob("pg*.txt")) + [ROOT / "tools/data/pg1661_holmes.txt",
                                                                ROOT / "tools/data/pg2701_mobydick.txt"]:
        ws |= set(re.findall(r"[a-z]+", p.read_text(errors="ignore").lower()))
    return ws


def clean(t):
    t = re.sub(r"<deletion>.*?</deletion>", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", "", t)
    return t.replace("&", " and ").replace("\r", "")


def entries(data):
    recs = json.load(open(Path(data) / "vol18.json"))["records"]
    pages = []
    for r in recs:
        t = r.get("transc")
        m = re.match(r"Page (\d+)", r["title"])
        if isinstance(t, str) and t.strip() and m:
            pages.append((int(m.group(1)), int(r["pointer"]), clean(t)))
    out, cur = [], None
    for pg, ptr, t in sorted(pages):
        for blk in [b for b in re.split(r"\n\s*\n", t) if b.strip()]:
            lines = [l for l in blk.split("\n") if l.strip()]
            hit = None
            for i, l in enumerate(lines[:3]):
                m = DATE.search(l)
                if m:
                    hit = (i, m)
                    break
            if hit:
                i, m = hit
                mon = [x[:3] for x in MONTHS].index(m.group(1)[:3].title())
                cur = {"page": pg, "ptr": ptr, "date": (1800 + int(m.group(3)), mon + 1, int(m.group(2))),
                       "header": " / ".join(lines[: i + 1]), "body": lines[i + 1:]}
                out.append(cur)
            elif cur is not None:
                cur["body"] += lines
    for n, e in enumerate(out):
        e["id"] = f"{e['ptr']}.{n}"
    return out


N1 = {"unity", "zebra", "zodiac", "walrus", "webster", "yoke", "youth"}  # No. 1 period / signature words
N2 = {"tulip", "pike", "yacht", "yawl", "yard", "yardstick"}  # No. 2 period / comma / signed (key-no2.md)


def book(text):
    """'1', '2' or '?': which printed book an entry uses, by its punctuation and signature words (marker counts)."""
    w = [x.lower() for x in re.findall(r"[A-Za-z]+", text)]
    n1, n2 = sum(x in N1 for x in w), sum(x in N2 for x in w)
    return "1" if n1 > n2 else "2" if n2 > n1 else "?"


def plain_of(reading):
    """The reading with brackets resolved to their meanings, braces (date, time, tail) dropped."""
    r = re.sub(r"\{[^}]*\}", " ", reading)
    r = re.sub(r"\[([^\]]*)\]", r" \1 ", r)
    return r


def words(t):
    return re.findall(r"[a-z]+|\d+", t.lower())


HDR = re.compile(r"^\s*(\d{1,4})\s+[A-Z][A-Z .,'-]{6,}|[A-Z.\]]\s+(\d{1,4})\s*$")  # or_match.py's page heading
PAGE = {}


def or_index(ordir, grams):
    vols, pos = {}, collections.defaultdict(list)
    for f in sorted(Path(ordir).glob("*.txt")):
        w, pg, cur = [], [], ""
        for line in f.read_text(errors="ignore").splitlines():
            m = HDR.search(line)
            if m:
                cur = m.group(1) or m.group(2)
            lw = words(line)
            w += lw
            pg += [cur] * len(lw)
        vols[f.stem], PAGE[f.stem] = w, pg
        for i in range(len(w) - 4):
            g = " ".join(w[i:i + 5])
            if g in grams:
                pos[g].append((f.stem, i))
    return vols, {g: l for g, l in pos.items() if len(l) <= 8}


def date_near(vw, j, date):
    y, mo, d = date
    win = " ".join(vw[max(0, j - 1500):j + 50])
    return re.search(rf"\b{MONTHS[mo - 1].lower()} {d} (?:{y}|18\d\d)?", win) is not None


def match(es, vols, pos, dates, minn=MIN):
    res = {}
    for e in es:
        gs = e["grams"]
        hits = collections.defaultdict(set)
        first = {}
        for g in sorted(gs):
            for v, j in pos.get(g, ()):
                hits[(v, j // 400)].add(g)
                first[(v, j // 400)] = min(first.get((v, j // 400), j), j)
        best = None
        for (v, b), s in sorted(hits.items()):
            if len(s) >= minn and date_near(vols[v], first[(v, b)], dates[e["id"]]):
                if best is None or len(s) > best[1]:
                    best = (v, len(s), first[(v, b)])
        if best:
            res[e["id"]] = best
    return res


def book_test():
    base = ROOT / "ciphers" / "eckert-1864"
    ok = tot = bad = 0
    for f, want in (("ciphertext.txt", "1"), ("ciphertext-no2.txt", "2")):
        for h, lines in d1.load_ciphertext(base / f):
            got = book(d1.entry_text(lines))
            tot += 1
            ok += got == want
            bad += got not in (want, "?")
            if got != want:
                print(f"miss: {f} {h[:50]} -> {got}")
    print(f"book rule known answer: {ok}/{tot} right, {bad} wrong book, {tot - ok - bad} unassigned")
    return 0 if bad == 0 else 1


STOP = {"maj", "gen", "genl", "general", "the", "of", "and", "u", "s", "us", "a", "in", "to", "col", "brig", "ed", "ing",
        "er", "lieut", "capt", "captain", "major", "dept", "department", "at", "on", "for", "by", "w", "h", "j", "b", "c",
        "e", "f", "g", "l", "m", "o", "p", "r", "t", "x", "y", "is", "be", "as", "fredk", "geo", "wm", "jno", "an"}


def meaning_words(reading):
    """Content words of each keyed word-kind meaning in a reading: list of sets (one per keyed token)."""
    out = []
    for m in re.findall(r"\[([^\]]*)\]", reading):
        if m in (".", ",", ";", ":", "?", "!", "-", "signed", '"', "( )", "(paragraph)") or m.isdigit():
            continue
        ws = {w for w in re.findall(r"[a-z]+", re.sub(r"\(.*?\)", " ", m.lower())) if w not in STOP and len(w) > 2}
        if ws:
            out.append(ws)
    return out


def agreement(pairs, vols):
    """pairs: [(meaning-word sets, (vol, n, j))]. Share of keyed meanings with a content word in the OR window."""
    hit = tot = 0
    for mws, (v, n, j) in pairs:
        win = set(vols[v][max(0, j - 150):j + 450])
        for ws in mws:
            tot += 1
            hit += bool(ws & win)
    return hit, tot


def main(argv):
    if argv and argv[0] == "--book-test":
        return book_test()
    data, ordir = argv[0], argv[1]
    key, voc = d1.load_key(), vocab()
    es = entries(data)
    for e in es:
        text = re.sub(r"\s+", " ", " ".join(e["body"])).strip()
        reading, counts = d1.decode_entry(text, key)
        e["reading"], e["counts"] = reading, counts
        bare = re.sub(r"\[[^\]]*\]|\{[^}]*\}", " ", reading)
        e["oov"] = sum(1 for w in re.findall(r"[A-Za-z]+", bare) if w.lower() not in voc and len(w) > 1)
        e["keyed"] = sum(counts.values())
        e["book"] = book(text)
        e["full"] = e["book"] == "1" and e["keyed"] >= 3 and e["oov"] == 0
        w = words(plain_of(reading))
        e["grams"] = {" ".join(w[i:i + 5]) for i in range(len(w) - 4)}
    full = [e for e in es if e["full"]]
    allg = set().union(*(e["grams"] for e in es))
    vols, pos = or_index(ordir, allg)
    real_dates = {e["id"]: e["date"] for e in full}
    real = match(full, vols, pos, real_dates)

    rng = random.Random(SEED)
    ids = [e["id"] for e in full]
    perm = []
    for k in range(20):
        sh = ids[:]
        rng.shuffle(sh)
        perm.append(len(match(full, vols, pos, {a: real_dates[b] for a, b in zip(ids, sh)})))
    # matcher sanity on every entry, any book (plain stretches still match when the book is wrong): real vs permuted
    alld = {e["id"]: e["date"] for e in es}
    allreal = match(es, vols, pos, alld)
    aids = [e["id"] for e in es]
    aperm = []
    for k in range(5):
        sh = aids[:]
        rng.shuffle(sh)
        aperm.append(len(match(es, vols, pos, {a: alld[b] for a, b in zip(aids, sh)})))
    # keyed meanings against the printed text of the same telegram (book-1 matched entries), and against another
    # matched entry's window (rotation by one; seed-free) as the control
    b1 = [e for e in es if e["id"] in allreal and e["book"] == "1"]
    b2 = [e for e in es if e["id"] in allreal and e["book"] == "2"]
    ag = agreement([(meaning_words(e["reading"]), allreal[e["id"]]) for e in b1], vols)
    agc = agreement([(meaning_words(e["reading"]), allreal[f["id"]]) for e, f in zip(b1, b1[1:] + b1[:1])], vols)
    ag2 = agreement([(meaning_words(e["reading"]), allreal[e["id"]]) for e in b2], vols)
    # the brief's 20-entry control: 20 fully keyed entries drawn with seed 18, dates permuted among them (derangement)
    draw = sorted(random.Random(SEED).sample(ids, min(20, len(ids))))
    sub = [e for e in full if e["id"] in draw]
    real20 = len(match(sub, vols, pos, real_dates))
    rot = draw[1:] + draw[:1]
    sh20 = len(match(sub, vols, pos, {a: real_dates[b] for a, b in zip(draw, rot)}))

    def fmt(d):
        return f"{d[0]}-{d[1]:02d}-{d[2]:02d}"
    ent = ["id\tpage\tdate\tbook\tkeyed\tH\tC\tI\tM\toov\tfully_keyed\tor_match"]
    for e in es:
        c = e["counts"]
        m = real.get(e["id"]) or allreal.get(e["id"])
        ent.append(f"{e['id']}\t{e['page']}\t{fmt(e['date'])}\t{e['book']}\t{e['keyed']}\t{c['H']}\t{c['C']}\t{c['I']}\t{c['M']}\t"
                   f"{e['oov']}\t{int(e['full'])}\t{'OR ' + m[0] if m else ''}")
    mt = ["id\tdate\tor_volume\tor_page_ocr\tshared_5grams\tor_context"]
    for e in full:
        if e["id"] in real:
            v, n, j = real[e["id"]]
            mt.append(f"{e['id']}\t{fmt(e['date'])}\t{v}\t{PAGE[v][j]}\t{n}\t{' '.join(vols[v][max(0, j - 15):j + 25])}")
    tot = collections.Counter()
    for e in full:
        tot.update(e["counts"])
    pm = sorted(perm)
    ctl = ["statistic\tvalue",
           f"pages_with_entry_header\t{len({e['page'] for e in es})}", f"entries\t{len(es)}",
           f"book_1\t{sum(e['book'] == '1' for e in es)}", f"book_2\t{sum(e['book'] == '2' for e in es)}",
           f"book_unassigned\t{sum(e['book'] == '?' for e in es)}", f"fully_keyed\t{len(full)}",
           f"fully_keyed_grades\tH {tot['H']}, C {tot['C']}, I {tot['I']}, M {tot['M']}",
           f"or_matches_real_dates\t{len(real)}",
           f"or_matches_permuted_dates_mean\t{sum(perm) / len(perm):.2f}",
           f"or_matches_permuted_dates_max\t{pm[-1]}",
           f"draw20_real_dates\t{real20}", f"draw20_rotated_dates\t{sh20}",
           f"all_entries_or_matches_real_dates\t{len(allreal)}",
           f"all_entries_or_matches_permuted_dates_mean\t{sum(aperm) / len(aperm):.2f}",
           f"all_entries_or_matches_by_book\t" + ", ".join(f"{b} {sum(1 for e in es if e['id'] in allreal and e['book'] == b)}"
                                                          for b in "12?"),
           f"book1_matched_keyed_meanings_in_print\t{ag[0]}/{ag[1]} = {ag[0] / max(1, ag[1]):.3f}",
           f"book1_control_other_entry_window\t{agc[0]}/{agc[1]} = {agc[0] / max(1, agc[1]):.3f}",
           f"book2_entries_read_with_key_md_in_print\t{ag2[0]}/{ag2[1]} = {ag2[0] / max(1, ag2[1]):.3f}",
           f"or_volumes\t{len(vols)}", f"min_5grams\t{MIN}"]
    rd = ["# mssEC 18: fully keyed entries read through Cipher No. 1 (A3V3-ECK18, 4 Oct 2026)", "",
          "Derived by ec18.py from the Decoding the Civil War volunteer transcription (not reconciled against the page "
          "image: every reading is conditional on that transcription, rule 2) and ciphers/eckert-1864/key.md (mssEC 41). "
          "Brackets are key.md meanings with that row's grade; words outside brackets are as the volunteers wrote them. "
          "Not a novelty claim (rule 10).", ""]
    for e in full:
        m = real.get(e["id"])
        c = e["counts"]
        rd += [f"**{e['id']}** (Page {e['page']}, {fmt(e['date'])}; H {c['H']} C {c['C']} I {c['I']} M {c['M']}; "
               f"{'print: OR ser. I vol. ' + m[0] + ' p. ' + PAGE[m[0]][m[2]] + ' (OCR running head), ' + str(m[1]) + ' shared 5-grams' if m else 'no OR ser. I vols. 32-46 match'})", "",
               e["reading"], ""]
    outs = {"entries.tsv": "\n".join(ent) + "\n", "matches.tsv": "\n".join(mt) + "\n",
            "control.tsv": "\n".join(ctl) + "\n", "readings.md": "\n".join(rd)}
    if "--write" in argv:
        for k, v in outs.items():
            (HERE / k).write_text(v)
    elif "--check" in argv:
        stale = [k for k, v in outs.items() if not (HERE / k).exists() or (HERE / k).read_text() != v]
        if stale:
            sys.stderr.write("stale: " + ", ".join(stale) + "\n")
            return 1
        print("current")
    print(outs["control.tsv"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

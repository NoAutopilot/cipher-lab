#!/usr/bin/env python3
"""A3V3-ECK18 (4 Oct 2026): mssEC 18 (Huntington object 10074, 1864-65 "Ciphers Sent") volunteer text read through
Cipher No. 1 with ciphers/eckert-1864/decode.py (imported, not copied), then print-checked against OR ser. I vols. 32-46.

Usage: ec18.py DATA_DIR OR_DIR [--book 2] [--possessive] [--guard DIR62] [--write | --check]
       ec18.py DATA_DIR OR_DIR --guard-test DIR62 [--possessive]
       ec18.py DATA_DIR OR_DIR --assign [--possessive] [--guard DIR62] [--write | --check]
       ec18.py DATA_DIR --assign-free DIR62 [--write | --check]
       ec18.py DATA_DIR --read-free DIR62 [--write | --check]
  DATA_DIR/vol18.json: one CONTENTdm dmQuery (URL and sha256 in ../pilot1864/manifest.tsv; the Decoding the Civil War
  volunteers' transcription, not committed). OR_DIR/<vol>.txt: IA _djvu.txt per OR volume (ids in or_volumes.tsv; not
  committed, re-fetch). --write rewrites entries.tsv, matches.tsv, control.tsv and readings.md; --check exits 1 if any
  is stale. --book 2 (A3V3-ECK2, 4 Oct 2026) reads every entry with ciphers/eckert-1864/key-no2.md (Cipher No. 2,
mssEC 47) instead of key.md, counts an entry fully keyed when its book is '2', and writes the same four outputs with a
_b2 suffix (entries_b2.tsv, matches_b2.tsv, control_b2.tsv, readings_b2.md); OR_DIR then holds ser. I vols. 32-49.

RUN3-ECK62 (4 Oct 2026; rules pre-registered in PREREG-ECK62.md): --possessive reads "Kettle's" as [Longstreet]'s
(decode.py possessive=True); --guard DIR62 applies decode.CollisionGuard built from the 1862 OR volumes in DIR62
(IA warofrebellionco0007vari, warofrebellion09..12secrrich _djvu.txt; none can print a 1864-65 telegram) and writes the
tokens it left plain to guard{_b2}.tsv. The committed outputs are written with the flags NOTES.md names for that run;
--check must be given the same flags. --guard-test scores the guard against A3V3-ECKC's known answer (align_tokens.tsv:
COLLISION word tokens caught vs AGREE word tokens wrongly guarded). --assign assigns Cipher No. 1 or No. 2 to the '?'
entries by print agreement (PREREG-ECK62 section c) with a known-answer run on the marker-assigned entries and a
rotated-window control, writing assign.tsv and assign_summary.tsv.
RUN6-ECK62 (5 Oct 2026; PREREG-ECK62-FREE.md): --assign-free DIR62 assigns the book with no print of the entry: corpus
bigram support (DIR62, OR 1862 volumes) for each keyed meaning against its neighbours, both keys, markers deleted;
known answer on the marker-known entries; control = 20 shuffled-meaning keys. Writes assign_free{,_summary}.tsv.
RUN6-ECK62R (5 Oct 2026): --read-free DIR62 reads each `1f`/`2f` entry of assign_free.tsv with its assigned key (full
text, markers kept, --possessive and the DIR62 guard as the committed outputs). Grade cap S: the book is S, so every
keyed token of an H/C key row counts as S; I and M rows keep I and M. "words" = >= 3 keyed tokens and oov 0 (the
fully-keyed rule); otherwise "not" with the oov words listed. Writes readings_free.tsv and readings_free.md.

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
            lw = [sys.intern(x) for x in words(line)]  # interned: the 48-volume index otherwise nears 15 GB
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


def make_guard(argv):
    if "--guard" in argv or "--guard-test" in argv:
        d = argv[argv.index("--guard" if "--guard" in argv else "--guard-test") + 1]
        return d1.CollisionGuard([f.read_text(errors="ignore") for f in sorted(Path(d).glob("*.txt"))])
    return None


def decode_all(es, key, pos, g):
    """Decode every entry; sets reading, counts, guarded, text on each entry dict (in place)."""
    for e in es:
        text = re.sub(r"\s+", " ", " ".join(e["body"])).strip()
        gl = []
        reading, counts = d1.decode_entry(text, key, possessive=pos, guard=g, guarded=gl)
        e["text"], e["reading"], e["counts"], e["guarded"] = text, reading, counts, gl


def occ(text, i):
    """(lowercased core, occurrence number) of word i of text.split(' ')."""
    ws = [w.strip(" .,;:'\"()").lower() for w in text.split(" ")]
    return ws[i], sum(1 for w in ws[:i] if w == ws[i])


def guard_test(argv):
    """Known answer: A3V3-ECKC's align_tokens.tsv statuses for word-kind keyed tokens (COLLISION vs AGREE)."""
    pos, g = "--possessive" in argv, make_guard(argv)
    es = {e["id"]: e for e in entries(argv[0])}
    keys = {"1": d1.load_key(ROOT / "ciphers/eckert-1864/key.md"), "2": d1.load_key(ROOT / "ciphers/eckert-1864/key-no2.md")}
    rows = [l.split("\t") for l in (HERE / "align_tokens.tsv").read_text().splitlines()[1:]]
    gset = {}
    for bk in "12":
        ids = {r[0] for r in rows if r[1] == bk}
        sub = [es[i] for i in ids]
        decode_all(sub, keys[bk], pos, g)
        for e in sub:
            gset[e["id"]] = {occ(e["text"], i): rule for i, core, m, rule in e["guarded"]}
    seen = collections.Counter()
    tab = collections.Counter()
    out = ["id\tcode_word\tmeaning\tstatus\tguarded"]
    for r in rows:
        if r[4] != "target" or r[9] != "word":
            continue
        k = (r[0], r[6].lower())
        n = seen[k]
        seen[k] += 1
        # possessive cores were stripped by the aligner: try both spellings
        rule = gset[r[0]].get((r[6].lower(), n)) or gset[r[0]].get((r[6].lower() + "'s", n), "")
        tab[(r[10], bool(rule))] += 1
        if rule or r[10] == "COLLISION":
            out.append(f"{r[0]}\t{r[6]}\t{r[7]}\t{r[10]}\t{rule}")
    for st in sorted({s for s, _ in tab}):
        out.append(f"# {st}: guarded {tab[(st, True)]} of {tab[(st, True)] + tab[(st, False)]}")
    return out


def main(argv):
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
    if "--guard-test" in argv:
        out = guard_test(argv)
        (HERE / "guard_test.tsv").write_text("\n".join(out) + "\n")
        print("\n".join(l for l in out if l.startswith("#") or "COLLISION" in l or "\tB" in l or "\tJ" in l))
        return 0
    if "--assign" in argv:
        return assign(argv)
    if "--assign-free" in argv:
        return assign_free(argv)
    if "--read-free" in argv:
        return read_free(argv)
    data, ordir = argv[0], argv[1]
    bk = "2" if "--book" in argv and argv[argv.index("--book") + 1] == "2" else "1"
    other, sfx = ("1" if bk == "2" else "2"), ("_b2" if bk == "2" else "")
    kfile = ROOT / "ciphers" / "eckert-1864" / ("key-no2.md" if bk == "2" else "key.md")
    key, voc = d1.load_key(kfile), vocab()
    es = entries(data)
    decode_all(es, key, "--possessive" in argv, make_guard(argv))
    for e in es:
        text, reading, counts = e["text"], e["reading"], e["counts"]
        bare = re.sub(r"\[[^\]]*\]|\{[^}]*\}", " ", reading)
        e["oov"] = sum(1 for w in re.findall(r"[A-Za-z]+", bare) if w.lower() not in voc and len(w) > 1)
        e["keyed"] = sum(counts.values())
        e["book"] = book(text)
        e["full"] = e["book"] == bk and e["keyed"] >= 3 and e["oov"] == 0
        w = words(plain_of(reading))
        e["grams"] = {" ".join(w[i:i + 5]) for i in range(len(w) - 4)}
    full = [e for e in es if e["full"]]
    allg = set().union(*(e["grams"] for e in es))
    vols, pos = or_index(ordir, allg)
    nums = sorted({int(v.split(".")[0]) for v in vols})
    vr = f"{nums[0]}-{nums[-1]}"
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
    b1 = [e for e in es if e["id"] in allreal and e["book"] == bk]
    b2 = [e for e in es if e["id"] in allreal and e["book"] == other]
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
           f"book{bk}_matched_keyed_meanings_in_print\t{ag[0]}/{ag[1]} = {ag[0] / max(1, ag[1]):.3f}",
           f"book{bk}_control_other_entry_window\t{agc[0]}/{agc[1]} = {agc[0] / max(1, agc[1]):.3f}",
           f"book{other}_entries_read_with_{kfile.stem.replace('-', '_')}_md_in_print\t{ag2[0]}/{ag2[1]} = {ag2[0] / max(1, ag2[1]):.3f}",
           f"or_volumes\t{len(vols)}", f"min_5grams\t{MIN}"]
    rd = [f"# mssEC 18: fully keyed entries read through Cipher No. {bk} "
          f"({'A3V3-ECK2' if bk == '2' else 'A3V3-ECK18'}, 4 Oct 2026)", "",
          "Derived by ec18.py from the Decoding the Civil War volunteer transcription (not reconciled against the page "
          "image: every reading is conditional on that transcription, rule 2) and ciphers/eckert-1864/"
          f"{kfile.name} ({'mssEC 47' if bk == '2' else 'mssEC 41'}). "
          f"Brackets are {kfile.name} meanings with that row's grade; words outside brackets are as the volunteers wrote them. "
          "Not a novelty claim (rule 10).", ""]
    for e in full:
        m = real.get(e["id"])
        c = e["counts"]
        rd += [f"**{e['id']}** (Page {e['page']}, {fmt(e['date'])}; H {c['H']} C {c['C']} I {c['I']} M {c['M']}; "
               f"{'print: OR ser. I vol. ' + m[0] + ' p. ' + PAGE[m[0]][m[2]] + ' (OCR running head), ' + str(m[1]) + ' shared 5-grams' if m else 'no OR ser. I vols. ' + vr + ' match'})", "",
               e["reading"], ""]
    gd = ["id\tword_index\tcode_word\tmeaning\trule"] + [f"{e['id']}\t{i}\t{c}\t{m}\t{r}" for e in es
                                                              for i, c, m, r in e["guarded"]]
    if "--possessive" in argv or "--guard" in argv:
        ctl += [f"flags\tpossessive={'--possessive' in argv} guard={'--guard' in argv}",
                f"guarded_tokens\t{len(gd) - 1}"]
    outs = {f"entries{sfx}.tsv": "\n".join(ent) + "\n", f"matches{sfx}.tsv": "\n".join(mt) + "\n",
            f"control{sfx}.tsv": "\n".join(ctl) + "\n", f"readings{sfx}.md": "\n".join(rd)}
    if "--guard" in argv:
        outs[f"guard{sfx}.tsv"] = "\n".join(gd) + "\n"
    if "--write" in argv:
        for k, v in outs.items():
            (HERE / k).write_text(v)
    elif "--check" in argv:
        stale = [k for k, v in outs.items() if not (HERE / k).exists() or (HERE / k).read_text() != v]
        if stale:
            sys.stderr.write("stale: " + ", ".join(stale) + "\n")
            return 1
        print("current")
    print(outs[f"control{sfx}.tsv"])
    return 0


def assign(argv):
    """PREREG-ECK62 section (c): book for '?' entries by which key's meanings occur in the entry's own print window."""
    data, ordir = argv[0], argv[1]
    pos, g = "--possessive" in argv, make_guard(argv)
    keys = {"1": d1.load_key(ROOT / "ciphers/eckert-1864/key.md"), "2": d1.load_key(ROOT / "ciphers/eckert-1864/key-no2.md")}
    runs = {}
    for bk in "12":
        es = entries(data)
        decode_all(es, keys[bk], pos, g)
        for e in es:
            w = words(plain_of(e["reading"]))
            e["grams"] = {" ".join(w[i:i + 5]) for i in range(len(w) - 4)}
            e["book"] = book(e["text"])
        runs[bk] = {e["id"]: e for e in es}
    ids = list(runs["1"])
    allg = set().union(*(e["grams"] for r in runs.values() for e in r.values()))
    vols, pos_ = or_index(ordir, allg)
    dates = {i: runs["1"][i]["date"] for i in ids}
    m1 = match(list(runs["1"].values()), vols, pos_, dates)
    m2 = match(list(runs["2"].values()), vols, pos_, dates)
    mt = {i: m1.get(i) or m2.get(i) for i in ids if m1.get(i) or m2.get(i)}

    def score(i, win_id):
        v, n, j = mt[win_id]
        win = set(vols[v][max(0, j - 150):j + 450])
        return tuple(sum(bool(ws & win) for ws in meaning_words(runs[bk][i]["reading"])) for bk in "12")

    def decide(s):
        return "1" if s[0] - s[1] >= 2 else "2" if s[1] - s[0] >= 2 else "?"
    known = [i for i in ids if i in mt and runs["1"][i]["book"] in "12"]
    unk = [i for i in ids if i in mt and runs["1"][i]["book"] == "?"]
    kres = [(i, runs["1"][i]["book"], decide(score(i, i))) for i in known]
    kdec = [x for x in kres if x[2] != "?"]
    kok = sum(1 for x in kdec if x[1] == x[2])
    kctl = [decide(score(i, w)) for i, w in zip(known, known[1:] + known[:1])]
    ures = [(i, score(i, i)) for i in unk]
    uctl = [decide(score(i, w)) for i, w in zip(unk, unk[1:] + unk[:1])]
    acc = kok / max(1, len(kdec))
    ud0 = sum(decide(s) != "?" for _, s in ures)
    uc0 = sum(x != "?" for x in uctl)
    # PREREG-ECK62 (c): not used when the rotated-window control decides nearly as often as the real windows;
    # "near" fixed at 09:46 UTC 4 Oct 2026, after the first run (41 vs 38): control decided > half the real count
    ctl_ok = uc0 <= 0.5 * ud0
    use = acc >= 0.85 and len(kdec) >= 20 and ctl_ok
    out = ["id\tdate\tor_volume\tscore_key1\tscore_key2\tassigned"]
    for i, s in ures:
        d = runs["1"][i]["date"]
        a = decide(s)
        out.append(f"{i}\t{d[0]}-{d[1]:02d}-{d[2]:02d}\t{mt[i][0]}\t{s[0]}\t{s[1]}\t{(a + 'a') if use and a != '?' else '?'}")
    ud = [decide(s) for _, s in ures]
    summ = ["statistic\tvalue", f"flags\tpossessive={pos} guard={g is not None}",
            f"unassigned_entries\t{sum(1 for i in ids if runs['1'][i]['book'] == '?')}",
            f"unassigned_print_matched\t{len(unk)}",
            f"known_answer_print_matched\t{len(known)}",
            f"known_answer_decided\t{len(kdec)}", f"known_answer_right\t{kok}/{len(kdec)} = {acc:.3f}",
            f"known_answer_decided_rotated_window\t{sum(x != '?' for x in kctl)}/{len(known)}",
            f"known_answer_right_rotated_window\t{sum(1 for (i, b, _), c in zip(kres, kctl) if c == b)}",
            f"gate_acc>=0.85_and_decided>=20\t{'PASS' if acc >= 0.85 and len(kdec) >= 20 else 'FAIL'}",
            f"unassigned_decided\t{sum(x != '?' for x in ud)}/{len(unk)} (1: {ud.count('1')}, 2: {ud.count('2')})",
            f"unassigned_decided_rotated_window\t{sum(x != '?' for x in uctl)}/{len(unk)}",
            f"gate_control_decided<=half_real\t{'PASS' if ctl_ok else 'FAIL'}",
            f"assignment_used\t{'yes' if use else 'no'}"]
    outs = {"assign.tsv": "\n".join(out) + "\n", "assign_summary.tsv": "\n".join(summ) + "\n"}
    if "--write" in argv:
        for k, v in outs.items():
            (HERE / k).write_text(v)
    elif "--check" in argv:
        stale = [k for k, v in outs.items() if not (HERE / k).exists() or (HERE / k).read_text() != v]
        if stale:
            sys.stderr.write("stale: " + ", ".join(stale) + "\n")
            return 1
        print("current")
    print(outs["assign_summary.tsv"])
    return 0


MARK = N1 | N2
UNIT = re.compile(r"\[[^\]]*\]|\{[^}]*\}|[^\s\[\]{}]+")


def bigrams(d):
    """Bigram counts over lowercased [a-z]+ words of every DIR62 file."""
    c = collections.Counter()
    for f in sorted(Path(d).glob("*.txt")):
        w = re.findall(r"[a-z]+", f.read_text(errors="ignore").lower())
        c.update(zip(w, w[1:]))
    return c


def support(reading, bg):
    """Keyed word-kind meanings in a reading with corpus bigram support (>= 2) on the left or right (PREREG-ECK62-FREE)."""
    units = []  # (kind, words): kind m = scored meaning, p = plain/other, b = boundary
    for u in UNIT.findall(reading):
        if u.startswith("{"):
            units.append(("b", []))
        elif u.startswith("["):
            mw = meaning_words(u)
            ws = re.findall(r"[a-z]+", re.sub(r"\(.*?\)", " ", u[1:-1].lower()))
            units.append(("m" if mw and ws else "p", ws))
        else:
            units.append(("p", re.findall(r"[a-z]+", u.lower())))
    n = 0
    for k, (kind, ws) in enumerate(units):
        if kind != "m":
            continue
        left = units[k - 1][1][-1:] if k and units[k - 1][0] != "b" else []
        right = units[k + 1][1][:1] if k + 1 < len(units) and units[k + 1][0] != "b" else []
        n += bool((left and bg[(left[0], ws[0])] >= 2) or (right and bg[(ws[-1], right[0])] >= 2))
    return n


def shuffled(key, seed):
    rng = random.Random(seed)
    ks = [k for k, v in key.items() if v[2] == "word"]
    ms = [key[k][0] for k in ks]
    rng.shuffle(ms)
    out = dict(key)
    for k, m in zip(ks, ms):
        out[k] = (m,) + tuple(key[k][1:])
    return out


def assign_free(argv):
    """PREREG-ECK62-FREE: print-free book assignment with a shuffled-key control."""
    data, d62 = argv[0], argv[argv.index("--assign-free") + 1]
    g = d1.CollisionGuard([f.read_text(errors="ignore") for f in sorted(Path(d62).glob("*.txt"))])
    bg = bigrams(d62)
    keys = {"1": d1.load_key(ROOT / "ciphers/eckert-1864/key.md"), "2": d1.load_key(ROOT / "ciphers/eckert-1864/key-no2.md")}
    es = entries(data)
    for e in es:
        e["book"] = book(" ".join(e["body"]))
        e["body"] = [" ".join(w for w in l.split(" ") if w.strip(" .,;:'\"()").lower() not in MARK) for l in e["body"]]

    def scores(ks):
        out = {}
        for bk in "12":
            decode_all(es, ks[bk], True, g)
            for e in es:
                out.setdefault(e["id"], []).append(support(e["reading"], bg))
        return out

    def decide(s):
        return "1" if s[0] - s[1] >= 2 else "2" if s[1] - s[0] >= 2 else "?"

    def known_acc(sc):
        dec = [(e["book"], decide(sc[e["id"]])) for e in es if e["book"] in "12"]
        dd = [x for x in dec if x[1] != "?"]
        return sum(a == b for a, b in dd) / max(1, len(dd)), len(dd), len(dec)
    real = scores(keys)
    acc, ndec, nk = known_acc(real)
    ctl = [known_acc(scores({b: shuffled(keys[b], 1000 * int(b) + s) for b in "12"})) for s in range(20)]
    cacc = [c[0] for c in ctl]
    cmean = sum(cacc) / len(cacc)
    gate = acc >= 0.85 and ndec >= 20 and acc > max(cacc) and acc - cmean >= 0.15
    unk = [e for e in es if e["book"] == "?"]
    ud = [decide(real[e["id"]]) for e in unk]
    out = ["id\tdate\tscore_key1\tscore_key2\tdecision\tassigned"]
    for e, a in zip(unk, ud):
        y, m, dd = e["date"]
        s = real[e["id"]]
        out.append(f"{e['id']}\t{y}-{m:02d}-{dd:02d}\t{s[0]}\t{s[1]}\t{a}\t{(a + 'f') if gate and a != '?' else '?'}")
    summ = ["statistic\tvalue", "flags\tpossessive=True guard=True markers_deleted=True",
            f"known_answer_entries\t{nk}", f"known_answer_decided\t{ndec}", f"known_answer_accuracy\t{acc:.3f}",
            f"shuffled_key_accuracy_20\t{' '.join(f'{x:.3f}' for x in cacc)}",
            f"shuffled_key_decided_20\t{' '.join(str(c[1]) for c in ctl)}",
            f"shuffled_key_accuracy_mean_max\t{cmean:.3f} {max(cacc):.3f}",
            f"unassigned_entries\t{len(unk)}",
            f"unassigned_decided\t{sum(x != '?' for x in ud)} (1: {ud.count('1')}, 2: {ud.count('2')})",
            f"gate\t{'PASS' if gate else 'FAIL'}", f"assignment_used\t{'yes' if gate else 'no'}"]
    outs = {"assign_free.tsv": "\n".join(out) + "\n", "assign_free_summary.tsv": "\n".join(summ) + "\n"}
    if "--write" in argv:
        for k, v in outs.items():
            (HERE / k).write_text(v)
    elif "--check" in argv:
        stale = [k for k, v in outs.items() if not (HERE / k).exists() or (HERE / k).read_text() != v]
        if stale:
            sys.stderr.write("stale: " + ", ".join(stale) + "\n")
            return 1
        print("current")
    print(outs["assign_free_summary.tsv"])
    return 0


def read_free(argv):
    """RUN6-ECK62R: read the print-free-assigned entries with the assigned key, tokens capped at grade S."""
    data, d62 = argv[0], argv[argv.index("--read-free") + 1]
    g = d1.CollisionGuard([f.read_text(errors="ignore") for f in sorted(Path(d62).glob("*.txt"))])
    keys = {"1": d1.load_key(ROOT / "ciphers/eckert-1864/key.md"), "2": d1.load_key(ROOT / "ciphers/eckert-1864/key-no2.md")}
    asg = {}
    for l in (HERE / "assign_free.tsv").read_text().splitlines()[1:]:
        f = l.split("\t")
        if f[5] in ("1f", "2f"):
            asg[f[0]] = f[5][0]
    voc = vocab()
    es = [e for e in entries(data) if e["id"] in asg]
    tsv = ["id\tpage\tdate\tassigned\tkeyed\tS\tI\tM\toov\tclass\toov_words"]
    md = ["# mssEC 18: print-free-assigned entries read with the assigned book (RUN6-ECK62R, 5 Oct 2026)", "",
          "Derived by `ec18.py DATA --read-free DIR62` from the Decoding the Civil War volunteer transcription (not "
          "reconciled against the page image, rule 2) and ciphers/eckert-1864/key.md (book 1f) or key-no2.md (book 2f), "
          "the book assigned print-free at grade S (RUN6-ECK62, PREREG-ECK62-FREE). Every keyed token is at most S "
          "(H/C key rows counted as S because the book is S). class 'words' = >= 3 keyed tokens and no out-of-vocabulary "
          "word outside brackets; 'not' otherwise. Known-answer precision of the assignment: '1' 0.956, '2' 0.821. "
          "Not a novelty claim (rule 10).", ""]
    tot = collections.Counter()
    for e in es:
        bk = asg[e["id"]]
        decode_all([e], keys[bk], True, g)
        c = e["counts"]
        bare = re.sub(r"\[[^\]]*\]|\{[^}]*\}", " ", e["reading"])
        oovw = [w for w in re.findall(r"[A-Za-z]+", bare) if w.lower() not in voc and len(w) > 1]
        keyed = sum(c.values())
        sg, ig, mg = c["H"] + c["C"], c["I"], c["M"]
        cls = "words" if keyed >= 3 and not oovw else "not"
        tot.update({"S": sg, "I": ig, "M": mg, cls: 1, "book" + bk + cls: 1})
        y, m, dd = e["date"]
        dt = f"{y}-{m:02d}-{dd:02d}"
        tsv.append(f"{e['id']}\t{e['page']}\t{dt}\t{bk}f\t{keyed}\t{sg}\t{ig}\t{mg}\t{len(oovw)}\t{cls}\t{' '.join(oovw)}")
        md += [f"**{e['id']}** (Page {e['page']}, {dt}; book {bk}f; S {sg} I {ig} M {mg}; oov {len(oovw)}; {cls})", "",
               e["reading"], ""]
    summ = (f"entries {len(es)}; words {tot['words']} (1f {tot['book1words']}, 2f {tot['book2words']}); "
            f"not {tot['not']} (1f {tot['book1not']}, 2f {tot['book2not']}); tokens S {tot['S']} I {tot['I']} M {tot['M']}")
    md.insert(4, "Summary: " + summ + ".\n")
    outs = {"readings_free.tsv": "\n".join(tsv) + "\n", "readings_free.md": "\n".join(md)}
    if "--write" in argv:
        for k, v in outs.items():
            (HERE / k).write_text(v)
    elif "--check" in argv:
        stale = [k for k, v in outs.items() if not (HERE / k).exists() or (HERE / k).read_text() != v]
        if stale:
            sys.stderr.write("stale: " + ", ".join(stale) + "\n")
            return 1
        print("current")
    print(summ)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

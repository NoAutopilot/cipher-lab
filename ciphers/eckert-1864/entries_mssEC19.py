#!/usr/bin/env python3
"""LS-PRE: segment mssEC 19 volunteer text into entries, count key vocabularies, check the Official Records.

  entries_mssEC19.py --or-dir SCRATCH/or --cache SCRATCH/or_hits.json [--rerun] [--min-cov N]
Reads sources/mssEC19/p<pointer>.json (tools/huntington_transc.py), key.md, key-no2.md, key-no9.md,
ciphertext*.txt and the reading tables (calibration) and writes entries-mssEC19.tsv. The OR check streams
IA _djvu.txt files of OR ser. I/III volumes (fetched to scratch, not committed) and looks for rare 3-grams of the
entry's plain (non-code) tokens clustered in one 400-token window. A ranking, not a verdict (rule 10).
"""
import argparse, collections, glob, json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MONTH = r"(Ja\w*|Fe\w*|M[a-z]{1,4}|Ap\w*|Ju\w*|Au\w*|Se\w*|Oc\w*|No\w*|De\w*)"
DATE = re.compile(r"\b" + MONTH + r"[.,]?\s+(\d{1,2})\s*(?:st|nd|rd|th|d|\.|\")?,?\s*(?:186[45]|64|65)?", re.I)
HDR = re.compile(r"(Wash\w*|Washington|W\.?\s?D\.?\s?C\.?)", re.I)

def toks(s):
    s = re.sub(r"\s*=\s*", "", s)           # clerk's syllable splits
    s = s.replace("’", "'")
    return re.findall(r"[a-z]+", s.lower())

def load_pages(pages_dir="sources/mssEC19"):
    out = []
    for fn in glob.glob(os.path.join(HERE, pages_dir, "p*.json")):
        p = int(os.path.basename(fn)[1:-5]); j = json.load(open(fn))
        out.append((p, j.get("title"), j.get("transc") or ""))
    return sorted(out)

def vocab(fn, first_col_only=True):
    v = set()
    for line in open(os.path.join(HERE, fn), encoding="utf-8"):
        if line.startswith("|") and not re.match(r"\|\s*(code word|-)", line, re.I):
            col = line.split("|")[1]
            v.update(toks(col))
    return v

def is_header(line, prev_blank):
    l = line.strip()
    if len(l) < 8 or len(l) > 110: return False
    m = DATE.search(l)
    if not m: return False
    if HDR.search(l): return True
    # no place word: accept a short line that is mostly name + date and follows a blank
    return prev_blank and len(l.split()) <= 12 and m.start() > 3

def segment(pages, base=8892, titled=False):
    """base: pointer - base = page number (mssEC 19); titled=True takes the page number from a 'Page N' title (object 5952)."""
    entries = []
    for ptr, title, text in pages:
        page = ptr - base
        if titled:
            tm = re.match(r"Page (\d+)$", title or "")
            page = int(tm.group(1)) if tm else 0
        lines = text.split("\n")
        cur = {"pointer": ptr, "page": page, "header": "", "lines": []}
        idx = 0; prev_blank = True
        for ln in lines:
            if is_header(ln, prev_blank) and (cur["lines"] or cur["header"] or idx == 0):
                if cur["lines"] or cur["header"]:
                    entries.append(cur)
                idx += 1
                cur = {"pointer": ptr, "page": page, "header": ln.strip(), "lines": []}
            elif ln.strip():
                cur["lines"].append(ln.strip())
            prev_blank = not ln.strip()
        if cur["lines"] or cur["header"]: entries.append(cur)
    seen = {}
    for e in entries:   # 0-based position in the page's segment list (a run-on from the previous page is 0)
        n = seen.get(e["pointer"], 0); e["entry_on_page"] = n; seen[e["pointer"]] = n + 1
    return entries

K1, K2, K9 = None, None, None
# function words are never treated as code words even where a key table lists them
FW = set("the of to and in a i have my his but him with that is are was were be been by for from on at as it its this these those you your will shall can could would should not no all any some them they their there then than we our us he she her me an or if so do does did has had may must which who whom what when where how one two three also only very more most such into upon out up down over under between about after before".split())
def load_vocab():
    global K1, K2, K9
    K1, K2, K9 = vocab("key.md"), vocab("key-no2.md"), vocab("key-no9.md")
    return (K1 | K2 | K9) - FW

def plain_runs(tokens, codes, minlen=4):
    runs, cur = [], []
    for i, t in enumerate(tokens):
        if t in codes or len(t) < 2 and t not in ("a", "i"):
            if len(cur) >= minlen: runs.append(cur)
            cur = []
        else: cur.append((i, t))
    if len(cur) >= minlen: runs.append(cur)
    return runs

M2 = {"tulip", "pike", "yacht", "yawl", "yardstick", "yard", "crowd", "mastiff"}
M1 = {"unity", "zebra", "growl", "grapes", "webster", "walrus", "yoke"}
M9 = {"applause", "abortion"}
STOP_HDR = re.compile(r"\b(Wash\w*)\b")

def analyse(e, codes):
    body = " ".join(e["lines"]); t = toks(body)
    e["tokens"] = t; e["words"] = len(t)
    c = collections.Counter(t)
    e["k1"] = sum(1 for w in t if w in K1); e["k2"] = sum(1 for w in t if w in K2); e["k9"] = sum(1 for w in t if w in K9)
    e["m1"] = sum(c[w] for w in M1); e["m2"] = sum(c[w] for w in M2); e["m9"] = sum(c[w] for w in M9)
    hdr = e["header"]
    hm = re.search(r'\((?:No\.?\s*)?([129])\)|"([129])"|\b(?:No\.?)\s*([129])\b', hdr)
    e["hdr_mark"] = next((g for g in (hm.groups() if hm else ()) if g), "")
    codefrac = sum(1 for w in t if w in codes) / max(1, len(t))
    e["codefrac"] = round(codefrac, 2)
    g = "?"                                   # filled by classify() once the labelled entries are known
    e["cipher_guess"] = g
    # sender in clear: leading words of header before the place word
    m = STOP_HDR.search(hdr)
    e["addressee"] = re.sub(r'\s+', ' ', hdr[:m.start()]).strip() if m else ""
    return e

N = 3           # n-gram length over plain tokens
MAXFREQ = 40    # an n-gram seen more often than this in the OR corpus is not specific
WINDOW = 400    # tokens
MINCOV = 7      # distinct entry plain tokens covered by hits inside one window

def or_tokens(text):
    text = re.sub(r"-\s*\n\s*", "", text)
    pages = text.split("\f")
    toks_, leaf = [], []
    for i, pg in enumerate(pages):
        t = re.findall(r"[a-z]+", pg.lower())
        toks_.extend(t); leaf.extend([i] * len(t))
    return toks_, leaf

def orcheck(entries, codes, ordir, cache):
    # query n-grams per entry
    q = collections.defaultdict(list)           # ngram -> [(entry index, start token idx)]
    for ei, e in enumerate(entries):
        e["_runs"] = plain_runs(e["tokens"], codes, N)
        for run in e["_runs"]:
            for k in range(len(run) - N + 1):
                g = tuple(w for _, w in run[k:k + N])
                q[g].append((ei, run[k][0]))
    freq = collections.Counter(); hits = collections.defaultdict(list)   # ngram -> [(vol, pos, leaf)]
    for fn in sorted(glob.glob(os.path.join(ordir, "*.txt"))):
        vol = os.path.basename(fn)[:-4]
        t, leaf = or_tokens(open(fn, encoding="utf-8", errors="replace").read())
        for i in range(len(t) - N + 1):
            g = (t[i], t[i + 1], t[i + 2])
            if g in q:
                freq[g] += 1
                if freq[g] <= MAXFREQ: hits[g].append((vol, i, leaf[i]))
        print("scanned", vol, len(t), file=sys.stderr)
    res = {}
    for ei, e in enumerate(entries):
        per = collections.defaultdict(list)     # vol -> [(pos, leaf, set(entry token idx))]
        for run in e["_runs"]:
            for k in range(len(run) - N + 1):
                g = tuple(w for _, w in run[k:k + N])
                if freq[g] > MAXFREQ: continue
                cov = {run[k + j][0] for j in range(N)}
                for vol, pos, lf in hits.get(g, ()): per[vol].append((pos, lf, cov))
        best = None
        for vol, hs in per.items():
            hs.sort()
            for a in range(len(hs)):
                cov = set(); b = a
                while b < len(hs) and hs[b][0] - hs[a][0] <= WINDOW:
                    cov |= hs[b][2]; b += 1
                if best is None or len(cov) > best[0]: best = (len(cov), vol, hs[a][1])
        res[ei] = best
    json.dump({str(k): v for k, v in res.items()}, open(cache, "w"))
    return res

MON = {"ja": 1, "fe": 2, "ma": 3, "mc": 3, "mr": 3, "ap": 4, "ju": 6, "au": 8, "se": 9, "oc": 10, "no": 11, "de": 12}
def day_month(s):
    m = DATE.search(s)
    if not m: return None
    mo = m.group(1).lower()
    if mo.startswith("ju"): mo = "jul" if mo.startswith(("jul", "jy")) else "jun"
    k = 7 if mo == "jul" else 6 if mo == "jun" else MON.get(mo[:2])
    if mo.startswith("ma") and mo[:3] == "may": k = 5
    return (k, int(m.group(2)))

def known_blocks():
    """id -> (pointer, (month, day)) for every already-read entry."""
    out = {}
    for fn in ("ciphertext.txt", "ciphertext-no2.txt", "ciphertext-no9.txt"):
        for l in open(os.path.join(HERE, fn), encoding="utf-8"):
            m = re.match(r"### (\S+) \| [^|]*\| (\d+) \| (.*)", l)
            if m:
                d = re.match(r"(\d{1,2}) (\w+)", m.group(3))
                out[m.group(1)] = (int(m.group(2)), day_month(f"{d.group(2)} {d.group(1)}") if d else None)
    return out

def truth():
    """id -> 'OR' | 'none' | 'other' from the repo's own tables (search results, rule 10 applies)."""
    t = {}
    for l in open(os.path.join(HERE, "reading-no2.md"), encoding="utf-8"):
        c = [x.strip() for x in l.split("|")]
        if len(c) == 6 and re.fullmatch(r"N2-[A-Z]+", c[1]):
            pr = c[4] if c[2].startswith("p.") else c[3]
            if re.search(r"not located|not in ", pr) and not re.search(r"Papers of|Grant Papers", pr): t[c[1]] = "none"
            elif re.search(r"Papers of|Grant Papers", pr) and not re.match(r"OR ", pr) and not re.match(r"I/", pr): t[c[1]] = "other"
            elif re.search(r"I/\d+|OR ", pr): t[c[1]] = "OR"
    for l in open(os.path.join(HERE, "reading-no9.md"), encoding="utf-8"):
        c = [x.strip() for x in l.split("|")]
        if len(c) == 6 and re.fullmatch(r"O9-[A-Z]+", c[1]):
            if c[2].startswith("not located"): t[c[1]] = "none"
            elif re.match(r"I/\d+", c[2]): t[c[1]] = "OR"
    for l in open(os.path.join(HERE, "AUDIT.md"), encoding="utf-8"):
        c = [x.strip() for x in l.split("|")]
        if len(c) > 4 and re.fullmatch(r"E\d+", c[1]):
            if c[3].startswith("**yes**: OR"): t[c[1]] = "OR"
            elif c[3].startswith("not located"): t[c[1]] = "none"
            elif c[3].startswith("**yes**"): t[c[1]] = "other"
    return t

def priority(e):
    cipher = e["cipher_guess"] in ("1", "2", "9", "mixed", "unk")
    # sender is inside the cipher, so the proxy is the operator at an army commander's headquarters
    # (Beckwith at Grant's, Kimber with Canby): those entries are mostly Halleck/Stanton/Lincoln to the commander
    big = re.search(r"beckwith|kimber|canby|grant|halleck|lincoln|stanton|president", (e["header"] + " " + e["sender_clear"]).lower())
    if cipher and e["or_hit"] == "none" and not e["already_read"] and not big: return 1
    if cipher and e["or_hit"] == "none": return 2
    return 3

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--or-dir", required=True); ap.add_argument("--cache", required=True)
    ap.add_argument("--rerun", action="store_true"); ap.add_argument("--min-cov", type=int, default=MINCOV)
    ap.add_argument("--pages-dir", default="sources/mssEC19", help="page transcriptions (default mssEC 19); another ledger is segmented and classified "
                    "with the mssEC 19 entries as the training set, and the calibration against the audits is skipped (FM-PRE, object 5952)")
    ap.add_argument("--prefix", default="mssEC19", help="output is entries-<prefix>.tsv"); ap.add_argument("--page-base", type=int, default=8892)
    ap.add_argument("--titled-pages", action="store_true", help="page number from the 'Page N' title instead of pointer - page-base")
    a = ap.parse_args(argv)
    codes = load_vocab()
    other = a.pages_dir != "sources/mssEC19"
    entries = segment(load_pages(a.pages_dir), a.page_base, a.titled_pages)
    train = []
    if other:
        train = segment(load_pages())
        for e in train: analyse(e, codes)
    for e in entries:
        analyse(e, codes)
        last = e["lines"][-1] if e["lines"] else ""
        lt = toks(last)
        e["sender_clear"] = last if 0 < len(lt) <= 5 and sum(w in codes for w in lt) <= len(lt) // 2 else ""
    entries = [e for e in entries if e["words"] >= 3 or e["header"]]
    if a.rerun or not os.path.exists(a.cache): orcheck(entries, codes, a.or_dir, a.cache)
    res = json.load(open(a.cache))
    for ei, e in enumerate(entries):
        b = res.get(str(ei))
        e["or_cov"] = b[0] if b else 0
        e["or_hit"] = f"{b[1]}@leaf{b[2]}(cov{b[0]})" if b and b[0] >= a.min_cov else "none"
    kb, tr = known_blocks(), truth()
    for e in entries: e["already_read"] = ""
    for kid, (ptr, dm) in kb.items():
        for e in entries:
            if e["pointer"] == ptr and day_month(e["header"]) == dm and not e["already_read"]:
                e["already_read"] = kid; break
    if other:
        for e in train: e["already_read"] = ""
        for kid, (ptr, dm) in kb.items():
            for e in train:
                if e["pointer"] == ptr and day_month(e["header"]) == dm and not e["already_read"]:
                    e["already_read"] = kid; break
        classify(train + entries, codes, None)
        for e in entries: e["priority"] = priority(e)
        write_tsv(entries, a, "FM-PRE (8 Oct 2026): entries of %s, a ranking, not a verdict; no calibration against the audits (mssEC 19 entries train the book guess)" % a.pages_dir)
        return
    classify(entries, codes, None)
    # calibration
    rec_n = rec_h = fh_n = fh_h = 0; rows = []
    for e in entries:
        k = e["already_read"]
        if k in tr:
            hit = e["or_hit"] != "none"
            if tr[k] == "OR": rec_n += 1; rec_h += hit
            elif tr[k] == "none": fh_n += 1; fh_h += hit
            rows.append((k, tr[k], e["or_cov"], e["words"]))
        e["priority"] = priority(e)
    lab = [(k[0], e) for e in entries for k in [e["already_read"]] if k]
    want = {"E": "1", "N": "2", "O": "9"}
    acc_n = len(lab); acc_h = sum(1 for k, e in lab if e["cipher_guess"] == want[k]); acc_nb = sum(1 for k, e in lab if e["nb_guess"] == want[k])
    cal = (f"cipher_guess on {acc_n} already-read entries (file of origin E=1, N2=2, O9=9 as the label; leave-one-out Bayes on key-table tokens): {acc_h} right; "
           f"recall {rec_h}/{rec_n} = {rec_h/max(1,rec_n):.2f} of known OR-printed entries found; "
           f"false hits {fh_h}/{fh_n} of known not-located entries (min cover {a.min_cov} plain tokens, {N}-grams, window {WINDOW}, max freq {MAXFREQ})")
    print(cal, file=sys.stderr)
    for r in sorted(rows): print("cal", *r, file=sys.stderr)
    write_tsv(entries, a, None, cal)
    cnt = collections.Counter((e["priority"], e["cipher_guess"]) for e in entries)
    print(sorted(cnt.items()), file=sys.stderr)

def write_tsv(entries, a, note, cal=None):
    cols = ["pointer", "page", "entry_on_page", "header", "addressee", "sender_clear", "words", "k1", "k2", "k9",
            "cipher_guess", "or_hit", "or_cov", "already_read", "priority"]
    if note:
        with open(os.path.join(HERE, "fortmonroe", "entries-%s.tsv" % a.prefix), "w") as f:
            f.write("# %s\n# OR volumes: %s\n" % (note, " ".join(sorted(os.path.basename(x)[:-4] for x in glob.glob(os.path.join(a.or_dir, '*.txt'))))))
            f.write("\t".join(cols) + "\n")
            for e in entries: f.write("\t".join(str(e[c]).replace("\t", " ") for c in cols) + "\n")
        return
    with open(os.path.join(HERE, "entries-%s.tsv" % a.prefix), "w") as f:
        f.write(f"# LS-PRE (7 Oct 2026): entries of mssEC 19 from sources/mssEC19 volunteer text; OR check = distinct plain-token cover by rare 3-gram hits in one 400-token window of IA _djvu.txt; a ranking, not a verdict.\n")
        f.write(f"# calibration: {cal}\n")
        f.write("# OR volumes: " + " ".join(sorted(os.path.basename(x)[:-4] for x in glob.glob(os.path.join(a.or_dir, '*.txt')))) + "\n")
        f.write("\t".join(cols) + "\n")
        for e in entries:
            f.write("\t".join(str(e[c]).replace("\t", " ") for c in cols) + "\n")



def classify(entries, codes, labels, loo=None):
    """Naive Bayes over code-vocabulary tokens, trained on the already-read entries (E=1, N2=2, O9=9).
    'clear' = under 12% code tokens and no header mark; 'short' = under 6 words."""
    cls = {"E": "1", "N": "2", "O": "9"}
    train = [(cls[k[0]], e) for e in entries for k in [e["already_read"]] if k]
    cnt = {c: collections.Counter() for c in "129"}; ndoc = collections.Counter()
    for c, e in train:
        ndoc[c] += 1; cnt[c].update(w for w in set(e["tokens"]) if w in codes)
    V = len(codes) + 1
    def score(e, own=None):
        out = {}
        for c in "129":
            n = ndoc[c] - (1 if own and own == c else 0)
            lp = math.log((n + 1) / (sum(ndoc.values()) + 3))
            for w in set(e["tokens"]):
                if w in codes:
                    k = cnt[c][w] - (1 if own and own == c and w in set(e["tokens"]) else 0)
                    lp += math.log((k + 0.5) / (n + 1))
            out[c] = lp
        return out
    for e in entries:
        own = next((c for c, ee in train if ee is e), None)
        if e["words"] < 6: g = "short"
        elif e["codefrac"] < 0.12 and not e["hdr_mark"]: g = "clear"
        else:
            sc = score(e, own); g = max(sc, key=sc.get)
        e["cipher_guess"] = g
        e["nb_guess"] = (lambda sc: max(sc, key=sc.get))(score(e, own)) if e["words"] >= 6 else ""

if __name__ == "__main__":
    main()

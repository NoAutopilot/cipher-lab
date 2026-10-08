#!/usr/bin/env python3
"""PF4 (8 Oct 2026, LANE ST-LEDGER-4): three-part pre-filter over unread mssEC 19 entries. No decoding, no reading.

  prefilter_ls4.py --scratch DIR [--control] [--pool] [--offline] [--hunt-budget 250] [--ia-budget 250]

Reuses the segmenter and vocab of entries_mssEC19.py (no private copy). Per entry, three checks:
 (a) PRINT, widened: the LS-PRE rare-3-gram window cover (entries_mssEC19.orcheck) over OR ser. III vols 4-5 (IA cu31924079575373,
     cu31924079575381) and ORN ser. I vols 11-12 (officialrecordso0011unse, officialrecordso0012unse), `or_cov_widened` = max(LS-PRE
     or_cov, added-volume cover); plus one or two quoted phrases (4 consecutive plain words, rarest) through be-api fts (no identifier);
     hit identifiers recorded, never page numbers. print-likely = widened cover >= 7, or a phrase hit (<= 20 items) in a work whose title
     names the war records / a correspondent.
 (b) HUNTINGTON full text: dmQuery CISOSEARCHALL^w1 w2^all^and on p16003coll11 with the transcription returned in the result (one
     request gives hits and text). Per hit other than the row's own pointer: cover of the row's plain rare 3-grams (y >= 7, unsure 3-6),
     and the share of ALL the row's 3-grams found (copy >= 0.5, a cipher copy of the same text). Own transcription mostly clear (code
     fraction < 0.12) is recorded as own=clear.
 (c) SAME LEAF and +/-1 page (offline): same day and (same sender-name, same header time, or >= 3 shared rare plain tokens), or >= 5 shared rare
     plain tokens on any day.
Verdict: clean | print-likely | clear-sibling | dup (several may be joined with +). A ranking, not a verdict (CLAUDE.md rule 10).
Caches (small JSON, committed under sources/ia-fulltext/print-check/ls4/) make --offline re-runnable; OR djvu text stays in --scratch.
"""
import argparse, collections, glob, gzip, hashlib, json, math, os, re, sys, time, urllib.parse, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import entries_mssEC19 as m

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CACHE = os.path.join(ROOT, "sources", "ia-fulltext", "print-check", "ls4")
UA_B = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
NEWVOLS = {"cu31924079575373": "OR III/4", "cu31924079575381": "OR III/5",
           "officialrecordso0011unse": "ORN I/11", "officialrecordso0012unse": "ORN I/12"}
REL = re.compile(r"rebellion|official records|union and confederate|lincoln|grant|sherman|sheridan|stanton|halleck|butler|welles|"
                 r"civil war|telegra|messages and papers|correspondence|papers of", re.I)

# control: id -> (pointer, entry_on_page, volume, expectation from the audits)
CONTROL = {
    "N2-BP": (9714, 1, "mssEC18", "lowered N1: print OR III/4 pp.238-239"),
    "E70": (8985, 2, "mssEC19", "lowered: Huntington transcription clear sibling"),
    "E74": (9071, 2, "mssEC19", "lowered N1: Huntington transcription, mostly clear"),
    "E76": (9111, 1, "mssEC19", "lowered N1: body clear in Huntington transcription"),
    "E83": (9901, 0, "mssEC18", "lowered N2: OR I/43 pt2 p.695 + same-leaf sibling"),
    "E86": (9948, 3, "mssEC18", "lowered: Huntington / print"),
    "O9-BC": (10028, 1, "mssEC18", "lowered: press (Urbana Union 1865), outside checks a-c"),
    "E77": (9143, 1, "mssEC19", "lowered: print"),
    "O9-AL": (9015, 1, "mssEC19", "lowered: print/clear"),
    "E78": (9714, 2, "mssEC18", "held N3"),
    "O9-BB": (9717, 2, "mssEC18", "held N3"),
    "O9-BA": (9717, 1, "mssEC18", "held N3 (weak)"),
}
LOWERED = ["N2-BP", "E70", "E74", "E76", "E83", "E86", "O9-BC", "E77", "O9-AL"]
HELD = ["E78", "O9-BB", "O9-BA"]


class Net:
    def __init__(self, offline, hunt_budget, ia_budget):
        self.offline = offline; self.budget = {"hdl": hunt_budget, "be-api": ia_budget}
        self.n = collections.Counter(); self.last = collections.defaultdict(float)
        os.makedirs(CACHE, exist_ok=True)
        self.countfile = os.path.join(CACHE, "requests.json")
        self.prior = json.load(open(self.countfile)) if os.path.exists(self.countfile) else {}

    def _path(self, url):
        return os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest()[:16] + ".json.gz")

    def get(self, host, url, gap, parse=True):
        p = self._path(url)
        if os.path.exists(p):
            return json.load(gzip.open(p, "rt"))
        if self.offline: return None
        if self.n[host] + self.prior.get(host, 0) >= self.budget[host]:
            raise BudgetStop(host)
        for attempt in (0, 1, 2):
            dt = time.time() - self.last[host]
            if dt < gap: time.sleep(gap - dt)
            self.last[host] = time.time(); self.n[host] += 1
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA_B})
                with urllib.request.urlopen(req, timeout=60) as r:
                    d = json.loads(r.read().decode("utf-8", "replace"))
                json.dump(d, gzip.open(p, "wt"))
                return d
            except urllib.error.HTTPError as e:
                if e.code in (429, 403): raise SystemExit(f"HTTP {e.code} from {host}: stopping host")
                if attempt == 2: return {"_error": e.code}
                time.sleep(4)
            except (urllib.error.URLError, OSError, ValueError):
                if attempt == 2: return {"_error": "net"}
                time.sleep(4)

    def save_counts(self):
        tot = dict(self.prior)
        for k, v in self.n.items(): tot[k] = tot.get(k, 0) + v
        json.dump(tot, open(self.countfile, "w"))


class BudgetStop(Exception):
    pass


# ---------------------------------------------------------------- entries
def pages_mssEC19():
    return m.load_pages()


def pages_mssEC18(scratch):
    """Local snapshots of the sent ledger mssEC 18: items-API files (key text) and huntington_transc.py files (key transc)."""
    out = []
    for fn in glob.glob(os.path.join(HERE, "sources/mssEC18/p*.json")):
        j = json.load(open(fn)); out.append((int(os.path.basename(fn)[1:-5]), "", j.get("text") or j.get("transc") or ""))
    return sorted(out)


def build(scratch):
    codes = m.load_vocab()
    res = {}
    for vol, pages in (("mssEC19", pages_mssEC19()), ("mssEC18", pages_mssEC18(scratch))):
        ents = m.segment(pages)
        for e in ents:
            m.analyse(e, codes)
            e["vol"] = vol
        res[vol] = [e for e in ents if e["words"] >= 3 or e["header"]]
    return codes, res


def header_time(h):
    t = re.search(r"(\d{1,2})[.: ]?(\d{2})?\s*(am|pm|a\.?\s?m|p\.?\s?m|m)\b", h, re.I)
    return (t.group(1) + (t.group(2) or ""), t.group(3)[0].lower()) if t else None


def sender_key(e):
    h = re.split(r"\b(Wash\w*)\b", e["header"])[0]
    h = re.sub(r"\(.*?\)|[^a-z ]", " ", h.lower()); w = [x for x in h.split() if len(x) > 2]
    return " ".join(w[:3])


# ---------------------------------------------------------------- corpus stats from the added volumes
def scan_new(entries, codes, scratch, cache):
    """3-gram frequency (entry plain 3-grams) and widened OR cover over the four added volumes. Returns (freq, cov, wordcount)."""
    if os.path.exists(cache):
        j = json.load(open(cache))
        return {tuple(k.split(" ")): v for k, v in j["freq"].items()}, {int(k): v for k, v in j["cov"].items()}, collections.Counter(j["wc"])
    q = collections.defaultdict(list)
    for ei, e in enumerate(entries):
        e["_runs"] = m.plain_runs(e["tokens"], codes, m.N)
        for run in e["_runs"]:
            for k in range(len(run) - m.N + 1):
                q[tuple(w for _, w in run[k:k + m.N])].append(ei)
    want = {w for e in entries for w in e["tokens"]}
    freq = collections.Counter(); hits = collections.defaultdict(list); wc = collections.Counter()
    for vol in NEWVOLS:
        t, leaf = m.or_tokens(open(os.path.join(scratch, "or", vol + ".txt"), encoding="utf-8", errors="replace").read())
        for w in t:
            if w in want: wc[w] += 1
        for i in range(len(t) - m.N + 1):
            g = (t[i], t[i + 1], t[i + 2])
            if g in q:
                freq[g] += 1
                if freq[g] <= m.MAXFREQ: hits[g].append((vol, i, leaf[i]))
    cov = {}
    for ei, e in enumerate(entries):
        per = collections.defaultdict(list)
        for run in e["_runs"]:
            for k in range(len(run) - m.N + 1):
                g = tuple(w for _, w in run[k:k + m.N])
                if freq[g] > m.MAXFREQ: continue
                c = {run[k + j][0] for j in range(m.N)}
                for vol, pos, lf in hits.get(g, ()): per[vol].append((pos, lf, c))
        best = [0, "", 0]
        for vol, hs in per.items():
            hs.sort()
            for a in range(len(hs)):
                cv = set(); b = a
                while b < len(hs) and hs[b][0] - hs[a][0] <= m.WINDOW: cv |= hs[b][2]; b += 1
                if len(cv) > best[0]: best = [len(cv), vol, hs[a][1]]
        cov[ei] = best
    json.dump({"freq": {" ".join(k): v for k, v in freq.items()}, "cov": cov, "wc": dict(wc)}, open(cache, "w"))
    return freq, cov, wc


# ---------------------------------------------------------------- check a: phrases
def phrases(e, wc, codes, n=4, k=2):
    """Rarest runs of n consecutive plain words (each seen >= 2 times in the added volumes, so not a transcription slip)."""
    cand = []
    for run in m.plain_runs(e["tokens"], codes, n):
        ws = [w for _, w in run]
        for i in range(len(ws) - n + 1):
            g = ws[i:i + n]
            if any(wc.get(w, 0) < 2 or len(w) < 2 for w in g): continue
            cand.append((sum(math.log(wc[w] + 1) for w in g), i, g))
    cand.sort(key=lambda x: (x[0], x[1]))
    out = []
    for sc, i, g in cand:
        if all(set(g) != set(o) and not (set(g) & set(o) and len(set(g) & set(o)) > 1) for o in out):
            out.append(g)
        if len(out) >= k: break
    return [" ".join(g) for g in out]


def fts(net, phrase):
    url = "https://be-api.us.archive.org/fts/v1/search?q=" + urllib.parse.quote(f'"{phrase}"')
    d = net.get("be-api", url, 1.6)
    if d is None or "_error" in d: return None
    h = d.get("hits", {}); tot = h.get("total", len(h.get("hits", [])))
    tot = tot.get("value", 0) if isinstance(tot, dict) else tot
    ids = []
    for x in h.get("hits", [])[:8]:
        f = x.get("fields", {})
        ids.append((f.get("identifier", ["?"])[0], (f.get("meta_title") or ["?"])[0][:60]))
    return tot, ids


# ---------------------------------------------------------------- check b: Huntington
def hunt_terms(e, wc, codes, k=2):
    """Rarest real plain words (seen >= 3 times in the added volumes, 4+ letters) of the entry, not the header's place word."""
    seen = set(); c = []
    for w in e["tokens"]:
        if w in codes or w in m.FW or len(w) < 4 or w in seen or wc.get(w, 0) < 3 or w.startswith("wash"): continue
        seen.add(w); c.append((wc[w], -len(w), w))
    c.sort()
    return [w for _, _, w in c[:k]]


def hunt(net, terms):
    url = (HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(" ".join(terms)) + "%5Eall%5Eand/title!transc/nosort/20/1/0/0/1/0/json")
    d = net.get("hdl", url, 1.7)
    if d is None or "_error" in d or "records" not in d: return None
    return d["pager"].get("total"), d["records"]


def parent_title(net, parent):
    url = HB + f"dmGetItemInfo/p16003coll11/{parent}/json"
    d = net.get("hdl", url, 1.7)
    if not d or "_error" in d: return "?"
    return f"{d.get('title') or '?'} / {d.get('callid') or ''}".strip(" /")


def grams(tokens, codes, freq, plain_only):
    out = {}
    if plain_only:
        for run in m.plain_runs(tokens, codes, 3):
            for k in range(len(run) - 2):
                g = tuple(w for _, w in run[k:k + 3])
                if freq.get(g, 0) <= m.MAXFREQ:
                    for j in range(3): out.setdefault(g, set()).add(run[k + j][0])
    else:
        for i in range(len(tokens) - 2): out.setdefault(tuple(tokens[i:i + 3]), set()).add(i)
    return out


def hit_scores(e, text, codes, freq):
    ht = m.toks(text)
    hg = {tuple(ht[i:i + 3]) for i in range(len(ht) - 2)}
    pg = grams(e["tokens"], codes, freq, True)
    cov = set()
    for g, idx in pg.items():
        if g in hg: cov |= idx
    ag = grams(e["tokens"], codes, freq, False)
    full = sum(1 for g in ag if g in hg) / max(1, len(ag))
    return len(cov), full


# ---------------------------------------------------------------- check c: siblings
def rare_plain(e, codes, wc, cut=400):
    return {w for w in e["tokens"] if w not in codes and w not in m.FW and len(w) >= 4 and 1 <= wc.get(w, 0) <= cut}


def leaf_sibs(e, allents, codes, wc):
    mine = rare_plain(e, codes, wc); dm = m.day_month(e["header"]); tm = header_time(e["header"]); sk = sender_key(e)
    out = []
    for o in allents:
        if o["vol"] != e["vol"] or o is e or abs(o["pointer"] - e["pointer"]) > 1: continue
        sh = mine & rare_plain(o, codes, wc)
        same_day = dm is not None and m.day_month(o["header"]) == dm
        why = []
        if same_day and sk and sender_key(o) == sk: why.append("sender")
        if same_day and tm and header_time(o["header"]) == tm: why.append("time")
        if same_day and len(sh) >= 3: why.append(f"{len(sh)}tok")
        if not same_day and len(sh) >= 5: why.append(f"{len(sh)}tok-nodate")
        if why:
            st = []
            if o.get("already_read"): st.append("read")
            if o["codefrac"] < 0.12: st.append("clear")
            out.append(f"dup:{o['pointer']}/{o['entry_on_page']}[{','.join(why)}{';' + ','.join(st) if st else ''}]")
    return out


# ---------------------------------------------------------------- driver
def check_entry(e, ei, ctx, net, nphr, do_net=True):
    codes, wc, freq, cov, allents = ctx
    r = {"words": e["words"], "or_cov_widened": max(e.get("or_cov", 0), cov[ei][0]), "new_cov": cov[ei][0], "new_vol": NEWVOLS.get(cov[ei][1], "")}
    r["own"] = "clear" if e["codefrac"] < 0.12 else "cipher"
    # a: phrases
    ph = phrases(e, wc, codes, 4, nphr); r["phrases"] = ph; ph_hits = []
    for p in ph:
        try: x = fts(net, p)
        except BudgetStop: x = None
        if x is None: ph_hits.append(f"{p}=?"); continue
        tot, ids = x
        rel = [i for i, t in ids if REL.search(t) or REL.search(i)]
        ph_hits.append(f"{p}={tot}" + (":" + ",".join(f"{i}" for i in rel[:3]) if rel and tot <= 20 else ""))
        if rel and tot <= 20: r.setdefault("print_phr", []).extend(rel[:3])
    r["print_hits"] = "; ".join(ph_hits) if ph_hits else "no-4-run"
    # b: Huntington
    terms = hunt_terms(e, wc, codes, 2); r["terms"] = terms; hh = []; best = "none"
    own_ptr = e["pointer"]
    if terms:
        tried = [terms]
        for attempt in range(2):
            try: x = hunt(net, tried[-1])
            except BudgetStop: x = None
            if x is None: hh.append("query=?"); break
            tot, recs = x; strong = False
            for rec in recs:
                if int(rec["pointer"]) == own_ptr: continue
                c, full = hit_scores(e, rec.get("transc") or "", codes, freq)
                lab = "y" if c >= 7 else "u" if c >= 3 else "n"
                if full >= 0.5: lab = "copy" if lab != "y" else "y+copy"
                if lab != "n":
                    hh.append(f"{rec['pointer']}@{rec['parentobject']}:{lab}:cov{c}:full{full:.2f}")
                    best = max(best, lab, key=lambda s: ["none", "n", "u", "copy", "y", "y+copy"].index(s) if s in ["none", "n", "u", "copy", "y", "y+copy"] else 0)
                if lab in ("y", "y+copy", "copy"): strong = True
            if strong or tot is None or int(tot) <= 20 or len(terms) < 4: break
            more = hunt_terms(e, wc, codes, 4)[2:4]          # one more pair if the first pair was too common to rank the sibling in
            if len(more) < 2: break
            tried.append(more)
    r["hunt_hits"] = " ".join(hh) if hh else ("none" if terms else "no-terms")
    r["hunt_clear"] = best
    # c
    r["leaf_sibs"] = " ".join(leaf_sibs(e, allents, codes, wc)) or "none"
    v = []
    if r["or_cov_widened"] >= m.MINCOV or r.get("print_phr"): v.append("print-likely")
    if best in ("y", "y+copy", "copy") or r["own"] == "clear": v.append("clear-sibling")
    if r["leaf_sibs"] != "none": v.append("dup")
    r["verdict"] = "+".join(v) if v else "clean"
    return r


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scratch", required=True); ap.add_argument("--offline", action="store_true")
    ap.add_argument("--control", action="store_true"); ap.add_argument("--pool", action="store_true")
    ap.add_argument("--hunt-budget", type=int, default=250); ap.add_argument("--ia-budget", type=int, default=250)
    ap.add_argument("--phrases", type=int, default=2)
    ap.add_argument("--out", default=os.path.join(HERE, "prefilter-ls4.tsv"))
    a = ap.parse_args(argv)
    codes, by = build(a.scratch)
    tsv = {}
    for l in open(os.path.join(HERE, "entries-mssEC19.tsv"), encoding="utf-8"):
        if l.startswith("#") or l.startswith("pointer\t"): continue
        c = l.rstrip("\n").split("\t"); tsv[(int(c[0]), int(c[2]))] = c
    e19 = by["mssEC19"]
    for e in e19:
        c = tsv.get((e["pointer"], e["entry_on_page"]))
        if c is None: continue
        e["cipher_guess"], e["or_cov"], e["already_read"], e["priority"] = c[10], int(c[12]), c[13], int(c[14])
    for e in by["mssEC18"]: e["or_cov"] = 0; e["already_read"] = ""
    allents = e19 + by["mssEC18"]
    ents = allents
    cache = os.path.join(CACHE, "newvol_scan.json"); os.makedirs(CACHE, exist_ok=True)
    freq, cov, wc = scan_new(ents, codes, a.scratch, cache)
    ctx = (codes, wc, freq, cov, allents)
    net = Net(a.offline, a.hunt_budget, a.ia_budget)
    rows = []
    idx = {id(e): i for i, e in enumerate(ents)}
    def find(ptr, n, vol):
        return next(e for e in ents if e["vol"] == vol and e["pointer"] == ptr and e["entry_on_page"] == n)
    if a.control:
        for cid, (ptr, n, vol, note) in CONTROL.items():
            e = find(ptr, n, vol)
            r = check_entry(e, idx[id(e)], ctx, net, a.phrases)
            r.update(id=cid, group="control-lowered" if cid in LOWERED else "control-held", pointer=ptr, page=ptr - 8892 if vol == "mssEC19" else ptr - 9666,
                     entry=n, cipher_guess=e.get("cipher_guess", "?"), priority="", note=note)
            rows.append(r); print(cid, r["verdict"], r["or_cov_widened"], r["print_hits"][:80], "|", r["hunt_clear"], r["own"], "|", r["leaf_sibs"][:80], file=sys.stderr)
            net.save_counts()
    if a.pool:
        pool = []
        for e in e19:
            if e.get("already_read") or e["pointer"] >= 9149 or e.get("priority") is None: continue
            g, p = e["cipher_guess"], e["priority"]
            grp = 1 if g == "9" else 2 if (g == "2" and p in (1, 2)) else 3 if (g == "1" and p in (1, 2)) else 0
            if grp: pool.append((grp, e["or_cov"], e))
        pool.sort(key=lambda t: (t[0], t[1], t[2]["pointer"], t[2]["entry_on_page"]))
        print("pool", collections.Counter(g for g, _, _ in pool), len(pool), file=sys.stderr); unchecked = []
        for grp, _, e in pool:
            if net.budget["be-api"] - net.n["be-api"] - net.prior.get("be-api", 0) < 8 or net.budget["hdl"] - net.n["hdl"] - net.prior.get("hdl", 0) < 6:
                unchecked.append(f"{e['pointer']}:{e['entry_on_page']}"); continue
            try:
                r = check_entry(e, idx[id(e)], ctx, net, a.phrases if grp < 3 else 1)
            except BudgetStop as b:
                print("budget stop", b, file=sys.stderr); unchecked.append(f"{e['pointer']}:{e['entry_on_page']}"); continue
            r.update(id=f"{e['pointer']}:{e['entry_on_page']}", group=f"pool-{grp}", pointer=e["pointer"], page=e["page"], entry=e["entry_on_page"],
                     cipher_guess=e["cipher_guess"], priority=e["priority"], note=e["header"][:60])
            rows.append(r)
            if len(rows) % 10 == 0: net.save_counts(); print(len(rows), dict(net.n), file=sys.stderr)
    net.save_counts()
    if a.pool:
        print("unchecked", len(unchecked), " ".join(unchecked), file=sys.stderr)
        parents = sorted({int(x.split("@")[1].split(":")[0]) for r in rows for x in r.get("hunt_hits", "").split() if "@" in x})
        with open(os.path.join(HERE, "prefilter-ls4-parents.tsv"), "w") as f:
            for pid in parents:
                try: f.write(f"{pid}\t{parent_title(net, pid)}\n")
                except BudgetStop: break
        net.save_counts()
    cols = ["group", "id", "pointer", "page", "entry", "cipher_guess", "priority", "words", "or_cov_widened", "new_vol", "print_hits",
            "hunt_terms", "hunt_hits", "hunt_clear", "own", "leaf_sibs", "verdict", "note"]
    with open(a.out, "w") as f:
        f.write("# PF4 (8 Oct 2026, LANE ST-LEDGER-4): pre-filter, a ranking not a verdict (rule 10). prefilter_ls4.py; hit lists: pointer@parentobject:y|u|copy:cov:full.\n")
        f.write("\t".join(cols) + "\n")
        for r in rows:
            r["hunt_terms"] = " ".join(r["terms"])
            f.write("\t".join(str(r.get(c, "")).replace("\t", " ").replace("\n", " ") for c in cols) + "\n")
    print("requests this run", dict(net.n), file=sys.stderr)
    return rows


if __name__ == "__main__":
    main()

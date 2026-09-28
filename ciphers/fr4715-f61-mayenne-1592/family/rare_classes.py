#!/usr/bin/env python3
"""F61-FAMILY-4, campaign step H45 part 3 (28 Sept 2026): the rare-class inference. Five sign classes of f.61r have no period
reading (CA, LOOPBAR, ZHOOK, CROSS, LL: no glossed hand writes them more than once or twice). `contexts` gathers EVERY
occurrence of them across the leaves on disk -- f.61r (scripts/passA_classes.tsv + passU2_classes.tsv), f.108r (the H19/H20
lines, f61joint.f108_lines), f.101r, f.188r, f.108v and f.124r (the reconciled drafts passes/rec*/ciphertext_draft.tsv) --
each with its four neighbours on either side rendered under the newest merged period key (--key, decode_period.py's rule:
n >= 2 and n >= 0.1 x the leaf class total, EBR_A/EBR_B folded into EBR): one letter where the key gives one (grade C),
[a/b] where it gives a pair (M), ? where the class has no period pair, | at a line end, a clear word as itself; the
occurrence itself is written _. Output family/rare_contexts.tsv (class, leaf, line, pos, left, right, firm_neighbours).
`build TAG` writes the sets one blind Opus TEXT call judges in the H16 shape (scripts/f61judge.py, family/f61ctx.py), the
key and the class names withheld: TAG target = the five rare classes as X1..X5 (set 0), plus 20 sets (seed 1) in which the
same contexts are re-dealt at random among the five labels in the same sizes; TAG control = the POSITIVE control run
first (rule 3): three covered classes (HASH4 d/q, BETA m, INF u -- chosen for counts near the rare classes' and for
being polyphonic and single alike) hidden from the key, their occurrences subsampled to at most 20 each (seed 3) and
shown as X1..X3 the same way, plus 20 re-dealt sets. The 21 sets are written in a shuffled order (seed 7) as S00..S20 to
passes/rare_<TAG>_sets.txt; the map behind the labels to passes/rare_<TAG>_key.json (never shown). The judge returns
passes/rare_<TAG>_verdict.tsv: set, label, letters, consistency_0_10, and one row per set with label=SET and the set's
overall consistency. `score TAG` ranks the true set among 21 by the SET score (ties against the target; gate rank 1 of
21, p = 0.048) and, for the control, checks each hidden class's proposed letters contain its top period letter. On a
control PASS the target call runs; its proposals become family/rare_classes.tsv at grade S with the control numbers and,
for the record only, the scattered n = 1 gloss attestations of each class (key_period_f101/f188.tsv, key_period_held.tsv)
and Tomokiyo's f.108r overlay letters at the ZHOOK positions -- reported beside the proposal, never used by the judge.
  python3 rare_classes.py contexts [--key key_period_v4.tsv]
  python3 rare_classes.py build control|target [--key ...]
  python3 rare_classes.py score control|target        (from the family folder)
"""
import csv, json, os, random, sys
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); P = f"{HERE}/passes"; sys.path.insert(0, S)
RARE = ["CA", "LOOPBAR", "ZHOOK", "CROSS", "LL"]; CTRL = ["HASH4", "BETA", "INF"]; FRAC = 0.1; W = 4
KEYFILE = sys.argv[sys.argv.index("--key") + 1] if "--key" in sys.argv else "key_period_v3.tsv"
KEYFILE = KEYFILE if os.path.isabs(KEYFILE) else f"{HERE}/{KEYFILE}"
def load_key(hide=()):
    rows = [r for r in csv.DictReader((l for l in open(KEYFILE) if not l.startswith("#")), delimiter="\t")]
    tot = defaultdict(int); key = defaultdict(dict)
    for r in rows:
        if r["letter"] != "-": tot[(r["class"], r["leaf"])] += int(r["n"])
    for r in rows:
        cl = {"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["class"], r["class"])
        if cl in hide or cl in ("PLAIN", "OTHER", "DASH"): continue
        if r["letter"] != "-" and int(r["n"]) >= 2 and int(r["n"]) >= FRAC * tot[(r["class"], r["leaf"])]:
            key[cl][r["letter"]] = key[cl].get(r["letter"], 0) + int(r["n"])
    return {c: sorted(v, key=lambda k: -v[k]) for c, v in key.items()}
def leaves():
    out = {}
    d = defaultdict(list)
    for p in (f"{S}/passA_classes.tsv", f"{S}/passU2_classes.tsv"):
        for r in csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t"): d[r["line"]].append((r["sign"], r.get("note", "")))
    out["f.61r"] = d
    from f61joint import f108_lines
    out["f.108r"] = {k: [(s, "") for s in v] for k, v in f108_lines().items()}
    for leaf, pre in (("f.101r", "f101r"), ("f.188r", "f188r"), ("f.108v", "108v"), ("f.124r", "f124r"), ("f.97r", "f97r")):   # f.97r added by F61-FAMILY-5 (28 Sept 2026)
        path = f"{P}/rec{pre}/ciphertext_draft.tsv"
        if not os.path.exists(path): continue
        d = defaultdict(list); A = {}
        if os.path.exists(f"{P}/{pre}_signsA.tsv"):
            for r in csv.DictReader(open(f"{P}/{pre}_signsA.tsv"), delimiter="\t"): A[(r["line"], r["pos"])] = r
        B = {}
        if os.path.exists(f"{P}/{pre}_signsB.tsv"):
            for r in csv.DictReader(open(f"{P}/{pre}_signsB.tsv"), delimiter="\t"): B[(r["line"], r["pos"])] = r
        for r in csv.DictReader(open(path), delimiter="\t"):
            code = r["sign"]; a = A.get((r["line"], r["position"])); b = B.get((r["line"], r["position"]))
            if a and b and {a["sign"], b["sign"]} == {"HASH4", "4STEM"}: code = "H24"   # align_period.py's H24 rule
            if code == "DASH": continue
            d[r["line"]].append((code, (a or {}).get("note", "")))
        out[leaf] = d
    return out
def render(tok, key, hide):
    c, note = tok
    if c == "PLAIN": return "{" + (note.strip().split()[0] if note.strip() else "word") + "}"
    if c in hide or c not in key: return "?"
    v = key[c]; return v[0] if len(v) == 1 else "[" + "/".join(v) + "]"
def contexts(classes, hide, key):
    rows = []
    for leaf, d in leaves().items():
        for line, toks in d.items():
            for i, (c, note) in enumerate(toks):
                if c not in classes: continue
                L = [render(t, key, hide) for t in toks[max(0, i - W):i]]; R = [render(t, key, hide) for t in toks[i + 1:i + 1 + W]]
                if i - W < 0: L = ["|"] + L
                if i + 1 + W > len(toks): R = R + ["|"]
                firm = sum(1 for x in L + R if len(x) == 1 and x.isalpha())
                rows.append({"class": c, "leaf": leaf, "line": line, "pos": i + 1, "left": " ".join(L), "right": " ".join(R), "firm": firm})
    return rows
def cmd_contexts():
    key = load_key(); rows = contexts(set(RARE), set(), key)
    with open(f"{HERE}/rare_contexts.tsv", "w") as f:
        f.write(f"# rare_contexts.tsv -- F61-FAMILY-4, 28 Sept 2026: every occurrence of the five uncovered classes across the leaves on disk, neighbours rendered under {os.path.basename(KEYFILE)} (one letter = grade C, [a/b] = period pair, ? = no period pair, | = line end, {{word}} = a clear word in the row). Built by rare_classes.py contexts.\n")
        f.write("class\tleaf\tline\tpos\tleft\tright\tfirm_neighbours\n")
        for r in sorted(rows, key=lambda r: (RARE.index(r["class"]), r["leaf"], r["line"], r["pos"])): f.write("\t".join(str(r[k]) for k in ("class", "leaf", "line", "pos", "left", "right", "firm")) + "\n")
    c = Counter(r["class"] for r in rows); print("occurrences:", dict(c), "total", len(rows)); print("per leaf:", dict(Counter((r["class"], r["leaf"]) for r in rows)))
def cmd_build(tag):
    if tag == "target": classes = RARE; hide = set(RARE); key = load_key()
    else: classes = CTRL; hide = set(CTRL); key = load_key(hide=hide)
    rows = contexts(set(classes), hide, key)
    if tag == "control":
        rng = random.Random(3); by = defaultdict(list)
        for r in rows: by[r["class"]].append(r)
        rows = [r for c in classes for r in (rng.sample(by[c], 20) if len(by[c]) > 20 else by[c])]
    by = defaultdict(list)
    for r in rows: by[r["class"]].append(r)
    sizes = [len(by[c]) for c in classes]; labels = [f"X{i+1}" for i in range(len(classes))]
    def fmt(groups):
        out = []
        for lab, g in zip(labels, groups):
            out.append(f"  {lab} ({len(g)} occurrences):")
            for r in g: out.append(f"    {r['left']} _ {r['right']}")
        return "\n".join(out)
    sets = [("true", [by[c] for c in classes])]
    rng = random.Random(1); pool = [r for c in classes for r in by[c]]
    for k in range(20):
        p = list(pool); rng.shuffle(p); groups = []; i = 0
        for n in sizes: groups.append(p[i:i + n]); i += n
        sets.append((f"perm{k+1}", groups))
    order = list(range(21)); random.Random(7).shuffle(order)
    keymap = {}; txt = []
    for j, idx in enumerate(order):
        name, groups = sets[idx]; lab = f"S{j:02d}"; keymap[lab] = name
        txt.append(f"SET {lab}\n" + fmt(groups))
    open(f"{P}/rare_{tag}_sets.txt", "w").write("\n\n".join(txt) + "\n")
    json.dump({"sets": keymap, "classes": dict(zip(labels, classes)), "key_file": os.path.basename(KEYFILE), "sizes": sizes, "hidden_key": {c: load_key().get(c, []) for c in classes}}, open(f"{P}/rare_{tag}_key.json", "w"), indent=1)
    print(tag, "sets written:", len(sets), "sizes", dict(zip(labels, sizes)))
def cmd_score(tag):
    km = json.load(open(f"{P}/rare_{tag}_key.json")); v = [r for r in csv.DictReader(open(f"{P}/rare_{tag}_verdict.tsv"), delimiter="\t")]
    setscore = {r["set"]: float(r["consistency_0_10"]) for r in v if r["label"] == "SET"}
    true_lab = [l for l, n in km["sets"].items() if n == "true"][0]; ts = setscore[true_lab]
    rank = 1 + sum(1 for l, s in setscore.items() if l != true_lab and s >= ts)
    print(f"{tag}: true set {true_lab} score {ts}, rank {rank} of {len(setscore)} (ties against); scores sorted: {sorted(setscore.values(), reverse=True)}")
    props = {r["label"]: r["letters"] for r in v if r["set"] == true_lab and r["label"] != "SET"}
    for lab, cls in km["classes"].items():
        hk = km["hidden_key"].get(cls, [])
        hit = (hk and hk[0] in [x.strip() for x in props.get(lab, "").replace("/", ",").split(",")]) if tag == "control" else None
        print(f"  {lab} = {cls}: judge proposes '{props.get(lab, '')}'" + (f"; period top letter {hk[0] if hk else '-'} ({'recovered' if hit else 'MISSED'})" if tag == "control" else ""))
    ok = rank == 1 and (tag != "control" or all((km["hidden_key"][c] and km["hidden_key"][c][0] in [x.strip() for x in props.get(l, "").replace("/", ",").split(",")]) for l, c in km["classes"].items()))
    print("GATE:", "PASS" if ok else "FAIL"); return ok, rank, props
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "contexts": cmd_contexts()
    elif cmd == "build": cmd_build(sys.argv[2])
    elif cmd == "score": cmd_score(sys.argv[2])

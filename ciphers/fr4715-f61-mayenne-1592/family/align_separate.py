#!/usr/bin/env python3
"""F61-FAMILY-3 (28 Sept 2026): period-key recovery from a SEPARATE-SHEET decipherment -- the cipher letter on one
leaf (fr.3984 f.188r: lines that mix clear words and cipher signs) and its contemporary clear copy on another
(fr.3984 f.184r: the whole letter in clear, the deciphered stretches underlined). align_period.py knows only the
interlinear case (one gloss line above each cipher row); this is the separate-sheet mode the H30 brief asked for.

Alignment rule (recorded in KEY.md): by text order and letter count, anchored on the clear words.
 1. Signs: passes/f188r_signsA_c*.tsv + _signsB_c*.tsv (two blind Opus passes, atlas codes, chunks of 8 bands)
    concatenated, reconciled by tools/reconcile_passes.py (nw) into passes/recf188r/ciphertext_draft.tsv; PLAIN rows
    (a clear word in the line) ride through as tokens and take pass A's word (pass B's in the note).
 2. Clear: passes/f184r_clearA.tsv + _clearB.tsv (two blind Opus passes, one row per line, {braces} = underlined)
    flattened to word sequences and reconciled by difflib on the folded words (agreed words kept at conf h; a
    'replace' takes A's spelling at conf m with B's as alt; a word one pass alone read is kept at conf l).
 3. Anchors: the PLAIN words of f.188 (in leaf order) are aligned monotonically to the f.184 words by a DP that
    maximises the summed similarity of matched pairs (difflib ratio on folded strings, a match needs >= ANCHOR_MIN).
 4. Spans: between two consecutive anchors the f.184 words are split among the bands' sign runs in proportion to
    their token counts (letters per sign about 1: the cipher is letter by letter with a few nulls), at word
    boundaries; a band's plain_raw is the words so assigned to it, its cipher_raw the band's tokens (@CODE, or the
    clear word itself, which --clear-consumes lets take its own span).
 5. tools/interlinear_align.py align --code-prefix @ --null-cost -1 --clear-consumes, one pair per band, as
    align_period.py does; key rows (class, letter, n, leaf, bands) to passes/f188r_keyrows.tsv -> key_period_f188.tsv.
 Checks reported: anchors matched / PLAIN tokens, per-band letters-per-sign, and the share of plain words assigned to
 sign runs that the clear copy underlines (the decipherer's own mark of what was in cipher) -- a low share means the
 anchors drifted, and that band is dropped from the key (listed).
Grade C for every pair: the meaning is the period decipherer's, nothing is fitted; no letter is guessed.
  python3 align_separate.py [--anchor-min 0.72]   (from the family folder)
"""
import csv, difflib, glob, json, os, re, subprocess, sys, unicodedata
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); P = f"{HERE}/passes"
OPEN_LPS = float(sys.argv[sys.argv.index("--open-lps") + 1]) if "--open-lps" in sys.argv else 1.0
ANCHOR_MIN = float(sys.argv[sys.argv.index("--anchor-min") + 1]) if "--anchor-min" in sys.argv else 0.72
LEAF = "fr.3984 f.188r/f.184r"
def rd(path):
    return [r for r in csv.DictReader((l for l in open(path) if not l.startswith("#")), delimiter="\t")]
def fold(w):
    w = unicodedata.normalize("NFKD", w.lower()); w = "".join(c for c in w if not unicodedata.combining(c))
    w = re.sub(r"\[[^\]]*\]", "", w)                       # expanded abbreviations dropped for matching
    w = w.replace("v", "u").replace("j", "i").replace("y", "i")
    return re.sub(r"[^a-z]", "", w)
def norm_conf(c):
    c = (c or "").strip().lower(); return {"high": "h", "medium": "m", "med": "m", "low": "l"}.get(c, c[:1] if c[:1] in "hml" else "m")
# ---------- 1. signs: concatenate chunks, reconcile
for pas in ("signsA", "signsB"):
    files = sorted(glob.glob(f"{P}/f188r_{pas}_c*.tsv"), key=lambda f: int(re.search(r"_c(\d+)\.tsv$", f).group(1)))
    rows = []
    for f in files:
        for line in open(f):
            line = line.rstrip("\n")
            if not line.strip() or line.startswith("#") or line.startswith("line\t"): continue
            cells = line.split("\t"); cells += [""] * (7 - len(cells)); cells[3] = norm_conf(cells[3]); rows.append("\t".join(cells[:7]))
    open(f"{P}/f188r_{pas}.tsv", "w").write("line\tpos\tsign\tconf\tsegment\tx_px\tnote\n" + "\n".join(rows) + "\n")
    print(pas, len(files), "chunks", len(rows), "rows")
os.makedirs(f"{P}/recf188r", exist_ok=True)
r = subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", f"{P}/f188r_signsA.tsv", f"{P}/f188r_signsB.tsv", "--out-dir", f"{P}/recf188r", "--method", "nw"], capture_output=True, text=True)
print(r.stdout.strip()[-600:]); print(r.stderr.strip()[-300:])
agree = tot = 0; low = []
for row in csv.DictReader(open(f"{P}/recf188r/agreement.tsv"), delimiter="\t"):
    a, t = int(row["agree"]), int(row["columns"]); agree += a; tot += t
    if t and a / t < 0.7: low.append(f"{row['line']}:{a}/{t}")
print(f"SIGN AGREEMENT {agree}/{tot} = {agree/tot if tot else 0:.3f}; bands under 70%: {' '.join(low) or 'none'}")
draft = rd(f"{P}/recf188r/ciphertext_draft.tsv"); A = rd(f"{P}/f188r_signsA.tsv"); B = rd(f"{P}/f188r_signsB.tsv")
ax = {(r["line"], int(r["pos"])): r for r in A}; bx = {(r["line"], int(r["pos"])): r for r in B}
toks = []   # in leaf order: dict(band, kind S/P, val, conf)
def clean_word(n):
    n = re.sub(r"\(.*?\)", "", n); n = re.split(r"[;,]", n)[0]
    n = re.sub(r"^(plain|clear|word)[:\s]+", "", n.strip(), flags=re.I).strip(" '\"")
    return n.split()[0] if n.split() and len(n.split()) > 2 else n            # a shape description is not a word
# the draft's 'position' is the aligned column, not pass A's pos (gap columns shift it), so a PLAIN token's word is taken
# from the passes by ORDER: the k-th PLAIN of the band in the draft takes pass A's k-th PLAIN note (pass B's when A has none)
plainA = defaultdict(list); plainB = defaultdict(list)
for r in A:
    if r["sign"] == "PLAIN": plainA[r["line"]].append(clean_word(r["note"]))
for r in B:
    if r["sign"] == "PLAIN": plainB[r["line"]].append(clean_word(r["note"]))
kseen = Counter()
for r in draft:
    line, pos = r["line"], int(r["position"]); code = r["sign"]
    if code == "DASH": continue
    if code == "PLAIN":
        k = kseen[line]; kseen[line] += 1
        w = plainA[line][k] if k < len(plainA[line]) else (plainB[line][k] if k < len(plainB[line]) else "")
        toks.append({"band": line, "kind": "P", "val": w, "conf": r["confidence"]})
    else:
        toks.append({"band": line, "kind": "S", "val": code, "conf": r["confidence"]})
bands = sorted({t["band"] for t in toks}); print("tokens", len(toks), "signs", sum(t["kind"] == "S" for t in toks), "clear words", sum(t["kind"] == "P" for t in toks), "bands", len(bands))
# ---------- 2. clear copy: flatten and reconcile the two passes
def clear_words(path):
    out = []
    for r in rd(path):
        text = r["text"]; ul = False
        for m in re.finditer(r"\{|\}|\[\[.*?\]\]|[^\s{}]+", text):
            s = m.group(0)
            if s == "{": ul = True; continue
            if s == "}": ul = False; continue
            if s.startswith("[["): continue                     # crossed out
            if s in ("--", "-", "—"): continue
            if not fold(s): continue
            out.append({"w": s, "ul": ul, "line": r["line"], "conf": norm_conf(r["conf"])})
    return out
CA, CB = clear_words(f"{P}/f184r_clearA.tsv"), clear_words(f"{P}/f184r_clearB.tsv")
fa, fb = [fold(w["w"]) for w in CA], [fold(w["w"]) for w in CB]
sm = difflib.SequenceMatcher(None, fa, fb, autojunk=False); words = []; cst = Counter()
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        for k in range(i2 - i1):
            wa, wb = CA[i1 + k], CB[j1 + k]; words.append(dict(wa, conf="h", src="AB", ul=wa["ul"] or wb["ul"], ul_agree=wa["ul"] == wb["ul"])); cst["agree"] += 1
    elif tag == "replace":
        for k in range(max(i2 - i1, j2 - j1)):
            if k < i2 - i1:
                w = dict(CA[i1 + k], conf="m", src="A", ul_agree=False); w["alt"] = CB[j1 + k]["w"] if k < j2 - j1 else ""; words.append(w); cst["differ"] += 1
            else: words.append(dict(CB[j1 + k], conf="l", src="B", ul_agree=False)); cst["B-only"] += 1
    elif tag == "delete":
        for k in range(i1, i2): words.append(dict(CA[k], conf="l", src="A", ul_agree=False)); cst["A-only"] += 1
    else:
        for k in range(j1, j2): words.append(dict(CB[k], conf="l", src="B", ul_agree=False)); cst["B-only"] += 1
n_ab = cst["agree"]; print("clear reconciliation:", dict(cst), f"word agreement {n_ab}/{len(CA)} (A) {n_ab}/{len(CB)} (B) = {2*n_ab/(len(CA)+len(CB)):.3f}; underline flag agreement on agreed words {sum(1 for w in words if w['src']=='AB' and w['ul_agree'])}/{n_ab}")
with open(f"{P}/f184r_clear_rec.tsv", "w") as f:
    f.write("idx\tword\tul\tconf\tsrc\talt\tlineA\n")
    for i, w in enumerate(words): f.write(f"{i}\t{w['w']}\t{int(w['ul'])}\t{w['conf']}\t{w['src']}\t{w.get('alt','')}\t{w['line']}\n")
# ---------- 3. anchors: monotone DP of the PLAIN tokens onto the clear words
pi = [i for i, t in enumerate(toks) if t["kind"] == "P"]; W = len(words)
def sim(a, b):
    fa_, fb_ = fold(a), fold(b)
    if not fa_ or not fb_: return 0.0
    return difflib.SequenceMatcher(None, fa_, fb_).ratio()
NP = len(pi); best = [[0.0] * (W + 1) for _ in range(NP + 1)]; back = [[None] * (W + 1) for _ in range(NP + 1)]
for i in range(1, NP + 1):
    for j in range(1, W + 1):
        best[i][j], back[i][j] = best[i - 1][j], "up"
        if best[i][j - 1] > best[i][j]: best[i][j], back[i][j] = best[i][j - 1], "left"
        wf = fold(toks[pi[i - 1]]["val"]); s = sim(toks[pi[i - 1]]["val"], words[j - 1]["w"])
        # anchors are weighted by length: a short function word (de, que, le) matches anywhere and would drift the
        # monotone path, so words under 3 letters never anchor, 3-letter words need an exact match, longer ones ANCHOR_MIN
        ok = (len(wf) >= 4 and s >= ANCHOR_MIN) or (len(wf) == 3 and s >= 0.99)
        if ok and best[i - 1][j - 1] + s * len(wf) > best[i][j]: best[i][j], back[i][j] = best[i - 1][j - 1] + s * len(wf), "diag"
i, j = NP, W; match = {}
while i > 0 and j > 0:
    if back[i][j] == "diag": match[pi[i - 1]] = j - 1; i -= 1; j -= 1
    elif back[i][j] == "up": i -= 1
    else: j -= 1
# outlier anchors: a junk clear word (a cipher run read as letters) can match a real word many lines away; the anchor set
# must follow one monotone trend (word index vs token index), so anchors whose residual from a least-squares line through
# the others exceeds 60 words are dropped one at a time, worst first, and the line refitted
def refit(m):
    xs = sorted(m); ys = [m[x] for x in xs]; n = len(xs)
    if n < 3: return {}
    mx, my = sum(xs) / n, sum(ys) / n; sxx = sum((x - mx) ** 2 for x in xs) or 1.0
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx; a = my - b * mx
    return {x: m[x] - (a + b * x) for x in xs}
dropped = []
while True:
    res = refit(match)
    if not res: break
    worst = max(res, key=lambda x: abs(res[x]))
    if abs(res[worst]) <= 60: break
    dropped.append((toks[worst]["val"], words[match[worst]]["w"], round(res[worst]))); del match[worst]
print(f"anchors: {len(match)}/{NP} clear words of f.188 matched to the clear copy (min similarity {ANCHOR_MIN}); off-trend anchors dropped: {dropped}")
# ---------- 4. spans: split the clear words between anchors among the token runs in proportion to token count
assign = [None] * len(toks)          # token index -> (w0, w1) word span for the band piece it belongs to (filled per piece)
anchors = sorted(match.items())       # (token idx, word idx)
def pieces(t0, t1):
    """token indices t0..t1-1 grouped by band, in order -> list of (band, [token idxs])"""
    out = []
    for k in range(t0, t1):
        if out and out[-1][0] == toks[k]["band"]: out[-1][1].append(k)
        else: out.append((toks[k]["band"], [k]))
    return out
band_words = defaultdict(list)       # band -> list of word idxs (in order)
def weight(k):
    t = toks[k]; return 1.0 if t["kind"] == "S" else max(1.0, len(fold(t["val"])))
segs = []
prev_t, prev_w = -1, -1
for (ti, wi) in anchors + [(len(toks), W)]:
    if ti < len(toks): band_words[toks[ti]["band"]].append(wi)                  # the anchor word itself
    pcs = pieces(prev_t + 1, ti); wl = list(range(prev_w + 1, wi))
    # before the first anchor and after the last one the clear copy runs on for the rest of the page: cap those two
    # open-ended spans at about OPEN_LPS letters per token (default 1.0, --open-lps), counted outward from the anchor (the rest of the page is not ours)
    if pcs and wl and (prev_t < 0 or ti >= len(toks)):
        budget = OPEN_LPS * sum(weight(k) for _, ks in pcs for k in ks); keep = []; acc = 0
        for w_ in (reversed(wl) if prev_t < 0 else wl):
            if acc >= budget: break
            keep.append(w_); acc += len(fold(words[w_]["w"]))
        wl = sorted(keep)
    if pcs and wl:
        tw = sum(weight(k) for _, ks in pcs for k in ks); letters = [len(fold(words[w]["w"])) for w in wl]; L = sum(letters)
        cum_target = 0.0; wpos = 0; assigned = 0
        for n_, (band, ks) in enumerate(pcs):
            cum_target += sum(weight(k) for k in ks) / tw * L; take = []
            if n_ == len(pcs) - 1: take = wl[wpos:]; wpos = len(wl)
            else:
                while wpos < len(wl) and assigned + letters[wpos] / 2 <= cum_target:
                    take.append(wl[wpos]); assigned += letters[wpos]; wpos += 1
            band_words[band].extend(take)
        segs.append((prev_t + 1, ti, prev_w + 1, wi, len(pcs)))
    elif pcs:
        segs.append((prev_t + 1, ti, prev_w + 1, wi, len(pcs)))   # signs with no clear words between anchors: no letters (recorded)
    prev_t, prev_w = ti, wi
# ---------- 5. pairs per band -> shared aligner
with open(f"{P}/f188r_pairs.tsv", "w") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["plain_line", "plain_raw", "cipher_line", "cipher_raw"])
    for band in bands:
        widx = sorted(set(band_words[band])); plain = " ".join(re.sub(r"\[[^\]]*\]", "", words[i]["w"]).strip("{}.,;:()'\"") for i in widx)
        ciph = " ".join(("@" + t["val"]) if t["kind"] == "S" else (fold(t["val"]) or "x") for t in toks if t["band"] == band)
        w.writerow([band, plain, band, ciph])
r = subprocess.run([sys.executable, f"{ROOT}/tools/interlinear_align.py", "align", f"{P}/f188r_pairs.tsv", f"{P}/f188r_align.tsv", f"{P}/f188r_key.tsv",
                    "--code-prefix", "@", "--null-cost", "-1", "--clear-consumes"], capture_output=True, text=True)
print("interlinear_align:", r.stdout.strip()[-400:], r.stderr.strip()[-300:])
# per-band checks: letters per sign, underline share, and the drop list
report = []; drop = set(sys.argv[sys.argv.index("--drop") + 1].split(",")) if "--drop" in sys.argv else set()   # --drop L23: bands excluded from the key by hand (a defective crop), listed in KEY.md
for band in bands:
    widx = sorted(set(band_words[band])); nS = sum(1 for t in toks if t["band"] == band and t["kind"] == "S")
    nP = [t for t in toks if t["band"] == band and t["kind"] == "P"]; anch = sum(1 for k, t in enumerate(toks) if t["band"] == band and k in match)
    cw = [words[i] for i in widx if i not in match.values()]     # words not anchors
    ul = sum(1 for x in cw if x["ul"]); L = sum(len(fold(x["w"])) for x in cw)
    wt = nS + sum(len(fold(t["val"])) for k, t in enumerate(toks) if t["band"] == band and t["kind"] == "P" and k not in match)
    lps = L / wt if wt else 0.0        # plain letters per unit of cipher weight (a sign = 1, an unmatched clear word = its letters)
    bad = nS >= 5 and (lps < 0.55 or lps > 1.6)
    if bad: drop.add(band)
    report.append((band, nS, len(nP), anch, len(cw), L, round(lps, 2), f"{ul}/{len(cw)}", "DROP" if band in drop else ""))
with open(f"{P}/f188r_spans.tsv", "w") as f:
    f.write("band\tsigns\tclear_words\tanchors\tplain_words\tplain_letters\tletters_per_sign\tunderlined\tverdict\n")
    for r_ in report: f.write("\t".join(map(str, r_)) + "\n")
print("band\tsigns\tclear\tanchors\tplain_words\tletters\tL/sign\tunderlined\tverdict"); [print("\t".join(map(str, r_))) for r_ in report]
ul_all = sum(int(r_[7].split("/")[0]) for r_ in report); cw_all = sum(int(r_[7].split("/")[1]) for r_ in report)
print(f"underline share of plain words assigned to sign runs: {ul_all}/{cw_all} = {ul_all/cw_all if cw_all else 0:.3f}; bands dropped: {' '.join(sorted(drop)) or 'none'}")
# key rows from the per-token alignment (dropped bands excluded)
pairs = Counter(); where = defaultdict(set)
for t in rd(f"{P}/f188r_align.tsv"):
    if t["kind"] != "code" or t["cipher_line"] in drop: continue
    code = t["raw"].lstrip("@"); ch = t["plain_chunk"].strip(); val = ch if ch else "-"
    pairs[(code, val)] += 1; where[(code, val)].add(t["cipher_line"])
with open(f"{P}/f188r_keyrows.tsv", "w") as f:
    f.write("class\tletter\tn\tleaf\tbands\n")
    for (code, val), n in sorted(pairs.items(), key=lambda kv: (kv[0][0], -kv[1], kv[0][1])):
        f.write(f"{code}\t{val}\t{n}\t{LEAF}\t{','.join(sorted(where[(code, val)]))}\n")
top = defaultdict(Counter)
for (code, val), n in pairs.items():
    if val != "-": top[code][val] += n
print("key rows:", len(pairs), "classes:", len(top)); print(" ".join(f"{c}={'/'.join(f'{l}{n}' for l, n in top[c].most_common(3))}" for c in sorted(top, key=lambda c: -sum(top[c].values()))))
json.dump({"anchor_min": ANCHOR_MIN, "anchors": len(match), "plain_tokens": NP, "sign_agreement": [agree, tot], "clear_word_agreement": [n_ab, len(CA), len(CB)], "dropped": sorted(drop)}, open(f"{P}/f188r_separate_stats.json", "w"), indent=1)

#!/usr/bin/env python3
"""Test 1 for rah-juan-manuel-1521 (LANE-JM JM-ALPHA, 4 Oct 2026): letter-alphabet recovery, held out.

Inputs (all in this folder): passes/f194_{A,B}.tsv and passes/f199_{A,B}.tsv (two blind Sonnet passes per cipher
page on tools/iiif_lines.py crops, shared sign inventory passes/inventory.md), gloss_f197.tsv + passes/gloss_f197_rest.tsv
(the clerk's decipherment of R9528 f.194) and passes/gloss_f201.tsv (the clerk's decipherment of R9529 f.199), and
Tomokiyo's nomenclator sources/cryptiana/keys/AlonsoSanchez_2.tsv (word codes only).

Steps
  1. normalise each pass to one label set (pass-local ?n labels mapped by their own descriptions, NORM below),
     drop the duplicate crop rows the line cutter produced (DUP), reconcile A/B per line by token alignment:
     err_2reader = 1 - agreed tokens / max(len A, len B), pooled. A disagreeing symbol becomes a unique unknown
     sign (@uN) that may take letters but never counts as evidence; a disagreeing pair where one side is a table
     code takes the code.
  2. build one alignment pair per page: table codes -> their word (clear-consumes anchor), bracketed clear words ->
     clear, symbols -> @LABEL (0-2 letters, --code-chunk 2), Latin groups missing from the table -> %group (a word
     code learned from the gloss), and run tools/interlinear_align.py's hard-EM aligner (same code path as its CLI).
  3. R9528 (in sample): alphabet = each symbol's top chunk (grade C, source f.194/f.197) -> alphabet.tsv.
  4. R9529 (held out): the SAME aligner on f.199 vs f.201 with NO prior (nothing from R9528 enters it); statistic
     S = share of f.199 symbol tokens (labels present in alphabet.tsv) whose aligned f.201 chunk equals the R9528
     alphabet value of that label. Null: 200 alphabets with the R9528 values permuted among the labels (seed 1..200);
     the alignment is fixed, so the permutation CAN move S (rule 3). Gate: witness/gate_alpha.txt (pre-registered).

  python3 scripts/test1.py [--check]      (--check: exit 1 if results_test1.json / alphabet.tsv differ from a rerun)
  python3 scripts/test1.py --alphabet key_tomokiyo_alpha.tsv [--check]
     (R11-RJMKEY, 6 Oct 2026: the same held-out S and permutation control with a published key in place of alphabet.tsv;
      gate witness/PREREG_tomokiyo_alpha.md; writes results_test1_tomokiyo.json only, alphabet.tsv untouched)
"""
import argparse, csv, difflib, importlib.util, json, random, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
ROOT = HERE.parent.parent
KEY = ROOT / "sources/cryptiana/keys/AlonsoSanchez_2.tsv"
spec = importlib.util.spec_from_file_location("ia", ROOT / "tools/interlinear_align.py")
ia = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ia)

# pass-local labels -> shared labels, from each pass's own description of its ?n signs
NORM = {
    ("f194", "A"): {"?1": "R", "?2": "K"},   # A: ?1 small raised co/ro with o beneath (= R); ?2 dagger-like cross-barred
    ("f194", "B"): {"?1": "K", "?2": "T"},   # B: ?1 circle on a cross, ankh-like (= A's ?2); ?2 hatched triple stroke (= T)
    ("f199", "A"): {},
    ("f199", "B"): {},
}
# duplicate crops: the slope tracker locked two bands onto one text line (fits a=560/562, 625/630, 1347/1353,
# 1482/1489 in images/crops_jmalpha_manifest.json); both passes flagged the same pairs. Drop the second of each.
DUP = {"f194": {9, 11, 23, 26}, "f199": set()}
SYMBOL = re.compile(r"^(?:[A-Z]|[0-9]|\?\d+)$")


def load_key():
    codes = {}
    for line in KEY.read_text().splitlines():
        if not line or line.startswith("#") or line.startswith("sign\t"):
            continue
        f = line.split("\t")
        v = re.sub(r"[\[\]?]", "", f[1]).replace("(", "").replace(")", "")
        codes.setdefault(f[0].strip(), v.strip())
    return codes


def tokens(cell, page, p):
    """one pass row -> tokens; bracketed clear runs kept as one token '[...]'."""
    out = []
    for m in re.finditer(r"\[[^\]]*\]|\S+", cell or ""):
        t = m.group(0)
        if t.startswith("["):
            out.append(t)
            continue
        t = t.rstrip("?") or "~"
        t = NORM[(page, p)].get(t, t)
        if t in ("tt", "#"):
            t = "T"
        out.append(t)
    return out


def load_pass(page, p):
    rows = {}
    with open(HERE / "passes" / f"{page}_{p}.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            n = int(r["line"])
            if n not in DUP[page]:
                rows[n] = tokens(r.get("tokens", ""), page, p)
    return rows


def reconcile(A, B, key):
    agree = tot = 0
    out = {}
    unk = [0]

    def u():
        unk[0] += 1
        return "~"
    for n in sorted(set(A) | set(B)):
        a, b = A.get(n, []), B.get(n, [])
        tot += max(len(a), len(b))
        sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
        line = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                agree += i2 - i1
                line += [(t, "agree") for t in a[i1:i2]]
                continue
            sa, sb = a[i1:i2], b[j1:j2]
            ka = sum(t in key for t in sa)
            kb = sum(t in key for t in sb)
            pick = sa if (ka > kb or (ka == kb and len(sa) >= len(sb))) else sb
            for t in pick:
                line.append((t, "split-code") if t in key else (u(), "split"))
        out[n] = line
    return out, (1 - agree / tot if tot else None), agree, tot


def to_pair(line_toks, key):
    raw, kinds = [], []
    for t, st in line_toks:
        if t.startswith("["):
            for w in re.findall(r"[A-Za-zñç]+", t):
                raw.append(w.lower()); kinds.append("clear")
        elif t == "~":
            raw.append("@~"); kinds.append("unk")
        elif SYMBOL.match(t):
            raw.append("@" + t); kinds.append("sym")
        elif t in key:
            w = re.sub(r"[^a-zñç]", "", key[t].lower())
            raw.append(w or "x"); kinds.append("code")
        else:
            raw.append("%" + t.lower()); kinds.append("miss")
    return raw, kinds


def gloss_text(paths):
    txt = []
    for pth in paths:
        with open(pth, encoding="utf-8") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                t = r["text"]
                if t.strip().lower().rstrip(".") == "claro":
                    continue
                txt.append(t)
    return " ".join(txt)


def align(rec, gloss, key):
    raw, kinds = [], []
    for n in sorted(rec):
        r, k = to_pair(rec[n], key)
        raw += r; kinds += k
    # unknown positions: give each a unique name so they never pool evidence
    c = 0
    for i, t in enumerate(raw):
        if t == "@~":
            c += 1
            raw[i] = "@~%d" % c
    ia.WORD_PFX = "%"
    ia.CODE_CHUNK = 2
    pair = {"plain_line": "1", "plain_raw": gloss, "cipher_line": "1", "cipher_raw": " ".join(raw)}
    prepared, results, counts, shown = ia.run_align([pair], floor=0, clear_consumes=True, code_prefix="@",
                                                    null_cost=-1.0, max_chunk=10)
    letters = prepared[0][3]
    chunks = [letters[c0:c1] if c else "" for c in results[0] for c0, c1 in [c or (0, 0)]]
    toks = [classify for classify in prepared[0][2]]
    return raw, kinds, chunks, counts, letters


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--shuffles", type=int, default=200)
    ap.add_argument("--alphabet", help="published key TSV (letter, shape, firm, our_label ...) scored instead of alphabet.tsv")
    a = ap.parse_args()
    key = load_key()
    res = {}
    recs = {}
    for page in ("f194", "f199"):
        A, B = load_pass(page, "A"), load_pass(page, "B")
        rec, err, agree, tot = reconcile(A, B, key)
        recs[page] = rec
        res[page] = {"err_2reader": round(err, 4), "agree_tokens": agree, "max_tokens": tot,
                     "lines": len(rec),
                     "symbols_agreed": sum(1 for l in rec.values() for t, s in l if s == "agree" and SYMBOL.match(t)),
                     "symbols_split": sum(1 for l in rec.values() for t, s in l if s == "split")}
    # R9528 in sample
    g197 = gloss_text([HERE / "gloss_f197.tsv", HERE / "passes/gloss_f197_rest.tsv"])
    raw, kinds, chunks, counts, _ = align(recs["f194"], g197, key)
    alpha = {}
    for t, k in zip(raw, kinds):
        if k == "sym":
            v = t[1:]
            cnt = counts.get(v, Counter())
            if cnt and v not in alpha:
                top, n = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[0]
                alpha[v] = (top, n, sum(cnt.values()), dict(cnt))
    occ = Counter(t[1:] for t, k in zip(raw, kinds) if k == "sym")
    insample_hit = sum(1 for t, k, ch in zip(raw, kinds, chunks) if k == "sym" and t[1:] in alpha
                       and ia.fold(ch) == alpha[t[1:]][0])
    insample_n = sum(1 for t, k in zip(raw, kinds) if k == "sym" and t[1:] in alpha)
    code_hit = sum(1 for t, k, ch in zip(raw, kinds, chunks) if k == "code" and ia.fold(ch) == ia.fold(t))
    res["f194_align"] = {"symbol_tokens": sum(occ.values()), "labels": len(occ), "labels_with_value": len(alpha),
                         "insample_symbol_selfagree": round(insample_hit / insample_n, 4) if insample_n else None,
                         "insample_n": insample_n,
                         "code_words_matched": code_hit, "code_words": sum(1 for k in kinds if k == "code"),
                         "gloss_letters": len(ia.plain_letters(g197)[0])}
    rows = [["sign", "letter", "n_agree", "n_occ", "others", "grade", "source"]]
    for v in sorted(alpha, key=lambda x: (-occ[x], x)):
        top, n, tot, cnt = alpha[v]
        others = ",".join("%s:%d" % (m, c) for m, c in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0])) if m != top)
        grade = "C" if n >= 2 else "M"
        rows.append([v, top, n, occ[v], others, grade, "R9528 f.194 (passes A/B reconciled) vs f.197 gloss"])
    alpha_txt = "".join("\t".join(map(str, r)) + "\n" for r in rows)
    # R9529 held out
    gate_file = HERE / "witness/gate_alpha.txt"
    g201p = HERE / "passes/gloss_f201.tsv"
    if gate_file.exists() and g201p.exists() and (HERE / "passes/f199_B.tsv").exists():
        g201 = gloss_text([g201p])
        raw2, kinds2, chunks2, _, _ = align(recs["f199"], g201, key)
        values = {v: alpha[v][0] for v in alpha}
        idx = [i for i, k in enumerate(kinds2) if k == "sym" and raw2[i][1:] in values]

        def stat(vals):
            return sum(ia.fold(chunks2[i]) == vals[raw2[i][1:]] for i in idx) / len(idx) if idx else 0.0
        real = stat(values)
        labs = sorted(values)
        null = []
        for s in range(1, a.shuffles + 1):
            rnd = random.Random(s)
            perm = [values[l] for l in labs]
            rnd.shuffle(perm)
            null.append(stat(dict(zip(labs, perm))))
        null.sort()
        code_hit2 = sum(1 for t, k, ch in zip(raw2, kinds2, chunks2) if k == "code" and ia.fold(ch) == ia.fold(t))
        res["heldout_f199"] = {"N_symbol_tokens": len(idx), "S_real": round(real, 4),
                               "null_mean": round(sum(null) / len(null), 4), "null_p95": round(null[int(0.95 * len(null)) - 1], 4),
                               "null_max": round(null[-1], 4), "rank": 1 + sum(x >= real for x in null),
                               "of": len(null) + 1, "code_words_matched": code_hit2,
                               "code_words": sum(1 for k in kinds2 if k == "code"),
                               "symbol_tokens_all": sum(1 for k in kinds2 if k == "sym")}
    if a.alphabet:
        return published(a, recs, (raw, kinds, chunks), g197, key)
    out_json = json.dumps(res, indent=1, sort_keys=True) + "\n"
    if a.check:
        ok = (HERE / "results_test1.json").read_text() == out_json and (HERE / "alphabet.tsv").read_text() == alpha_txt
        print("up to date" if ok else "STALE")
        sys.exit(0 if ok else 1)
    (HERE / "results_test1.json").write_text(out_json)
    (HERE / "alphabet.tsv").write_text(alpha_txt)
    rc = {}
    for page, rec in recs.items():
        rc[page] = "".join("%d\t%s\n" % (n, " ".join(t for t, _ in rec[n])) for n in sorted(rec))
        (HERE / f"ciphertext_{page}_reconciled.tsv").write_text("line\ttokens\n" + rc[page])
    print(out_json)


def score(raw, kinds, chunks, values, shuffles):
    """S = share of symbol tokens (labels in values) whose aligned chunk equals the value; null = values permuted."""
    idx = [i for i, k in enumerate(kinds) if k == "sym" and raw[i][1:] in values]

    def stat(vals):
        return sum(ia.fold(chunks[i]) == vals[raw[i][1:]] for i in idx) / len(idx) if idx else 0.0
    real = stat(values)
    labs = sorted(values)
    null = []
    for s in range(1, shuffles + 1):
        rnd = random.Random(s)
        perm = [values[l] for l in labs]
        rnd.shuffle(perm)
        null.append(stat(dict(zip(labs, perm))))
    null.sort()
    per = {}
    for i in idx:
        l = raw[i][1:]
        h, n = per.get(l, (0, 0))
        per[l] = (h + (ia.fold(chunks[i]) == values[l]), n + 1)
    return {"N_symbol_tokens": len(idx), "S_real": round(real, 4), "null_mean": round(sum(null) / len(null), 4),
            "null_p95": round(null[int(0.95 * len(null)) - 1], 4), "null_max": round(null[-1], 4),
            "rank": 1 + sum(x >= real for x in null), "of": len(null) + 1,
            "gate": "PASS" if real > null[-1] and real >= 0.24 else "FAIL",
            "per_label": {l: "%d/%d" % per[l] for l in sorted(per)}}


def published(a, recs, f194, g197, key):
    values = {}
    for r in csv.DictReader((l for l in open(HERE / a.alphabet) if not l.startswith("#")), delimiter="\t"):
        if r["firm"] == "1" and r["our_label"]:
            for lab in r["our_label"].split(","):
                values[lab] = "" if r["letter"] == "null" else r["letter"]
    res = {"key": a.alphabet, "values": values}
    res["f194_secondary"] = score(*f194, values, a.shuffles)
    g201 = gloss_text([HERE / "passes/gloss_f201.tsv"])
    raw2, kinds2, chunks2, _, _ = align(recs["f199"], g201, key)
    res["heldout_f199"] = score(raw2, kinds2, chunks2, values, a.shuffles)
    out_json = json.dumps(res, indent=1, sort_keys=True) + "\n"
    out = HERE / "results_test1_tomokiyo.json"
    if a.check:
        ok = out.exists() and out.read_text() == out_json
        print("up to date" if ok else "STALE")
        sys.exit(0 if ok else 1)
    out.write_text(out_json)
    print(out_json)


if __name__ == "__main__":
    main()

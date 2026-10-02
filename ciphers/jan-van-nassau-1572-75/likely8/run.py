#!/usr/bin/env python3
"""LIKELY-8 (2 Oct 2026, account-4): first cheap test on WVO 5549, exactly as likely-solves row 8 names it.

Step 1, known answer first (README common tail): the postscript stretch (ciphertext_5549_ps.tsv, PS1-PS26) decoded
under key_full.tsv (Lodewijk's 1574 table + AX-MERGE additions) is scored against Groen's clear print of the same
stretch (groen/gpas_lettre45.txt, Suppl. pp.146*-148*), KEY and TRANSCRIPTION separately:
  key:            mean per-line letter similarity (difflib ratio) real key vs 20 value-shuffled keys;
  transcription:  per token, aligned letter match; a mismatch that a single digit confusion of the token (4/9, 1/7,
                  3/8, 0/6, 5/6, 2/7, or a dropped/doubled digit) would repair is 'transcription-explainable'.
Step 2: the 537 body groups (runs 1-61) under key_1572, key_5549 (= Lodewijk's table) and key_full, each against 20
value-shuffled copies of the same key, scored with the judge's own de16 4-gram model (mean log10 / letter) and
word cover; plus tools/judge_plaintext.py PASS/FAIL through specs/jan-van-nassau-1572-75.json.
Disk only. Writes likely8/results.json and likely8/*.txt. Exit 0.
"""
import csv, difflib, json, os, random, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools"))
import judge_plaintext as J

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, "..")
KEYS = {"key_1572": os.path.join(T, "key_1572.tsv"),
        "key_5549": os.path.join(T, "key_5549.tsv"),
        "key_full": os.path.join(T, "..", "lodewijk-van-nassau-1573-74", "key_full.tsv")}
NSHUF = 20

def read_key(p):
    k = {}
    with open(p, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            k[r["code"].strip()] = (r["value"].strip(), r.get("grade", "").strip())
    return k

def shuffled(key, seed):
    codes = list(key); vals = [key[c] for c in codes]
    random.Random(seed).shuffle(vals)
    return dict(zip(codes, vals))

def read_ps():
    lines = {}
    with open(os.path.join(T, "ciphertext_5549_ps.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            lines.setdefault(r["line"], []).append(r["token"].strip())
    return lines

def read_body():
    runs = {}
    with open(os.path.join(T, "ciphertext_5549.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r["run"].startswith("PS"):
                continue
            runs.setdefault(r["run"], []).append((r["token"].strip(), r["kind"]))
    return runs

def dec_tok(tok, key):
    """-> (letters, cls) cls in letter|word|null|unknown|clear"""
    if tok.startswith("="):
        return J.fold(tok[1:]), "clear"
    v = key.get(tok)
    if v is None:
        return "", "unknown"
    val = v[0]
    if val in ("NULL",):
        return "", "null"
    if val in ("", "?"):
        return "", "unknown"
    return J.fold(val), ("letter" if len(J.fold(val)) == 1 else "word")

def norm(s):
    s = J.fold(s)
    return s.replace("v", "u").replace("w", "u").replace("j", "i").replace("y", "i")

# Groen's clear span for each PS line that has one (hand-mapped 2 Oct 2026 from reading_5549_ps_full.txt vs
# groen/gpas_lettre45.txt lines 251-271). PS1-PS6: Groen's print diverges from the leaf at the start of the
# stretch (the leaf's clear context 'sollt mich' is not in Groen; the WVO record calls the edition 'onv.'), so
# no counterpart. PS12: Groen prints only '[de]' (his own bracket) for the three-group run. PS26: a dot.
GROEN = {
    "PS7": "Monsieur de la Noue", "PS8": "Strossi", "PS9": "uf dem wasser", "PS10": "vii odder viii",
    "PS11": "gutter", "PS13": "ahn der hant", "PS14": "grentzen und", "PS15": "fussvolck",
    "PS16": "fussvolck des", "PS17": "gedanckt", "PS18": "zuvor gedinet", "PS19": "ligen",
    "PS20": "zu E.G.", "PS21": "in zihen", "PS22": "volck", "PS23": "de Lumbres",
    "PS24": "bey Palsgrave", "PS25": "Zuleger",
}
CONF = {"4": "9", "9": "4", "1": "7", "7": "1", "3": "8", "8": "3", "0": "6", "6": "0", "5": "6", "2": "7"}

def neighbours(tok):
    out = set()
    for i, ch in enumerate(tok):
        if ch in CONF:
            out.add(tok[:i] + CONF[ch] + tok[i + 1:])
        out.add(tok[:i] + tok[i + 1:])          # dropped digit
        out.add(tok[:i] + ch + ch + tok[i + 1:])  # doubled digit
    out.discard(tok); out.discard("")
    return out

def ps_key_score(key, lines):
    sims = []
    for ln, g in GROEN.items():
        d = "".join(dec_tok(t, key)[0] for t in lines[ln])
        sims.append(difflib.SequenceMatcher(None, norm(d), norm(g)).ratio())
    return sum(sims) / len(sims)

def ps_transcription(key, lines):
    """per-token alignment of the real-key decode against Groen; mismatches tested for a digit-confusion repair."""
    rows = []; tot = {"match": 0, "mismatch": 0, "tx_explainable": 0, "unknown": 0, "null": 0, "word": 0, "clear": 0}
    for ln, g in GROEN.items():
        toks = lines[ln]; pieces = [dec_tok(t, key) for t in toks]
        d = "".join(p[0] for p in pieces); gn = norm(g); dn = norm(d)
        # letter index -> matched?
        sm = difflib.SequenceMatcher(None, dn, gn); matched = [False] * len(dn); gmap = {}
        for a, b, n in sm.get_matching_blocks():
            for i in range(n):
                matched[a + i] = True; gmap[a + i] = b + i
        # which groen letter a mismatched decode letter faces (best effort: nearest unmatched by order)
        pos = 0
        for t, (letters, cls) in zip(toks, pieces):
            L = len(norm(letters))
            if cls in ("unknown", "null", "clear", "word"):
                tot[cls] += 1
                if cls == "word":
                    tot["match" if all(matched[pos:pos + L]) else "mismatch"] += 0  # words scored in key score only
                pos += L; continue
            ok = all(matched[pos:pos + L]) and L > 0
            if ok:
                tot["match"] += 1
            else:
                tot["mismatch"] += 1
                # the groen letter at the aligned slot: use opcode replace region
                want = None
                for tag, i1, i2, j1, j2 in sm.get_opcodes():
                    if tag in ("replace", "delete") and i1 <= pos < i2:
                        want = gn[j1:j2]; break
                expl = False
                if want:
                    for nb in neighbours(t):
                        l2, c2 = dec_tok(nb, key)
                        if c2 == "letter" and norm(l2) and norm(l2) in want:
                            expl = True; break
                tot["tx_explainable"] += int(expl)
                rows.append((ln, t, letters, want or "", "digit-swap" if expl else "key-or-groen"))
            pos += L
    return tot, rows

def body_decode(key, runs):
    out = []; cls = {"letter": 0, "word": 0, "null": 0, "unknown": 0, "clear": 0, "roman": 0}
    for run, toks in runs.items():
        s = ""
        for tok, kind in toks:
            if kind == "roman":
                cls["roman"] += 1; continue
            if kind == "clear":
                cls["clear"] += 1; s += J.fold(tok); continue
            letters, c = dec_tok(tok, key); cls[c] += 1; s += letters
        out.append(s)
    return out, cls

def main():
    model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["de"]])
    res = {}
    ps = read_ps(); runs = read_body()
    # ---- step 1: known answer on the postscript
    kf = read_key(KEYS["key_full"])
    real = ps_key_score(kf, ps)
    shuf = [ps_key_score(shuffled(kf, s), ps) for s in range(1, NSHUF + 1)]
    tot, rows = ps_transcription(kf, ps)
    dps = "\n".join("".join(dec_tok(t, kf)[0] for t in ps[ln]) for ln in GROEN)
    gps = "\n".join(GROEN.values())
    res["step1_postscript_known_answer"] = {
        "lines_scored": len(GROEN), "lines_without_groen_counterpart": ["PS1", "PS2", "PS3", "PS4", "PS5", "PS6", "PS12", "PS26"],
        "key_similarity_real": round(real, 3), "key_similarity_shuffle_mean": round(sum(shuf) / len(shuf), 3),
        "key_similarity_shuffle_max": round(max(shuf), 3),
        "transcription": tot, "mismatch_rows": rows,
        "lm_decode": round(model.score(dps), 3), "lm_groen_same_span": round(model.score(gps), 3),
        "lm_decode_shuffled_keys_max": round(max(model.score("\n".join("".join(dec_tok(t, shuffled(kf, s))[0] for t in ps[ln]) for ln in GROEN)) for s in range(1, NSHUF + 1)), 3),
    }
    # positive control for step 2's instrument: the whole postscript stretch (226 tokens) under key_full vs 20 shuffles,
    # scored exactly as the body is (de16 4-gram + word cover + judge)
    allps = {ln: [(t, "num") for t in toks] for ln, toks in ps.items()}
    dps_all, cls_ps = body_decode(kf, allps); lps = J.fold("\n".join(dps_all))
    sps = [model.score(J.fold("\n".join(body_decode(shuffled(kf, s), allps)[0]))) for s in range(1, NSHUF + 1)]
    cps = [model.cover(J.fold("\n".join(body_decode(shuffled(kf, s), allps)[0]))) for s in range(1, NSHUF + 1)]
    spec = json.load(open(os.path.join(T, "..", "..", "specs", "jan-van-nassau-1572-75.json")))
    res["step2_control_postscript_key_full"] = {
        "token_classes": cls_ps, "letters": len(lps),
        "lm_real": round(model.score(lps), 3), "lm_shuffle_mean": round(sum(sps) / len(sps), 3), "lm_shuffle_max": round(max(sps), 3),
        "cover_real": round(model.cover(lps), 3), "cover_shuffle_mean": round(sum(cps) / len(cps), 3), "cover_shuffle_max": round(max(cps), 3),
        "judge": J.judge(spec, "\n".join(dps_all)),
    }
    open(os.path.join(HERE, "ps_decode_vs_groen.txt"), "w").write(
        "\n".join(f"{ln}\t{''.join(dec_tok(t, kf)[0] for t in ps[ln])}\t{g}" for ln, g in GROEN.items()) + "\n")
    # ---- step 2: body under each key vs 20 shuffled keys
    for name, p in KEYS.items():
        key = read_key(p)
        dec, cls = body_decode(key, runs)
        txt = "\n".join(dec); letters = J.fold(txt)
        sc = model.score(letters); cv = model.cover(letters)
        ssc = []; scv = []
        for s in range(1, NSHUF + 1):
            d2, _ = body_decode(shuffled(key, s), runs); l2 = J.fold("\n".join(d2))
            ssc.append(model.score(l2)); scv.append(model.cover(l2))
        open(os.path.join(HERE, f"body_{name}.txt"), "w").write(txt + "\n")
        jd = J.judge(spec, txt)
        res[f"step2_body_{name}"] = {
            "token_classes": cls, "letters": len(letters),
            "lm_real": round(sc, 3), "lm_shuffle_mean": round(sum(ssc) / len(ssc), 3), "lm_shuffle_max": round(max(ssc), 3),
            "cover_real": round(cv, 3), "cover_shuffle_mean": round(sum(scv) / len(scv), 3), "cover_shuffle_max": round(max(scv), 3),
            "judge": jd,
        }
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1)
    print(json.dumps(res, indent=1))

if __name__ == "__main__":
    main()

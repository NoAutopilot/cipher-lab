#!/usr/bin/env python3
"""test5_rate_claims.py -- score two published McCormick token readings through tools/judge_plaintext.py.

FT4-mccormick-1999 (account-4), 3 Oct 2026. Rule 10: these are other people's readings; we only score them.
  Tsuchimoto, M. (26 Jan 2026), "Research Paper: Structural Solution of the Ricky McCormick Notes", Zenodo,
    https://doi.org/10.5281/zenodo.18375728 -- section 3 table (6 rows) plus the "V-Removal" operator.
  Sadak, S. (Jun 2026), "Forensic Manuscript Volume VI", Zenodo, https://doi.org/10.5281/zenodo.20767125 --
    Case 2, one line (note 2 line 10) rendered "36 MILES 74 SPRING PARK 29 BLOCKS 175 ROUTE TRAFFIC".
Both glosses are typed here from the papers' text (ciphers/mccormick-1999/second-opinions/*.txt); no code copied.

Variants, each applied to both notes (spec transcription) and to K letter-shuffled copies of them (shuffled-target
control: letters permuted within each note, separators kept, so which substrings occur -- hence coverage and the
judge score -- CAN differ from the target; a token-order shuffle could not, CLAUDE.md rule 3, bCAS):
  T-tok  Tsuchimoto, whole-token match only (tokens split as token_anneal.py does)
  T-sub  Tsuchimoto, substring match, longest key first, after V-removal
  S-sub  Sadak's four glosses, substring match
Line level: Sadak's own rendered line vs placebo lines (same digits, the four gloss slots filled with random corpus
words of the same lengths) through a length-free copy of the judge block -- tests whether the judge can tell his
hand-chosen gloss from any hand-chosen English words at all.
Corpora: default `en` (unknown reliability, tools/data/en/README.md) and an American-vernacular pair (Huck Finn +
Gatsby, tools/data/en/) as the nearest on disk to 1999 US vernacular; no 1999-era corpus exists in tools/data.
Writes test5_result.json beside this file. Offline.
"""
import json, os, random, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SPEC = os.path.join(ROOT, "specs", "mccormick-1999.json")
JUDGE = os.path.join(ROOT, "tools", "judge_plaintext.py")
K = 20
TSU = {"PNSE": "PREDNISONE", "NSE": "SEREVENT", "SE": "SEREVENT", "ALPM": "ALPRAZOLAM", "ALPRM": "ALPRAZOLAM",
       "OLPLM": "OLANZAPINE", "WBT": "WELLBUTRIN", "ACDN": "ACETAMINOPHEN CODEINE"}
SAD = {"MLSE": "MILES", "SPRKSE": "SPRING PARK", "KCNOB": "BLOCKS", "RTRSE": "ROUTE TRAFFIC"}
SAD_LINE = "36 MILES 74 SPRING PARK 29 BLOCKS 175 ROUTE TRAFFIC"
CORPORA = {"en": None, "en_us_vern": ["tools/data/en/pg76_huckfinn.txt", "tools/data/en/pg64317_gatsby.txt"]}


def notes():
    d = json.load(open(SPEC))
    return ["\n".join(d["ciphertext"]["note_1"]), "\n".join(d["ciphertext"]["note_2"])]


def tok_sub(text, table):
    def rep(m):
        return table.get(m.group(0).upper(), m.group(0))
    return re.sub(r"[A-Za-z]+", rep, text)


def str_sub(text, table, drop_v=False):
    if drop_v:
        text = text.replace("V", "")
    keys = sorted(table, key=len, reverse=True)
    pat = re.compile("|".join(map(re.escape, keys)))
    return pat.sub(lambda m: " " + table[m.group(0)].lower() + " ", text)


def coverage(src, table, whole):
    toks = re.findall(r"[A-Za-z]+", src)
    letters = sum(len(t) for t in toks)
    if whole:
        hit = sum(len(t) for t in toks if t.upper() in table)
    else:
        keys = sorted(table, key=len, reverse=True)
        pat = re.compile("|".join(map(re.escape, keys)))
        hit = sum(len(m.group(0)) for m in pat.finditer(src))
    return hit / letters


def shuffle_letters(text, rng):
    letters = [c for c in text if c.isalpha()]
    rng.shuffle(letters)
    it = iter(letters)
    return "".join(next(it) if c.isalpha() else c for c in text)


def judge(text, spec_path):
    p = subprocess.run([sys.executable, JUDGE, spec_path, "--text", text, "--json"], capture_output=True, text=True)
    return json.loads(p.stdout)


def spec_variant(corpus, length_free):
    d = json.load(open(SPEC))
    j = d["judge"]
    if CORPORA[corpus]:
        j.pop("language", None)
        j["corpora"] = [os.path.join(ROOT, c) for c in CORPORA[corpus]]
    if length_free:
        for k in ("letters_min", "letters_max"):
            j.pop(k, None)
    path = os.path.join(HERE, f".tmp_spec_{corpus}_{int(length_free)}.json")
    json.dump(d, open(path, "w"))
    return path


def summ(r):
    c = r["checks"]
    lang = c.get("language", {})
    return {"pass": r["pass"], "letters": c.get("length", {}).get("got", lang.get("N")), "score": lang.get("score"),
            "null_p99": lang.get("null_p99"), "real_p05": lang.get("real_p05"),
            "lang_pass": lang.get("pass"), "word_cover": c.get("words", {}).get("cover")}


def main():
    rng = random.Random(1999)
    src = notes()
    full = "\n".join(src)
    variants = {
        "T-tok": (lambda t: tok_sub(t, TSU), TSU, True),
        "T-sub": (lambda t: str_sub(t, TSU, drop_v=True), TSU, False),
        "S-sub": (lambda t: str_sub(t, SAD), SAD, False),
    }
    shuffles = ["\n".join(shuffle_letters(n, rng) for n in src) for _ in range(K)]
    out = {"K": K, "seed": 1999, "variants": {}, "line": {}}
    for corpus in CORPORA:
        sp = spec_variant(corpus, False)
        base = summ(judge(full, sp))
        out.setdefault("unglossed_ciphertext", {})[corpus] = base
        for name, (fn, table, whole) in variants.items():
            tgt = summ(judge(fn(full), sp))
            tgt["coverage"] = round(coverage(full, table, whole), 4)
            ctl = []
            for s in shuffles:
                r = summ(judge(fn(s), sp))
                r["coverage"] = round(coverage(s, table, whole), 4)
                ctl.append(r)
            sc = sorted(x["score"] for x in ctl)
            cv = sorted(x["coverage"] for x in ctl)
            out["variants"].setdefault(name, {})[corpus] = {
                "target": tgt, "shuffled_target_scores_min_med_max": [sc[0], sc[K // 2], sc[-1]],
                "shuffled_target_pass_count": sum(x["pass"] for x in ctl),
                "shuffled_target_coverage_min_med_max": [cv[0], cv[K // 2], cv[-1]],
                "target_score_rank_among_shuffles": sum(s < tgt["score"] for s in sc)}
        # line level
        spl = spec_variant(corpus, True)
        words = [w for w in re.findall(r"[a-z]+", open(os.path.join(ROOT, "tools/data/en/pg64317_gatsby.txt"),
                 encoding="utf-8", errors="ignore").read().lower())]
        bylen = {}
        for w in words:
            bylen.setdefault(len(w), []).append(w)
        sad = summ(judge(SAD_LINE, spl))
        plac = []
        for _ in range(K):
            line = "36 %s 74 %s %s 29 %s 175 %s %s" % tuple(rng.choice(bylen[n]) for n in (5, 6, 4, 6, 5, 7))
            plac.append(summ(judge(line, spl)))
        ps = sorted(x["score"] for x in plac)
        ref = summ(judge("he said he would meet us at the spring by the park", spl))
        out["line"][corpus] = {"sadak_line": sad, "placebo_scores_min_med_max": [ps[0], ps[K // 2], ps[-1]],
                               "placebo_pass_count": sum(x["pass"] for x in plac),
                               "plain_english_reference_same_length": ref}
        for p in (sp, spl):
            os.remove(p)
    json.dump(out, open(os.path.join(HERE, "test5_result.json"), "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()

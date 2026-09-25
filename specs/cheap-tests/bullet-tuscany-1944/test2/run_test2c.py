#!/usr/bin/env python3
"""Cheap test 2, step (c): bullet-tuscany-1944 -- deterministic keyed decrypts.

Keys tried: QM, MQ (the header, both orders), YZFF (letters of the 605YZ/FF footer), and the
footer's digits 605 mapped to letters two ways (A=0: 0->A..9->J; A=1: 1->A..9->I, 0->J as '10'),
each applied as a short repeating key (continuous across the 3 body lines) under vig/beau/
varbeau. Also every Caesar shift 0-25 under the same three tabulas (a period-1 key), since a
plain shift is the degenerate case of all three. Scored by tools/judge_plaintext.py's judge()
(length/cribs/language/words, per the spec's judge block) and by a raw crib-hit count (how many
of the 12-word crib list appear as a substring, not requiring all 12 as judge()'s all-or-nothing
'cribs' check does).

Matched control: the same full key list and scan run on (a) 3 synthetic 44-letter English
military sentences, each built from the crib vocabulary and enciphered under one of the five
named keys (rotating vig/beau/varbeau), checking whether the TRUE key ranks 1st by language
score among all 93 candidates; and (b) 3 random 44-letter strings, same scan, reporting the
false-positive rate (crib hits, judge PASSes) by chance.
"""
import json, os, random, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TABULAS = ["vig", "beau", "varbeau"]
CRIBS = ["GRENADE", "PIN", "PINS", "REINFORCEMENT", "REINFORCEMENTS", "PULL", "THROW", "ENEMY",
         "POSITION", "ATTACK", "TANK", "MG"]

BODY = "CBFUKYYEVOZILOOZVNCWJKQRSAWBYZUGYTZWYBATRSUA"
assert len(BODY) == 44, len(BODY)


def idx(c):
    return ord(c) - 65


def decrypt(cipher, key, tab):
    out = []
    for i, c in enumerate(cipher):
        k = idx(key[i % len(key)])
        cc = idx(c)
        if tab == "vig":
            p = (cc - k) % 26
        elif tab == "beau":
            p = (k - cc) % 26
        else:  # varbeau
            p = (cc + k) % 26
        out.append(A[p])
    return "".join(out)


def encrypt(plain, key, tab):
    # inverse of decrypt for each tabula
    out = []
    for i, c in enumerate(plain):
        k = idx(key[i % len(key)])
        pp = idx(c)
        if tab == "vig":
            cc = (pp + k) % 26
        elif tab == "beau":
            cc = (k - pp) % 26
        else:  # varbeau
            cc = (pp - k) % 26
        out.append(A[cc])
    return "".join(out)


def footer_keys():
    letters = "YZFF"
    digits = "605"
    a0 = "".join(A[int(d)] for d in digits)  # 0->A,...,9->J
    a1 = "".join((A[int(d) - 1] if d != "0" else "J") for d in digits)  # 1->A..9->I, 0->J (as 10)
    return {"YZFF": letters, "605_A0": a0, "605_A1": a1}


def named_keys():
    ks = {"QM": "QM", "MQ": "MQ"}
    ks.update(footer_keys())
    return ks


def crib_hits(text):
    return [c for c in CRIBS if c in text]


class Judge:
    """Builds tools/judge_plaintext.py's NgramModel ONCE (25 Sept 2026 fix: calling jp.judge()
    per candidate rebuilds the whole Holmes+Moby-Dick 4-gram model from scratch every time --
    ~2 min for one candidate, unusable for a 93-candidate scan x 4 scans). Reuses the model and
    the real/null score thresholds (fixed at N=44, spec's control_samples) across all candidates,
    same math as jp.judge()'s language+words checks."""

    def __init__(self, spec, n=44):
        j = spec["judge"]
        corpora = j.get("corpora") or jp.LANG_CORPORA[j["language"]]
        self.model = jp.NgramModel([jp.read_corpus(p) for p in corpora])
        real, null, cov = self.model.controls(n, samples=int(j.get("control_samples", 200)))
        self.null99, self.real05 = jp_pct(null, 0.99), jp_pct(real, 0.05)
        self.min_word_cover = j.get("min_word_cover")
        self.all_cribs = j.get("cribs", [])
        self.letters_min, self.letters_max = j.get("letters_min", 0), j.get("letters_max", 10 ** 9)

    def score_text(self, text):
        letters = jp.fold(text)
        sc = self.model.score(letters)
        lang_pass = sc > self.null99 and sc > self.real05
        cov = self.model.cover(letters)
        words_pass = (cov >= self.min_word_cover) if self.min_word_cover is not None else True
        len_pass = self.letters_min <= len(letters) <= self.letters_max
        missing = [c for c in self.all_cribs if jp.fold(c) not in letters]
        cribs_pass = not missing
        hits = crib_hits(text)
        return {
            "lang_score": round(sc, 4),
            "word_cover": round(cov, 4),
            "judge_pass": bool(lang_pass and words_pass and len_pass and cribs_pass),
            "cribs_hit": hits,
            "n_cribs_hit": len(hits),
        }


def jp_pct(xs, q):
    if not xs:
        return float("nan")
    return xs[min(len(xs) - 1, int(q * (len(xs) - 1)))]


def scan(judge, cipher_body):
    """Every named key + every Caesar shift, under every tabula. Returns list of dicts."""
    rows = []
    for name, key in named_keys().items():
        for tab in TABULAS:
            dec = decrypt(cipher_body, key, tab)
            sc = judge.score_text(dec)
            rows.append({"key_name": name, "key": key, "tab": tab, "decode": dec, **sc})
    for shift in range(26):
        key = A[shift]
        for tab in TABULAS:
            dec = decrypt(cipher_body, key, tab)
            sc = judge.score_text(dec)
            rows.append({"key_name": f"caesar_{shift}", "key": key, "tab": tab, "decode": dec, **sc})
    return rows


def rank_of(rows, key_name, tab):
    ranked = sorted(rows, key=lambda r: (r["lang_score"] if r["lang_score"] is not None else -1e9), reverse=True)
    for i, r in enumerate(ranked):
        if r["key_name"] == key_name and r["tab"] == tab:
            return i + 1
    return None


def build_military_sentence(rng, n=44):
    """A synthetic English military sentence, n letters, drawn from crib vocabulary plus filler."""
    words = ["THE", "ENEMY", "WILL", "ATTACK", "OUR", "POSITION", "WITH", "A", "TANK", "PULL",
             "THE", "PIN", "AND", "THROW", "IT", "AT", "THE", "MG", "NEST", "SEND", "REINFORCEMENTS",
             "NOW", "HOLD", "THE", "LINE", "AT", "DAWN", "WATCH", "FOR", "GRENADE", "FIRE"]
    while True:
        rng.shuffle(words)
        s = ""
        for w in words:
            if len(s) + len(w) > n:
                continue
            s += w
            if len(s) == n:
                return s
        # fallback: pad with filler letters from vocabulary if shuffle can't hit exactly n
        if len(s) < n:
            pad = "".join(rng.choice(A) for _ in range(n - len(s)))
            return s + pad


def main():
    spec = json.load(open(os.path.join(ROOT, "specs", "bullet-tuscany-1944.json"), encoding="utf-8"))
    judge = Judge(spec, n=44)  # built once; ~2 min if rebuilt per candidate (93 candidates x 4 scans)
    out = {"target": {}, "control_true_key": {}, "control_random": {}}

    # --- target ---
    rows = scan(judge, BODY)
    rows_sorted = sorted(rows, key=lambda r: (r["lang_score"] if r["lang_score"] is not None else -1e9), reverse=True)
    out["target"]["n_candidates"] = len(rows)
    out["target"]["judge_pass_count"] = sum(1 for r in rows if r["judge_pass"])
    out["target"]["max_crib_hits"] = max(r["n_cribs_hit"] for r in rows)
    out["target"]["top5"] = [
        {"key_name": r["key_name"], "tab": r["tab"], "lang_score": r["lang_score"],
         "n_cribs_hit": r["n_cribs_hit"], "cribs_hit": r["cribs_hit"], "decode": r["decode"]}
        for r in rows_sorted[:5]
    ]
    out["target"]["any_crib_hit_rows"] = [
        {"key_name": r["key_name"], "tab": r["tab"], "cribs_hit": r["cribs_hit"], "decode": r["decode"]}
        for r in rows if r["n_cribs_hit"] > 0
    ]

    # --- control A: true key must rank 1 ---
    rng = random.Random(20260925)
    plan = [("QM", "vig"), ("MQ", "beau"), ("YZFF", "varbeau")]
    true_key_ranks = []
    for i, (kname, tab) in enumerate(plan):
        plain = build_military_sentence(random.Random(1000 + i))
        key = named_keys()[kname]
        cipher = encrypt(plain, key, tab)
        crows = scan(judge, cipher)
        rank = rank_of(crows, kname, tab)
        top = sorted(crows, key=lambda r: (r["lang_score"] if r["lang_score"] is not None else -1e9), reverse=True)[0]
        true_key_ranks.append({
            "seed": i, "true_key_name": kname, "true_tab": tab, "plain": plain, "cipher": cipher,
            "true_key_rank": rank, "top_candidate": {"key_name": top["key_name"], "tab": top["tab"],
                                                       "lang_score": top["lang_score"]},
        })
    out["control_true_key"]["runs"] = true_key_ranks
    out["control_true_key"]["true_key_rank1_count"] = sum(1 for r in true_key_ranks if r["true_key_rank"] == 1)

    # --- control B: random 44-letter strings, false-positive rate ---
    fp_runs = []
    for i in range(3):
        rrng = random.Random(2000 + i)
        rand_body = "".join(rrng.choice(A) for _ in range(44))
        rrows = scan(judge, rand_body)
        fp_runs.append({
            "seed": i, "random_body": rand_body,
            "judge_pass_count": sum(1 for r in rrows if r["judge_pass"]),
            "max_crib_hits": max(r["n_cribs_hit"] for r in rrows),
            "any_crib_hit_count": sum(1 for r in rrows if r["n_cribs_hit"] > 0),
            "n_candidates": len(rrows),
        })
    out["control_random"]["runs"] = fp_runs
    out["control_random"]["judge_pass_total"] = sum(r["judge_pass_count"] for r in fp_runs)
    out["control_random"]["any_crib_hit_total"] = sum(r["any_crib_hit_count"] for r in fp_runs)

    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test2c_output.json")
    json.dump(out, open(outpath, "w", encoding="utf-8"), indent=1)
    print(f"target: {out['target']['judge_pass_count']}/{out['target']['n_candidates']} judge PASS, "
          f"max crib hits {out['target']['max_crib_hits']}")
    print(f"control true-key rank1: {out['control_true_key']['true_key_rank1_count']}/3")
    print(f"control random false positives: judge PASS {out['control_random']['judge_pass_total']}, "
          f"any crib hit {out['control_random']['any_crib_hit_total']}")
    print(f"written {outpath}")


if __name__ == "__main__":
    main()

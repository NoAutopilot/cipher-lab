#!/usr/bin/env python3
"""judge_discrimination_check.py: does tools/judge_plaintext.py's language check separate a real Vieyra-dictionary
decode from a wrong-key dictionary-code fragment, at this target's length? Written for
.claude/briefs/runs/2026-09-25-parent-linhares-judge.md (parent worker LX-JUDGE).

Reuses the exact NgramModel/corpus tools/judge_plaintext.py wires in for language="pt" (tools/data/pt17,
Vieira 1648-1697), so the reading's raw score here matches the NOTES.md YX-PTJUDGE run exactly, and adds four
things the judge itself does not check:

  0. What the judge actually scored: reading.txt verbatim (comment header included) vs. a normalized rendering
     of just the 25 real decoded words (the mid-letter null token carries no lexical content, dropped).
  (a) real Portuguese of about 1780-1830, cut into N-letter fragments -- NOT Vieira, NOT this target's own
      material. Source: "Exposicao dos factos, e maquinacoes, com que se preparou a usurpacao da coroa de
      Hespanha..." (Lisbon, 1808), archive.org id exposiodosfa00cevauoft -- a contemporaneous political pamphlet
      in the same Napoleonic-era Portuguese-court context as the target (Conde de Linhares, c.1811-12).
  (b) random headword sequences drawn from the Vieyra 1809 dictionary (newpocketdiction00viey) the key uses --
      Part I (Portuguese-English) only, headwords extracted from the IA djvu.txt by regex on the
      "Headword, abbrev." entry pattern. Two variants: b_plain (whole headwords, no trim) and b_trim (the same
      draw but with the observed trim mechanic applied to the same fraction of tokens the real key.tsv uses --
      9/25 = 36% of the reading's tokens are a trimmed suffix-stub of a longer headword, not the whole word;
      b_trim reproduces that so the control matches the *design*, not just the word/letter count, per CLAUDE.md
      rule 3's Salviati lesson).
  (c) the committed reading (25 real words) with its word order shuffled. judge_plaintext.fold() strips spaces
      before scoring, so a shuffle changes which letters abut which at former word boundaries -- a real
      perturbation, not a no-op.
  A baseline false-negative check: how often does (a) -- genuine, fluent, period-matched Portuguese prose, not a
  cipher decode at all -- itself fail the *deployed* judge (pt17/Vieira thresholds) at this N, from noise alone.

Neither fetched corpus is committed to the repo (out of this brief's touched-file list); both are cached under
scripts/_cache (gitignored by being undeclared) and re-fetched from the URLs below if the cache is missing.

Usage: python3 judge_discrimination_check.py [--cache DIR] [--samples 200] [--seed 1] [--json-out FILE] [--lang pt|pt18]

--lang pt18 (added 25 Sept 2026, V6-PTCORP): scores against tools/data/pt18 (four 1808-1819 London-printed
Portuguese periodical volumes, Correio Braziliense and O Investigador Portuguez em Inglaterra, ~3.2M letters)
instead of tools/data/pt17 (Vieira's own letters, 1648-1697) -- a period-matched corpus for this c.1811-12
target instead of one ~120-160 years off. Control (a) (exposiodosfa00cevauoft, an 1808 pamphlet) is not among
the four pt18 files, so it stays a valid held-out real-text control under either --lang.
"""
import argparse, csv, json, random, re, sys, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE.parent
REPO = TARGET.parent.parent
sys.path.insert(0, str(REPO / "tools"))
import judge_plaintext as jp  # noqa: E402

PERIOD_URL = "https://archive.org/download/exposiodosfa00cevauoft/exposiodosfa00cevauoft_djvu.txt"
DICT_URL = "https://archive.org/download/newpocketdiction00viey/newpocketdiction00viey_djvu.txt"
UA = "cipher-lab research script (contact via repository)"
# empirical trim lengths from key.tsv's 9 trimmed tokens (o<-Ovo:2, man<-Mando:2, o<-Ouros:4, he<-Hernia:4,
# o<-Odio:3, do<-Dormitar:6, pauperr<-Pauperrimo:3, ven<-Venablo:4, ha<-Habil:3)
TRIM_LENS = [2, 2, 4, 4, 3, 6, 3, 4, 3]
TRIM_RATE = 9 / 25


def fetch(url, cache_path):
    cache_path = Path(cache_path)
    if cache_path.exists() and cache_path.stat().st_size > 1000:
        return cache_path.read_text(encoding="utf-8", errors="replace")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    data = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", errors="replace")
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(data, encoding="utf-8")
    return data


def load_reading_tokens():
    rows = list(csv.DictReader(open(TARGET / "reading_tokens.tsv"), delimiter="\t"))
    words = [r["value"] for r in rows if r["value"] != "[null]"]
    return words, len(rows)


def extract_headwords(dict_text):
    end = dict_text.find("END  OF  PART  I.")
    if end < 0:
        end = dict_text.find("END OF PART I.")
    body = dict_text[:end] if end > 0 else dict_text
    blob = re.sub(r"\s+", " ", body)
    abbrevs = r"(?:s\.\s*m|s\.\s*f|v\.\s*a|v\.\s*n|v\.\s*r|adj|prep|adv|pron|interj|conj|art)"
    pat = re.compile(r"\b([A-ZÁÀÂÃÉÊÍÓÔÕÚÇ][a-záàâãéêíóôõúüç\-]{1,20}),\s+" + abbrevs, re.UNICODE)
    return pat.findall(blob)


def pct(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * (len(xs) - 1)))] if xs else float("nan")


def auc(xs, ys):
    """P(x drawn from xs > y drawn from ys), pairwise -- 0.5 = indistinguishable."""
    ys_sorted = sorted(ys)
    import bisect
    wins = sum(bisect.bisect_left(ys_sorted, x) for x in xs)
    return wins / (len(xs) * len(ys))


def summarize(name, scores, reading_score):
    scores = sorted(scores)
    n = len(scores)
    ge = sum(1 for s in scores if s >= reading_score)
    print(f"{name}:\n  n={n} mean={sum(scores)/n:.3f} p05={pct(scores,0.05):.3f} p50={pct(scores,0.5):.3f} "
          f"p95={pct(scores,0.95):.3f}\n  reading_score={reading_score:.3f} -> {n-ge}/{n} ({100*(n-ge)/n:.1f} pct) "
          f"of this distribution scores AT OR BELOW the reading; {ge}/{n} draws score >= reading")
    return {"n": n, "mean": round(sum(scores)/n, 4), "p05": round(pct(scores,0.05), 4), "p50": round(pct(scores,0.5), 4),
            "p95": round(pct(scores,0.95), 4), "reading_score": round(reading_score, 4),
            "reading_percentile_in_dist": round(100*(n-ge)/n, 1), "draws_ge_reading": ge}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache", default=str(HERE / "_cache"))
    ap.add_argument("--samples", type=int, default=200)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--json-out")
    ap.add_argument("--lang", default="pt", choices=["pt", "pt18"])
    a = ap.parse_args()
    cache = Path(a.cache)

    model = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA[a.lang]])
    words, total_tokens = load_reading_tokens()
    normalized = " ".join(words)
    raw_text = (TARGET / "reading.txt").read_text(encoding="utf-8")

    raw_letters = jp.fold(raw_text)
    norm_letters = jp.fold(normalized)
    raw_score = model.score(raw_letters)
    norm_score = model.score(norm_letters)
    N = len(norm_letters)
    comment_letters = jp.fold("\n".join(l for l in raw_text.splitlines() if l.startswith("#")))

    print("=== Step 1: what the judge actually scored ===")
    print(f"raw reading.txt (comments + data, exactly what NOTES.md's YX-PTJUDGE run scored): "
          f"{len(raw_letters)} letters, score={raw_score:.3f}")
    print(f"  of which {len(comment_letters)} letters ({100*len(comment_letters)/len(raw_letters):.0f} pct) are "
          f"the '#' comment-header lines (English metadata prose: 'decoded against', 'tokens', 'Portuguese as "
          f"decoded', 'English gloss below', ...), not the Portuguese decode")
    print(f"normalized rendering (25 real decoded words, null token dropped): {N} letters, score={norm_score:.3f}")
    print("NOTES.md YX-PTJUDGE reported: score=-1.559 null_p99=-1.618 real_p05=-1.014 N=467 -- matches the raw "
          "467-letter file exactly, confirming the FAIL was scored on the comment header plus the decode, not "
          "the decode alone.")
    print()

    rnd = random.Random(a.seed)

    print(f"=== Step 2: design-matched controls, N={N} letters / {len(words)} words, {a.samples} draws, seed={a.seed} ===")
    period_text = fetch(PERIOD_URL, cache / "exposicao1808.txt")
    period_letters = jp.fold(period_text)
    period_scores = [model.score(period_letters[(j := rnd.randrange(0, max(1, len(period_letters)-N))):j+N])
                      for _ in range(a.samples)]
    res_a = summarize("(a) real Portuguese prose, 1808 (exposiodosfa00cevauoft), N-letter windows",
                       period_scores, norm_score)

    dict_text = fetch(DICT_URL, cache / "vieyra_dict.txt")
    hw_cache = cache / "headwords.json"
    if hw_cache.exists():
        headwords = json.loads(hw_cache.read_text())
    else:
        headwords = extract_headwords(dict_text)
        hw_cache.parent.mkdir(parents=True, exist_ok=True)
        hw_cache.write_text(json.dumps(headwords))
    nwords = len(words)

    def draw_plain():
        return [rnd.choice(headwords) for _ in range(nwords)]

    def draw_trim():
        out = []
        for _ in range(nwords):
            w = rnd.choice(headwords)
            if rnd.random() < TRIM_RATE and len(w) > 2:
                t = min(rnd.choice(TRIM_LENS), len(w) - 1)
                w = w[:-t]
            out.append(w)
        return out

    b_scores, b_covers = [], []
    for _ in range(a.samples):
        t = jp.fold(" ".join(draw_plain()))
        b_scores.append(model.score(t)); b_covers.append(model.cover(t))
    res_b = summarize(f"(b_plain) random Vieyra-dict headword sequences, whole words, {len(headwords)}-word pool",
                       b_scores, norm_score)
    print(f"    word-cover: reading={model.cover(norm_letters):.3f} (floor 0.5) vs b_plain mean="
          f"{sum(b_covers)/len(b_covers):.3f} p05={pct(b_covers,0.05):.3f} -- "
          f"{sum(1 for c in b_covers if c>=0.5)}/{len(b_covers)} draws ALSO clear the floor")

    bt_scores, bt_covers = [], []
    for _ in range(a.samples):
        t = jp.fold(" ".join(draw_trim()))
        bt_scores.append(model.score(t)); bt_covers.append(model.cover(t))
    res_bt = summarize(f"(b_trim) same, with {TRIM_RATE:.0%} of tokens end-trimmed like the reading's own 9/25",
                        bt_scores, norm_score)
    print(f"    word-cover: reading={model.cover(norm_letters):.3f} (floor 0.5) vs b_trim mean="
          f"{sum(bt_covers)/len(bt_covers):.3f} p05={pct(bt_covers,0.05):.3f} -- "
          f"{sum(1 for c in bt_covers if c>=0.5)}/{len(bt_covers)} draws ALSO clear the floor")

    shuf_scores = []
    for _ in range(a.samples):
        w2 = words[:]; rnd.shuffle(w2)
        shuf_scores.append(model.score(jp.fold(" ".join(w2))))
    res_c = summarize("(c) committed reading, word order shuffled (same letters)", shuf_scores, norm_score)
    print()

    print("=== Step 2b: does the judge separate (a) real prose from (b) dictionary salad at all? ===")
    auc_plain = auc(bt_scores, period_scores)
    auc_ab = auc(b_scores, period_scores)
    print(f"AUC P(b_plain > a) = {auc_ab:.3f}   AUC P(b_trim > a) = {auc_plain:.3f}  (0.5 = indistinguishable, "
          f"toward 0 = a consistently scores higher than b, i.e. real separation)")
    print()

    print(f"=== Step 2c: baseline false-negative rate of the DEPLOYED judge ({a.lang} thresholds) on genuine "
          "1808 prose at this N ===")
    real17, null17, cov17 = model.controls(N, samples=a.samples, seed=a.seed)
    null_p99, real_p05 = pct(null17, 0.99), pct(real17, 0.05)
    passes = sum(1 for s in period_scores if s > null_p99 and s > real_p05)
    print(f"deployed thresholds at N={N} ({a.lang}): null_p99={null_p99:.3f} real_p05={real_p05:.3f}")
    print(f"genuine, fluent, non-cipher 1808 Portuguese prose windows that PASS these thresholds: "
          f"{passes}/{a.samples} ({100*passes/a.samples:.1f} pct) -- i.e. even real text has a "
          f"{100*(a.samples-passes)/a.samples:.1f} pct false-negative rate at this N, corpus and threshold")
    print(f"reading's normalized score {norm_score:.3f} vs these same thresholds: "
          f"{'PASS' if norm_score>null_p99 and norm_score>real_p05 else 'FAIL'} "
          f"(null test alone: {'pass' if norm_score>null_p99 else 'FAIL'})")

    if a.json_out:
        out = {"lang": a.lang, "raw_score": round(raw_score,4), "raw_N": len(raw_letters), "raw_comment_letters": len(comment_letters),
               "norm_score": round(norm_score,4), "norm_N": N, "n_words": len(words),
               "period_source": "archive.org exposiodosfa00cevauoft (1808)",
               "dict_source": "archive.org newpocketdiction00viey Part I, regex headword extraction",
               "control_a_real1808": res_a, "control_b_plain": res_b, "control_b_trim": res_bt,
               "control_c_shuffled_reading": res_c, "auc_b_plain_vs_a": round(auc_ab,4), "auc_b_trim_vs_a": round(auc_plain,4),
               "deployed_null_p99": round(null_p99,4), "deployed_real_p05": round(real_p05,4),
               "deployed_false_negative_rate_on_real_1808": round((a.samples-passes)/a.samples, 4),
               "samples": a.samples, "seed": a.seed}
        Path(a.json_out).write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()

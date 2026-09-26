#!/usr/bin/env python3
"""ARM-A2: direct transfer of every published sibling table (tools/data/uscodes-1800/*.tsv) to the
20 Feb 1808 Armstrong-Madison target, against a structure-preserving shuffled-table control and a
shuffled-order-of-target control (CLAUDE.md rule 3: both controls CAN differ from the target,
per this job's own brief). Offline, seeded, no network.

For each table T:
  1. Positive control (round-trip sanity check, not a cryptanalytic claim): if a decode file in
     tools/data/uscodes-1800/decodes/ exists for T's own correspondence, extract its resolved words,
     re-encode them under T (word -> value, seeded choice among homophones), decode that synthetic
     ciphertext with T, report coverage and the judge verdict on the round-tripped text. If no such
     decode exists (WE028: no Monroe-side decode file on disk), say so and skip.
  2. Target: decode the 20 Feb letter's 369 numeral groups with T (unresolved values kept as
     "{value}"), report token/distinct coverage, a word-bigram score under en18 (via a bigram model
     built directly from the en18 corpus files judge_plaintext.py already registers under
     LANG_CORPORA["en18"]; falls back to "en" if en18 is absent), and the judge verdict via
     tools/judge_plaintext.py on the decode text.
  3. Control A -- 200 tables built from T by permuting its plaintext column WITHIN alphabetical
     blocks of 20 consecutive values (sorted by value; keeps the one-part value range and block
     structure, destroys the value->word pairing). Same target token sequence decoded under each;
     report the target's percentile in that distribution of bigram scores.
     Control B (reverse) -- 200 shuffles of the target's own token ORDER, decoded with the real,
     unpermuted T; report the target's (real-order) percentile in that distribution.

Usage: python3 ciphers/armstrong-madison-1808/a2/transfer.py [--seed N] [--controls N]
"""
import argparse
import math
import random
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TARGET_DIR = ROOT / "ciphers" / "armstrong-madison-1808"
TABLES_DIR = ROOT / "tools" / "data" / "uscodes-1800"
sys.path.insert(0, str(ROOT / "tools"))
import judge_plaintext as jp  # noqa: E402

TABLES = ["WE028.tsv", "THE972_bourdeau.tsv", "THE972_tomokiyo_clean.tsv", "THE972_tomokiyo_partial.tsv"]
# T -> correspondence label -> decode file for the positive control (WE028's own correspondent, Monroe,
# has no decode file on disk; only Armstrong's THE=972 decodes exist, per uscodes-1800/README.md)
POSITIVE_DECODE = {
    "WE028.tsv": None,
    "THE972_bourdeau.tsv": "armstrong_1808-02-15.txt",
    "THE972_tomokiyo_clean.tsv": "armstrong_1808-02-15.txt",
    "THE972_tomokiyo_partial.tsv": "armstrong_1808-02-15.txt",
}
WORD_RE = re.compile(r"[A-Za-z]+")


def load_table(path):
    """value(int) -> word(str), in file order (== value-sorted for these tables, checked by caller)."""
    val2word = {}
    for line in path.read_text(encoding="utf-8").splitlines()[1:]:
        if not line.strip():
            continue
        value, plaintext, grade, source_line = line.split("\t", 3)
        val2word[int(value)] = plaintext
    return val2word


def word2vals(val2word):
    out = {}
    for v, w in val2word.items():
        out.setdefault(w.lower(), []).append(v)
    return out


def parse_ciphertext():
    text = (TARGET_DIR / "ciphertext.txt").read_text(encoding="utf-8")
    toks = []
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        toks.extend(line.split())
    return toks  # list of str: digit strings, '*', '**', '***', '<..>'


def decode_tokens(tokens, val2word):
    """-> (decoded_words_by_run, coverage_stats). A 'run' is a maximal span of consecutive
    resolved numeral tokens (a symbol/illegible/unresolved token breaks the run, per the brief's
    bigram-over-adjacent-decoded-words design)."""
    runs, cur = [], []
    covered_tokens = 0
    numeral_tokens = 0
    covered_values = set()
    distinct_values = set()
    for t in tokens:
        if t.isdigit():
            numeral_tokens += 1
            v = int(t)
            distinct_values.add(v)
            if v in val2word:
                covered_tokens += 1
                covered_values.add(v)
                cur.append(val2word[v].lower())
                continue
        if cur:
            runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)
    stats = {
        "numeral_tokens": numeral_tokens,
        "covered_tokens": covered_tokens,
        "distinct_values": len(distinct_values),
        "covered_distinct_values": len(covered_values),
    }
    return runs, stats


def decode_text(tokens, val2word):
    out = []
    for t in tokens:
        if t.isdigit():
            v = int(t)
            out.append(val2word.get(v, "{%d}" % v))
        else:
            out.append(t)
    return " ".join(out)


class WordBigram:
    def __init__(self, corpus_files, k=0.5):
        self.k = k
        words = []
        for p in corpus_files:
            words.extend(w.lower() for w in WORD_RE.findall(jp.read_corpus(p)))
        self.uni = Counter(words)
        self.bi = Counter(zip(words, words[1:]))
        self.V = len(self.uni)

    def logp(self, w1, w2):
        return math.log10((self.bi.get((w1, w2), 0) + self.k) / (self.uni.get(w1, 0) + self.k * self.V))

    def score(self, runs):
        total, n = 0.0, 0
        for run in runs:
            for i in range(len(run) - 1):
                total += self.logp(run[i], run[i + 1])
                n += 1
        return (total / n, n) if n else (None, 0)


def permute_table_within_blocks(val2word, block=20, seed=1):
    rnd = random.Random(seed)
    items = sorted(val2word.items())  # [(value, word), ...] ascending by value
    vals = [v for v, _ in items]
    words = [w for _, w in items]
    out_words = list(words)
    for i in range(0, len(words), block):
        chunk = list(range(i, min(i + block, len(words))))
        shuffled = [words[j] for j in chunk]
        rnd.shuffle(shuffled)
        for j, w in zip(chunk, shuffled):
            out_words[j] = w
    return dict(zip(vals, out_words))


def positive_control(table_name, val2word, w2v, bigram, spec):
    decode_name = POSITIVE_DECODE[table_name]
    if decode_name is None:
        return "no sibling decode letter on disk for this table's correspondence (WE028/Monroe) -- skipped, per brief item 1"
    raw = (TABLES_DIR / "decodes" / decode_name).read_text(encoding="utf-8")
    raw = "\n".join(l for l in raw.splitlines() if not l.strip().startswith("=="))
    known_words = [w.lower() for w in WORD_RE.findall(raw)]
    rnd = random.Random(7)
    encoded_vals, covered = [], 0
    for w in known_words:
        cands = w2v.get(w)
        if cands:
            encoded_vals.append(rnd.choice(cands))
            covered += 1
        else:
            encoded_vals.append(None)
    resolved_words = [val2word[v] for v in encoded_vals if v is not None]
    roundtrip_text = " ".join(resolved_words)
    cov = covered / len(known_words) if known_words else 0.0
    try:
        verdict = jp.judge(spec, roundtrip_text)
        v_str = "PASS" if verdict["pass"] else "FAIL"
    except Exception as e:  # pragma: no cover
        v_str = f"error({e})"
    return f"known_words={len(known_words)} coverage={cov:.3f} ({covered}/{len(known_words)}) roundtrip_judge={v_str}"


def run_table(table_name, spec, bigram, n_controls, seed):
    path = TABLES_DIR / table_name
    val2word = load_table(path)
    w2v = word2vals(val2word)
    tokens = parse_ciphertext()

    pos = positive_control(table_name, val2word, w2v, bigram, spec)

    runs, stats = decode_tokens(tokens, val2word)
    real_score, real_n = bigram.score(runs)
    dtext = decode_text(tokens, val2word)
    try:
        verdict = jp.judge(spec, dtext)
        v_str = "PASS" if verdict["pass"] else "FAIL"
        v_detail = verdict["checks"].get("language", {})
    except Exception as e:  # pragma: no cover
        v_str, v_detail = f"error({e})", {}

    # Control A: permute T's plaintext column within alphabetical (value-sorted) blocks of 20
    permA_scores = []
    for i in range(n_controls):
        pv2w = permute_table_within_blocks(val2word, block=20, seed=seed * 10000 + i)
        pruns, _ = decode_tokens(tokens, pv2w)
        s, n = bigram.score(pruns)
        if s is not None:
            permA_scores.append(s)
    permA_scores.sort()

    # Control B: shuffle the target's own token order, decode with the REAL table
    permB_scores = []
    rnd = random.Random(seed * 20000 + 1)
    for i in range(n_controls):
        shuffled = list(tokens)
        rnd.shuffle(shuffled)
        bruns, _ = decode_tokens(shuffled, val2word)
        s, n = bigram.score(bruns)
        if s is not None:
            permB_scores.append(s)
    permB_scores.sort()

    def percentile_of(real, dist):
        if real is None or not dist:
            return None
        below = sum(1 for x in dist if x <= real)
        return 100.0 * below / len(dist)

    pctA = percentile_of(real_score, permA_scores)
    pctB = percentile_of(real_score, permB_scores)

    salad = [t if not t.isdigit() else val2word.get(int(t), "{%s}" % t) for t in tokens[:30]]

    return {
        "table": table_name,
        "entries": len(val2word),
        "positive_control": pos,
        "coverage_tokens": f"{stats['covered_tokens']}/{stats['numeral_tokens']}",
        "coverage_distinct": f"{stats['covered_distinct_values']}/{stats['distinct_values']}",
        "bigram_score": real_score,
        "bigram_pairs": real_n,
        "pct_vs_permuted": pctA,
        "pct_vs_shuffled_order": pctB,
        "judge": v_str,
        "judge_detail": v_detail,
        "salad": " ".join(salad),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seed", type=int, default=26092026)
    ap.add_argument("--controls", type=int, default=200)
    a = ap.parse_args()

    spec = __import__("json").loads((ROOT / "specs" / "armstrong-madison-1808.json").read_text(encoding="utf-8"))
    lang = spec.get("judge", {}).get("language", "en18")
    corpora = jp.LANG_CORPORA.get(lang) or jp.LANG_CORPORA["en"]
    used_lang = lang if jp.LANG_CORPORA.get(lang) else "en (en18 absent)"
    bigram = WordBigram(corpora)

    print(f"# word-bigram model: {used_lang}, {len(bigram.uni)} word types, "
          f"{sum(bigram.uni.values())} tokens")
    for table_name in TABLES:
        r = run_table(table_name, spec, bigram, a.controls, a.seed)
        print(f"\n== {r['table']} ({r['entries']} entries) ==")
        print(f"positive control: {r['positive_control']}")
        print(f"target coverage: tokens {r['coverage_tokens']}, distinct {r['coverage_distinct']}")
        print(f"bigram score: {r['bigram_score']:.4f} over {r['bigram_pairs']} pairs" if r['bigram_score'] is not None else "bigram score: n/a (no adjacent covered pairs)")
        print(f"percentile vs 200 permuted-table controls: {r['pct_vs_permuted']}")
        print(f"percentile vs 200 shuffled-order controls: {r['pct_vs_shuffled_order']}")
        print(f"judge: {r['judge']} {r['judge_detail']}")
        print(f"salad (first 30 tokens, NOT a reading): {r['salad']}")


if __name__ == "__main__":
    main()

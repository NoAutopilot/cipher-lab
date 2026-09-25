#!/usr/bin/env python3
"""Matched control for the first cheap test (CLAUDE.md rule 3): same design as thurloe-barriere-1654 -- a
word-per-code nomenclature with homophones, sparse partial interlinear gloss, run structure copied token-for-
token from the real letter's passA.tsv (same N per run, same number of gloss-revealed words per run, taken as a
prefix) -- built over a fresh, unrelated chunk of real period French (tools/data/fr16) instead of the target's
own words. Ground truth is known here, so this reports coverage AND sense rate (rule 3: report both numbers).

Usage: python3 matched_control.py [--seed N]
"""
import argparse, gzip, random, re, sys, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CORPUS = os.path.join(REPO, 'tools/data/fr16/lettresindites00marg_djvu.txt.gz')
PASSA = os.path.join(HERE, 'passA.tsv')
KEYGLOSS = os.path.join(HERE, 'key_gloss.tsv')


def strip_mark(tok):
    return re.sub(r'[\*\^`\'´ˇ¨=]+$', '', tok)


def real_run_profile():
    """(run_id, n_tokens) for every run in passA.tsv, and k_gloss (count of key_gloss.tsv rows whose
    source_run is this run or a run merged into the same gloss group) for each."""
    runs = []
    with open(PASSA) as f:
        header = None
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            row = line.rstrip('\n').split('\t')
            if header is None:
                header = row
                continue
            d = dict(zip(header, row))
            runs.append((d['run_id'], len(d['tokens'].split())))
    counts = collections.Counter()
    with open(KEYGLOSS) as f:
        header = None
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            row = line.rstrip('\n').split('\t')
            if header is None:
                header = row
                continue
            d = dict(zip(header, row))
            counts[d['source_run']] += 1
    profile = []
    for run_id, n in runs:
        k = min(counts.get(run_id, 0), n)
        profile.append((run_id, n, k))
    return profile


def load_words(n_needed):
    text = gzip.open(CORPUS, 'rt', encoding='utf-8', errors='ignore').read()
    text = text[20000:20000 + 60000]
    words = re.findall(r"[A-Za-zÀ-ÿ']+", text.lower())
    words = [w for w in words if len(w) >= 1]
    if len(words) < n_needed:
        words = (words * (n_needed // len(words) + 1))
    return words[:n_needed]


def build_control(seed):
    rng = random.Random(seed)
    profile = real_run_profile()
    total_n = sum(n for _, n, _ in profile)
    words = load_words(total_n)

    freq = collections.Counter(words)
    top_words = [w for w, _ in freq.most_common(9)]  # mimic the real letter's ~9 heavily-reused function words

    code_pool = list(range(10, 99))
    rng.shuffle(code_pool)
    next_code = iter(code_pool)
    word_to_codes = {}
    for w in top_words:
        # 2-4 homophone codes per top word, same conflict-generating structure as the real pass
        n_hom = rng.choice([2, 3, 3, 4])
        word_to_codes[w] = [next(next_code) for _ in range(n_hom)]
    used_word_code = {}  # (word) -> the single code used at each occurrence position, chosen per-occurrence

    # Assign a code to every word occurrence in position order
    codes_at_pos = []
    for w in words:
        if w in word_to_codes:
            c = rng.choice(word_to_codes[w])
        else:
            if w not in used_word_code:
                used_word_code[w] = next(next_code, None) or rng.randint(100, 199)
            c = used_word_code[w]
        codes_at_pos.append(str(c))

    # Walk the run profile, slicing codes_at_pos / words in order; first k words of each run are "glossed"
    pos = 0
    key_rows = []   # (code, value, source_run)
    run_tokens = {}  # run_id -> list of codes
    run_truth = {}   # run_id -> list of true words
    for run_id, n, k in profile:
        toks = codes_at_pos[pos:pos + n]
        truth = words[pos:pos + n]
        run_tokens[run_id] = toks
        run_truth[run_id] = truth
        for i in range(k):
            key_rows.append((toks[i], truth[i], run_id))
        pos += n

    # Build primary (non-conflicting) key exactly as the real pass did
    code_values = collections.defaultdict(set)
    for code, value, _ in key_rows:
        code_values[code].add(value)
    primary_key = {c: next(iter(v)) for c, v in code_values.items() if len(v) == 1}

    # Apply to everything; compute coverage and sense rate against ground truth
    total_tokens = sum(len(t) for t in run_tokens.values())
    glossed_positions = set()
    p2 = 0
    for run_id, n, k in profile:
        for i in range(k):
            glossed_positions.add((run_id, i))
        p2 += n

    read = 0
    correct_new = 0
    new_covered = 0
    for run_id, n, k in profile:
        toks = run_tokens[run_id]
        truth = run_truth[run_id]
        for i, t in enumerate(toks):
            if t in primary_key:
                read += 1
                is_new = (run_id, i) not in glossed_positions
                if is_new:
                    new_covered += 1
                    if primary_key[t] == truth[i]:
                        correct_new += 1
    return dict(key_size=len(primary_key), total_tokens=total_tokens, read=read,
                new_covered=new_covered, correct_new=correct_new)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seeds', type=int, default=5)
    args = ap.parse_args()
    results = [build_control(seed) for seed in range(args.seeds)]
    for i, r in enumerate(results):
        cov = 100 * r['read'] / r['total_tokens']
        sense = 100 * r['correct_new'] / r['new_covered'] if r['new_covered'] else float('nan')
        print(f"seed {i}: key={r['key_size']} tokens={r['total_tokens']} read={r['read']} ({cov:.1f}%) "
              f"new_covered={r['new_covered']} correct_new={r['correct_new']} sense_rate={sense:.1f}%")
    avg_cov = sum(100 * r['read'] / r['total_tokens'] for r in results) / len(results)
    avg_sense = sum((100 * r['correct_new'] / r['new_covered'] if r['new_covered'] else 0) for r in results) / len(results)
    print(f"\naverage coverage over {args.seeds} seeds: {avg_cov:.1f}%")
    print(f"average sense rate (of newly-covered tokens, i.e. beyond the ones the gloss itself gave) over {args.seeds} seeds: {avg_sense:.1f}%")


if __name__ == '__main__':
    main()

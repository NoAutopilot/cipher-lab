#!/usr/bin/env python3
"""Matched control for the first cheap test (CLAUDE.md rule 3): same design as thurloe-barriere-1654 -- a
word-per-code nomenclature with homophones, sparse partial interlinear gloss, run structure copied token-for-
token from the real letter's ciphertext (same N per run, same number of gloss-revealed words per run, taken as a
prefix) -- built over a fresh, unrelated chunk of real period French (tools/data/fr16) instead of the target's
own words. Ground truth is known here, so this reports coverage AND sense rate (rule 3: report both numbers).

Usage: python3 matched_control.py [--seed N] [--ctpath passA.tsv|ciphertext.tsv]
Default --ctpath is passA.tsv (the original single-pass transcription), which reproduces TX-BARRT's 25 Sept 2026
numbers exactly (checked: 33.4% avg coverage over 10 seeds, unchanged). YX-BARB, 25 Sept 2026, added --ctpath so
the same control design can be rebuilt against ciphertext.tsv, the pass-A/pass-B reconciled transcription
(tools/reconcile_passes.py plus this worker's own image check -- see NOTES.md).

For ctpath != passA.tsv, k_gloss per run is NOT taken from that run's raw gloss_as_printed word count -- an
earlier version of this edit tried that and it roughly doubled the control's average key size (30 -> ~81-87),
because ciphertext.tsv's gloss field, unlike key_gloss.tsv, includes gloss text passA's own notes explicitly
flagged as NOT confidently mapped per token ("sparse/mismatched, no confident per-token mapping attempted") --
counting it as revealed gave the control a bigger, better key than the real pass actually built, exactly the
un-matched-design failure CLAUDE.md rule 3 warns against. Instead: the set of ciphertext.tsv token positions
counted as "glossed" is the ORIGINAL passA.tsv glossed-position set (first k tokens of each passA.tsv run, k from
key_gloss.tsv's source_run counts -- the same method the passA.tsv branch below uses) projected onto ciphertext.tsv
via the same Needleman-Wunsch alignment used to build ciphertext.tsv itself (see build script referenced in
NOTES.md), after stripping marks and normalizing symbol labels (Th/Ph -> [circle-dot]/[phi-symbol]) on both sides.
A ciphertext.tsv token that aligns 1:1 to a "glossed" passA.tsv token inherits that status; every token that is
NEW relative to passA.tsv (the recovered missing line, the "17", the end-of-page "Ph"+"47" -- i.e. every position
pass A simply never transcribed) is counted as UNGLOSSED for this purpose. This deliberately does not credit the
control with any gloss the reconciliation itself uncovered, so the reported control number is, if anything,
conservative (a lower bound on how much a correctly-sized gloss-reveal profile could achieve by chance).
"""
import argparse, gzip, random, re, sys, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CORPUS = os.path.join(REPO, 'tools/data/fr16/lettresindites00marg_djvu.txt.gz')
PASSA = os.path.join(HERE, 'passA.tsv')
KEYGLOSS = os.path.join(HERE, 'key_gloss.tsv')


def strip_mark(tok):
    return re.sub(r'[\*\^`\'´ˇ¨=]+$', '', tok)


def norm_sym(tok):
    return {'Th': '[circle-dot]', 'Ph': '[phi-symbol]'}.get(tok, tok)


def load_tsv_runs(path):
    runs = []
    with open(path) as f:
        header = None
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            row = line.rstrip('\n').split('\t')
            if header is None:
                header = row
                continue
            d = dict(zip(header, row))
            if d.get('run_id') == 'run_id':
                continue
            runs.append(d)
    return runs


def nw(x, y):
    """Needleman-Wunsch alignment, identical to tools/reconcile_passes.py's nw(): list of (i, j) pairs, None
    for a gap on that side."""
    n, m = len(x), len(y)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0] = -i
    for j in range(1, m + 1):
        S[0][j] = -j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = max(S[i - 1][j - 1] + (1 if x[i - 1] == y[j - 1] else -1), S[i - 1][j] - 1, S[i][j - 1] - 1)
    i, j, path = n, m, []
    while i or j:
        if i and j and S[i][j] == S[i - 1][j - 1] + (1 if x[i - 1] == y[j - 1] else -1):
            path.append((i - 1, j - 1)); i -= 1; j -= 1
        elif i and S[i][j] == S[i - 1][j] - 1:
            path.append((i - 1, None)); i -= 1
        else:
            path.append((None, j - 1)); j -= 1
    return path[::-1]


def passA_glossed_positions():
    """Boolean list, one per passA.tsv token in reading order: True if that position is among the first k_gloss
    tokens of its run (k_gloss from key_gloss.tsv's source_run counts -- the original TX-BARRT method)."""
    runs = load_tsv_runs(PASSA)
    counts = collections.Counter()
    for d in load_tsv_runs(KEYGLOSS):
        counts[d['source_run']] += 1
    flags = []
    for d in runs:
        toks = d['tokens'].split()
        k = min(counts.get(d['run_id'], 0), len(toks))
        flags += [True] * k + [False] * (len(toks) - k)
    return flags


def real_run_profile(ctpath=PASSA):
    """(run_id, n_tokens, k_gloss) for every run in ctpath. For ctpath == passA.tsv: k_gloss from key_gloss.tsv's
    source_run counts (original TX-BARRT method, reproduces its numbers exactly). For any other ctpath (e.g.
    ciphertext.tsv): k_gloss is the count of that run's tokens that align (NW, marks/symbol-labels stripped) to a
    passA.tsv token flagged glossed by the method above -- see module docstring for why raw gloss-word-counting
    was rejected."""
    runs = load_tsv_runs(ctpath)
    if os.path.abspath(ctpath) == os.path.abspath(PASSA):
        counts = collections.Counter()
        for d in load_tsv_runs(KEYGLOSS):
            counts[d['source_run']] += 1
        return [(d['run_id'], len(d['tokens'].split()), min(counts.get(d['run_id'], 0), len(d['tokens'].split())))
                for d in runs]

    streamA = [norm_sym(strip_mark(t)) for d in load_tsv_runs(PASSA) for t in d['tokens'].split()]
    glossedA = passA_glossed_positions()
    streamB = [norm_sym(strip_mark(t)) for d in runs for t in d['tokens'].split()]
    glossedB = [False] * len(streamB)
    for i, j in nw(streamA, streamB):
        if i is not None and j is not None and glossedA[i]:
            glossedB[j] = True

    profile = []
    pos = 0
    for d in runs:
        n = len(d['tokens'].split())
        k = sum(1 for x in glossedB[pos:pos + n] if x)
        profile.append((d['run_id'], n, k))
        pos += n
    return profile


def load_words(n_needed):
    text = gzip.open(CORPUS, 'rt', encoding='utf-8', errors='ignore').read()
    text = text[20000:20000 + 60000]
    words = re.findall(r"[A-Za-zÀ-ÿ']+", text.lower())
    words = [w for w in words if len(w) >= 1]
    if len(words) < n_needed:
        words = (words * (n_needed // len(words) + 1))
    return words[:n_needed]


def build_control(seed, ctpath=PASSA):
    rng = random.Random(seed)
    profile = real_run_profile(ctpath)
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


def build_control_observations(seed, ctpath=PASSA):
    """Same construction as build_control() above (identical rng call sequence for a given seed, so seed N
    here is the same control realization as build_control(N)), but returns the per-token (code, value,
    source_run) observations -- one per glossed position -- instead of aggregate coverage/sense counts.
    Added ZX-BAR, 25 Sept 2026, for permutation_test.py's leave-one-out statistic, so the same test that runs
    on key_gloss.tsv can run on a control of the identical design (CLAUDE.md rule 3)."""
    rng = random.Random(seed)
    profile = real_run_profile(ctpath)
    total_n = sum(n for _, n, _ in profile)
    words = load_words(total_n)

    freq = collections.Counter(words)
    top_words = [w for w, _ in freq.most_common(9)]

    code_pool = list(range(10, 99))
    rng.shuffle(code_pool)
    next_code = iter(code_pool)
    word_to_codes = {}
    for w in top_words:
        n_hom = rng.choice([2, 3, 3, 4])
        word_to_codes[w] = [next(next_code) for _ in range(n_hom)]
    used_word_code = {}

    codes_at_pos = []
    for w in words:
        if w in word_to_codes:
            c = rng.choice(word_to_codes[w])
        else:
            if w not in used_word_code:
                used_word_code[w] = next(next_code, None) or rng.randint(100, 199)
            c = used_word_code[w]
        codes_at_pos.append(str(c))

    pos = 0
    observations = []
    for run_id, n, k in profile:
        toks = codes_at_pos[pos:pos + n]
        truth = words[pos:pos + n]
        for i in range(k):
            observations.append({'code': toks[i], 'value': truth[i], 'source_run': run_id})
        pos += n
    return observations


MARK_TYPES = ['circumflex', 'grave', 'acute', 'macron', 'caron', 'diaeresis', 'dot']


def build_control_observations_marked(seed, ctpath=PASSA, marked_share=0.75):
    """Code+mark variant of build_control_observations() (ZX-BAR2, 25 Sept 2026): same run/profile
    construction, same homophone-code assignment per top word, but each observation also gets a mark. A mark
    is a deterministic function of (code, word) drawn from a 7-symbol pool (a separate rng stream, so it does
    not perturb the unmarked function's draws) -- every occurrence of code C standing for word W gets the SAME
    mark, so if C is also used (elsewhere) for a different word W', that occurrence very likely gets a
    DIFFERENT mark (7 symbols vs typically 2-4 homophones per code), i.e. marks carry real, exploitable
    meaning in this control, by construction. Only a `marked_share` fraction of occurrences actually receive
    their mark (rng-drawn per occurrence); the rest are tagged 'none', modelling a partially-marked design like
    the real letter's (not every token carries a visible mark). The returned 'code' field is 'BARECODE-MARK'
    (e.g. '43-circumflex' or '43-none'), the same string shape key_gloss_marked.tsv uses, so
    permutation_test.py's existing per-code grouping treats a marked and an unmarked occurrence of the same
    bare digit as different keys, exactly modelling the code+mark hypothesis under test.
    `marked_share` should be set to the SAME share the real key_gloss_marked.tsv observations show (computed by
    the caller from that file), so the control matches the target's actual marked/unmarked ratio, not an
    assumed one (CLAUDE.md rule 3)."""
    rng = random.Random(seed)
    profile = real_run_profile(ctpath)
    total_n = sum(n for _, n, _ in profile)
    words = load_words(total_n)

    freq = collections.Counter(words)
    top_words = [w for w, _ in freq.most_common(9)]

    code_pool = list(range(10, 99))
    rng.shuffle(code_pool)
    next_code = iter(code_pool)
    word_to_codes = {}
    for w in top_words:
        n_hom = rng.choice([2, 3, 3, 4])
        word_to_codes[w] = [next(next_code) for _ in range(n_hom)]
    used_word_code = {}

    mark_rng = random.Random(seed * 7919 + 13)
    mark_for_pair = {}

    def mark_of(code, word):
        key = (code, word)
        if key not in mark_for_pair:
            mark_for_pair[key] = mark_rng.choice(MARK_TYPES)
        return mark_for_pair[key]

    codes_at_pos = []
    for w in words:
        if w in word_to_codes:
            c = rng.choice(word_to_codes[w])
        else:
            if w not in used_word_code:
                used_word_code[w] = next(next_code, None) or rng.randint(100, 199)
            c = used_word_code[w]
        codes_at_pos.append(str(c))

    pos = 0
    observations = []
    for run_id, n, k in profile:
        toks = codes_at_pos[pos:pos + n]
        truth = words[pos:pos + n]
        for i in range(k):
            code, word = toks[i], truth[i]
            mark = mark_of(code, word) if rng.random() < marked_share else 'none'
            observations.append({'code': f'{code}-{mark}', 'value': word, 'source_run': run_id})
        pos += n
    return observations


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seeds', type=int, default=5)
    ap.add_argument('--ctpath', default=PASSA, help='passA.tsv (default) or a reconciled file such as ciphertext.tsv')
    args = ap.parse_args()
    results = [build_control(seed, args.ctpath) for seed in range(args.seeds)]
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

"""Shared library for the untersberg-code abbreviation-expansion control (NEAR.md step 1).

Not a network tool; disk-only. See README.md for the method this implements.
"""
import json
import math
import random
import re

CORPUS_PATH = "tools/data/de16/composed_enhg.txt"
SPEC_PATH = "specs/untersberg-code.json"


def load_corpus_words():
    text = open(CORPUS_PATH, encoding="utf-8").read()
    return re.findall(r"[A-Za-zÄÖÜäöüß]+", text)


def target_shape():
    """Derive the target's own token shape from the spec ciphertext: total tokens,
    digit-token count and digit-length multiset, and letter-token length multiset
    (bucketed 1/2/3/4+, with the exact lengths kept for the 4+ bucket)."""
    spec = json.load(open(SPEC_PATH, encoding="utf-8"))
    tokens = []
    for line in spec["ciphertext"]:
        for raw in line.split():
            raw = raw.strip(",")
            if raw:
                tokens.append(raw)
    digit_lens = []
    letter_lens = []
    for t in tokens:
        core = t[:-1] if t.endswith(".") else t
        if core.isdigit():
            digit_lens.append(len(core))
        else:
            letter_lens.append(len(core))
    return {
        "n_tokens": len(tokens),
        "digit_lens": digit_lens,
        "letter_lens": letter_lens,
    }


def abbreviation_length_labels(letter_lens):
    """Turn the target's letter-token length multiset into an assignment list of
    abbreviation lengths (one int per scored word-token in a synthetic window)."""
    return list(letter_lens)


def build_windows(words, n_windows=5, window_len=71, seed=20260925, starts=None):
    """Pick n_windows non-overlapping windows of window_len words each."""
    if starts is None:
        span = len(words) - window_len
        step = span // n_windows
        starts = [i * step for i in range(n_windows)]
    windows = []
    for s in starts:
        windows.append((s, words[s:s + window_len]))
    return windows


def rest_of_corpus(words, start, window_len):
    """Words before and after the window, each kept as its own contiguous run
    (so no bigram bridges the removed window)."""
    before = words[:start]
    after = words[start + window_len:]
    return before, after


def build_bigram_model(before, after):
    """Unigram + bigram counts from two contiguous runs (never the window itself)."""
    unigram = {}
    bigram = {}
    vocab = set()
    for run in (before, after):
        for w in run:
            vocab.add(w)
            unigram[w] = unigram.get(w, 0) + 1
        for a, b in zip(run, run[1:]):
            bigram.setdefault(a, {})
            bigram[a][b] = bigram[a].get(b, 0) + 1
    return {"unigram": unigram, "bigram": bigram, "vocab": vocab, "total": sum(unigram.values())}


def make_synthetic_window(window_words, letter_len_labels, digit_lens, seed):
    """Turn one real-word window into an abbreviated token sequence.

    n_tokens = len(window_words) = len(letter_len_labels) + len(digit_lens).
    A random subset of positions (size len(digit_lens)) become digit tokens
    (unscored filler, length drawn from the target's own digit-length multiset,
    value arbitrary since no digit token in the target is claimed to be a coded
    word); the rest are abbreviated by suspension (first k letters + '.', k drawn
    from letter_len_labels, shuffled) -- the stated scheme in the brief.
    """
    rng = random.Random(seed)
    n = len(window_words)
    n_digit = len(digit_lens)
    digit_positions = set(rng.sample(range(n), n_digit))
    letter_labels = list(letter_len_labels)
    rng.shuffle(letter_labels)
    digit_lens_shuf = list(digit_lens)
    rng.shuffle(digit_lens_shuf)

    tokens = []
    true_words = {}  # position -> true word, only for scored (letter) positions
    li = 0
    di = 0
    for pos, word in enumerate(window_words):
        if pos in digit_positions:
            length = digit_lens_shuf[di]
            di += 1
            # Arbitrary digit filler (not claimed to encode anything); deterministic
            # from position so the run is reproducible.
            digits = "".join(str((pos * 7 + k * 3 + 1) % 10 or 1) for k in range(length))
            tokens.append(digits + ".")
        else:
            k = letter_labels[li]
            li += 1
            core = word[:k] if k < len(word) else word
            tokens.append(core + ".")
            true_words[pos] = word
    return tokens, true_words


def token_letters(tok):
    core = tok[:-1] if tok.endswith(".") else tok
    return core


LOG_FLOOR = -30.0


def beam_expand(tokens, true_positions, model, beam_width=25, top_candidates=40):
    """Beam search: propose a full word for each non-digit token, scored by a
    word bigram (with unigram backoff / additive smoothing), constrained to
    vocabulary words whose lowercase form starts with the token's (lowercased)
    letters and is at least as long as them (suspension = a real prefix)."""
    unigram = model["unigram"]
    bigram = model["bigram"]
    vocab_list = sorted(model["vocab"])
    vocab_size = max(len(vocab_list), 1)
    total = max(model["total"], 1)

    # Precompute lowercase prefix index once for speed.
    lower_vocab = [(w, w.lower()) for w in vocab_list]

    def candidates_for(prefix_lower):
        cands = [w for w, wl in lower_vocab if wl.startswith(prefix_lower) and len(wl) >= len(prefix_lower)]
        # Rank by unigram frequency, keep the top N to bound beam branching.
        cands.sort(key=lambda w: -unigram.get(w, 0))
        return cands[:top_candidates]

    def word_logprob(prev_word, word):
        if prev_word is not None and prev_word in bigram and word in bigram[prev_word]:
            ctx_total = sum(bigram[prev_word].values())
            return math.log((bigram[prev_word][word] + 0.1) / (ctx_total + 0.1 * vocab_size))
        # backoff to unigram
        return math.log((unigram.get(word, 0) + 0.1) / (total + 0.1 * vocab_size)) - 1.0

    # beam: list of (score, prev_word, choices_dict)
    beam = [(0.0, None, {})]
    for pos, tok in enumerate(tokens):
        letters = token_letters(tok)
        is_digit = letters.isdigit()
        new_beam = []
        if is_digit:
            for score, prev_word, choices in beam:
                new_beam.append((score, None, choices))  # digit breaks context
        else:
            prefix_lower = letters.lower()
            cands = candidates_for(prefix_lower)
            if not cands:
                for score, prev_word, choices in beam:
                    c = dict(choices)
                    c[pos] = None
                    new_beam.append((score + LOG_FLOOR, prev_word, c))
            else:
                for score, prev_word, choices in beam:
                    for w in cands:
                        lp = word_logprob(prev_word, w)
                        c = dict(choices)
                        c[pos] = w
                        new_beam.append((score + lp, w, c))
        new_beam.sort(key=lambda x: -x[0])
        beam = new_beam[:beam_width]

    best_score, _, best_choices = beam[0]
    correct = 0
    scored = 0
    for pos in true_positions:
        scored += 1
        if best_choices.get(pos) == true_positions[pos]:
            correct += 1
    return {
        "score": correct / scored if scored else 0.0,
        "correct": correct,
        "scored": scored,
        "choices": best_choices,
    }

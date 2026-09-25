#!/usr/bin/env python3
"""Word-pattern crib solver for kaliningrad-2015 against the Frank/2021 Synodal-Bible claim.

Design (GOLD-KAL1, 25 Sept 2026; brief .claude/briefs/runs/2026-09-25-lane-gold-c4-kaliningrad-crib-and-homophonic.md).

A cipher word's *pattern* is the sequence of first-occurrence indices of its signs, e.g.
"elhxikixacel" tokenised to signs [e,l,h,x,i,k,i,x,a,c,e,l] has pattern (0,1,2,3,4,5,4,3,6,7,0,1) --
invariant under ANY injective substitution of signs for letters (a pattern-matching crib solver never
needs to know or guess a substitution key; that is the whole point of word-pattern solving, and it is
why the control below uses a plain *random relabelling* of a real plaintext window's own tokens as
signs, rather than building a separate "encipherment": relabelling is cryptanalytically equivalent to
any other injective substitution for a solver that only ever looks at abstract sign patterns).

Two tokenisations (brief's conventions):
  A: a letter plus a following apostrophe merges into ONE sign (matches ic_analysis.py; K=36 on the
     target). On the plaintext side the equivalent merge is a Cyrillic consonant plus a following
     soft sign (ь) or hard sign (ъ) -- exactly the shape the apostrophe is claimed to transliterate.
  B: the apostrophe is its own sign (K about 27 on the target). On the plaintext side nothing merges;
     Cyrillic already writes ь/ъ as ordinary separate letters.

Dotted abbreviation groups (x.s.f.d., c.f., ...: >=2 dots) are excluded from crib matching (abbreviations
do not appear as vocabulary word forms) but are still counted as tokens. A handful of words carry a
single TRAILING dot immediately before one of Ernst's own running-count markers ([194] etc.) or a closing
quote -- that dot is a section/quote boundary in his transcript, not part of the sign sequence, and is
stripped before tokenising the word itself.

Vocabulary: word forms (with counts) read from every chapter in a corpus directory (tools/data/ru19,
one .txt.gz per book, chapters marked "== CHAPTER N ==") plus a parallel per-chapter word multiset for
the "best matching chapter" report.

Solver: beam-search constraint propagation, cipher words processed longest-first (most signs first,
since long words disambiguate the sign->letter map fastest and leave the shortest, most ambiguous
words for last, when the map is already mostly pinned down). For each cipher word, candidates are
vocabulary words of the identical pattern and length that are consistent with the CURRENT partial
sign->letter map (one letter per sign, one sign per letter -- a proper substitution, checked both
directions). A single greedy commit-the-best-candidate pass is fragile (one wrong choice on an early
long word can lock a wrong pair that blocks every later word's correct candidate for the rest of the
run -- measured directly on a real control window, see solve()'s own docstring); a beam of the top
states by (words matched, corpus-frequency-weighted log-score) is kept instead, each word branching
into its top few consistent candidates plus a "leave unmatched" option. A word with no consistent
candidate in a surviving state is left unmatched (not forced). Score = share of words matched (== a
vocabulary form under the current map)
and share of distinct signs mapped to a letter.
"""
import argparse
import gzip
import math
import random
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET_CIPHERTEXT = HERE.parent / "ciphertext.txt"
DEFAULT_CORPUS = HERE.parent.parent.parent / "tools" / "data" / "ru19"

APOST = "'"
SOFT_HARD = ("ь", "ъ")  # ь, ъ
CYR_RE = re.compile(r"[а-яё]+", re.IGNORECASE)


# ---------------------------------------------------------------- ciphertext side

def load_ciphertext_words(path=TARGET_CIPHERTEXT):
    """Return (words, abbrev_groups) -- words: list of raw cleaned word strings (no dots, no leading/
    trailing quote, internal hyphens dropped); abbrev_groups: list of raw tokens with >=2 dots, kept
    separately and never matched against the vocabulary."""
    text = path.read_text(encoding="utf-8")
    words, abbrevs = [], []
    for line in text.splitlines():
        if not line.strip() or line.startswith("#") or line.startswith("[SECTION"):
            continue
        line = re.sub(r"^\[[^\]]+\]\s*", "", line)
        line = re.sub(r"\[\d+\]", "", line)
        for raw in line.split():
            if set(raw) <= set("."):
                continue  # the "eimat . . . . ." filler line
            if raw.count(".") >= 2:
                abbrevs.append(raw)
                continue
            w = raw.strip('"')
            w = w.replace("-", "")
            if w.endswith(".") and w.count(".") == 1:
                w = w[:-1]  # section/quote boundary marker, not a sign
            if not w:
                continue
            words.append(w)
    return words, abbrevs


def cipher_signs_A(word):
    out, i = [], 0
    while i < len(word):
        c = word[i]
        nxt = word[i + 1] if i + 1 < len(word) else ""
        if nxt == APOST:
            out.append(c + nxt)
            i += 2
        elif c == APOST:
            i += 1  # stray apostrophe, shouldn't occur after cleaning
        else:
            out.append(c)
            i += 1
    return out


def cipher_signs_B(word):
    return list(word)


# ---------------------------------------------------------------- plaintext side

def plain_tokens_A(word):
    """Merge a consonant (any Cyrillic letter) with a following soft/hard sign into one token."""
    out, i = [], 0
    while i < len(word):
        c = word[i]
        nxt = word[i + 1] if i + 1 < len(word) else ""
        if nxt in SOFT_HARD:
            out.append(c + nxt)
            i += 2
        else:
            out.append(c)
            i += 1
    return out


def plain_tokens_B(word):
    return list(word)


def signs_fn(convention, side):
    if convention == "A":
        return cipher_signs_A if side == "cipher" else plain_tokens_A
    return cipher_signs_B if side == "cipher" else plain_tokens_B


# ---------------------------------------------------------------- pattern

def pattern_of(tokens):
    idx = {}
    out = []
    for t in tokens:
        if t not in idx:
            idx[t] = len(idx)
        out.append(idx[t])
    return tuple(out)


# ---------------------------------------------------------------- corpus / vocabulary

def iter_corpus_chapters(corpus_dir):
    """Yield (book_nr, chapter_no, [cyrillic-lowercase words]) for every chapter in every .txt.gz."""
    for fp in sorted(Path(corpus_dir).glob("*.txt.gz")):
        book_nr = int(fp.name.split("_", 1)[0])
        with gzip.open(fp, "rt", encoding="utf-8") as f:
            text = f.read()
        chapter_no = None
        words = []
        for line in text.splitlines():
            m = re.match(r"== CHAPTER (\d+) ==", line)
            if m:
                if chapter_no is not None:
                    yield book_nr, chapter_no, words
                chapter_no = int(m.group(1))
                words = []
                continue
            words.extend(w.lower() for w in CYR_RE.findall(line))
        if chapter_no is not None:
            yield book_nr, chapter_no, words


def build_vocab(corpus_dir, convention, exclude_chapter=None):
    """exclude_chapter: optional (book_nr, chapter_no) to hold out of the vocabulary.
    Returns (vocab_by_pattern: pattern -> list[(tokens_tuple, count)] sorted by count desc,
             word_count: Counter of word string -> count,
             chapters: dict (book_nr, chapter_no) -> Counter(word_str))."""
    plain_fn = signs_fn(convention, "plain")
    word_count = Counter()
    chapters = {}
    for book_nr, chapter_no, words in iter_corpus_chapters(corpus_dir):
        if exclude_chapter is not None and (book_nr, chapter_no) == exclude_chapter:
            continue
        chapters[(book_nr, chapter_no)] = Counter(words)
        word_count.update(words)
    by_tokens = {}
    for w, c in word_count.items():
        toks = tuple(plain_fn(w))
        by_tokens[toks] = by_tokens.get(toks, 0) + c
    vocab_by_pattern = {}
    for toks, c in by_tokens.items():
        patt = pattern_of(toks)
        vocab_by_pattern.setdefault(patt, []).append((toks, c))
    for patt in vocab_by_pattern:
        vocab_by_pattern[patt].sort(key=lambda x: -x[1])
    return vocab_by_pattern, word_count, chapters


# ---------------------------------------------------------------- solver

def _consistent_candidates(signs, candidates, sign2letter, letter2sign):
    """Yield (cand_tokens, count, new_s2l, new_l2s) for candidates consistent with the given partial
    map (checked both directions: one letter per sign, one sign per letter)."""
    for cand_tokens, count in candidates:
        if len(cand_tokens) != len(signs):
            continue
        ok = True
        new_s2l, new_l2s = {}, {}
        for s, l in zip(signs, cand_tokens):
            cur = sign2letter.get(s, new_s2l.get(s))
            if cur is not None:
                if cur != l:
                    ok = False
                    break
                continue
            if letter2sign.get(l, new_l2s.get(l)) is not None:
                ok = False
                break
            new_s2l[s] = l
            new_l2s[l] = s
        if ok:
            yield cand_tokens, count, new_s2l, new_l2s


def solve(cipher_word_signs, vocab_by_pattern, candidate_cap=200, beam_width=12, branch_cap=4):
    """Beam-search constraint propagation over cipher words longest-first (brief's design: one letter
    per sign, one sign per letter, candidates scored by corpus frequency). A beam (not a single greedy
    commit) is kept because a pure greedy longest-first commit is fragile: a single wrong choice on an
    early long word can lock a wrong sign->letter pair that then blocks every later word's correct
    candidate for the rest of the run (found on a real control window, GOLD-KAL1 25 Sept 2026 -- one
    seed's recovery collapsed to about 3 pct under pure greedy, 100 pct under beam search on the SAME
    window). Each beam state is (sign2letter, letter2sign, matched dict, cumulative log-score); at each
    word, every state branches into its top `branch_cap` consistent candidates (by corpus frequency)
    plus a "leave unmatched" branch, and the beam keeps the top `beam_width` states by
    (words matched so far, cumulative score). Returns (matched, sign2letter) from the best final state.
    cipher_word_signs: list of (word_id, [sign, sign, ...])."""
    ordered = sorted(cipher_word_signs, key=lambda x: -len(x[1]))
    # state: (sign2letter, letter2sign, matched, score)
    beam = [({}, {}, {}, 0.0)]
    for word_id, signs in ordered:
        patt = pattern_of(signs)
        candidates = vocab_by_pattern.get(patt, [])[:candidate_cap]
        next_states = []
        for sign2letter, letter2sign, matched, score in beam:
            branched = 0
            for cand_tokens, count, new_s2l, new_l2s in _consistent_candidates(
                signs, candidates, sign2letter, letter2sign
            ):
                if branched >= branch_cap:
                    break
                branched += 1
                s2l = {**sign2letter, **new_s2l}
                l2s = {**letter2sign, **new_l2s}
                m = {**matched, word_id: cand_tokens}
                next_states.append((s2l, l2s, m, score + math.log(count + 1)))
            # always keep the "leave this word unmatched" branch too
            next_states.append((sign2letter, letter2sign, matched, score))
        next_states.sort(key=lambda st: (len(st[2]), st[3]), reverse=True)
        # de-duplicate identical (sign2letter) states before truncating the beam
        seen = set()
        deduped = []
        for st in next_states:
            key = tuple(sorted(st[0].items()))
            if key in seen:
                continue
            seen.add(key)
            deduped.append(st)
            if len(deduped) >= beam_width:
                break
        beam = deduped
    best = max(beam, key=lambda st: (len(st[2]), st[3]))
    return best[2], best[0]


def words_matched_share(cipher_word_signs, matched):
    n = len(cipher_word_signs)
    return (len(matched) / n) if n else 0.0


def letters_mapped_share(cipher_word_signs, sign2letter):
    all_signs = set()
    for _wid, signs in cipher_word_signs:
        all_signs.update(signs)
    if not all_signs:
        return 0.0
    return len(sign2letter) / len(all_signs)


def best_chapter(matched, chapters):
    """Chapter whose word multiset covers the most decoded (matched) words. Returns
    ((book_nr, chapter_no), covered_count, total_matched) or (None, 0, total_matched)."""
    decoded_words = ["".join(toks) for toks in matched.values()]
    total = len(decoded_words)
    if not total:
        return None, 0, 0
    best_key, best_cov = None, -1
    for key, ctr in chapters.items():
        cov = sum(1 for w in decoded_words if ctr.get(w, 0) > 0)
        if cov > best_cov:
            best_cov = cov
            best_key = key
    return best_key, best_cov, total


# ---------------------------------------------------------------- control generation

def make_control_window(corpus_dir, convention, seed, target_signs=978):
    """Pick a random chapter, take a prefix window of about target_signs signs (convention A/B
    tokenisation), relabel each distinct token with a random synthetic sign (a random injective
    substitution -- see module docstring for why the *particular* substitution does not matter to a
    pattern-based solver). Returns (chapter_key, cipher_word_signs, true_tokens_per_word,
    n_true_letters)."""
    rng = random.Random(seed)
    plain_fn = signs_fn(convention, "plain")
    chapters = list(iter_corpus_chapters(corpus_dir))
    # only chapters long enough to fill a target_signs-sign window on their own (no cross-chapter
    # concatenation, so the window stays a single coherent passage as the brief specifies)
    chapters = [
        c for c in chapters
        if sum(len(plain_fn(w)) for w in c[2]) >= target_signs
    ]
    book_nr, chapter_no, words = rng.choice(chapters)
    window_words = []
    n_signs = 0
    for w in words:
        toks = plain_fn(w)
        if n_signs and n_signs + len(toks) > target_signs:
            break
        window_words.append(toks)
        n_signs += len(toks)
        if n_signs >= target_signs:
            break
    distinct = sorted({t for toks in window_words for t in toks})
    rng.shuffle(distinct)
    label = {t: f"s{i}" for i, t in enumerate(distinct)}
    cipher_word_signs = []
    true_tokens_per_word = []
    n_letters = 0
    for i, toks in enumerate(window_words):
        cipher_word_signs.append((i, [label[t] for t in toks]))
        true_tokens_per_word.append(toks)
        n_letters += sum(len(t) for t in toks)
    return (book_nr, chapter_no), cipher_word_signs, true_tokens_per_word, n_letters, label


def score_control(cipher_word_signs, true_tokens_per_word, sign2letter, label):
    """Share of plaintext LETTERS recovered: for every sign occurrence, does sign2letter map it to
    the true token (expanded to its letter count)?"""
    inv_label = {v: k for k, v in label.items()}
    total_letters = 0
    correct_letters = 0
    for (word_id, signs), true_toks in zip(cipher_word_signs, true_tokens_per_word):
        for s, true_tok in zip(signs, true_toks):
            n = len(true_tok)
            total_letters += n
            if sign2letter.get(s) == true_tok:
                correct_letters += n
    return (correct_letters / total_letters) if total_letters else 0.0


# ---------------------------------------------------------------- target shuffle null

def shuffle_null(cipher_word_signs, seed):
    """Shuffle each word's own sign sequence's letters (a permutation of that word's own signs, not
    a corpus draw) -- the null the brief asks for: 'the share of words matched by chance' when the
    words no longer carry real internal repeat structure beyond what survives a random within-word
    permutation."""
    rng = random.Random(seed)
    out = []
    for wid, signs in cipher_word_signs:
        s2 = signs[:]
        rng.shuffle(s2)
        out.append((wid, s2))
    return out


# ---------------------------------------------------------------- CLI

def cipher_word_signs_for(convention, words):
    fn = cipher_signs_A if convention == "A" else cipher_signs_B
    return [(i, fn(w)) for i, w in enumerate(words)]


def run_target(convention, corpus_dir, exclude_chapter=None, shuffle_seed=None):
    words, abbrevs = load_ciphertext_words()
    cws = cipher_word_signs_for(convention, words)
    if shuffle_seed is not None:
        cws = shuffle_null(cws, shuffle_seed)
    vocab, _wc, chapters = build_vocab(corpus_dir, convention, exclude_chapter=exclude_chapter)
    matched, sign2letter = solve(cws, vocab)
    wshare = words_matched_share(cws, matched)
    lshare = letters_mapped_share(cws, sign2letter)
    bchap, cov, tot = best_chapter(matched, chapters)
    return {
        "convention": convention,
        "n_words": len(cws),
        "n_abbrev": len(abbrevs),
        "words_matched": len(matched),
        "words_matched_share": wshare,
        "letters_mapped_share": lshare,
        "best_chapter": bchap,
        "best_chapter_cover": cov,
        "best_chapter_total_matched": tot,
    }


def run_control(convention, corpus_dir, seed, holdout, target_signs=978):
    chap_key, cws, true_toks, n_letters, label = make_control_window(
        corpus_dir, convention, seed, target_signs=target_signs
    )
    exclude = chap_key if holdout else None
    vocab, _wc, _chapters = build_vocab(corpus_dir, convention, exclude_chapter=exclude)
    matched, sign2letter = solve(cws, vocab)
    letters_recovered = score_control(cws, true_toks, sign2letter, label)
    return {
        "convention": convention,
        "seed": seed,
        "holdout": holdout,
        "chapter": chap_key,
        "n_words": len(cws),
        "n_true_letters": n_letters,
        "n_signs": len(label),
        "letters_recovered_share": letters_recovered,
        "words_matched_share": words_matched_share(cws, matched),
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    pc = sub.add_parser("control", help="matched control: real chapter window, solved by the same solver")
    pc.add_argument("--convention", choices=["A", "B"], required=True)
    pc.add_argument("--seed", type=int, required=True)
    pc.add_argument("--holdout", action="store_true", help="exclude the control's own chapter from the vocabulary")
    pc.add_argument("--corpus", default=str(DEFAULT_CORPUS))
    pc.add_argument("--target-signs", type=int, default=978)

    pt = sub.add_parser("target", help="run on the real kaliningrad-2015 ciphertext")
    pt.add_argument("--convention", choices=["A", "B"], required=True)
    pt.add_argument("--corpus", default=str(DEFAULT_CORPUS))

    pn = sub.add_parser("null", help="shuffle-null on the target's own words")
    pn.add_argument("--convention", choices=["A", "B"], required=True)
    pn.add_argument("--corpus", default=str(DEFAULT_CORPUS))
    pn.add_argument("--seed", type=int, required=True)

    args = ap.parse_args(argv)

    if args.cmd == "control":
        r = run_control(args.convention, args.corpus, args.seed, args.holdout, args.target_signs)
        print(
            f"CONTROL convention={r['convention']} seed={r['seed']} holdout={r['holdout']} "
            f"chapter={r['chapter']} n_words={r['n_words']} n_true_letters={r['n_true_letters']} "
            f"n_signs={r['n_signs']} letters_recovered={r['letters_recovered_share']:.3f} "
            f"words_matched={r['words_matched_share']:.3f}"
        )
    elif args.cmd == "target":
        r = run_target(args.convention, args.corpus)
        print(
            f"TARGET convention={r['convention']} n_words={r['n_words']} n_abbrev={r['n_abbrev']} "
            f"words_matched={r['words_matched']}/{r['n_words']} "
            f"({r['words_matched_share']:.3f}) letters_mapped={r['letters_mapped_share']:.3f} "
            f"best_chapter={r['best_chapter']} cover={r['best_chapter_cover']}/{r['best_chapter_total_matched']}"
        )
    elif args.cmd == "null":
        r = run_target(args.convention, args.corpus, shuffle_seed=args.seed)
        print(
            f"NULL convention={r['convention']} seed={args.seed} n_words={r['n_words']} "
            f"words_matched={r['words_matched']}/{r['n_words']} ({r['words_matched_share']:.3f}) "
            f"letters_mapped={r['letters_mapped_share']:.3f}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())

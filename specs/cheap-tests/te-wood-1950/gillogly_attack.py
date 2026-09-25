#!/usr/bin/env python3
"""Gillogly-style dictionary attack on te-wood-1950 (Thouless/Wood running-sum cipher).

Method (Cipherbrain post 35, sources/schmeh/posts/35-thouless.txt): a key text supplies a sequence
of distinct words (duplicates of earlier words in the sequence dropped) starting at some offset; each
word's letters are summed A=1..Z=26 and reduced mod 26 to give one key number per plaintext letter;
ciphertext = plaintext + key (mod 26). This script tries every start offset in a candidate key text,
derives the N-letter key stream, decrypts, and scores the putative plaintext for real-word content
via tools/english_score.py's EnglishModel.cover() (longest stretch that splits wholly into dictionary
words) against an English model and against a model built from the key text's own language.

At N=21 (te-wood-1950) this is far too short for a score-based PASS (CLAUDE.md rule 3, spec
cheap_tests_in_order[0]): a hit is reported only as a candidate for a person's manual inspection.

Own code; nothing copied from the solver repositories (CLAUDE.md rule 8).

Usage:
  python3 gillogly_attack.py attack --cipher FVAMINTKFXXWATBOIZVVX --keytext keytexts/fr_bible.txt \
      --lang-name french --max-words 20000 --topn 10
  python3 gillogly_attack.py control --keytext keytexts/de_novel_faust.txt --n 21 --seeds 3 --topn 10
"""
import argparse
import random
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from english_score import EnglishModel, az, DATA as TOOLS_DATA  # noqa: E402

N_DEFAULT = 21


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def read_key_text(path, max_chars=3_000_000):
    t = Path(path).read_text(encoding="utf-8", errors="replace")
    return t[:max_chars]


def key_words(text):
    """Raw word tokens in reading order, A-Z only after accent-stripping (letters used for the
    Gillogly running sum), each paired with its precomputed value = sum(A=1..Z=26) mod 26."""
    raw = re.findall(r"[A-Za-zÀ-ſ]+", text)
    out = []
    for w in raw:
        up = strip_accents(w).upper()
        up = re.sub(r"[^A-Z]", "", up)
        if not up:
            continue
        val = sum(ord(c) - 64 for c in up) % 26
        out.append((up, val))
    return out


def keystream_at(words, start, n, max_lookahead=400):
    """Walk forward from `start`, collecting the first n distinct word-strings (case-normalised),
    dropping repeats of any word already used in this run (Gillogly/Thouless dedup rule). Returns
    the list of n key values, or None if n distinct words are not reached within max_lookahead raw
    words (rare; only near a very short/duplicate-heavy stretch)."""
    seen = set()
    vals = []
    i = start
    limit = min(len(words), start + max_lookahead)
    while i < limit and len(vals) < n:
        w, v = words[i]
        if w not in seen:
            seen.add(w)
            vals.append(v)
        i += 1
    if len(vals) < n:
        return None
    return vals


def decrypt(cipher_vals, key_vals):
    return "".join(chr((c - k) % 26 + 65) for c, k in zip(cipher_vals, key_vals))


def cipher_to_vals(cipher_str):
    s = az(cipher_str)
    return [ord(c) - 65 for c in s]


def build_model(paths=None, texts=()):
    return EnglishModel(paths=paths, texts=texts)


def score_candidate(plain, en_model, lang_model):
    en_cover, en_pos = en_model.cover(plain)
    la_cover, la_pos = (lang_model.cover(plain) if lang_model is not None else (0, 0))
    return max(en_cover, la_cover), en_cover, la_cover


def run_attack(cipher_str, keytext_path, lang_name, max_words, topn, en_model, lang_model):
    text = read_key_text(keytext_path)
    words = key_words(text)[:max_words]
    cvals = cipher_to_vals(cipher_str)
    n = len(cvals)
    results = []
    limit = len(words)
    for s in range(limit):
        kv = keystream_at(words, s, n)
        if kv is None:
            continue
        plain = decrypt(cvals, kv)
        total, en_c, la_c = score_candidate(plain, en_model, lang_model)
        results.append((total, en_c, la_c, s, plain))
    results.sort(key=lambda r: -r[0])
    print(f"# key text: {keytext_path} ({lang_name}), {len(words)} raw words scanned (capped at {max_words})")
    print(f"# candidate offsets scored: {len(results)}")
    print("rank\tscore(max)\ten_cover\t{}_cover\toffset\tplaintext".format(lang_name))
    for i, (total, en_c, la_c, s, plain) in enumerate(results[:topn], 1):
        print(f"{i}\t{total}\t{en_c}\t{la_c}\t{s}\t{plain}")
    return results


def run_control(keytext_path, n, seeds, topn, en_model, lang_model, lang_name, max_words):
    """True offset is planted inside the SAME [0, max_words) search range the real attack scans
    (not just forward from the true offset), so the control matches the real search conditions."""
    text = read_key_text(keytext_path)
    words = key_words(text)[:max_words]
    en_corpus_text = Path(TOOLS_DATA / "pg1661_holmes.txt").read_text(encoding="utf-8", errors="replace")
    az_en = az(en_corpus_text)
    ranks = []
    for seed in range(seeds):
        rng = random.Random(2000 + seed)
        # pick a real English sentence-length window of n letters from the corpus
        p_start = rng.randrange(0, len(az_en) - n)
        plain = az_en[p_start:p_start + n]
        # pick a random true key offset, leaving room for the keystream lookahead
        true_off = rng.randrange(0, max(1, len(words) - 200))
        kv = keystream_at(words, true_off, n)
        if kv is None:
            print(f"# seed {seed}: keystream_at failed at offset {true_off}, skipping")
            continue
        pvals = [ord(c) - 65 for c in plain]
        cvals = [(p + k) % 26 for p, k in zip(pvals, kv)]
        cipher_str = "".join(chr(c + 65) for c in cvals)
        results = []
        for s in range(len(words)):
            kv2 = keystream_at(words, s, n)
            if kv2 is None:
                continue
            cand = decrypt(cvals, kv2)
            total, en_c, la_c = score_candidate(cand, en_model, lang_model)
            results.append((total, en_c, la_c, s, cand))
        results.sort(key=lambda r: -r[0])
        rank = next((i for i, r in enumerate(results, 1) if r[3] == true_off), None)
        ranks.append(rank)
        print(f"# seed {seed}: true_off={true_off} plain={plain} cipher={cipher_str}")
        print(f"# seed {seed}: rank of true offset = {rank} of {len(results)} candidates searched "
              f"(full range 0..{len(words)})")
        print(f"# seed {seed}: top {topn} candidates:")
        print("rank\tscore(max)\ten_cover\t{}_cover\toffset\tplaintext".format(lang_name))
        for i, (total, en_c, la_c, s, cand) in enumerate(results[:topn], 1):
            marker = " <-- TRUE" if s == true_off else ""
            print(f"{i}\t{total}\t{en_c}\t{la_c}\t{s}\t{cand}{marker}")
    print(f"# control ranks per seed: {ranks}")
    return ranks


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("attack")
    a.add_argument("--cipher", required=True)
    a.add_argument("--keytext", required=True)
    a.add_argument("--lang-name", required=True)
    a.add_argument("--max-words", type=int, default=20000)
    a.add_argument("--topn", type=int, default=10)

    c = sub.add_parser("control")
    c.add_argument("--keytext", required=True)
    c.add_argument("--lang-name", default="lang")
    c.add_argument("--n", type=int, default=N_DEFAULT)
    c.add_argument("--seeds", type=int, default=3)
    c.add_argument("--topn", type=int, default=10)
    c.add_argument("--max-words", type=int, default=20000)

    args = ap.parse_args()

    if args.cmd == "attack":
        en_model = build_model()  # default English corpora
        lang_text = read_key_text(args.keytext, max_chars=1_500_000)
        lang_model = build_model(texts=[lang_text])
        run_attack(args.cipher, args.keytext, args.lang_name, args.max_words, args.topn, en_model, lang_model)
    else:
        en_model = build_model()
        lang_text = read_key_text(args.keytext, max_chars=1_500_000)
        lang_model = build_model(texts=[lang_text])
        run_control(args.keytext, args.n, args.seeds, args.topn, en_model, lang_model, args.lang_name,
                    args.max_words)


if __name__ == "__main__":
    main()

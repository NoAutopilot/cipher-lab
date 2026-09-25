"""Hypothesis-family plugins for tools/family_run.py (25 Sept 2026, TOOL-FAMILY).

A family is one module in this package exposing:

  DESCRIPTION                      one line, printed by family_run.py --help
  make_control(spec, seed, corpora, params) -> (cipher_msgs, plain, train_corpora)
      params always carries N, K, lengths (per message), messages_independent (True when the spec gives separate
      {groups} messages, False for one text over several lines) and target_msgs (the target's tokens, for a
      design that needs a statistic of the target such as a scanned period), plus every --param k=v as strings.
      build rule 3's matched control: same N, same K, same design and language as the target. cipher_msgs is a
      list of messages, each a list of sign strings; plain is the true plaintext (folded letters, all messages
      joined); train_corpora is the list of corpus texts the solver may train on for THIS control (the control's
      own plaintext window is cut out, so the control is never solved against a model that has seen it).
  solve(cipher_msgs, spec, seed, restarts, corpora, params) -> (best_plain, score, info)
      run the family's solver blind; best_plain is the decode as folded letters (messages joined), score the
      solver's own objective for the best restart (higher is better), info a small dict for the decode file.
  score_recovery(plain, truth) -> float
      share of positions read correctly, 0..1.

Shared helpers below: draw_window() cuts a control plaintext out of a corpus and returns the corpus with that
window removed; letters() flattens messages. Families wrap existing tools (homophonic_anneal.py, running_key.py)
by importing them, never by copying their logic (CLAUDE.md Usage 8)."""
import os, random, sys

TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)

REGISTRY = ("masc", "homophonic", "periodic_vigenere", "running_key", "keyed_running_key", "permuted_tableau")


def draw_window(text, n, seed, accept=None, tries=200, margin=2000):
    """Cut an n-letter window out of the middle 90% of text. accept(window) may reject a window (e.g. wrong
    number of distinct letters); after `tries` rejections the last window is used. Returns (window, rest) where
    rest is text with the window and a margin around it removed, for training a solver that must not see it."""
    if len(text) < n + 2 * margin + 10:
        margin = max(0, (len(text) - n) // 4)
    rng = random.Random(seed * 7919 + n)
    lo, hi = len(text) // 20, len(text) * 19 // 20 - n
    if hi <= lo:
        lo, hi = 0, max(1, len(text) - n)
    w = text[:n]
    for _ in range(tries):
        s = rng.randrange(lo, hi)
        w = text[s:s + n]
        if accept is None or accept(w):
            break
    rest = text[:max(0, s - margin)] + text[s + n + margin:]
    return w, rest


def letters(msgs):
    return "".join("".join(m) for m in msgs)


def load(name):
    import importlib
    if name not in REGISTRY:
        raise SystemExit(f"unknown family {name!r}; known: {', '.join(REGISTRY)}")
    return importlib.import_module(f"families.{name}")

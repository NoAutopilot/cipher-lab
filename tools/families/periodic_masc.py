"""periodic_masc: period-P general substitution -- P independent monoalphabetic substitution alphabets applied
in rotation (position i decodes under the alphabet for coset i % P), each coset's key an unrelated full
substitution, unlike periodic_vigenere's shift-only cosets (HES-PHASE, 27 Sept 2026, hessen-1824: the second
opinion's lead A -- the leaf's own Anmerkung names a period-P key with 'Auflosungsbuchstaben' resolution
letters, periodic_vigenere excluded shifted alphabets at periods 2-20, masc excluded a single alphabet, but
neither tested P independently permuted alphabets).

Solver: wraps tools/homophonic_anneal.py the way masc.py does, but each ciphertext token is expanded to a
composite sign "<token>#<coset>" so anneal() assigns an independent key letter to every (token, coset) pair.
The corpus n-gram model still scores the single decoded stream in its original order, so the P key tables are
optimised jointly against one full-text objective, not P separate unigram tables.

Control: a corpus window with exactly K distinct letters (masc.py's own K-matching design, since K here is the
target's own total distinct-sign count, not a per-coset count), enciphered under P independent random keys of
that many signs each -- one key per coset, same N, K, P and language as the target.

params: period=P (required, no default -- the runner passes it explicitly per the brief's P in 6/7/8 sweep),
iters (default 40000), order (3), uni_weight (1.0), continuous (as periodic_vigenere: key phase runs on across
message boundaries unless the spec gives separate {groups} messages or --param continuous=0/1 overrides),
noise=p (GAPS69, 3 Oct 2026, riksarkivet-r4282-1628: a share p of control tokens redrawn from the control's own
token stream, frequency-weighted, ignoring coset -- a misread sign is still a sign from the same inventory -- so
the control runs at the target's measured transcription error, CLAUDE.md rule 3 SALV-DIAG paragraph; default 0)."""
import random
import homophonic_anneal as ha
from families import draw_window

DESCRIPTION = "periodic general substitution: P independent monoalphabetic alphabets in rotation (own signs via homophonic_anneal.py; --param period=P required)"


def _p(params, k, d):
    return type(d)(params.get(k, d))


def _period(params):
    P = int(params.get("period", 0))
    if not P:
        raise SystemExit("periodic_masc needs --param period=P")
    return P


def _continuous(params):
    """Same rule as periodic_vigenere: the key phase runs on across message boundaries (one text over several
    lines) unless the spec gives separate messages ({groups} entries) or --param continuous=0/1 says otherwise."""
    if "continuous" in params:
        return bool(int(params["continuous"]))
    return not params.get("messages_independent", False)


def _composite(msgs, P, cont):
    """Flatten msgs into one sign sequence, sign = f"{token}#{coset}"; coset counts across message boundaries
    when cont, else restarts at 0 for every message."""
    seq, pos = [], 0
    for m in msgs:
        for i, c in enumerate(m):
            j = (pos + i) if cont else i
            seq.append(f"{c}#{j % P}")
        pos += len(m)
    return seq


def make_control(spec, seed, corpora, params):
    N, K = params["N"], params["K"]
    P = _period(params)
    cont = _continuous(params)
    text = ha.fold("\n".join(corpora))
    accept = lambda w: len(set(w)) == K
    plain, rest = draw_window(text, N, seed, accept)
    lengths = params.get("lengths") or [N]
    rng = random.Random(seed + 1000)
    distinct = sorted(set(plain))
    keys = []
    for c_ in range(P):
        signs = [f"s{c_}_{i}" for i in range(len(distinct))]
        rng.shuffle(signs)
        keys.append(dict(zip(distinct, signs)))
    msgs, pos = [], 0
    for n in lengths:
        p = plain[pos:pos + n]
        seg = []
        for i, a in enumerate(p):
            j = (pos + i) if cont else i
            seg.append(keys[j % P][a])
        msgs.append(seg)
        pos += n
    noise = float(params.get("noise", 0) or 0)
    if noise:  # GAPS69 3 Oct 2026: see module docstring
        nrng = random.Random(seed + 9000)
        flat = [x for m in msgs for x in m]
        msgs = [[nrng.choice(flat) if nrng.random() < noise else x for x in m] for m in msgs]
    return msgs, plain, [rest]


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    P = _period(params)
    cont = _continuous(params)
    seq = _composite(cipher_msgs, P, cont)
    model = ha.Model(corpora, _p(params, "order", 3))
    res = ha.solve(seq, model, restarts, _p(params, "iters", 40000), seed, _p(params, "uni_weight", 1.0))
    sc, key = res[0]
    dec = "".join(key[x] for x in seq)
    return dec, sc, {"period": P, "continuous_key": cont, "restart_scores": [round(r[0], 1) for r in res]}


def score_recovery(plain, truth):
    n = max(1, len(truth))
    return sum(1 for a, b in zip(plain, truth) if a == b) / n

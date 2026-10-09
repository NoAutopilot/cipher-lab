#!/usr/bin/env python3
"""family_run.py: run one hypothesis family on a spec, matched control FIRST, and log both numbers side by side.

Rule 3 (CLAUDE.md) made mechanical (25 Sept 2026, UPDATES.md): a solver's failure on a target means nothing
unless the same solver reads a synthetic cipher of the same length, sign count, design and language. This tool
builds that control from the spec (N, K, the spec's judge corpus from tools/data), solves it blind with the seeds
given, and only if the control's mean recovery meets --gate does it run the target. Otherwise it prints
CONTROL BELOW GATE, writes the control row, exits 3, and never touches the target. Every run appends one row
to ciphers/<slug>/HYPOTHESES.md (created with a header if absent); a target run also writes the best decode to
ciphers/<slug>/families/<family>-<seed>.txt and, when the spec has a judge block, runs tools/judge_plaintext.py
on it and records the verdict line.

  python3 tools/family_run.py SPEC --family FAMILY [--control-only | --target-only-if-gated]
          [--seed 1] [--seeds 3] [--restarts 8] [--corpus PATH ...] [--gate 0.6] [--out HYPOTHESES.md]
          [--label TEXT] [--param k=v ...] [--cipher PATH] [--tokens auto|letters|space]
          [--shuffle-target SEED] [--dry-run]

  example (the demonstration of 25 Sept 2026):
  python3 tools/family_run.py specs/cigaret-case-1909.json --family masc --seed 1 --restarts 4 --seeds 3 \\
          --label "TOOL-FAMILY demo"
      -> control: German window N=45 K=18 under a simple substitution, 3 seeds; gate 0.6 not met at this N
         (a MASC anneal has almost no power at 45 letters), so the row says CONTROL BELOW GATE and exit 3.
  python3 tools/family_run.py specs/koehler-1944.json --family periodic_vigenere --seeds 3 --gate 0.6
  python3 tools/family_run.py specs/koehler-1944.json --family running_key --corpus tools/data/de20 --param beam=300

Families (tools/families/<name>.py, each wraps an existing tool, see the package docstring for the interface):
  masc               simple substitution: homophonic_anneal.py with one sign per letter; control has the target's K
  homophonic         homophonic substitution: homophonic_anneal.py with the spec's K (--param profile=target
                     matches the target's own sign-count profile; --param noise=p redraws a share p of control
                     tokens at the target's own type frequencies, GOLD-D1 25 Sept 2026; --param merge=k nulls=p
                     collapses k letters' signs into one symbol and makes a share p of tokens nulls, H22 28 Sept 2026;
                     --param wild=sM,HOOK anneals each occurrence of a wild sign as its own letter, H25 28 Sept 2026;
                     --param alphabet=ru-s3p-soft sets the plaintext alphabet, A2P4-KAL4 3 Oct 2026 -- give the
                     spec's judge block the same "alphabet")
  periodic_vigenere  Vigenere/Beaufort/variant-Beaufort, short repeating key (own solver; --param tabula=beau period=7)
  periodic_masc      period-P general substitution: P independent monoalphabetic alphabets in rotation, not a shift
                     (HES-PHASE 27 Sept 2026, hessen-1824): homophonic_anneal.py over composite (token, coset) signs,
                     jointly annealed under one full-text n-gram objective; --param period=P is required, no scan
  running_key        book-key Vigenere: running_key.py two-stream beam decoder (needs >= 3 corpus texts; slow)
  keyed_running_key  book key through a keyword-mixed tableau (family B', 25 Sept 2026): stage 1 ranks keywords by the
                     ciphertext letter counts, stage 2 beam-decodes the top ones (--param kcorpus=tools/data/nl20 top=3)
  syllabary          partial syllabary (LANE R8 DSN, 25 Sept 2026): base code = letter, a superscript mark on a consonant
                     base = the following vowel; control laid on the spec's row_pattern with the CM3 measured error mix
                     (--param err=0.05 gap=2 use=auto); recovery is token accuracy
  permuted_tableau   book key through a GENERAL permuted tableau, first B''-c: a free permutation on the cipher side
                     (family B'', GOLD-B2D 25 Sept 2026): sort-match start, anneal under an n-gram sum-stream proxy,
                     beam rescoring; control = random S3 of 26! (--param kcorpus=tools/data/nl20 chains=3 evals=30000)
  nomenclator        two-level numeric word code (family C, armstrong-madison-1808, ARM-C1 26 Sept 2026): particle
                     block 1-99 + family book >= 100 (decade = family, units digit = member slot), word-trigram Gibbs
                     anneal with the sibling-vocabulary prior; `*`/`**`/`<..>` tokens are OOV wildcards; the control
                     is a letter from a HELD-OUT corpus file (--param holdout=5 sweeps=30), run with --tokens space
  wordcode           letter-or-word nomenclator inside sign runs (bSALW 26 Sept 2026, fr2933-salviati-1525): each sign type
                     = one letter or one whole word / <NAME> code (--param codes=marked|topk:N|all vocab=1000 err=0.064);
                     runs bounded by words, mixed spaced/unspaced trigram score; control on the target's run lengths with
                     the target's code token share and code-type count; token accuracy, per class printed (letters/codes)
  phased_homophonic  two-digit homophonic in unsegmented digit runs with stray single digits (BIRAGO-NUM3 2 Oct 2026): phase
                     resampled jointly with the key (Viterbi re-cut under trigram + P(pair|letter), alternating with
                     homophonic_anneal); control on the target's run lengths (--param cells=40 strays=0.05; --cipher FILE
                     --tokens space, one run per line); recovery = right phase AND right letter
  seeded_code        homophonic two-part code of syllables/words with a partial key pinned (A2-CAS8 2 Oct 2026,
                     castelcicala-1816): --param pins=<key.tsv>, local alphabetical runs as bracket constraints
                     (run=6 bracket=8), control at the target's pinned token share (pinshare=0 = blind baseline);
                     recovery = token accuracy on unpinned positions; --param lm=entry scores entries with an
                     entry-bigram model instead of the letter 4-gram (A2-CAS9 3 Oct 2026)
  cycling_homophonic homophonic with each letter's homophones used in a fixed cyclic order (Pelling 2020; R11-SCORPCYC
                     6 Oct 2026, scorpion-1991): anneal with -lam x cycle violations (no sign twice between two
                     consecutive occurrences of another sign of the same letter); --param lam=2.0 (lam=50 near-hard)
  masc_words         simple substitution, n-gram anneal + dictionary-segmentation polish (R12D-FAIR 6 Oct 2026)
  masc_inj           strictly injective simple substitution by a left-to-right word-pattern beam (R12D-FAIR2 6 Oct 2026,
                     fair-game-2010: control 0.576 at N=67 beam 1000, bimodal -- a wrong opening is never recovered)
  columnar_homophonic irregular columnar transposition (widths 2-12) of a homophonic substitution, joint numpy anneal
                     over column order and key (R15-KAL14 6 Oct 2026, kaliningrad-2015); --param widths=, iters=, ctrl_widths=

Modes: --target-only-if-gated (default) runs the control, then the target only if the gate is met;
--control-only runs the control alone (calibration) and logs it. --seeds N runs the control on seeds
--seed .. --seed+N-1 and reports mean and range; the target runs once on --seed.
--control-n N (bMALC, 26 Sept 2026; valid only with --control-only, else exit 2): the tool otherwise always
overwrites params["N"] with the target's own ciphertext length, so a control at a projected pool size (before
the pooling fetch is paid for) could never be run. --control-n builds the control at N instead, keeping the
target's own K; any --param profile=target sign-count profile is scaled proportionally from the target's real
counts to N (each count's occurrences repeated round(count * N/actual_N) times before the family reads it, so
the bucket-allocation shape is preserved, not just its absolute size). The HYPOTHESES.md row and the printed
plan both say "projected N" next to the value, and the target is never run (control-only is required).
Corpora: --corpus files or directories (all .txt / .txt.gz inside); default is the spec's judge.corpora, else
tools/judge_plaintext.py's LANG_CORPORA for judge.language. The control plaintext window is cut from the corpus
and removed from what the control's solver trains on.
Ciphertext: read from the spec (`ciphertext` as a string, a list of lines, or a list of {groups} messages); --tokens
letters = every a-z letter is a sign, space = whitespace-separated tokens are signs ('.' tokens dropped as word
dividers), auto (default) = letters when the spec's alphabet says a-z/Latin/letters, else space. --cipher PATH
overrides with a long-format TSV (header with a `sign` column, DOT/COL rows dropped) or a text file.
--shuffle-target SEED replaces the target ciphertext's own letters/tokens with a random permutation of themselves
(Random(SEED).shuffle, redistributed back into the original message lengths, so N/K/design are unchanged) before
the target solve; the control is unaffected (still the ordinary matched-corpus control, built from the unshuffled
target's params["target_msgs"]: before R14-KAL12, 6 Oct 2026, the shuffled tokens were passed, so a family whose
control reads the target's token order -- wordcode's Counter.most_common tie order -- built a different control under
--shuffle-target than without it at the same --seed, which R14-KAL11 logged as 'not seed-reproducible'). This is the false-positive
floor for a gate-plus-judge PASS on garbage of the same shape (CLAUDE.md rule 3); the decode file and row are
marked shuffle=SEED so they never collide with the real target's own row. A judge PASS on this shuffled decode
voids the judge as a gate for this family at this N (CLAUDE.md rule 3; ARM-C1, 26 Sept 2026: the en18 judge
PASSed a nomenclator decode of shuffled armstrong-madison-1808) -- run --shuffle-target before trusting a PASS
on the real target as a gate.
--param lock=FILE (MQS-LOCK, 9 Oct 2026; tools/tests/PREREG-MQS-LOCK.md): hold confirmed sign values fixed through
every restart and sweep and re-run the rest -- the confirm-lock-re-run step of Lasry, Biermann and Tomokiyo 2023
pp.115-117 (Figs 6-7) and CTTS's 'Locked' homophones. FILE is `sign<TAB>value[<TAB>grade]` ('#' comments, NULL = a
null), seeded_code's pins contract (read_pins, A2-CAS8 2 Oct 2026, castelcicala-1816). Wired for homophonic (fixed=),
nomenclator (cribs), wordcode and syllabary (a held map), and seeded_code, where lock= is an alias of pins= and nothing
else (its own control share and unpinned scoring). Any other family: exit 2, naming the family (a lock is never
silently ignored). A lock sign absent from the ciphertext is reported in the plan and ignored, never an error. The
control locks its OWN synthetic key at the target's locked TOKEN share (seeded_code's target_pinshare rule: types
drawn with weight count**lockpow, default 2, each at its majority true value); recovery is scored on UNLOCKED token
positions only and the row carries the lock file's sha256, row count and both locked shares. Control knobs:
lockshare=p (override the share; 0 = the blind baseline), lockapply=0 (select and score the same positions but do not
hold them: blind on identical positions), lockperm=1 (the wrong-key null: the same signs held at permuted values),
lockdraw=D (another random draw of the locked types at the same share and seed; default 0).
Promoted from ciphers/clair1161-avis-flandre-1688/two/reanneal.py stage 1 as run by two/lolo_diag.py (C1161-LOLO,
4 Oct 2026, planted control 3/3); its stage 2 (word cover) is left behind, since that is what failed there.
Not a fourth try of tools/crib_rounds.py's held re-anneal (rule 3's third-attempt clause): crib_rounds measures a
reader loop (cribs proposed from a partial decode, round by round) and failed below a ~45% decode (solvEX, solvEX2,
ARM3-LOOP); lock measures only the harness step -- values confirmed outside the run, held, the rest re-run and scored
against a matched-share control -- and makes no claim that a reader can find the locks.
Meant to catch: a run that re-anneals a sign a verifier already confirmed; a control that scores locked tokens as
recovered (inflating the figure). Must NOT block: any run without lock= (byte-identical to before), a lock file
naming signs the ciphertext lacks. Tests: tools/tests/test_family_run_lock.py.
Exit codes: 0 run complete (gate met, or --control-only); 3 CONTROL BELOW GATE (control row written, no target);
2 bad arguments (a --label carrying a rule 10 word: solved, new, first, unpublished; lock= on a family it is not
wired for; a missing lock file).
The row never carries a decode; the decode is in the families/ file. The tool never writes the words solved,
new, first or unpublished (rule 10).

Wall-clock box (GOLD-K1, 25 Sept 2026): the tool has no --timeout of its own -- the process runs the control
seeds and, if gated, the target in one call, in that order. If you wrap this call in an external timeout (a
worker's own wall-clock box, `timeout N python3 tools/family_run.py ...`), size N to cover the control battery
plus the target run combined, not a single-stage estimate: a 1500 s box that only budgeted the control killed
the target mid-run, and the worker had to notice and rerun the target alone by hand to keep rule 3's control+target
pairing intact. When in doubt, run `--control-only` first to see how long the control battery actually takes,
then size the target call's own box on top of that.

A newly added control option (a new `--param profile=...`, a new corpus flag, anything that changes what the
control plaintext looks like) is worth a single-seed sanity comparison against the target -- run one seed of each
side and eyeball the profile/L1 numbers -- before the full `--seeds` battery runs. A wrong first implementation
still burns a complete run either way (GOLD-D1, 25 Sept 2026: a wrong first `profile=target` implementation was
only caught after the full seeded control had already run).

Test: python3 tools/tests/test_family_run.py  (offline, under two minutes)
"""
import argparse, json, os, re, statistics, subprocess, sys, time
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
sys.path.insert(0, TOOLS)
import judge_plaintext as jp  # noqa: E402
import families  # noqa: E402

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
HEADER = ("| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |\n"
          "|---|---|---|---|---|---|---|---|---|\n")
MARKER = "<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->"
BANNED = re.compile(r"\b(solved|new|first|unpublished)\b", re.I)


def utc_date():
    t = time.gmtime()
    return f"{t.tm_mday} {MONTHS[t.tm_mon - 1]} {t.tm_year} {t.tm_hour:02d}:{t.tm_min:02d}"


# ---------------------------------------------------------------- ciphertext
def _tokens_of_line(line, mode):
    if mode == "letters":
        return list(jp.fold(line))
    toks = [t for t in line.split() if t not in (".", "|.", "·")]
    return toks


def read_spec_cipher(spec, mode):
    c = spec.get("ciphertext")
    if c is None:
        raise SystemExit("spec has no ciphertext on disk (ciphertext_pending?); give --cipher PATH")
    alpha = str(spec.get("alphabet", ""))
    msgs = []
    if isinstance(c, list) and c and isinstance(c[0], dict):
        for m in c:
            msgs.append(list(jp.fold(m.get("groups") or m.get("text") or "")))
        return msgs, "letters (separate messages)"
    if isinstance(c, dict):
        for k in ("groups", "text", "lines", "main", "body", "main_body"):
            if k in c:
                c = c[k]
                break
        else:
            raise SystemExit("spec ciphertext is a dict without a groups/text/lines key; give --cipher PATH")
    if isinstance(c, str):
        c = c.splitlines()
    if mode == "auto":
        mode = auto_mode([l for l in c if isinstance(l, str)])
    for line in c:
        if not isinstance(line, str) or not line.strip() or re.match(r"\s*#(\s|$)", line):
            continue  # a comment line is "#" followed by a space or nothing; "#^ ..." is a sign named # (Salviati)
        t = _tokens_of_line(line, mode)
        if t:
            msgs.append(t)
    return msgs, mode


def auto_mode(lines):
    """letters when every whitespace token is purely alphabetic (runs of a-z are the signs); space when any token
    carries a digit or mark (each token is one engraved sign, '.' a divider)."""
    toks = [re.sub(r"[.,;:()'\"-]", "", t) for l in lines for t in l.split()]
    toks = [t for t in toks if t]
    return "letters" if toks and all(re.fullmatch(r"[A-Za-z\u00c0-\u017f]+", t) for t in toks) else "space"


def read_cipher_file(path, mode):
    rows = [l.rstrip("\n") for l in open(path, encoding="utf-8") if l.strip() and not l.startswith("#")]
    if rows and "\t" in rows[0] and "sign" in rows[0].split("\t"):
        h = rows[0].split("\t")
        si, li = h.index("sign"), (h.index("line") if "line" in h else None)
        msgs, cur, curline = [], [], None
        for r in rows[1:]:
            f = r.split("\t")
            s = f[si].rstrip("?")
            if s in ("DOT", "COL", ""):
                continue
            ln = f[li] if li is not None else None
            if cur and ln != curline:
                msgs.append(cur)
                cur = []
            curline = ln
            cur.append(s)
        if cur:
            msgs.append(cur)
        return msgs, "tsv"
    if mode == "auto":
        mode = auto_mode(rows)
    return [t for t in (_tokens_of_line(r, mode) for r in rows) if t], mode


# ---------------------------------------------------------------- corpora
def corpus_paths(spec, cli):
    paths = []
    if cli:
        for p in cli:
            if os.path.isdir(p):
                paths += sorted(os.path.join(p, f) for f in os.listdir(p) if f.endswith((".txt", ".txt.gz"))
                                and not f.upper().startswith(("LICENSE", "README", "MANIFEST")))
            else:
                paths.append(p)
        return paths
    j = spec.get("judge") or {}
    if j.get("corpora"):
        return [os.path.join(ROOT, p) if not os.path.isabs(p) else p for p in j["corpora"]]
    lang = j.get("language") or (spec.get("language_candidates") or [""])[0]
    if lang in jp.LANG_CORPORA:
        return [str(p) for p in jp.LANG_CORPORA[lang]]
    raise SystemExit(f"no corpus: spec judge has no corpora and language {lang!r} is not in LANG_CORPORA; give --corpus")


# ---------------------------------------------------------------- HYPOTHESES.md
def append_row(out, cells):
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    row = "| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in cells) + " |\n"
    if BANNED.search(row):
        raise SystemExit("refusing to write a row carrying a rule 10 word (solved/new/first/unpublished): " + row)
    exists = os.path.exists(out)
    text = open(out, encoding="utf-8").read() if exists else ""
    tail = [l for l in text.splitlines() if l.strip()]
    if not exists:
        slug = os.path.basename(os.path.dirname(os.path.abspath(out)))
        text = (f"# {slug} -- hypothesis families\n\nAppend-only. Rows below are written by `tools/family_run.py` "
                "(CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row "
                "with gate met = no reports a control that could not read its own design, and the target was not "
                "run). Prose sections may be added above this table by workers.\n\n")
    with open(out, "a", encoding="utf-8") as f:
        if not exists:
            f.write(text)
        elif not text.endswith("\n"):
            f.write("\n")
        if not (tail and tail[-1].startswith("|") and MARKER in text and tail[-1].count("|") == row.count("|")):
            f.write(("\n" if exists else "") + MARKER + "\n\n" + HEADER)
        f.write(row)
    return row


# ---------------------------------------------------------------- --param lock=FILE (MQS-LOCK, 9 Oct 2026)
LOCK_FAMILIES = ("homophonic", "nomenclator", "wordcode", "syllabary", "seeded_code")


def read_lock(path):
    """The lock file: TSV `sign<TAB>value[<TAB>grade]`, '#' comments, value NULL = a null; an optional header row
    `sign value [grade]` (or seeded_code's `group value`) is skipped. Same contract as seeded_code.read_pins (A2-CAS8,
    2 Oct 2026, castelcicala-1816), except that the value is kept as written (seeded_code folds it to a-z itself; a
    homophonic soft alphabet has upper-case letters). Returns ({sign: value}, {sign: grade}); a row with no TAB value
    is an error (never silently dropped)."""
    vals, grades = {}, {}
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        if line.startswith("#") or not line.strip():
            continue
        p = [x.strip() for x in line.rstrip("\n").split("\t")]
        if len(p) < 2 or not p[0]:
            raise SystemExit(f"lock file {path} line {n}: expected sign<TAB>value[<TAB>grade], got {line.rstrip()!r}")
        if n == 1 and p[0].lower() in ("sign", "group") and p[1].lower() == "value":
            continue
        vals[p[0]] = "" if p[1] == "NULL" else p[1]
        grades[p[0]] = p[2] if len(p) > 2 and p[2] else "-"
    return vals, grades


def sha256_of(path):
    import hashlib
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def choose_control_lock(flat, truth, share, seed, pinpow=2.0, perm=False, draw=0):
    """The control's own lock, matched to the target's locked TOKEN share (seeded_code.make_control's rule, A2-CAS8):
    sign types are drawn at random with weight count**pinpow (default 2: a few frequent types carry the share, as a
    verifier's confirmed signs do) until the locked tokens reach share * N; each locked type takes its TRUE value (the
    majority truth over its occurrences, so an error-injected control is locked to what the sign mostly stands for).
    perm=True is the wrong-key null: the locked values are permuted among themselves (a derangement of the distinct
    values), so the same signs are held at the same share but at wrong values. Its own RNG; the family's RNG is never
    touched, so lockshare=0 reproduces the blind run exactly."""
    import random
    from collections import defaultdict
    by = defaultdict(Counter)
    for t, v in zip(flat, truth):
        if v is not None:
            by[t][v] += 1
    key = {t: c.most_common(1)[0][0] for t, c in by.items()}
    cnt = Counter(t for t in flat if t in key)
    rng = random.Random(seed * 7919 + 4243 + 1000003 * draw)
    types = sorted(cnt, key=lambda t: (-cnt[t], t))
    locked, cov, N = {}, 0, len(flat)
    while cov < share * N and types:
        t = rng.choices(types, weights=[cnt[x] ** pinpow for x in types])[0]
        types.remove(t)
        locked[t] = key[t]
        cov += cnt[t]
    if perm and locked:
        vals = sorted(set(locked.values()))
        if len(vals) > 1:
            while True:
                sh = vals[:]
                rng.shuffle(sh)
                if all(a != b for a, b in zip(vals, sh)):
                    break
            m = dict(zip(vals, sh))
            locked = {t: m[v] for t, v in locked.items()}
    return locked, cov / max(1, N)


def unlocked_recovery(decoded, truth, flat, locked):
    """Token accuracy over UNLOCKED positions only (a locked token reads right because it is locked, so it is never
    counted); positions whose truth is None (a null, an inserted token, a wildcard) are not counted either.
    Returns (share right, positions counted)."""
    pos = [i for i, (t, v) in enumerate(zip(flat, truth)) if v is not None and t not in locked]
    if not pos:
        return 0.0, 0
    return sum(1 for i in pos if i < len(decoded) and decoded[i] == truth[i]) / len(pos), len(pos)


# ---------------------------------------------------------------- main
def run_judge(spec_path, decode_path):
    r = subprocess.run([sys.executable, os.path.join(TOOLS, "judge_plaintext.py"), spec_path, "--file", decode_path],
                       capture_output=True, text=True)
    lines = [l for l in (r.stdout + r.stderr).splitlines() if l.strip()]
    verdict = next((l for l in lines if l.startswith(("PASS", "FAIL"))), lines[-1] if lines else "judge produced no output")
    return verdict.strip()


def fmt(x):
    return f"{x:.3f}"


def rel(p):
    r = os.path.relpath(p, ROOT)
    return p if r.startswith("..") else r


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    ap.add_argument("--family", required=True, choices=families.REGISTRY)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--control-only", action="store_true", help="run and log the control alone (calibration)")
    g.add_argument("--target-only-if-gated", action="store_true", help="default: control first, target only if gated")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--seeds", type=int, default=3, help="number of control seeds starting at --seed (default 3)")
    ap.add_argument("--restarts", type=int, default=8)
    ap.add_argument("--corpus", action="append", help="corpus file or directory (repeatable); default from the spec")
    ap.add_argument("--gate", type=float, default=0.6, help="control mean recovery the target run needs (default 0.6)")
    ap.add_argument("--out", help="HYPOTHESES.md path (default ciphers/<slug>/HYPOTHESES.md)")
    ap.add_argument("--label", default="", help="who ran it and why; rule 10 words are refused")
    ap.add_argument("--param", action="append", default=[], help="family parameter k=v (iters, order, tabula, period, beam ...)")
    ap.add_argument("--measured-error", type=float, default=None, metavar="P",
                     help="the target's own measured transcription disagreement rate (0-1, from reconcile_passes.py "
                          "or a leaf's two-pass reconciliation); if the family's own noise/err --param is below this, "
                          "the run is not refused but its HYPOTHESES.md row is marked as a non-test, not a negative "
                          "(CLAUDE.md rule 3, SALV-DIAG paragraph, 26 Sept 2026)")
    ap.add_argument("--cipher", help="ciphertext file overriding the spec (long-format TSV with a sign column, or text)")
    ap.add_argument("--tokens", default="auto", choices=["auto", "letters", "space"])
    ap.add_argument("--shuffle-target", type=int, default=None, metavar="SEED",
                    help="replace the target's own tokens with a random permutation of themselves (false-positive "
                         "floor); N/K/message lengths unchanged, control unaffected")
    ap.add_argument("--control-n", type=int, default=None, metavar="N",
                    help="build the control at this projected N instead of the target's own N (requires "
                         "--control-only); K stays the target's own K, any profile=target sign-count profile is "
                         "scaled proportionally to N")
    ap.add_argument("--decode-tag", default="", metavar="TAG",
                    help="extra suffix on the decode filename (R15-KAL13, 6 Oct 2026: two --cipher files with the same "
                         "family/params/corpus, e.g. convention A and B, otherwise write one decode file); omitted = old name")
    ap.add_argument("--dry-run", action="store_true", help="print the plan (N, K, corpora, paths) and run nothing")
    a = ap.parse_args(argv)

    if BANNED.search(a.label):
        print("--label carries a rule 10 word (solved/new/first/unpublished); reword it", file=sys.stderr)
        return 2
    if a.control_n is not None and not a.control_only:
        print("--control-n requires --control-only (a projected-N control never runs the target)", file=sys.stderr)
        return 2
    spec = json.load(open(a.spec, encoding="utf-8"))
    slug = spec.get("slug") or os.path.splitext(os.path.basename(a.spec))[0]
    params = dict(kv.split("=", 1) for kv in a.param)
    lock_path = None
    if "lock" in params:
        if a.family not in LOCK_FAMILIES:
            print(f"--param lock= is not wired for family {a.family!r} (lock families: {', '.join(LOCK_FAMILIES)}); "
                  "refusing rather than ignoring the lock", file=sys.stderr)
            return 2
        if not os.path.exists(params["lock"]):
            print(f"--param lock={params['lock']}: no such file", file=sys.stderr)
            return 2
        if a.family == "seeded_code":  # an alias of pins (A2-CAS8), nothing else: its own control, share and scoring
            params["pins"] = params.pop("lock")
        else:
            lock_path = params["lock"]
    label_note = ""
    if a.measured_error is not None:
        err_param = params.get("err") or params.get("noise")
        if err_param is not None and float(err_param) < a.measured_error:
            print(f"WARNING: control error param ({err_param}) is below --measured-error ({a.measured_error}) -- "
                  f"a FAIL here is not yet a design-family negative (CLAUDE.md rule 3, SALV-DIAG paragraph)",
                  file=sys.stderr)
            label_note = f" [control error {err_param} < measured {a.measured_error}: non-test, not a negative]"
    if a.cipher:
        msgs, mode = read_cipher_file(a.cipher, a.tokens)
    else:
        msgs, mode = read_spec_cipher(spec, a.tokens)
    ctl_msgs = msgs  # the control is built from the unshuffled target (R14-KAL12, 6 Oct 2026: see --shuffle-target)
    if a.shuffle_target is not None:
        import random
        rng = random.Random(a.shuffle_target)
        toks_shuf = [t for m in msgs for t in m]
        rng.shuffle(toks_shuf)
        shuffled, pos = [], 0
        for m in msgs:
            shuffled.append(toks_shuf[pos:pos + len(m)])
            pos += len(m)
        msgs = shuffled
    toks = [t for m in msgs for t in m]
    N, K = len(toks), len(set(toks))
    if N == 0:
        raise SystemExit("no ciphertext tokens read")
    params.update({"N": N, "K": K, "lengths": [len(m) for m in msgs], "target_msgs": ctl_msgs,
                   "messages_independent": "separate" in mode})
    N_display = N
    if a.control_n is not None:
        scale = a.control_n / N
        counts = Counter(toks)
        scaled_tokens = [tok for tok, c in counts.items() for _ in range(max(1, round(c * scale)))]
        params["target_msgs"] = [scaled_tokens]
        params["N"] = a.control_n
        N_display = f"{a.control_n} (projected N, actual target N={N})"
    paths = corpus_paths(spec, a.corpus)
    out = a.out or os.path.join(ROOT, "ciphers", slug, "HYPOTHESES.md")
    fam = families.load(a.family)
    seeds = list(range(a.seed, a.seed + max(1, a.seeds)))
    lock_t, lock_line, lock_cell = None, "", ""
    if lock_path:
        lvals, lgrades = read_lock(lock_path)
        tset = set(toks)
        lock_t = {sg: v for sg, v in lvals.items() if sg in tset}
        absent = sorted(sg for sg in lvals if sg not in tset)
        tshare = sum(1 for t in toks if t in lock_t) / N
        lshare = float(params.get("lockshare", tshare))
        lapply = str(params.get("lockapply", "1")) not in ("0", "no", "false")
        lperm = str(params.get("lockperm", "0")) not in ("0", "no", "false", "")
        lpow = float(params.get("lockpow", 2.0))
        ldraw = int(params.get("lockdraw", 0))
        gmix = ",".join(f"{g}:{c}" for g, c in sorted(Counter(lgrades[sg] for sg in lock_t).items()))
        lsha = sha256_of(lock_path)
        lock_line = (f"\nlock {rel(os.path.abspath(lock_path))} sha256 {lsha[:16]}: {len(lvals)} rows, {len(lock_t)} signs in the "
                     f"ciphertext (grades {gmix or '-'}), locked token share {tshare:.3f}; {len(absent)} absent from the "
                     f"ciphertext, ignored" + (f" ({' '.join(absent[:12])}{' ...' if len(absent) > 12 else ''})" if absent else "") +
                     f"\ncontrol lock share {lshare:.3f}" + ("" if lapply else " (lockapply=0: selected and scored, NOT held: "
                     "the blind arm on the same positions)") + (" lockperm: control locked at WRONG values (null)" if lperm else "") +
                     "; recovery is scored on unlocked positions only")
        lock_cell = (f" lock_sha256={lsha[:16]} lock_rows={len(lvals)} lock_in_cipher={len(lock_t)} lock_share_target={tshare:.3f}"
                     f" lock_share_control={lshare:.3f}" + ("" if lapply else " lock_NOT_applied") + (" lock_WRONG_values" if lperm else "")
                     + " recovery=unlocked_positions")
        if not (hasattr(fam, "lock_truth") and hasattr(fam, "lock_decode")):
            raise SystemExit(f"family {a.family} is in LOCK_FAMILIES but has no lock_truth/lock_decode hooks")
    pshow = ",".join(f"{k}={v}" for k, v in params.items() if k not in ("N", "K", "lengths", "target_msgs", "messages_independent"))
    if a.shuffle_target is not None:
        pshow = (pshow + "," if pshow else "") + f"shuffle_target={a.shuffle_target}"
    dsuffix = f"-shuffle{a.shuffle_target}" if a.shuffle_target is not None else ""
    if a.param:  # DSN2 (25 Sept 2026): variants of one family on one seed no longer overwrite each other's decode
        dsuffix += "-" + re.sub(r"[^A-Za-z0-9=.,~#+_-]", "_", ",".join(a.param))[:80]
    if a.label:
        # bBLZ4 (26 Sept 2026): two runs of the same family/seed/params on different corpora (an English judge
        # rerun on German text, say) wrote the same families/<family>-<seed>.txt and silently overwrote each
        # other (bBLZ3's masc-1-de.txt collided with bBLZ2's own masc-1.txt). Prefer a corpus-derived tag (the
        # thing that actually varied); fall back to the label itself. Only added when --label is given, so a
        # caller that never passes one keeps the exact old filename.
        tag_src = os.path.splitext(os.path.basename((a.corpus[0] if a.corpus else "").rstrip("/")))[0] or a.label
        tag = re.sub(r"[^A-Za-z0-9]+", "", tag_src).lower()[:16]
        if tag:
            dsuffix += f"-{tag}"
    if a.decode_tag:
        dsuffix += "-" + re.sub(r"[^A-Za-z0-9_-]+", "", a.decode_tag)[:24]
    plan = (f"family {a.family}: {fam.DESCRIPTION}\nspec {a.spec} slug {slug}\nciphertext: {len(msgs)} message(s), "
            f"N={N_display} signs, K={K} distinct, tokens={mode}" +
            (f" (target letters shuffled, seed {a.shuffle_target}, false-positive floor)" if a.shuffle_target is not None else "") +
            f"\ncorpora: {', '.join(rel(p) for p in paths)}\n"
            f"control seeds {seeds}, restarts {a.restarts}, gate {a.gate}, params {pshow or '-'}\n"
            f"row -> {rel(out)}; decode -> ciphers/{slug}/families/{a.family}-{a.seed}{dsuffix}.txt" + lock_line)
    print(plan)
    if a.dry_run:
        return 0

    corpora = [jp.read_corpus(p) for p in paths]
    # 1. control, always first
    recs = []
    for s in seeds:
        cm, plain, train = fam.make_control(spec, s, corpora, dict(params))
        sp = dict(params)
        if lock_path:
            flatc = [t for m in cm for t in m]
            truth = fam.lock_truth(cm, plain)
            clock, cshare = choose_control_lock(flatc, truth, lshare, s, lpow, lperm, ldraw)
            sp["lock"] = clock if lapply else {}
        dec, sc, info = fam.solve(cm, spec, s, a.restarts, train, sp)
        rec = fam.score_recovery(dec, plain)
        if lock_path:
            rec_all = rec
            rec, npos = unlocked_recovery(fam.lock_decode(dec, cm), truth, flatc, clock)
            print(f"  lock (control seed {s}): {len(clock)} sign types locked, token share {cshare:.3f} (target "
                  f"{tshare:.3f}){'' if lapply else ', NOT held (lockapply=0)'}; recovery on {npos} unlocked positions "
                  f"{rec:.3f} (family's own figure over all positions {rec_all:.3f})")
        recs.append(rec)
        print(f"CONTROL seed {s}: N={sum(len(m) for m in cm)} K={len({t for m in cm for t in m})} recovery {rec:.3f} score {sc:.2f}")
    mean = statistics.mean(recs)
    ctl = f"{fmt(mean)} ({fmt(min(recs))}-{fmt(max(recs))})"
    gated = mean >= a.gate
    date = utc_date()
    par = f"N={N_display} K={K} restarts={a.restarts} corpus={'+'.join(os.path.basename(p) for p in paths)}" + (f" {pshow}" if pshow else "") + lock_cell
    if a.control_only:
        row = append_row(out, [date, a.family, par, f"{seeds[0]}-{seeds[-1]}" if len(seeds) > 1 else seeds[0], ctl,
                              "not run (control-only)", "-", "yes" if gated else "no", a.label or "-"])
        print(f"CONTROL mean {mean:.3f} gate {a.gate} {'met' if gated else 'NOT met'}; row appended to {rel(out)}")
        return 0
    if not gated:
        row = append_row(out, [date, a.family, par, f"{seeds[0]}-{seeds[-1]}" if len(seeds) > 1 else seeds[0], ctl,
                              "not run (CONTROL BELOW GATE)", "-", f"no (gate {a.gate})", a.label or "-"])
        print(f"CONTROL BELOW GATE: mean {mean:.3f} < {a.gate}; target not run; row appended to {rel(out)}")
        return 3
    # 2. target
    tp = dict(params)
    if lock_path:
        tp["lock"] = lock_t if lapply else {}
    dec, sc, info = fam.solve(msgs, spec, a.seed, a.restarts, corpora, tp)
    fdir = os.path.join(ROOT, "ciphers", slug, "families")
    os.makedirs(fdir, exist_ok=True)
    dpath = os.path.join(fdir, f"{a.family}-{a.seed}{dsuffix}.txt")
    with open(dpath, "w", encoding="utf-8") as f:
        shuf_note = f"; TARGET LETTERS SHUFFLED (seed {a.shuffle_target}, false-positive floor)" if a.shuffle_target is not None else ""
        f.write(f"# {slug} {a.family} seed {a.seed} restarts {a.restarts} {date} UTC; control mean {ctl}; score {sc:.3f}{shuf_note}\n")
        f.write(f"# {json.dumps(info, ensure_ascii=False, default=str)[:2000]}\n")
        lines = fam.split_decode(dec, msgs) if hasattr(fam, "split_decode") else None
        if lines is None:
            lines, pos = [], 0
            for m in msgs:
                lines.append(dec[pos:pos + len(m)]); pos += len(m)
        for line in lines:
            f.write(line + "\n")
    verdict = run_judge(a.spec, dpath) if spec.get("judge") else "no judge block"
    print(f"TARGET best score {sc:.3f}; decode -> {rel(dpath)}; judge: {verdict}")
    append_row(out, [date, a.family, par, a.seed, ctl, f"{sc:.3f}", verdict + label_note, f"yes (gate {a.gate})", a.label or "-"])
    print(f"row appended to {rel(out)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

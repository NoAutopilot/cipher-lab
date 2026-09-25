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
                     tokens at the target's own type frequencies, GOLD-D1 25 Sept 2026)
  periodic_vigenere  Vigenere/Beaufort/variant-Beaufort, short repeating key (own solver; --param tabula=beau period=7)
  running_key        book-key Vigenere: running_key.py two-stream beam decoder (needs >= 3 corpus texts; slow)
  keyed_running_key  book key through a keyword-mixed tableau (family B', 25 Sept 2026): stage 1 ranks keywords by the
                     ciphertext letter counts, stage 2 beam-decodes the top ones (--param kcorpus=tools/data/nl20 top=3)

Modes: --target-only-if-gated (default) runs the control, then the target only if the gate is met;
--control-only runs the control alone (calibration) and logs it. --seeds N runs the control on seeds
--seed .. --seed+N-1 and reports mean and range; the target runs once on --seed.
Corpora: --corpus files or directories (all .txt / .txt.gz inside); default is the spec's judge.corpora, else
tools/judge_plaintext.py's LANG_CORPORA for judge.language. The control plaintext window is cut from the corpus
and removed from what the control's solver trains on.
Ciphertext: read from the spec (`ciphertext` as a string, a list of lines, or a list of {groups} messages); --tokens
letters = every a-z letter is a sign, space = whitespace-separated tokens are signs ('.' tokens dropped as word
dividers), auto (default) = letters when the spec's alphabet says a-z/Latin/letters, else space. --cipher PATH
overrides with a long-format TSV (header with a `sign` column, DOT/COL rows dropped) or a text file.
--shuffle-target SEED replaces the target ciphertext's own letters/tokens with a random permutation of themselves
(Random(SEED).shuffle, redistributed back into the original message lengths, so N/K/design are unchanged) before
the target solve; the control is unaffected (still the ordinary matched-corpus control). This is the false-positive
floor for a gate-plus-judge PASS on garbage of the same shape (CLAUDE.md rule 3); the decode file and row are
marked shuffle=SEED so they never collide with the real target's own row.
Exit codes: 0 run complete (gate met, or --control-only); 3 CONTROL BELOW GATE (control row written, no target);
2 bad arguments (a --label carrying a rule 10 word: solved, new, first, unpublished).
The row never carries a decode; the decode is in the families/ file. The tool never writes the words solved,
new, first or unpublished (rule 10).

Test: python3 tools/tests/test_family_run.py  (offline, under two minutes)
"""
import argparse, json, os, re, statistics, subprocess, sys, time

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
        if not isinstance(line, str) or not line.strip() or line.lstrip().startswith("#"):
            continue
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
    ap.add_argument("--cipher", help="ciphertext file overriding the spec (long-format TSV with a sign column, or text)")
    ap.add_argument("--tokens", default="auto", choices=["auto", "letters", "space"])
    ap.add_argument("--shuffle-target", type=int, default=None, metavar="SEED",
                    help="replace the target's own tokens with a random permutation of themselves (false-positive "
                         "floor); N/K/message lengths unchanged, control unaffected")
    ap.add_argument("--dry-run", action="store_true", help="print the plan (N, K, corpora, paths) and run nothing")
    a = ap.parse_args(argv)

    if BANNED.search(a.label):
        print("--label carries a rule 10 word (solved/new/first/unpublished); reword it", file=sys.stderr)
        return 2
    spec = json.load(open(a.spec, encoding="utf-8"))
    slug = spec.get("slug") or os.path.splitext(os.path.basename(a.spec))[0]
    params = dict(kv.split("=", 1) for kv in a.param)
    if a.cipher:
        msgs, mode = read_cipher_file(a.cipher, a.tokens)
    else:
        msgs, mode = read_spec_cipher(spec, a.tokens)
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
    params.update({"N": N, "K": K, "lengths": [len(m) for m in msgs], "target_msgs": msgs,
                   "messages_independent": "separate" in mode})
    paths = corpus_paths(spec, a.corpus)
    out = a.out or os.path.join(ROOT, "ciphers", slug, "HYPOTHESES.md")
    fam = families.load(a.family)
    seeds = list(range(a.seed, a.seed + max(1, a.seeds)))
    pshow = ",".join(f"{k}={v}" for k, v in params.items() if k not in ("N", "K", "lengths", "target_msgs", "messages_independent"))
    if a.shuffle_target is not None:
        pshow = (pshow + "," if pshow else "") + f"shuffle_target={a.shuffle_target}"
    dsuffix = f"-shuffle{a.shuffle_target}" if a.shuffle_target is not None else ""
    plan = (f"family {a.family}: {fam.DESCRIPTION}\nspec {a.spec} slug {slug}\nciphertext: {len(msgs)} message(s), "
            f"N={N} signs, K={K} distinct, tokens={mode}" +
            (f" (target letters shuffled, seed {a.shuffle_target}, false-positive floor)" if a.shuffle_target is not None else "") +
            f"\ncorpora: {', '.join(rel(p) for p in paths)}\n"
            f"control seeds {seeds}, restarts {a.restarts}, gate {a.gate}, params {pshow or '-'}\n"
            f"row -> {rel(out)}; decode -> ciphers/{slug}/families/{a.family}-{a.seed}{dsuffix}.txt")
    print(plan)
    if a.dry_run:
        return 0

    corpora = [jp.read_corpus(p) for p in paths]
    # 1. control, always first
    recs = []
    for s in seeds:
        cm, plain, train = fam.make_control(spec, s, corpora, dict(params))
        dec, sc, info = fam.solve(cm, spec, s, a.restarts, train, dict(params))
        rec = fam.score_recovery(dec, plain)
        recs.append(rec)
        print(f"CONTROL seed {s}: N={sum(len(m) for m in cm)} K={len({t for m in cm for t in m})} recovery {rec:.3f} score {sc:.2f}")
    mean = statistics.mean(recs)
    ctl = f"{fmt(mean)} ({fmt(min(recs))}-{fmt(max(recs))})"
    gated = mean >= a.gate
    date = utc_date()
    par = f"N={N} K={K} restarts={a.restarts} corpus={'+'.join(os.path.basename(p) for p in paths)}" + (f" {pshow}" if pshow else "")
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
    dec, sc, info = fam.solve(msgs, spec, a.seed, a.restarts, corpora, dict(params))
    fdir = os.path.join(ROOT, "ciphers", slug, "families")
    os.makedirs(fdir, exist_ok=True)
    dpath = os.path.join(fdir, f"{a.family}-{a.seed}{dsuffix}.txt")
    with open(dpath, "w", encoding="utf-8") as f:
        shuf_note = f"; TARGET LETTERS SHUFFLED (seed {a.shuffle_target}, false-positive floor)" if a.shuffle_target is not None else ""
        f.write(f"# {slug} {a.family} seed {a.seed} restarts {a.restarts} {date} UTC; control mean {ctl}; score {sc:.3f}{shuf_note}\n")
        f.write(f"# {json.dumps(info, ensure_ascii=False, default=str)[:2000]}\n")
        pos = 0
        for m in msgs:
            f.write(dec[pos:pos + len(m)] + "\n")
            pos += len(m)
    verdict = run_judge(a.spec, dpath) if spec.get("judge") else "no judge block"
    print(f"TARGET best score {sc:.3f}; decode -> {rel(dpath)}; judge: {verdict}")
    append_row(out, [date, a.family, par, a.seed, ctl, f"{sc:.3f}", verdict, f"yes (gate {a.gate})", a.label or "-"])
    print(f"row appended to {rel(out)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

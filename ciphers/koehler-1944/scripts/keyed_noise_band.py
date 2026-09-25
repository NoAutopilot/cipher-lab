#!/usr/bin/env python3
"""GOLD-K3: beau noise band for the keyword-mixed keyed-running-key pipeline (family B'), ten synthetic texts
through the SAME settings as GOLD-K2 variant 1 (arith=beau, kcorpus=tools/data/nl20, top=30, beam=300, order=6,
spaces=1, modes default): six uniform-random texts at the five target lengths (seeds 1-6) and four shuffles of
the target's own 924 letters (seeds 1-4, all messages pooled then redistributed back into the five message
lengths -- keeps the target's pooled letter counts, so stage 1 ranks identically to the real target and stage 2
is the only difference: the sharper of the two floors). Calls families.keyed_running_key.solve() directly on
each synthetic text (never family_run.py, which would rerun the control every time).

  python3 ciphers/koehler-1944/scripts/keyed_noise_band.py TASK [TASK ...] --out PATH
      TASK: u1..u6 (uniform random text, seed 1-6) or s1..s4 (letter-shuffle of the target, seed 1-4)

One line is appended to --out per text, flushed immediately after that text finishes, so a killed process still
leaves its completed rows. Run several of these as separate OS processes (at most 3 decoder processes at once,
counting any concurrent family_run.py run) covering disjoint TASK subsets, each with its own --out under the
scratchpad, then concatenate into the repo once every process has exited; never `git rebase --autostash` or
`tools/room.py --push` while one of these is still writing.
"""
import argparse, json, os, random, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..", "..")
TOOLS = os.path.join(ROOT, "tools")
sys.path.insert(0, TOOLS)
import family_run as frmod  # noqa: E402
import judge_plaintext as jp  # noqa: E402
import families  # noqa: E402
import running_key as rk  # noqa: E402

SPEC_PATH = os.path.join(ROOT, "specs", "koehler-1944.json")
PARAMS = {"kcorpus": "tools/data/nl20", "arith": "beau", "top": "30", "beam": "300", "order": "6", "spaces": "1"}


def build_task(kind, seed, lengths, target_letters):
    rng = random.Random(seed)
    if kind == "u":
        return ["".join(rng.choice(rk.A) for _ in range(n)) for n in lengths], f"uniform seed {seed}"
    if kind == "s":
        toks = list(target_letters)
        rng.shuffle(toks)
        out, pos = [], 0
        for n in lengths:
            out.append("".join(toks[pos:pos + n]))
            pos += n
        return out, f"shuffle seed {seed}"
    raise SystemExit(f"bad task kind {kind!r}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tasks", nargs="+", help="u1..u6 or s1..s4")
    ap.add_argument("--out", required=True, help="TSV to append rows to")
    a = ap.parse_args()

    spec = json.load(open(SPEC_PATH, encoding="utf-8"))
    msgs, _ = frmod.read_spec_cipher(spec, "auto")
    lengths = [len(m) for m in msgs]
    target_letters = "".join("".join(m) for m in msgs)
    paths = frmod.corpus_paths(spec, None)
    corpora = [jp.read_corpus(p) for p in paths]
    fam = families.load("keyed_running_key")

    for task in a.tasks:
        kind, seed = task[0], int(task[1:])
        text_msgs, label = build_task(kind, seed, lengths, target_letters)
        toks_all = [t for m in text_msgs for t in m]
        params = dict(PARAMS, N=len(toks_all), K=len(set(toks_all)), lengths=lengths,
                      target_msgs=text_msgs, messages_independent=True)
        t0 = time.time()
        dec, sc, info = fam.solve(text_msgs, spec, seed, 8, corpora, dict(params))
        elapsed = time.time() - t0
        line = f"{task}\t{label}\t{sc:.4f}\t{info['tabula']}\t{info['stage1_nats']}\t{elapsed:.0f}s\n"
        with open(a.out, "a", encoding="utf-8") as outf:
            outf.write(line)
            outf.flush()
        print(f"{task}: {label} -> pooled joint ll/letter {sc:.4f} tabula {info['tabula']} "
              f"stage1 {info['stage1_nats']} nats ({elapsed:.0f}s)", flush=True)


if __name__ == "__main__":
    main()

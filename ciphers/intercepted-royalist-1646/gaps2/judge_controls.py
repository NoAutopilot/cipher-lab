#!/usr/bin/env python3
"""GAPS2-intercepted-royalist-1646 (2 Oct 2026, account-4): the en16 judge on the f.10 decode with its controls (rule 3).

Regenerates the judge input from f10_ct.tsv + key.tsv (likely9/run.py's text_of: clear words and keyed tokens, unkeyed
tokens dropped), then scores through tools/judge_plaintext.py (spec specs/intercepted-royalist-1646.json, corpora en16_repo):
  candidate            text_f10.txt
  shuffled-null x20    the candidate's letters permuted within the text, word lengths kept (seeds 1-20)
  shuffled-target x20  cipher tokens permuted among cipher positions, clear words fixed, decoded with the same key (seeds 1-20)
Writes gaps2/judge_controls.tsv (one row per text: kind, seed, N, score, null_p99, real_p05, cover, pass) and prints the summary.
A judge PASS on a shuffled-target decode voids the judge as a gate for this key family at this N (CLAUDE.md rule 3, ARM-C1).
"""
import json, random, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
T = ROOT / "ciphers/intercepted-royalist-1646"
sys.path.insert(0, str(T / "likely9"))
from run import load_ct, load_key, text_of  # noqa: E402

SPEC = ROOT / "specs/intercepted-royalist-1646.json"
OUT = T / "gaps2"


def judge(text):
    r = subprocess.run([sys.executable, str(ROOT / "tools/judge_plaintext.py"), str(SPEC), "--text", text, "--json"],
                       capture_output=True, text=True)
    j = json.loads(r.stdout)
    L = j["checks"]["language"]; W = j["checks"].get("words", {})
    return {"N": L["N"], "score": L["score"], "null_p99": L["null_p99"], "real_p05": L["real_p05"],
            "cover": W.get("cover"), "pass": j["pass"]}


def shuffle_letters(text, seed):
    rnd = random.Random(seed)
    words = text.split()
    letters = [ch for w in words for ch in w if ch.isalpha()]
    rnd.shuffle(letters)
    it = iter(letters)
    return " ".join("".join(next(it) if ch.isalpha() else ch for ch in w) for w in words)


def shuffled_target(rows, seed):
    rnd = random.Random(seed)
    idx = [i for i, r in enumerate(rows) if not r[2].startswith("[PLAIN:")]
    perm = idx[:]; rnd.shuffle(perm); sh = rows[:]
    for i, j in zip(idx, perm):
        sh[i] = rows[j]
    return sh


def main():
    key = {c: v[0] for c, v in load_key(T / "key.tsv").items()}
    rows = load_ct(T / "f10_ct.tsv")
    cand = text_of(rows, key)
    (OUT / "text_f10.txt").write_text(cand + "\n")
    out = [("candidate", 0, judge(cand))]
    for s in range(1, 21):
        out.append(("shuffled-null", s, judge(shuffle_letters(cand, s))))
    for s in range(1, 21):
        out.append(("shuffled-target", s, judge(text_of(shuffled_target(rows, s), key))))
    with open(OUT / "judge_controls.tsv", "w") as f:
        f.write("kind\tseed\tN\tscore\tnull_p99\treal_p05\tcover\tpass\n")
        for k, s, j in out:
            f.write(f"{k}\t{s}\t{j['N']}\t{j['score']}\t{j['null_p99']}\t{j['real_p05']}\t{j['cover']}\t{j['pass']}\n")
    c = out[0][2]
    print(f"candidate: N {c['N']} score {c['score']} null_p99 {c['null_p99']} real_p05 {c['real_p05']} cover {c['cover']} pass {c['pass']}")
    for kind in ("shuffled-null", "shuffled-target"):
        xs = [j["score"] for k, s, j in out if k == kind]; cv = [j["cover"] for k, s, j in out if k == kind]
        npass = sum(1 for k, s, j in out if k == kind and j["pass"])
        print(f"{kind} x{len(xs)}: score mean {sum(xs)/len(xs):.3f} min {min(xs):.3f} max {max(xs):.3f}; "
              f"cover mean {sum(cv)/len(cv):.3f} max {max(cv):.3f}; judge PASS {npass}/{len(xs)}; "
              f"candidate above {sum(1 for x in xs if c['score'] > x)}/{len(xs)} on score")


if __name__ == "__main__":
    main()

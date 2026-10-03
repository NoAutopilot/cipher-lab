#!/usr/bin/env python3
"""H73 driver (ciphers/armstrong-madison-1808, 3 Oct 2026; PREREGISTRATION.md in this folder).

  python3 run_h73.py build                       write control_plain.txt + controls.tsv (stats only, no solve)
  python3 run_h73.py control --seeds 1 2 3 [--book THE972 --prior WE028] [--thin 0.75] [--baseline]
                                                 V1 (vocab_order=1) on the cross-held-out control; --baseline also
                                                 runs the unchanged ARM-C1 solver on the same letter
  python3 run_h73.py target --prior WE028        V1 on the target + its shuffled order, both through the en18 judge
Outputs append to results.tsv (one row per solve) and write decodes to out/."""
import argparse, contextlib, io, json, os, random, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp  # noqa: E402
from families import nomenclator as nm  # noqa: E402

TARGET = os.path.join(ROOT, "ciphers", "armstrong-madison-1808", "ciphertext.txt")


def target_msgs():
    return [l.split() for l in open(TARGET) if l.strip() and not l.startswith("#")]


def corpora():
    return [jp.read_corpus(str(p)) for p in jp.LANG_CORPORA["en18"]]


def per_class(dec, plain, classes):
    h, t = {"P": 0, "B": 0}, {"P": 0, "B": 0}
    for a, b, k in zip(dec.split(), plain.split(), classes):
        if k in h:
            t[k] += 1; h[k] += (a == b)
    n = t["P"] + t["B"]
    return (h["P"] + h["B"]) / n, h["P"] / max(1, t["P"]), h["B"] / max(1, t["B"])


def row(fields):
    path = os.path.join(HERE, "results.tsv")
    new = not os.path.exists(path)
    with open(path, "a") as f:
        if new:
            f.write("utc\trun\tseed\tbook\tprior\tthin\tN\tblended\tparticle\tbook_acc\tscore\tnote\n")
        f.write("\t".join(str(x) for x in fields) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "control", "target"])
    ap.add_argument("--seeds", type=int, nargs="+", default=[1])
    ap.add_argument("--book", default="THE972")
    ap.add_argument("--prior", default="WE028")
    ap.add_argument("--thin", type=float, default=0.0)
    ap.add_argument("--baseline", action="store_true")
    ap.add_argument("--restarts", type=int, default=3)
    a = ap.parse_args()
    C = corpora()
    tm = target_msgs()
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    stamp = lambda: time.strftime("%Y-%m-%d %H:%M", time.gmtime())
    if a.cmd == "build":
        lm = nm.get_lm(C, 3)
        words = []
        for f in nm.CONTROL_LETTERS:
            words += nm.rebuild_words(open(os.path.join(nm.CODES_DIR, "decodes", f)).read(), lm.vocab)
        open(os.path.join(HERE, "control_plain.txt"), "w").write(" ".join(words) + "\n")
        with open(os.path.join(HERE, "controls.tsv"), "w") as f:
            f.write("book\tprior\tseed\tstats_json\n")
            for book, prior in (("THE972", "WE028"), ("WE028", "THE972")):
                for s in (1, 2, 3):
                    with contextlib.redirect_stdout(io.StringIO()):
                        nm.make_control({}, s, C, {"vocab_order": 1, "book": book, "prior": prior, "target_msgs": tm})
                    f.write(f"{book}\t{prior}\t{s}\t{json.dumps(nm._LAST_CONTROL['stats'])}\n")
        print(open(os.path.join(HERE, "controls.tsv")).read())
        return
    if a.cmd == "control":
        for s in a.seeds:
            par = {"vocab_order": 1, "book": a.book, "prior": a.prior, "target_msgs": tm}
            cm, plain, train = nm.make_control({}, s, C, par)
            classes = list(nm._LAST_CONTROL["classes"]); st = dict(nm._LAST_CONTROL["stats"])
            bk = [w for w, k in zip(plain.split(), classes) if k == "B"]
            runs = [("V1", {**par, "thin": a.thin, "_truth_book": bk, "book_size": st["book_list"]})]
            if a.baseline:
                runs.append(("ARM-C1", {"target_msgs": tm}))
            for name, p in runs:
                t0 = time.time()
                dec, sc, info = nm.solve(cm, {}, s, a.restarts, train, p)
                bl, pa, bo = per_class(dec, plain, classes)
                tag = f"{name}-{a.book}-{a.prior}-t{a.thin}-s{s}"
                open(os.path.join(HERE, "out", tag + ".txt"), "w").write(dec + "\n")
                row([stamp(), name, s, a.book, a.prior, a.thin, st["coded"], f"{bl:.3f}", f"{pa:.3f}", f"{bo:.3f}",
                     f"{sc:.1f}", f"win={info.get('win', '-')} {time.time() - t0:.0f}s cov={st['book_token_coverage']}"])
                print(f"{tag}: blended {bl:.3f} particle {pa:.3f} book {bo:.3f} ({time.time() - t0:.0f}s)", flush=True)
        return
    # target: V1 on the target and on its shuffled order, both through the en18 judge
    flat = [t for m in tm for t in m]
    sh = flat[:]; random.Random(1).shuffle(sh)
    for name, msgs in (("target", tm), ("shuffled", [sh])):
        dec, sc, info = nm.solve(msgs, {}, 1, a.restarts, C, {"vocab_order": 1, "prior": a.prior})
        path = os.path.join(HERE, "out", f"V1-{name}-{a.prior}.txt")
        open(path, "w").write(dec + "\n")
        j = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "judge_plaintext.py"),
                            os.path.join(ROOT, "specs", "armstrong-madison-1808.json"), "--file", path],
                           capture_output=True, text=True).stdout.strip().splitlines()
        row([stamp(), f"V1-{name}", 1, "-", a.prior, 0, len(flat), "-", "-", "-", f"{sc:.1f}", j[-1] if j else "?"])
        print(name, j[-3:] if j else "?")


if __name__ == "__main__":
    main()

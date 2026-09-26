#!/usr/bin/env python3
"""Offline test for tools/family_run.py (25 Sept 2026, TOOL-FAMILY). No network. Builds a synthetic spec in a
temp dir: a 300-letter English window from tools/data/pg1661_holmes.txt enciphered here under a random simple
substitution; runs the masc family with the control first and checks (1) the control reads above 0.9, (2) the
target row and decode file are written and the decode reads the known plaintext above 0.9, (3) a control below
the gate exits 3 without a target row or decode, (4) the HYPOTHESES.md table is well formed (every row has the
header's cell count, the marker is present once), (5) a --label with a rule 10 word is refused (exit 2), (6) the periodic_vigenere family reads the same window
under a period-7 key (control and target above 0.9, key recovered, judge PASS in the row), (7) --shuffle-target permutes
the target's own tokens (N/K unchanged), writes a distinctly-suffixed decode file, and marks the row.
(8) a --label given adds a corpus/label-derived suffix to the decode filename so two runs of the same family/seed
on different corpora never collide (bBLZ4, 26 Sept 2026: bBLZ3's German-corpus masc-1 run silently overwrote
bBLZ2's English masc-1.txt); no --label keeps the exact old bare filename.
Run: python3 tools/tests/test_family_run.py   (about a minute)"""
import glob, json, os, random, re, subprocess, sys, tempfile, time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, "tools", "family_run.py")
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp  # noqa: E402


def run(*args):
    r = subprocess.run([sys.executable, TOOL, *args], capture_output=True, text=True, cwd=ROOT)
    return r.returncode, r.stdout + r.stderr


def test_family_run():
    t0 = time.time()
    holmes = jp.read_corpus(os.path.join(ROOT, "tools", "data", "pg1661_holmes.txt"))
    text = jp.fold(holmes)
    plain = text[200000:200300]
    assert len(plain) == 300
    rng = random.Random(7)
    letters = list("abcdefghijklmnopqrstuvwxyz")
    perm = letters[:]
    rng.shuffle(perm)
    key = dict(zip(letters, perm))
    cipher = "".join(key[a] for a in plain)
    with tempfile.TemporaryDirectory() as d:
        spec = {"slug": "synthetic-masc-test", "alphabet": "a-z",
                "ciphertext": [cipher[i:i + 100] for i in range(0, 300, 100)],
                "matched_control": "English window, N=300, simple substitution",
                "judge": {"language": "en", "letters_min": 250, "letters_max": 350, "control_samples": 40}}
        sp = os.path.join(d, "synthetic-masc-test.json")
        json.dump(spec, open(sp, "w"))
        out = os.path.join(d, "ciphers", "synthetic-masc-test", "HYPOTHESES.md")
        # decode files go to ciphers/<slug>/families under ROOT; keep the slug unique and clean up after
        fdir = os.path.join(ROOT, "ciphers", "synthetic-masc-test")
        try:
            # (5) rule 10 word in the label is refused before anything runs
            rc, log = run(sp, "--family", "masc", "--label", "a new reading", "--out", out)
            assert rc == 2, (rc, log)
            assert not os.path.exists(out)
            # (1)+(2) control first, gate met, target run
            rc, log = run(sp, "--family", "masc", "--seed", "1", "--seeds", "2", "--restarts", "3",
                          "--param", "iters=150000", "--gate", "0.9", "--out", out, "--label", "offline test")
            assert rc == 0, (rc, log)
            ctl = [float(m) for m in re.findall(r"CONTROL seed \d+: .* recovery ([0-9.]+)", log)]
            assert len(ctl) == 2 and min(ctl) > 0.9, (ctl, log)
            # a --label was given, so the decode filename carries a label-derived suffix (8), never the bare name
            assert not os.path.exists(os.path.join(fdir, "families", "masc-1.txt")), log
            cand = glob.glob(os.path.join(fdir, "families", "masc-1-*.txt"))
            assert len(cand) == 1, (cand, log)
            dec_path = cand[0]
            dec = "".join(l.strip() for l in open(dec_path) if not l.startswith("#"))
            # the anneal folds j->i and v->u, so compare on the tool's own 24-letter folding
            import homophonic_anneal as ha
            truth = ha.fold(plain)
            assert len(dec) == len(truth), (len(dec), len(truth))
            acc = sum(a == b for a, b in zip(dec, truth)) / len(truth)
            assert acc > 0.9, (acc, dec[:80], truth[:80])
            table = open(out, encoding="utf-8").read()
            assert "yes (gate 0.9)" in table and "| masc |" in table and "offline test" in table, table
            assert re.search(r"\| (PASS|FAIL)", table), table  # the judge verdict line is in the row
            # (3) control below gate: exit 3, control row written, no target row, no second decode file
            rc, log = run(sp, "--family", "masc", "--seed", "5", "--seeds", "1", "--restarts", "1",
                          "--param", "iters=3000", "--gate", "1.01", "--out", out, "--label", "gate check")
            assert rc == 3 and "CONTROL BELOW GATE" in log, (rc, log)
            assert not os.path.exists(os.path.join(fdir, "families", "masc-5.txt"))
            table = open(out, encoding="utf-8").read()
            assert "not run (CONTROL BELOW GATE)" in table and "no (gate 1.01)" in table, table
            # (4) well-formed table: one marker, every row has the header's cell count, no rule 10 words
            assert table.count("family_run.py table") == 1, table
            rows = [l for l in table.splitlines() if l.startswith("|")]
            widths = {l.count("|") for l in rows}
            assert widths == {10}, (widths, rows)
            assert len(rows) == 4, rows  # header, separator, target row, gate row
            assert not re.search(r"\b(solved|new|first|unpublished)\b", table, re.I), table
            # (7) --shuffle-target: target's own tokens permuted (false-positive floor); decode file gets a
            # distinct suffix so it never collides with the real target-1.txt, N/K unchanged, row marks the seed
            rc, log = run(sp, "--family", "masc", "--seed", "9", "--seeds", "1", "--restarts", "2",
                          "--param", "iters=20000", "--gate", "0.0", "--shuffle-target", "3",
                          "--out", out, "--label", "offline test shuffle")
            assert rc == 0, (rc, log)
            assert "target letters shuffled, seed 3" in log and "N=300 signs, K=" in log, log
            assert not os.path.exists(os.path.join(fdir, "families", "masc-9-shuffle3.txt")), log  # label-suffixed now
            shuf_cand = glob.glob(os.path.join(fdir, "families", "masc-9-shuffle3-*.txt"))
            assert len(shuf_cand) == 1 and not os.path.exists(os.path.join(fdir, "families", "masc-9.txt")), (shuf_cand, log)
            shuf_path = shuf_cand[0]
            shuf_dec = "".join(l.strip() for l in open(shuf_path) if not l.startswith("#"))
            assert len(shuf_dec) == len(truth), (len(shuf_dec), len(truth))
            assert "TARGET LETTERS SHUFFLED (seed 3" in open(shuf_path).read()
            table = open(out, encoding="utf-8").read()
            assert "shuffle_target=3" in table, table
            # periodic_vigenere on a second synthetic spec: the same window under a period-7 Vigenere key
            # written as three lines (continuous key); the control uses the period scanned on the target
            A = "abcdefghijklmnopqrstuvwxyz"
            vkey = "holmesx"
            vc = "".join(A[(A.index(a) + A.index(vkey[i % 7])) % 26] for i, a in enumerate(plain))
            vspec = dict(spec, slug="synthetic-vig-test", ciphertext=[vc[i:i + 100] for i in range(0, 300, 100)])
            vp = os.path.join(d, "synthetic-vig-test.json")
            json.dump(vspec, open(vp, "w"))
            vout = os.path.join(d, "ciphers", "synthetic-vig-test", "HYPOTHESES.md")
            rc, log = run(vp, "--family", "periodic_vigenere", "--seeds", "2", "--restarts", "2", "--gate", "0.9",
                          "--out", vout, "--label", "offline test")
            assert rc == 0, (rc, log)
            vctl = [float(m) for m in re.findall(r"CONTROL seed \d+: .* recovery ([0-9.]+)", log)]
            assert len(vctl) == 2 and min(vctl) > 0.9, (vctl, log)
            vcand = glob.glob(os.path.join(ROOT, "ciphers", "synthetic-vig-test", "families", "periodic_vigenere-1-*.txt"))
            assert len(vcand) == 1, (vcand, log)  # label-suffixed, same as the masc case above
            vdec_path = vcand[0]
            vdec = "".join(l.strip() for l in open(vdec_path) if not l.startswith("#"))
            vacc = sum(a == b for a, b in zip(vdec, plain)) / 300
            assert vacc > 0.9, (vacc, vdec[:80])
            assert '"key": "holmesx"' in open(vdec_path).read() and "| PASS" in open(vout).read(), log
            # (8) the actual bug (bBLZ4): same family/seed/params, different --corpus, both --label'd -> two
            # distinct decode files, neither overwriting the other (was: both wrote masc-1-iters=20000.txt)
            rc, log = run(sp, "--family", "masc", "--seed", "1", "--seeds", "1", "--restarts", "2",
                          "--param", "iters=20000", "--gate", "0.0",
                          "--corpus", os.path.join(ROOT, "tools", "data", "pg1661_holmes.txt"),
                          "--out", out, "--label", "corpus A run")
            assert rc == 0, (rc, log)
            a_cand = glob.glob(os.path.join(fdir, "families", "masc-1-iters=20000-*holmes*.txt"))
            assert len(a_cand) == 1, (a_cand, log)
            rc, log = run(sp, "--family", "masc", "--seed", "1", "--seeds", "1", "--restarts", "2",
                          "--param", "iters=20000", "--gate", "0.0",
                          "--corpus", os.path.join(ROOT, "tools", "data", "pg2701_mobydick.txt"),
                          "--out", out, "--label", "corpus B run")
            assert rc == 0, (rc, log)
            b_cand = glob.glob(os.path.join(fdir, "families", "masc-1-iters=20000-*mobydick*.txt"))
            assert len(b_cand) == 1, (b_cand, log)
            assert a_cand[0] != b_cand[0] and os.path.exists(a_cand[0]), (a_cand, b_cand, log)  # A survived B's run
            # no --label given at all: falls back to the exact old bare-plus-param name, no corpus tag added
            rc, log = run(sp, "--family", "masc", "--seed", "1", "--seeds", "1", "--restarts", "2",
                          "--param", "iters=20000", "--gate", "0.0",
                          "--corpus", os.path.join(ROOT, "tools", "data", "pg2701_mobydick.txt"), "--out", out)
            assert rc == 0, (rc, log)
            bare_path = os.path.join(fdir, "families", "masc-1-iters=20000.txt")
            assert os.path.exists(bare_path), (log, os.listdir(os.path.join(fdir, "families")))
            assert os.path.exists(a_cand[0]) and os.path.exists(b_cand[0]), "unlabeled run must not touch labeled files"
            # --dry-run touches nothing
            before = os.path.getmtime(out)
            rc, log = run(sp, "--family", "masc", "--dry-run", "--out", out)
            assert rc == 0 and "N=300 signs, K=" in log and os.path.getmtime(out) == before, log
        finally:
            import shutil
            shutil.rmtree(fdir, ignore_errors=True)
            shutil.rmtree(os.path.join(ROOT, "ciphers", "synthetic-vig-test"), ignore_errors=True)
    print(f"ok family_run: masc control {ctl}, target accuracy {acc:.3f}, gate exit 3, table 4 rows; "
          f"periodic_vigenere control {vctl}, target accuracy {vacc:.3f}; {time.time() - t0:.0f}s")


if __name__ == "__main__":
    test_family_run()

#!/usr/bin/env python3
"""Hard-EM alignment of 5799's cipher codes to Groen IV, Lettre CDIX's printed plaintext.

Same algorithm as ciphers/jan-van-nassau-1572-75/align/em_align.py (hard-EM: each cipher code
emits 0-3 letters of the printed span; iterate counts to convergence), specialised to 5799's
own ciphertext_5799.tsv (mixed clear/=word and bare-numeral rows) and its three numeral runs
that fall between clear anchor words already transcribed on the page. The clear words already
match Groen's print at each anchor (checked by eye against groen/groen_IV_CDIX.txt), which is
what licenses treating this as known-plaintext alignment (rule 4 grade C) rather than
cryptanalysis from scratch.

Note (26 Sept 2026, LEARN-2026-09-26-0058): tools/interlinear_align.py's `align` subcommand already does this
same DP/hard-EM job in general form; kept here as-is because this file's output (pairs_5799.tsv) is already
cited in NOTES.md. A future letter in this pool should call the shared tool instead of copying this file again.

Usage: python3 em_align_5799.py [--check]
Writes key_5799.tsv (code, value, grade, source, note) and align/pairs_5799.tsv.
"""
import csv, math, sys, os, unicodedata, collections

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)
CIPHERTEXT = os.path.join(TARGET, "ciphertext_5799.tsv")
KEY_OUT = os.path.join(TARGET, "key_5799.tsv")
PAIRS_OUT = os.path.join(HERE, "pairs_5799.tsv")


def letters(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if c.isalpha() and c.isascii())
    return s.replace("j", "i").replace("v", "u").replace("w", "uu")


# Three print spans, copied verbatim from Groen IV Lettre CDIX (groen/groen_IV_CDIX.txt),
# matched by eye to the text between consecutive clear (=) anchor words on the transcribed page.
RUN_PRINT_SPANS = [
    "que aulcun appointement se polra faire ou non",
    "l'Empereur auroit escrit au Conte Palatin qu'il vouloit assister le Duc le priant",
    "commandant de faire le mesme",
    "paix ny d'appointement",
]

# (line, idx) literal calendar digits inside otherwise-clear closing lines: never cipher codes.
LITERAL_DATE_CELLS = {("05799_p1_L14", "16"), ("05799_p1_L15", "3")}


def load_rows():
    rows = []
    with open(CIPHERTEXT) as f:
        for r in csv.DictReader(f, delimiter="\t"):
            rows.append(r)
    return rows


def build_runs(rows):
    runs = []
    cur = None
    for r in rows:
        sign = r["sign"]
        is_clear = sign.startswith("=")
        is_literal_date = (r["line"], r["position"]) in LITERAL_DATE_CELLS
        if is_clear or is_literal_date:
            if cur is not None:
                runs.append(cur)
                cur = None
            continue
        if cur is None:
            cur = {"codes": [], "pos": []}
        cur["codes"].append(sign)
        cur["pos"].append((r["line"], r["position"]))
    if cur is not None:
        runs.append(cur)
    return runs


PRIOR = {0: math.log(0.06), 1: math.log(0.85), 2: math.log(0.06), 3: math.log(0.03)}


NULL_STREAK_PENALTY = math.log(0.15)  # a real cipher's nulls scatter; penalise a null right after a null


def align(groups, plain, C, T, first):
    # state (i, j, was_null): was_null tracks whether position i-1's emission was k=0, to
    # discourage the DP from clustering the run's forced surplus-code nulls together (an
    # artifact seen without this penalty: 9-11 consecutive nulls in one spot of a run,
    # implausible for a real homophonic table's null design -- see NOTES.md caveat).
    n, m = len(groups), len(plain)
    NEG = -1e18
    D = [[[NEG, NEG] for _ in range(m + 1)] for _ in range(n + 1)]
    B = [[[None, None] for _ in range(m + 1)] for _ in range(n + 1)]
    D[0][0][0] = 0
    for i in range(n):
        g = groups[i]
        tot = T.get(g, 0)
        for j in range(m + 1):
            for wn in (0, 1):
                if D[i][j][wn] == NEG:
                    continue
                base = D[i][j][wn]
                for k in (0, 1, 2, 3):
                    if j + k > m:
                        continue
                    ch = plain[j:j + k] if k else "-"
                    if first:
                        s = PRIOR[k]
                    else:
                        s = PRIOR[k] + math.log((C.get((g, ch), 0) + 0.02) / (tot + 1.0))
                    if k == 0 and wn == 1:
                        s += NULL_STREAK_PENALTY
                    nwn = 1 if k == 0 else 0
                    if base + s > D[i + 1][j + k][nwn]:
                        D[i + 1][j + k][nwn] = base + s
                        B[i + 1][j + k][nwn] = (j, ch, wn)
    jbest, wnbest = max(
        ((j, wn) for j in range(m + 1) for wn in (0, 1)),
        key=lambda jw: D[n][jw[0]][jw[1]] - 3.0 * abs(m - jw[0]),
    )
    out = []
    j, wn = jbest, wnbest
    for i in range(n, 0, -1):
        pj, ch, pwn = B[i][j][wn]
        out.append(ch)
        j, wn = pj, pwn
    return out[::-1], jbest


def main(argv):
    check = "--check" in argv
    rows = load_rows()
    raw_runs = build_runs(rows)
    assert len(raw_runs) == len(RUN_PRINT_SPANS), (
        f"expected {len(RUN_PRINT_SPANS)} numeral runs, found {len(raw_runs)} -- "
        "ciphertext_5799.tsv layout changed, update RUN_PRINT_SPANS"
    )
    runs = []
    for r, span in zip(raw_runs, RUN_PRINT_SPANS):
        runs.append({"groups": r["codes"], "pos": r["pos"], "span": span, "plain": letters(span)})

    C, T, prev = collections.Counter(), collections.Counter(), None
    res = None
    for it in range(20):
        newC, newT, res = collections.Counter(), collections.Counter(), []
        for r in runs:
            a, used = align(r["groups"], r["plain"], C, T, it == 0)
            res.append((r, a, used))
            for g, ch in zip(r["groups"], a):
                newC[(g, ch)] += 1
                newT[g] += 1
        C, T = newC, newT
        sig = tuple(tuple(x[1]) for x in res)
        if sig == prev:
            break
        prev = sig
    iterations = it + 1

    with open(PAIRS_OUT, "w") as f:
        f.write("line\tidx\tcode\tchunk\trun_span\n")
        for r, a, used in res:
            for (line, idx), g, ch in zip(r["pos"], r["groups"], a):
                f.write(f"{line}\t{idx}\t{g}\t{ch}\t{r['span'][:60]}\n")

    # Per-code winning chunk (mode over its occurrences) restricted to single letters (k=1),
    # since R18's sibling table (key.tsv) is a strict one-code-one-letter homophonic design and
    # the brief's fit-check hypothesis is a consecutive-block variant of the same design.
    by_code = collections.defaultdict(list)
    for r, a, used in res:
        for g, ch in zip(r["groups"], a):
            by_code[g].append(ch)

    rows_out = []
    for code in sorted(by_code, key=lambda x: int(x)):
        chunks = by_code[code]
        letter_chunks = [c for c in chunks if len(c) == 1 and c != "-"]
        if letter_chunks:
            cnt = collections.Counter(letter_chunks)
            value, n_match = cnt.most_common(1)[0]
        else:
            cnt = collections.Counter(chunks)
            value, n_match = cnt.most_common(1)[0]
            value = "NULL" if value == "-" else value
        n_total = len(chunks)
        rows_out.append((code, value, n_match, n_total))

    new_key_lines = ["code\tvalue\tgrade\tsource\tnote\n"]
    for code, value, n_match, n_total in rows_out:
        # rule 4: C only where >=2 independent occurrences agree on a majority value;
        # a code seen once in this small, EM-clustered alignment (see NOTES.md caveat
        # on null placement) is M, uncertain, not a confirmed known-plaintext match.
        grade = "C" if (n_total >= 2 and n_match / n_total > 0.5) else "M"
        new_key_lines.append(
            f"{code}\t{value}\t{grade}\taligned to Groen IV CDIX\tmatches plaintext {n_match}x of {n_total}\n"
        )
    new_key_text = "".join(new_key_lines)
    if check:
        old_key_text = open(KEY_OUT).read() if os.path.exists(KEY_OUT) else ""
        if old_key_text != new_key_text:
            print("CHECK FAILED: regenerated key_5799.tsv differs from the committed file")
            return 1
        print("CHECK: key_5799.tsv regenerates identical to the committed file")
        return 0
    with open(KEY_OUT, "w") as f:
        f.write(new_key_text)

    print(f"iterations: {iterations}")
    print(f"runs: {len(runs)}, total codes: {sum(len(r['groups']) for r in runs)}, "
          f"total plaintext letters: {sum(len(r['plain']) for r in runs)}")
    print(f"distinct codes: {len(rows_out)}; codes seen more than once: "
          f"{sum(1 for c in by_code.values() if len(c) > 1)}")
    for r, a, used in res:
        print(r["span"][:60], "|", "".join(x if x != "-" else "_" for x in a),
              f"({used}/{len(r['plain'])} letters used)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

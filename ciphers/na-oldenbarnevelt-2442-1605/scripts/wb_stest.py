#!/usr/bin/env python3
"""OLD-WB (10 Oct 2026): word-boundary-insensitive S test on leaves 004/005/007 (transcription/PREREG_OLD-WB.md).

Sign agreement is judged on each line's concatenated sign string (minimum-edit alignment of the reconciled line to the
best-matching line of each blind pass, token boundaries dropped); lexicon cover accepts a token whose decode is a lexicon
word or which lies in a 2-3 cipher-token window whose joined decode segments completely into lexicon words (pieces >= 2
letters or a/e/i/o/u). S = sign-agreed AND covered. Matched control: the same 120 vowel-map permutations as OLD-O2.

  python3 scripts/wb_stest.py            print target numbers, the control, write depth/wb_tokens_OLDWB.tsv
  python3 scripts/wb_stest.py --check    exit 1 if depth/wb_tokens_OLDWB.tsv differs from a fresh run
"""
import itertools, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import decode_L457 as D  # noqa: E402

LEAVES = ("L4", "L5", "L7")
SINGLE = set("aeiou")


def align_agree(r, p):
    """Per character of r: True if aligned to an identical character of p (one Levenshtein alignment, ties diag>del>ins)."""
    n, m = len(r), len(p)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = min(dp[i - 1][j - 1] + (r[i - 1] != p[j - 1]), dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    ok = [False] * n
    i, j = n, m
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j - 1] + (r[i - 1] != p[j - 1]):
            ok[i - 1] = r[i - 1] == p[j - 1]; i -= 1; j -= 1
        elif dp[i][j] == dp[i - 1][j] + 1:
            i -= 1
        else:
            j -= 1
    return ok


def best_str(normed, plines):
    s = "".join(normed)
    best, bd = "", 1e9
    for toks in plines.values():
        x = "".join(toks)
        dd = D.lev(s, x) / max(len(s), 1)
        if dd < bd:
            best, bd = x, dd
    return best if bd < 0.6 else ""


def structure():
    """Key-independent part: per line, list of (raw, cipher, abbr, digits, sign_agreed)."""
    passes = {(lf, s): D.pass_lines(lf, s, "O2", "o4") for lf in LEAVES for s in "AB"}
    out = []
    for (blk, ln), toks in D.rec_lines("O2").items():
        if blk not in LEAVES:
            continue
        toks = [t for t in toks if t != "[del]"]
        normed = [D.sn(D.core(t), "o4") for t in toks]
        r = "".join(normed)
        ag = [align_agree(r, best_str(normed, passes[(blk, s)])) for s in "AB"]
        rows, pos = [], 0
        for t, nm in zip(toks, normed):
            k = len(nm)
            agreed = all(ag[0][pos:pos + k]) and all(ag[1][pos:pos + k]) and k > 0
            pos += k
            cipher = bool(re.search(r"\d", t))
            rows.append(dict(raw=t, cipher=cipher, abbr=bool(D.ABBR.match(t)), agreed=agreed,
                             digits=sum(c in D.VOW for c in D.core(t)) if cipher else 0))
        out.append((blk, ln, rows))
    return out


def word(t, key):
    return D.fold(re.sub(r"[^a-zñ]", "", "".join(key.get(ch, ch) for ch in D.core(t)).lower()))


def segments(s, lex, memo):
    if s in memo:
        return memo[s]
    n = len(s)
    ok = [True] + [False] * n
    for i in range(1, n + 1):
        for j in range(i):
            if ok[j]:
                w = s[j:i]
                if (len(w) >= 2 and w in lex) or (len(w) == 1 and w in SINGLE):
                    ok[i] = True
                    break
    memo[s] = ok[n] and n > 0
    return memo[s]


def grade(struct, key, lex, memo):
    res = []
    for blk, ln, rows in struct:
        words = [word(r["raw"], key) if r["cipher"] and not r["abbr"] else "" for r in rows]
        cov = [False] * len(rows)
        for i, r in enumerate(rows):
            if r["cipher"] and r["agreed"] and (r["abbr"] or (words[i] in lex)):
                cov[i] = True
        for w in (2, 3):
            for i in range(len(rows) - w + 1):
                win = rows[i:i + w]
                if all(x["cipher"] and not x["abbr"] and x["agreed"] for x in win):
                    if segments("".join(words[i:i + w]), lex, memo):
                        for k in range(i, i + w):
                            cov[k] = True
        for i, r in enumerate(rows):
            g = ("S" if r["agreed"] and cov[i] else "M") if r["cipher"] else "clear"
            res.append((blk, ln, i + 1, r, words[i], g))
    return res


def stats(res, leaves_share=("L4", "L7")):
    sh = [g == "S" for blk, ln, i, r, w, g in res if r["cipher"] and not r["abbr"] and blk in leaves_share]
    share = sum(sh) / max(len(sh), 1)
    best, per = 0, {}
    for lf in LEAVES:
        cur = b = 0
        for blk, ln, i, r, w, g in res:
            if blk != lf or not r["cipher"]:
                continue
            cur = cur + r["digits"] if g == "S" else 0
            b = max(b, cur)
        per[lf] = b
        best = max(best, b)
    return share, best, per


def longest_words(res):
    out = {}
    for lf in LEAVES + (None,):
        cur, ws, best, bw = 0, [], 0, []
        for blk, ln, i, r, w, g in res:
            if lf and blk != lf:
                continue
            if not r["cipher"]:
                if cur:
                    ws.append(r["raw"])
                continue
            if g == "S":
                cur += r["digits"]; ws.append(w or "V.S.")
                if cur > best:
                    best, bw = cur, list(ws)
            else:
                cur, ws = 0, []
        out[lf] = (best, bw)
    return out


def main():
    lex = D.lexicon()
    memo = {}
    st = structure()
    res = grade(st, D.KEY, lex, memo)
    lines = ["block\tline\ttoken_index\traw_token\tdecode\tdigits\tsign_agreed\tgrade_WB"]
    for blk, ln, i, r, w, g in res:
        lines.append(f"{blk}\t{ln}\t{i}\t{r['raw']}\t{w if r['cipher'] else r['raw']}\t{r['digits']}\t{int(r['agreed'])}\t{g}")
    tsv = "\n".join(lines) + "\n"
    path = os.path.join(D.T, "depth/wb_tokens_OLDWB.tsv")
    if "--check" in sys.argv:
        if not os.path.exists(path) or open(path).read() != tsv:
            print("STALE: depth/wb_tokens_OLDWB.tsv"); sys.exit(1)
        print("wb_stest --check: committed WB grades match a fresh run"); return
    open(path, "w").write(tsv)
    # target numbers
    for lf in LEAVES + (None,):
        sub = [x for x in res if x[3]["cipher"] and (lf is None or x[0] == lf)]
        sw = sum(x[5] == "S" for x in sub); mw = len(sub) - sw
        sd = sum(x[3]["digits"] for x in sub if x[5] == "S"); td = sum(x[3]["digits"] for x in sub)
        ag = sum(x[3]["agreed"] for x in sub)
        print(f"{lf or 'L4+L5+L7'}: cipher words {len(sub)} S {sw} M {mw} (sign-agreed {ag}); digits {td}, S {sd} ({sd/max(td,1):.1%})")
    lw = longest_words(res)
    share, best, per = stats(res)
    mw_all = sum(1 for x in res if x[3]["cipher"] and x[5] == "M")
    ad = 1.5 * (6.91 + 2.32 * mw_all) / 1.83
    for lf in LEAVES:
        print(f"longest S stretch {lf}: {lw[lf][0]} digits [{' '.join(lw[lf][1])}]")
    print(f"longest S stretch pooled: {best} digits; floor 24.2; AD with {mw_all} M words {ad:.0f} digits")
    # ceiling: sign-agreed only
    ceil = 0
    for lf in LEAVES:
        cur = 0
        for blk, ln, i, r, w, g in res:
            if blk == lf and r["cipher"]:
                cur = cur + r["digits"] if r["agreed"] else 0
                ceil = max(ceil, cur)
    print(f"diagnostic ceiling (sign-agreed, lexicon ignored): longest {ceil} digits")
    # control
    vals = [D.KEY[d] for d in D.VOW]
    out = []
    for perm in itertools.permutations(vals):
        k = dict(D.KEY); k.update(dict(zip(D.VOW, perm)))
        s, b, _ = stats(grade(st, k, lex, memo))
        out.append((s, b, perm == tuple(vals), "".join(f"{d}={v}" for d, v in zip(D.VOW, perm))))
    tgt = [o for o in out if o[2]][0]
    oth = [o for o in out if not o[2]]
    for idx, name in ((0, "S share L4+L7 (V.S. excl.)"), (1, "longest S stretch pooled (digits)")):
        xs = [o[idx] for o in oth]
        rank = 1 + sum(x >= tgt[idx] for x in xs)
        top = sorted(out, key=lambda o: -o[idx])[:3]
        print(f"control {name}: target {tgt[idx]:.3f} rank {rank} of 120; 119 perms mean {sum(xs)/len(xs):.3f} max {max(xs):.3f};"
              f" perms below target {sum(x < tgt[idx] for x in xs)}/119; top three: " + "; ".join(f"{o[3]} {o[idx]:.3f}" for o in top))
    print(f"(OLD-O2 token-boundary S share L4+L7 for reference: 0.236)")


if __name__ == "__main__":
    main()

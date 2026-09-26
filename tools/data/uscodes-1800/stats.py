#!/usr/bin/env python3
"""ARM-CODES stats unit (CLAUDE.md brief .claude/briefs/runs/2026-09-26-lane-arm-codes.md, item 3).

Offline: reads only the TSVs in this directory and ciphers/armstrong-madison-1808/ciphertext.txt.
Writes stats.tsv beside this script. No cryptanalysis, no decoding of the target -- comparison
statistics only (per the brief: "Do NOT decode the target with any table").
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent.parent
TARGET_CT = REPO / "ciphers" / "armstrong-madison-1808" / "ciphertext.txt"

TABLES = ["WE028.tsv", "THE972_bourdeau.tsv", "THE972_tomokiyo_partial.tsv", "THE972_tomokiyo_clean.tsv"]

# The four passages of real THE=972 usage embedded in Bourdeau's decode972.py (armstrong/decode972.py,
# fetched from github.com/dbourdeau/cyphersolver commit fc0c9e8), copied here as literal token strings
# so this script has no import-time dependency on the cloned repo (which is not committed).
THE972_USAGE = {
    "1808-08-30_ps": "1394 1116 1273 250 1165 1405 972 148 1459 1482 1201 821 130 821 1429 720 970 1482 992 1319 1048 584 687 249 736 1013 750 967 1459 1482 1202 1561 927 1090 1052 832 1482 934 510 860 1459 1482 1320 384 1280 1216 1481 1483 555",
    "1808-02-22": "972 1394 1090 1354 946 985 608 899 1482 1228 1492 297 1001 26 736 1587 916 369 630 1478 860 1090 758 1282 1284 825 1484 1436 1078 368 1463 337 1354 1463 1358 1217 631 463 1354 470 1257 1217 593 383 821 1463 1247 1181 967 860 1479 972 1224 1116 1354 1069 962 396 972 752 1483 61 385 590 1572 1373 380 1478 537 1467 1247 631 578 1116 1165 509 943 590 988 1304 1217 985 351 1431 972 769 803 1354 1467 193 514 1217 972 511 1116 579 821 1429 1484 1165 1201 1157 1082 972 1090 578 882 1257 1480 1479 26 1354 1201 191 690 962 1354 968 1494 1244 1387 305 1587 947 765 1587 87 1478 804 1158 860 1225 1132 1116 927 1090 803 1247 655 1126 1478 550 917 1354 972 236 523 1247 1182 967 933 1088 1078 431",
    "1808-02-15": "632 550 1453 1105 587 541 899 972 1415 1116 1131 1431 1116 1354 1287 427 426 38 897 632 972 249 587 1561 803 772 899 632 621 1086 623 1020 1587 803 741 636 578 590 1097 827 832 1105 1217 632 1419 1105 587 649 419 1367 1373 747 1292 1116 632 817 1089 801 1090 808 1016 1087 790 1105 1005 888 962 1484 417 1217 1089 1177 1001 790 962 590 1482 41 1562 1274 417 1216 1509 795 514 890 1086 1484 1146 741 1001 1116 1105 415 630 1458 1201 307 1217 587 1354 972 1118 1097 827 1217 1228 1492 1405 1078 368 1165 1397 1132 702 1104 1086 1484 765 1587 1146 741 1001 1105 972 1530 1172 817 630 819 1415 972 1492 962 1086 38 316 921 983 1517 872 1366 1268 1463 1124 1121 1116 1225 1165 921 416 1268 1463 492 1090 772 1354 1089 662 514 1105 1484 405 1405 624 1105 1587 947 1165 561 1482 578 972 664 1078 781 1268 427 632 590 193 514 1105 1428 1165 561 1284 1090 972 523 507 1268 1555 1596 484 1105 1116 810 1445 1165 1480 1116 945 1367 1 962 1086 946 972 249 1453 1105 415 316 921 473 1165 1416 383 1116 632 38 1201 1238 849 1354 972 287 1116 312 1164 514 1354 1201 391 968 821 726 897 692 972 187 1116",
    "1808-09-07_frag3414": "1280 18 415 1165 1020 632 972 187 1116 1217 410 391 796 1319 69 1116 392 1503 415 653 772 1226 1201 287 945 166 988 1304",
}


def read_tsv(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        next(f)
        for line in f:
            value, plaintext, grade, source_line = line.rstrip("\n").split("\t")
            rows.append((int(value), plaintext, grade, source_line))
    return rows


def target_tokens():
    text = TARGET_CT.read_text(encoding="utf-8")
    tokens = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        for tok in line.split():
            if tok in ("*", "**", "***") or tok == "<..>":
                continue
            tokens.append(int(tok))
    return tokens


def last_digit_dist(values):
    dist = [0] * 10
    for v in values:
        dist[v % 10] += 1
    return dist


def hundred_block_dist(values):
    from collections import Counter
    return Counter((v // 100) * 100 for v in values)


def spearman_rho(values, plaintexts):
    """Rank correlation between value order and alphabetical order of plaintext (no tie correction)."""
    n = len(values)
    if n < 2:
        return None
    order_by_value = sorted(range(n), key=lambda i: values[i])
    value_rank = [0] * n
    for r, i in enumerate(order_by_value):
        value_rank[i] = r
    order_by_word = sorted(range(n), key=lambda i: plaintexts[i].lower())
    word_rank = [0] * n
    for r, i in enumerate(order_by_word):
        word_rank[i] = r
    d2 = sum((value_rank[i] - word_rank[i]) ** 2 for i in range(n))
    return 1 - (6 * d2) / (n * (n * n - 1))


def alphabetical_blocks(values, plaintexts):
    pairs = sorted(zip(values, plaintexts), key=lambda p: p[0])
    blocks = 1
    prev = None
    for _, word in pairs:
        w = word.lower()
        if prev is not None and w < prev:
            blocks += 1
        prev = w
    return blocks


def clean_word(word):
    return re.sub(r"[^a-zA-Z]", "", word).lower()


def top_homophones(plaintexts, n=10):
    from collections import Counter
    c = Counter(clean_word(w) for w in plaintexts if clean_word(w))
    return c.most_common(n)


def main():
    out = []
    header = ["dataset", "entry_count", "value_min", "value_max", "last_digit_0-9",
              "hundred_block_counts", "spearman_rho_value_vs_alpha", "alphabetical_blocks", "top10_homophones"]
    out.append(header)

    for name in TABLES:
        rows = read_tsv(HERE / name)
        values = [r[0] for r in rows]
        plaintexts = [r[1] for r in rows]
        rho = spearman_rho(values, plaintexts)
        blocks = alphabetical_blocks(values, plaintexts)
        homs = top_homophones(plaintexts)
        out.append([
            name, str(len(rows)), str(min(values)), str(max(values)),
            ",".join(str(d) for d in last_digit_dist(values)),
            ";".join(f"{k}:{v}" for k, v in sorted(hundred_block_dist(values).items())),
            f"{rho:.3f}" if rho is not None else "n/a",
            str(blocks),
            ";".join(f"{w}={c}" for w, c in homs),
        ])

    for label, tokstr in THE972_USAGE.items():
        values = [int(t) for t in tokstr.split()]
        out.append([
            f"THE972_usage_{label}", str(len(values)), str(min(values)), str(max(values)),
            ",".join(str(d) for d in last_digit_dist(values)),
            ";".join(f"{k}:{v}" for k, v in sorted(hundred_block_dist(values).items())),
            "n/a (usage instance, not a table)", "n/a", "n/a",
        ])
    all_usage = [int(t) for tokstr in THE972_USAGE.values() for t in tokstr.split()]
    out.append([
        "THE972_usage_ALL", str(len(all_usage)), str(min(all_usage)), str(max(all_usage)),
        ",".join(str(d) for d in last_digit_dist(all_usage)),
        ";".join(f"{k}:{v}" for k, v in sorted(hundred_block_dist(all_usage).items())),
        "n/a (usage instance, not a table)", "n/a", "n/a",
    ])

    target = target_tokens()
    distinct = sorted(set(target))
    out.append([
        "armstrong-madison-1808_target_ALL_369_tokens", str(len(target)), str(min(target)), str(max(target)),
        ",".join(str(d) for d in last_digit_dist(target)),
        ";".join(f"{k}:{v}" for k, v in sorted(hundred_block_dist(target).items())),
        "n/a (ciphertext, no known plaintext)", "n/a", "n/a",
    ])
    out.append([
        "armstrong-madison-1808_target_216_distinct", str(len(distinct)), str(min(distinct)), str(max(distinct)),
        ",".join(str(d) for d in last_digit_dist(distinct)),
        ";".join(f"{k}:{v}" for k, v in sorted(hundred_block_dist(distinct).items())),
        "n/a (ciphertext, no known plaintext)", "n/a", "n/a",
    ])

    with open(HERE / "stats.tsv", "w", encoding="utf-8") as f:
        for row in out:
            f.write("\t".join(row) + "\n")

    for row in out:
        print("\t".join(row))


if __name__ == "__main__":
    main()

"""H82 positive control (rule 3, positive-control subsample): does freq.py's Sukhotin --vowels classing
still find the vowels of a known letter cipher when the stream is cut down to the target's size?
Known answer: Ormonde (Tomokiyo ormonde.htm), parsed and keyed by tools/tests/tt_freq_controls.py (the
TT-FREQ C4 harness that PASSed at full length, 0.800 vs order-null 0.545). Windows: contiguous Ormonde
windows holding 132 letter tokens (the target's sub-100 count, 132 groups / 48 values; the target's letters,
if any, are sparser and less adjacent than this, so this control is the favourable case). Gate per the TT-FREQ
pre-registration C4: accuracy >= 0.75 and >= order-null mean + 0.15, reached in the mean over windows."""
import sys, os, re, random
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools", "tests")); sys.path.insert(0, os.path.join(ROOT, "tools"))
import tt_freq_controls as T
toks, word_of, key = T.ormonde()
isl = [bool(re.fullmatch(r"[a-z]", key.get(t, ""))) for t in toks]
print(f"ormonde tokens {len(toks)}, letter tokens {sum(isl)}")
full, _, _ = T.vowel_acc(toks, key)
print(f"full length accuracy {full:.3f}")
NL = 132; K = 20
rows = []
starts = range(0, len(toks), 25)
for s in starts:
    n = 0; e = s
    while e < len(toks) and n < NL:
        n += isl[e]; e += 1
    if n < NL: break
    w = toks[s:e]
    try:
        acc, _, lets = T.vowel_acc(w, key, n_letters=K)
    except Exception as ex:
        continue
    nulls = [T.vowel_acc(T.order_null(w, sd), key, n_letters=K)[0] for sd in range(20)]
    rows.append((s, e - s, len(lets), acc, sum(nulls) / len(nulls)))
for r in rows: print("start %d len %d letters_scored %d acc %.3f null_mean %.3f" % r)
if rows:
    ma = sum(r[3] for r in rows) / len(rows); mn = sum(r[4] for r in rows) / len(rows)
    passed = sum(1 for r in rows if r[3] >= 0.75 and r[3] >= r[4] + 0.15)
    print(f"windows {len(rows)}  mean acc {ma:.3f}  mean null {mn:.3f}  windows passing gate {passed}/{len(rows)}")
    print("CONTROL", "PASS" if ma >= 0.75 and ma >= mn + 0.15 else "BELOW GATE")

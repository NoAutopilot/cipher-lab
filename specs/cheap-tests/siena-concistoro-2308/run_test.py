import sys, random, json
sys.path.insert(0, "/home/user/cipher-lab/tools")
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import judge_plaintext as jp
from pieces import PIECES
from keys import KEYS

CORPORA = jp.LANG_CORPORA["it"]
model = jp.NgramModel([jp.read_corpus(p) for p in CORPORA])

def decode(tokens, key):
    letters = []
    matched = 0
    for t in tokens:
        v = key.get(t)
        if v is None:
            v = key.get(t.upper())
        if v is None:
            v = key.get(t.lower())
        if v and v.isalpha() and len(v) == 1:
            letters.append(v)
            matched += 1
    return "".join(letters), matched, len(tokens)

results = []
for pname, tokens in PIECES.items():
    for kname, key in KEYS.items():
        real_text, matched, total = decode(tokens, key)
        cov_frac = matched / total if total else 0.0
        real_score = model.score(real_text) if len(real_text) >= 4 else None
        real_cover = model.cover(real_text) if real_text else 0.0
        scrambled_scores = []
        scrambled_covers = []
        for seed in (1, 2, 3):
            rnd = random.Random(seed)
            shuf = list(tokens)
            rnd.shuffle(shuf)
            s_text, s_matched, s_total = decode(shuf, key)
            assert s_matched == matched
            if len(s_text) >= 4:
                scrambled_scores.append(model.score(s_text))
            scrambled_covers.append(model.cover(s_text) if s_text else 0.0)
        row = {
            "piece": pname, "key": kname, "sign_coverage": round(cov_frac, 3),
            "matched": matched, "total": total, "decoded_letters": len(real_text),
            "real_score": round(real_score, 3) if real_score is not None else None,
            "scrambled_score_mean": round(sum(scrambled_scores)/len(scrambled_scores), 3) if scrambled_scores else None,
            "real_cover": round(real_cover, 3),
            "scrambled_cover_mean": round(sum(scrambled_covers)/len(scrambled_covers), 3),
            "real_text": real_text,
        }
        results.append(row)

for r in results:
    print(f"{r['piece']:5s} {r['key']:5s} sign_cov={r['sign_coverage']:.3f} ({r['matched']}/{r['total']}) "
          f"decoded_len={r['decoded_letters']:3d} real_score={r['real_score']} scrambled_score_mean={r['scrambled_score_mean']} "
          f"real_cover={r['real_cover']:.3f} scrambled_cover_mean={r['scrambled_cover_mean']:.3f} text={r['real_text'][:60]!r}")

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json"), "w") as f:
    json.dump(results, f, indent=1)

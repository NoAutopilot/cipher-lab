"""build_subset.py -- MCC-CMU (LANE DEFAULT-A1-1140-15, 15 Oct 2026): the CMUdict subset used by token_anneal.py --phonetic.

Source: CMU Pronouncing Dictionary (BSD 2-clause, Carnegie Mellon University), fetched once on 15 Oct 2026 11:58 UTC from
https://raw.githubusercontent.com/cmusphinx/cmudict/master/cmudict.dict (3,618,488 bytes, 135,166 lines,
sha1 2619f7ef5e6dbdd3c1f9ea7e45bdd5e72cc39a0e). The full file is not committed; this subset keeps the first
pronunciation of every word that occurs in the five English corpora the instrument reads (tools/data/en: Pride, Gatsby,
Huck Finn for the LM/pool; Holmes and Moby-Dick for the control), which is every word the instrument can look up.

Regenerate: curl -sS -o cmudict.dict https://raw.githubusercontent.com/cmusphinx/cmudict/master/cmudict.dict
            python3 build_subset.py cmudict.dict cmudict_subset.dict
"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "specs/cheap-tests/mccormick-1999"))
sys.argv, _argv = sys.argv[:1], sys.argv
import token_anneal as T  # noqa: E402
sys.argv = _argv


def main(src, dst):
    need = set(T.corpus_words_from(T.HELDOUT_EN)) | set(T.corpus_words())
    out, seen = [], set()
    for line in Path(src).read_text(encoding="utf-8", errors="replace").splitlines():
        body = line.split("#")[0].strip()
        if not body:
            continue
        w = body.split()[0]
        if "(" in w or w in seen or w.lower() not in need:
            continue
        seen.add(w)
        out.append(body)
    Path(dst).write_text(";;; CMUdict subset (BSD 2-clause, Carnegie Mellon University); see build_subset.py\n".replace(";;;", "#")
                         + "\n".join(out) + "\n")
    print(f"{len(out)} entries of {len(need)} corpus word types")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

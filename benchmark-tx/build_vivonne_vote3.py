#!/usr/bin/env python3
"""VIV-DECH3 (14 Oct 2026, PREREG-VIVDECH3.md): rebuild three Vivonne truth items with a third blind read of the clerk decipherment as a
vote, as NEW items suffixed -3 beside the old ones (the old truth files, sha256s and outputs are never touched).

    python3 benchmark-tx/build_vivonne_vote3.py            # build vivonne1573-f201r-dev-3, -f201v-dev-3, -f103r-confirm2-3
    python3 benchmark-tx/build_vivonne_vote3.py --check    # exit 1 if any -3 file is stale
    python3 benchmark-tx/build_vivonne_vote3.py --null     # PREREG null: pass C taken from a different page; prints only

The three builders (build_vivonne_f201r.py, build_vivonne_f201v.py, build_vivonne_confirm2.py) are imported and run with their code
unchanged; only (1) the letter streams dec67_norm.txt / dec67b_norm.txt / dec_norm.txt, read through a temporary shadow of tx/ whose
three stream files are the three-vote twins from ciphers/.../tx/vote3.py, and (2) the clerk-split mask (vote3's per-letter agreed mask)
are swapped in. Each builder's own alignment control is re-run on the new text and written into the header.
"""
import hashlib, os, shutil, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_vivonne_confirm2 as c2  # noqa: E402
import build_vivonne_f201r as b67  # noqa: E402
import build_vivonne_f211r as b70  # noqa: E402
import build_vivonne_f201v as b201v  # noqa: E402
sys.path.insert(0, c2.TX)
import vote3  # noqa: E402

ROOT, TX = c2.ROOT, c2.TX
NULL = '--null' in sys.argv
CMAP = vote3.NULL_CMAP if NULL else None


def shadow():
    d = tempfile.mkdtemp(prefix='vote3_')
    for n in os.listdir(TX):
        os.symlink(os.path.join(TX, n), os.path.join(d, n))
    for name in vote3.STREAMS:
        os.remove(os.path.join(d, name))
        open(os.path.join(d, name), 'w').write(vote3.stream(name, CMAP)[0] + '\n')
    return d


def mapped(name, n_letters=None):
    txt, mask = vote3.stream(name, CMAP)
    if n_letters is not None:
        assert len(txt) == n_letters, (name, len(txt), n_letters)
    return mask


def head3(body, item, note):
    lines = body.split('\n', 2)
    return lines[0] + ' VIV-DECH3 three-vote rebuild %s (benchmark-tx/build_vivonne_vote3.py, PREREG-VIVDECH3.md; %s).\n%s\n%s' % (
        item, note, lines[1], lines[2])


def item_f201r():
    pub, force, grade, let, stream = b67.load()
    seq = [t[0] for t in stream]
    ctl = b67.control(seq, let, pub)
    body, outs = b67.truth(pub, force, grade, let, stream, ctl)
    return 'vivonne1573-f201r-dev-3', head3(body, 'vivonne1573-f201r-dev-3', 'pass C on ff.205r-205v'), outs, ctl


def item_f201v():
    pub, force, grade, let, mask, stream = b201v.load()
    seq = [t[0] for t in stream]
    ctl = b70.control(seq, let, pub)
    body, outs = b201v.truth(pub, force, grade, let, mask, stream, ctl)
    return 'vivonne1573-f201v-dev-3', head3(body, 'vivonne1573-f201v-dev-3', 'pass C on ff.205v, 206r-206v'), outs, ctl


def item_f103r():
    body, outs, nex, ctrl, rows, offs = c2.build()
    return ('vivonne1573-f103r-confirm2-3', head3(body, 'vivonne1573-f103r-confirm2-3',
                                                  'pass C on ff.108r-108v only; ff.105v-107v two-vote; split confirm2 kept, never a reader-tuning item'),
            outs, ctrl)


def main():
    d = shadow()
    try:
        for m in (c2, b67, b70, b201v):
            m.TX = d
        c2.clerk_mask = lambda n: mapped('dec_norm.txt', n)
        b67.clerk_mask = lambda n: mapped('dec67_norm.txt', n)
        b201v.clerk_mask_b = lambda: mapped('dec67b_norm.txt')
        built = [item_f201r(), item_f201v(), item_f103r()]
    finally:
        shutil.rmtree(d)
    stale = []
    for item, body, outs, ctl in built:
        fl = [l.split('\t') for l in body.splitlines() if l and not l.startswith('#') and not l.startswith('line\t')]
        sc = [r for r in fl if r[5] == 'scored']
        print('%s: positions %d, scored %d, any flag %d (%.3f), clerk-split %d (%.3f); control %s' % (
            item, len(fl), len(sc), sum(1 for r in sc if r[6]), sum(1 for r in sc if r[6]) / len(sc),
            sum(1 for r in sc if 'clerk-split' in r[6]), sum(1 for r in sc if 'clerk-split' in r[6]) / len(sc),
            ctl if isinstance(ctl, str) else '%.3f vs p95 %.3f rank %d' % (ctl['real'], ctl['null_p95'], ctl['rank'])))
        if NULL:
            continue
        truth = os.path.join(HERE, item + '.truth.tsv')
        sha = '%s  %s\n' % (hashlib.sha256(body.encode()).hexdigest(), os.path.basename(truth))
        files = [(truth, body), (truth + '.sha256', sha)] + [(os.path.join(HERE, 'outputs', item, n + '.tsv'), b) for n, b in outs.items()]
        if '--check' in sys.argv:
            stale += [os.path.relpath(p, ROOT) for p, w in files if not os.path.exists(p) or open(p, encoding='utf-8').read() != w]
            continue
        os.makedirs(os.path.join(HERE, 'outputs', item), exist_ok=True)
        for p, w in files:
            open(p, 'w', encoding='utf-8').write(w)
    if '--check' in sys.argv:
        print('stale: ' + ', '.join(stale) if stale else 'ok: -3 truths, sha256 and outputs current')
        sys.exit(1 if stale else 0)


if __name__ == '__main__':
    main()

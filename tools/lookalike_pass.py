#!/usr/bin/env python3
"""Look-alike pass for a symbol-cipher transcription read by two blind passes (LOOKALIKE-TOOL, 2 Oct 2026).

What it is for. Two blind machine passes over a symbol cipher disagree mostly on a few sign pairs that look alike
(on the Nevers/Birago 1572 sheet: T83/X_NEW, T60/T86, T18/T98, T24/T83). Instead of a third full pass, re-read only
the tiles where the readers split or whose label sits in a frequent confusion pair, against a sheet cut showing only the
candidate signs, and fold that re-read in by a fixed 2-of-3 rule. Promoted from ciphers/nevers-birago-fr3251-1572/harvest/
{confusion_1572.py, lookalike_packet.py, lookalike_reconcile.py} (NEVBIR-LOOKALIKE, 2 Oct 2026). Three subcommands:

  confusion AGREEMENT.tsv... --out confusion.tsv [--target LEAF ...]
      Label swaps (unordered pairs) with counts across every two-reader alignment written by reconcile_passes.py-style
      tools (columns idA, idB, status, passage, posA). Only rows with both labels and status 'split*' count; gaps do not.
      An off-sheet label (X_NEW) is a label like any other. Leaf name = the agreement file's parent folder.
  packet --agreement A.tsv --confusion confusion.tsv [--passc passC.tsv] --top 10 --crops DIR --sheet SHEET.png
         --sheet-map MAP.json --out DIR [--run NAME] [--cell 110 --cols 9]
      Flag every tile whose two readers split or whose passC label sits in a top-N pair; candidates per tile are A's,
      B's and passC's labels plus the label's two most frequent confusion partners. A passC row past the end of its
      passage in the alignment (one reader only, e.g. a re-cut line tail) is flagged 'single' with A = its label. Writes <run>_tiles.tsv,
      <run>_candidates.png (only the candidate cells of the blind sheet: ids, never values) and <run>_prompt.md
      (the value-blind re-read prompt: crop paths, tile ids, the passC label sequence for orientation, no key values).
  reconcile --tiles T.tsv --passc passC.tsv --reread R.tsv --out passD.tsv [--alt passD_alt.tsv] [--focus focus.tsv]
      The rule, fixed before any score is computed: a firm (H/M, not SPLIT) re-read that matches reader A or reader B
      settles the tile at 2-of-3 (the re-read label wins); anything else stays UNSETTLED and keeps the passC label (a third
      reader alone does not overturn two) and goes to focus.tsv (sid<TAB>question) for tools/sign_sorter.py --focus.
      --alt writes the secondary sequence taking every firm re-read label (a pointer only, never the primary).
      Residual disagreement = unsettled / all signs (a 2-of-3 figure, not the two-reader rate, and not true error).
  (The brief named `reconcile --passA --passB`; reader A's and B's aligned labels reach reconcile through the tiles
  file the packet wrote from the agreement alignment, so the raw passes are not re-aligned here.)

Known-answer result (LOOKALIKE-TOOL, 2 Oct 2026, no.87 f.178r + f.179r against the clerk's clear sheet on canvas 182):
see LESSONS.md "Look-alike pass" for the before/after true error; read it before trusting a residual as reader error.

Must NOT be used for: settling the sign inventory itself (which shapes are one sign, which cell is a bad cut) -- when the
two passes split on more than about a tenth of signs because the alphabet is unsettled, that is the owner's sign sorter
(CLAUDE.md Usage 6), and this pass would only make three machine readers agree on a wrong sheet. Nor for a single-pass
transcription (no A/B split to vote on), nor as a source of S grades on its own: its residual is agreement, not truth.

Offline test: python3 tools/tests/test_lookalike_pass.py
"""
import argparse, collections, csv, json, os, sys
from pathlib import Path


def _read(p):
    return list(csv.DictReader(open(p, newline=''), delimiter='\t'))


def _write(p, rows, fields=None):
    with open(p, 'w', newline='') as o:
        w = csv.DictWriter(o, fieldnames=fields or list(rows[0]), delimiter='\t', lineterminator='\n')
        w.writeheader(); w.writerows(rows)


def confusion(files, out, targets=()):
    cnt, tgt, tot = collections.Counter(), collections.Counter(), 0
    ex = collections.defaultdict(list)
    for f in files:
        leaf = Path(f).parent.name
        for r in _read(f):
            a, b, st = r.get('idA', ''), r.get('idB', ''), r.get('status', '')
            if not a or not b:
                continue
            tot += 1
            if not st.startswith('split') or a == b:
                continue
            k = tuple(sorted((a, b)))
            cnt[k] += 1
            if leaf in targets:
                tgt[k] += 1
            if len(ex[k]) < 4:
                ex[k].append(f"{leaf}:{r.get('passage', '')}.{r.get('posA', '')}")
    rows = [dict(label_a=k[0], label_b=k[1], n=n, n_target=tgt[k], examples=' '.join(ex[k]))
            for k, n in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))]
    _write(out, rows, ['label_a', 'label_b', 'n', 'n_target', 'examples'])
    return dict(pairs_read=tot, swaps=sum(cnt.values()), distinct=len(cnt))


PROMPT = """# Look-alike re-read, {run} (value-blind)

You are re-reading {n} sign tiles of a symbol-cipher transcription. Two earlier readers disagreed on some of them, or
gave a label that is often confused with another. You see only the line crops and a sheet of the candidate sign shapes,
labelled by id. You are never told what any sign means; do not guess letters or words.

Line crops (read these images): {crops}
Candidate sheet (ids only): {sheet}

For each tile below, find the sign at that passage and position (the passC sequence of the line is given for
orientation; 'before'/'after' are the neighbouring labels) and pick the candidate id whose shape it is.
Answer one TSV row per tile, header: passage<TAB>pos<TAB>label<TAB>conf<TAB>second<TAB>note
  label  one of the tile's candidates, X_NEW if none fits, or SPLIT:a|b if you cannot choose between two
  conf   H (clear), M (probable), L (guess); second = your runner-up id or empty; note = the shape feature you used.

Tiles (passage, pos, candidates, before | after):
{tiles}

Line sequences (passC, for orientation only):
{seqs}
"""


def packet(agreement, conf_path, passc, top, crops, sheet, sheet_map, out, run, cell=110, cols=9):
    from PIL import Image
    conf = _read(conf_path)
    toplabs = {x for r in conf[:top] for x in (r['label_a'], r['label_b'])}
    partners = collections.defaultdict(list)
    for r in conf:
        partners[r['label_a']].append(r['label_b']); partners[r['label_b']].append(r['label_a'])
    al, pc = _read(agreement), _read(passc)
    merged = [r for r in al if r.get('merged', '') not in ('', 'NONE')]
    tiles, used, j = [], set(), 0
    for i, c in enumerate(pc, 1):
        lab = c['sign_id']
        if j < len(merged) and merged[j]['passage'] == c['passage']:
            r = merged[j]; j += 1
            if r['merged'] != lab:
                sys.exit(f'packet: passC row {i} {c["passage"]}.{c["pos"]}={lab} does not follow the agreement '
                         f'merged column ({r["passage"]} {r["merged"]}); pass the passC built from this agreement')
            A, B, st = r['idA'], r['idB'], r['status']
            split = st != 'agree'
        else:   # a passC row past the end of its passage in the alignment: read by one reader only (e.g. a re-cut tail)
            A, B, st, split, r = lab, '', 'single', True, {}
        if not split and lab not in toplabs:
            continue
        cand = [x for x in dict.fromkeys([A, B, lab] + partners[lab][:2]) if x]
        used.update(cand)
        ctx = ' '.join(p['sign_id'] for p in pc[max(0, i - 4):i - 1] if p['passage'] == c['passage'])
        ctx2 = ' '.join(p['sign_id'] for p in pc[i:i + 3] if p['passage'] == c['passage'])
        tiles.append(dict(run=run, passage=c['passage'], pos=c['pos'], passC=lab, A=A, B=B, status=st,
                          why='single' if st == 'single' else ('split' if split else 'top-pair'),
                          candidates=','.join(cand), before=ctx, after=ctx2,
                          noteA=r.get('noteA', ''), noteB=r.get('noteB', '')))
    if j != len(merged):
        sys.exit(f'packet: agreement merged {len(merged)} signs, passC matched only {j}')
    os.makedirs(out, exist_ok=True)
    fields = ['run', 'passage', 'pos', 'passC', 'A', 'B', 'status', 'why', 'candidates', 'before', 'after', 'noteA', 'noteB']
    _write(os.path.join(out, f'{run}_tiles.tsv'), tiles, fields)
    order = [c['id'] for c in json.load(open(sheet_map))]
    ids = sorted(t for t in used if t in order)
    cand_png = os.path.join(out, f'{run}_candidates.png')
    if ids:
        sh = Image.open(sheet); nc = min(8, len(ids))
        im = Image.new('RGB', (nc * cell, ((len(ids) + nc - 1) // nc) * cell), 'white')
        for n, t in enumerate(ids):
            k = order.index(t); gx, gy = (k % cols) * cell, (k // cols) * cell
            im.paste(sh.crop((gx, gy, gx + cell, gy + cell)), ((n % nc) * cell, (n // nc) * cell))
        im.save(cand_png)
    seqs = collections.OrderedDict()
    for p in pc:
        seqs.setdefault(p['passage'], []).append(p['sign_id'])
    crop_list = sorted(str(p.resolve()) for p in Path(crops).glob('*.jpg') if 'debug' not in p.name) if crops else []
    txt = PROMPT.format(run=run, n=len(tiles), crops=', '.join(crop_list) or '(none given)', sheet=os.path.abspath(cand_png),
                        tiles='\n'.join(f"{t['passage']}\t{t['pos']}\t{t['candidates']}\t{t['before']} | {t['after']}"
                                        for t in tiles),
                        seqs='\n'.join(f'{k}: {" ".join(v)}' for k, v in seqs.items()))
    open(os.path.join(out, f'{run}_prompt.md'), 'w').write(txt)
    return dict(signs=len(pc), tiles=len(tiles), split=sum(t['why'] == 'split' for t in tiles), cands=len(ids))


def reconcile(tiles_p, passc, reread, out, alt_out=None, focus_out=None, run=None):
    pc, tiles = _read(passc), _read(tiles_p)
    rr = {(r['passage'], r['pos']): r for r in _read(reread)}
    tk = {(t['passage'], t['pos']): t for t in tiles}
    missing = [k for k in tk if k not in rr]
    if missing:
        sys.exit(f'reconcile: {len(missing)} flagged tiles have no re-read row, e.g. {missing[0]}')
    run = run or (tiles[0]['run'] if tiles else 'run')
    outr, alt, focus, uns, changed = [], [], [], 0, 0
    for c in pc:
        k = (c['passage'], c['pos']); lab, conf, note, q = c['sign_id'], c.get('conf', ''), 'passC', ''
        alt_lab = None
        if k in tk:
            t, r = tk[k], rr[k]
            rl, rc = r['label'].strip(), r['conf'].strip()
            firm = rc in ('H', 'M') and not rl.startswith('SPLIT')
            if firm and rl in (t['A'], t['B']):
                note = 'lookalike 2-of-3' if t['why'] == 'split' else 'lookalike confirms'
                lab, conf = rl, rc
            else:
                uns += 1; note = 'lookalike UNSETTLED'
                parts = rl.replace('SPLIT:', '').split('|')
                cands = sorted({x for x in (t['A'], t['B'], t['passC'], *parts, r.get('second', '')) if x})
                q = (f"{c['passage']}.{c['pos']}: readers {t['A'] or '-'}/{t['B'] or '-'}, look-alike {rl} ({rc}); "
                     f"which of {', '.join(cands)}?")
                focus.append((f"{run}_{c['passage']}_{c['pos']}", q))
            if firm:
                alt_lab = rl
            if lab != c['sign_id']:
                changed += 1
        outr.append(dict(passage=c['passage'], pos=c['pos'], sign_id=lab, conf=conf, note=note, question=q))
        alt.append(dict(passage=c['passage'], pos=c['pos'], sign_id=alt_lab or lab, conf=conf, note=note))
    _write(out, outr)
    if alt_out:
        _write(alt_out, alt)
    if focus_out:
        with open(focus_out, 'w') as o:
            for sid, q in focus:
                o.write(f'{sid}\t{q}\n')
    return dict(signs=len(pc), flagged=len(tiles), relabelled=changed, unsettled=uns,
                residual=round(uns / max(1, len(pc)), 3))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)
    c = sp.add_parser('confusion', help='label swaps across two-reader alignments')
    c.add_argument('agreement', nargs='+'); c.add_argument('--out', required=True)
    c.add_argument('--target', action='append', default=[], help='leaf folder name counted in n_target (repeatable)')
    p = sp.add_parser('packet', help='flag tiles, cut the candidate sheet, write the value-blind prompt')
    p.add_argument('--agreement', required=True); p.add_argument('--confusion', required=True)
    p.add_argument('--passc', help='default: passC.tsv beside the agreement file')
    p.add_argument('--top', type=int, default=10); p.add_argument('--crops', default='')
    p.add_argument('--sheet', required=True); p.add_argument('--sheet-map', required=True)
    p.add_argument('--out', required=True); p.add_argument('--run')
    p.add_argument('--cell', type=int, default=110); p.add_argument('--cols', type=int, default=9)
    r = sp.add_parser('reconcile', help='fold the re-read in by the fixed 2-of-3 rule')
    r.add_argument('--tiles', required=True); r.add_argument('--passc', required=True)
    r.add_argument('--reread', required=True); r.add_argument('--out', required=True)
    r.add_argument('--alt'); r.add_argument('--focus'); r.add_argument('--run')
    a = ap.parse_args(argv)
    if a.cmd == 'confusion':
        res = confusion(a.agreement, a.out, set(a.target))
    elif a.cmd == 'packet':
        passc = a.passc or os.path.join(os.path.dirname(a.agreement), 'passC.tsv')
        res = packet(a.agreement, a.confusion, passc, a.top, a.crops, a.sheet, a.sheet_map, a.out,
                     a.run or Path(a.agreement).parent.name, a.cell, a.cols)
    else:
        res = reconcile(a.tiles, a.passc, a.reread, a.out, a.alt, a.focus, a.run)
    print(json.dumps(res))
    return res


if __name__ == '__main__':
    main()

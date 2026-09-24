#!/usr/bin/env python3
"""Apply LANE R worker R6's image-read settlements (NOTES.md 'R6 progress', 24 Sept 2026) to
recon_decipher/ciphertext_draft.tsv (blind-pass reconciliation of mssDE 68/37/55) and write
ciphertext_decipher.tsv in the same (line, pos, group, conf, note) schema as ciphertext.tsv.

  python3 apply_r6_settlements.py           write ciphertext_decipher.tsv
  python3 apply_r6_settlements.py --check   exit 1 if the committed file differs from a regeneration (rule 7)

Every settlement below is R6's value read directly off the image crop for that disagreement row
(recon_decipher/disagreements.tsv); several settled values match neither blind pass (the hand's flat-topped
'3' is split between 2, 3 and 9 by the two passes -- see NOTES.md). Rows not in this dict (agreements, and
the 'agree-flagged' rows where both passes matched but stayed uncertain) are carried over unchanged; R6's
brief did not resettle those.
"""
import csv, sys, os, io

HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda f: os.path.join(HERE, f)

# (line, pos) -> (group, conf)  -- conf 'M' only where NOTES.md marks it so; else settled to 'H'.
SETTLEMENTS = {
    ('mssDE68_p1_L01', 3): ('1066', 'H'),
    ('mssDE68_p1_L02', 9): ('391', 'H'),
    ('mssDE68_p1_L02', 12): ('49', 'M'),
    ('mssDE68_p2_L01', 3): ('346', 'H'),
    ('mssDE68_p2_L01', 8): ('391', 'H'),
    ('mssDE68_p2_L02', 5): ('341', 'H'),
    ('mssDE68_p2_L02', 7): ('391', 'H'),
    ('mssDE68_p2_L03', 1): ('80', 'H'),
    ('mssDE68_p2_L05', 9): ('1125', 'H'),
    ('mssDE68_p2_L05', 11): ('30', 'M'),
    ('mssDE68_p2_L06', 5): ('534', 'H'),
    ('mssDE68_p2_L09', 4): ('341', 'H'),
    ('mssDE68_p2_L09', 6): ('391', 'H'),
    ('mssDE68_p2_L09', 10): ('391', 'H'),
    ('mssDE37_p1_L04', 7): ('832', 'H'),
    ('mssDE37_p1_L06', 5): ('931', 'H'),
    ('mssDE37_p1_L06', 8): ('1103', 'M'),
    ('mssDE37_p2_L01', 2): ('341', 'H'),
    ('mssDE37_p2_L03', 4): ('381', 'H'),
    ('mssDE37_p2_L04', 8): ('339', 'H'),
    ('mssDE37_p2_L04', 9): ('832', 'H'),
    ('mssDE37_p2_L07', 9): ('1137', 'M'),
    ('mssDE55_p1_L06', 8): ('12', 'H'),
    ('mssDE55_p1_L08', 8): ('444', 'H'),
    ('mssDE55_p1_L09', 3): ('713', 'M'),
    ('mssDE55_p2_L01', 5): ('40', 'H'),
    ('mssDE55_p2_L01', 9): ('953', 'M'),
    ('mssDE55_p2_L03', 10): ('336', 'M'),
    ('mssDE55_p2_L11', 9): ('1187', 'H'),
}

NOTE = 'R6 settlement (NOTES.md, 24 Sept 2026): read from images/crops/'


def build():
    rows = [['line', 'pos', 'group', 'conf', 'note']]
    seen = set()
    with open(P('recon_decipher/ciphertext_draft.tsv')) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            line, pos = r['line'], int(r['position'])
            key = (line, pos)
            if key in SETTLEMENTS:
                seen.add(key)
                group, conf = SETTLEMENTS[key]
                note = f'{NOTE} (draft: {r["sign"]}/{r.get("alt", "") or "-"})'
            else:
                group, conf, note = r['sign'], r['confidence'], r['why']
            rows.append([line, str(pos), group, conf, note])
    missing = set(SETTLEMENTS) - seen
    return rows, missing


def tsv(rows):
    s = io.StringIO()
    csv.writer(s, delimiter='\t', lineterminator='\n').writerows(rows)
    return s.getvalue()


def main():
    rows, missing = build()
    if missing:
        print('SETTLEMENT NOT FOUND IN DRAFT:', sorted(missing), file=sys.stderr)
        sys.exit(1)
    out = tsv(rows)
    target = P('ciphertext_decipher.tsv')
    if '--check' in sys.argv:
        if not os.path.exists(target) or open(target).read() != out:
            print('stale: ciphertext_decipher.tsv', file=sys.stderr)
            sys.exit(1)
        print('ok: ciphertext_decipher.tsv up to date')
        return
    open(target, 'w').write(out)
    print('wrote', len(rows) - 1, 'rows,', len(SETTLEMENTS), 'settlements applied')


if __name__ == '__main__':
    main()

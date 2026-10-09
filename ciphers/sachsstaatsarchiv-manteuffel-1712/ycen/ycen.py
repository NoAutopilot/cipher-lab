#!/usr/bin/env python3
"""MANT-YCEN (9 Oct 2026): y-glyph 4|9 census and known-answer score, per PREREG-MANT-YCEN.md.
Disk only. Rows are transcribed from the committed per-leaf notes named in column `src`.
Writes ycen/census.tsv, ycen/known.tsv, ycen/score.txt; --check exits 1 if any committed output is stale."""
import csv, os, random, sys
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(D)
key = {r[0]: r for r in csv.reader(open(os.path.join(T, 'key.tsv')), delimiter='\t') if r and r[0].isdigit()}
def val(c):
    r = key.get(c)
    if not r: return '(absent)'
    v = r[1] or '(null)'
    if 'Ilgen' in (r[4] if len(r) > 4 else '') and len(c) <= 2: v += '/Ilgen'
    return v
# leaf, vol, tok, settled, as4, as9, hand, tier, answer, src/note
ROWS = [
 ('0383','08','r02','9','4','9','unrecorded','P','Ilgen','f0383_08 print_spans P02 (BO I pp.257-258)'),
 ('0383','08','r06','9','4','9','unrecorded','P','Ilgen','print_spans P06'),
 ('0383','08','r21','39','34','39','unrecorded','P','Ilgen','print_spans P08; NOTES MANT-UNG r21/r22 39|34 low'),
 ('0383','08','r22','39','34','39','unrecorded','P','Ilgen','print_spans P09'),
 ('0309','08','T020','9','4','9','unrecorded','G','Ilgen','spans_G1/G2 R06 Ilgen/Ilyen, both blind passes'),
 ('0309','08','T035','9','4','9','unrecorded','G','Ilgen','R09 Ilg./Ilg.'),
 ('0309','08','T048','9','4','9','unrecorded','G','Ilgen','R16 Ilg./Ily.'),
 ('0490','08','T003','9','4','9','unrecorded','G','i','G01 la p-a-[i]-x: 17 66 _ 4(x)'),
 ('0490','08','T048','9','4','9','unrecorded','G','i','G05 Blacksche-[i]-ffen: 74 35 _ 77'),
 ('0490','08','T083','9','4','9','unrecorded','G','i','G12a vouloi[s]: 12 33 _ 28 -- o _ t, gloss voulois/voulut i'),
 ('0490','08','T087','9','4','9','unrecorded','G','i','G12a fa-[i]-re: 11 66 _ 60'),
 ('0490','08','T138','39','34','39','unrecorded','G','i','G17 mouvro-[i]-t: 27 33 _ 28'),
 ('0494','08','T019','4','4','9','unrecorded','G','i','L02 mancheroient: 72 35 26 33 _ 21 59 (ch e r o _ n t)'),
 ('0494','08','T021','59','54','59','unrecorded','G','t','L02 mancheroien-[t]: 21 _ 66'),
 ('0494','08','T072','29','24','29','unrecorded','G','s','L06/L07 contre le-[s]: 96 _ 74'),
 ('0063','09','slot01','7','4','9','unrecorded','G','i','eye63 A1 tok2, gloss Si'),
 ('0063','09','slot02','84','84','89','unrecorded','G','th','eye63 B2, gloss Barth (neither value is th)'),
 ('0063','09','slot03','24','24','29','unrecorded','G','s','eye63 C1 tok6, gloss was hast'),
 ('0063','09','slot04','34','34','39','unrecorded','G','i','eye63 C1 tok11, gloss dich'),
 ('0391','08','r4t5','39','34','39','unrecorded','K','i','f0390_08 runs: B-u-l-l-[i]-n-b-r-o-u-g'),
 ('0395','08','r2t5','9','4','9','unrecorded','K','i','f0390_08 runs: f-e-r-d-[i]-n-a-n-d (100 = d)'),
 ('0007','09','b2','39','34','39','unrecorded','W','Ilgen','gloss blind passes Hy, worker Ilg'),
 ('0136','08','T060','254','254','259','unrecorded','W','Ilgen','gloss blind Flyn, worker eye Ilgen; key 259 Ilgen M'),
 ('0136','08','T064','254','254','259','unrecorded','W','Ilgen','gloss blind Haer, worker eye Ilgen'),
 ('0309','08','T010','259','254','259','unrecorded','W','Ilgen','G2 Ilyen one pass, G1 Ryga'),
 ('0398','08','s02','19','14','19','unrecorded','D','n','cuc_candidates: Polo-[n]-ois; shape disputed (two blind reads 19)'),
 ('0410','08','s02','19','14','19','unrecorded','D','n','cuc_candidates: Ha-[n].; shape disputed'),
]
UNSCORED = [  # y-noted tokens with no independent answer
 ('0007','09','b5','39','34','39','unrecorded','-','','no gloss'),('0007','09','b7','39','34','39','unrecorded','-','','si 39 y avoit, no gloss'),
 ('0052','09','tok?','344','344','399','unrecorded','-','','3yy, U either way'),('0089','08','T020','84','84','89','unrecorded','-','','under Keuk gloss; final letter not fixed'),
 ('0136','08','T037','199','194','199','unrecorded','-','','held, no value'),('0176','08','r02t3','9','4','9','unrecorded','-','','m\'a assure que 9 enverroit'),
 ('0290','08','r03','447','447','449','unrecorded','-','','unkeyed'),('0290','08','r12','259','254','259','unrecorded','-','','no gloss at slot'),
 ('0314','08','T039','190','150','190','unrecorded','-','','5 vs 9, not a 4|9 question'),
 ('0383','08','r07','9','4','9','unrecorded','-','','no print span'),('0383','08','r10','9','4','9','unrecorded','-','','no print span'),
 ('0383','08','r11','9','4','9','unrecorded','-','','no print span'),('0383','08','r13','9','4','9','unrecorded','-','','no print span'),
 ('0383','08','r17','9','4','9','unrecorded','-','','no print span'),('0474','08','T072','39','34','39','unrecorded','-','','alt 37'),
 ('0490','08','T052','29','24','29','unrecorded','-','','gloss end -en: neither'),('0490','08','T069','9','4','9','unrecorded','-','','gloss postining, not anchored'),
 ('0494','08','T058','59','54','59','unrecorded','-','','unanchored'),('0494','08','T059','99','44','99','unrecorded','-','','unanchored'),
 ('0494','08','T071','96','46','96','unrecorded','-','','2y note ambiguous'),('0494','08','T236','499','444','499','unrecorded','-','','unkeyed'),
 ('0494','08','T237','419','414','419','unrecorded','-','','unkeyed'),('0390','08','r9t3','9','4','9','unrecorded','-','','FRIB[A]END, word not fixed'),
 ('0395','08','r3t2','9','4','9','unrecorded','-','','not fixed'),('0214','08','r3','9','4','9','unrecorded','-','','not fixed'),
 ('0241','08','r1','99','44','99','unrecorded','-','','two y-glyphs'),('0070','09','r3','19','14','19','unrecorded','-','','ingenium de 7.16.19.120'),
]
POOL_TEXT = ['la paix sans tiers', 'Blackscheiffen', 'voulois faire', 'mouvroit', 'mancheroient', 'contre les', 'Si', 'Barth', 'was hast', 'dich', 'Bullinbroug', 'Ferdinand']
N_ILGEN_POOL = 7  # print/gloss Ilgen slots in the same spans (0383 x4, 0309 x3)
def hit(code, ans):
    v = val(code)
    return ans in v.split('/') or ans in v.split('|')
def main():
    check = '--check' in sys.argv
    out = {}
    hdr = 'leaf\tvol\ttok\tsettled\tas4\tkey4\tas9\tkey9\thand\ttier\tanswer\tR4hit\tR9hit\tsrc\n'
    out['census.tsv'] = hdr + ''.join(f"{l}\t694/{v}\t{t}\t{s}\t{a4}\t{val(a4)}\t{a9}\t{val(a9)}\t{h}\t{ti}\t{an}\t{int(hit(a4,an)) if an else ''}\t{int(hit(a9,an)) if an else ''}\t{src}\n"
                                      for (l,v,t,s,a4,a9,h,ti,an,src) in ROWS + UNSCORED)
    known = [r for r in ROWS]
    out['known.tsv'] = hdr + ''.join(l for l in out['census.tsv'].splitlines(True)[1:] if l.split('\t')[9] in 'PGKWD' and l.split('\t')[9] != '-')
    pool = [c for s in POOL_TEXT for c in s.lower() if c.isalpha()] + ['Ilgen'] * N_ILGEN_POOL
    lines = []
    for name, tiers, vols in [('primary P+G+K pooled','PGK',('08','09')),('primary 694/08','PGK',('08',)),('primary 694/09','PGK',('09',)),
                              ('secondary P+G+K+W pooled','PGKW',('08','09')),('disputed-shape D (code 19)','D',('08','09'))]:
        S = [r for r in known if r[7] in tiers and r[1] in vols]
        if not S: continue
        r9 = sum(hit(r[5], r[8]) for r in S); r4 = sum(hit(r[4], r[8]) for r in S)
        rng = random.Random(1712); null = sorted(sum(hit(r[5], rng.choice(pool)) for r in S) for _ in range(10000))
        rng = random.Random(1712); null4 = sorted(sum(hit(r[4], rng.choice(pool)) for r in S) for _ in range(10000))
        p99, p99_4 = null[9899], null4[9899]; mean = sum(null)/len(null)
        g9 = 'PASS' if (r9 > p99 and r9 > r4 and r9/len(S) >= 0.80) else 'FAIL'
        g4 = 'PASS' if (r4 > p99_4 and r4 > r9 and r4/len(S) >= 0.80) else 'FAIL'
        lines.append(f"{name}: N={len(S)} R9 hits {r9} ({r9/len(S):.3f}) vs null mean {mean:.2f} p99 {p99} -> R9 {g9}; R4 hits {r4} ({r4/len(S):.3f}) vs null p99 {p99_4} -> R4 {g4}")
    lines.append(f"pool: {len(pool)} labels ({len(pool)-N_ILGEN_POOL} letters + {N_ILGEN_POOL} Ilgen); seed 1712; 10000 draws")
    lines.append("per-hand: no hand attribution recorded on disk for any scored leaf (hand column 'unrecorded'); volume used as the only split")
    out['score.txt'] = '\n'.join(lines) + '\n'
    stale = 0
    for f, txt in out.items():
        p = os.path.join(D, f)
        if check:
            if not os.path.exists(p) or open(p).read() != txt: print('STALE', f); stale = 1
        else: open(p, 'w').write(txt)
    print(out['score.txt'], end='')
    sys.exit(stale)
main()

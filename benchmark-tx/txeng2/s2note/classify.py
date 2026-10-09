import sys, collections
sys.path.insert(0, 'tools'); import tx_bench as T
D='benchmark-tx/outputs/vivonne1573-f103r-confirm2/'
truth = T.read_tsv('benchmark-tx/vivonne1573-f103r-confirm2.truth.tsv')   # opening 1
lm = T.load_label_map('benchmark-tx/txeng2/s2note/norm_map.tsv')
out = T.load_output([D+sys.argv[1]])
def classify(rows_all):
    by=collections.defaultdict(list)
    for r in rows_all: by[r['line']].append(r)
    C=collections.Counter(); ex=collections.Counter()
    for ln, rows in by.items():
        if ln not in out: continue
        rows.sort(key=lambda r: float(r['pos']))
        ref=[r['ref_sign'] for r in rows]; ts=[set(filter(None,r['truth'].split('|'))) for r in rows]
        for ri, o in T.align(ref, ts, out[ln]):
            if ri is None: C['segmentation:inserted']+=1; continue
            r=rows[ri]
            if r['status']!='scored': continue
            if o is None: C['segmentation:deleted']+=1
            elif o not in ts[ri]:
                mo=lm.get(o,o); mts={lm.get(t,t) for t in ts[ri]}
                if mo in mts:
                    C['notation']+=1; ex['%s->%s'%(o,mo)]+=1
                elif o==r['ref_sign']: C['read:=committed ref']+=1
                else: C['read:other']+=1; ex['R %s<-%s'%(r['plain'],o)]+=0
    return C, ex
for name, rows in (('as measured', truth), ('flagged excluded', T.drop_flagged(truth))):
    C, ex = classify(rows)
    print(sys.argv[1], name, 'total', sum(C.values()), dict(C), 'notation by label:', dict(ex))

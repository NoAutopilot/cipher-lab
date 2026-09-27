from pathlib import Path
import json,sys

D=Path(__file__).resolve().parent
controls=json.loads((D/'controls.json').read_text())
result=[]
for c in controls:
    for mode in ['hard','soft']:
        path=D/f'results/control{c["seed"]}-{mode}.tsv'
        if not path.exists():continue
        row=path.read_text().splitlines()[0].split('\t');key=row[1];pred=row[2].replace('|','')
        changes={int(x.split(':')[0]):int(x.split(':')[1]) for x in row[3].split(',') if x}
        seq=c['observed_sequence'].copy()
        for ix,v in changes.items():seq[ix]=v
        check=''.join(key[v] for v in seq if v>=0);assert pred==check
        correct=sum(a==b for a,b in zip(pred,c['plaintext']));assert len(pred)==c['N']
        restored=sum(seq[ix]==c['truth_sequence'][ix] for ix in c['wrong_positions'])
        false_changes=sum(ix not in c['wrong_positions'] for ix in changes)
        r=dict(seed=c['seed'],mode=mode,score=float(row[0]),correct=correct,N=c['N'],
               recovery=correct/c['N'],planted_label_errors_restored=restored,
               false_changes=false_changes,changes=changes,reading=pred)
        result.append(r)
        print(c['seed'],mode,f'{correct}/{c["N"]}',f'{correct/c["N"]:.2%}',
              f'planted errors restored={restored}/5',f'false changes={false_changes}')
soft=[r for r in result if r['mode']=='soft']
gate=len(soft)==2 and all(r['recovery']>=.95 and r['planted_label_errors_restored']>=4 for r in soft)
(D/'control_results.json').write_text(json.dumps(dict(rows=result,target_gate_passed=gate),indent=2)+'\n')
print('TARGET_GATE',gate)

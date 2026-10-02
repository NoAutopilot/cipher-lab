set -x
for s in 7 11; do
python3 ../../ceppo-nevers-fr3251-1570s/harvest/decode_control.py no90/verify/portion742.tsv --map sign_id_map_1572_fit.json --err 0.12 --seed $s > no90/verify/ctl_portion742_s$s.txt 2>&1 &
python3 ../../ceppo-nevers-fr3251-1570s/harvest/decode_control.py no90/passC_all.tsv --map sign_id_map_1572_fit.json --err 0.12 --seed $s > no90/verify/ctl_whole966_s$s.txt 2>&1 &
wait
python3 ../../ceppo-nevers-fr3251-1570s/harvest/decode_control.py no90/verify/f185v.tsv --map sign_id_map_1572_fit.json --err 0.29 --seed $s > no90/verify/ctl_f185v_s$s.txt 2>&1 &
python3 ../../ceppo-nevers-fr3251-1570s/harvest/decode_control.py no90/verify/f185r_185b.tsv --map sign_id_map_1572_fit.json --err 0.12 --seed $s > no90/verify/ctl_f185r185b_s$s.txt 2>&1 &
python3 ../../ceppo-nevers-fr3251-1570s/harvest/decode_control.py no90/verify/portion742.tsv --map sign_id_map_1572_fit.json --err 0.26 --seed $s > no90/verify/ctl_portion742_err26_s$s.txt 2>&1 &
wait
done
python3 ../../ceppo-nevers-fr3251-1570s/harvest/decode_control.py no90/verify/f185v.tsv --map sign_id_map_1572_fit.json --err 0.12 --seed 7 > no90/verify/ctl_f185v_err12_s7.txt 2>&1
echo ALLDONE

#!/bin/sh
# H393 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026): --check on every runner-14 script; one line per script into h393_check_sweep_result.txt.
# Heavy ones (order gains) run four at a time. Run: sh h393_check_sweep.sh
cd "$(dirname "$0")"; T=$(mktemp -d)
run() { n=$1; shift; out=$("$@" --check 2>&1 | tail -1); printf '%s\t%s\n' "$n" "$out" > "$T/$(echo "$n" | tr ' ' '_')"; }
for s in "h367_bowl_f61.py score" "h368_bowl_106r.py score" "h370_bowl_97r.py score" "h372_bowl_code_table.py" "h373_97r_c2_reread.py" "h381_shape_letter_pool.py" "h384_shape_at_f61.py" "h386_4stem_by_shape.py" "h390_bowl_kappa_gated.py score" "h391_bowl_reader_agreement.py"; do
  run "$s" python3 $s
done
run "h371 score" python3 h371_97r_4tri_split.py score & run "h374 f97r" python3 h374_split_randctl.py f97r & run "h374 f124r" python3 h374_split_randctl.py f124r & run "h374 f101r" python3 h374_split_randctl.py f101r & wait
run "h377 score" python3 h377_97r_4tri_more.py score & run "h379" python3 h379_108v_shape_relabel.py & run "h380" python3 h380_106r_shape_relabel.py & run "h383" python3 h383_shape_shuftarget.py & wait
run "h385 score" python3 h385_106r_c43_bowl.py score & run "h387 score" python3 h387_101r_4stem_bowl.py score & wait
cat "$T"/* | sort > h393_check_sweep_result.txt; rm -rf "$T"; cat h393_check_sweep_result.txt

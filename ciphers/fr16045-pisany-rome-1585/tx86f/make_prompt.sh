#!/bin/sh
# make_prompt.sh READER LINE -> the exact prompt given to one blind reader call (PIS1-275V, PREREG kp86f)
R=$1; L=$2; n=$(echo $L | sed 's/^L0*//')
if [ $n -le 5 ]; then C=$(printf 'f275vA_L%02d' $n); else C=$(printf 'f275vB_L%02d' $((n-5))); fi
NOTE="The whole line is cipher."
[ $n -eq 5 ] && NOTE="The line ends in ordinary handwriting (\"ou ie suis\") after the last cipher sign: do not read it."
[ $n -eq 6 ] && NOTE="The line starts with one ordinary handwritten word (\"touchant\"): do not read it; start at the first cipher sign after it."
D=/home/user/cipher-lab/ciphers/fr16045-pisany-rome-1585
cat <<P
You are blind reader $R. Read $D/tx86f/PASS_BRIEF86f.md and follow it exactly; it is your whole task.
Your line is $L. Its crops: $D/images/${C}_s1.jpg and $D/images/${C}_s2.jpg (in the brief these are called images/f275vL_Lnn_s1/_s2).
Reference sheet: $D/tx86f/SIGNSHEET86.png. $NOTE
Open only these three images and the brief; read no other file and run no command. Reply with exactly one line: $L<TAB>labels.
P

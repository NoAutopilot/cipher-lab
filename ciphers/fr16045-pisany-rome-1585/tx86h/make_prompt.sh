#!/bin/sh
# make_prompt.sh READER LINE -> the exact prompt given to one blind reader call (RUN6-PIS, PREREG kp86h). LINE = L17..L20
# = f.275v block B lines 12-15 = crops images/f275vB2_L01..L04. Brief and sign sheet are tx86f's (copied unchanged to tx86h/).
R=$1; L=$2; n=$(echo $L | sed 's/^L0*//')
C=$(printf 'f275vB2_L%02d' $((n-16)))
NOTE="The whole line is cipher."
D=/home/user/cipher-lab/ciphers/fr16045-pisany-rome-1585
cat <<P
You are blind reader $R. Read $D/tx86h/PASS_BRIEF86f.md and follow it exactly; it is your whole task.
Your line is $L. Its crops: $D/images/${C}_s1.jpg and $D/images/${C}_s2.jpg (in the brief these are called images/f275vL_Lnn_s1/_s2).
Reference sheet: $D/tx86h/SIGNSHEET86.png. $NOTE
Open only these three images and the brief; read no other file and run no command. Reply with exactly one line: $L<TAB>labels.
P

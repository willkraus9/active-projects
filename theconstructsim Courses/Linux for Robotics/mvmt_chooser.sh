#!/bin/bash
ARG1 = $1
if [ $ARG1 == 'circle']; then
        rosrun move_bb8_pkg move_bb8_square.py
elif [ $ARG1 == 'forward_backward']; then
        rosrun move_bb8_pkg move_bb8_forward_backward.py
elif [ $ARG1 == 'square']; then
        rosrun move_bb8_pkg move_bb8_square.py
fi
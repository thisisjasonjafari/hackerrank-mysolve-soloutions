#!/bin/bash
read X
read Y
printf "%s\n" $X{+,-,*,/}"($Y)" | bc
#!/bin/bash
set -ex

freq=$1

for n in {1..8}
do
    ssh node$n apt update
    ssh node$n apt install -y indicator-cpufreq
    ssh node$n apt install -y cpufrequtils

    for i in {0..7}
    do 
        ssh node$n cpufreq-set -c $i -g performance -f $freq
    done
done
    
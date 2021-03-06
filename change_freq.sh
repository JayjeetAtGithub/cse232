#!/bin/bash
set -ex

freq=$1

for n in {1..8}
do
    ssh node$n apt update
    ssh node$n apt install -y indicator-cpufreq
    ssh node$n apt install -y cpufrequtils

    for i in {0..15}
    do 
        ssh node$n sudo cpufreq-set -c $i -f $freq
    done
done
    
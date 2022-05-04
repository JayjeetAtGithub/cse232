#!/bin/bash
set -ex

freq=$1

for i in {0..15}
do 
    sudo cpufreq-set -c $i -f $freq
done

#!/bin/bash
set -ex

freq=$1

apt update
apt install -y indicator-cpufreq
apt install -y cpufrequtils

for i in {0..15}
do 
    sudo cpufreq-set -c $i -f $freq
done

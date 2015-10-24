#!/bin/bash
file=$(ls|grep crnum_all.crn)
let atom=$(sed -n "4p" $file)
let lines=$(nl $file|wc -l|cut -c 2-)
let stpdif=$(sed -n "$[$atom+9+2]"p $file)

./msdBA.py $atom $lines $stpdif 500

#!/bin/sh

file="../crnum_1.crn"
file1="../crnum_-1.crn"

let atom=$(sed -n "4p" $file)
let adder=$(tail -$[$atom+9] $file1 | sed -n 2p)
let lines=$(nl $file|wc -l)
let frame=$lines/$[$atom+9]
let stpdif=$(sed -n "$[$atom+9+2]"p $file) 
let ttlstp=$[$frame-1]*$stpdif

touch crnum_positive.crn
for i in $( seq 2 $frame )
do
	let init=$[$i-1]*$[$atom+9]+1
	let finl=$i*$[$atom+9]
	let odstp=$(sed -n "$[$init+1]"p $file)
	let nwstp=$odstp+$adder
	sed -n "$init,$finl"p $file | sed "2s/^.*/$nwstp/" >> crnum_positive.crn
done

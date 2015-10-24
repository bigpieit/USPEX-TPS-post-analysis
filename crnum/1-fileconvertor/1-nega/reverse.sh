#!/bin/sh

file="../crnum_-1.crn" 

let atom=$(sed -n "4p" $file)
let lines=$(nl $file|wc -l)
let frame=$lines/$[$atom+9]
let stpdif=$(sed -n "$[$atom+9+2]"p $file)
let ttlstp=$[$frame-1]*$stpdif

touch crnum_negative.crn
for j in $( seq 1 $frame )
do
	let i=$frame-$j+1
	let init=$[$i-1]*$[$atom+9]+1
	let finl=$i*$[$atom+9]
	let odstp=$(sed -n "$[$init+1]"p $file)
	let nwstp=$ttlstp-$odstp
	sed -n "$init,$finl"p $file | sed "2s/^.*/$nwstp/" >> crnum_negative.crn
done

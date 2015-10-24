set N 1404

for { set i 0 } { $i< $N } { incr i } {
	mol new $i.xyz
	display projection orthographic
	mol delrep 0 top
	mol representation VDW 0.5 12.0
	mol color Element
	color Element H white
	color Element He purple
	color Element Li red
	color Element Be blue
	color Element B green
	color Element C yellow
	mol selection {all}
	mol material Opaque
	mol addrep top
	rotate z by 90
	rotate y by 90
	catch [ render snapshot $i.ppm ]
	mol delete $i
}

set x [ pwd ]
set M [ expr $N - 1 ]
set y "PATTERN IBBPBBPBBPBBPBB\nOUTPUT $x/movie-y.mpeg\nINPUT_DIR $x\nINPUT\n*.ppm \[0-$M\]\nEND_INPUT\nBASE_FILE_FORMAT PPM\nINPUT_CONVERT *\nGOP_SIZE 15\nSLICES_PER_FRAME 1\nPIXEL HALF\nRANGE 32\nPSEARCH_ALG LOGARITHMIC\nBSEARCH_ALG CROSS2\nIQSCALE 8\nPQSCALE 10\nBQSCALE 25\nREFERENCE_FRAME DECODED\nFORCE_ENCODE_LAST_FRAME\n\n"

set parmfilename "parm"

set fileID [ open $parmfilename "w" ]

puts -nonewline $fileID $y

close $fileID

ppmtompeg -realquiet parm

for { set i 0 } { $i< $N } { incr i } {
	rm $i.ppm
}

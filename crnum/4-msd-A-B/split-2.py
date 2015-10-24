#!/usr/bin/python
import os, sys
import numpy as np
import pylab as plt

# comes in handy
if len(sys.argv) != 5:
        sys.exit("Usage : ./this_script refFp myRdf ")


####### Read Data #######
files=sys.argv[1]
atoms=int(sys.argv[2])
lines=int(sys.argv[3])
stpdif=int(sys.argv[4])

steps=lines/(atoms+9)

########### Write ##########
crnfile=open(files,'r')

for step in range(steps):
        for i in range(5): crnfile.readline()
        x=crnfile.readline()
        y=crnfile.readline()
        z=crnfile.readline()
        crnfile.readline()
        trjfile=open(str(step),'w')
        content1=str(8000)+'\n'
        content2='Atoms. '+'Timestep: '+str(step*stpdif)+'\n'
        trjfile.write(content1)
        trjfile.write(content2)
        trjfile.write(x)
        trjfile.write(y)
        trjfile.write(z)

        for coor in range(atoms):
                line=crnfile.readline().split()
                content3=line[5]+' '+line[1]+' '+line[2]+' '+line[3]+'\n'
                trjfile.write(content3)

        trjfile.close()

crnfile.close()

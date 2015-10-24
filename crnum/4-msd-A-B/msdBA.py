#!/usr/bin/python
import os, sys
import numpy as np
import pylab as plt

############### User-defined Function ###############
def MSD(init,next,initcell,nextcell):
	atoms=float(len(init.keys()))
	sum=0
	for keys in init.keys():
		for i in range(len(next[keys])):
			diff=abs(init[keys][i]-next[keys][i])
			crtval=nextcell[i][1]-nextcell[i][0]
			if diff>crtval/2:
				diff=crtval-diff
			sum+=diff**2
	sum=sum/atoms
	return sum


###############       Main Code       ###############
#######      Read Data      #######
atoms=8000
lines=11252645
stpdif=100
every=500


#######   Basic Parameter   #######
maximages=lines/(atoms+9)-1
imagestep=every/stpdif

print atoms,lines,stpdif,every,maximages,imagestep

####### Self-defined Variable #######
x=[]
msd=[]

#### init coor ####
i=0
init={}
files=open('0','r')
for i in range(2):
	files.readline()
initcell=[]
for i in range(3):
	content=files.readline().split()
	initcell.append([float(content[0]),float(content[1])])
for i in range(atoms):
	content=files.readline().split()
	index=content[0]
	coor=[float(content[i]) for i in range(1,4)]
	init[index]=coor
files.close()

####### Self-defined Variable #######
msdvalue=[]
for i in range(0,1405,imagestep):
	next={}
	filename=str(i)
	files=open(filename,'r')
	for j in range(2):
		files.readline()
	nextcell=[]
	for l in range(3):
		content=files.readline().split()
		nextcell.append([float(content[0]),float(content[1])])
	for k in range(atoms):
		content=files.readline().split()
		index=content[0]
		coor=[float(content[t]) for t in range(1,4)]
		next[index]=coor
	files.close()

	abnormal={}
	for keys in init.keys():
		sum=0
		for k in range(len(next[keys])):
			diff=abs(init[keys][k]-next[keys][k])
			crtval=nextcell[k][1]-nextcell[k][0]
			if diff>crtval/2:
				diff=crtval-diff
			sum+=diff**2
		if sum >100:
			abnormal[keys]=sum
			#print i,keys,sum
	#print i,len(abnormal),abnormal

	msdvalue.append(MSD(init,next,initcell,nextcell))

x=range(0,1405,imagestep)
plt.plot(x,msdvalue,'-r',label=r"$fcc \rightarrow hcp\ transition$",linewidth=1)


####### Self-defined Variable #######
x=[]
msd=[]

#### init coor ####
i=0
init={}
files=open('1404','r')
for i in range(2):
	files.readline()
initcell=[]
for i in range(3):
	content=files.readline().split()
	initcell.append([float(content[0]),float(content[1])])
for i in range(atoms):
	content=files.readline().split()
	index=content[0]
	coor=[float(content[i]) for i in range(1,4)]
	init[index]=coor
files.close()

####### Self-defined Variable #######
msdvalue=[]
for i in range(1404,-1,-imagestep):
	next={}
	filename=str(i)
	files=open(filename,'r')
	for j in range(2):
		files.readline()
	nextcell=[]
	for l in range(3):
		content=files.readline().split()
		nextcell.append([float(content[0]),float(content[1])])
	for k in range(atoms):
		content=files.readline().split()
		index=content[0]
		coor=[float(content[t]) for t in range(1,4)]
		next[index]=coor
	files.close()

	abnormal={}
	for keys in init.keys():
		sum=0
		for k in range(len(next[keys])):
			diff=abs(init[keys][k]-next[keys][k])
			crtval=nextcell[k][1]-nextcell[k][0]
			if diff>crtval/2:
				diff=crtval-diff
			sum+=diff**2
		if sum >5:
			abnormal[keys]=sum
			#print i,keys,sum
	#print i,len(abnormal),abnormal
	#print i,len(abnormal),abnormal
	msdvalue.append(MSD(init,next,initcell,nextcell))


y=range(1404,-1,-imagestep)
plt.plot(y,msdvalue,'-b',label=r"$hcp \rightarrow fcc\ transition$",linewidth=1)

plt.legend(loc="upper right",frameon=False)
plt.title("Mean Square Displacement of Ar Phase Transition")
plt.ylabel(r"$MSD A^2$",fontsize=12)
plt.grid(True)

plt.savefig("double-end.png")

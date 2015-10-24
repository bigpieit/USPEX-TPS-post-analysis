#!/usr/bin/python
import os, sys
import numpy as np
import pylab as plt

# comes in handy
if len(sys.argv) != 5:
        sys.exit("Usage : ./this_script refFp myRdf ")

def mergeA2B(A,B,atstep):
	for key in A.keys():
		if key in B.keys():
			B[key]+=A[key]
		else:
			B[key]=[]
			for i in range(atstep): B[key].append(0)
			B[key]+=A[key]

	for key in B.keys():
		if key not in A.keys():
			B[key]+=[0]
	return B

def printline(dic):
	for key in dic:
		print key
		print dic[key]

def smallest(l):
	mini=int(l[0])
	for i in l:
		if int(i)<mini:
			mini=int(i)
	return mini


###################### Main code Here ######################
files=sys.argv[1]
atoms=int(sys.argv[2])
lines=int(sys.argv[3])
stpdif=int(sys.argv[4])
steps=lines/(atoms+9)

######## Statistics ########
crnfile=open(files,'r')
crndic={}

for step in range(steps):
	for i in range(9): crnfile.readline()
	locdic={}
	
	for coor in range(atoms):
		line=crnfile.readline().split()
		crns=line[4]
		if crns not in locdic.keys():
			locdic[crns]=[1]
		else:
			locdic[crns][0]+=1

	crndic=mergeA2B(locdic,crndic,step)

crnfile.close()

########### Plot ###########
keylist=crndic.keys()
x=[i*stpdif-steps/2*stpdif for i in range(steps)]
atoms=float(atoms)
numplot=len(keylist)

minimum=smallest(keylist)
k=[0 for i in range(numplot)]
for element in keylist:
	k[int(element)-minimum]=element

keylist=k

color=['k','m','r','b','g','y']
plt.figure(figsize=(18,6), dpi=100)
plt.rc('xtick', labelsize = 15)
plt.rc('ytick', labelsize = 15)
for key in keylist:
	pos=keylist.index(key)
	y=[i/atoms*100 for i in crndic[key]]
	plt.plot(x,y,color[pos],label=r'CN='+key,linewidth=1.5)
#plt.xlabel('0.1 fs for every step',fontsize=28)
plt.ylabel('Percentage %',fontsize=28)
plt.xlim(-80000,80000)
plt.xticks(np.linspace(-80000,80000,9, endpoint=True))
plt.legend(prop={'size':20},loc="upper right",frameon=False)
plt.savefig("crn.png")

########### Output ##########
count=0
minimum=atoms
fw=open('crn.txt','w')
for i in crndic['12']:
	if i < minimum:
		minimum = i
pos=crndic['12'].index(minimum)
for key in keylist:
	avg=0
	for i in range(pos-10,pos,1):
		avg+=crndic[key][i]
	for i in range(pos,pos+10,1):
		avg+=crndic[key][i]
	avg=avg/20/atoms*100
	content1='CN = '+key+'\n'
	content2='Percentage is '+str(round(avg,3))+' %'+'\n'
	fw.write(content1)
	fw.write(content2)
fw.close()

########### Write ##########
crnfile=open(files,'r')
atoms=int(atoms)
elmntlst=['H','He','Li','Be','B','C','N','O','F','Ne']

smallest=int(keylist[0])
for key in keylist:
        if smallest>int(key):
                smallest=int(key)

for step in range(steps):
        for i in range(9): crnfile.readline()
        filename=str(step)+'.xyz'
	trjfile=open(filename,'w')
        content1=str(8000)+'\n'
        content2='Atoms. '+'Timestep: '+str(step*stpdif)+'\n'
        trjfile.write(content1)
        trjfile.write(content2)

        for coor in range(atoms):
                line=crnfile.readline().split()
                elmntnum=int(line[4])-smallest
                elmnt=elmntlst[elmntnum]
                content3=elmnt+' '+line[1]+' '+line[2]+' '+line[3]+'\n'
                trjfile.write(content3)

        trjfile.close()

crnfile.close()

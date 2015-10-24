#!/usr/bin/python
import numpy as np
import pylab as plt
file=open('msd_-1.msd','r')
step=[0]
msd=[0]
for j in range(5):
		file.readline()

for i in range((355-5)/5):
	content=file.readline().split()
	nstp=int(content[0])*(-1)
	step=[nstp]+step
	for j in range(3):
		file.readline()
	content=file.readline().split()[1]
	msdisp=float(content)
	msd=[msdisp]+msd
file.close()



file=open('msd_1.msd','r')
for j in range(5):
		file.readline()

for i in range((355-5)/5):
	content=file.readline().split()
	nstp=int(content[0])
	step.append(nstp)
	for j in range(3):
		file.readline()
	content=file.readline().split()[1]
	msdisp=float(content)
	msd.append(msdisp)
file.close()

plt.plot(step,msd,'-r',label=" msd A^2 ",linewidth=1)

plt.xlabel('0.1fs for every step',fontsize=14)
plt.ylabel('MSD A',fontsize=14)
plt.title("MSD")
plt.grid(True)
plt.legend(numpoints=3,loc="lower right",frameon=False)
plt.savefig("msd-mid.png")

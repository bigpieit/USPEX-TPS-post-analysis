import scipy.io as sio
import pylab as plt
import numpy as np
import math

TPS_STRUC=sio.loadmat('TPS_STRUC.mat')
tps_struc=TPS_STRUC['TPS_STRUC']
ht=tps_struc['op'][0][0]

x=[]
A=[]
B=[]

for i in ht:
	x.append(i[0])
	A.append(i[1])
	B.append(i[2])

stp=x[1]-x[0]
count=x[0]
for i in A:
	if i >0.999:
		break
	count+=stp
finl=count

count=x[0]
for i in B:
	if i <0.999:
		break
	count+=stp
init=count
time=(finl-init)*0.1/1000

plt.figure(figsize=(18, 6), dpi=100)

plt.rc('xtick', labelsize = 15)
plt.rc('ytick', labelsize = 15)

plt.plot(x,A,'r',label=r"$hcp$",linewidth=1.5)
plt.plot(x,B,'b',label=r"$fcc$",linewidth=1.5)

plt.xlabel('0.1 fs for every step',fontsize=28)
plt.ylabel('Structure Similarity',fontsize=28)
p = plt.axvspan(init,finl,facecolor='g',alpha=0.5)
plt.text(55000,0.91,r'$time \ =\ $'+str(time)+r'$\ ps$',color='k',fontsize=18)
#plt.grid(True)
plt.legend(numpoints=15,prop={'size':28},loc="lower right",frameon=False)
plt.savefig("Structure-similarity.png")

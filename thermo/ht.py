import scipy.io as sio
import pylab as plt
import numpy as np
import math

TPS_STRUC=sio.loadmat('TPS_STRUC.mat')
tps_struc=TPS_STRUC['TPS_STRUC']
ht=tps_struc['HT'][0][0]

x=[]
H=[]
T=[]

for i in ht:
	x.append(i[0])
	H.append(i[1]*0.043/8000)
	T.append(i[2])
avg=0
for i in range(20000):
	avg+=H[i]

print avg/20000

peak=-float('inf')
for i in H:
	if i > peak:
		peak=i

print peak 

avg=0
for i in range(130000,len(H),1):
	avg+=H[i]

print avg/(len(H)-130000)

H=[i*1000.0 for i in H]


plt.rc('xtick', labelsize = 15)
plt.rc('ytick', labelsize = 15)

plt.figure(figsize=(18, 6), dpi=100)
plt.plot(x,H,'-r',label="",linewidth=1)

plt.ylabel('Enthalpy meV/atom',fontsize=28)
#plt.title("Enthalpy")
plt.text(-60000,-69.0,r'$fcc$',color='k',fontsize=28)
plt.text(60000,-69.0,r'$hcp$',color='k',fontsize=28)
plt.ylim(-70.5,-66.5)
plt.yticks(np.linspace(-70.5,-66.5,5,endpoint=True))
plt.grid(True)
plt.legend(numpoints=3,loc="upper right",frameon=False)
plt.savefig("Enthalpy.png")

plt.figure(figsize=(18, 3), dpi=100)
plt.plot(x,T,'-r',label="",linewidth=1)

plt.xlabel('0.1 fs for every step',fontsize=28)
plt.ylabel('Temperature / K',fontsize=28)
#plt.title("Temperature")
plt.text(-60000,41.0,r'$fcc$',color='k',fontsize=28)
plt.text(60000,41.0,r'$hcp$',color='k',fontsize=28)
plt.grid(True)
plt.legend(numpoints=3,loc="upper right",frameon=False)
plt.savefig("Temperature.png")


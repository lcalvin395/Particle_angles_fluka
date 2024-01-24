import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import math
import matplotlib.ticker
from matplotlib.ticker import (MultipleLocator, 
                               FormatStrFormatter, 
                               AutoMinorLocator) 
path="/Users/lukecalvin/2023/eli_np_muon_primaries_1.0GeV/"
file1 = open("%smuon+_time.txt"%(path), "r")
file2 = open("%spositime.txt"%(path), "r")
x=0
y=0
energy=[]
div=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
particles=[]
angle=[]
h=0
divergence=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
energyofmu=[]
energymuon=[]
divmuon=[]
energymuonnew=[]
divmuonnew=[]
for e in range(1,9,1):
    energyofmu.append(e/10)
particles = [0]*len(energyofmu)
for z in range(len(energyofmu)):
    particles[z]=[0]*len(divergence)
print(particles)
print(energyofmu)

#print("energy:", energy)
while h<=len(divergence)-1:    
    div[h]=divergence[h]/(180/math.pi)
    h=h+1
for line in file2.readlines():
    if len(line)>1:
        #print(len(line))
        columns=line.split()
        #print(columns)
        if columns[2]=='11' or x!=0:
            x=x+1
            if x==1:
                energy=(float(columns[3])/1000)
                energymuon.append(energy)
            if x==3:
                degree=(180/math.pi)*math.acos(float(columns[2]))
                print(degree)
                divmuon.append(math.acos(float(columns[2])))
                x=0
for line in file1.readlines():
    if len(line)>1:
        #print(len(line))
        columns=line.split()
        #print(columns)
        if columns[2]=='10' or x!=0:
            x=x+1
            if x==1:
                energy=(float(columns[3])/1000)
                energymuonnew.append(energy)
            if x==3:
                degree=(180/math.pi)*math.acos(float(columns[2]))
                print(degree)
                divmuonnew.append(math.acos(float(columns[2])))
                x=0


print(particles)
print(energyofmu)
print(float((math.acos(0.9999)))*(180/math.pi))
maxpeak=0
ymax=0
b=0
n=0
total=0

#peak=[0]*len(divergence)
    
#while n<len(particles)-1:
#    ymax=0
#    b=0
#    while b<len(particles[n]):
#        if ymax<particles[n][b]:
#            ymax=particles[n][b]
#            peak[n]=energyofmu[b]
#            if maxpeak<peak[n]:
 #               maxpeak=peak[n]
#        b=b+1
#    n=n+1
#print("peak: ",peak)
#x = (line.split()[0])
#print(xs)
#print(line)

#ax.set_xlim(10)
#plt.xscale("log")
#ax = fig.add_subplot(111)
#ax.xaxis.set_major_locator(MultipleLocator(10))
#ax.xaxis.set_major_formatter(FormatStrFormatter('% 1.2f'))


#ax.set_xlim([0,xlim])


#titlein = input("Set graph title? - \n0:no\n1:yes \n :")
#if titlein == "1":

#else:
#    plt.title(search_phrase)
#ax.text(x=1, y=ymax*1.1, s='total particles: %d'%(int(total*float(prim))), color='#334f8d')
print("this is working")
#plt.plot(x, y, label="total particles: %d"%(int(total)))

#ax.xaxis.set_ticks(a)
#locmaj = matplotlib.ticker.LogLocator(base=10,numticks=5)
#ax.xaxis.set_major_locator(locmaj)
#locmin = matplotlib.ticker.LogLocator(base=10,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),numticks=9)
#ax.xaxis.set_minor_locator(locmin)

#ax.text(x=6, y=20, s="total particles: %fcm" %(total), color='#334f8d')

#print("total: ", total)
print(ymax)
print(total)
print("div: ", div)
print("particles: ",particles)

total = 0

fig, ax=plt.subplots()
ax = plt.gca()
xlim = 16
ylim = maxpeak*1.5
#ax.set_ylim([0,ylim])
font = {'family' : 'Arial',
        'weight' : 'normal',
        'size'   : 17}


matplotlib.rc('font', **font)
matplotlib.rc('xtick', labelsize=13) 
matplotlib.rc('ytick', labelsize=13) 

plt.ylabel("Divergence - (rad)")
plt.xlabel('Energy - (GeV)')
#title = ("Muon energy vs divergence - 2GeV")
#plt.title(title)
#ax.plot(energymuon, divmuon, 'o', color='blue', markersize=1, label='Muon-')
ax.plot(energymuonnew,divmuonnew, 'o', color='red', markersize=1, label='Muon+')
leg = ax.legend();
#ax.xaxis.set_major_locator(plt.MultipleLocator(0.05))
#ax.xaxis.set_minor_locator(plt.MultipleLocator(0.01))
ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
plt.savefig('%sdivergencevsenergy_muonboth.png'%(path),bbox_inches='tight', dpi=1000)
plt.show()
print(divmuon)
print(energymuon)
print(np.mean(divmuonnew))
print(len(divmuonnew))
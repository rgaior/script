import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import glob
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
sys.path.append(classpath)
import utils
import constant
import event

basename = sys.argv[1]

folder = '/Users/romain/work/Auger/EASIER/IPNcode/myversion/out/txt/'
names = glob.glob(folder+ basename+ '*.dat')

distances = [0,50,250,500,1000]
colors = ['#009900', '#e6b3cc', '#4d4dff', '#0099cc','#ff66d9']

print names
for n in names:
    ev = event.Event(fname=n, type='test')
    ev.loadevent()
    figtrace = plt.figure()
#    figtrace.suptitle('file: '+n,fontweight='bold',fontsize=15)
    axtrace = plt.subplot(111)
    for ant, d,c in zip(ev.antennas,distances,colors): 
        if np.isnan(np.max(ant.power)):
            print 'nan !!!!!!!'
            continue
        print 'max = ', np.max(ant.power)

        time = ant.maketimearray()
        print 'len height = ', len(ev.shower.height)
        print 'len power = ' , len(ant.power)
        print 'len(electro ) = ' , len(ev.shower.electron)
        print 'len(posz = ) = ' , len(ev.shower.posz)
#        axtrace.plot(ev.shower.posz,ev.shower.electron[:-1],label=str(ant.id))
#        axtrace.plot(ev.shower.electron[:-1],ant.aeff,label=str(ant.id))
#        axtrace.plot(ev.shower.height,ant.power,label=str(ant.id))
        axtrace.semilogy(time*1e9,ant.power*1e5,lw=2,c=c, label=str(d)+' m')
#        axtrace.semilogy(time*1e9,ant.power,c=c, label=str(d))
#        axtrace.plot(time*1e9,ant.power,label=str(ant.id))

plt.xlabel('time [ns]')
plt.ylabel('spectral intensity [W/GHz/cm^2]')
plt.ylim(1e-20,1e-15)
plt.xlim(0,4500)
plt.legend()
plt.show()

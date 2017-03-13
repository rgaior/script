import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import glob
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
#srcd = '/Users/romain/work/Auger/EASIER/IPNcode/script/'
#classpath = srcd + '/classes/'
#utilspath = srcd + '/utils/'
sys.path.append(utilspath)
sys.path.append(classpath)
import utils
import constant
import event

basename = sys.argv[1]

folder = '/Users/romain/work/Auger/EASIER/IPNcode/myversion/out/txt/'
names = glob.glob(folder+ basename+ '*.dat')
leg = ['0 m', '50 m', '250 m', '500 m', '1000 m']
col = ['g','y','b','c','m']
#print names
for n in names:
    ev = event.Event(fname=n, type='test')
    ev.loadevent()
    figtrace = plt.figure(figsize=(10,8))
    figtrace.suptitle('file: '+n,fontweight='bold',fontsize=15)
    axtrace = plt.subplot(111)
    for ant,l,c in zip(ev.antennas,leg,col): 
        if np.isnan(np.max(ant.power)):
            print 'nan !!!!!!!'
            continue
 
        time = ant.maketimearray()
#        axtrace.plot(ev.shower.posz,ev.shower.electron[:-1],label=str(ant.id))
#        axtrace.plot(ev.shower.electron[:-1],ant.aeff,label=str(ant.id))
#        axtrace.plot(ev.shower.height,ant.power,label=str(ant.id))
#        axtrace.semilogy(time*1e9,ant.power,label=str(ant.id))
        axtrace.semilogy(time*1e6,ant.power*1e5,lw=2,color=c,label=l)
#        axtrace.plot(time*1e9,ant.power,label=str(ant.id))
        
#        axtrace.plot(time*1e9,ant.power,label=str(ant.id))
plt.xlim(-0.1,5)
#plt.xlim(-100,5000)
plt.ylim(1e-20,1e-15)
plt.xlabel('time [us]')
plt.ylabel('Spectral Intensity [W/GHz/cm^2]')
#plt.ylabel('flux [W/m^2/Hz]')
plt.legend(loc=1)
plt.show()

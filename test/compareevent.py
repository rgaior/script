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
basename2 = sys.argv[2]

folder = '/Users/romain/work/Auger/EASIER/IPNcode/myversion/out/txt/'
name =folder+ basename
name2 =folder+ basename2
names = [name,name2]
figtrace = plt.figure()
#figtrace.suptitle('file: '+n,fontweight='bold',fontsize=15)
axtrace = plt.subplot(111)
for n in names:  
    if n == name:
        lstyle = '-'
    if n == name2:
        lstyle = '--'
        
    ev = event.Event(fname=n, type='test')
    ev.loadevent()
    for ant in ev.antennas: 
        if np.isnan(np.max(ant.power)):
            print 'nan !!!!!!!'
            continue

        time = ant.maketimearray()
        axtrace.plot(time*1e9,ant.power,ls=lstyle,label=str(ant.id))
#        axtrace.semilogy(time*1e9,ant.power,ls=lstyle,label=str(ant.id))

plt.legend(loc=4)
plt.show()

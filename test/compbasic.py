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
bnames = [basename, basename2]
fighist = plt.figure(figsize=(12,8))
ax1 = plt.subplot2grid((2,2), (0,0))
ax2 = plt.subplot2grid((2,2), (0,1))           
ax3 = plt.subplot2grid((2,2), (1,0))   
ax5 = plt.subplot2grid((2,2), (1,1))   
def getdetpos(typeofarray):
    detx = np.array([])
    dety = np.array([])
    if typeofarray == 'EA7':
        pos = constant.EA7position

    for p in pos.values():
        detx = np.append(detx,p[0])
        dety = np.append(dety,p[1])
    
    return [detx,dety]


for bn in bnames:
    folder = '/Users/romain/work/Auger/EASIER/IPNcode/myversion/out/txt/'
    names = glob.glob(folder+ bn+'*.dat')
    
    a_energy = np.array([])
    a_max = np.array([])
    a_theta = np.array([])
    a_dist = np.array([])
    count = 0
    a_x = np.array([])
    a_y = np.array([])
    det_x = np.array([])
    det_y = np.array([])
#for n in names[:100]:
#print names
    for n in names:
        ev = event.Event(fname=n, type='test')
        ev.loadevent()
    
        #    figtrace = plt.figure()
        #    axtrace = plt.subplot(111)
        for ant in ev.antennas: 
            if np.isnan(np.max(ant.power)):
                print 'nan !!!!!!!'
                continue
            a_energy = np.append(a_energy,ev.shower.energy)
            #        print 'max = ', np.max(ant.power)
            a_max = np.append(a_max,np.max(ant.power))  
            a_theta = np.append(a_theta,ev.shower.theta)
            corepos = np.array([ev.shower.x, ev.shower.y, 1400])
            #        disttocore = utils.getdistance(antpos,corepos)
            #        print 'antpos = ', antpos, ' corepos = ', corepos
            #        a_dist = np.append(a_dist,disttocore)
            #        print np.max(ant.power)
            a_x = np.append(a_x,ev.shower.x)
            a_y = np.append(a_y,ev.shower.y)

        
        #        plt.plot(ant.power)
        #        print np.max(ant.power)
        
            #            time = ant.maketimearray()
    #        axtrace.plot(time*1e9,ant.power,label=str(ant.id))
            count += 1
    
            print 'count = ', count
#fig1 = plt.figure(figsize = (8,8))                                              

#ax1 = plt.subplot(211)
#ax2 = plt.subplot(212)
#ax3 = plt.subplot(221)
#ax5 = plt.subplot(222)
#ax1.hist(a_energy,histtype='step',lw=2)
#ax2.hist(a_max,histtype='step',lw=2)
    ax1.hist(a_energy,histtype='step',lw=2,log=True)
#ax1.set_title('Energy [EeV]')
    ax1.set_xlabel('Energy [EeV]',fontsize=15)
    ax2.hist(a_max,histtype='step',lw=2,log=True)
#ax2.set_title('radio max [W]')
    ax2.set_xlabel('radio max [W]',fontsize=15)
    ax3.hist(a_theta,histtype='step',lw=2,log=True)
#ax3.set_title('theta [deg]')
    ax3.set_xlabel('theta [deg]',fontsize=15)
#ax5.hist(a_dist/1000,histtype='step',lw=2,log=True)
#ax5.set_title('dist to core [m]')
    ax5.set_xlabel('dist to core [km]',fontsize=15)
#ax3.plot(a_energy,histtype='step',lw=2,log=True)
#plt.hist(a_energy)
#plt.plot(a_energy,a_max,'o')
#plt.plot(ev.shower.depth,ev.shower.electron)

figarray = plt.figure(figsize=(8,8))
ax4 = plt.subplot(111)
ax4.plot(a_x,a_y,'o',label='shower core')
[det_x,det_y] = getdetpos('EA7')
ax4.plot(det_x,det_y,'ro',ms=10,label='detector position')
ax4.set_xlabel('X [m]')
ax4.set_ylabel('Y [m]')
plt.legend(loc=4)
plt.show()

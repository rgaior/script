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
plottrace = sys.argv[2]

folder = '/Users/romain/work/Auger/EASIER/IPNcode/myversion/out/'
print folder+ basename+'*.dat'
names = glob.glob(folder+ basename+'*.dat')
col = constant.col
a_energy = np.array([])
a_max = np.array([])
a_theta = np.array([])
a_dist = np.array([])
a_dist2 = np.array([])
count = 0
a_x = np.array([])
a_y = np.array([])
det_x = np.array([])
det_y = np.array([])
#for n in names[:100]:
#print names
sigma = 3e-14
nrofsigma = 5
print names
for n in names[::1]:
    ev = event.Event(fname=n, type='test')
    ev.loadevent()
    if ev.shower.energy < 5:
        print ' ev.shower.energy = ' , ev.shower.energy
        continue
        
    a_energy = np.append(a_energy,ev.shower.energy)
    a_theta = np.append(a_theta,ev.shower.theta)
    for ant in ev.antennas: 
        if np.isnan(np.max(ant.power)):
            print 'nan !!!!!!!'
            continue
        ant.power = ant.power
        max = np.max(ant.power)
        if max < nrofsigma*sigma:
            continue


        if plottrace == 'y':    
            title = 'E = '+str(ev.shower.energy) + ' theta = ' + str(ev.shower.theta) + ' phi = '+str(ev.shower.phi) + ' x = '+str(ev.shower.x) + ' y = '+str(ev.shower.y)
            figtrace = plt.figure()
            figtrace.suptitle(title)
            axtrace = plt.subplot(111)
#        print 'max = ', np.max(ant.power)
        a_max = np.append(a_max,np.max(ant.power))
        corepos = np.array([ev.shower.x, ev.shower.y, 50])
        u = utils.getvectorfromangle(corepos,utils.degtorad(ev.shower.theta),utils.degtorad(ev.shower.phi))
        #        corepos = np.array([ev.shower.x, ev.shower.y, 1400])
        antpos = constant.EA7position[ant.id]
        d = utils.getdistancetoline(corepos,antpos,u)
        disttocore = utils.getdistance(antpos,corepos)
        #        print 'antpos = ', antpos, ' corepos = ', corepos
        a_dist = np.append(a_dist,d)
        a_dist2 = np.append(a_dist2,disttocore)
        #        print np.max(ant.power)
        a_x = np.append(a_x,ev.shower.x)
        a_y = np.append(a_y,ev.shower.y)


#        plt.plot(ant.power)
#        print np.max(ant.power)

        time = ant.maketimearray()
        if plottrace == 'y':
            axtrace.semilogy(time*1e9,ant.power,c=col[ant.id],label=str(ant.id))
    count += 1

print 'count = ', count
#fig1 = plt.figure(figsize = (8,8))                                              
fighist = plt.figure(figsize=(10,8))
ax1 = plt.subplot2grid((2,2), (0,0))
ax2 = plt.subplot2grid((2,2), (0,1))           
ax3 = plt.subplot2grid((2,2), (1,0))   
ax5 = plt.subplot2grid((2,2), (1,1))   

#ax1 = plt.subplot(211)
#ax2 = plt.subplot(212)
#ax3 = plt.subplot(221)
#ax5 = plt.subplot(222)
#ax1.hist(a_energy,histtype='step',lw=2)
#ax2.hist(a_max,histtype='step',lw=2)
ax1.hist(a_energy*1e18,bins=np.logspace(18, 20, 20), histtype='step',lw=2,log=True)
ax1.set_xscale("log")
#ax1.set_title('Energy [EeV]')
ax1.set_xlabel('Energy [EeV]',fontsize=15)
ax2.hist(a_max,histtype='step',lw=2,log=True)
#ax2.set_title('radio max [W]')
ax2.set_xlabel('radio max [W]',fontsize=15)
ax3.hist(np.cos(a_theta*3.14/180),histtype='step',lw=2,log=True)
#ax3.set_title('theta [deg]')
ax3.set_xlabel('cos(theta)',fontsize=15)
#ax5.hist(a_dist/1000,histtype='step',lw=2,log=True)
ax5.hist(a_dist2/1000,histtype='step',lw=2,log=True)

#ax5.set_title('dist to core [m]')
ax5.set_xlabel('dist to axis [km]',fontsize=15)
#ax3.plot(a_energy,histtype='step',lw=2,log=True)
#plt.hist(a_energy)
#plt.plot(a_energy,a_max,'o')
#plt.plot(ev.shower.depth,ev.shower.electron)

figarray = plt.figure(figsize=(8,8))
ax4 = plt.subplot(111)
ax4.plot(a_x,a_y,'o',label='shower core')

pos = constant.EA7position
#x = np.array([])
#y = np.array([])
col = constant.col
#col = ['b','g','r','c','m','y','k']
for ant,c in zip(pos.values(),col.values()):
    ax4.plot(ant[0],ant[1],'o', markersize=20,c=c)
#ax4.plot(det_x,det_y,'ro',ms=10,label='detector position')
ax4.set_xlabel('X [m]')
ax4.set_ylabel('Y [m]')
plt.legend(loc=4)
plt.show()

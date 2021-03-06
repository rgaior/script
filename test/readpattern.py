import numpy as np
import sys
import matplotlib.pyplot as plt
import os
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
sys.path.append(classpath)
import utils

#fname = sys.argv[1]
basefolder = '/Users/romain/work/Auger/EASIER/IPNcode/myversion/install/config/GainPatterns/'
#basefolder = '/Users/romain/work/Auger/EASIER/IPNcode/newtry/mbr_imen/mbr/config/GainPatterns/'
fname = 'ASCONECHINOIS_dBGainTotal.xml'
fname2 = 'GainPattern-EASIER.xml'

#fname = 'LPSC_GainPattern.xml'
#fname = 'DMX_horn.xml'
#fname = 'LPSC_horn.xml'
file2 = basefolder + fname
file = basefolder + fname2

# print '********************************'
# print 'reading file:'
# print '********************************'

#phi = np.arange(-180,180,sphi)
#theta = np.arange(-180,170,stheta)
#print ' theta in main :  ', theta 
#print pattern

# #phi = np.arange(0,359,1)
# #theta = np.arange(0,179,2)

# #phi = [0,30,60,90]
# intpattern = 0
for f in [file, file2]: 
    pattern = utils.readpattern(f)
    sphi = 10
    stheta = 5
    [theta,phi] = utils.getpatternaxes(f)
    for p in [45,135]:
        if f == file and p == 45:
            continue
            
        thetagain = np.array([])
        for t in theta[:-2]:
            phigain = pattern[t]
            phiindex = int( (p-phi[0])/sphi )
            thetagain = np.append(thetagain,phigain[phiindex])
        if f == file2:
            plt.plot(theta[:-2],thetagain,ls='--',lw=2,label='GIOGADuck phi = '+str(p) + ' deg. (sim.)')
        if f == file:
            plt.plot(theta[:-2],thetagain,lw=2,label='EASIER (meas.)')

#print intpattern/np.pi
        
plt.xlim(0,180)
plt.ylim(-30,20)
plt.xlabel('angle [deg]')
plt.ylabel('gain [dB]')
plt.legend()
plt.show()

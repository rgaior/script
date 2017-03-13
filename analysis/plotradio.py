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
import simulation
import detector
import analyse
import waveform
import argparse
import glob
import pickle

parser = argparse.ArgumentParser()
parser.add_argument("-det", type=str, nargs='?',default='norsat', help="type of detector: gi, dmx, norsat, helix")
parser.add_argument("-scale", type=int, nargs='?',default=1, help="scaling of the radio power")
parser.add_argument("-iter", type=int, nargs='?',default=1, help="simulation iteration")
args = parser.parse_args()
dettype = args.det
scale = args.scale
iter = args.iter 

tsys = 100
binsize = 25e-9
tracelimit = 20
det = detector.Detector(temp = tsys, type=dettype)
det.loadspectrum()

folder = '/Users/romain/work/Auger/EASIER/IPNcode/script/results/afterelec/' + '/scaling' + str(int(scale)) + '/' + str(iter) + '/'
filenames = 'ev_'
names = glob.glob(folder+ filenames+'*.pkl')
ana = analyse.Analyse(det=det)
evcount = 0
a_max = np.array([])
noisedist = np.array([])
for n in names[::1]:
    print n
    file = open(n, 'rb')
    revent = pickle.load(file)
    if revent.shower.energy < 5:
        continue
    for ant in revent.antennas:       
        size = len(ant.trace)
        if size==0:
            continue
        time = np.arange(0,size*binsize,binsize)
        wf = waveform.Waveform(time,ant.trace)
        timepower = ant.maketimearray()
        wfori = waveform.Waveform(timepower,ant.power)
#        time = ant.maketimearray()
#        lpwf = ana.lowpass(wf,1e6,2)
        powerwf = ana.producepowerwaveform(wf)
        sigmawf = ana.producesigmawaveform(powerwf)
#        a_max = np.append(a_max, np.max(sigmawf.amp[100:-100]))
        if np.max(sigmawf.amp[180:220]) > 5:
            fig , (ax0,ax1) = plt.subplots(2,1)
            ax0.plot(wfori.time,wfori.amp)
#            ax1.plot(sigmawf.time,sigmawf.amp)
            ax1.plot(sigmawf.amp)
#        ax1.plot(powerwf.time,powerwf.amp)
#        plt.plot(ant.trace)
        
    file.close()
print 'events = ', evcount
plt.show()


#     id = int(n[n.rfind('_')+1:n.find('.dat')])
#     ev = event.Event(fname=n, type='test')
#     ev.loadevent()
#     ev.id = id
#     for ant in ev.antennas: 
#         if np.isnan(np.max(ant.power)):
#             print 'nan !!!!!!!'
#             continue
#         ant.power = ant.power
# #        ant.power = scale*ant.power
#         max = np.max(ant.power)
#         if max < nrofsigma*sigma:
#             continue
#         count+=1
#         time = ant.maketimearray()
#         sim = simulation.Simulation(det=det)        
#         sim.producetime()
#         sim.producenoise(True)
            
# #        sim.time = time
#         sim.setpowerenvelopewitharray([time,ant.power])
#         sim.producesignal()
#         simwf = waveform.Waveform(sim.time,sim.noise+sim.signal, type='hf')
#         wf = det.producesimwaveform(simwf,'adc',method)
#         ant.trace = wf.amp
        
#         #########save waveform##########
#         print 'here !!! '
#         filename = '/Users/romain/work/Auger/EASIER/IPNcode/script/results/afterelec/scaling1/testo_' + str(ev.id) + '_' + str(ant.id) + '.pkl'
#         output = open(filename, 'wb')
#         pickle.dump(ev,output)
#         output.close()

#         if (plottrace==True and count< tracelimit):
#             figtrace = plt.figure(figsize=(10,8))
#             figtrace.suptitle('file: '+n,fontweight='bold',fontsize=15)
#             axtrace = plt.subplot(111)
#             plt.plot(wf.time, wf.amp)
        
# plt.show()

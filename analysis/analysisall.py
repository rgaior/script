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
args = parser.parse_args()
dettype = args.det

tsys = 100
normalization = 699/63.5
binsize = 25e-9
tracelimit = 20
det = detector.Detector(temp = tsys, type=dettype)
det.loadspectrum()

scales = np.array([1,10,50,100,200])
iter = [1,2,3,4,5,6,7,8,9,10]
a_mean = np.array([])
a_rms = np.array([])
for scale in scales:
    meannr = 0 
    rmsnr = 0
    a_ev = np.array([])
    for it in iter:
        folder = '/Users/romain/work/Auger/EASIER/IPNcode/script/results/afterelec/' + '/scaling' + str(int(scale)) + '/' + str(it) + '/'
        filenames = 'ev_'
        names = glob.glob(folder+ filenames+'*.pkl')
        ana = analyse.Analyse(det=det)
        evcount = 0
        a_max = np.array([])
#        print names
        for n in names[::1]:
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
                #        time = ant.maketimearray()
                #        lpwf = ana.lowpass(wf,1e6,2)
                powerwf = ana.producepowerwaveform(wf)
                sigmawf = ana.producesigmawaveform(powerwf)
                a_max = np.append(a_max, np.max(sigmawf.amp[150:250]))
                if np.max(sigmawf.amp[150:250]) > 5 :
                    evcount +=1
            file.close()
        print ' evcount = ' , evcount        
        a_ev = np.append(a_ev,evcount)
    a_mean = np.append(a_mean,np.mean(a_ev)/normalization) 
    a_rms = np.append(a_rms,np.std(a_ev)/normalization) 

out = 'results'
print a_mean
np.savez(out,scales=scales, mean=a_mean,rms=a_rms)

plt.errorbar(scales,a_mean,yerr=a_rms)
plt.gca().set_xscale("log", nonposy='clip')
plt.gca().set_yscale("log", nonposy='clip')

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

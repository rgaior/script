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
import waveform
import argparse
import glob
import pickle

parser = argparse.ArgumentParser()
parser.add_argument("-det", type=str, nargs='?',default='norsat', help="type of detector: gi, dmx, norsat, helix")
parser.add_argument("-folder", type=str, nargs='?',default='/helix/txt/', help="folder with the text file of events")
parser.add_argument("-basename", type=str, nargs='?',default='Helixdelta500', help="name of the files to glob on")
parser.add_argument("-scale", type=int, nargs='?',default=1, help="scaling of the radio power")
parser.add_argument("-iter", type=int, nargs='?',default=1, help="simulation iteration")
parser.add_argument("-plottrace", action='store_true',help="plot the traces (can be lots of them) if stated")
args = parser.parse_args()
dettype = args.det
plottrace = args.plottrace
basefolder = args.folder
basename = args.basename
folder = constant.MBRsimoutfolder +  basefolder
names = glob.glob(folder+basename+'*.dat')
scale = args.scale
iter = args.iter 
print 'folder+basename+*.dat) = ' , folder+basename
print '#####################################'
print '#####################################'
method = 3

tsys = 100
tracelimit = 20
det = detector.Detector(temp = tsys, type=dettype)
det.loadspectrum()
count = 0
nrofsigma = 1
sigma = 3e-14

for n in names:
    saveevent = False
    id = int(n[n.rfind('_')+1:n.find('.dat')])
    ev = event.Event(fname=n, type='test')
    ev.loadevent()
    ev.id = id
    ev.scale = scale
    for ant in ev.antennas: 
        if np.isnan(np.max(ant.power)):
            print 'nan !!!!!!!'
            continue

        ant.power = scale*ant.power
        max = np.max(ant.power)
        if max < nrofsigma*sigma:
            continue
        saveevent = True
        count+=1
        time = ant.maketimearray()
        sim = simulation.Simulation(det=det)        
        sim.producetime()
        sim.producenoise(True)
            
#        sim.time = time
        sim.setpowerenvelopewitharray([time,ant.power])
        sim.producesignal()
        simwf = waveform.Waveform(sim.time,sim.noise+sim.signal, type='hf')
        wf = det.producesimwaveform(simwf,'adc',method)
        ant.trace = wf.amp
        

        if (plottrace==True and count< tracelimit):
            figtrace = plt.figure(figsize=(10,8))
            figtrace.suptitle('file: '+n,fontweight='bold',fontsize=15)
            axtrace = plt.subplot(111)
            plt.plot(wf.time, wf.amp)
    if saveevent == True:
        #########save waveform##########
        folder = '/Users/romain/work/Auger/EASIER/IPNcode/script/results/afterelec/' + '/scaling' + str(int(scale)) + '/' + str(iter) + '/'
        filename = 'ev_' + str(ev.id) + '.pkl'
        output = open(folder + filename, 'wb')
        pickle.dump(ev,output)
        output.close()
        
        
plt.show()

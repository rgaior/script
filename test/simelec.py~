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

file = '/Users/romain/work/Auger/EASIER/IPNcode/myversion/out/EASIERGDcomparison/txt/EASIER_power_13.dat'
parser = argparse.ArgumentParser()
parser.add_argument("detector", type=str, nargs='?',default='norsat', help="type of detector: gi, dmx, norsat, helix")
args = parser.parse_args()
#basename = sys.argv[1]
#plottrace = sys.argv[2]

folder = '/Users/romain/work/Auger/EASIER/IPNcode/myversion/out/'
names = glob.glob(folder+ basename+'*.dat')

print '#####################################'
print '###### detector: ', args.detector ,' ######'
print '###### power det method: ', args.method ,' ######'
print '#####################################'
dettype = args.detector
method = 3
#signalfiles = glob.glob(args.signalfile+'/simTrace*')
#signalfiles = glob.glob(args.signalfile+'/simTrace_ev2_433*')                                                                                                   
names = [file]

print names

tsys = 1

det = detector.Detector(temp = tsys, type=dettype)
det.loadspectrum()
#print names
for n in names:
    ev = event.Event(fname=n, type='test')
    ev.loadevent()
    figtrace = plt.figure(figsize=(10,8))
    figtrace.suptitle('file: '+n,fontweight='bold',fontsize=15)
    axtrace = plt.subplot(111)
    for ant in ev.antennas: 
        if np.isnan(np.max(ant.power)):
            print 'nan !!!!!!!'
            continue 
        time = ant.maketimearray()
        sim = simulation.Simulation(det=det)
        
        sim.producetime()
        sim.producenoise(True)
        
#        sim.time = time
        sim.setpowerenvelopewitharray([time,ant.power])
        sim.producesignal()
        simwf = waveform.Waveform(sim.time,sim.noise+sim.signal, type='hf')
        wf = det.producesimwaveform(simwf,'adc',method)

        fig = plt.figure()
        plt.plot(wf.time, wf.amp)
        
plt.show()

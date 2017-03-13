import matplotlib.pyplot as plt
import numpy as np
import os
import sys
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
sys.path.append(classpath)
import utils
import constant

pos = constant.EA7position
x = np.array([])
y = np.array([])
col = constant.col
for ant,c in zip(pos.values(),col.values()):
    plt.plot(ant[0],ant[1],'o', markersize=50,c=c)

plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.show()


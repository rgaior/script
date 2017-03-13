import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
import math
def degtorad(deg):
    return math.pi*deg/180

fig = plt.figure()
ax = fig.gca(projection='3d')
pos = constant.EA7position
x = np.array([])
y = np.array([])
col = constant.col
    
theta = degtorad(45)
phi = degtorad(-90)
rshower = np.linspace(0,100,100)

B = np.array([0,0,0])
x = rshower * np.sin(theta) * np.cos(phi) + B[0]
y = rshower * np.sin(theta) * np.sin(phi) + B[1]
z = rshower * np.cos(theta) + B[2]

A = np.array([10,10,0])
BA = B-A
u = [np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)]
BAxu = np.cross(BA,u)
d = np.linalg.norm(BAxu)/np.linalg.norm(u)
print 'distance = ' , d

ax.plot(x,y,z)
#ax.plot(x,y,z,'k')
#for ant,c in zip(pos.values(),col.values()):
#    plt.plot(ant[0],ant[1],0,'o', markersize=50,color=c)
    
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.xlim(-20,20)
plt.ylim(-20,20)
ax.set_zlim(0,40)
plt.show()


#import utils
import math
import numpy as np
#import constant
import shower
class Shower:
    def __init__(self):
        self.energy = 0
        self.theta = 0
        self.phi = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.depth = np.array([])
        self.electron = np.array([])
        self.dedx = np.array([])        
        self.height = np.array([])        
        self.posx = np.array([])
        self.posy = np.array([])
        self.posz = np.array([])
        

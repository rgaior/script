#import utils
import math
import numpy as np
#import constant
class Antenna:
    def __init__(self):
        self.id = 0
        self.starttime = 0
        self.binwidth = 0
        self.power = np.array([])
        self.aeff = np.array([])
        self.trace = np.array([])
 
    def maketimearray(self):
        return np.arange(self.starttime,self.binwidth*len(self.power),self.binwidth)

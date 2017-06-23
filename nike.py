import sqlite3
from datetime import datetime
from datetime import date
import matplotlib.pyplot as plt
import numpy
import numpy as np
from matplotlib import pylab as pl

from initializer import DBInitializer


def curve(self, x, theta):
    curve = list()
    for th in theta:
        x1 = x[0] / np.sqrt(2)
        x2 = x[1] * np.sin(th)
        #x3 = x[2] * np.cos(th)
        #x4 = x[3] * np.sin(2. * th)
        curve.append(x1 + x2 + x3 + x4)
    return curve

def draw_curve(self, x):
    accuracy = 1000
    theta = np.linspace(-np.pi, np.pi, accuracy)
    pl.plot(theta, self.curve(x, theta), 'r')
    #obj = Oracle('data_base.db')



"workspace change"
s = [-23615.74443014163, 1470.9718784037736, 161004.2953757798, 597514.4771759581]
s1 = [-27.499999999987086, 236.14285714274644, -467.35714285685185, 736343.3999999999]
#obj.draw_curve(s)
obj.draw_curve(s1)

pl.xlim(-np.pi, np.pi)
pl.show()
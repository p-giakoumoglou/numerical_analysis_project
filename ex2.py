# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:56:54 2021
@author: Paschalis Giakoumoglou 10054
@author: Christos Kyratsous 10105 
"""

import matplotlib.pyplot as plt
import numpy as np

def euler(F, x0, t0, tmax, dt):
    t = np.arange(t0, tmax + dt, dt)
    x = np.zeros((len(t), len(x0)), np.float64)
    x[0, :] = x0
    for n in range(len(t) - 1):
        x[n + 1, :] = x[n, :] + dt * F(t[n], x[n, :])
    return t, x

def F(t, x):
    return np.array([1.1 * x[0] - 0.4 * x[0] * x[1], 0.4 * x[0] * x[1] - 0.1 * x[1]])

x0 = np.array([20, 1])
dt = [10**-2, 10**-3]
for i in range(len(dt)):
    t, x = euler(F, x0, 0, 200, dt[i])
    #t, x = euler(F, x0, 0, 2000, 10**-5)
    
    plt.plot(t, x)
    plt.title("Time Evolution of Foxes and Rabbits Population (dt ="+str(dt[i])+")")
    plt.legend("RF")
    plt.xlabel("Time")
    plt.ylabel("No. of Rabbits and No. of Foxes")
    plt.grid(axis="x")
    plt.show()
    
    plt.plot(x[:, 0], x[:, 1])
    plt.title("Evolution of Foxes and Rabbits Population (dt ="+str(dt[i])+")")
    plt.xlabel("Rabbits")
    plt.ylabel("Foxes")
    plt.grid()
    plt.show()




# -*- coding: utf-8 -*-
"""
Created on 21/05/2021
@author: Paschalis Giakoumoglou 10054
@author: Christos Kyratsous 10105 
"""

import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    return math.exp(3*x)*math.sin(2*x)

def rectLeft(f, a, b, N):
    h = (b-a)/N
    tot = 0
    for i in range(N):
        tot += f(a+i*h)
    return tot*h
    
def rectRight(f, a, b, N):
    h = (b-a)/N
    tot = 0
    for i in range(N):
        tot += f(a+i*h+h)
    return tot*h

def trapezoid(f, a, b, N):
    h = (b - a) / N
    tot = f(a)+f(b)
    for i in range(1, N):
        tot += 2 * f(a + i * h)
    return (h / 2) * tot

def simp(f, a,b,N):
    h = (b-a)/N
    tot = f(a) + f(b)
    for i in range(1,N,1):
        tot += f(a+i*h)*(2*(i%2 == 0) + 4*(i%2 == 1))
    return tot*h/3

def calcError(f, a, b, maxErrors, realResult):
    val = np.arange(10,1010,10)
    val = val.astype(np.int64)
    exponents = np.array([1,1,2,4])
    x = np.zeros((100,1), np.double)
    y = np.zeros((100,1), np.double)
    z = np.zeros((100,1), np.double)
    name = ["Left Rectangle", "Right Rectangle", "Trapezoid", "Simpson"]
    for counter, fun in enumerate([rectLeft, rectRight, trapezoid, simp]):
        for i, N in enumerate(val):
            y[i] = math.log10(((abs(fun(f ,a, b, N)-realResult))))
            x[i] = math.log10((b-a)/N)
            z[i] = math.log10(maxErrors[counter]/val[i]**exponents[counter])
        
        plt.xlabel("Values of h")
        plt.ylabel("Absolute Error")
        plt.plot(x, y, marker = 'o')
        plt.plot(x, z, marker = 'o')
        plt.title(name[counter])
        plt.show()
      
realResult = 3/13*math.exp(3*math.pi/4)+2/13
a = 0
b = math.pi/4   
maxErrors = np.array([(((b-a)**2)/2)*3*math.exp(3*math.pi/4), 
                      (((b-a)**2)/2)*3*math.exp(3*math.pi/4), 
                      ((b-a)**3)/12 * 5 * math.exp(3*math.pi/4), 
                      ((b-a)**5/180) * 119 * math.exp(3*math.pi/4)]) 
calcError(f, a, b, maxErrors, realResult)

  


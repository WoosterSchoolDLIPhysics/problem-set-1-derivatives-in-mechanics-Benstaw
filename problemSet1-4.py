#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:30:21 2017

@author: ben
"""

from pylab import *

dx = .001
xa = -pi
xb = .5+dx
t = arange(xa,xb,dx)

def der_fivept(f,x):
    '''This is the left handed derivative. 
    Where on the interval does it fail? This is fourth order accurate!'''
    d = zeros(len(x))
    d[1:-1] = (f[2:]-f[:-2])/(x[2:]-x[:-2])
    d[2:-2] = (-f[4:]+8*f[3:-1]-8*f[1:-3]+f[:-4])/(12*(x[1]-x[0]))
    d[0] = (f[1]-f[0])/(x[1]-x[0])
    d[-1] = (f[-1]-f[-2])/(x[-1]-x[-2])
    return d

f = 3 * sin(2 * pi * t) + 2 * cos(2 * pi * t)

g = sqrt(der_fivept(3 * sin(2 * pi * t),t)**2 + der_fivept(2 * cos(2 * pi * t),t)**2)

h = der_fivept(sqrt(der_fivept(3 * sin(2 * pi * t),t)**2 + der_fivept(2 * cos(2 * pi * t),t)**2),t)

print(max(g))

for counter in range(len(g)):
    if g[counter] == max(g):
        print(counter)
        

figure(1)
clf()
title("Distance V. Time")
plot(t,f, 'b-o')

figure(2)
clf()
title("Velocity V. Time")
plot(t,g, 'r-o')

figure(3)
clf()
title("Acceleration V. Time")
plot(t,h, 'k-o')

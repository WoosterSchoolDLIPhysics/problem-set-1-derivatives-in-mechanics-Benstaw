#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 08:15:30 2017

@author: ben
"""

from pylab import *

dx = .001
xa = -pi
xb = .5+dx
t = arange(0,5,.1)

def der_fivept(f,x):
    '''This is the left handed derivative. 
    Where on the interval does it fail? This is fourth order accurate!'''
    d = zeros(len(x))
    d[1:-1] = (f[2:]-f[:-2])/(x[2:]-x[:-2])
    d[2:-2] = (-f[4:]+8*f[3:-1]-8*f[1:-3]+f[:-4])/(12*(x[1]-x[0]))
    d[0] = (f[1]-f[0])/(x[1]-x[0])
    d[-1] = (f[-1]-f[-2])/(x[-1]-x[-2])
    return d

distance = t**4 - 4 * t**3 + 2 * t**2 + 6
distance2 = u**4 - 4 * u**3 + 2 * u**2 + 6


velocity = der_fivept(distance, t)
velocity2 = der_fivept(distance2, u)
        
acceleration = der_fivept(velocity,t)

for time in range(len(t)):
    if time == 1:
        print(acceleration[time])


figure(1)
clf()
title("Velocity V. Time")
plot(t,velocity, 'r-o')


figure(2)
clf()
title("Acceleration V. Time")
plot(t,acceleration, "b-o")
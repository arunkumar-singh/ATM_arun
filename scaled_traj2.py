# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 14:40:17 2016

@author: aks
"""

from numpy import *


def scaled_traj2(x, y, theta, vel, thetadot, scale, delt_sc):
    
    
    #print sqrt(xdot**2+ydot**2)
    xdot = (vel*scale)*cos(theta+thetadot*scale*delt_sc) 
    ydot = (vel*scale)*sin(theta+thetadot*scale*delt_sc) 
    
    xt = x+xdot*delt_sc
    yt = y+ydot*delt_sc
    thetat = theta+thetadot*scale*delt_sc
    
    return xt, yt, thetat, vel*scale, thetadot*scale
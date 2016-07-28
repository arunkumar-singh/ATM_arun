# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:46:55 2016

@author: aks
"""

from numpy import *


def scale_calc_iter(xt_1, yt_1, theta_1, vel_1, xt_2, yt_2, theta_2, vel_2, rad):
     R = rad
     x1t = xt_1
     y1t = yt_1
     xot = xt_2
     yot = yt_2
     x1tdot = vel_1*cos(theta_1)     
     y1tdot = vel_1*sin(theta_1)
     xotdot = vel_2*cos(theta_2)
     yotdot = vel_2*sin(theta_2)
     
    
     
    
     
     A = (-R**2*(x1tdot**2+y1tdot**2)+((x1t-xot)*y1tdot+x1tdot*(-y1t+yot))**2)
     
     B = 2*(-((x1t-xot)*y1tdot+x1tdot*(-y1t+yot))*(xotdot*(-y1t+yot)+(x1t-xot)*yotdot)+R**2*(x1tdot*xotdot+y1tdot*yotdot))
     
     C = (xotdot*(y1t-yot)+(-x1t+xot)*yotdot)**2-R**2*(xotdot**2+yotdot**2)
     
     
   
     
     
     return A, B, C

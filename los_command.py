# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 14:10:15 2016

@author: aks
"""

from numpy import *

def los_command(xo, yo, xf, yf, vel, theta):
    t = 10    
    
    t1 = 1.3
    ts = t1
    a1 = 0
    theta1 = theta
    
    
   
    
    R = 1.3
    
    temp_velx = (xf-xo)/t
    temp_vely = (yf-yo)/t
    look_ahead_x = xo+temp_velx*t1
    look_ahead_y = yo+temp_vely*t1
    
    look_ahead_vector = array([look_ahead_x-xo, look_ahead_y-yo])
    current_vel_vector = array([vel*cos(theta), vel*sin(theta)])
    sin_eta = cross(current_vel_vector, look_ahead_vector)/(linalg.norm(look_ahead_vector)*linalg.norm(current_vel_vector))
    
        
    commanded_acc = abs((2*(vel**2)/(linalg.norm(look_ahead_vector)))*sin_eta)
    
       
    thetadot = sign(sin_eta)*sqrt(commanded_acc/R)
    w1 = thetadot
    
    
    #print sin_eta    
    
    delt = 0.01
    
    
    xt = xo+vel*cos(theta+thetadot*delt)*delt
    yt = yo+vel*sin(theta+thetadot*delt)*delt
    theta_new = theta+thetadot*delt
    
#    
#    if(thetadot!=0):
#        xt = xo+a1*ts*sin(theta1 + ts*w1)/w1 - a1*cos(theta1)/w1**2 + a1*cos(theta1 + ts*w1)/w1**2 - v1*sin(theta1)/w1 + v1*sin(theta1 + ts*w1)/w1
#
#        yt = yo-a1*ts*cos(theta1 + ts*w1)/w1 - a1*sin(theta1)/w1**2 + a1*sin(theta1 + ts*w1)/w1**2 + v1*cos(theta1)/w1 - v1*cos(theta1 + ts*w1)/w1
#        theta_new = theta+thetadot*t1         
#        
#    if(thetadot==0):
#        xt = xo + (a1*ts**2/2 + ts*v1)*cos(theta1)
#
#        yt = yo + (a1*ts**2/2 + ts*v1)*sin(theta1)
#        
#        theta_new = theta+thetadot*t1
    
    
    
    
    return xt, yt, theta_new, vel, thetadot
    
    
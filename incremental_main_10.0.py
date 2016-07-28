# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 11:26:32 2016

@author: aks
"""

from numpy import *
from perturbed_finalpos import perturbed_finalpos
from los_command import los_command
from mat_comp_iter import matrix_comp_iter
from sc_fn_compute3 import sc_fn_compute3
from scaled_int import scaled_int
from scaled_traj2 import scaled_traj2
import matplotlib.pyplot as plt
from drawnow import drawnow



r = 2.5
rad = 0.125/2
num = 20 #### number of robots

Vmin = 0.4
Vmax = 2.0
xddotmax = 5.0
yddotmax = 5.0



theta_1 = pi/20
theta_2 = 2*pi/20
theta_3 = 3*pi/20
theta_4 = 4*pi/20
theta_5 = 5*pi/20
theta_6 = 6*pi/20
theta_7 = 7*pi/20
theta_8 = 8*pi/20
theta_9 = 9*pi/20
theta_10 = 10*pi/20
theta_11 = 11*pi/20
theta_12 = 12*pi/20
theta_13 = 13*pi/20
theta_14 = 14*pi/20
theta_15 = 15*pi/20
theta_16 = 16*pi/20
theta_17 = 17*pi/20
theta_18 = 18*pi/20
theta_19 = 19*pi/20
theta_20 = 20*pi/20

##################robot 1

xo_1 = r*cos(theta_1)
xf_1 = r*cos(theta_1+pi)
xdoto_1 = (xf_1-xo_1)/(10.220-2)
xdotf_1 = xdoto_1
xddoto_1 = 0
xddotf_1 = 0

yo_1 = r*sin(theta_1)
yf_1 = r*sin(theta_1+pi)
ydoto_1 = (yf_1-yo_1)/(10.220-2)
ydotf_1 = ydoto_1
yddoto_1 = 0
yddotf_1 = 0

########################################################robot 2

xo_2 = r*cos(theta_2)
xf_2 = r*cos(theta_2+pi)
xdoto_2 = (xf_2-xo_2)/(10.220-2)
xdotf_2 = xdoto_2
xddoto_2 = 0
xddotf_2 = 0

yo_2 = r*sin(theta_2)
yf_2 = r*sin(theta_2+pi)
ydoto_2 = (yf_2-yo_2)/(10.220-2)
ydotf_2 = ydoto_2
yddoto_2 = 0
yddotf_2 = 0


##############################robot 3



xo_3 = r*cos(theta_3)
xf_3 = r*cos(theta_3+pi)
xdoto_3 = (xf_3-xo_3)/(10.220-2)
xdotf_3 = xdoto_3
xddoto_3 = 0
xddotf_3 = 0

yo_3 = r*sin(theta_3)
yf_3 = r*sin(theta_3+pi)
ydoto_3 = (yf_3-yo_3)/(10.220-2)
ydotf_3 = ydoto_3
yddoto_3 = 0
yddotf_3 = 0


########################################################robot 4

xo_4 = r*cos(theta_4)
xf_4 = r*cos(theta_4+pi)
xdoto_4 = (xf_4-xo_4)/(10.220-2)
xdotf_4 = xdoto_4
xddoto_4 = 0
xddotf_4 = 0

yo_4 = r*sin(theta_4)
yf_4 = r*sin(theta_4+pi)
ydoto_4 = (yf_4-yo_4)/(10.220-2)
ydotf_4 = ydoto_4
yddoto_4 = 0
yddotf_4 = 0


########################################################robot 5

xo_5 = r*cos(theta_5)
xf_5 = r*cos(theta_5+pi)
xdoto_5 = (xf_5-xo_5)/(10.220-2)
xdotf_5 = xdoto_5
xddoto_5 = 0
xddotf_5 = 0

yo_5 = r*sin(theta_5)
yf_5 = r*sin(theta_5+pi)
ydoto_5 = (yf_5-yo_5)/(10.220-2)
ydotf_5 = ydoto_5
yddoto_5 = 0
yddotf_5 = 0


########################################################robot 6

xo_6 = r*cos(theta_6)
xf_6 = r*cos(theta_6+pi)
xdoto_6 = (xf_6-xo_6)/(10.220-2)
xdotf_6 = xdoto_6
xddoto_6 = 0
xddotf_6 = 0

yo_6 = r*sin(theta_6)
yf_6 = r*sin(theta_6+pi)
ydoto_6 = (yf_6-yo_6)/(10.220-2)
ydotf_6 = ydoto_6
yddoto_6 = 0
yddotf_6 = 0

########################################################robot 7

xo_7 = r*cos(theta_7)
xf_7 = r*cos(theta_7+pi)
xdoto_7 = (xf_7-xo_7)/(10.220-2)
xdotf_7 = xdoto_7
xddoto_7 = 0
xddotf_7 = 0

yo_7 = r*sin(theta_7)
yf_7 = r*sin(theta_7+pi)
ydoto_7 = (yf_7-yo_7)/(10.220-2)
ydotf_7 = ydoto_7
yddoto_7 = 0
yddotf_7 = 0


########################################################robot 8

xo_8 = r*cos(theta_8)
xf_8 = r*cos(theta_8+pi)
xdoto_8 = (xf_8-xo_8)/(10.220-2)
xdotf_8 = xdoto_8
xddoto_8 = 0
xddotf_8 = 0

yo_8 = r*sin(theta_8)
yf_8 = r*sin(theta_8+pi)
ydoto_8 = (yf_8-yo_8)/(10.220-2)
ydotf_8 = ydoto_8
yddoto_8 = 0
yddotf_8 = 0


########################################################robot 9

xo_9 = r*cos(theta_9)
xf_9 = r*cos(theta_9+pi)
xdoto_9 = (xf_9-xo_9)/(10.220-2)
xdotf_9 = xdoto_9
xddoto_9 = 0
xddotf_9 = 0

yo_9 = r*sin(theta_9)
yf_9 = r*sin(theta_9+pi)
ydoto_9 = (yf_9-yo_9)/(10.220-2)
ydotf_9 = ydoto_9
yddoto_9 = 0
yddotf_9 = 0


########################################################robot 10

xo_10 = r*cos(theta_10)
xf_10 = r*cos(theta_10+pi)
xdoto_10 = (xf_10-xo_10)/(10.220-2)
xdotf_10 = xdoto_10
xddoto_10 = 0
xddotf_10 = 0

yo_10 = r*sin(theta_10)
yf_10 = r*sin(theta_10+pi)
ydoto_10 = (yf_10-yo_10)/(10.220-2)
ydotf_10 = ydoto_10
yddoto_10 = 0
yddotf_10 = 0


#####################robot 11

xo_11 = r*cos(theta_11)
xf_11 = r*cos(theta_11+pi)
xdoto_11 = (xf_11-xo_11)/(10.220-2)
xdotf_11 = xdoto_11
xddoto_11 = 0
xddotf_11 = 0

yo_11 = r*sin(theta_11)
yf_11 = r*sin(theta_11+pi)
ydoto_11 = (yf_11-yo_11)/(10.220-2)
ydotf_11 = ydoto_11
yddoto_11 = 0
yddotf_11 = 0

#########################robot 12

xo_12 = r*cos(theta_12)
xf_12 = r*cos(theta_12+pi)
xdoto_12 = (xf_12-xo_12)/(10.220-2)
xdotf_12 = xdoto_12
xddoto_12 = 0
xddotf_12 = 0

yo_12 = r*sin(theta_12)
yf_12 = r*sin(theta_12+pi)
ydoto_12 = (yf_12-yo_12)/(10.220-2)
ydotf_12 = ydoto_12
yddoto_12 = 0
yddotf_12 = 0

###############################robot 13

xo_13 = r*cos(theta_13)
xf_13 = r*cos(theta_13+pi)
xdoto_13 = (xf_13-xo_13)/(10.220-2)
xdotf_13 = xdoto_13
xddoto_13 = 0
xddotf_13 = 0

yo_13 = r*sin(theta_13)
yf_13 = r*sin(theta_13+pi)
ydoto_13 = (yf_13-yo_13)/(10.220-2)
ydotf_13 = ydoto_13
yddoto_13 = 0
yddotf_13 = 0

#################robot 14
xo_14 = r*cos(theta_14)
xf_14 = r*cos(theta_14+pi)
xdoto_14 = (xf_14-xo_14)/(10.220-2)
xdotf_14 = xdoto_14
xddoto_14 = 0
xddotf_14 = 0

yo_14 = r*sin(theta_14)
yf_14 = r*sin(theta_14+pi)
ydoto_14 = (yf_14-yo_14)/(10.220-2)
ydotf_14 = ydoto_14
yddoto_14 = 0
yddotf_14 = 0

#######################robot 15

xo_15 = r*cos(theta_15)
xf_15 = r*cos(theta_15+pi)
xdoto_15 = (xf_15-xo_15)/(10.220-2)
xdotf_15 = xdoto_15
xddoto_15 = 0
xddotf_15 = 0

yo_15 = r*sin(theta_15)
yf_15 = r*sin(theta_15+pi)
ydoto_15 = (yf_15-yo_15)/(10.220-2)
ydotf_15 = ydoto_15
yddoto_15 = 0
yddotf_15 = 0

##############robot 16
xo_16 = r*cos(theta_16)
xf_16 = r*cos(theta_16+pi)
xdoto_16 = (xf_16-xo_16)/(10.220-2)
xdotf_16 = xdoto_16
xddoto_16 = 0
xddotf_16 = 0

yo_16 = r*sin(theta_16)
yf_16 = r*sin(theta_16+pi)
ydoto_16 = (yf_16-yo_16)/(10.220-2)
ydotf_16 = ydoto_16
yddoto_16 = 0
yddotf_16 = 0

##################robot 17
xo_17 = r*cos(theta_17)
xf_17 = r*cos(theta_17+pi)
xdoto_17 = (xf_17-xo_17)/(10.220-2)
xdotf_17 = xdoto_17
xddoto_17 = 0
xddotf_17 = 0

yo_17 = r*sin(theta_17)
yf_17 = r*sin(theta_17+pi)
ydoto_17 = (yf_17-yo_17)/(10.220-2)
ydotf_17 = ydoto_17
yddoto_17 = 0
yddotf_17 = 0

##############robot 18

xo_18 = r*cos(theta_18)
xf_18 = r*cos(theta_18+pi)
xdoto_18 = (xf_18-xo_18)/(10.220-2)
xdotf_18 = xdoto_18
xddoto_18 = 0
xddotf_18 = 0

yo_18 = r*sin(theta_18)
yf_18 = r*sin(theta_18+pi)
ydoto_18 = (yf_18-yo_18)/(10.220-2)
ydotf_18 = ydoto_18
yddoto_18 = 0
yddotf_18 = 0

####################robot 19
xo_19 = r*cos(theta_19)
xf_19 = r*cos(theta_19+pi)
xdoto_19 = (xf_19-xo_19)/(10.220-2)
xdotf_19 = xdoto_19
xddoto_19 = 0
xddotf_19 = 0

yo_19 = r*sin(theta_19)
yf_19 = r*sin(theta_19+pi)
ydoto_19 = (yf_19-yo_19)/(10.220-2)
ydotf_19 = ydoto_19
yddoto_19 = 0
yddotf_19 = 0

#####################robot 20
xo_20 = r*cos(theta_20)
xf_20 = r*cos(theta_20+pi)
xdoto_20 = (xf_20-xo_20)/(10.220-2)
xdotf_20 = xdoto_20
xddoto_20 = 0
xddotf_20 = 0

yo_20 = r*sin(theta_20)
yf_20 = r*sin(theta_20+pi)
ydoto_20 = (yf_20-yo_20)/(10.220-2)
ydotf_20 = ydoto_20
yddoto_20 = 0
yddotf_20 = 0

###################################


count = 10000

#####################################

init_xdot = array([xdoto_1, xdoto_2, xdoto_3, xdoto_4, xdoto_5, xdoto_6, xdoto_7, xdoto_8, xdoto_9, xdoto_10, xdoto_11, xdoto_12, xdoto_13, xdoto_14, xdoto_15, xdoto_16, xdoto_17, xdoto_18, xdoto_19, xdoto_20 ]) 

init_ydot = array([ydoto_1, ydoto_2, ydoto_3, ydoto_4, ydoto_5, ydoto_6, ydoto_7, ydoto_8, ydoto_9, ydoto_10, ydoto_11, ydoto_12, ydoto_13, ydoto_14, ydoto_15, ydoto_16, ydoto_17, ydoto_18, ydoto_19, ydoto_20 ])


init_xddot = array([xddoto_1, xddoto_2, xddoto_3, xddoto_4, xddoto_5, xddoto_6, xddoto_7, xddoto_8, xddoto_9, xddoto_10, xddoto_11, xddoto_12, xddoto_13, xddoto_14, xddoto_15, xddoto_16, xddoto_17, xddoto_18, xddoto_19, xddoto_20 ]) 

init_yddot = array([yddoto_1, yddoto_2, yddoto_3, yddoto_4, yddoto_5, yddoto_6, yddoto_7, yddoto_8, yddoto_9, yddoto_10, yddoto_11, yddoto_12, yddoto_13, yddoto_14, yddoto_15, yddoto_16, yddoto_17, yddoto_18, yddoto_19, yddoto_20 ])



init_x = array([xo_1, xo_2, xo_3, xo_4, xo_5, xo_6, xo_7, xo_8, xo_9, xo_10, xo_11, xo_12, xo_13, xo_14, xo_15, xo_16, xo_17, xo_18, xo_19, xo_20])
init_y = array([yo_1, yo_2, yo_3, yo_4, yo_5, yo_6, yo_7, yo_8, yo_9, yo_10, yo_11, yo_12, yo_13, yo_14, yo_15, yo_16, yo_17, yo_18, yo_19, yo_20])


init_theta = array([arctan2(yf_1-yo_1, xf_1-xo_1), arctan2(yf_2-yo_2, xf_2-xo_2), arctan2(yf_3-yo_3, xf_3-xo_3), arctan2(yf_4-yo_4, xf_4-xo_4), arctan2(yf_5-yo_5, xf_5-xo_5), arctan2(yf_6-yo_6, xf_6-xo_6), arctan2(yf_7-yo_7, xf_7-xo_7), arctan2(yf_8-yo_8, xf_8-xo_8), arctan2(yf_9-yo_9, xf_9-xo_9), arctan2(yf_10-yo_10, xf_10-xo_10), arctan2(yf_11-yo_11, xf_11-xo_11), arctan2(yf_12-yo_12, xf_12-xo_12), arctan2(yf_13-yo_13, xf_13-xo_13), arctan2(yf_14-yo_14, xf_14-xo_14), arctan2(yf_15-yo_15, xf_15-xo_15), arctan2(yf_16-yo_16, xf_16-xo_16), arctan2(yf_17-yo_17, xf_17-xo_17), arctan2(yf_18-yo_18, xf_18-xo_18), arctan2(yf_19-yo_19, xf_19-xo_19), arctan2(yf_20-yo_20, xf_20-xo_20) ])



fin_x = array([xf_1, xf_2, xf_3, xf_4, xf_5, xf_6, xf_7, xf_8, xf_9, xf_10, xf_11, xf_12, xf_13, xf_14, xf_15, xf_16, xf_17, xf_18, xf_19, xf_20 ])

fin_y = array([yf_1, yf_2, yf_3, yf_4, yf_5, yf_6, yf_7, yf_8, yf_9, yf_10, yf_11, yf_12, yf_13, yf_14, yf_15, yf_16, yf_17, yf_18, yf_19, yf_20 ])

thetadot_init = zeros(20)



init_vel = ones(20)

init_veldot = ones(20)

x_current = ones((num,count))
y_current = ones((num,count))

xdot_current = zeros((num,count))
ydot_current = zeros((num,count))

xddot_current = zeros((num,count))
yddot_current = zeros((num,count))    

vel_current =  zeros((num,count))
veldot_current =  zeros((num,count))
theta_current = zeros((num,count))
thetadot_current = zeros((num,count))


for i in range(0, 20):
    init_vel[i] = sqrt(init_xdot[i]**2+init_ydot[i]**2)
    init_veldot[i] = sqrt(init_xddot[i]**2+init_yddot[i]**2)
    x_current[i] = fin_x[i]*ones(count)
    x_current[i][0] = init_x[i]
    y_current[i] = fin_y[i]*ones(count)
    y_current[i][0] = init_y[i]
    xdot_current[i][0] = init_xdot[i]
    ydot_current[i][0] = init_ydot[i]
    vel_current[i][0]  = init_vel[i]
    veldot_current[i][0] = init_veldot[i]
    theta_current[i][0] = init_theta[i]
    thetadot_current[i][0] = thetadot_init[i]
    
    

dist1 = sqrt((xf_1-xo_1)**2+(yf_1-yo_1)**2)
dist2 = sqrt((xf_2-xo_2)**2+(yf_2-yo_2)**2)
dist3 = sqrt((xf_3-xo_3)**2+(yf_3-yo_3)**2)
dist4 = sqrt((xf_4-xo_4)**2+(yf_4-yo_4)**2)
dist5 = sqrt((xf_5-xo_5)**2+(yf_5-yo_5)**2)
dist6 = sqrt((xf_6-xo_6)**2+(yf_6-yo_6)**2)
dist7 = sqrt((xf_7-xo_7)**2+(yf_7-yo_7)**2)
dist8 = sqrt((xf_8-xo_8)**2+(yf_8-yo_8)**2)
dist9 = sqrt((xf_9-xo_9)**2+(yf_9-yo_9)**2)
dist10 = sqrt((xf_10-xo_10)**2+(yf_10-yo_10)**2)
dist11 = sqrt((xf_11-xo_11)**2+(yf_11-yo_11)**2)
dist12 = sqrt((xf_12-xo_12)**2+(yf_12-yo_12)**2)
dist13 = sqrt((xf_13-xo_13)**2+(yf_13-yo_13)**2)
dist14 = sqrt((xf_14-xo_14)**2+(yf_14-yo_14)**2)
dist15 = sqrt((xf_15-xo_15)**2+(yf_15-yo_15)**2)
dist16 = sqrt((xf_16-xo_16)**2+(yf_16-yo_16)**2)
dist17 = sqrt((xf_17-xo_17)**2+(yf_17-yo_17)**2)
dist18 = sqrt((xf_18-xo_18)**2+(yf_18-yo_18)**2)
dist19 = sqrt((xf_19-xo_19)**2+(yf_19-yo_19)**2)
dist20 = sqrt((xf_20-xo_20)**2+(yf_20-yo_20)**2)

dist = array([dist1, dist2, dist3, dist4, dist5, dist6, dist7, dist8, dist9, dist10, dist11, dist12, dist13, dist14, dist15, dist16, dist17, dist18, dist19, dist20])


count1 = 1
delt = 0.01
horizon = 1



next_state = zeros((num,5))


#sc_int = random.rand(20)

sc_int = arange(0.5, 4.5, 0.2)

sc_int = sorted(sc_int, reverse = True)

while(count1<= 1000):
   
    if(count1==1):
        inner_iter = 8
    if(count1>1):
        inner_iter = 2
        
    if(count1<=500):
        pert_factor = 0.4*ones(20)
    if(count1>500):
        pert_factor = 0*ones(20)
         
    for i in range(0, 20):
        
      pert_finx, pert_finy = perturbed_finalpos(x_current[i][count1-1], y_current[i][count1-1], fin_x[i], fin_y[i], pert_factor[i] )
      
      x_nex, y_nex, theta_nex, vel_nex, thetadot_nex =  los_command(x_current[i][count1-1], y_current[i][count1-1], pert_finx, pert_finy, vel_current[i][count1-1], theta_current[i][count1-1]) 
      
      next_state[i] = array([x_nex, y_nex, theta_nex, vel_nex, thetadot_nex])      
      
    for k in range(0, inner_iter):  
      for i in range(0,20):
        if(i==0 and count1==1):
         mat1 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==0 and count1>1):
         mat1 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
         
        if(i==1 and count1==1):
         mat2 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==1 and count1>1):
         mat2 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
            
        if(i==2 and count1==1):
         mat3 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==2 and count1>1):
         mat3 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)         
         
        if(i==3 and count1==1):
         mat4  = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==3 and count1>1):
         mat4  = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
         
         
        if(i==4 and count1==1):
         mat5  = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==4 and count1>1):
         mat5 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)         
         
        if(i==5 and count1==1):
         mat6  = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)  
        if(i==5 and count1>1):
         mat6 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)          
         
        if(i==6 and count1==1):
         mat7  = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==6 and count1>1):
         mat7 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)  
         
        if(i==7 and count1==1):
         mat8  = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==7 and count1>1):
         mat8 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)         
         
        if(i==8 and count1==1):
         mat9  = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)    
        if(i== 8 and count1>1):
         mat9 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int) 
         
         
        if(i==9 and count1==1):
         mat10  = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==9 and count1>1):
         mat10 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)         
         
        if(i==10 and count1==1):
         mat11  = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==10 and count1>1):
         mat11 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)          
         
        if(i==11 and count1==1):
         mat12  = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==11 and count1>1):
         mat12 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)   
         
        if(i==12 and count1==1):
         mat13  = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==12 and count1>1):
         mat13 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int) 
         
        if(i==13 and count1==1):
         mat14  = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==16 and count1>1):
         mat14 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int) 
         
        if(i==14 and count1==1):
         mat15 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==14 and count1>1):
         mat15 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int) 
         
         
        if(i==15 and count1==1):
         mat16  = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==15 and count1>1):
         mat16 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)    
        
        if(i==16 and count1==1):
         mat17 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==16 and count1>1):
         mat17 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
         
        if(i==17 and count1==1):
         mat18  = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==17 and count1>1):
         mat18 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
         
        if(i==18 and count1==1):
         mat19 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
        if(i==18 and count1>1):
         mat19 = matrix_comp_iter(next_state, 2.8*rad, i, sc_int)
       
         
       
      mat1 = mat1[~all(mat1==0,axis=1)]
      mat2 = mat2[~all(mat2==0,axis=1)]
      mat3 = mat3[~all(mat3==0,axis=1)]
      mat4 = mat4[~all(mat4==0,axis=1)]
      mat5 = mat5[~all(mat5==0,axis=1)]
      mat6 = mat6[~all(mat6==0,axis=1)]
      mat7 = mat7[~all(mat7==0,axis=1)]
      mat8 = mat8[~all(mat8==0,axis=1)]
      mat9 = mat9[~all(mat9==0,axis=1)]
      mat10 = mat10[~all(mat10==0,axis=1)]
      mat11 = mat11[~all(mat11==0,axis=1)]
      mat12 = mat12[~all(mat12==0,axis=1)]
      mat13 = mat13[~all(mat13==0,axis=1)]
      mat14 = mat14[~all(mat14==0,axis=1)]
      mat15 = mat15[~all(mat15==0,axis=1)]
      mat16 = mat16[~all(mat16==0,axis=1)]
      mat17 = mat17[~all(mat17==0,axis=1)]
      mat18 = mat18[~all(mat18==0,axis=1)]
      mat19 = mat19[~all(mat19==0,axis=1)]
    
      mat_comb = vstack((mat1,mat2,mat3,mat4,mat5,mat6,mat7,mat8,mat9,mat10,mat11,mat12,mat13,mat14,mat15,mat16,mat17,mat18,mat19))
       
      sol = sc_fn_compute3(next_state, mat_comb, Vmax, Vmin, xddotmax, yddotmax)
      q = sol[0:20]
      for j in range(0, 20):
          if(q[j]>0):
           sc_int[j] = q[j]
          if(abs(q[j])<0.0001):
              sc_int[j] = random.rand()


    if(min(q)<0.001):
        kkkkkk
        
    #q = ones(20)
    delt_sc = scaled_int(q, delt)
    
    for i in range(0, 20):
        if(dist[i]>0.1): 
            xt, yt, theta, vel, thetadot = scaled_traj2(x_current[i][count1-1], y_current[i][count1-1], theta_current[i][count1-1], next_state[i][3], next_state[i][4], q[i], delt_sc)
            x_current[i][count1:count1+horizon] = xt
            y_current[i][count1:count1+horizon] = yt
            vel_current[i][count1:count1+horizon] = vel
            theta_current[i][count1:count1+horizon] = theta
            thetadot_current[i][count1:count1+horizon] = thetadot
            dist[i] =  sqrt((fin_x[i]-x_current[i][count1+horizon-1])**2+(fin_y[i]-y_current[i][count1+horizon-1])**2)
        if(dist[i]<=0.1):
            x_current[i][count1:count1+horizon] = x_current[i][count1-1]
            y_current[i][count1:count1+horizon] = y_current[i][count1-1]
            vel_current[i][count1:count1+horizon] = vel_current[i][count1-1]
            theta_current[i][count1:count1+horizon] = theta_current[i][count1-1]
            thetadot_current[i][count1:count1+horizon] = thetadot_current[i][count1-1]
            dist[i] =  sqrt((fin_x[i]-x_current[i][count1+horizon-1])**2+(fin_y[i]-y_current[i][count1+horizon-1])**2)

            
        

        
    
        
    
    count1 = count1+horizon





theta = linspace(0,2*pi,1601)
def makeFig():
    cirx1 = x_1+rad*cos(theta)
    ciry1 = y_1+rad*sin(theta)
    cirx2 = x_2+rad*cos(theta)
    ciry2 = y_2+rad*sin(theta)
    cirx3 = x_3+rad*cos(theta)
    ciry3 = y_3+rad*sin(theta)     
    cirx4 = x_4+rad*cos(theta)
    ciry4 = y_4+rad*sin(theta)
    cirx5 = x_5+rad*cos(theta)
    ciry5 = y_5+rad*sin(theta)
    cirx6 = x_6+rad*cos(theta)
    ciry6 = y_6+rad*sin(theta)
    cirx7 = x_7+rad*cos(theta)
    ciry7 = y_7+rad*sin(theta)
    cirx8 = x_8+rad*cos(theta)
    ciry8 = y_8+rad*sin(theta)
    cirx9 = x_9+rad*cos(theta)
    ciry9 = y_9+rad*sin(theta)
    cirx10 = x_10+rad*cos(theta)
    ciry10 = y_10+rad*sin(theta)
    cirx11 = x_11+rad*cos(theta)
    ciry11 = y_11+rad*sin(theta)
    cirx12 = x_12+rad*cos(theta)
    ciry12 = y_12+rad*sin(theta)
    cirx13 = x_13+rad*cos(theta)
    ciry13 = y_13+rad*sin(theta)
    cirx14 = x_14+rad*cos(theta)
    ciry14 = y_14+rad*sin(theta)
    cirx15 = x_15+rad*cos(theta)
    ciry15 = y_15+rad*sin(theta)
    cirx16 = x_16+rad*cos(theta)
    ciry16 = y_16+rad*sin(theta)
    cirx17 = x_17+rad*cos(theta)
    ciry17 = y_17+rad*sin(theta)
    cirx18 = x_18+rad*cos(theta)
    ciry18 = y_18+rad*sin(theta)
    cirx19 = x_19+rad*cos(theta)
    ciry19 = y_19+rad*sin(theta)
    cirx20 = x_20+rad*cos(theta)
    ciry20 = y_20+rad*sin(theta)
    plt.plot(cirx1,ciry1,'-b',cirx2,ciry2,'-g',cirx3,ciry3,'-r',cirx4,ciry4,'-c',cirx5,ciry5,'-m',cirx6,ciry6,'-y',cirx7,ciry7,'-k',cirx8,ciry8,'-b',cirx9,ciry9,'-g',cirx10,ciry10,'-r',cirx11,ciry11,'-b',cirx12,ciry12,'-b',cirx13,ciry13,'-b',cirx14,ciry14,'-b',cirx15,ciry15,'-b',cirx16,ciry16,'-b',cirx17,ciry17,'-b',cirx18,ciry18,'-b',cirx19,ciry19,'-b',cirx20,ciry20,'-b')
    plt.plot(x_current[0],y_current[0],'-b',x_current[1],y_current[1],'-g',x_current[2],y_current[2],'-r',x_current[3],y_current[3],'-c',x_current[4],y_current[4],'-m',x_current[5],y_current[5],'-y',x_current[6],y_current[6],'-k',x_current[7],y_current[7],'--b',x_current[8],y_current[8],'--g',x_current[9],y_current[9],'--r',x_current[10],y_current[10],'--r',x_current[11],y_current[11],'--r',x_current[12],y_current[12],'--r',x_current[13],y_current[13],'--r',x_current[14],y_current[14],'--r',x_current[15],y_current[15],'--r',x_current[16],y_current[16],'--r',x_current[17],y_current[17],'--r',x_current[18],y_current[18],'--r',x_current[19],y_current[19],'--r')
    plt.axis([-2.7, 2.7, -2.7, 2.7])    


x_1 = []
y_1 = []
x_2 = []
y_2 = []    
x_3 = []
y_3 = []
x_4 = []
y_4 = []
x_5 = []
y_5 = []
x_6 = []
y_6 = []
x_7 = []
y_7 = []
x_8 = []
y_8 = []
x_9 = []
y_9 = []           
x_10 = []
y_10 = []
x_11 = []
y_11 = []
x_12 = []
y_12 = []
x_13 = []
y_13 = []
x_14 = []
y_14 = []
x_15 = []
y_15 = []
x_16 = []
y_16 = []
x_17 = []
y_17 = []
x_18 = []
y_18 = []
x_19 = []
y_19 = []
x_20 = []
y_20 = []


for i in xrange(0, 1000, 10):
        x_1 = x_current[0][i]
        y_1 = y_current[0][i]
        x_2 = x_current[1][i]
        y_2 = y_current[1][i]
        x_3 = x_current[2][i]
        y_3 = y_current[2][i]
        x_4 = x_current[3][i]
        y_4 = y_current[3][i]
        x_5 = x_current[4][i]
        y_5 = y_current[4][i]
        x_6 = x_current[5][i]
        y_6 = y_current[5][i]
        x_7 = x_current[6][i]
        y_7 = y_current[6][i]
        x_8 = x_current[7][i]
        y_8 = y_current[7][i]
        x_9 = x_current[8][i]
        y_9 = y_current[8][i]
        x_10 = x_current[9][i]
        y_10 = y_current[9][i]
        x_11 = x_current[10][i]
        y_11 = y_current[10][i]
        x_12 = x_current[11][i]
        y_12 = y_current[11][i]
        x_13 = x_current[12][i]
        y_13 = y_current[12][i]
        x_14 = x_current[13][i]
        y_14 = y_current[13][i]
        x_15 = x_current[14][i]
        y_15 = y_current[14][i]
        x_16 = x_current[15][i]
        y_16 = y_current[15][i]
        x_17 = x_current[16][i]
        y_17 = y_current[16][i]
        x_18 = x_current[17][i]
        y_18 = y_current[17][i]
        x_19 = x_current[18][i]
        y_19 = y_current[18][i]
        x_20 = x_current[19][i]
        y_20 = y_current[19][i]
        drawnow(makeFig) 
        plt.pause(0.005)





#
#
#
#
#
testx = array([xo_4, xf_4])
testy = array([yo_4, yf_4])
#print shape(x_current[0][0:len(x_current[0])-1])

plt.plot(x_current[17], y_current[17],'.r',x_current[16],y_current[16],'.b',x_current[15], y_current[15],'.k',x_current[14], y_current[14],'.r')
#plt.plot(xdot_current[8])
plt.show()    
    
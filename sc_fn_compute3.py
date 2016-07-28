# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 14:31:27 2016

@author: aks
"""

from numpy import *
from cvxopt import solvers
import cvxopt
import matplotlib.pyplot as plt


num = 20

u = 0.1

smax = zeros((20,1))
smin = zeros((20,1))

xdot = zeros((20,1))
ydot = zeros((20,1))
xddot = zeros((20,1))
yddot = zeros((20,1))


def sc_fn_compute3(next_state, mat_comb, Vmax, Vmin, xddotmax, yddotmax):
    for i in range(0, 20):
       smax[i][0] = Vmax/next_state[i][3]
       smin[i][0] = Vmin/next_state[i][3]
       
       
    
    ident1 = identity(20)
    ident2 = -identity(20)
    pos_con = -identity(20)
    A_comb1 = vstack((mat_comb, ident1, ident2, pos_con))
    B_comb1 = zeros((len(mat_comb),1))
    B_comb =  vstack((B_comb1, smax**2, -smin**2, zeros((20,1))))
    
    A_comb = vstack((A_comb1))
    B_comb = vstack((B_comb))
    obj = -2*ones(num)
    #obj = -2*smax
    obj1 = -ones(num)
    
       
    sol = solvers.qp(cvxopt.matrix(2*identity(20),tc='d'), cvxopt.matrix(obj,tc='d'),cvxopt.matrix(A_comb,tc='d'),cvxopt.matrix(B_comb,tc='d'))
    
    #sol = solvers.lp(cvxopt.matrix(obj1,tc='d'),cvxopt.matrix(A_comb,tc='d'),cvxopt.matrix(B_comb,tc='d'))

    sol1 = sol['x']
    sol2 = zeros(20)
    for i in range(0, 20):
        sol2[i] = sol1[i]
        
    
    sol2 = around(sol2, decimals=4)    
    
    print sol2
    
    return sqrt(sol2)
       
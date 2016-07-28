# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 14:20:23 2016

@author: aks
"""

from numpy import *


def perturbed_finalpos(xo, yo, xf, yf, pert):
    
    r = sqrt((xf-xo)**2+(yf-yo)**2)
    phi = arctan2((yf-yo), (xf-xo))+pert
    pert_finx = xo+r*cos(phi)
    pert_finy = yo+r*sin(phi)
    
    
    
    return pert_finx, pert_finy 
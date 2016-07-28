# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 00:06:44 2016

@author: aks
"""

from numpy import *

def scaled_int(q, delt):
    delt_sc = delt*ones(20)
    for i in range(0, len(q)):
        delt_sc[i] = delt/(q[i])
    
    return min(delt_sc)    
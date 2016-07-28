# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 13:16:56 2016

@author: aks
"""

from numpy import *
from scale_comp_iter import scale_calc_iter

num = 20
count = 100






def matrix_comp_iter(next_state, rad, i, sc_int):
     mat = zeros((100, num))
        
    
    
     counter = 0
         
    
     for j in range(i+1, 20):
        #print counter
        A, B, C = scale_calc_iter(next_state[i][0], next_state[i][1], next_state[i][2], next_state[i][3],  next_state[j][0],  next_state[j][1], next_state[j][2], next_state[j][3], rad)
        #print A, B, C
        if(A>0 and C>0 and B<0):
            
            c1 = (-A-(0.5*B)*(sc_int[j]/sc_int[i]))
            c2 = (-C-(0.5*B)*(sc_int[i]/sc_int[j]))
            
            mat[counter][i] = c1
            mat[counter][j] = c2
            counter = counter+1
            
            
            
            
            
#            c1 = C-A*sc_int[i]**2
#            c2 = 2*A*sc_int[i]+B
#            
#            if(c1>0 and c2>0):
#                 mat[counter][i] = -1
#                 mat[counter][j] = 0.00000001
#            if(c1>0 and c2<0):
#                 mat[counter][i] = 1
#                 mat[counter][j] = -(-c1/c2)**2
#            if(c1<0 and c2<0):
#                mat[counter][i] = 1
#                mat[counter][j] = -10
#            if(c1<0 and c2>0):
#                mat[counter][i] = -1
#                mat[counter][j] = (-c1/c2)**2
#                
#            counter = counter+1
#            
           
        if(A>0 and C>0 and B>0):
            mat[counter][i] = 1
            mat[counter][j] = -1000
           
            counter = counter+1
           
            
            
           
        
        if(A<0 and C>0):
            root1 = (-B+sqrt(B**2 - 4*A*C))/(2*A)

            root2 = (-B-sqrt(B**2 - 4*A*C))/(2*A)
            
            scalemax = max(root1,root2)
            scalemin = min(root1,root2)
            
            if(scalemin>0):
               mat[counter][i] = 1
               mat[counter][j] = -(scalemax**2) 
               mat[counter+num][i] = -1
               mat[counter+num][j] = scalemin**2
               
               counter = counter+1
               
            if(scalemin<0):
               mat[counter][i] = 1
               mat[counter][j] = -(scalemax**2)
               
               counter = counter+1
               
                
        if(A>0 and C<0):
            root1 = (-B+sqrt(B**2 - 4*A*C))/(2*C)

            root2 = (-B-sqrt(B**2 - 4*A*C))/(2*C)
            
            scalemax = max(root1,root2)
            scalemin = min(root1,root2)
            
            if(scalemin>0):
               mat[counter][i] = -(scalemax**2)
               mat[counter][j] = 1 
               mat[counter+num][i] = scalemin**2
               mat[counter+num][j] = -1
               
               counter = counter+1
               
            if(scalemin<0):
               mat[counter][i] = -(scalemax**2)
               mat[counter][j] = 1
               
               counter = counter+1   
                        
            
            
                
        
        
        
        
     return mat               
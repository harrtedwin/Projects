# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 01:20:31 2022

@author: Phoenix
"""

for row in range(5):
    if row % 2 == 0:
        for  column in range(1,6):
            if column % 2 == 1:
                if column % 2 != 5:
                    print(" ", end="")
                else:
                    print(" ")
            else: 
                print("|",end="")
        #print(" | | ")
    else:
        print("-----")
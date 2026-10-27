# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:31:18 2026

@author: acer
"""


widgets = int(input("How many widgets?:"))

if widgets >= 100:
    cost = widgets * 0.20   
else:
    cost = widgets * 0.25   

print(cost)


# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:02:51 2026

@author: acer
"""

basic = float(input("Enter Basic Salary: "))

hra = 0.20 * basic   
ta  = 0.05 * basic   
da  = 0.10 * basic   

gross = basic + hra + ta + da

print("Gross Salary =", gross)

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:13:14 2026

@author: acer
"""

basic = float(input("Enter Basic Salary: "))

hra = 0.20 * basic
ta  = 0.05 * basic
da  = 0.10 * basic

gross = basic + hra + ta + da
print("Gross Salary =", gross)

if gross < 300000:
    print("Tax Slab: 0% (No Tax)")
elif gross <= 1000000:
    print("Tax Slab: 10%")
elif gross <= 2500000:
    print("Tax Slab: 20%")
else:
    print("Tax Slab: 30%")

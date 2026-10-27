# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:44:25 2026

@author: acer
"""

Price = 2.50

pounds = float(input("Enter the number of pounds of apples: "))
cash = float(input("Enter the amount of cash tendered: "))

total_cost = pounds * Price

if cash >= total_cost:
    change = cash - total_cost
    print("your change is $",change)
else:
    owed = total_cost - cash
    print("you owe $",owed)

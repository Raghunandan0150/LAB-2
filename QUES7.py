# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:35:06 2026

@author: acer
"""

Color=input("Enter Color:")
Mode=input("Enter mode:")
if Color == "red" and Mode == "flashing" :
    print("Snow veiw")
elif Color == "red" and Mode == "steady" :
    print("Rain veiw")
elif Color == "blue" and Mode == "flashing" :
    print("Clouds")
elif Color == "blue" and Mode == "steady" :
    print("Clear veiw")
else:
    print("Recheck the color and mode")
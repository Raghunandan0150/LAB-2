# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:31:21 2026

@author: Lenovo
"""

weight=float(input("enter weight (kg) : "))
height=float(input("enter height (m) : "))

BMI= weight/(height**2)
if BMI >= 35 :
    print("Clinically Obese")
elif BMI >= 30 :
    print("Obese")
elif BMI >= 25 :
    print("Slightly Overweight")
elif BMI >= 18.5 : 
    print("Normal Weight")
else:
    print("Underweight")
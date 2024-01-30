# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 09:05:22 2024

@author: lenovo
"""

import pandas

file=pandas.read_csv("country_data.CSV")
print (file)

print(file.info())

print(file.describe())



file1=pandas.read_csv("iris_data.CSV")
print (file1)

print(file1.info())

print(file1.describe())




file2=pandas.read_csv("diab_data.CSV")
print (file2)

print(file2.info())

print(file2.describe())




columnnames=["A","B", "C","D"]

file3=pandas.read_csv("housing_data.CSV", names=columnnames)
print (file3)

print(file3.info())

print(file3.describe())

         
file4=pandas.read_csv("insurance_data.CSV")
print (file4)

print(file4.info())

print(file4.describe())

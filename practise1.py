# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:40:36 2024

@author: lenovo
"""
inserting/labelling of columns"""
import pandas


columnnames=["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]
file3=pandas.read_csv("housing_data.CSV",names=columnnames)
print (file3)



print(file3.info())
"""print(file3.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 506 entries, 0 to 505
Data columns (total 14 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   A       506 non-null    float64
 1   B       506 non-null    float64
 2   C       506 non-null    float64
 3   D       506 non-null    float64
 4   E       506 non-null    float64
 5   F       506 non-null    float64
 6   G       506 non-null    float64
 7   H       506 non-null    float64
 8   I       506 non-null    int64  
 9   J       506 non-null    float64
 10  K       506 non-null    float64
 11  L       506 non-null    float64
 12  M       506 non-null    float64
 13  N       452 non-null    float64
dtypes: float64(13), int64(1)
memory usage: 55.5 KB
None"""
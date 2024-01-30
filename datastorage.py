# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:40 2024

@author: Akinshola

Storin data: Using List variables"""



import pandas

file=pandas.read_csv("country_data.CSV")

print(file)
 
"""
Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

#Using list

age=[39,25,29,46,22,35,22,49,30,40,30]

print (age)


"""
[39, 25, 29, 46, 22, 35, 22, 49, 30, 40, 30]
"""


age.append(100)

print(age)




#Gender Listing of text

gender=["M","M","F","M","F","F","F","M","M","F","M"]

print(gender[0])

print(gender[6])

print(gender[-1])




mylist = [42, -2021, 6.283,"tau", "node"]

print(mylist)

mylist.append("pi")

print(mylist)

mylist.insert(0,"pi2")

print(mylist)


mylist.remove("tau")

print(mylist)

print(mylist[:1])

person={'name':'Akinshola A','age':38,'address':'40 Ararat Westdene','Phone number':'0635111078'}

print(person['name'])


print(person['address'])




#Creating data frame

import pandas as pd

data= {
'age':[30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],

'gender':["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],

'country':["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}


#df=data frame

df=pd.DataFrame(data)
 
#Displaying the data frame

print(df)


print(df[1:4])

print(df['age'].min())

print(df['age'].sum())

print(df['gender'])

df['new_column']=[1,2,3,4,5,6,7,8,9,10,11]

print(df)

df.drop(columns=['new_column'], inplace=True)

print(df)



df['new_row']=[1,2,3,4,5,6,7,8,9,10,11]

print(df)

#fintering data

print(df['age']>30)


















# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qbHQn9sNz4vG8tMBi7_JW0IOlFzGi-mY
"""

import numpy as np
arry=[]
array=[]
m=int (input("Rows :"))
n=int (input("Columns :"))
x=m*n
print ("Array 1st : ")
for i in range(x):
    arry+=[int(input(""))]
NewArray = np.asarray(arry)
print ("Array 2nd :")
for j in range(x):
    array+=[int(input(""))]
NewArray2 = np.asarray(array)
NewArray = np.asarray(arry)
NewArryNumpy = NewArray2.reshape(int(m),n)
print(NewArryNumpy)
NewArrayNumpy = NewArray.reshape(int(n),m)
print(NewArrayNumpy)
Results=np.add(NewArrayNumpy,NewArryNumpy)
print(Results)
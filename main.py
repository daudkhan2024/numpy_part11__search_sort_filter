#search an array foro a cetian valu,
# #nd return th indexes that get match
print("Search" )
import numpy as np
var = np.array([1,2,3,4,4,2,3,46,8])
#first we will mame a variable
x =  np.where(var == 2)
print(x)

print()
x =  np.where(var %2 == 0)
print(x)

print()
print("Search Sort Array")
#binary search
var1 = np.array([1,2,3,4,6,7,8])
#first we will mame a variable
x1 =  np.searchsorted(var1 , 5)
print(x1)
#left to right
print()

print("from right side")
var12= np.array([1,2,3,4,6,7,8,9,10])
#first we will mame a variable
x2 =  np.searchsorted(var12 ,[5,6,7],side="right")
print(x2)

print()
print("sort Array")
#acending or decending order
var_2= np.array([1,2,3,4,6,7,8,9,10])
print(np.sort(var_2))


# for alphabet
var_4 = np.array(["a","khan","ahmad","banana"])
print(np.sort(var_4))

print()
print("2D array")
c1 = np.array([[1,2,3],[3,4,5],[3,4,5]])
print("array numbers   :",c1.ndim)
print("order might not same of elements :",np.sort(c1))

print()
print("FiLTR ARRAY")
#getting some elements out of an existing array and creat
#new array out of them
var_5 = np.array(["a","khan","ahmad","banana"])
f = [True,False,True,True]
new_a = var_5[f]
print(new_a)
print(type(new_a))
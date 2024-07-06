# This file is created to practice  tuple list datatype concept
# Created by suketh :  on 05/07/2024

tu = (1,2.0,True,1+2j,"etl",[1,2]) #we are able to store the heterogenous datatype (different data types)
print("value of tu is", tu)
print("type of tu is", type(tu))
print("memory  tu ls is", id(tu))

print("first element of tuple is ", tu[0], type(tu[0]), id(tu[0]))
print("second element of list is ", tu[1], type(tu[1]), id(tu[1]))
print("third element of list is ", tu[2], type(tu[2]), id(tu[2]))
print("fourth element of list is ", tu[3], type(tu[3]), id(tu[3]))
print("fifth element of list is ", tu[4], type(tu[4]), id(tu[4]))
print("sixth element", tu[5], type(tu[5]), id(tu[5]))
print("[1:3] element", tu[1:3], type(tu[1:3]), id(tu[1:3]))
#
tu = (1,2,3,4,5)
print("value of tu is", tu)
print("type of tu is", type(tu))
print("memory of tu is", id(tu))

print("methods availble in list",  dir(tu))

tu2 = tuple() #empty list
#tu2 = () #empty list
print("value of tu2 is", tu2)
print("type of tu2 is", type(tu2))
print("memory  tu2 ls is", id(tu2))
#
# count and index

t2 =(1,1,1,1,2,2,2,3,3,3,3,3,4,4,4,4)
print("count  of 2 is", t2.count(2))


t2 =(1,1,1,1,2,2,2,3,3,3,3,3,4,4,4,4)
print("index  of 2 is", t2.index(2))

#tupple has no attribute eror we will get  if use append pop or anyother command from list
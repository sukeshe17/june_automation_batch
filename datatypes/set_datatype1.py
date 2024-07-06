# This file is created to practice  set  datatype concept
# Created by suketh :  on 05/07/2024

s = {1,2.0,True,1+2j,"etl"}  #we are able to store the heterogenous datatype (different data types)
print("value of set is", s)
print("type of set is", type(s))
print("memory  set ls is", id(s))

s1 = {1,2,3,4,5}
print("value of set is", s1)
print("type of set is", type(s1))
print("memory of set is", id(s1))

print("methods availble in set",  dir(s1))

#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

s3 ={1,1,1,1,2,2,2,3,3,3,3,3,4,4,4,4}
s3 = set(s3)
print(s3)

s4 = set() #empty set
#s4 = {}# it will create dict
print("value of s4 is", type(s4))

s1 = {1,2,3,4}
s2 = {3,4,5}

print("s1.intersection(s2)", s1.intersection(s2))
print("s1.difference(s2)", s1.difference(s2))

s1.add(8)
print("after add of 8",s1)

fs =frozenset(s1)
print("value of frozenset is", fs)
print("type of frozenset is", type(fs))
print("memory of frozenset is", id(fs))

print("methods availble in frozenset",  dir(fs))
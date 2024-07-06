# This file is created to practice  dictionary datatype concept
# Created by suketh :  on 05/07/2024

d = {}
print("type of d is", type(d))
d1 = {1}
print("type of d is", type(d1))

#syntax variable_name ={key1:value1 ,key2:value2,key3:value}
d2 = {1:'Sreeni' ,2:"Hari",3:"ram"}
print("value of d2 is", d2)
print("type of d2 is", type(d2))
print("memory  d2  is", id(d2))

print("methods availble in dict",  dir(d2))

#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

#adding and update

d2[4] = 'janav'
print("value of d2 after adding d4", d2)

d2[1] = 'seenivas'
print("value of d2 after update  d1", d2)

d2.update({5:"somu",2:"Hari Kishore",6:"ram"})
print("value of d2 after update method ", d2)

print("keys in d2",d2.keys())
# print("type  of keys in d2.keys()",type (d2.keys()))
# print("values in d2",d2.values())
# print("type  of keys in d2.values()",type (d2.values()))
# print("items in d2",d2.items())
# print("type  of keys in d2.items()",type (d2.items()))

# d2.pop(5)
# print("value of d2 after pop method ", d2)
# print("values in d2",d2[2])
#
# d2.popitem()
# print("value of d2 after popitem method ", d2)
#
# d2.popitem()
# print("value of d2 after popitem method ", d2)

# to access the elements
print("values in d2",d2[2])
print("get method ", d2.get((2)))


#help
print(help(d2.pop))

#print(pd.DataFrame(d2))
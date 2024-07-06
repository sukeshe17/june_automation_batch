# This file is created to practice  list datatype concept
# Created by suketh :  on 05/07/2024

# ls = [1,2.0,True,1+2j,"etl",[1,2]] #we are able to store the heterogenous datatype (different data types)
# print("value of ls is", ls)
# print("type of ls is", type(ls))
# print("memory  of ls is", id(ls))
#
# print("first element of list is ", ls[0], type(ls[0]), id(ls[0]))
# print("second element of list is ", ls[1], type(ls[1]), id(ls[1]))
# print("third element of list is ", ls[2], type(ls[2]), id(ls[2]))
# print("fourth element of list is ", ls[3], type(ls[3]), id(ls[3]))
# print("fifth element of list is ", ls[4], type(ls[4]), id(ls[4]))
# print("sixth element", ls[5], type(ls[5]), id(ls[5]))
#
# ls = [1,2,3,4,5]
# print("value of ls is", ls)
# print("type of ls is", type(ls))
# print("memory  of ls is", id(ls))
#
# print("methods availble in list",  dir(ls))

ls2 = list() #empty list
#ls2 = [] #empty list
print("value of ls is", ls2)
print("type of ls is", type(ls2))
print("memory  of ls is", id(ls2))

#append , insert , extend

#append

print("value of ls Before append is", ls2)
ls2.append(1)
print("value of ls after append is", ls2)
ls2.append(2)
print("value of ls after append is", ls2)
ls2.append(True)
print("value of ls after append is", ls2)
ls2.append("ETL")
print("value of ls after append is", ls2)
ls2.append([1,2,3])
print("value of ls after append is", ls2)

#extend  #it takes iterative data as I/P so we can pass list ,tuple ,dict,set ,fs,string
ls2.extend("ETL")
print("value of ls after extend is", ls2)
ls2.extend([1,2,3])
print("value of ls after extend is", ls2)

#insert

ls2.insert(2,"AUTOMATION")
print("value of ls after insert is", ls2)

ls2[0]=25
print("value of ls after update is", ls2)




# clear ,pop , remove

#pop
# to remove the element from specified index value if index is not paased the last element will be removed

ls2.pop()
print("value of ls after pop is", ls2)

ls2.pop(0)
print("value of ls after pop is", ls2)

#remove
ls2.remove("ETL")    # remove will be used to removed the data  pass the direct value insted of index
print("value of ls after remove is", ls2)

#clear
# ls2.clear()
# print("value of ls after clear is", ls2)

ls3 = [1,2,2,2,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,5]
print("count of 5", ls3.count(5))
#print("count of ls3", ls3.count())  #ask  question is there any way to count number items in the list
print("count of ls3", len(ls3))


ls3.reverse()
print("value of ls after reverse is", ls3)

ls3.sort(reverse=False)
print("value of ls after sort is", ls3)

unique_elements_s_ls3 = set(ls3)
print("unique elemets are in ls3 ", unique_elements_s_ls3)